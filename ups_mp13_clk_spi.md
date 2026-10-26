# ups_mp13_clk_spi

**STATUS : `V1 SENT`** (v2 en préparation)  <!-- DRAFT | V<n> SENT | V<n> REVIEWED | ACKED | APPLIED | MERGED | ABANDONED -->
**SOC : STM32MP13**  <!-- STM32MP13 | STM32MP15 | STM32MP21 | STM32MP25 | STM32MP (commun) -->
**Dernière MAJ : 2026-10-26**

## INFO

<!-- auto:begin (remplacé à chaque refresh, ne pas éditer à la main) -->
| Champ | Valeur |
|---|---|
| Branche | `b4/ups_mp13_clk_spi` |
| Repo kernel | `~/Views/upstream_mp21/linux-next` |
| Base | `v7.3-rc6` (`a90ee4305c4a`) |
| Change-Id | `20261016-ups_mp13_clk_spi-cc1ad9d1f7e7` |
| Titre (cover) | clk: stm32mp13: add the SPI1 to SPI5 bus clocks |
| Révision courante | v2 (dernière envoyée : v1) |
| Sous-système / ML | linux-clk@vger.kernel.org, linux-stm32@st-md-mailman.stormreply.com, linux-arm-kernel@lists.infradead.org, devicetree@vger.kernel.org, linux-kernel@vger.kernel.org |
| Maintainers | Stephen Boyd <sboyd@kernel.org>, Brian Masney <bmasney+clk@redhat.com>, Jerome Brunet <jbrunet+clk@baylibre.com>, Maxime Coquelin <mcoquelin.stm32@gmail.com>, Alexandre Torgue <alexandre.torgue@foss.st.com>, Rob Herring <robh@kernel.org>, Krzysztof Kozlowski <krzk+dt@kernel.org>, Conor Dooley <conor+dt@kernel.org> |
| Tree(s) cible(s) | `git://git.kernel.org/pub/scm/linux/kernel/git/clk/linux.git` (clk-next), `git://git.kernel.org/pub/scm/linux/kernel/git/atorgue/stm32.git` (stm32-next) |
| Patchwork | [linux-clk](https://patchwork.kernel.org/project/linux-clk/cover/20261020-ups_mp13_clk_spi-v1-0-6c00730945c7@foss.st.com/) — [série](https://patchwork.kernel.org/series/1189542/) |

### Patches (révision courante)

| # | Sujet | Commit | État Patchwork (v1, linux-clk) | Tags reçus |
|---|---|---|---|---|
| 1/3 | clk: stm32mp13: define the number of clocks in the driver | `dcb56a3945b5` | new (checks: pending) | - |
| 2/3 | dt-bindings: clock: stm32mp13: add SPI1 to SPI5 bus clocks | `b671228de46b` | new (checks: pending) | - |
| 3/3 | clk: stm32mp13: add the SPI1 to SPI5 bus clocks | `3c339a2ea5f2` | new (checks: pending) | - |

### Versions envoyées

| Version | Date | Message-ID | Lore | Patchwork |
|---|---|---|---|---|
| v1 | 2026-10-20 | `20261020-ups_mp13_clk_spi-v1-0-6c00730945c7@foss.st.com` | [lore](https://lore.kernel.org/r/20261020-ups_mp13_clk_spi-v1-0-6c00730945c7@foss.st.com) | [série](https://patchwork.kernel.org/series/1189542/) |
<!-- auto:end -->

## COMMENTS

- 2026-10-22 [v1] Krzysztof Kozlowski : Acked-by sur 2/3 (dt-bindings) (https://patchwork.kernel.org/comment/27302252/)

<!-- Ajouter en haut les plus récents : `- YYYY-MM-DD [vN] <qui> : résumé (lien lore)` -->

## COMMANDS

```bash
# Aller sur la branche
cd ~/Views/upstream_mp21/linux-next && git checkout b4/ups_mp13_clk_spi

# Vérifs avant envoi
b4 prep --edit-cover                        # éditer la cover / changelog
b4 prep -c                                  # (re)calculer To/Cc automatiques
b4 prep -p /tmp/ups_mp13_clk_spi_out && scripts/checkpatch.pl --strict /tmp/ups_mp13_clk_spi_out/*.patch
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

- [ ] Récupérer l'Acked-by de Krzysztof sur 2/3 : `b4 trailers -u`
- [ ] Finaliser la v2 (cover + changelog), puis `b4 send --reflect` avant l'envoi réel

---

[⬅ Previous](./UPSTREAM.md)
