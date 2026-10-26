# {{NAME}}

**STATUS : `{{STATUS}}`**  <!-- DRAFT | V<n> SENT | V<n> REVIEWED | ACKED | APPLIED | MERGED | ABANDONED -->
**SOC : {{SOC}}**  <!-- STM32MP13 | STM32MP15 | STM32MP21 | STM32MP25 | STM32MP (commun) -->
**Dernière MAJ : {{DATE}}**

## INFO

<!-- auto:begin (remplacé à chaque refresh, ne pas éditer à la main) -->
| Champ | Valeur |
|---|---|
| Branche | `{{BRANCH}}` |
| Repo kernel | `{{REPO}}` |
| Base | `{{BASE_DESCRIBE}}` (`{{BASE_COMMIT}}`) |
| Change-Id | `{{CHANGE_ID}}` |
| Titre (cover) | {{COVER_SUBJECT}} |
| Révision courante | {{REVISION}} (dernière envoyée : {{LAST_SENT}}) |
| Sous-système / ML | {{MAILING_LISTS}} |
| Maintainers | {{MAINTAINERS}} |
| Tree(s) cible(s) | {{TREES}} |
| Patchwork | {{PATCHWORK_URLS}} |

### Patches (révision courante)

| # | Sujet | Commit | État Patchwork (dernière version envoyée) | Tags reçus |
|---|---|---|---|---|
{{PATCH_ROWS}}

### Versions envoyées

| Version | Date | Message-ID | Lore | Patchwork |
|---|---|---|---|---|
{{VERSION_ROWS}}
<!-- auto:end -->

## COMMENTS

<!-- Ajouter en haut les plus récents : `- YYYY-MM-DD [vN] <qui> : résumé (lien lore)` -->

## COMMANDS

```bash
# Aller sur la branche
cd {{REPO}} && git checkout {{BRANCH}}

# Vérifs avant envoi
b4 prep --edit-cover                        # éditer la cover / changelog
b4 prep -c                                  # (re)calculer To/Cc automatiques
b4 prep -p /tmp/{{NAME}}_out && scripts/checkpatch.pl --strict /tmp/{{NAME}}_out/*.patch
b4 prep --compare-to v{{LAST_SENT_NUM}}     # range-diff vs dernière version envoyée

# Envoi
b4 send --dry-run                          # relire les mails générés
b4 send --reflect                          # tout envoyer à soi-même d'abord
b4 send                                    # envoi réel

# Après review : récupérer les trailers (Reviewed-by, Acked-by...)
b4 trailers -u

# Récupérer un thread / une série
b4 am -o- <msgid> | git am
b4 mbox <msgid>

# Quand c'est accepté
b4 ty --auto --dry-run                      # puis sans --dry-run (ou -S pour envoyer)
```

## TODO

- [ ] (à compléter)
