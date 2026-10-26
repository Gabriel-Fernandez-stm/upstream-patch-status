#!/usr/bin/env python3
"""Génère UPSTREAM.md : tableau de bord des séries b4 groupées par SoC STM32MP.

Sources :
  - branches b4/* du repo kernel (suivi b4 lu dans le commit de cover, sans checkout)
  - fiches <série>.md du workspace (STATUS, SOC, COMMENTS, TODO)
  - Patchwork (états, checks, tags, nombre de commentaires de la dernière version envoyée)

Usage: b4_dashboard.py [--repo PATH] [--workspace DIR] [--output FILE] [--offline] [--stdout]
"""
import argparse
import json
import os
import re
import subprocess
import sys
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from b4_status import DEFAULT_REPO, pw_get  # noqa: E402

DEFAULT_WORKSPACE = os.path.expanduser("~/Workspace/Upstream-Stuff")
DEFAULT_EXCLUDE = r"_(old|backup|back_v\d+|v\d+)$"
IGNORED_STATES = {"handled-elsewhere", "not-applicable"}
SOCS = {
    "COMMON": "STM32MP (commun)",
    "MP13": "STM32MP13",
    "MP15": "STM32MP15",
    "MP21": "STM32MP21",
    "MP25": "STM32MP25",
}
TRACKING_RE = re.compile(r"--- b4-submit-tracking ---\n(?:#.*\n)?(\{.*?\n\})", re.S)
TRAILER_RE = re.compile(r"^(Reviewed|Acked|Tested|Reported|Suggested)-by:", re.M)
CHECK_RANK = {"success": 0, "pending": 1, "warning": 2, "fail": 3}
CHECK_ICON = {"success": "✅", "pending": "⏳", "warning": "⚠️", "fail": "❌"}
STATUS_ICON = (
    ("ABANDONED", "⛔"),
    ("MERGED", "🟢"),
    ("APPLIED", "🟢"),
    ("ACKED", "✅"),
    ("REVIEWED", "💬"),
    ("SENT", "📤"),
    ("DRAFT", "📝"),
)


def git(repo, *args):
    res = subprocess.run(["git", "-C", repo, *args], capture_output=True, text=True)
    return res.stdout.strip() if res.returncode == 0 else ""


def read_series(repo, branch):
    """Lit le suivi b4 (revision, versions envoyées) depuis le commit de cover ou la description de branche."""
    cover = git(repo, "log", "-n1", "--format=%H", "--grep=^--- b4-submit-tracking ---", branch)
    text = git(repo, "show", "-s", "--format=%B", cover) if cover else git(repo, "config", "--get", f"branch.{branch}.description")
    match = TRACKING_RE.search(text)
    if not match:
        return None
    series = json.loads(match.group(1))["series"]
    sent = {int(v.lstrip("v")): ids for v, ids in series.get("history", {}).items()}
    title = re.sub(r"^(Subject:\s*)?(\[[^\]]*\]\s*)?", "", text.splitlines()[0])
    return {"title": title, "revision": series.get("revision", 1), "sent": sent}


def read_fiche(path):
    if not os.path.exists(path):
        return None
    with open(path, encoding="utf-8") as fh:
        text = fh.read()

    def section(name):
        m = re.search(rf"^## {name}\s*\n(.*?)(?=^## |\Z)", text, re.S | re.M)
        return m.group(1) if m else ""

    status = re.search(r"\*\*STATUS\s*:\s*`([^`]+)`", text)
    soc = re.search(r"\*\*SOC\s*:\s*([^*]+?)\s*\*\*", text)
    comments = [line[2:].strip() for line in section("COMMENTS").splitlines() if line.startswith("- ")]
    return {
        "status": status.group(1).strip().upper() if status else "",
        "soc": soc.group(1) if soc else "",
        "last_comment": comments[0] if comments else "",
        "todo_open": len(re.findall(r"^- \[ \](?!\s*\(à compléter\))", section("TODO"), re.M)),
    }


def soc_of(name, fiche):
    """SoC explicite dans la fiche (**SOC : ...**), sinon déduit du nom ups_mpNN_*, sinon commun."""
    raw = (fiche or {}).get("soc", "")
    if raw:
        m = re.search(r"mp(\d+)", raw, re.I)
        return f"MP{m.group(1)}" if m else "COMMON"
    m = re.match(r"ups_(mp\d+)_", name)
    return m.group(1).upper() if m else "COMMON"


