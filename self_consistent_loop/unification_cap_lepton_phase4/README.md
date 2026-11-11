# Phase 4: 1-Loop Vacuum Selection, 4D $dP_9$ Cusp-Cap Gluing & Quark–Lepton PMNS Unification Engine

Clean-room pre-registered mathematical-physics audit (`0 of 19` empirical inputs) testing the three open questions arising from Phases 1–3:

1. **Gate 1 (`src/phase4_loop/gate1_vacuum_selection.py`) — Unrestricted Necklace Census & 1-Loop Vacuum Selection:**
   - Exhaustive enumeration of all primitive Golden-$v_5$-preserving monodromy necklaces ($2 \le |W| \le 12$), collapsing `285` necklaces under 3D orientation-preserving and orientation-reversing isometries into `228` oriented 3-manifolds and `124` relational weak-compass classes (`20` amphicheiral, `70` chiral reversible, `34` chiral irreversible).
   - **Test 1A (Fox–Wada Reidemeister Torsion & 1-Loop Casimir/CW Audit):** Proves that on every punctured-torus bundle, the cusp-unramified ($k = 0$) $\mathbb{Z}/5\mathbb{Z}$ torsion line is non-acyclic ($\tau_{\text{Reid}} = 0$), whereas all $4$ cusp-ramified ($k \ne 0$) torsion lines are acyclic with universal cyclotomic product $\prod_{q=1}^4 \tau_{\text{Reid}}(q) = 5 = \Phi_5(1)$. Audits UV-subtracted Casimir and Coleman–Weinberg Yukawa potentials across unrestricted minimal reversible (`b++LLLRLL`, $\operatorname{Vol} = 3.2969$) vs. unrestricted minimal chiral irreversible (`b+-RRRRLRRLLR`, $\operatorname{Vol} = 7.1961$).
   - **Test 1B (Relational `A-all` Ensemble & Hyperelliptic Doublet Pairing):** Evaluates deduplicated partition sums over $\mathcal{M}_{\le 12}/\mathrm{Isom}_{\pm}$, proving exact cancellation of unbroken 4-line sums under the hyperelliptic involution $\tilde{\sigma}_{\text{hyp}}$ (`1`-bit spontaneous bundle-branch sign choice) and quantifying the spontaneous ground-state branch expectation.

2. **Gate 2 (`src/phase4_loop/gate2_dp9_cusp_cap.py`) — 4D $dP_9$ Cusp-Cap Gluing & Mod-5 Ramification Audit:**
   - Constructs $H_2(dP_9; \mathbb{Z}) \cong \mathbf{I}_{1,9}$, extracts the Mordell–Weil orthogonal sublattice $\{F, \Sigma_0\}^\perp \cong E_8(-1)$ (`240` roots, $\det = 1$), verifies the symmetric $E_8 \times E_8$ Bianchi threshold match $k_{\text{vis}} = 6 = k_{\text{inst},\min}(3)$, and audits the ’t Hooft mod-1 congruence and Friedman–Morgan–Witten spectral curve $C \in |5\Sigma_0 + 6F|$ ($g(C) = 16$, $R = 40$).

3. **Gate 3 (`src/phase4_loop/gate3_quark_lepton_unification.py`) — Quark–Lepton $SU(5)_{\text{GUT}}$ Lopsidedness & Neutrino Seesaw/Weinberg PMNS Acid Test:**
   - Verifies $E_8 \supset \mathfrak{su}(5)_{\text{GUT}} \oplus \mathfrak{su}(5)_\perp$ charge uniqueness ($Y_e = Y_d^T$ and $q(N^c) = 0$) and evaluates parameter-free CKM and PMNS observables under both 3D Kaluza–Klein singlet seesaw ($N_1$) and 3D contact Weinberg ($N_2$) mechanisms across negative controls, reversible manifolds, and chiral irreversible candidates at $N_{\text{sub}} \in \{3, 4, 5\}$.

## Directory Layout

- `PREREGISTRATION_PHASE4.md` and `SEAL_SHA256.txt` — Cryptographically sealed pre-registration contract (`7cc9965761c0497533147382e3f8ace80dd9582d1296f03abe64a09331a0b4f6`).
- `src/phase4_loop/phase4_core.py` — 14-point degree-5 tetrahedral quadrature, Epstein–Penner geometry, Smith Normal Form cohomology, Fox–Wada torsion, twisted 3D P1 FEM, bilinear Majorana / trilinear Yukawa / quartic Weinberg overlaps, and Haar $U(3)^3$ verifiers.
- `src/phase4_loop/calibration_gate.py` — Step 2 textbook calibration gate.
- `src/phase4_loop/phase4_engine.py` — Composite pipeline writing `outputs/phase4_results.json`.
- `scripts/referee_phase4.py` — AST-isolated zero-import referee countercheck (50-digit `mpmath` Fox–Wada torsion, Weyl-reflection $E_8(-1)$ builder, Keast 11-point degree-4 FEM countercheck, and 25-trial Haar $U(3)^3$ scrambling) writing `outputs/referee_phase4_verdict.json`.
- `tests/test_phase4.py` — Automated `unittest` verification suite.

## Reproduction Commands

```bash
PYTHONPATH=src python3 -m phase4_loop.calibration_gate
PYTHONPATH=src python3 -m phase4_loop.gate1_vacuum_selection
PYTHONPATH=src python3 -m phase4_loop.gate2_dp9_cusp_cap
PYTHONPATH=src python3 -m phase4_loop.gate3_quark_lepton_unification
PYTHONPATH=src python3 -m phase4_loop.phase4_engine
python3 scripts/referee_phase4.py
python3 -m unittest discover -s tests -v
```
