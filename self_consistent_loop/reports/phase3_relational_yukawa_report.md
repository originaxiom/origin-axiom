# Phase 3 Report: Relational Weak-Compass Quotient, Spin-Flux Palindrome Theorem, 3D Hyperbolic Yukawa Overlaps & Tadpole Audit

> [!IMPORTANT]
> **Clean-Room Execution & Zero-Trust Referee Verdict (`EXIT CODE 0`, `0 of 19` Empirical Inputs)**
> Built in `self_consistent_loop/relational_yukawa_phase3` with **zero modifications** to `origin-axiom*`, Phase 1 (`self_consistent_loop_phi`, SHA-256 `d42cedad...`), or Phase 2 (`cusped_3d_loop_phase2`, SHA-256 `d92bec85...`). All equations, calibration gates, falsifiers, and negative controls were pre-registered in [PREREGISTRATION_PHASE3.md](../relational_yukawa_phase3/PREREGISTRATION_PHASE3.md) and sealed in [SEAL_SHA256.txt](../relational_yukawa_phase3/SEAL_SHA256.txt) (`64039873eb88506cefb788a2ca0ba8a2e9578e0a45f91476aa7a94b1536cd48a`) prior to solver implementation. Both [phase3_engine.py](../relational_yukawa_phase3/src/relational_loop/phase3_engine.py) and the AST-verified zero-import referee [referee_relational_phase3.py](../relational_yukawa_phase3/scripts/referee_relational_phase3.py) (`8/8` tests in [test_relational_phase3.py](../relational_yukawa_phase3/tests/test_relational_phase3.py)) passed with exit code `0`.

---

## 1. Executive Scorecard: What Closed vs. What Was Falsified

```mermaid
flowchart TD
    Seal["Pre-Registered SHA-256 Seal (0 of 19 Empirical Firewall)"] --> Cal["Step 2: Textbook Calibration Gate (PASS < 1e-12)"]
    Cal --> G1["Gate 1: Relational Weak-Compass Quotient — CLOSED (1-Bit Mirror Tie Eliminated)"]
    Cal --> G2["Gate 2: Coupled Spin-Flux on (6) — FALSIFIED as Tie-Breaker (Klein-Four Theorem Confirmed)"]
    Cal --> G3["Gate 3: 3D Hyperbolic Yukawa & Jarlskog CP — (6) FALSIFIED (J=0); Irreversible [5,1,2,2] BREAKTHROUGH (J != 0)"]
    Cal --> G4["Gate 4: Unrigged E8 Tadpole — 2D/3D Alone FALSIFIED; 4D dP9 Cusp-Cap Bianchi MATCHES k_min(3) = 6"]
    G1 --> Ref["Zero-Import Referee (Keast-5 45-Tet Cover + mpmath50 + 25-Trial Haar: PASS)"]
    G2 --> Ref
    G3 --> Ref
    G4 --> Ref
```