def pw_collect(msgid):
    """Résume l'état Patchwork d'une version envoyée (msgid de la cover, ou du patch pour une série sans cover)."""
    entries = []
    for obj in pw_get("covers/", msgid=msgid) or pw_get("patches/", msgid=msgid):
        serie = obj["series"][0] if obj["series"] else None
        patches = pw_get("patches/", series=serie["id"], per_page=100) if serie else [obj]
        is_cover = "/covers/" in obj["url"]
        entries.append({
            "project": obj["project"]["link_name"],
            "url": serie["web_url"] if serie else obj["web_url"],
            "cover": obj["id"] if is_cover else None,
            "patches": patches,
        })
    if not entries:
        return None

    primary = max(entries, key=lambda e: sum(p["state"] not in IGNORED_STATES for p in e["patches"]))
    ordered = [primary] + [e for e in entries if e is not primary]
    by_name = {}
    for entry in ordered:
        for patch in entry["patches"]:
            by_name.setdefault(patch["name"], []).append(patch)

    # Patchwork ne convertit pas toujours les trailers des réponses en tags : on les lit dans les commentaires.
    n_comments, trailers = 0, {}
    for patch in primary["patches"]:
        replies = pw_get(f"patches/{patch['id']}/comments/")
        n_comments += len(replies)
        trailers[patch["id"]] = Counter(f"{m}-by" for r in replies for m in TRAILER_RE.findall(r["content"]))
    if primary["cover"]:
        n_comments += len(pw_get(f"covers/{primary['cover']}/comments/"))

    states, tags, check = Counter(), Counter(), ""
    for candidates in by_name.values():
        best = next((p for p in candidates if p["state"] not in IGNORED_STATES), candidates[0])
        states[best["state"]] += 1
        patch_tags = Counter({t: v if isinstance(v, int) else 1 for t, v in (best.get("tags") or {}).items()})
        tags.update(patch_tags | trailers.get(best["id"], Counter()))
        if CHECK_RANK.get(best.get("check"), -1) > CHECK_RANK.get(check, -1):
            check = best["check"]

    return {"url": primary["url"], "states": states, "tags": tags, "check": check, "comments": n_comments}


def pw_safe(msgid):
    try:
        return pw_collect(msgid)
    except Exception as err:  # réseau, JSON, schéma : ne doit pas casser le dashboard
        return f"⚠ Patchwork injoignable ({type(err).__name__})"


def fmt_pw(pw, sent):
    if not sent:
        return "—"
    if pw is None:
        return "non indexé"
    if isinstance(pw, str):
        return pw
    out = f"[{', '.join(f'{n}×{s}' for s, n in pw['states'].most_common())}]({pw['url']})"
    if pw["check"]:
        out += f" {CHECK_ICON.get(pw['check'], '')}"
    if pw["tags"]:
        out += " · " + ", ".join(f"{t}×{n}" for t, n in pw["tags"].items())
    if pw["comments"]:
        out += f" · 💬 {pw['comments']}"
    return out


def status_icon(status):
    return next((icon for key, icon in STATUS_ICON if key in status), "❔")


def status_category(status):
    if "ABANDONED" in status:
        return None
    if "MERGED" in status or "APPLIED" in status:
        return "done"
    if "REVIEWED" in status or "ACKED" in status:
        return "review"
    return "sent" if "SENT" in status else "draft"


def cell(text, limit=0):
    text = text.replace("|", "\\|")
    return text if not limit or len(text) <= limit else text[: limit - 1] + "…"


def build_rows(repo, workspace, exclude, offline):
    branches = git(repo, "branch", "--list", "b4/*", "--format=%(refname:short)").split()
    kept = [b for b in branches if not re.search(exclude, b)]
    rows = []
    for branch in kept:
        name = branch.removeprefix("b4/")
        fiche = read_fiche(os.path.join(workspace, f"{name}.md"))
        series = read_series(repo, branch)
        sent = max(series["sent"]) if series and series["sent"] else 0
        git_status = f"V{sent} SENT" if sent else "DRAFT"
        status = (fiche or {}).get("status") or git_status
        m = re.match(r"V(\d+)", status)
        fiche_ver = int(m.group(1)) if m else (0 if status.startswith("DRAFT") else None)
        rows.append({
            "name": name,
            "branch": branch,
            "fiche": fiche,
            "series": series,
            "sent": sent,
            "status": status,
            "git_status": git_status,
            "stale": bool(fiche and fiche_ver is not None and fiche_ver < sent),
            "soc": soc_of(name, fiche),
            "pw": None,
        })
    if not offline:
        todo = [r for r in rows if r["sent"]]
        with ThreadPoolExecutor(max_workers=4) as pool:
            for row, pw in zip(todo, pool.map(lambda r: pw_safe(r["series"]["sent"][r["sent"]][0]), todo)):
                row["pw"] = pw
    return rows, [b for b in branches if b not in kept]


def version_label(row):
    series = row["series"]
    if not series:
        return "?"
    if not row["sent"]:
        return f"v{series['revision']} (draft)"
    label = f"v{row['sent']} envoyée"
    return label + (f" · v{series['revision']} en cours" if series["revision"] > row["sent"] else "")


