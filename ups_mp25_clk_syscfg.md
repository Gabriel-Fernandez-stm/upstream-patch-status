# ups_mp25_clk_syscfg

**STATUS : `DRAFT`**  <!-- DRAFT | V<n> SENT | V<n> REVIEWED | ACKED | APPLIED | MERGED | ABANDONED -->
**SOC : STM32MP25**  <!-- STM32MP13 | STM32MP15 | STM32MP21 | STM32MP25 | STM32MP (commun) -->
**Dernière MAJ : 2026-10-26**

## INFO

<!-- auto:begin (remplacé à chaque refresh, ne pas éditer à la main) -->
| Champ | Valeur |
|---|---|
| Branche | `b4/ups_mp25_clk_syscfg` |
| Repo kernel | `~/Views/upstream-next/linux-next` (worktree de `~/Views/upstream_mp21/linux-next`) |
| Base | `next-20261023` (`20a33c6b6cbe`) |
| Change-Id | `20261026-ups_mp25_clk_syscfg-8fc6c68a0de3` |
| Titre (cover) | Add STM32MP2 LTDC pixel clock multiplexer |
| Révision courante | v1 (dernière envoyée : aucune) |
| Sous-système / ML | devicetree@vger.kernel.org, linux-stm32@st-md-mailman.stormreply.com, linux-arm-kernel@lists.infradead.org, linux-kernel@vger.kernel.org |
| Maintainers | Maxime Coquelin <mcoquelin.stm32@gmail.com>, Alexandre Torgue <alexandre.torgue@foss.st.com>, Christophe Roullier <christophe.roullier@foss.st.com>, Rob Herring <robh@kernel.org>, Krzysztof Kozlowski <krzk+dt@kernel.org>, Conor Dooley <conor+dt@kernel.org> |
| Tree(s) cible(s) | `git://git.kernel.org/pub/scm/linux/kernel/git/atorgue/stm32.git` (stm32-next), `git://git.kernel.org/pub/scm/linux/kernel/git/robh/linux.git` (bindings) |
| Patchwork | - |

### Patches (révision courante)

| # | Sujet | Commit | État Patchwork (dernière version envoyée) | Tags reçus |
|---|---|---|---|---|
| 1/4 | dt-bindings: arm: stm32: Document st,stm32mp23/25-syscfg clocks | `3ff074a41754` | - | - |
| 2/4 | soc: st: stm32mp2-syscfg: add LTDC pixel clock mux | `7d9c623e81d3` | - | - |
| 3/4 | arm64: dts: st: reference DSI byte clock in RCC only on SoCs with DSI | `3edecd4099ec` | - | - |
| 4/4 | arm64: dts: st: describe LTDC pixel clock mux inputs on stm32mp235/255 | `0835777f3303` | - | - |

### Versions envoyées

| Version | Date | Message-ID | Lore | Patchwork |
|---|---|---|---|---|
| - | - | - | - | - |
<!-- auto:end -->

## COMMENTS

<!-- Ajouter en haut les plus récents : `- YYYY-MM-DD [vN] <qui> : résumé (lien lore)` -->

## COMMANDS

```bash
# Aller sur la branche (déjà checkoutée dans ce worktree ; impossible de la checkout ailleurs)
cd ~/Views/upstream-next/linux-next && git checkout b4/ups_mp25_clk_syscfg

# Vérifs avant envoi
b4 prep --edit-cover                        # éditer la cover / changelog
b4 prep -c                                  # (re)calculer To/Cc automatiques
b4 prep -p /tmp/ups_mp25_clk_syscfg_out && scripts/checkpatch.pl --strict /tmp/ups_mp25_clk_syscfg_out/*.patch

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

- [ ] Base = `next-20261023` (autres séries sur `v7.3-rc6`) : confirmer la base d'envoi (stm32-next) et rebaser la branche si besoin
- [ ] Vérifier la mention « Parts of this series were prepared with the help of GitHub Copilot » dans la cover vs. la politique du kernel (`Documentation/process/coding-assistants.rst`, `generated-content.rst`) : aucun trailer d'assistance IA sur les 4 commits
- [ ] Valider les bindings : `make dt_binding_check DT_SCHEMA_FILES=st,stm32-syscon.yaml` et `make CHECK_DTBS=y st/stm32mp235f-dk.dtb st/stm32mp255c-dhcos-dhsbc.dtb`
- [ ] Cover : l'horloge DSI byte reste un placeholder `clk_dsi_txbyte` tant que le nœud DSI n'est pas ajouté — le confirmer dans la cover
- [ ] `checkpatch --strict` puis `b4 send --reflect` avant l'envoi réel de la v1

---

[⬅ Previous](./UPSTREAM.md)
