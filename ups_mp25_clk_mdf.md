# ups_mp25_clk_mdf

**STATUS : `V1 SENT`** (v2 en préparation)  <!-- DRAFT | V<n> SENT | V<n> REVIEWED | ACKED | APPLIED | MERGED | ABANDONED -->
**SOC : STM32MP25**  <!-- STM32MP13 | STM32MP15 | STM32MP21 | STM32MP25 | STM32MP (commun) -->
**Dernière MAJ : 2026-10-26**

## INFO

<!-- auto:begin (remplacé à chaque refresh, ne pas éditer à la main) -->
| Champ | Valeur |
|---|---|
| Branche | `b4/ups_mp25_clk_mdf` |
| Repo kernel | `~/Views/upstream_mp21/linux-next` |
| Base | `v7.3-rc6` (`a90ee4305c4a`) |
| Change-Id | `20261022-ups_mp25_clk_mdf-99ca54f9ac96` |
| Titre (cover) | clk: stm32mp25: allow MDF kernel clock rate changes to propagate to parent |
| Révision courante | v2 (dernière envoyée : v1) |
| Sous-système / ML | linux-clk@vger.kernel.org, linux-stm32@st-md-mailman.stormreply.com, linux-arm-kernel@lists.infradead.org, linux-kernel@vger.kernel.org |
| Maintainers | Stephen Boyd <sboyd@kernel.org>, Brian Masney <bmasney+clk@redhat.com>, Jerome Brunet <jbrunet+clk@baylibre.com>, Maxime Coquelin <mcoquelin.stm32@gmail.com>, Alexandre Torgue <alexandre.torgue@foss.st.com> |
| Tree(s) cible(s) | `git://git.kernel.org/pub/scm/linux/kernel/git/clk/linux.git` (clk-next), `git://git.kernel.org/pub/scm/linux/kernel/git/atorgue/stm32.git` (stm32-next) |
| Patchwork | [linux-clk](https://patchwork.kernel.org/project/linux-clk/patch/20261023-ups_mp25_clk_mdf-v1-1-3043b3fd4bc9@foss.st.com/) — [série](https://patchwork.kernel.org/series/1191837/) |

### Patches (révision courante)

| # | Sujet | Commit | État Patchwork (v1, linux-clk) | Tags reçus |
|---|---|---|---|---|
| 1/1 | clk: stm32mp25: allow MDF kernel clock rate changes to propagate to parent | `67444c84c580` | new (checks: pending) | - |

### Versions envoyées

| Version | Date | Message-ID | Lore | Patchwork |
|---|---|---|---|---|
| v1 | 2026-10-23 | `20261023-ups_mp25_clk_mdf-v1-1-3043b3fd4bc9@foss.st.com` | [lore](https://lore.kernel.org/r/20261023-ups_mp25_clk_mdf-v1-1-3043b3fd4bc9@foss.st.com) | [série](https://patchwork.kernel.org/series/1191837/) |
<!-- auto:end -->

## COMMENTS

<!-- Ajouter en haut les plus récents : `- YYYY-MM-DD [vN] <qui> : résumé (lien lore)` -->

## COMMANDS

```bash
# Aller sur la branche
cd ~/Views/upstream_mp21/linux-next && git checkout b4/ups_mp25_clk_mdf

# Vérifs avant envoi
b4 prep --edit-cover                        # éditer la cover / changelog
b4 prep -c                                  # (re)calculer To/Cc automatiques
b4 prep -p /tmp/ups_mp25_clk_mdf_out && scripts/checkpatch.pl --strict /tmp/ups_mp25_clk_mdf_out/*.patch
b4 prep --compare-to v1                     # range-diff vs dernière version envoyée

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

- [ ] Vérifier sur lore s'il y a des retours sur la v1 (aucun commentaire Patchwork au 2026-10-26)
- [ ] Remplir le changelog v2 dans la cover (`b4 prep --edit-cover`, lignes EDITME) — v2 pas encore envoyable (`needs-editing`) ; n'envoyer la v2 que si des retours le justifient

---

[⬅ Previous](./UPSTREAM.md)
