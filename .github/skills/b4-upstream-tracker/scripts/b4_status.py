#!/usr/bin/env python3
"""Collecte l'état d'une branche b4 (b4 prep) et son suivi Patchwork.

Usage: b4_status.py [--repo PATH] [--branch b4/xxx] [--offline]

La branche doit être celle actuellement checkoutée dans le repo (limite de
`b4 prep --show-info`). Sortie en texte clé: valeur, facile à reporter dans la fiche.
"""
import argparse
import json
import os
import re
import subprocess
import sys
import urllib.error
import urllib.parse
import urllib.request

PW_API = "https://patchwork.kernel.org/api/1.2"
DEFAULT_REPO = os.path.expanduser("~/Views/upstream_mp21/linux-next")


def run(cmd, cwd, check=False):
    res = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True)
    if check and res.returncode:
        sys.exit(f"ERREUR: {' '.join(cmd)}\n{res.stderr.strip()}")
    return res.stdout.strip() if res.returncode == 0 else ""


def pw_get(path, **params):
    url = f"{PW_API}/{path}"
    if params:
        url += "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers={"User-Agent": "b4-upstream-tracker"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.load(resp)


def parse_show_info(text):
    info, series = {}, {}
    for line in text.splitlines():
        key, _, val = line.partition(": ")
        m = re.fullmatch(r"series-v(\d+)", key)
        if m:
            rng, _, msgid = val.partition(" ")
            series[int(m.group(1))] = (rng, msgid.strip())
        else:
            info[key] = val
    return info, series


def patchwork_status(version, msgid):
    """Retourne les lignes de statut Patchwork pour un msgid de cover (ou de patch 1)."""
    out = []
    entries = pw_get("covers/", msgid=msgid)
    kind = "cover"
    if not entries:
        entries, kind = pw_get("patches/", msgid=msgid), "patch"
    if not entries:
        return [f"v{version}: introuvable sur Patchwork (pas encore indexé ou msgid {msgid})"]
    for entry in entries:
        project = entry["project"]["link_name"]
        out.append(f"v{version} [{project}] {entry['web_url']}")
        out.append(f"  lore: {entry['list_archive_url']}  date: {entry['date']}")
        if kind == "patch":
            patches = [entry]
        else:
            series = pw_get(f"series/{entry['series'][0]['id']}/")
            out.append(f"  series: {series['web_url']}  ({series['received_total']}/{series['total']} reçus)")
            patches = [pw_get(f"patches/{p['id']}/") for p in series["patches"]]
        for p in patches:
            tags = ", ".join(f"{k}:{v}" for k, v in p.get("tags", {}).items()) or "-"
            out.append(f"  - {p['name']} | state={p['state']} | checks={p['check']} | tags={tags}")
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--repo", default=DEFAULT_REPO)
    ap.add_argument("--branch", help="vérifie que cette branche est bien checkoutée")
    ap.add_argument("--offline", action="store_true", help="ne pas interroger Patchwork")
    args = ap.parse_args()

    repo = os.path.expanduser(args.repo)
    current = run(["git", "branch", "--show-current"], repo, check=True)
    if args.branch and args.branch != current:
        sys.exit(f"ERREUR: branche courante '{current}' != '{args.branch}' (git checkout d'abord)")

    info, series = parse_show_info(run(["b4", "-n", "--offline-mode", "prep", "--show-info"], repo, check=True))
    base = info.get("base-commit", "")
    start, end = info.get("start-commit", ""), info.get("end-commit", "")

    sent = max(series) if series else 0
    revision = int(info.get("revision", sent + 1))
    status = "DRAFT" if not sent else f"V{sent} SENT"

    print("== BRANCH ==")
    print(f"branch: {current}")
    print(f"repo: {repo}")
    print(f"base-commit: {base[:12]} ({run(['git', 'describe', '--tags', '--always', base], repo)})")
    print(f"change-id: {info.get('change-id', '')}")
    print(f"cover-subject: {info.get('cover-subject', '')}")
    print(f"cover-strategy: {info.get('cover-strategy', '')}")
    print(f"needs-editing: {info.get('needs-editing', '')}")
    print(f"current-revision: v{revision}")
    print(f"last-sent-version: {'v%d' % sent if sent else 'none'}")
    print(f"suggested-status: {status}" + (f" (v{revision} en préparation)" if sent and revision > sent else ""))

    print("\n== PATCHES (ordre d'application) ==")
    if start and end:
        log = run(["git", "log", "--reverse", "--format=%h %s", f"{start}^..{end}"], repo)
        has_cover = info.get("cover-strategy") == "commit"
        for i, line in enumerate(log.splitlines()):
            print(f"{i}{' (cover)' if has_cover and i == 0 else ''}: {line}")

    print("\n== SENT VERSIONS ==")
    for v in sorted(series):
        rng, msgid = series[v]
        print(f"v{v}: range={rng} msgid=<{msgid}> lore=https://lore.kernel.org/r/{msgid}")

    print("\n== MAINTAINERS / LISTES / TREES ==")
    files = run(["git", "diff", "--name-only", f"{base}..{end}"], repo).split() if base and end else []
    if files and os.path.exists(os.path.join(repo, "scripts/get_maintainer.pl")):
        print(run(["scripts/get_maintainer.pl", "--nogit", "--nogit-fallback", "--scm", "--no-rolestats", "-f", *files], repo))

    print("\n== PATCHWORK ==")
    if args.offline:
        print("(offline)")
    for v in sorted(series):
        if args.offline:
            break
        try:
            print("\n".join(patchwork_status(v, series[v][1])))
        except (urllib.error.URLError, TimeoutError) as err:
            print(f"v{v}: Patchwork injoignable ({err})")


if __name__ == "__main__":
    main()