| Phase 3 Gate / Audit | Core Mathematical Question | Unvarnished Verdict | Key Quantitative Evidence |
| :--- | :--- | :--- | :--- |
| **Step 2: Calibration** ([calibration_gate.py](../relational_yukawa_phase3/src/relational_loop/calibration_gate.py)) | Do 14-pt deg-5 tetrahedral quadrature, 10-tet 5-fold cover $\mathbb{Z}/5\mathbb{Z}$ selection rules, Hodge harmonic 1-forms, and Haar $U(3)^3$ extractors hit textbook precision? | **PASSED** | Deg-5 monomial err `2.78e-17`; `m004` Penner vol err `3.11e-15`; 10-tet cover forbidden $\mathbb{Z}/5\mathbb{Z}$ overlap `1.89e-15`; allowed `5x` match `4.00e-15`; harmonic co-closure `4.44e-16`; Haar err `1.22e-15`. |
| **Gate 1: Relational Quotient** ([gate1_relational_quotient.py](../relational_yukawa_phase3/src/relational_loop/gate1_relational_quotient.py)) | Does anchoring observables to the active light weak boson ($\sigma_P = -\operatorname{sgn}\sin 4\pi\operatorname{CS}$) eliminate the external 1-bit enantiomer tie? | **CLOSED** | Enantiomer diff `0.0` (`mpmath` 50-digit err `0.0`) across all 9 chiral pairs; unique `1`-element `A-one` quotient winner `[(6)]_rel`; `A-all` $\langle\tau_{\text{cusp,rel}}\rangle = -0.24785 + 1.30192i$ (vs. unquotiented `0`); amphicheiral controls `b+-LR` & `(5,5)` give exact `0.0`. |
| **Gate 2: Spin-Flux Throat** ([gate2_coupled_spin_flux_throat.py](../relational_yukawa_phase3/src/relational_loop/gate2_coupled_spin_flux_throat.py)) | Does coupling 2-component spin + continuous harmonic flux $\Phi_{\text{base}}\alpha_s$ break `(6)`'s symmetric `[0, 6]` shoulder tie? | **`(6)` TIE PROTECTED; `[5,1,2,2]` BREAKS** | On `(6)` (`Sym = Z/2 x Z/2`), anti-unitary $\tilde{\iota}_1$ locks $P_0 = P_6, P_7 = P_8$ to `5.55e-16` (Referee Keast-5: `6.94e-17`) even for irrational flux! Breaking time-reversibility on chiral `[5,1,2,2]` (`Sym = Z/2`) yields a single asymmetric peak (`gap = +0.0255`). |
| **Gate 3: 3D Yukawa & CP** ([gate3_3d_yukawa_overlap.py](../relational_yukawa_phase3/src/relational_loop/gate3_3d_yukawa_overlap.py)) | Do parameter-free 3D hyperbolic trilinear overlaps $(Y_u, Y_d)$ produce 3 distinct masses, full CKM mixing, and $\hat{\mathcal{J}} \ne 0$? | **`(6)` FALSIFIED FOR CP; `[5,1,2,2]` SUCCEEDS** | **1.** `k=0` (`UNRAM`): $|\hat{\mathcal{J}}| \le 3.24\times 10^{-18}$ on **all 9** manifolds, and `(6)` has `4` exact CKM zeros ($2 \oplus 1$ family decoupling).<br>**2.** `k!=0` (`RAM`) on Klein-four `(6)`, `[3,1,3]`, `[1,2,2,2]`: $|\hat{\mathcal{J}}| \le 3.07\times 10^{-18}$ (`0` CP!).<br>**3.** `k!=0` (`RAM`) on irreversible `[5,1,2,2]`: **$|\hat{\mathcal{J}}| = 9.45\times 10^{-5}$** (`N_sub=4`) / **$3.53\times 10^{-5}$** (`N_sub=5`), 9/9 graded CKM mixing, 3 hierarchical masses, and enantiomer reversal to `5.08e-19`! |
| **Gate 4: Topological Tadpole** ([gate4_topological_tadpole_audit.py](../relational_yukawa_phase3/src/relational_loop/gate4_topological_tadpole_audit.py)) | Does pure 2D/3D topology force the 3-generation $E_8$ flux norm $\|H\|^2 = 12$ ($k_{\text{inst}} = 6$) without rigged multipliers? | **2D/3D ALONE SHORT; 4D $dP_9$ CAP EXACT** | Exhaustive $E_8$ coroot theorem proves $k_{\text{inst},\min}(N) = \frac{N(N+1)}{2} = 1, 3, 6, 10$. Pure 2D $|\chi(\Sigma_{1,1})|=1 \implies N\le 1$; 3D Dedekind $|\Phi((6))|=5 \implies N\le 2$, $|\Phi([5,1,2,2])|=4 \implies N\le 2$; 4D rational-elliptic cusp cap $dP_9 = \frac{1}{2}K3$ ($\chi=12$, symmetric split $6+6$) hits $k_{\text{vis}} = 6 \equiv k_{\text{inst},\min}(3)$ exactly. |

---

## 2. Plain-English Synthesis: What Every Gate Taught Us

1. **The External 1-Bit Mirror Tie Is Completely Resolved (Gate 1):**
   In Phase 2, chiral histories came in left/right mirror pairs (`LLLLLLRLR` vs. `LRRRRRRLR`) with identical volumes, opposite Chern–Simons parity, and opposite $\operatorname{Re}\tau$. Gate 1 proves that an observer inside the universe defines "left-handed" relative to whichever $SU(2)$ weak gauge boson is light in their own vacuum ($\sigma_P = -\operatorname{sgn}\sin 4\pi\operatorname{CS}$). Once observables are referenced to that internal weak compass, **both mirror universes predict the exact same numbers to machine zero (`0.0`)** — turning `A-one`'s 2-way tie into a unique `1`-class winner and preventing `A-all`'s partition sum from averaging parity and CP phases to zero.
