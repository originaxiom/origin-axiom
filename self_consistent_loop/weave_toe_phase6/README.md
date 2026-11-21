# Phase 6: Coherent Whitehead Weave, Zero-Anchor Scales, `11D` Hořava–Witten Parent, & Cosmological Closure

Clean-room two-track implementation (`Track A`: `0 of 19` pure theoretical derivations in reduced Planck units; `Track B`: explicitly priced empirical comparison boundary), AST-isolated zero-import referee (`65 / 65` cumulative planted-fault controls caught across Phases 5–6), and `unittest`/`pytest` verification suite.

## Directory Layout

- `PREREGISTRATION_PHASE6.md` & `SEAL_SHA256.txt` — Pre-registration plan, gate definitions, and SHA-256 integrity seal.
- `src/phase6_toe/w1_whitehead_weave.py` — **Gate P6-1 (`0 of 19`):** Chiral `1`-octahedron Whitehead parent link `m129` ($\operatorname{Vol} = 4G = 3.663862\dots$, $\mathrm{CS} = +1/8$), $\mathbb{F}_3 \times \mathbb{F}_5$ mirror-slope exclusion, coordinate-invariant Ford horoball ratio $\hat{z}_{\mathrm{ap}}(\gamma)$, IR-localized same-bundle overtone tower $p \equiv -3q \pmod{10}$, and amphicheiral Shell-1 leptogenesis vanishing.
- `src/phase6_toe/w2_zero_anchor_hosotani.py` — **Gate P6-2 (`0 of 19`):** Zero-anchor `Spin(11)` NDA coupling at round-trip collar cutoff $\Lambda_7 R_0 = 2 L_c^*$ ($\alpha_{\mathrm{GUT},0}^{-1} = 43.2464$), collar/Weyl Planck hierarchy ($M_{\mathrm{KK}}/M_{\mathrm{Pl,red}} = e^{-2L_c^*}/\sqrt{3}$, $v_{\mathrm{EW}}/M_{\mathrm{Pl,red}} = e^{-(19/2)L_c^*}/\sqrt{3}$), self-consistent `2`-loop RGE IR fixed point, and `1`-loop Hosotani radiative EWSB ($\frac{9}{4}g_2^2 - 3 y_t^2 < 0$).
- `src/phase6_toe/w3_horava_witten_11d.py` — **Gate P6-3 (`0 of 19`):** `11D` Hořava–Witten parent $\mathbb{R}^{1,3} \times M_3 \times dP_9$ ($4 + 3 + 4 = 11$), `10D` wall $I_{12}$ selection of $\dim G_{\mathrm{wall}} = 248$ (`E_8`), $dP_9$ Bianchi identity ($n_{\mathrm{M5}} = 0, N_{\mathrm{gen}} = 3$), `SymPy` cancellation of all local + $[B-L]^3$ + Witten $\mathrm{SU}(2)_L$ + Dai–Freed anomalies, and KK graviton unitarity ($M_7 = 2 L_c^* M_{\mathrm{KK}}$).
- `src/phase6_toe/w4_cosmology_dark_sector.py` — **Gate P6-4 (`0 of 19`):** Planck-normalized Svrček–Witten $C_3$ axion decay constant ($f_a / M_{\mathrm{Pl,red}}$), UV vs. IR neutrino Casimir densities, canonical stabilized radion mass & reheating ratios, and dynamical strong-CP relaxation ($\partial_\alpha V_{\mathrm{QCD}} = 0$, `< 1e-12`).
- `src/phase6_toe/phase6_engine.py` — **Composite Engine (`0 of 19`):** Verifies Phases 1–6 SHA-256 seals + Phase 5's immutable `v1` lock (`ece3d983...2edbd`) and executes Gates `P6-1` through `P6-5`.
- `src/phase6_toe/track_b_toe_scorecard.py` — **Gate P6-5 (`Track B`):** `24`-row `v8_weave` scorecard (`22 / 24` hits, $|J_q| = 9.995\times 10^{-6}$ promoted to `Tier 2`, `10`-trial `SU(3)^5` Haar check `< 1e-11`), `50`-digit Takagi/CRV + Buchmüller–Di Bari–Plümacher leptogenesis bound, zero-anchor gauge/Planck comparison, and cosmological/BBN audit.
- `scripts/referee_phase6.py` — AST-isolated zero-import referee executing all **`65 / 65` cumulative planted-fault controls** (`45` Phase-5 + `20` Phase-6).
- `outputs/` — `phase6_results.json` and `referee_phase6_verdict.json`.
- `tests/test_phase6.py` — Automated verification test suite.

## Reproducing Phase 6

```bash
cd self_consistent_loop/weave_toe_phase6
PYTHONPATH=src python3 -m phase6_toe.phase6_engine
python3 scripts/referee_phase6.py
python3 -m unittest discover -s tests -v
```
