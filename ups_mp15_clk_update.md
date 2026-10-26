# ups_mp15_clk_update

**STATUS : `V1 SENT`** (v2 en préparation)  <!-- DRAFT | V<n> SENT | V<n> REVIEWED | ACKED | APPLIED | MERGED | ABANDONED -->
**SOC : STM32MP15**  <!-- STM32MP13 | STM32MP15 | STM32MP21 | STM32MP25 | STM32MP (commun) -->
**Dernière MAJ : 2026-10-26**

## INFO

<!-- auto:begin (remplacé à chaque refresh, ne pas éditer à la main) -->
| Champ | Valeur |
|---|---|
| Branche | `b4/ups_mp15_clk_update` |
| Repo kernel | `~/Views/upstream_mp21/linux-next` |
| Base | `v7.3-rc6` (`a90ee4305c4a`) |
| Change-Id | `20261020-ups_mp15_clk_update-5e5900c0aaa1` |
| Titre (cover) | clk: stm32mp1: add I2S_CKIN as PLL4 source and keep boot-enabled clocks running ⚠ le sujet de la cover contient encore `Subject: [PATCH 0/3] ` en préfixe (envoyé ainsi en v1) |
| Révision courante | v2 (dernière envoyée : v1) |
| Sous-système / ML | linux-clk@vger.kernel.org, linux-stm32@st-md-mailman.stormreply.com, linux-arm-kernel@lists.infradead.org, linux-kernel@vger.kernel.org |
| Maintainers | Stephen Boyd <sboyd@kernel.org>, Brian Masney <bmasney+clk@redhat.com>, Jerome Brunet <jbrunet+clk@baylibre.com>, Maxime Coquelin <mcoquelin.stm32@gmail.com>, Alexandre Torgue <alexandre.torgue@foss.st.com> |
| Tree(s) cible(s) | `git://git.kernel.org/pub/scm/linux/kernel/git/clk/linux.git` (clk-next), `git://git.kernel.org/pub/scm/linux/kernel/git/atorgue/stm32.git` (stm32-next) |
| Patchwork | [linux-clk](https://patchwork.kernel.org/project/linux-clk/cover/20261020-ups_mp15_clk_update-v1-0-67da20111b08@foss.st.com/) — [série](https://patchwork.kernel.org/series/1189603/) |

### Patches (révision courante)

| # | Sujet | Commit | État Patchwork (v1, linux-clk) | Tags reçus |
|---|---|---|---|---|
| 1/3 | clk: stm32mp1: add i2s_ckin as a clock source of PLL4 | `bb365fcaf31b` | new (checks: pending) | - |
| 2/3 | clk: stm32mp1: don't disable a PLL while its P/Q/R outputs are enabled | `8a8b3e896825` | new (checks: pending) | - |
| 3/3 | clk: stm32mp1: don't disable the ck_trace clock when unused | `99e94fc6eb18` | new (checks: pending) | - |

### Versions envoyées

| Version | Date | Message-ID | Lore | Patchwork |
|---|---|---|---|---|
| v1 | 2026-10-20 | `20261020-ups_mp15_clk_update-v1-0-67da20111b08@foss.st.com` | [lore](https://lore.kernel.org/r/20261020-ups_mp15_clk_update-v1-0-67da20111b08@foss.st.com) | [série](https://patchwork.kernel.org/series/1189603/) |
<!-- auto:end -->

## COMMENTS

- 2026-10-26 [v1] Gabriel Fernandez : erreur à l'envoi de la v1 — `Subject: [PATCH 0/3] ` copié-collé au début du titre de la cover (publiée « [0/3] Subject: [PATCH 0/3] clk: stm32mp1: … » sur Patchwork/lore) ; aucun commentaire reçu pour l'instant, j'attends quelques remarques avant d'envoyer la v2 (https://lore.kernel.org/r/20261020-ups_mp15_clk_update-v1-0-67da20111b08@foss.st.com)

<!-- Ajouter en haut les plus récents : `- YYYY-MM-DD [vN] <qui> : résumé (lien lore)` -->

## COMMANDS

```bash
# Aller sur la branche
cd ~/Views/upstream_mp21/linux-next && git checkout b4/ups_mp15_clk_update

# Vérifs avant envoi
b4 prep --edit-cover                        # éditer la cover / changelog
b4 prep -c                                  # (re)calculer To/Cc automatiques
b4 prep -p /tmp/ups_mp15_clk_update_out && scripts/checkpatch.pl --strict /tmp/ups_mp15_clk_update_out/*.patch
grep -m1 '^Subject:' /tmp/ups_mp15_clk_update_out/0000-*.patch   # le sujet de la cover ne doit plus contenir "Subject: [PATCH 0/3]"
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

- [ ] Corriger le titre de la cover pour la v2 : retirer le préfixe `Subject: [PATCH 0/3] ` (`b4 prep --edit-cover`) puis vérifier le sujet généré (`[PATCH v2 0/3] clk: stm32mp1: …`)
- [ ] Nettoyer le corps de la cover : puce « Patch 3 » mal indentée (`- Patch 3` sans espace initial) et espaces en fin de ligne
- [ ] Remplir le changelog v2 dans la cover (lignes EDITME) — v2 pas encore envoyable (`needs-editing`) ; y mentionner la correction du sujet de la cover
- [ ] Attendre/vérifier les retours sur la v1 (lore + Patchwork, aucun commentaire au 2026-10-26) puis intégrer les remarques dans la v2
- [ ] Après review : `b4 trailers -u`

---

[⬅ Previous](./UPSTREAM.md)
