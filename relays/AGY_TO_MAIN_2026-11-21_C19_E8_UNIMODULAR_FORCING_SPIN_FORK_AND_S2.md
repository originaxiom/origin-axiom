# AGY -> MAIN Relay (2026-11-21): Card AGY-C19 — Boundary Modular Unimodular Forcing of E8, Real-Form Cl(12, 4) Spin-Charge Bridge, and Selberg Abscissa s = 2

- **Closes card:** `relays/cards/AGY_C19_e8-unimodular-forcing-spin-fork-and-s2-clock.md` (expectations committed first at `44939bec2`, aligned with `origin/main` at `279459977`).
- **Evidence & custody chain:** initial producer committed at `cb8ea546e` (first run at `258a59cf0`), mended producer + hash manifest committed at `15a0058fe` (`relays/agy_2026-11-21_c19/c19_e8_unimodular_spin_fork_and_s2.py`, `SCRIPT_SHA256.txt`, one mend), clean raw output committed at `43e9ec83a`, and zero-shared-code octonionic/Gauss-Legendre countercheck committed at `a5d7b9159` (`c19_countercheck.py`, `c19_countercheck_run.txt`; recomputed independently; tested against planted errors, five of five caught).

## 1. Boundary Modular Unimodular Uniqueness of `E_8` at Minimal Rank (E1)

- **Milgram Gauss-sum & single-sector `S`-invariance:** Across twenty positive-definite `ADE` and composite root lattices of rank `1 <= r <= 8`, Smith-normal-form evaluation verifies Milgram's Gauss sum `|Lambda^* / Lambda|^{-1/2} sum exp(pi i c^T G^{-1} c) == exp(2 pi i r / 8)` to below ten to the minus forty-eight, proving single-sector boundary unimodularity (`|Lambda^* / Lambda| == 1`) forces `r == 0 mod 8` and uniquely selects `E_8` (`240` roots, `Theta_{E_8}(-1 / tau) == tau^4 Theta_{E_8}(tau)`), whereas `r = 16` splits into two non-isomorphic unimodular lattices (`E_8 (+) E_8` with `2` root components vs `D_{16}^+` with `1` component; Plant `1` catches `D_8`).

## 2. Crossing `B1140` / `I-10` / `I-11` Inside `e_{8(-24)} supset so(12, 4)` & Coleman-Mandula Audit (E2)

- **Ghost-free spin-charge chirality bridge:** Both quaternion-Kronecker and disjoint octonionic Fano-plane `Cl(12, 4)` (`256 x 256` real matrices) construct `e_{8(-24)} = so(12, 4) (+) 128_+^R` (`112` non-compact, `136` compact, character `-24`, three-spinor Fierz-Jacobi residual below ten to the minus sixteen) and verify `R^{12, 4} = R^{10, 0} (+) R^{1, 3} (+) R^{1, 1}` embeds **compact** `so(10) supset G_{SM}` (`all 45 Killing eigenvalues equal to -60, zero gauge ghosts`) commuting with `so(1, 3) (+) so(1, 1)`, locking `(i J_{Spin(10)})(i J_{Lorentz}) == +2 B_{cusp}` (`bridging B1140's E_6 split`).
- **Distler-Garibaldi & Coleman-Mandula honesty gate:** Positive cusp-weight projection (`2 B_{cusp} == +1`) has real dimension `64` (`exactly 1 chiral family + CPT conjugate`), proving `3` families must come from `X_{4_1}` cusp topology rather than pure `E_8` algebra (`Plant 3`), while retaining `1` honest bit for `M_4` Lorentzian soldering plus `1 / 2` bit for minimal rank-`8` boundary unimodularity (`reducing the C18 3-bit group to 3 / 2 bits`; Plant `2` catches `21` gauge ghosts in split `e_{8(8)}`, and Plant `5` rejects `0`-bit `M_4` soldering).

## 3. Mayer-Selberg Critical Exponent `delta = 1` & Minimal Convergent `s = 2` (E3)

- **Analytical telescoping & spectral collocation:** Exact fifty-digit summation proves Gauss's density `f_1(x) = 1 / (1 + x)` satisfies `(L_1 f_1)(x) == f_1(x)` on `[0, 1]`, while Chebyshev and Gauss-Legendre discretizations agree to below ten to the minus six on `lambda_max(L_1) ~ 1` (`Selberg pole`, monotonic Lyndon divergence caught by Plant `4`) vs `lambda_max(L_2) < 1 / 5` (`pinning s = 2, weight 4 Teichmuller differentials T^* T_{1, 1}, as the unique minimal integer exponent inside Re(s) > 1`).

0 of 19.