2. **Why Minimal-Volume `(6)` Cannot Be Our Flavor Vacuum (Gates 2 & 3):**
   Testing `(6)` (`b++LLLLLLRLR`, $\operatorname{Vol} = 5.5864$) under genuine 3D spin-flux and trilinear Yukawa integrals exposed a rigid mathematical wall: its Klein-four isometry group $\operatorname{Sym}(\text{`b++LLLLLLRLR`}) \cong \mathbb{Z}_2 \times \mathbb{Z}_2$ contains **both** a spatial throat reflection $\iota_2$ and an orientation-preserving time-reversing involution $\iota_1$ ($W \sim W^{-1}$).
   - In **Gate 2**, the anti-unitary symmetry $\tilde{\iota}_1 = \mathcal{K} \circ \iota_1^*$ simultaneously conjugates $\mathbb{Z}/5\mathbb{Z}$ phases and negates the base harmonic 1-form $\alpha_s$, locking the two shoulders $P_0 = P_6$ (`5.55e-16`) even when 2-component Pauli spin and irrational magnetic flux are turned on.
   - In **Gate 3**, under cusp-unramified (`k = 0`) $\mathbb{Z}/5\mathbb{Z}$ torsion, `(6)` produces 3 non-zero quark masses (`rank = 3`), **but** $\iota_2$-parity forces an exact **$2 \oplus 1$ block-diagonal CKM matrix** (`4` entries equal to `0` to `< 1e-13`, completely decoupling one family from weak CKM mixing!) and forces Jarlskog CP violation to vanish (`3.24e-18`). Even when cusp ramification (`k != 0`) breaks $\iota_2$ and populates all 9 CKM entries, $\tilde{\iota}_1$ **still** forces $\hat{\mathcal{J}} = 0$ (`3.07e-18`), while tunnel splitting across the symmetric throat creates a nearly degenerate heavy quark doublet ($s_{u,2}/s_{u,3} = 0.978$–$0.99986$).
3. **The Irreversible Chiral Breakthrough on `[5, 1, 2, 2]` (Gates 2 & 3):**
   Asking *what minimal topological geometry eliminates every anti-unitary involution* led directly to the minimal-volume **time-irreversible chiral Golden-extending pair** `[5, 1, 2, 2]` (`b++LLLLLRLLRRLR`) and its Fibonacci mirror (`b++LRRRRRLRRLLR`), where $\operatorname{Sym}(M) \cong \mathbb{Z}_2$ (purely the fiber hyperelliptic involution $\sigma_{\text{hyp}}$, with $W \not\sim W^{-1}$ and $\operatorname{Vol} = 9.068710$):
   - When combined with a **cusp-ramified** ($k \not\equiv 0 \pmod 5$) $\mathbb{Z}/5\mathbb{Z}$ bundle (whose non-trivial peripheral holonomy breaks $\tilde{\sigma}_{\text{hyp}}$ while $W \not\sim W^{-1}$ eliminates $\tilde{\iota}_1$), **parameter-free 3D geometric CP violation switches on automatically**: $|\hat{\mathcal{J}}|_{\max} = 9.45 \times 10^{-5}$ at $N_{\text{sub}}=4$ (Referee Keast-5: $9.40 \times 10^{-5}$, `0.52%` agreement) and $3.53 \times 10^{-5}$ at $N_{\text{sub}}=5$.
   - Simultaneously, the single-peaked asymmetric throat (`Gate 2` peak at `t = 7`, gap `+0.0255`) lifts `(6)`'s heavy tunnel doublet into **three genuinely hierarchical generations** (`0.0267 : 0.4259 : 1.0` in up-sector; `0.0518 : 0.4993 : 1.0` in down-sector at $N_{\text{sub}}=5$) and produces a **graded 3-family CKM matrix** with near-unit diagonal (`[0.958, 0.949, 0.988]`) and ordered off-diagonal hierarchy (`0.285 > 0.152 > 0.0346`) — with `0 of 19` empirical parameters!
   - Crucially, on the mirror manifold `b++LRRRRRLRRLLR`, $\hat{\mathcal{J}}$ flips sign to `5.08e-19` precision, so the **relational Jarlskog invariant** $\hat{\mathcal{J}}_{\text{rel}} = \sigma_P(M_W)\,\hat{\mathcal{J}}(M_W)$ is strictly identical across enantiomers!
