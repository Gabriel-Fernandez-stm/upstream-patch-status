# UPSTREAM — suivi des séries kernel STM32MP

_Généré le 2026-10-26 16:13 par le skill `b4-upstream-tracker` — ne pas éditer à la main : `python3 .github/skills/b4-upstream-tracker/scripts/b4_dashboard.py`. STATUS, COMMENTS et TODO viennent des fiches ; versions envoyées et Patchwork viennent de b4 et Patchwork._

## Vue d'ensemble

| SoC | 📝 DRAFT | 📤 SENT | 💬 REVIEWED / ACKED | 🟢 APPLIED / MERGED | Total |
|---|---|---|---|---|---|
| STM32MP (commun) | 0 | 1 | 0 | 0 | 1 |
| STM32MP13 | 1 | 1 | 0 | 0 | 2 |
| STM32MP15 | 0 | 1 | 0 | 0 | 1 |
| STM32MP21 | 0 | 0 | 0 | 0 | 0 |
| STM32MP25 | 1 | 2 | 0 | 0 | 3 |

## À traiter

- ⚠ **ups_mp15_clk_update** : fiche manquante → `/b4-upstream-tracker create b4/ups_mp15_clk_update`

## STM32MP (commun)

| Série | Titre (cover) | Version | STATUS | Patchwork (dernière version envoyée) | Dernier commentaire | TODO |
|---|---|---|---|---|---|---|
| [ups_reset_control_reset](./ups_reset_control_reset.md) | clk: stm32: add support for reset_control_reset() | v2 envoyée · v3 en cours | 📤 V2 SENT | [1×new](https://patchwork.kernel.org/series/1188872/) ⏳ | 2026-10-14 [v1] Gabriel Fernandez : réponse à Philipp — consommateurs concernés : stm32-d… | 3 |

## STM32MP13

| Série | Titre (cover) | Version | STATUS | Patchwork (dernière version envoyée) | Dernier commentaire | TODO |
|---|---|---|---|---|---|---|
| [ups_mp13_clk_rng](./ups_mp13_clk_rng.md) | clk: stm32mp13: remove LSE from the RNG1 kernel clock sources | v1 (draft) | 📝 DRAFT | — | — | 4 |
| [ups_mp13_clk_spi](./ups_mp13_clk_spi.md) | clk: stm32mp13: add the SPI1 to SPI5 bus clocks | v1 envoyée · v2 en cours | 📤 V1 SENT | [3×new](https://patchwork.kernel.org/series/1189542/) ⏳ · Acked-by×1 · 💬 1 | 2026-10-22 [v1] Krzysztof Kozlowski : Acked-by sur 2/3 (dt-bindings) | 2 |

## STM32MP15

| Série | Titre (cover) | Version | STATUS | Patchwork (dernière version envoyée) | Dernier commentaire | TODO |
|---|---|---|---|---|---|---|
| ups_mp15_clk_update ⚠ fiche manquante | clk: stm32mp1: add I2S_CKIN as PLL4 source and keep boot-enabled clocks running | v1 envoyée · v2 en cours | 📤 V1 SENT | [3×new](https://patchwork.kernel.org/series/1189603/) ⏳ | — | — |

## STM32MP21

_Aucune série._

## STM32MP25

| Série | Titre (cover) | Version | STATUS | Patchwork (dernière version envoyée) | Dernier commentaire | TODO |
|---|---|---|---|---|---|---|
| [ups_mp25_clk_mdf](./ups_mp25_clk_mdf.md) | clk: stm32mp25: allow MDF kernel clock rate changes to propagate to parent | v1 envoyée · v2 en cours | 📤 V1 SENT | [1×new](https://patchwork.kernel.org/series/1191834/) ⏳ | — | 2 |
| [ups_mp25_clk_syscfg](./ups_mp25_clk_syscfg.md) | Add STM32MP2 LTDC pixel clock multiplexer | v1 (draft) | 📝 DRAFT | — | — | 5 |
| [ups_mp25_clk_update](./ups_mp25_clk_update.md) | clk: stm32mp25: add Cortex-M0 D3 clocks, ETR/STM and USB2PHY1 STP | v2 envoyée · v3 en cours | 📤 V2 SENT | [7×new](https://patchwork.kernel.org/series/1192280/) ⏳ | 2026-10-23 [v1] sashiko-bot (revue IA) : 2 remarques Medium sur 7/7 (`.disable_unused` ma… | 3 |
