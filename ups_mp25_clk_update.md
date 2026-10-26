# ups_mp25_clk_update

**STATUS : `V2 SENT`** (v3 en préparation)  <!-- DRAFT | V<n> SENT | V<n> REVIEWED | ACKED | APPLIED | MERGED | ABANDONED -->
**SOC : STM32MP25**  <!-- STM32MP13 | STM32MP15 | STM32MP21 | STM32MP25 | STM32MP (commun) -->
**Dernière MAJ : 2026-10-26**

## INFO

<!-- auto:begin (remplacé à chaque refresh, ne pas éditer à la main) -->
| Champ | Valeur |
|---|---|
| Branche | `b4/ups_mp25_clk_update` |
| Repo kernel | `~/Views/upstream_mp21/linux-next` |
| Base | `v7.3-rc6` (`a90ee4305c4a`) |
| Change-Id | `20261022-ups_mp25_clk_update-7f1a03b1c6f2` |
| Titre (cover) | clk: stm32mp25: add Cortex-M0 D3 clocks, ETR/STM and USB2PHY1 STP |
| Révision courante | v3 (dernière envoyée : v2) |
| Sous-système / ML | linux-clk@vger.kernel.org, devicetree@vger.kernel.org, linux-stm32@st-md-mailman.stormreply.com, linux-arm-kernel@lists.infradead.org, linux-kernel@vger.kernel.org |
| Maintainers | Stephen Boyd <sboyd@kernel.org>, Brian Masney <bmasney+clk@redhat.com>, Jerome Brunet <jbrunet+clk@baylibre.com>, Rob Herring <robh@kernel.org>, Krzysztof Kozlowski <krzk+dt@kernel.org>, Conor Dooley <conor+dt@kernel.org>, Maxime Coquelin <mcoquelin.stm32@gmail.com>, Alexandre Torgue <alexandre.torgue@foss.st.com>, Gabriel Fernandez <gabriel.fernandez@foss.st.com> |
| Tree(s) cible(s) | `git://git.kernel.org/pub/scm/linux/kernel/git/clk/linux.git` (clk-next), `git://git.kernel.org/pub/scm/linux/kernel/git/robh/linux.git` (bindings), `git://git.kernel.org/pub/scm/linux/kernel/git/atorgue/stm32.git` (stm32-next) |
| Patchwork | [linux-clk](https://patchwork.kernel.org/project/linux-clk/cover/20261023-ups_mp25_clk_update-v2-0-398d348ea8fd@foss.st.com/) — [série](https://patchwork.kernel.org/series/1192281/) |

### Patches (révision courante)

| # | Sujet | Commit | État Patchwork (v2, linux-clk) | Tags reçus |
|---|---|---|---|---|
| 1/7 | clk: stm32mp25: define the number of clocks in the driver | `a13421736573` | new (checks: pending) | - |
| 2/7 | dt-bindings: stm32: add kernel clocks for ETR and STM | `1e747b40f99b` | new (checks: pending) | - |
| 3/7 | clk: stm32mp25: update register with reference manual | `830ea31efcb9` | new (checks: pending) | - |
| 4/7 | dt-bindings: stm32: add clock binding for Cortex-CM0 on stm32mp25 platform | `9dddb37d285a` | new (checks: pending) | - |
| 5/7 | clk: stm32mp25: add clock for D3 peripherals allocation for Cortex-CM0 | `044bfe763652` | new (checks: pending) | - |
| 6/7 | dt-bindings: stm32: add binding for usb2phy1stp clock on stm32mp25 | `93d1945f2c50` | new (checks: pending) | - |
| 7/7 | clk: stm32mp25: add ck_ker_usb2phy1_stp clock | `499d9acce698` | new (checks: pending) | - |

### Versions envoyées

| Version | Date | Message-ID | Lore | Patchwork |
|---|---|---|---|---|
| v1 | 2026-10-23 | `20261023-ups_mp25_clk_update-v1-0-e906e7a38cb3@foss.st.com` | [lore](https://lore.kernel.org/r/20261023-ups_mp25_clk_update-v1-0-e906e7a38cb3@foss.st.com) | [série](https://patchwork.kernel.org/series/1192156/) (superseded) |
| v2 | 2026-10-23 | `20261023-ups_mp25_clk_update-v2-0-398d348ea8fd@foss.st.com` | [lore](https://lore.kernel.org/r/20261023-ups_mp25_clk_update-v2-0-398d348ea8fd@foss.st.com) | [série](https://patchwork.kernel.org/series/1192281/) |
<!-- auto:end -->

## COMMENTS

- 2026-10-23 [v1] sashiko-bot (revue IA) : 2 remarques Medium sur 7/7 (`.disable_unused` manquant, rate en cache périmé/nul pour ck_ker_usb2phy1_stp) → corrigé en v2 avec `clk_stm32_gate_ops` (https://patchwork.kernel.org/comment/27305200/)

<!-- Ajouter en haut les plus récents : `- YYYY-MM-DD [vN] <qui> : résumé (lien lore)` -->

## COMMANDS

```bash
# Aller sur la branche
cd ~/Views/upstream_mp21/linux-next && git checkout b4/ups_mp25_clk_update

# Vérifs avant envoi
b4 prep --edit-cover                        # éditer la cover / changelog
b4 prep -c                                  # (re)calculer To/Cc automatiques
b4 prep -p /tmp/ups_mp25_clk_update_out && scripts/checkpatch.pl --strict /tmp/ups_mp25_clk_update_out/*.patch
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

- [ ] Vérifier sur lore s'il y a des retours humains sur la v2 (aucun commentaire Patchwork au 2026-10-26 ; patches 1/7 et 2/7 en `needs-ack` côté projet devicetree)
- [ ] Remplir le changelog v3 dans la cover (`b4 prep --edit-cover`, lignes EDITME) — v3 pas encore envoyable (`needs-editing`)
- [ ] Après review : `b4 trailers -u`

---

[⬅ Previous](./UPSTREAM.md)