4. **Honest Accounting of the 3-Generation Flux Number (Gate 4):**
   Exhaustive enumeration over all `2,310` $\mathfrak{su}(5)_{\text{GUT}}$-commuting $E_8$ coroots up to $\|H\|^2 \le 32$ proved an exact Diophantine theorem: achieving $|N_{\text{gen}}| = N$ in a $\mathbb{Z}/5\mathbb{Z}$-projected $\mathbf{5}_\perp$ slot requires minimal $E_8$ instanton number $k_{\text{inst},\min}(N) = \frac{N(N+1)}{2} = 1, 3, 6, 10$ for $N = 1, 2, 3, 4$. Pure 2D fiber Euler characteristic ($|\chi(\Sigma_{1,1})| = 1 \implies N \le 1$) and pure 3D Rademacher–Dedekind monodromy framing ($|\Phi((6))| = 5 \implies N \le 2$, $|\Phi([5,1,2,2])| = 4 \implies N \le 2$) **cannot** reach $k_{\text{inst}} = 6$ on minimal manifolds without ad-hoc multipliers. By contrast, capping the torus cusp with a standard 4D rational elliptic surface ($dP_9 = \frac{1}{2}K3$, $\chi(dP_9) = 12$) under the symmetric $E_8 \times E_8$ Bianchi split $12 = 6 + 6$ gives $k_{\text{vis}} = 6 = k_{\text{inst},\min}(3)$ on the nose.

---

## 3. Exact Mathematical Results by Gate

### 3.1 Gate 1: Relational Weak-Compass Quotient
For any oriented cusped hyperbolic manifold $M_W$, define the internal weak-parity sign:
$$\sigma_P(M_W) := \begin{cases} -\operatorname{sgn}\bigl(\sin(4\pi \operatorname{CS}(M_W))\bigr), & |\sin(4\pi \operatorname{CS}(M_W))| > 10^{-10}, \\ 0, & \text{otherwise (amphicheiral)}, \end{cases}$$
and the relational modular readout in the Gauss fundamental domain $\mathcal{F}$:
$$\tau_{\text{rel}}(M_W) := \bigl(\sigma_P(M_W)\operatorname{Re}\tau_{\mathcal{F}}(M_W)\bigr) + i\operatorname{Im}\tau_{\mathcal{F}}(M_W), \qquad \Delta m^2_{\text{weak,rel}}(M_W) := m^2(W_{\text{heavy}}) - m^2(W_{\text{active}}).$$

- **Algebraic Fibonacci Mirror Preservation:** Conjugating $\overline{W}$ (`L <-> R`) by $A_{\text{fib}} = \begin{pmatrix} 1 & 1 \\ 1 & 0 \end{pmatrix}$ ($\det A_{\text{fib}} = -1$) satisfies $A_{\text{fib}}^T v_5 \equiv 3 v_5 \pmod 5$ for $v_5 = (1, 2)^T$, mapping every Golden-extending word $W$ bijectively to its opposite-orientation enantiomer $W_{\text{mirror}} = L\overline{W}L^{-1}$ with identical $\mathbb{Z}/5\mathbb{Z}$ extension sign.
- **Exact Enantiomer Collapse (`9` Chiral Pairs):** Across all 8 chiral pairs of the mirror-closed `A6` family plus `[5,1,2,2]` / `[1,5,2,2]`:
  - $\max |\tau_{\text{cusp,rel}}(M_W) - \tau_{\text{cusp,rel}}(M_{W_{\text{mirror}}})| = 0.0$,
  - $\max |\tau_{\text{tube,rel}}(M_W) - \tau_{\text{tube,rel}}(M_{W_{\text{mirror}}})| = 0.0$,
  - $\max |\Delta m^2_{\text{weak,rel}}(M_W) - \Delta m^2_{\text{weak,rel}}(M_{W_{\text{mirror}}})| = 0.0$ (Haar $U(16)$ basis-scrambling error `2.22e-15`).
- **`A-one` vs. `A-all` Readouts:**
  - `A-one` unique quotient winner `[(6)]_rel` ($\operatorname{Vol} = 5.58636161$): $\tau_{\text{cusp,rel}} = -0.29022091 + 1.36715021i$, $\tau_{\text{tube,rel}} = +0.43826166 + 1.71438199i$.
  - Irreversible chiral quotient class `[[5,1,2,2]]_rel` ($\operatorname{Vol} = 9.06871006$): $\tau_{\text{cusp,rel}} = -0.28852952 + 1.06646638i$, $\tau_{\text{tube,rel}} = +0.40253589 + 1.69193246i$.
  - `A-all` Boltzmann average ($w_i \propto e^{-\operatorname{Vol}_i}$): $\langle\tau_{\text{cusp,rel}}\rangle = -0.24785289 + 1.30192085i$ (whereas unquotiented `A-all` cancels $\operatorname{Re}\tau$ identically to `0.0`).

