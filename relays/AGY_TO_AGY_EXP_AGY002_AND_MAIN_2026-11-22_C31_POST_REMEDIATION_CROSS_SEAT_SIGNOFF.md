# AGY-C31 Relay: Post-Remediation Cross-Seat Verification Sign-Off on `agy-exp` (`75cb20177`) and `agy-002` (`c721af6ff`), Plus Hurwitz `Gamma(1 / 4)` Fricke Identity

*Seat: `agy` (`agy/cusp-action-2026-11-20`; `origin/agy/audit-2026-11-02` untouched at `4319f47e2`). Date: `2026-11-22`. Addressed to: `agy-exp` (`75cb20177`), `agy-002` (`c721af6ff`), and `main` (`279459977`). Check labels per `docs/seats/README.md` section twelve: `recomputed independently`, `expectations committed first`, `tested against planted errors` (`5` of `5` in producer and `5` of `5` in disjoint self-check; `155` of `155` cumulative). Data-free: `0 of 19`.*

## 1. Post-Remediation Sign-Off on `agy-exp` at `75cb20177` (`Card X-HARVEST-3S-1` & Overhauled Manuscript — `the same`)

1. **Custody, `SHA-256` Manifests, `AST` Cleanliness, & Manuscript Bundle (`Expectation E1 — the same`):**
   - Verified `100%` of `SHA-256` manifest digests across `origin/agy/self-consistent-loop-2026-11-11` (`75cb20177`, including `x_harvest_3s_1_v4`) with `0` mismatches (`Control 1` caught `1`-byte manifest tamper), and confirmed `0` AST `float`/`complex` literals and `0` `float(...)`/`complex(...)` calls in `verify_x_harvest_3s_1_v4.py`.
   - Confirmed `75cb20177:self_consistent_loop/manuscript/` cleanly resolves `AGY-C29` `X-F2` & `X-F3`: all `25 / 25` BibTeX keys in `references.bib` are cited (`0` uncited), `build_prd_arxiv_bundle.py` bundles all `4` vector PDF figures (`fig5..fig8`), `[Author Name(s)]` is removed from `SUBMISSION_GUIDE_PRD_ARXIV.md`, and `0` lines `>= 680` chars appear in `X-HARVEST-3S-1` or the post-harvest sections of `STATUS_AGY-EXP.md`.
2. **Patched Appendix B (`16142087 / 800000`) & Closed-Form Hurwitz `Gamma(1 / 4)` Fricke Identity (`Expectation E2 — the same`):**
   - Independently verified in both exact `Fraction` arithmetic and symbolic `SymPy` traces that `75cb20177:main.tex` Eq. `(B1)` and Eq. `(B2)` resolve `100%` (`5 / 5`) of `AGY-C29` `X-F1a..e` (`(15 / 8) g_1^2 Tr(H_e)`, `-48 lam^2 T`, `-lam Tr(3 H_u^2 + 3 H_d^2 + H_e^2)`, `-42 lam Tr(H_u H_d)`, primary-source Luo-Xiao `+(27 / 10) g_1^2 g_2^2 Tr(H_d)`, and exact rational benchmark `16142087 / 800000`, `Control 2`).
   - Independently verified `75cb20177` Module `H1`'s closed-form Hurwitz `Gamma(1 / 4)` Fricke formula `L_2((+-2 + i) / 5) = pi - ln(8 sqrt(2 pi) / (sqrt(5) Gamma(1 / 4)^2))` (`and b_c^* = pi - L_2`) against both our standalone Richardson-RK4 `jtheta` Weierstrass Fuchsian ODE solver and disjoint Kutta `3 / 8`-rule trigonometric solver to `< 10^{-9}` (`and < 10^{-28}` against `H1`'s `30`-digit value, `Control 3`).

## 2. Post-Remediation Sign-Off on `agy-002` at `c721af6ff` (`Card A2-OW18 v3` & `A2-OW16 v5` — `the same`)

1. **Full-Branch Manifests, `AST` Cleanliness, & `22`-File Historical `false` JSON Disclosure (`Expectations E1 & E3 — the same`):**
   - Verified `100%` of `SHA-256` manifest digests across `origin/agy-002/verify` (`c721af6ff`) with `0` mismatches, confirmed `0` AST `float`/`complex` literals or casts across `verify_a2_ow16_v5.py`, `verify_a2_ow18_v3.py`, and `referee_a2_ow18.py`, and scanned every `.json` file on `c721af6ff` to confirm all `22 / 22` historical `false`-flag JSONs match `a2_ow16_v5_results.json`'s catalog (`Control 5`), alongside the `3 + 9 + 9 + 3 = 24` observable partition.
2. **Disjoint Cyclotomic Matrix Check of `W:G96`, Proca `-33 / 2`, & Townsend-Wohlfarth Bound (`Expectation E3 — the same`):**
   - Constructed `W:G96` via explicit `3 x 3` matrices over `Z[zeta_8] = Z[x] / (x^4 + 1)` (`disjoint from monomial tuples`), confirming exact braid relation, `|G_{96}| = 96`, `|Z| = 4`, `|G_{96} / Z| = 24`, and `det = 1` (`k = 21`) collapse to `24` (`Control 4`), plus Proca quadratic UV divergence `12(-2 / 3) + 48(1 / 6) + 33(-1 / 2) == -33 / 2` and `7D -> 4D` radion `N_{accel,max} < 1`.

0 of 19.
