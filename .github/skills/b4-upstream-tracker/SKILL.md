---
name: b4-upstream-tracker
description: 'Gérer l''upstream d''un patch ou d''une série kernel avec b4 : créer, rafraîchir et annoter la fiche de suivi (.md) d''une branche b4/<nom> dans Upstream-Stuff (statut DRAFT/V1 SENT/V2 SENT, état Patchwork, maintainers, COMMENTS, COMMANDS, TODO) et générer le tableau de bord UPSTREAM.md des séries par SoC (STM32MP commun, MP13, MP15, MP21, MP25). Use when: fiche upstream, suivi de série, dashboard/tableau de bord/status global upstream, b4 prep/send, patchwork, review kernel, status de ma série, ajouter un commentaire/une commande/un todo à une fiche.'
argument-hint: 'dashboard | create|refresh|comment|todo|command [branche b4/xxx]'
---

# b4 Upstream Tracker

Maintient une fiche Markdown par branche b4 (`b4/ups_mp13_clk_spi` → `ups_mp13_clk_spi.md`) dans la racine du workspace `~/Workspace/Upstream-Stuff/`, et un tableau de bord `UPSTREAM.md` qui les agrège par SoC.

## Conventions

- Fiche : `/local/home/frq07381/Workspace/Upstream-Stuff/<branche sans "b4/">.md`
- Tableau de bord : `/local/home/frq07381/Workspace/Upstream-Stuff/UPSTREAM.md` (fichier **généré**, ne jamais l'éditer à la main)
- Repo kernel par défaut : `~/Views/upstream_mp21/linux-next` (demander si l'utilisateur travaille dans un autre `~/Views/*`).
- Template : [fiche-template.md](./assets/fiche-template.md)
- Fiche d'une branche : [b4_status.py](./scripts/b4_status.py) (b4 + git + get_maintainer + API Patchwork)
- Tableau de bord : [b4_dashboard.py](./scripts/b4_dashboard.py) (toutes les branches `b4/*`, sans checkout)
- La zone entre `<!-- auto:begin -->` et `<!-- auto:end -->` est régénérée ; tout le reste (STATUS manuel, SOC, COMMENTS, COMMANDS, TODO) est du contenu utilisateur à préserver.
- Chaque fiche se termine par le pied de page `[⬅ Previous](./UPSTREAM.md)` (retour au tableau de bord), après un `---`. À ajouter si absent lors d'un `refresh`, jamais en doublon ; toute nouvelle entrée de TODO s'insère avant ce pied de page.
- Ne jamais lancer `b4 send`, `git push` ni changer de branche sans demande explicite.

## Procédure : dashboard

1. Lancer `python3 ./scripts/b4_dashboard.py` (options : `--offline` sans Patchwork, `--stdout` pour ne pas écrire, `--repo`, `--workspace`, `--exclude <regex>`).
2. Le script écrit `UPSTREAM.md` : vue d'ensemble par SoC, section « À traiter », puis un tableau par SoC (STM32MP commun, MP13, MP15, MP21, MP25) avec titre de cover, version, STATUS, état Patchwork de la dernière version envoyée (états, checks, trailers `Acked-by`/`Reviewed-by`/… lus dans les réponses, nombre de commentaires), dernier commentaire et TODO ouverts de la fiche.
3. Lire la section « À traiter » et la résumer à l'utilisateur ; proposer pour chaque point l'action correspondante (`create` d'une fiche manquante, `refresh` d'une fiche obsolète, nouvelle révision si `changes-requested`).
4. Règles appliquées par le script :
   - SoC = ligne `**SOC : ...**` de la fiche, sinon préfixe `ups_mpNN_` du nom de branche, sinon `STM32MP (commun)`.
   - STATUS = celui de la fiche ; sans fiche, déduit de b4 (`DRAFT` ou `V<n> SENT`). Une fiche en retard sur git est signalée `⚠`.
   - Branches ignorées par défaut : suffixes `_old`, `_backup`, `_back_vN`, `_vN`.
   - Patchwork : l'état d'un patch est celui du projet principal (celui où le plus de patches ont un état utile) ; `handled-elsewhere` et `not-applicable` sont ignorés.
5. Après un `create` ou un `refresh` de fiche, relancer le dashboard pour garder `UPSTREAM.md` à jour.

## Procédure : create

1. Déterminer la branche (argument, sinon `git branch --show-current` dans le repo). Elle doit commencer par `b4/`.
2. Si la fiche existe déjà → ne pas l'écraser, basculer sur **refresh**.
3. La branche doit être checkoutée (limite de `b4 prep --show-info`) ; sinon demander à l'utilisateur de faire le checkout.
4. Lancer `python3 ./scripts/b4_status.py --repo <repo> --branch <branche>` (ajouter `--offline` si pas de réseau).
5. Remplir le template :
   - `STATUS` = `suggested-status` du script.
   - `SOC` = `STM32MPNN` d'après le nom de branche (`ups_mp13_*` → `STM32MP13`), sinon `STM32MP (commun)`.
   - Maintainers / listes / trees : sortie `get_maintainer.pl` (adresses perso en `Nom <mail>`, listes `@vger`/`lists.*`, lignes `git ...` pour les trees ; mettre la tree cible principale en premier).
   - Patches : une ligne par commit (hors cover), état/tags Patchwork du projet principal (ex. `linux-clk`) pour la dernière version envoyée.
   - Versions envoyées : une ligne par `series-vN` (date Patchwork, msgid, lien lore, lien série Patchwork).
   - `LAST_SENT_NUM` = numéro de la dernière version envoyée (retirer la commande `--compare-to` si DRAFT).
6. Créer la fiche, puis la résumer en quelques lignes à l'utilisateur.

## Procédure : create hors b4

Pour une série envoyée sans `b4 prep` (branche non `b4/*`, éventuellement dans un autre repo, ex. `~/Views/upstream_mp21/stm32`) : pas de `b4_status.py`, la fiche est remplie à la main.

1. Repérer le repo et la branche (`git branch -vv`), la base (`git describe --tags`) et les commits propres à la branche.
2. Retrouver l'envoi sur Patchwork (`/api/1.2/patches/?q=<sujet>&order=-date`) : msgid, date, série, état par projet, commentaires (réponses « Applied… »). Vérifier que l'envoi est bien le commit local (`git patch-id --stable` sur le commit et sur `https://patchwork.kernel.org/patch/<id>/mbox/`) et chercher une version plus récente.
3. Si le commit est déjà dans le repo (`git branch -r --contains <hash>`, `git describe --contains`), le noter ; STATUS `MERGED` s'il est dans linux-next/mainline, `APPLIED` s'il est seulement accepté.
4. Créer `<branche>.md` depuis le template avec, dans la zone `auto`, une ligne `| Suivi | manuel (hors b4) : ... |` en première ligne du tableau (marqueur lu par le dashboard), `Change-Id` = `-`, `Titre (cover)` = sujet du patch, `Révision courante` = `v<n> (dernière envoyée : v<n>)` et une ligne par version dans « Versions envoyées » (`| vN | date | \`msgid\` | lore | Patchwork |`) : le dashboard en lit msgid, titre et révision pour interroger Patchwork.
5. Adapter COMMANDS : pas de `b4 prep`/`b4 send` ; `checkpatch`, `git format-patch -v<n+1> --base=auto`, `git send-email --dry-run`, `b4 am`/`b4 mbox`, `b4 prep --enroll <base>` pour passer sous b4.
6. Relancer le dashboard : une fiche marquée « manuel » sans branche `b4/*` y est ajoutée automatiquement.
7. Refresh d'une telle fiche : refaire les étapes 2 et 3 à la main (le script `b4_status.py` ne s'applique pas).

## Procédure : refresh

1. Relancer le script, remplacer uniquement la zone `auto`, mettre à jour `Dernière MAJ`.
2. Proposer un nouveau STATUS selon les règles ci-dessous ; le modifier uniquement s'il avance (pas de retour en arrière, ne jamais écraser `ABANDONED`/`MERGED`).
3. Si Patchwork montre des changements notables (state ≠ `new`, tags `Reviewed-by`/`Acked-by`, checks `fail`/`warning`, nouveaux commentaires), ajouter une ligne datée dans COMMENTS (le dashboard affiche la première ligne `- ...` de COMMENTS comme « Dernier commentaire ») et proposer des TODO (ex. `b4 trailers -u`, préparer v<n+1>).
4. Relancer le dashboard.

## Procédure : comment / todo / command

- **COMMENTS** : ajouter en haut de la section `- YYYY-MM-DD [vN] <qui> : résumé (lien lore si dispo)`.
- **TODO** : ajouter `- [ ] tâche` ; cocher `- [x]` (avec date) quand c'est fait, ne pas supprimer.
- **COMMANDS** : ajouter la commande dans le bloc ```bash avec un commentaire court ; pas de doublon.
- Ne modifier que la section visée.

## Règles de STATUS

| Statut | Condition |
|---|---|
| `DRAFT` | aucune `series-vN` envoyée |
| `V<n> SENT` | dernière version envoyée = n (noter « v<n+1> en préparation » si la révision courante > n) |
| `V<n> REVIEWED` | retours reçus (comments/tags) sur la v<n>, pas encore applicable |
| `ACKED` | tous les patches ont les Reviewed-by/Acked-by nécessaires |
| `APPLIED` | Patchwork `accepted` ou mail « applied » du maintainer |
| `MERGED` | présent dans linux-next / mainline |
| `ABANDONED` | décision manuelle de l'utilisateur |

États Patchwork utiles : `new`, `under-review`, `changes-requested` (→ prévoir v<n+1>), `accepted`, `superseded` (version remplacée), `rejected`, `awaiting-upstream`. Les entrées des projets `devicetree`/`linux-arm-kernel` en `handled-elsewhere`/`not-applicable` sont normales : se baser sur le projet du sous-système (ex. `linux-clk`).

## Rappels b4 (v0.13)

`b4 prep --show-info` · `b4 prep --compare-to vN` · `b4 prep -c` · `b4 send --dry-run|--reflect` · `b4 trailers -u` · `b4 am`/`b4 mbox <msgid>` · `b4 ty --auto`. `b4 prep --check` et `b4 dig` n'existent pas dans cette version.
