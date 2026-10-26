# ups_mp21_dt_rcc

**STATUS : `V1 SENT`**  <!-- DRAFT | V<n> SENT | V<n> REVIEWED | ACKED | APPLIED | MERGED | ABANDONED -->
**SOC : STM32MP21**  <!-- STM32MP13 | STM32MP15 | STM32MP21 | STM32MP25 | STM32MP (commun) -->
**Dernière MAJ : 2026-10-26**

## INFO

<!-- auto:begin (remplacé à chaque refresh, ne pas éditer à la main) -->
| Champ | Valeur |
|---|---|
| Suivi | manuel (hors b4) : patch unique envoyé sans `b4 prep`, donc ni cover ni change-id |
| Branche | `ups_mp21_dt_rcc` (snapshot v1 : `ups_mp21_dt_rcc_v1`, identique) |
| Repo kernel | `~/Views/upstream_mp21/stm32` |
| Base | `stm32-dt-for-v7.4-1` (`f831584128ac`) |
| Change-Id | - |
| Titre (cover) | arm64: dts: st: add RCC support for STM32MP21 |
| Révision courante | v1 (dernière envoyée : v1) |
| Sous-système / ML | devicetree@vger.kernel.org, linux-stm32@st-md-mailman.stormreply.com, linux-arm-kernel@lists.infradead.org, linux-kernel@vger.kernel.org |
| Maintainers | Rob Herring <robh@kernel.org>, Krzysztof Kozlowski <krzk+dt@kernel.org>, Conor Dooley <conor+dt@kernel.org>, Maxime Coquelin <mcoquelin.stm32@gmail.com>, Alexandre Torgue <alexandre.torgue@foss.st.com> |
| Tree(s) cible(s) | `git://git.kernel.org/pub/scm/linux/kernel/git/atorgue/stm32.git` (stm32-next), `git://git.kernel.org/pub/scm/linux/kernel/git/robh/linux.git` |
| Patchwork | [linux-arm-kernel](https://patchwork.kernel.org/project/linux-arm-kernel/patch/20261008080437.20270-1-gabriel.fernandez@foss.st.com/) — [série](https://patchwork.kernel.org/series/1181385/) |

### Patches (révision courante)

| # | Sujet | Commit | État Patchwork (v1, linux-arm-kernel) | Tags reçus |
|---|---|---|---|---|
| 1/1 | arm64: dts: st: add RCC support for STM32MP21 | `33cc819b4d00` | new (checks: pending) | - |

### Versions envoyées

| Version | Date | Message-ID | Lore | Patchwork |
|---|---|---|---|---|
| v1 | 2026-10-08 | `20261008080437.20270-1-gabriel.fernandez@foss.st.com` | [lore](https://lore.kernel.org/r/20261008080437.20270-1-gabriel.fernandez@foss.st.com) | [série](https://patchwork.kernel.org/series/1181385/) |
<!-- auto:end -->

## COMMENTS

- 2026-10-26 [v1] Gabriel Fernandez : aucun retour sur lore/Patchwork depuis l'envoi du 2026-10-08 (état `new`, 0 commentaire) ; dépend du fix clk `STM32MP21_LAST_CLK` (voir ups_mp21_rcc_fix_last_clock_binding)
- 2026-10-08 [v1] Gabriel Fernandez : v1 envoyée hors b4 (patch-id identique au commit local `33cc819b4d00`) ; ajoute le nœud `rcc` (`st,stm32mp21-rcc`, horloges SCMI en parents) et passe `usart2` sur `CK_KER_USART2` en retirant les `fixed-clock` flexgen

<!-- Ajouter en haut les plus récents : `- YYYY-MM-DD [vN] <qui> : résumé (lien lore)` -->

## COMMANDS

```bash
# Aller sur la branche
cd ~/Views/upstream_mp21/stm32 && git checkout ups_mp21_dt_rcc

# Vérifs (hors b4)
scripts/checkpatch.pl --strict -g HEAD
make ARCH=arm64 CROSS_COMPILE=aarch64-linux-gnu- CHECK_DTBS=y st/stm32mp215f-dk.dtb

# Régénérer la série en v2 si besoin (puis relire avec --dry-run avant d'envoyer)
git format-patch -1 -v2 --base=auto -o /tmp/ups_mp21_dt_rcc_out
scripts/get_maintainer.pl --nogit --nogit-fallback /tmp/ups_mp21_dt_rcc_out/*.patch
git send-email --dry-run /tmp/ups_mp21_dt_rcc_out/*.patch

# Passer sous b4 pour la suite (optionnel)
b4 prep --enroll f831584128ac

# Récupérer le patch / le thread
b4 am -o- 20261008080437.20270-1-gabriel.fernandez@foss.st.com | git am
b4 mbox 20261008080437.20270-1-gabriel.fernandez@foss.st.com
```

## TODO

- [ ] Vérifier que le fix clk `57e9b2c11056` (clk-pile, linux-next) est en amont avant l'application du DT RCC dans stm32-next (dépendance de merge)
- [ ] Surveiller l'application dans stm32-next (Alexandre Torgue) ; relancer si l'état Patchwork reste `new`

---

[⬅ Previous](./UPSTREAM.md)
