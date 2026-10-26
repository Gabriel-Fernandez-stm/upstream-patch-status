# ups_reset_control_reset

**STATUS : `V2 SENT`** (v3 en préparation)  <!-- DRAFT | V<n> SENT | V<n> REVIEWED | ACKED | APPLIED | MERGED | ABANDONED -->
**SOC : STM32MP (commun)**  <!-- STM32MP13 | STM32MP15 | STM32MP21 | STM32MP25 | STM32MP (commun) -->
**Dernière MAJ : 2026-10-26**

## INFO

<!-- auto:begin (remplacé à chaque refresh, ne pas éditer à la main) -->
| Champ | Valeur |
|---|---|
| Branche | `b4/ups_reset_control_reset` |
| Repo kernel | `~/Views/upstream_mp21/linux-next` |
| Base | `v7.3-rc6` (`a90ee4305c4a`) |
| Change-Id | `20261013-ups_reset_control_reset-4c2f1b08ddf1` |
| Titre (cover) | clk: stm32: add support for reset_control_reset() |
| Révision courante | v3 (dernière envoyée : v2) |
| Sous-système / ML | linux-clk@vger.kernel.org, linux-stm32@st-md-mailman.stormreply.com, linux-arm-kernel@lists.infradead.org, linux-kernel@vger.kernel.org |
| Maintainers | Stephen Boyd <sboyd@kernel.org>, Brian Masney <bmasney+clk@redhat.com>, Jerome Brunet <jbrunet+clk@baylibre.com>, Maxime Coquelin <mcoquelin.stm32@gmail.com>, Alexandre Torgue <alexandre.torgue@foss.st.com>, Philipp Zabel <p.zabel@pengutronix.de> (reset controller, en To de la cover) |
| Tree(s) cible(s) | `git://git.kernel.org/pub/scm/linux/kernel/git/clk/linux.git` (clk-next), `git://git.kernel.org/pub/scm/linux/kernel/git/atorgue/stm32.git` (stm32-next) |
| Patchwork | [linux-clk](https://patchwork.kernel.org/project/linux-clk/patch/20261019-ups_reset_control_reset-v2-1-be4ccf511cbb@foss.st.com/) — [série](https://patchwork.kernel.org/series/1188872/) |

### Patches (révision courante)

| # | Sujet | Commit | État Patchwork (v2, linux-clk) | Tags reçus |
|---|---|---|---|---|
| 1/1 | clk: stm32: add support for reset_control_reset() | `163de836c0ad` | new (checks: pending) | - |

### Versions envoyées

| Version | Date | Message-ID | Lore | Patchwork |
|---|---|---|---|---|
| v1 | 2026-10-13 | `20261013-ups_reset_control_reset-v1-1-f8a6c7f6cc3c@foss.st.com` | [lore](https://lore.kernel.org/r/20261013-ups_reset_control_reset-v1-1-f8a6c7f6cc3c@foss.st.com) | [série](https://patchwork.kernel.org/series/1184849/) (superseded) |
| v2 | 2026-10-19 | `20261019-ups_reset_control_reset-v2-1-be4ccf511cbb@foss.st.com` | [lore](https://lore.kernel.org/r/20261019-ups_reset_control_reset-v2-1-be4ccf511cbb@foss.st.com) | [série](https://patchwork.kernel.org/series/1188872/) |
<!-- auto:end -->

## COMMENTS

- 2026-10-14 [v1] Gabriel Fernandez : réponse à Philipp — consommateurs concernés : stm32-dma3 et glue hantro STM32MP25 (`reset_control_reset()` renvoie -ENOTSUPP aujourd'hui) ; certains IP (GPU, driver pas encore upstream) ont un reset auto-désasserté (https://patchwork.kernel.org/comment/27281673/)
- 2026-10-13 [v1] Philipp Zabel : demande des consommateurs ; `.reset` est prévu pour les resets auto-désasserté, pas pour la commodité ; questions sur le délai d'assert (2 µs) et le polling après deassert → v2 : délai 50 µs, polling retiré (https://patchwork.kernel.org/comment/27279398/)

<!-- Ajouter en haut les plus récents : `- YYYY-MM-DD [vN] <qui> : résumé (lien lore)` -->

## COMMANDS

```bash
# Aller sur la branche
cd ~/Views/upstream_mp21/linux-next && git checkout b4/ups_reset_control_reset

# Vérifs avant envoi
b4 prep --edit-cover                        # éditer la cover / changelog
b4 prep -c                                  # (re)calculer To/Cc automatiques
b4 prep -p /tmp/ups_reset_control_reset_out && scripts/checkpatch.pl --strict /tmp/ups_reset_control_reset_out/*.patch
b4 prep --compare-to v2                     # range-diff vs dernière version envoyée

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

- [ ] Vérifier sur lore s'il y a des retours sur la v2 (aucun commentaire Patchwork au 2026-10-26) avant de préparer la v3
- [ ] Remplir le changelog v3 dans la cover (`b4 prep --edit-cover`, lignes EDITME) — v3 pas encore envoyable (`needs-editing`)
- [ ] Si le polling après deassert est nécessaire : patch séparé (il concerne tous les deassert STM32), cf. changelog v2

---

[⬅ Previous](./UPSTREAM.md)
