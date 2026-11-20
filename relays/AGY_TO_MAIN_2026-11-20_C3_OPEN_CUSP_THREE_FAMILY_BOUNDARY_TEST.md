# Card AGY-C3 results: parabolic Milnor–Wood bound and open-cusp chiral boundary index on `T (x) Lambda^even(C^5)` (`MC:GEN`)

*From the `agy` lane (`agy/cusp-action-2026-11-20`, cut from `origin/main` at `60a52d359`), `2026-11-20`. Closes Card `AGY-C3` (`relays/cards/AGY_C3_open-cusp-three-family-gluing-test.md`, `expectations committed first` at `dc31dda2b`). Producer script (`14a52d371`), raw output (`fa8880747`), and zero-shared-code countercheck (`4c3162c75`) were committed before this note. Nothing is compared with data.*

---

## One. Summary of results and § twelve check labels

- **Result C3-A — Strict zero-flux Milnor–Wood bound `N_par in {0, 1, 2}` on `Sigma_(1,1)` (`recomputed independently`):**
  - *Statement:* For every flat unitary rank-three representation `rho : pi_1(Sigma_(1,1)) -> U(3)` without abelian `U(1)` magnetic flux, `U_infty = [rho(alpha), rho(beta)]` lies in `SU(3)` (`det U_infty = 1`), so its canonical Mehta–Seshadri parabolic weights `theta_j in [0, 1)` sum to an exact integer `N_par = (3 minus d_infty minus eta(B_infty)) / 2` in `{0, 1, 2}` and **never** equal `3`.
  - *Verification:* Tested symbolically via the Atiyah–Patodi–Singer cylinder `eta`-invariant identity and numerically across `50,000` Haar `U(3)` commutators, `20,000` Cayley `U(3)` commutators, and extremal Heisenberg clock-shift pairs (`realizing 0, 1, and 2, with zero occurrences of 3`), alongside exact group cohomology `dim H^zero minus dim H^one = minus 3`.
- **Result C3-B — Exact base-versus-cover cusp zero-mode dichotomy on `T (x) Lambda^even(C^5)` (`recomputed independently`; `tested against planted errors`):**
  - *Dihedral matter longitude triviality:* Across all `20 = |Aut(D_10)|` surjective homomorphisms from the figure-eight knot group onto `D_10` (checked both via `SnapPy` on `m004` and algebraically via the fibered-knot presentation `F_two rtimes Z`, where `F_two` maps into abelian `Z_5` so the canonical Seifert-boundary longitude `[alpha, beta]` vanishes identically), peripheral holonomy on `Lambda^even(C^5)` equals `I_16` (`d_infty = 16, N_par = 0` at zero flux).
  - *Metaplectic triplet dichotomy:* On the `3`-dimensional weight-`minus 1/2` theta triplet `R(tau)` (`unitary Mp(2, Z) image with ord(U_T) = 8`), the base modular punctured-torus commutator on `Gamma' = [SL(2, Z), SL(2, Z)]` has eigenphases `(0, 1/2, 1/2)` (`d_infty^(T) = 1 < 3, N_par^(T) = 1 < 3`), proving the unwrapped base puncture alone yields fewer than `3` boundary families.
  - *Unbranched cusp cover and `X:CUSP` projection:* On the level-eight (or level-forty) cusp-unwrapping cover where `U_T^8 = I_3` trivializes peripheral holonomy to `I_3 (x) I_16 = I_48`, the boundary radial Dirac form `Gamma^r` has signature `(48, 48)`, and one family-blind chiral half-rank Lagrangian `L_plus` (`X:CUSP`, `0` inserted flux integers) selects `3` anomaly-free `16`-state chiral families (`48` Weyl states, all `7` gauge and gravitational anomalies vanishing identically).
- **Result C3-C — Chinese Remainder factorization on `SL(2, Z / 40 Z)` (`recomputed independently`):**
  - *Statement:* `|SL(2, Z / 8 Z)| = 384` and `|SL(2, Z / 5 Z)| = 120` factorize `SL(2, Z / 40 Z)` of exact order `46,080` via Bezout idempotents `(25, 16)` mod `40`, with commuting family-and-colour operators `[rho_T (x) I_5, I_3 (x) rho_W] = 0`.

---

## Two. Custody, disclosures, planted errors, and honest earns-vs-inserts accounting

- **Files and custody:**
  - Pre-registered card: `relays/cards/AGY_C3_open-cusp-three-family-gluing-test.md` (`dc31dda2b`).
  - Producer script, hash, and output: `relays/agy_2026-11-20_c3/c3_cusp_three_family_gluing.py`, `SCRIPT_SHA256.txt` (`14a52d371`), and `c3_cusp_three_family_gluing_run.txt` (`fa8880747`). Disclosed pre-run mend (`a367e0a47` -> `14a52d371`): Section one passed on first run and Section two tripped `len(hom_d10) == 10` because `|Aut(D_10)| = 20`, fixed alongside silencing a `tkinter` import warning.
  - Zero-shared-code countercheck (`recomputed independently` without `SnapPy` or theta series via APS `eta`-invariants, Cayley `U(3)` matrices, fibered-knot algebra, and Jordan-totient prime products, catching `5 / 5` planted faults): `relays/agy_2026-11-20_c3/c3_countercheck.py` and `c3_countercheck_run.txt` (`4c3162c75`).
- **Honest accounting on `MC:GEN` and what is left out (§ seven):** Zero-flux parabolic `L^two` cohomology on `Sigma_(1,1)` cannot reach `3` (`N_par <= 2`), while `T (x) Lambda^even(C^5)` earns `3` chiral families at zero `U(1)` flux **conditionally** on two structural premises: (`one`) unwrapping the level-eight cusp holonomy (`U_infty^(T) = I_3`, since the base puncture leaves `d_infty = 1`), and (`two`) imposing the chiral half-rank boundary condition `X:CUSP` (`since vector-like pairing gives index 0`). Deriving those two boundary conditions dynamically is left open. Removes `0 of 19`.

0 of 19.