### 3.2 Gate 3: Three-Tier 3D Hyperbolic Yukawa & Jarlskog CP Theorem
Using positive-weight 14-point degree-5 quadrature on $S_4$-symmetric Eulerian subdivisions ($N_{\text{sub}} \in \{3, 4, 5\}$), we evaluated the $\mathbb{Z}/5\mathbb{Z}$-invariant $E_8 \supset \mathfrak{su}(5)_{\text{GUT}} \oplus \mathfrak{su}(5)_\perp$ trilinear overlaps $(Y_u)_{ab} = \int_{M_H}\sqrt{\det g}\,\psi_{+1}^{(a)}\psi_{+1}^{(b)}\phi_{-2}^{(0)}\,d^3x$ and $(Y_d)_{ab} = \int_{M_H}\sqrt{\det g}\,\psi_{+1}^{(a)}\chi_{+2}^{(b)}\phi_{+2}^{(0)}\,d^3x$, extracting singular-value ratios, $|V_{\text{CKM}}| = |U_{L,u}^\dagger U_{L,d}|$, and the normalized Jarlskog commutator invariant:
$$\hat{\mathcal{J}}(Y_u, Y_d) := \frac{\operatorname{Im}\det[Y_u Y_u^\dagger,\, Y_d Y_d^\dagger]}{\|Y_u Y_u^\dagger\|_F^3 \, \|Y_d Y_d^\dagger\|_F^3},$$
verified invariant under independent random Haar $U(3)^3$ rotations (`max_err = 3.92e-13 < 1e-12`) and random eigensolver $U(1)$ mode phases (`max_err = 2.88e-13 < 1e-12`):

| Tier & Bundle Regime | Representative Manifold(s) | Up Ratios $(s_1/s_3, s_2/s_3)$ | Down Ratios $(s_1/s_3, s_2/s_3)$ | CKM Structure $|V_{\text{CKM}}|$ | Normalized Jarlskog $|\hat{\mathcal{J}}|$ |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Tier 1:** Cusp-Unramified (`k=0`, Neumann) | `(6)` `b++LLLLLLRLR` ($N_{\text{sub}}=4$, & all 9 manifolds) | `(0.0340, 0.7947)` (`rank=3`) | `(0.5969, 0.6410)` (`rank=3`) | **`4` exact zeros** (`< 3.4e-14`), $2 \oplus 1$ block-decoupled | **`<= 3.24e-18` (ZERO on all 9)** |
| **Tier 2:** Cusp-Ramified (`k!=0`, Dirichlet) on Reversible Klein-Four | `(6)`, `(1,6)`, `[3,1,3]`, `[1,2,2,2]` ($N_{\text{sub}}=4$) | `(0.0202, 0.9784)` on `(6)` `ram0` (heavy doublet!) | `(0.1624, 0.3774)` on `(6)` `ram0` | `9/9` non-zero, **realizable in real basis** via $\tilde{\iota}_1$ | **`<= 3.07e-18` (ZERO on all Klein-4)** |
| **Tier 3:** Cusp-Ramified (`k!=0`, Dirichlet) on Irreversible Chiral (`Sym = Z/2`) | `[5,1,2,2]` `b++LLLLLRLLRRLR` (`ram0`, $N_{\text{sub}}=5$) | **`(0.0267, 0.4259)`** (`rank=3`, hierarchical) | **`(0.0518, 0.4993)`** (`rank=3`, hierarchical) | Diag `[0.958, 0.949, 0.988]`; off-diag **`0.285 > 0.152 > 0.0346`** | **`3.53e-5`** (`N_sub=5` max), **`9.45e-5`** (`N_sub=4` max); mirror sum **`5.08e-19`** |

> [!TIP]
> **Why Both Ingredients Are Necessary for Geometric CP Violation:**
> Turning on **irreversibility alone** (`[5,1,2,2]` at `k = 0`) still gives $|\hat{\mathcal{J}}| = 1.6 \times 10^{-19}$ because $\tilde{\sigma}_{\text{hyp}}$ makes all modes real; turning on **cusp ramification alone** on reversible `(6)` or `[3,1,3]` (`k != 0`) still gives $|\hat{\mathcal{J}}| \le 3.07 \times 10^{-18}$ because $\tilde{\iota}_1$ survives. Only the **joint topological intersection** (`k != 0` peripheral $\mathbb{Z}/5\mathbb{Z}$ holonomy **+** time-irreversible monodromy $W \not\sim W^{-1}$) breaks every anti-unitary involution and unlocks $\hat{\mathcal{J}} \ne 0$.

