# ups_mp21_rcc_fix_last_clock_binding

**STATUS : `MERGED`**  <!-- DRAFT | V<n> SENT | V<n> REVIEWED | ACKED | APPLIED | MERGED | ABANDONED -->
**SOC : STM32MP21**  <!-- STM32MP13 | STM32MP15 | STM32MP21 | STM32MP25 | STM32MP (commun) -->
**Dernière MAJ : 2026-10-26**

## INFO

<!-- auto:begin (remplacé à chaque refresh, ne pas éditer à la main) -->
| Champ | Valeur |
|---|---|
| Suivi | manuel (hors b4) : patch unique envoyé sans `b4 prep`, donc ni cover ni change-id |
| Branche | `ups_mp21_rcc_fix_last_clock_binding` |
| Repo kernel | `~/Views/upstream_mp21/linux-next` |
| Base | `v7.3-rc6` (`a90ee4305c4a`) |
| Change-Id | - |
| Titre (cover) | clk: stm32: fix clock array size for STM32MP21 |
| Révision courante | v1 (dernière envoyée : v1) |
| Sous-système / ML | linux-clk@vger.kernel.org, linux-stm32@st-md-mailman.stormreply.com, linux-arm-kernel@lists.infradead.org, linux-kernel@vger.kernel.org |
| Maintainers | Stephen Boyd <sboyd@kernel.org>, Brian Masney <bmasney+clk@redhat.com>, Jerome Brunet <jbrunet+clk@baylibre.com>, Maxime Coquelin <mcoquelin.stm32@gmail.com>, Alexandre Torgue <alexandre.torgue@foss.st.com> |
| Tree(s) cible(s) | `git://git.kernel.org/pub/scm/linux/kernel/git/clk/linux.git` (clk-pile, appliqué), `git://git.kernel.org/pub/scm/linux/kernel/git/atorgue/stm32.git` (stm32-next) |
| Patchwork | [linux-clk](https://patchwork.kernel.org/project/linux-clk/patch/20261012131859.215240-1-gabriel.fernandez@foss.st.com/) — [série](https://patchwork.kernel.org/series/1183920/) |

### Patches (révision courante)

| # | Sujet | Commit | État Patchwork (v1, linux-clk) | Tags reçus |
|---|---|---|---|---|
| 1/1 | clk: stm32: fix clock array size for STM32MP21 | `798c74a4f7f2` | accepted (delegate Jerome Brunet) → [`57e9b2c11056`](https://git.kernel.org/clk/linux/c/57e9b2c11056), dans linux-next depuis `next-20261023` | - |

### Versions envoyées

| Version | Date | Message-ID | Lore | Patchwork |
|---|---|---|---|---|
| v1 | 2026-10-12 | `20261012131859.215240-1-gabriel.fernandez@foss.st.com` | [lore](https://lore.kernel.org/r/20261012131859.215240-1-gabriel.fernandez@foss.st.com) | [série](https://patchwork.kernel.org/series/1183920/) (accepted) |
<!-- auto:end -->

## COMMENTS

- 2026-10-12 [v1] Jerome Brunet : Applied to clk/linux.git (clk-pile), commit 57e9b2c11056 ; présent dans linux-next (next-20261023) (https://patchwork.kernel.org/comment/27275202/)
- 2026-10-12 [v1] Gabriel Fernandez : v1 envoyée hors b4 (patch-id identique au commit local `798c74a4f7f2`) ; `STM32MP21_LAST_CLK` = `CK_KER_STM + 1` au lieu de `CK_SCMI_KER_ETR` ; pas de backport stable (aucun DT n'utilise encore le RCC STM32MP21)

<!-- Ajouter en haut les plus récents : `- YYYY-MM-DD [vN] <qui> : résumé (lien lore)` -->

## COMMANDS

```bash
# Aller sur la branche
cd ~/Views/upstream_mp21/linux-next && git checkout ups_mp21_rcc_fix_last_clock_binding

# Suivre l'arrivée du commit en amont
git fetch origin && git describe --contains 57e9b2c11056   # next-YYYYMMDD puis vX.Y-rcN une fois dans mainline

# Récupérer le patch / le thread
b4 am -o- 20261012131859.215240-1-gabriel.fernandez@foss.st.com | git am
b4 mbox 20261012131859.215240-1-gabriel.fernandez@foss.st.com
```

## TODO

- [ ] (à compléter)

---

[⬅ Previous](./UPSTREAM.md)
