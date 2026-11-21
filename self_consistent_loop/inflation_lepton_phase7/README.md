# Phase 7: `7D` Radion Plateau Inflation, Kähler Baryogenesis, Adams Cusp/Schwinger Audit, `Pin_-` Lepton Closure, & Bousso–Polchinski No-Go Theorems

Clean-room two-track implementation (`Track A`: `0 of 19` pure theoretical derivations in reduced Planck units; `Track B`: explicitly priced empirical comparison boundary), AST-isolated zero-import referee (`85 / 85` cumulative planted-fault controls caught across Phases 5–7), and `unittest`/`pytest` verification suite.

## Directory Layout

- `PREREGISTRATION_PHASE7.md` & `SEAL_SHA256.txt` — Pre-registration plan, gate definitions, and SHA-256 integrity seal.
- `src/phase7_toe/p7_1_inflation_baryogenesis.py` — **Gate P7-1 (`0 of 19`):** Starobinsky $N_* = 55$ Hubble-flow benchmark, self-consistent Liddle–Leach radion plateau inflation at $V_0 = M_7^4$ ($A_s^{\mathrm{pred}} = 2.504\times 10^{-9}$, $n_s = 0.9575$, $r = 0.00061$), $f_a(R) = f_{a,0}(R_0/R)^3$ Weyl scaling, and `2`-field cylindrical Kähler Affleck–Dine ODE driven by the chiral Whitehead overtone sum $W_{\mathrm{ov}}$.
- `src/phase7_toe/p7_2_schwinger_adams_cusp.py` — **Gate P7-2 (`0 of 19`):** `50`-digit Schwinger proper-time quadrature & Contino–Pilo $\frac{1}{2}\ln\pi$ benchmark, Adams' maximal horoball volume $V_{\mathrm{horo}}(0) = \sqrt{3}$ (`A_{\mathrm{cusp}}(L_c^*)/6 = e^{-2L_c^*}/\sqrt{3}`), and `7D` $m=0$ cubic divergence vs. covering-circle circumference $L_{S^1}/R_0 = 2 L_c^*$ (`Clause P7-C2`).
- `src/phase7_toe/p7_3_lepton_pin_minus.py` — **Gate P7-3 (`0 of 19`):** Closed-form hypercharge reactor–solar sum rule $w_e^{(0)} = (c^* + a^*,\; a^* - c^*,\; -2a^*)^T / \sqrt{2(|c|^2 + 3|a|^2)}$, $A_4$ monomial preservation of diagonal Weinberg operators, and `Pin_-` odd-systole ($\chi_{\mathrm{spin}} = -1$) Shell-2 Majorana operator.
- `src/phase7_toe/p7_4_nogo_and_bp_flux.py` — **Gate P7-4 (`0 of 19`):** Symbolic `SymPy` proof of $|V_{\mathrm{bulk}}(1)| / (M_{\mathrm{Pl,red}}^2 m_{\mathrm{rad}}^2) = 5/42$, degenerate `4D` Type-I seesaw solar/atmospheric clash, and Künneth Betti audit $b_4(\overline{M^{(5)}}\times dP_9) = 21$ (`Clause P7-C4b`).
- `src/phase7_toe/phase7_engine.py` — **Composite Engine (`0 of 19`):** Verifies Phases 1–7 SHA-256 seals + Phase 5's immutable `v1` lock (`ece3d983...2edbd`) and executes Gates `P7-1` through `P7-5`.
- `src/phase7_toe/track_b_phase7_scorecard.py` — **Gate P7-5 (`Track B`):** `24`-row `v9_pin_weave` scorecard (`12` Tier-1 + `10` Tier-2 = `22 / 24` SM hits, keeping $|J_q| = 9.995\times 10^{-6}$ in `Tier 2` AND promoting $\Delta m_{21}^2/\Delta m_{31}^2 = 0.0247$ into `Tier 1`, `10`-trial `SU(3)^5` Haar check `< 1e-11`), Planck CMB & baryogenesis comparison, and Radion–BBN lower-bound audit.
- `scripts/referee_phase7.py` — AST-isolated zero-import referee executing all **`85 / 85` cumulative planted-fault controls** (`65` Phases 1–6 + `20` Phase 7).
- `outputs/` — `phase7_results.json` and `referee_phase7_verdict.json`.
- `tests/test_phase7.py` — Automated verification test suite.

## Reproducing Phase 7

```bash
cd self_consistent_loop/inflation_lepton_phase7
PYTHONPATH=src python3 -m phase7_toe.phase7_engine
python3 scripts/referee_phase7.py
python3 -m unittest discover -s tests -v
```
