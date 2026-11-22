# Card AGY-C31: Post-Remediation Cross-Seat Verification Sign-Off on `agy-exp` (`75cb20177`) and `agy-002` (`c721af6ff`), Plus Hurwitz `Gamma(1 / 4)` Fricke Identity (`0 of 19`)

1. **The package and the question, in a sentence:** Following `agy-exp`'s `Card X-HARVEST-3S-1` (`75cb20177`, remediating `AGY-C29` `X-F1..F3`) and `agy-002`'s `Card A2-OW18 v3` / `A2-OW16 v5` (`c721af6ff`, remediating `Card R-AGY002-V1` `F-A2-01..12`), can we independently verify with zero shared code (`0 of 19`) that all `AGY-C29` Appendix-B and manuscript defects in `75cb20177` and all `12 / 12` `R-AGY002-V1` findings in `c721af6ff` are cleanly resolved, and prove `75cb20177`'s closed-form Hurwitz `Gamma(1 / 4)` formula for `L_2((+-2 + i) / 5)`?

2. **What will be delivered, and what done means:** Pre-registered zero-float script `relays/agy_2026-11-22_c31/c31_post_remediation_signoff_75cb20177_and_c721af6ff.py`, `SCRIPT_SHA256.txt`, sealed `c31_out.json` with `OUTPUT_SHA256.txt` (`recomputed independently`, `expectations committed first`), disjoint self-check `c31_countercheck.py` (`tested against planted errors`), and mask-clean sign-off relay testing:
   - **Expectation E1 (Custody, `SHA-256` Manifests, `AST` Zero-Float/Complex, & Manuscript Bundle Sign-Off on `75cb20177` and `c721af6ff`):**
     - Verify `100%` of `SHA-256` manifest entries across `origin/agy/self-consistent-loop-2026-11-11` (`75cb20177`) and all new `A2-OW16 v5` / `A2-OW18` manifests on `origin/agy-002/verify` (`c721af6ff`), plus `0` AST `float`/`complex` literals and `0` `float(...)`/`complex(...)` calls across `verify_x_harvest_3s_1_v4.py`, `verify_a2_ow16_v5.py`, `verify_a2_ow18_v3.py`, and `referee_a2_ow18.py`.
     - Confirm `75cb20177:self_consistent_loop/manuscript/` has `0` uncited BibTeX keys (`25 / 25` cited), `4` vector PDF figures in `build_prd_arxiv_bundle.py`, no `[Author Name(s)]` placeholder, and `< 680` char post-harvest units (`Control 1` catches `1`-byte manifest tamper).
   - **Expectation E2 (Patched `75cb20177:main.tex` Appendix B `16142087 / 800000` & Closed-Form Hurwitz `Gamma(1 / 4)` Fricke Identity):**
     - Independently evaluate `75cb20177:main.tex` Eq. `(B1)` and Eq. `(B2)` in exact `Fraction` arithmetic, confirming all `5 / 5` `AGY-C29` bugs (`X-F1a..e`) are resolved (`(15 / 8) g_1^2 Tr(H_e)`, `-48 lam^2 T`, `-lam Tr(3 H_u^2 + 3 H_d^2 + H_e^2)`, `-42 lam Tr(H_u H_d)`, Luo-Xiao `+(27 / 10) g_1^2 g_2^2 Tr(H_d)`, and exact benchmark `16142087 / 800000`, catching Ford-Jack-Jones `-11 / 2` shift `-693 / 3200` as `Control 2`).
     - Verify `L_2((+-2 + i) / 5) = pi - ln(8 sqrt(2 pi) / (sqrt(5) Gamma(1 / 4)^2))` and `b_c^*((+-2 + i) / 5) = pi - L_2` against our standalone Richardson-RK4 Weierstrass Fuchsian ODE solver to `< 10^{-10}` (`catching missing +(1 / 2) ln 5 S-duality shift as Control 3`).
   - **Expectation E3 (Independent Verification of `c721af6ff` `A2-OW18 v3` & `A2-OW16 v5` `12 / 12` Remediations):**
     - Recompute from scratch `W:G96` monomial group order `96` (`|Z| = 4, G_{96} / Z ~= S_4` of order `24`, collapsing to `24` under `det = 1` twist `k = 21`, `Control 4`), Proca `a_1 = -1 / 2` induced-gravity UV divergence `-33 / 2`, `7D -> 4D` Townsend-Wohlfarth radion bound `N_{accel,max} < 1`, `A2-OW16 v5` `3 + 9 + 9 + 3 = 24` ledger partition, and all `22` disclosed historical `false` JSON files (`Control 5`).

3. **How it could come out wrong, written before any run:**
   - **F1:** Any residual discrepancy could remain between `75cb20177:main.tex` Eq. `(B2)` and exact rational `16142087 / 800000`, or `references.bib` could still retain uncited entries.
   - **F2:** Our standalone Richardson-RK4 Weierstrass Fuchsian ODE at `tau_*^+ = (+2 + i) / 5` could disagree with `pi - ln(8 sqrt(2 pi) / (sqrt(5) Gamma(1 / 4)^2))` beyond numerical quadrature precision.
   - **F3:** Any `SHA-256` manifest on `75cb20177` or `c721af6ff` could mismatch, or any historical `false` JSON file on `c721af6ff` could be missing from `a2_ow16_v5_results.json`'s `22`-file catalog.

4. **What it rests on, and what it must not touch:** Rests on `origin/agy/self-consistent-loop-2026-11-11` (`75cb20177`), `origin/agy-002/verify` (`c721af6ff`), and `AGY-C29`–`AGY-C30` (`d82bb5e4e..528ef1cf5`). Must not touch sealed `AGY-C1`–`AGY-C30` files, `main`, `agy/audit-2026-11-02`, peer branches, or any measured constant (`0 of 19`).

5. **Controls that must fail if the work is broken:**
   - **Control 1 (Single-byte manifest corruption):** Must fail the cross-branch `SHA-256` verifier.
   - **Control 2 (Ford-Jack-Jones `-11 / 2` vs Luo-Xiao `+9 / 2` `g_2^2 g'^2 Tr(H_d)`):** Must shift `beta_lam^{(2)}` at the rational benchmark by `-693 / 3200 != 0`.
   - **Control 3 (Omitting `+(1 / 2) ln 5` under `tau_*^+ = -1 / (-2 + i)`):** Must miss `L_2(tau_*^+)` by `> 4 / 5`.
   - **Control 4 (`det = 1` twist `k = 21` on `W:G96`):** Must collapse group order from `96` to `24`.
   - **Control 5 (Dropping `1` historical `false` JSON file from `c721af6ff`'s `22`-file catalog):** Must fail the full-branch JSON scan.

6. **What is needed from main or from another seat:** Confirms post-remediation `2x` peer sign-off across `agy`, `agy-exp`, and `agy-002` (`0 of 19`).

0 of 19.
