# ups_mp13_clk_rng

**STATUS : `DRAFT`**  <!-- DRAFT | V<n> SENT | V<n> REVIEWED | ACKED | APPLIED | MERGED | ABANDONED -->
**SOC : STM32MP13**  <!-- STM32MP13 | STM32MP15 | STM32MP21 | STM32MP25 | STM32MP (commun) -->
**Dernière MAJ : 2026-10-26**

## INFO

<!-- auto:begin (remplacé à chaque refresh, ne pas éditer à la main) -->
| Champ | Valeur |
|---|---|
| Branche | `b4/ups_mp13_clk_rng` |
| Repo kernel | `~/Views/upstream_mp21/linux-next` |
| Base | `v7.3-rc6` (`a90ee4305c4a`) |
| Change-Id | `20261016-ups_mp13_clk_rng-fe616b378bbc` |
| Titre (cover) | clk: stm32mp13: remove LSE from the RNG1 kernel clock sources |
| Révision courante | v1 (dernière envoyée : aucune) |
| Sous-système / ML | linux-clk@vger.kernel.org, linux-stm32@st-md-mailman.stormreply.com, linux-arm-kernel@lists.infradead.org, linux-kernel@vger.kernel.org |
| Maintainers | Stephen Boyd <sboyd@kernel.org>, Brian Masney <bmasney+clk@redhat.com>, Jerome Brunet <jbrunet+clk@baylibre.com>, Maxime Coquelin <mcoquelin.stm32@gmail.com>, Alexandre Torgue <alexandre.torgue@foss.st.com> |
| Tree(s) cible(s) | `git://git.kernel.org/pub/scm/linux/kernel/git/clk/linux.git` (clk-next), `git://git.kernel.org/pub/scm/linux/kernel/git/atorgue/stm32.git` (stm32-next) |
| Patchwork | - |

### Patches (révision courante)

| # | Sujet | Commit | État Patchwork (dernière version envoyée) | Tags reçus |
|---|---|---|---|---|
| 1/2 | clk: stm32: add support for a parent table in the muxes | `6de80b3ccab0` | - | - |
| 2/2 | clk: stm32mp13: remove LSE from the RNG1 clock sources | `33204c2b0f9c` | - | - |

### Versions envoyées

| Version | Date | Message-ID | Lore | Patchwork |
|---|---|---|---|---|
| - | - | - | - | - |
<!-- auto:end -->

## COMMENTS

<!-- Ajouter en haut les plus récents : `- YYYY-MM-DD [vN] <qui> : résumé (lien lore)` -->

## COMMANDS

```bash
# Aller sur la branche
cd ~/Views/upstream_mp21/linux-next && git checkout b4/ups_mp13_clk_rng

# Vérifs avant envoi
b4 prep --edit-cover                        # éditer la cover / changelog
b4 prep -c                                  # (re)calculer To/Cc automatiques
b4 prep -p /tmp/ups_mp13_clk_rng_out && scripts/checkpatch.pl --strict /tmp/ups_mp13_clk_rng_out/*.patch

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

- [ ] Cover : remplacer le `[TODO: add RM0475 / errata reference]` par la référence RM0475 / errata (LSE réservé sur silicium cut 1.1)
- [ ] Cover : compléter le paragraphe « Tested on [STM32MP135F-DK, cut 1.1 / 1.0 - TODO] » (rng1_k parent/rate dans clk_summary, probe RNG, lecture hwrng)
- [ ] Vérifier le comportement orphan si LSE reste sélectionné par un stage de boot précédent (cut 1.0)
- [ ] `checkpatch --strict` puis `b4 send --reflect` avant l'envoi réel de la v1

---

[⬅ Previous](./UPSTREAM.md)