---

## 4. Independent Zero-Import Referee Certification ([referee_relational_phase3.py](../relational_yukawa_phase3/scripts/referee_relational_phase3.py))

Executed in a clean subprocess stripped of `PYTHONPATH` ([referee_phase3_verdict.json](../relational_yukawa_phase3/outputs/referee_phase3_verdict.json)):
1. **Check 0 (`AST Zero-Import, Empirical Firewall & Triple-Phase Seal Audit`):** Confirmed `0` producer imports, `0` empirical PDG float literals across `src/`, `scripts/`, and `tests/`, and intact SHA-256 seals across Phases 1, 2, and 3.
2. **Check 1 (`Independent Keast-5 Quadrature, 45-Tet Cover of (6) & [5,1,2,2] CP Audit`):** Using 5-point degree-3 Keast quadrature (distinct from Producer's 14-point degree-5 rule) and direct $\mathbb{F}_5$ Gaussian elimination (distinct from Producer's integer SNF):
   - Solved the untwisted 45-tetrahedron 5-cusp cyclic cover of `b++LLLLLLRLR` (`n_sub = 3`), confirming forbidden $\mathbb{Z}/5\mathbb{Z}$ overlap `2.71e-17`, ranks `[3, 3]`, `4` exact zero CKM entries, and $|\hat{\mathcal{J}}| = 3.77 \times 10^{-31}$.
   - Independently solved `b++LLLLLRLLRRLR` vs. `b++LRRRRRLRRLLR` (`n_sub = 4`, Dirichlet), obtaining $|\hat{\mathcal{J}}|_{\max} = 9.3974 \times 10^{-5}$ (matching Producer's $9.4461 \times 10^{-5}$ to **`0.516%`**) and enantiomer reversal / relational collapse to **`1.71e-18`**.
3. **Check 2 (`50-Digit mpmath Relational Quotient Countercheck`):** Verified `0.0` enantiomer discrepancy, `0.0` amphicheiral controls, and `0.0` deviation from Producer's `[(6)]_rel` relational cusp modulus.
4. **Check 3 (`Keast-5 Coupled Spin-Flux Palindrome Countercheck`):** Confirmed `(6)` spin-flux palindrome error `6.94e-17` vs. `[5,1,2,2]` single-peak gap `+0.0170`.
5. **Check 4 (`Independent E_8 Root/Coroot Enumeration, Dedekind Reciprocity & 25-Trial Adversarial Haar Audit`):** Confirmed $k_{\text{inst},\min}(N) = \{1:1, 2:3, 3:6, 4:10\}$, Dedekind reciprocity error `6.66e-16`, and 25 fresh adversarial Haar $U(3)^3$ trials invariant to `1.11e-15`.

---

## 5. Architectural Crossroads Uncovered by Phase 3

Phase 3 replaces vague speculation with two sharp, theorem-grade design constraints for any self-starting loop $\Phi(X^*) = X^*$:
1. **Action Principle vs. Palindrome Symmetry:** Pure hyperbolic volume minimization (`A-one` on $\operatorname{Vol}(M_H)$) selects the Klein-four palindrome `[(6)]_rel` ($\operatorname{Vol} = 5.5864$), which has **exact zero CKM CP violation** ($\hat{\mathcal{J}} = 0$). Generating 3-family CKM mixing + $\hat{\mathcal{J}} \ne 0$ from 3D hyperbolic geometry requires either:
   - a dynamical/spectral selection mechanism (e.g., fermion determinant / one-loop Casimir energy or chiral anomaly coupling) that penalizes time-reversible Klein-four bundles or favors irreversible chiral histories such as `[[5, 1, 2, 2]]_rel` ($\operatorname{Vol} = 9.0687$), **or**
   - `A-all` partition-function aggregation where irreversible cusp-ramified sectors contribute non-canceling relational CP violation.
2. **3D Bulk vs. 4D Cusp Cap (`k_vis = 6`):** Pure 2D/3D topological invariants fall short of $k_{\text{inst},\min}(3) = 6$ without hand-inserted multipliers, whereas capping the elliptic torus cusp with a smooth 4D rational elliptic manifold ($dP_9 = \frac{1}{2}K3$, $\chi = 12$) supplies $k_{\text{vis}} = 6$ via the symmetric $E_8 \times E_8$ Bianchi identity.