def render_row(row, out_dir, workspace, offline):
    fiche = row["fiche"]
    link = os.path.relpath(os.path.join(workspace, f"{row['name']}.md"), out_dir)
    name = f"[{row['name']}](./{link})" if fiche else f"{row['name']} ⚠ fiche manquante"
    status = f"{status_icon(row['status'])} {row['status']}"
    if row["stale"]:
        status += f" ⚠ git : {row['git_status']}"
    pw = "(offline)" if offline and row["sent"] else fmt_pw(row["pw"], row["sent"])
    title = row["series"]["title"] if row["series"] else "⚠ pas de suivi b4"
    last = re.sub(r"\s*\(?https?://\S+?\)?\s*$", "", fiche["last_comment"]) if fiche else ""
    last = cell(last, 90) if last else "—"
    todo = str(fiche["todo_open"]) if fiche else "—"
    return f"| {name} | {cell(title)} | {version_label(row)} | {status} | {pw} | {last} | {todo} |"


def attention_items(rows):
    items = []
    for r in rows:
        if not r["fiche"]:
            items.append(f"- ⚠ **{r['name']}** : fiche manquante → `/b4-upstream-tracker create {r['branch']}`")
        if r["stale"]:
            items.append(f"- ⚠ **{r['name']}** : la fiche indique `{r['status']}` mais git indique `{r['git_status']}` → refresh")
        if not r["series"]:
            items.append(f"- ⚠ **{r['name']}** : aucun suivi b4 trouvé sur la branche")
        pw = r["pw"]
        if isinstance(pw, dict):
            bad = [s for s in pw["states"] if s in ("changes-requested", "rejected")]
            if bad:
                items.append(f"- 🔧 **{r['name']}** : Patchwork `{', '.join(bad)}` → préparer la révision suivante")
    return items


def render(rows, ignored, args):
    out_dir = os.path.dirname(os.path.abspath(args.output))
    groups = {}
    for r in rows:
        groups.setdefault(r["soc"], []).append(r)
    order = list(SOCS) + sorted(k for k in groups if k not in SOCS)

    lines = [
        "# UPSTREAM — suivi des séries kernel STM32MP",
        "",
        f"_Généré le {datetime.now():%Y-%m-%d %H:%M} par le skill `b4-upstream-tracker` — ne pas éditer à la main : "
        "`python3 .github/skills/b4-upstream-tracker/scripts/b4_dashboard.py`. "
        "STATUS, COMMENTS et TODO viennent des fiches ; versions envoyées et Patchwork viennent de b4 et Patchwork._",
        "",
        "## Vue d'ensemble",
        "",
        "| SoC | 📝 DRAFT | 📤 SENT | 💬 REVIEWED / ACKED | 🟢 APPLIED / MERGED | Total |",
        "|---|---|---|---|---|---|",
    ]
    for key in order:
        if key not in SOCS and key not in groups:
            continue
        cats = Counter(status_category(r["status"]) for r in groups.get(key, []))
        lines.append(f"| {SOCS.get(key, 'STM32' + key)} | {cats['draft']} | {cats['sent']} | {cats['review']} | {cats['done']} | {len(groups.get(key, []))} |")

    attention = attention_items(rows)
    if attention:
        lines += ["", "## À traiter", "", *attention]

    for key in order:
        if key not in SOCS and key not in groups:
            continue
        lines += ["", f"## {SOCS.get(key, 'STM32' + key)}", ""]
        if key not in groups:
            lines.append("_Aucune série._")
            continue
        lines += [
            "| Série | Titre (cover) | Version | STATUS | Patchwork (dernière version envoyée) | Dernier commentaire | TODO |",
            "|---|---|---|---|---|---|---|",
        ]
        lines += [render_row(r, out_dir, args.workspace, args.offline) for r in sorted(groups[key], key=lambda r: r["name"])]

    if ignored:
        lines += ["", f"_Branches ignorées (backup/old) : {', '.join(b.removeprefix('b4/') for b in ignored)}._"]
    return "\n".join(lines) + "\n"


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--repo", default=DEFAULT_REPO)
    ap.add_argument("--workspace", default=DEFAULT_WORKSPACE, help="dossier des fiches")
    ap.add_argument("--output", help="défaut: <workspace>/UPSTREAM.md")
    ap.add_argument("--exclude", default=DEFAULT_EXCLUDE, help="regex des branches à ignorer")
    ap.add_argument("--offline", action="store_true", help="ne pas interroger Patchwork")
    ap.add_argument("--stdout", action="store_true", help="afficher au lieu d'écrire le fichier")
    args = ap.parse_args()
    args.repo = os.path.expanduser(args.repo)
    args.workspace = os.path.expanduser(args.workspace)
    args.output = os.path.expanduser(args.output or os.path.join(args.workspace, "UPSTREAM.md"))

    rows, ignored = build_rows(args.repo, args.workspace, args.exclude, args.offline)
    if not rows:
        sys.exit(f"ERREUR: aucune branche b4/* dans {args.repo}")
    content = render(rows, ignored, args)
    if args.stdout:
        print(content, end="")
        return
    with open(args.output, "w", encoding="utf-8") as fh:
        fh.write(content)
    print(f"{args.output} : {len(rows)} séries, {len(attention_items(rows))} point(s) à traiter")


if __name__ == "__main__":
    main()
