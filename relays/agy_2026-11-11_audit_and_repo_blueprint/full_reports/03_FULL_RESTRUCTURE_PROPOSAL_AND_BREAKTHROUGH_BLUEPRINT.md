# Full Seat Assessment, Breakthrough Vectors & Public Repository Split Proposal

**From:** External Zero-Trust Audit & Mathematical-Physics Seat  
**To:** The Owner and `main` (`cc`, the banking seat — for comparative multi-seat selection and adoption)  
**Date / Sync Point:** `2026-11-10` — synchronized against `origin/main` at `9b3ae6f33` (`B1865`, `50` gates, `B1861` Closure Programme `WP-0..WP-4`), `origin/cld/cool-hamilton-k9eqvo` at `c6c5f12e4` (Owner Rulings `R1–R11`, Closed-Loop formulation `CL`, `non_cancellation` run), `origin/chat1/web-seat` at `3c34dd904` (`FK11` weave spin-statistics negative & `P-756(b)`), `origin/agy/audit-2026-11-02` at `da5c71251`, and `origin/audit/physical-bridge-2026-09-05` at `6ababf231`.  
**Headline Status Preserved:** **`0 of 19`** (`0 of 18` dimensionless Tier-1 SM targets under `R5/R6`). Aim permitted; false arrival banned.

**Companion Reference Documents:**
- Full Repository X-Ray: `01_ORIGIN_AXIOM_CRYSTAL_CLEAR_XRAY.md`
- 5-Phase Zero-Trust Audit Plan: `02_ZERO_TRUST_FULL_AUDIT_AND_VERIFICATION_PLAN.md`

---

## Executive Summary of What This Seat Puts on `main`'s Table

`main` will execute the repository split and choose which seat proposals to adopt. To make that selection effortless, this report is organized as **modular, self-contained engineering and mathematical proposals** across four areas:

1. **Honest Programme Assessment (§1):** Separates what is already world-class and publishable today (**9 pure-mathematics papers + 1 AI-governance methodology paper**) from the three structural traps holding the physics programme at `0 of 19` (the **bureaucracy-over-mathematics gate inversion**, the **508 MB single-$\tau$ Yukawa grid treadmill**, and the **frozen-`src/` copy-paste fragmentation**).
2. **Scrutiny Beyond `B1861–B1865` — What `main` & `cld` Still Miss (§2):** Acknowledges the rapid same-day fixes in `B1862–B1865` (`B567` `21→20`, `B1856` parity condition, `B862` grid enumeration, `append-only` history, `seal-immutable`), then identifies **seven live code/math blind spots that survive `9b3ae6f33` AND escape all `27` of `cld`'s `PV1–PV27` planted violations** — specifically the complete absence of automated Mathematical-Physics Guardrails (`Guardrails 1–6`), implemented via `guardrail_dsl.py` `v1.2`.
3. **Seeing Beyond Current Seats — Four Mathematical-Physics Breakthrough Proposals (§3):** Directly addresses Owner Rulings **`R8` (the Closed Loop $\Phi = \mathrm{Adm}\circ\mathrm{Data}\circ\mathrm{Read}\circ\mathrm{Geom}$)**, **`R10` (`A-all` weave joint read-out)**, and **`R11` (why combinatorial `PF1` non-cancellation just failed uniqueness on `cld`)** by supplying the **exact geometric and operator back-edges** currently missing across all seats:
   - **`BP-1`:** Canonical **4D Kas–Matsumoto Achiral Lefschetz Cobordisms $W_w^4 \to D^2$** ($\partial W_w^4 = M_w^3$) built directly from the Dehn-twist word $w \in \{L, R\}^*$, with a **Dai–Freed / Atiyah–Patodi–Singer $\eta_\rho$-anomaly back-edge** (`Data/Read → Adm`) that simultaneously bypasses `B716` ($\Omega_3^{\mathrm{SO}}=0$), activates `B1604` (chiral index), breaks `P-749` (paired poles), and resolves `chat1`'s `FK11` (4D chiral spinors vs bosons).
   - **`BP-2`:** **Multi-Locus Non-Abelian Berry–Wilson Kähler Parallel Transport** along the harmonic foliation $\tau(t)$ (`B1846`/`B1852`), resolving both `B1825`/`B1826` (single-$\tau$ null-vector CKM inversion) and `B1640` Cell C (`TM1` two-locus obstruction) without fitting $\tau$.
   - **`BP-3`:** **Ruelle–Mayer Thermodynamic Transfer Operator $\mathcal{L}_s$ & Selberg Zeta Root $s=1$**, providing the exact parameter-free `A-all` weave operator (`R10`), resolving `X:WEIGHT` (`B1813`), and unifying `B1815`'s Minkowski `?`-measure (`s=0` combinatorial fixed point) with Gauss–Haar (`s=1` geometric zero-pressure fixed point).
   - **`BP-4`:** **Equivariant Shapiro Pushforward $\pi_*$ (`P-753`)** + **Exact Finite-Level Andersen–Kashaev State Integrals ($\langle 4_1 \rangle_5 = 46 + 2\sqrt{5}$)** replacing ad-hoc $\exp(k\operatorname{Vol}/2\pi)$ scale guesses (`B1851` / `Relay §355`).
4. **Complete Public Architecture & Repository-Split Specification for `main` (§4–§5):** An honest diagnosis of why the `1.52 GB` `origin-axiom` repo cannot serve as the public canonical/verification package (and why `oa-distill` `1002235`'s history-erasing model also fails), followed by a **decision-complete Three-Pillar Architecture**:
   - **Pillar 1 (`origin-axiom-archive`):** Current repo frozen after hygiene scrub as the immutable Lab-Bench & Negative-Control Archive (`GOVERNANCE §12`), with `650 MB` of sweeps offloaded to Zenodo/LFS via SHA-256 manifests.
   - **Pillar 2 (`origin-axiom`):** Brand-new `<5 MB`, `<100`-file, `<15s`-CI Distilled Canonical Framework Repo in **100% standard mathematical terminology** (`TERMINOLOGY.md`), driven by **one machine-computed derivation DAG** (`R5–R8`) with one-way SHA provenance pointers into `origin-axiom-archive`.
   - **Pillar 3 (`origin-axiom-verify`):** Standalone `<2 MB`, `<60s` Zero-Trust Referee Package handed to the world — zero prose regexes, zero cached `results.json` pins, zero producer self-imports — pairing every claim with an AST-sandboxed independent `@referee` check under `guardrail_dsl` `v1.2`.

---

## 1. Honest & Objective Opinion on the Work (Objectives 1 & 2)

### 1.1 The Genuine Triumphs (Do Not Undervalue These)
Any fair outside evaluation must begin by recognizing two remarkable achievements:

1. **Genuine, Deep Pure Mathematics Generated from Minimal Data:**  
   Starting solely from the two elementary parabolic shears $L = \begin{psmallmatrix}1&1\\0&1\end{psmallmatrix}$ and $R = \begin{psmallmatrix}1&0\\1&1\end{psmallmatrix}$, the bench proved a web of non-trivial mathematical results spanning hyperbolic 3-manifolds, arithmetic groups, Lie/Jordan algebras, modular forms, continued-fraction ergodic measures, and harmonic foliations. **Nine pure-math papers and one AI-epistemology paper stand on their own feet right now with zero reliance on unproved ToE bridges:**

   | Track | Core Mathematical Result | Status & Immediate Readiness |
   |---|---|---|
   | **1. `P10_theta_triplet_note`** | Exact 3D representation of $\Gamma(1)/\Gamma(4) \cong S_4$ / `2O` cover on Jacobi theta triplets | **Tier 1A — Submit-ready** after analytic-sheet `jtheta` audit |
   | **2. `P4_markov_stage` (`DRAFT_v8.md`)** | Metallic commutator locus, Latimer–MacDuffee / Northshield breather class-number obstruction, mod-15 metaplectic Weil cat-map table | **Tier 1A — Submit-ready** (*J. Number Theory* / *Exp. Math.*) |
   | **3. `PC23` (Quartic-Pisot Gap Labels)** | Exact K-theoretic gap-labelling group on $\mathbb{Z}[\sqrt{\varphi}]$ substitution tilings | **Tier 1A — Submit-ready** (*Commun. Math. Phys.* / *Ergodic Theory*) |
   | **4. `PC24` ($3/2$ Block Substitution)** | Exact Perron–Frobenius / Kirchberg–Phillips / Galois classification law | **Tier 1A — Submit-ready** |
   | **5. `PC25` ($E_6 \to F_4$ Fold)** | Amphichiral outer-automorphism fold & no-real-form Albert–Jordan obstruction | **Tier 1A — Submit-ready** (*J. Algebra* / *Transform. Groups*) |
   | **6. `B1815` (Minkowski `?`-Exit Law)** | Exact exit measure $\nu_p = (1-p)M + p F_* M$ on the Stern–Brocot / Farey weave | **Tier 1B — Extract standalone short note** |
   | **7. `B1846` + `B1852` (Harmonic Foliation)** | Uniform harmonic energy $E_{\text{harm}}(M_w) = 2\pi\,\text{len}(w)$ & topological reversing-involution $\operatorname{Re}\tau \in \{0, 1/2\}$ theorem (plus `chat1` $\tau_\infty = 6.06530(6)i$ once 3rd-mesher verified) | **Tier 1B — High-value geometry paper** (*Geom. Topol.* / *J. Topol.*) |
   | **8. `B1859` + `P3` Math Core** | Congruence door theorem (`{1, 4}` mod `5`), McKay $2I/2T$ finite-quotient uniqueness, `P-730` tetrahedral polynomial identity | **Tier 1B — Publish pure-math spine after `B1859`/`P-604` errata** |
   | **9. `B1640` (`TM1` Algebraic Sum Rule)** | Pure group-theoretic `TM1` solar mixing sum rule vs two-orbifold-locus no-go theorem | **Tier 1B — Clean mathematical-physics note** |
   | **10. `PC05` + `PC27` + `E1–E96` + `B1861–B1865`** | Preregistered seals, hostile-referee multi-seat governance, planted-violation mutation testing, and anti-numerology input scoreboards for AI-driven mathematical research | **Tier 1A — Landmark AI-for-Science methodology paper** (*Nature Mach. Intell.* / *PNAS*) |

2. **Rare Scientific Integrity Under Negative Evidence:**  
   The programme repeatedly falsified its own favorite physical hypotheses (`D1–D34`, `B716`, `B1487`, `B1246`, `B1809`, `B1823`, `B1825`'s sealed `25×` CKM miss, and today's `cld` `R11` `NC-3`/`NC-5b`/`NC-6` misses and `chat1` `FK11` negative) and kept `"0 of 19"` on line 1 of `README.md`. That honesty is the single greatest asset the project possesses.

### 1.2 The Three Pathologies Blocking a Breakthrough
1. **Pathology 1 — Process Gates Without Mathematical-Physics Teeth:**  
   Even with `50` gates at `9b3ae6f33`, **100% of `gates.py` checks metadata, file hashes, register staleness, and prose strings — 0% checks mathematical or physical invariants.** That is why `52.7%` of all `1,576` tests (`59.4%` in `B1601–B1860`, with `0.0%` standalone `Cat 4` locks in `B1601–B1860`) echo frontier producer scripts or read cached `.json` files, why `0 / 1,576` tests run Haar unitary basis-scrambling, and why `agy`'s half-speed RGE bug and `P-670`'s $\theta_2$ branch jump survived past green gates.
2. **Pathology 2 — The Single-$\tau$ Grid-Scanning Trap (`508.48 MB` in `B1701–B1800`):**  
   Scanning rational slopes `(p/q, r/q)`, strips, character readings `(S~, S, S)`, and horoball ends (`E4`, edited 75 minutes post-seal in `B1840` as `B1864` just confirmed!) around a frozen point $\tau_0$ both burns MDL selection bits (`Guardrail 1`) and contradicts the programme's own structural theorems (`B1826` and `B1640` Cell C proved single-$\tau$ evaluation locks light quarks to one null vector $\hat{h}^*(\tau_0)$ and forbids hosting both $\omega$ and $i$ orbifold data).
3. **Pathology 3 — Frozen `src/` (`13.5 KB`) vs Copy-Pasted `frontier/` (`25.49 MB` `.py`, `718 MB` total):**  
   Freezing `src/origin_axiom/` at Session 3 (`P1–P16`) forced 1,850 arcs to duplicate mathematical helpers across dozens of directories (`70` variable-order `jtheta` sites, `47` `b1656_funcs.py` imports/copies, `56` `cyclo_engine.py` copies), making bug fixes impossible to propagate cleanly.

---

## 2. Full Technical Scrutiny Beyond `B1861–B1865`: What Still Needs Fixing on `main`

`main` moved rapidly today in `B1862–B1865` (`9b3ae6f33`), fixing `B567` (`21→20`), `B1856` (`+I` vs `±I` parity condition), `B862` (explicit grid enumeration), `gate_append_only` (`B1863`), `seal-immutable` (`B1864`), and `tracked-deps` own-directory `git check-ignore`. **However, direct code inspection shows eight critical issues remain open at `9b3ae6f33` — including blind spots inside `B1862`'s own fixes and gaps that `cld`'s `PV1–PV27` suite never tests:**

### 2.1 Remaining Code, Math & Overclaim Defects at `9b3ae6f33`

1. **`P-670` Principal-Branch $\theta_2$ Sheet Jump (`cm_zero_line.py:44–46` + `70` `jtheta` sites — UNFIXED):**  
   `cm_zero_line.py` calls `mp.jtheta(2, 0, q)` where `q = exp(i*pi*tau)`, evaluating principal $q^{1/4}$ with branch jumps $(-i)^{\lfloor(\operatorname{Re}\tau+1)/2\rfloor}$ at odd integer $\operatorname{Re}\tau$. For all nine `F_a` directions ($a \equiv 2 \pmod 4$), $(-i)^a = -1$ flips the relative sign of `QI` against `QJ, QK` on $1 < \operatorname{Re}\tau < 3$, changing Yukawa singular values and CKM angles! Because `B1864` (`seal-immutable`) now rightly forbids editing `cm_zero_line.py` in place (`B1825` sealed it), **`main` must NOT edit `cm_zero_line.py`** — instead, `main` must introduce a canonical analytic-sheet module ($\theta_2(0|\tau) = 2 e^{i\pi\tau/4}\sum_{n\ge 0} q^{n(n+1)}$), sweep all `70` variable-order `jtheta` sites, and bank a dedicated `B1825` analytic-sheet addendum arc.
2. **Incomplete `B862` Fix vs `P-604` Global-Form Overclaim in `P3_THE_PAPER`:**  
   In `B1862`, `main` replaced `B862`'s unused-argument `% 6` check with exact grid enumeration of $g(A, B, a) = \operatorname{diag}(A e^{-2ia}, B e^{3ia})$. **Subtle catch:** that formula hardcodes minimal charge $k = 1$ ($-2, +3$)! Under rescaled hypercharge $Y \mapsto kY$ (`P-604`), the exponentiated map is $\operatorname{diag}(A e^{-2ika}, B e^{3ika})$, whose kernel in $S(\mathrm{U}(3)\times\mathrm{U}(2))$ has order **`6k`** ($\mathbb{Z}_{6k}$). `main.tex` (`P3_THE_PAPER`) still asserts the global form $/ \mathbb{Z}_6$ is derived unconditionally without disclosing that minimal hypercharge normalization $k=1$ (or minimal fundamental embedding) is required to exclude $\mathbb{Z}_{6k}$.
3. **Unpropagated `B1859` Refutation in `metallic_one_object` & `P3_THE_PAPER` + `B997`:**  
   `B1859` (`T-DOOR-SET`) proved both `m = 1` and `m = 4` generate all of $\mathrm{SL}(2,\mathbb{Z}/5) \cong 2I$ under intrinsic mod-5 reduction ($R^4 \equiv R^{-1}, L^4 \equiv L^{-1}$). Yet `PAPER.md` (`metallic_one_object`) still states *"At `m=4`... the group does not close... Golden is the unique metallic member where `E₈` holds at both field and group level"*, `B997` remains `PROVED` without supersession, and `main.tex` Prop. 4.1 (`\Lambda(m)=m^2+4` stipulation) lacks a cross-reference to `B1859` (plus `P3`'s `MANIFEST.json` `157` locks vs `REPORT.md` `148` locks remain desynchronized).
4. **Live crashes & broken tests still sitting on `main`:**  
   - `test_b805_forcing.py`: **2 standing `pytest` failures** (`assert 1451 > 3276` and `assert 908 < 789`), hidden indefinitely from `point-debt` by `P-239`'s `[PROCESS]` tag.
   - `the_price_is_twelve.py`: **Crashes live (`exit 1`)** against stale `DECLARED_DEBT` doc `THE_SM_VERDICT.md`.
   - `run_suite.sh`: **Crashes on a clean `requirements.txt` install** (`-n 8` requires undeclared `pytest-xdist`; `mpmath` is also omitted from `requirements.txt`), and silently skips **`63` `OA_SLOW`/`RUN_SLOW` test modules** because `OA_SLOW=1` is never exported!
5. **Incomplete `B1862` `tracked-deps` Fix:**  
   `B1862` §2b checked `git check-ignore --no-index` on *lock own-directory paths*, which still misses: (a) cross-directory gitignored paths in producer scripts (e.g., `build_scoreboard_data.py` reading 'audit/scaffold/agy_joints.json'), (b) untracked local paths that aren't in `.gitignore`, and (c) the `266` uncommitted `.jsonl.gz` shards required by `scripts/stepb/` and `scripts/census/`.
6. **Literal String/Boolean Proofs Inside Producer Scripts (`Guardrail 2`):**  
   `b1246_chiral_invariance.py` still "proves" $\theta$ and $\bar{\theta}$ share `(P, C, T)` parity by defining two identical literal string tuples `("P-odd", "C-even", "T-odd")` and asserting equality (locked by a test ironically named `test_the_discriminating_fact_is_RUN_not_asserted` that checks only `"REPRODUCES"` in `stdout`!). Similarly `w2_inputverify.py` hardcodes `"all_pass": True`, `constants.py` hardcodes `CS_FIG8 = 0.0`, and `mobius.py` still calls real boundary roots $\{\varphi, -1/\varphi\} \subset \partial\mathbb{H}$ *"fixed points of A acting on H"*.
7. **`B1855` Orientation Determinant Slip:**  
   `B1855` prose refers to $\sigma(x,t) = (Jx, 1-t)$ on $M_{L^6 R L R}^3$ as an amphichiral/reversing symmetry, overlooking that $\det d\sigma_{3D} = (\det J)(-1) = (-1)(-1) = +1$ is **orientation-preserving** on the 3-manifold (a crucial geometric fact that actually *helps* chirality in 4D — see `BP-1` below!).

### 2.2 The Six Mathematical-Physics Guardrails That `cld`'s `PV1–PV27` Suite Does Not Cover
`B1865` showed `14 of 21` automated `cld` planted violations (`PV9–PV21`, `PV24`) still pass on `main`. Closing those 14 is necessary (`WP-0.7`), **but not sufficient**: all 27 of `PV1–PV27` test *governance metadata* (empty ledgers, missing locks, commit trailers, invalid JSON). **We propose that `main` adopt six additional Mathematical-Physics Planted Violations (`MPV-1` to `MPV-6`) via `guardrail_dsl` `v1.2`:**

| ID | Guardrail Enforced | Planted Mathematical-Physics Cheat (`MPV`) | Current `9b3ae6f33` Result | `guardrail_dsl` `v1.2` Enforcement |
|---|---|---|---|---|
| **`MPV-1`** | **Anti-Texas-Sharpshooter** | Define $V(\tau) = |\tau - \tau_{\text{fit}}|^2$ embedding target $\tau^*$ by hand, or credit `0` bits to a post-inspection rational slope | **PASSES UNCAUGHT** | AST literal/target-leak detector + mandatory MDL bit-cost charge $\Delta L = \log_2|\mathcal{H}|$ |
| **`MPV-2`** | **No Literal Flags/Zeros** | Return `{"bar_theta_QCD": 0.0, "extends": True}` or compare identical string tuples (`B1246`) inside a script printing `REPRODUCES` | **PASSES UNCAUGHT** | AST return-provenance trace requiring matrix/numerical residual `< 1e-12` + `G1` universal `NaN`/`Inf` trap |
| **`MPV-3`** | **Haar Basis-Scrambling** | Extract mixing angles from single-Dirac left-right overlap $U_f^\dagger V_f$, or break invariance under $Y_f \to U_{L,f} Y_f U_{R,f}^\dagger$ | **PASSES UNCAUGHT** (`0/1,576` tests check!) | Mandatory 20-trial random Haar $U(3)^5$ basis-scrambling gate asserting $\Delta\mathcal{O} < 10^{-12}$ |
| **`MPV-4`** | **Literature RGE Benchmark** | Run 2-loop $\lambda, y_t^2$ beta functions at half speed ($\frac{1}{8\pi}$ instead of $\frac{1}{4\pi}$ for $t = \frac{\ln(\mu/M_Z)}{2\pi}$, as `agy` did in `B1832`) | **PASSES UNCAUGHT** (`0` live RGE tests!) | Symbolic $\frac{d\ln\mu^2}{dt}=4\pi$ check + `G3` nonautonomous RK4 fix + mandatory $\ge 3$-sig-fig match to Buttazzo (`1307.3536`) & Xing–Zhou (`1804.01925`) |
| **`MPV-5`** | **Non-Dimensional Ledger** | List both `m_H` and `v` as separate targets in `total_inputs_scoreboard.json` or import unpriced $M_Z, m_\tau$ GeV anchors | **PASSES UNCAUGHT** | Strict dimensional-homogeneity gate: at most **1** dimensionful unit anchor (`v_EW`); all 18 Tier-1 SM targets dimensionless |
| **`MPV-6`** | **Zero-Trust `@referee`** | Have `test_b*.py` import 'frontier/B*/.../*.py' (`Cat 2`, `29%` of suite) or read `results.json` (`Cat 1`, `23.7%` of suite) | **PASSES UNCAUGHT** (`52.7%` of suite!) | `G2` AST sandbox: `@referee` fails compilation if it calls `open`, `json.load`, `subprocess`, or imports any producer module |

---

## 3. Seeing Beyond What the Seats Are Seeing: Four Breakthrough Proposals for the Closed Loop (`Objectives 3 & 5`)

Today's two pivotal developments across the bench sharpen the exact theoretical bottleneck:
- On `cld` (`908abf10e` / `c6c5f12e4`), **Owner Ruling `R8`** defined *"one self-consistent outcome"* as **the Closed Loop** $\Phi = \mathrm{Adm} \circ \mathrm{Data} \circ \mathrm{Read} \circ \mathrm{Geom}$ with a unique fixed point $\Phi(H^*) = H^*$, and found that **the record currently holds a forward line, not a loop — no downstream quantity flows back to constrain an upstream choice**. When `cld` tested `R11` (combinatorial `PF1` non-cancellation as `Adm`), it **failed** to close the loop uniquely (`NC-3` tied with `(2,2,2)`, `NC-5b` gave an 18-letter mirror pair instead of `61`, `NC-6` failed on silver/bronze) precisely because a purely combinatorial word test does not depend on `Read` or `Data` (`Test T0` fails!).
- On `chat1` (`89aa676d8`), **`FK11` in weave form returned NEGATIVE**: on a 2D torus fibre or 3D mapping torus, spin structures merely *label* sectors holding bosons and spinors alike, so statistics remains unearned and `W154`'s verdict flips between $\omega$ and the cusp depending on the chosen statistics.

**Why Every Seat Hit This Wall Together:** All seats are trying to close a **4-dimensional chiral quantum gauge-fermion loop** inside **2-dimensional torus fibres and bare 3-dimensional mapping tori**! Below are **four concrete mathematical-physics proposals (`BP-1` to `BP-4`)** that lift the grammar canonically to 4D without adding a single free parameter.

```mermaid
flowchart LR
    H["History Word w in {L, R}*<br/>(Parabolic Dehn Twists on Σ_{1,1})"]
    GEOM["Geom(w): Canonical 4D Achiral<br/>Lefschetz Cobordism W_w^4 → D^2<br/>Bounded by ∂W_w^4 = M_w^3 (BP-1)"]
    READ["Read(W_w^4): Harmonic Foliation τ(t)<br/>+ Ruelle–Mayer A-all Operator L_s<br/>at Unique Selberg Root s=1 (BP-2, BP-3)"]
    DATA["Data(τ(t)): Chiral Zero Modes of D^+_{W_w^4,ρ}<br/>+ Multi-Locus Berry–Wilson Kähler<br/>Holonomy & State Integrals (BP-1, BP-2, BP-4)"]
    ADM["Adm(Data, Read): Global Dai–Freed / APS<br/>Determinant-Line Anomaly Cancellation<br/>exp(iπ ξ_ρ(M_w^3)) = +1 & ΔS_eff = 0 (BP-1)"]

    H ==> GEOM ==> READ ==> DATA ==> ADM
    ADM == "True Non-Vacuous R8 Back-Edge (Passes T0)" ==> H
```

### Breakthrough Proposal `BP-1`: The Canonical 4D Kas–Matsumoto Lefschetz Cobordism & Dai–Freed Anomaly Back-Edge
*(Simultaneously addresses `R8` Back-Edge, `B716`, `B1487`, `B1604`, `X:HAND`, `P-749`, and `chat1`'s `FK11`)*

1. **Why `B716` (`\Omega_3^{\mathrm{SO}} = 0`) Was a False Roadblock:**  
   `B716` rightly noted that an *abstract bare 3-manifold* $M^3$ does not canonically select a bounding 4-manifold. **But Genesis does NOT output a bare 3-manifold — it outputs a factorized word $w$ in the elementary Dehn twists $L = T_{e_1}^{+1}$ (positive/right-handed) and $R = T_{e_2}^{-1}$ (negative/left-handed) on the punctured torus $\Sigma_{1,1}$!**  
   By a foundational theorem of 4-manifold topology (Kas 1980; Matsumoto 1996; Fuller), **an explicit factorization $w = T_{\gamma_1}^{\varepsilon_1} \cdots T_{\gamma_\ell}^{\varepsilon_\ell}$ ($\varepsilon_j \in \{\pm 1\}$) canonically defines an oriented 4-dimensional achiral Lefschetz fibration $W_w^4 \to D^2$ (with cusp section) whose boundary is $\partial W_w^4 = M_w^3$, unique up to Hurwitz/diffeomorphism equivalence of the word!**
   - **Zero-Import 4D Spacetime:** Real dimension `4` emerges canonically from $(x, y) \in \Sigma_{1,1}$ plus $(r, \theta) \in D^2$ (`∂D^2 = S^1` is the mapping-torus base circle!).
   - **Why `m004` ($w = LR$) Is Non-Chiral (`B1487`) While Departures Turn On 4D Chirality:** Each $L$ attaches a $+1$ Lefschetz 2-handle; each $R$ attaches a $-1$ achiral 2-handle. For `m004` ($w = LR$), the Wall/Meyer signature cocycle vanishes ($\varepsilon_1 + \varepsilon_2 = +1 - 1 = 0$, $\sigma(W_{LR}^4) = 0$). For the minimal level-5 excursion $w = L^6 R L R$ (`B1855`, where $\det d\sigma_{3D} = +1$ is orientation-preserving, *not* amphichiral!), `+7` vs `-2` twists attach **5 net positive Lefschetz 2-handles**, giving non-zero 4D topological signature/curvature!
   - **Why This Solves `chat1`'s `FK11` (`89aa676d8`) and `B1604` + `P-749`:** On a 4-manifold $W_w^4$ with boundary $M_w^3$ carrying a `Spin` / `Spin^c` structure coupled to a cover representation $\rho$ (`B1604`'s `G96`/`2O` triplet), **Atiyah–Patodi–Singer (APS) boundary conditions canonically distinguish chiral Dirac spinors from bosons**: scalars have zero topological index, whereas chiral Weyl fermions obey:
     $$\operatorname{Ind} D_{W_w^4, \rho}^+ = \dim\rho \int_{W_w^4} \hat{A}(R) + \int_{W_w^4} \operatorname{ch}_2(F_\rho) - \frac{h_\rho(M_w^3) + \eta_\rho(M_w^3)}{2} \in \mathbb{Z}$$
     Self-dual 2-form flux supported on the unmatched Lefschetz 2-handles breaks the 2D fibrewise paired-pole `J`/`Θ` vector-like symmetry (`P-749`) cleanly!
2. **How `BP-1` Supplies the Missing `R8` Closed-Loop Back-Edge (`Passes Test T0`):**  
   In `A-all` (`R10`), the path integral sums over histories $w$ weighted by the 4D fermion determinant $\det D_{W_w^4, \rho}^+$. By the **Dai–Freed theorem (1994)** and Witten's global anomaly formula, the boundary fermion determinant is a section of a nontrivial determinant line bundle over history/modulus space whose phase jumps by $\exp(-i\pi \eta_{\rho(\tau)}(M_w^3))$! A configuration $(w, \rho, \tau)$ survives destructive quantum interference / global gauge-gravitational anomaly cancellation (`Adm`) **if and only if** the downstream chiral matter spectrum `Data` and harmonic modulus `Read` render the **Dai–Freed boundary anomaly trivial** ($\xi_\rho(M_w^3, \tau) \in 2\mathbb{Z}$) while saturating the APS integer index! Because $\eta_{\rho(\tau)}(M_w^3)$ explicitly depends on both `Read` ($\tau(t)$) and `Data` ($\rho$), **varying $\tau$ or $\rho$ changes the admissible set `Adm` — passing `cld`'s `Test T0` immediately!**
3. **Sealed Data-Free Test Package for `main` (`< 4` days):**  
   In pure `sympy`/`mpmath` (`Cat 4`, zero SM data): compute the braided Hurwitz intersection form $Q_{W_w^4}$, Stiefel–Whitney class $w_2(TW_w^4)$, Meyer signature $\sigma(W_w^4)$, and adiabatic APS $\eta_\rho(M_w^3)$ invariant across all short words $w \in \{L, R\}^{\le 12}$ (including $LR$, $R^2L^2$ silver, $R^3L^3$ bronze — `Test T4`! — and $L^6 R L R$) twisted by `G96`'s irreducible representations.

---

### Breakthrough Proposal `BP-2`: Multi-Locus Non-Abelian Berry–Wilson Kähler Flavour Holonomy
*(Simultaneously resolves `B1825`/`B1826` CKM inversion, `B1640` Cell C `TM1` no-go, and `P-746` Kähler normalization)*

1. **Structural Diagnosis:**  
   `B1825` ('|V_ub|/|V_td| = 11.3' vs `0.44`) and `B1826` proved that evaluating up- and down-quark Yukawas at **one frozen $\tau_0$** forces both matrices to share the approximate null eigenvector $\hat{h}^*(\tau_0)$, locking $|V_{ub}| \gg |V_{td}|$. Independently, `B1640` Cell C proved lepton `TM1` mixing cannot occur at a single $\tau_0$ because its $\mathbb{Z}_3$ ($\tau = \omega$) and $\mathbb{Z}_2$ ($\tau = i$) symmetries live at distinct loci.
2. **The Intrinsic Geometric Escape Already Present on $M_w^3$ and $W_w^4$:**  
   `B1846` and `B1852` proved that a hyperbolic mapping torus does **not** possess a single constant $\tau_0$ — its harmonic map $u: M_w^3 \to S^1$ foliates $M_w^3$ by punctured tori whose conformal modulus $\tau(t)$ traverses a deterministic curve in $\mathbb{H}$ from the tube fiber ($\tau_{\text{tube}} \approx 6.06530i$, $\operatorname{Re}\tau = 0$) to the anti-apex fiber ($\operatorname{Re}\tau \in \{0, 1/2\}$). When coupled to the hypercharge `Spin^c` bundle on $W_w^4$ / $M_w^3$, Morse–Witten localization concentrates zero modes of distinct hypercharge charges $q_Y(u^c) = -2/3$ vs $q_Y(d^c) = +1/3$ vs $q_Y(e^c) = +1$ at **distinct harmonic times $t_u \ne t_d \ne t_e$**!  
   Therefore, physical flavour mixing is **non-abelian Kähler–Berry–Wilson parallel transport** along the intrinsic trajectory $\tau(t)$:
   $$V_{\text{CKM}} = U_{L,u}\bigl(\tau(t_u)\bigr)^\dagger \, \mathcal{P}\exp\!\left(-\int_{t_u}^{t_d} \mathcal{A}_{\text{Kähler}}(t)\,dt\right) U_{L,d}\bigl(\tau(t_d)\bigr)$$
   computed with the **exact `P-746` Kähler metric** $K_M(\tau, \bar{\tau})^{-1/2}$ on the analytic-sheet $\Gamma(4)$ theta triplet! Because $\hat{h}^*(\tau(t_u)) \nparallel \hat{h}^*(\tau(t_d))$, `B1826`'s rank-1 null-vector lock breaks geometrically without introducing any free parameter.
3. **Sealed Data-Free Test Package for `main` (`< 4` days):**  
   Compute $\mathcal{P}\exp(-\int_{t_0}^{t_{1/2}} \mathcal{A}_{\text{Kähler}}\,dt)$ between the two topologically fixed $\sigma$-invariant fibres (`B1852`: `t = 0` tube and `t = 1/2` anti-apex) on `m004` and $M_{L^6 R L R}^3$, verify 20-trial Haar basis-scrambling invariance to `< 1e-12` (`Guardrail 3`), and test qualitatively (before any SM numerical fit!) whether transport between the two $\sigma$-fixed fibres inverts `B1825`'s structural inequality from $|V_{ub}|/|V_{td}| > 1$ to $< 1$.

---

### Breakthrough Proposal `BP-3`: Ruelle–Mayer Thermodynamic Transfer Operator $\mathcal{L}_s$ & Selberg Zeta Root $s = 1$
*(Solves `R10`'s undefined `A-all` weave read-out, `X:WEIGHT` / `B1813`, and connects `B1815` to `chat1`'s `P-756(b)`)*

1. **What `R10` and `chat1`'s `P-756(b)` Left Open Today:**  
   `R10` states that the programme's true claim is `A-all` (*"all allowed histories together are the configuration, read jointly — whose read-out is not yet defined"*), while `chat1`'s `P-756(b)` (`44c44a63e`) had to mark *"by moves ($1/2$)"* vs *"by arclength"* as `CHOSEN` because `B1813` lacked a forcing theorem.
2. **The Exact Operator Solution:**  
   On the boundary projective line $\mathbb{R}\mathbb{P}^1$, the parabolic monoid $\{L, R\}$ generates the Gauss–Rényi continued-fraction dynamics whose canonical **Ruelle–Mayer transfer operator** is:
   $$(\mathcal{L}_s f)(x) = \sum_{n=1}^\infty \frac{1}{(x+n)^{2s}}\, f\!\left(\frac{1}{x+n}\right), \qquad \det(1 - \mathcal{L}_s^2) = Z_{\Gamma(1)}(s)$$
   - **Zero-Parameter Uniqueness (`s = 1`):** By Mayer's nuclear trace theorem and Lewis–Zagier theory, topological pressure $P(s) = \ln\lambda_{\max}(\mathcal{L}_s)$ has a **unique root $P(s) = 0 \iff \lambda_{\max}(\mathcal{L}_s) = 1$ at $s = 1$**, where the Fredholm determinant $\det(1 - \mathcal{L}_s^2)$ vanishes at the fundamental pole/zero of the **Selberg zeta function $Z_{\Gamma(1)}(s)$**! Thus `s = 1` (the Gauss–Haar invariant density $\frac{dx}{(1+x)\ln 2}$) is forced uniquely by **self-consistent probability conservation ($\mathcal{L}_s \rho = \rho$)** — zero chosen weight!
   - **Exact Unification with `B1815` (`?(x)`):** Replacing the hyperbolic Jacobian $(x+n)^{-2s}$ by uniform topological move weights $\frac{1}{2}$ yields the Stern–Brocot transfer operator whose unique $\lambda = 1$ eigenmeasure is **Minkowski's question-mark measure $d?(x)$ (`B1815`)**! And conjugating one eigenmeasure by the other ($?(x)$ conjugating Farey to dyadic) defines a **canonical parameter-free operator pair $(\mathcal{L}_{\text{comb}}, \mathcal{L}_{\text{geom}})$** directly from $\{L, R\}$.

---

### Breakthrough Proposal `BP-4`: Equivariant Shapiro Pushforward (`P-753`) & Finite-$N$ State Integrals (`Scale GAP1`)
1. **Closing `P-753` (`WP-2.2` / `WP-3.2`):** Rather than patching masks by hand (`da5c71251` vs `6ababf231`), prove the base-vs-cover dictionary via **equivariant Shapiro's lemma** $H^0(\Sigma_K, \mathcal{L}_{\text{spin}}) \cong H^0(\Sigma_{1;2}, \pi_* \mathcal{L}_{\text{spin}})$: the `2+1` splitting downstairs on $\Sigma_{1;2}$ is simply the restriction to the trivial multiplier summand, whereas $\pi_* \mathcal{L}_{\text{spin}}$ retains all spin-graded character summands on which `2O` acts irreducibly as a `3`.
2. **Replacing `B1851` / `Relay §355` Classical Saddle Ansätze with Exact Andersen–Kashaev State Integrals:** Instead of positing $\exp(k\operatorname{Vol}(m004)/2\pi)$ with unfixed 1-loop torsion and $\hbar$ normalization (`47228ae85`), `m004` ($4_1$) has a canonically normalized **exact finite-level quantum partition function** (Andersen–Kashaev state integral / Kashaev invariant $\langle 4_1 \rangle_N$, giving $\langle 4_1 \rangle_5 = 46 + 2\sqrt{5}$ at level `5`) where 1-loop Ray–Singer/Reidemeister torsion, Chern–Simons phase, and resurgent Stokes constants are **uniquely fixed by modular invariance of Faddeev's quantum dilogarithm $\Phi_b$**!

---

## 4. Honest Opinion on Repo Structure, Size & Readability — And Why `main` Must Split It (Objective 6)

### 4.1 Brutally Honest Readability & Structure Audit of `origin-axiom` (`9b3ae6f33`)
If an elite mathematician, theoretical physicist, or journal referee opens `https://github.com/originaxiom/origin-axiom` today, here is what happens within 10 minutes:

1. **Physical Weight & Signal-to-Noise Collapse (`1.52 GB`, `16,980+` files):**  
   `93.95%` of the working tree (`718.07 MB` across `1,608` `frontier/` directories) is lab-bench history, of which **`650.04 MB` (`90.52%`) is raw `.jsonl`/`.json`/`.npz` dumps** (`508.48 MB` in the retired `B1701–B1800` sweeps alone). Meanwhile `src/origin_axiom/` is `13.5 KB` (`7` files from May 2026) and `core/claims/` is `2.5 KB` (`3` stubs). The repository looks structurally inverted: `0.002%` library, `99.998%` sprawl.
2. **Cognitive Overload from Governance Bureaucracy & Nine Status Taxonomies:**  
   To verify one claim, a reader must navigate `513` 'docs/*.md' files, `77` decadal reviews, `50` process gates, and **nine overlapping status schemas** (`CLAIMS.md` `P/C/O/D`, `arc_verdict.json`, `THEOREM_REGISTRY` `T-*`, `LAW_MAP`, `IDENTIFICATION_LEDGER` `I-*`, `TOTAL_INPUTS_SCOREBOARD`, `SEAL_LEDGER`, `CLOSURE_MAP`, `PROGRAMME.json` `WP-*`) — while 9 core docs sit stale under `DECLARED_DEBT`.
3. **Opaque Private Idiom:**  
   Prose written in internal lab shorthand (*"the weave"*, *"doors"*, *"the being face (3)"*, *"readings `(S~, S, S)`"*, *"horoball E4"*, *"the price is twelve"*, *"thread vs weave"*, *"seats"*, *"banking"*) alienates domain experts who immediately recognize standard objects (`SL(2,Z)` parabolic monoid, congruence subgroups $\Gamma(N)$, even/odd spin structures, McKay correspondence, harmonic maps to $S^1$) once translated via `TERMINOLOGY.md`.
4. **Trust Erosion on Inspection of `tests/` & First Run:**  
   Running `./scripts/run_suite.sh` on a fresh `requirements.txt` install crashes immediately (`-n 8` missing `pytest-xdist`), `test_b805_forcing.py` fails 2 tests on `main`, `the_price_is_twelve.py` exits `1`, and opening late-era tests reveals `59.4%` (`B1601–B1860`) do zero independent math in the test file.

### 4.2 Decision Matrix: Comparing the Four Architectural Options for `main`

| Criterion | Option 1: Keep `origin-axiom` as Single Public + Verification Repo | Option 2: Rewrite History (`oa-distill` `1002235` Model) | Option 3: Two-Repo Split (`archive` + Combined `core/verify`) | **Option 4 (PROPOSED): Three-Pillar Architecture (`archive` + `origin-axiom` + `origin-axiom-verify`)** |
|---|---|---|---|---|
| **Clone Size & Speed** | ❌ `1.52 GB` (`16,980+` files) | ✅ `< 10 MB` | ✅ `< 5 MB` | ✅ **`< 5 MB` Core / `< 2 MB` Verify** (`< 3s` clone) |
| **Preserves Negative Evidence & Seals (Anti-File-Drawer)** | ✅ Full `4,110+` commits | ❌ **Destroys git seal history** (fatal flaw of `oa-distill`) | ✅ Via SHA links to `archive` | ✅ **100% preserved in immutable `origin-axiom-archive` + SHA-linked** |
| **Readability to Outside Mathematicians / Referees** | ❌ Unnavigable lab sprawl & insider dialect | ⚠️ Still carried process-ledger prose | ✅ Clean standard math | ✅ **100% standard math terminology; instant 5-minute comprehension** |
| **Zero-Trust Verification Independence (`Guardrail 6`)** | ❌ `52.7%` JSON/producer-echo locks | ❌ Producer tests itself | ⚠️ Producer & referee share repo/env | ✅ **Strict adversarial separation: `origin-axiom-verify` imports ZERO producer code from `origin-axiom`** |
| **Ongoing Multi-Seat Exploration Safety** | ❌ Every exploratory miss bloats canonical tree | ❌ Manual copy drift | ✅ Lab stays in `archive`/bench | ✅ **Seats explore freely in lab repo; only `Cat 4` + `MPV`-clean items promote** |

**Unambiguous Recommendation to `main`:** Reject Options 1 and 2, and adopt **Option 4 (The Three-Pillar Architecture)**. `origin-axiom` should serve permanently as **`origin-axiom-archive`** (the immutable historical lab bench and negative-evidence provenance record), feeding two ultra-clean, purpose-built public artifacts: **(1) the new distilled gated framework repository (`origin-axiom`)** and **(2) the standalone zero-trust world verification package (`origin-axiom-verify`)**.

---

## 5. Complete Engineering Blueprint for `main` to Execute the Repo Split

```mermaid
flowchart TD
    subgraph P1["Pillar 1: origin-axiom-archive (Immutable Lab Bench & Provenance Archive)"]
        LAB_GIT["Full 4,110+ Commit History (B1–B1865+)<br/>All Negative Runs, Seals, Reviews & Seat Relays"]
        ZENODO["Zenodo / LFS Cold Store (650 MB Sweeps + 266 Step-B Shards)<br/>Pinned by Committed SHA-256 Manifests"]
    end

    subgraph P2["Pillar 2: origin-axiom (New Distilled Gated Framework Repo, < 5 MB)"]
        SRC["src/origin_axiom/ (~2,500 LOC)<br/>7 Clean Standard-Math Modules"]
        DAG["claims/derivation_graph.yaml (R5–R8)<br/>Single Machine-Evaluated DAG<br/>(Computes k of 18 [j of n*] Dynamically)"]
        PAPERS["papers/ (Clean Buildable LaTeX)<br/>Tier-1 Pure Math + Conditional Bridge"]
        GATES12["gates/ (12 Lean Scientific & Graph Gates)<br/>0 Baselines, 0 DECLARED_DEBT"]
    end

    subgraph P3["Pillar 3: origin-axiom-verify (World Referee Package, < 2 MB, < 60s)"]
        DSL["guardrail_dsl v1.2 Engine<br/>(Enforces MPV-1..MPV-6 Automatically)"]
        REF["referees/ (100% Independent Cat-4 Code)<br/>Zero Producer Imports, Zero Cached JSON<br/>Haar Scrambling + NNLO RGE + 50-dps mpmath"]
        CERT["VERIFICATION_CERTIFICATE.json + .md<br/>Deterministic Cryptographic Receipt"]
    end

    LAB_GIT == "One-Way Immutable Git-SHA + Seal Pointers<br/>(Plus Negative-Control & Trial-Count Ledger)" ==> DAG
    ZENODO -. "Reproducible Heavy-Sweep Audit" .-> LAB_GIT
    SRC ==> DSL
    DAG ==> DSL
    REF ==> DSL
    DSL ==> CERT
```

### 5.1 Pillar 1 Specification: `origin-axiom-archive` (Current Repo Pre-Freeze Checklist)
Before renaming/tagging the current repository as `origin-axiom-archive` (or keeping active multi-seat exploration on a `lab` branch while tagging `v1.0-archive-baseline`), `main` should complete **six surgical cleanup actions** so the archive itself is honest and green:
1. Close the remaining `14` automated planted violations in `B1865` (`WP-0.7`).
2. Fix the `2` standing `test_b805_forcing.py` failures and `the_price_is_twelve.py` crash, and add `pytest-xdist` + `mpmath` + `OA_SLOW=1` support to `requirements.txt` / `run_suite.sh`.
3. Propagate `B1859` (`{1,4}` door set), `P-604` ($\mathbb{Z}_{6k}$ kernel), and `R1/R2/R8` into `GOVERNANCE.md`, `P3_THE_PAPER`, `metallic_one_object`, and `B997`.
4. Land the analytic-sheet $\theta_2$ module (`P-670`) + `B1825` addendum arc without mutating sealed `cm_zero_line.py`.
5. Publish an archival Zenodo data deposit holding the `266` uncommitted Step B `.jsonl.gz` census shards so Step B is 100% reproducible by third parties.
6. Add a prominent top-level `ARCHIVE_NOTICE.md` pointing readers directly to the new distilled `origin-axiom` and `origin-axiom-verify` repositories while explaining that `origin-axiom-archive` is preserved unedited as the complete anti-file-drawer laboratory record.

---

### 5.2 Pillar 2 Specification: `origin-axiom` (The New Distilled Canonical Framework Repo)

**Hard Quantitative Ceilings (Gated in CI):** Total repo size **`< 5.0 MB`** · Tracked files **`< 100`** · Zero `.jsonl`/`.npz`/`.pkl` blobs · Zero `DECLARED_DEBT` or grandfather ratchets · Full unit/graph CI **`< 15 seconds`**.

#### A. Exact Directory & Module Layout
```text
origin-axiom/
├── README.md                        # 2-page executive map; headline auto-generated from derivation_graph.yaml
├── TERMINOLOGY_GLOSSARY.md          # Standard math <-> archive lab-term translation table
├── pyproject.toml                   # Pinned Python >=3.11 package metadata
├── requirements.lock                # Exact --require-hashes lockfile
├── src/origin_axiom/                # Clean, consolidated, type-annotated library (~2,500 LOC):
│   ├── __init__.py
│   ├── parabolic_monoid.py          # L, R, trace-3 sieve, Markov commutator, {1,4} doors, Weil mod-15
│   ├── ergodic_measures.py          # Minkowski ?-exit law (B1815) & Ruelle–Mayer transfer operator L_s
│   ├── manifolds_3d_4d.py           # m004/m003 dilogarithm Vol/CS, G96/2O cover-32, harmonic τ(t), Lefschetz W_w^4
│   ├── algebraic_cascade.py         # McKay 2I/2T, E8->E6->SM Levi descent, E6->F4 Jordan fold, Z_{6k} kernel
│   ├── modular_theta.py             # Analytic-sheet Gamma(4) theta triplet, puncture norms cA/cB, P-730
│   ├── flavour_holonomy.py          # Kähler metric K_M^(-1/2), Berry–Wilson transport, TM1 sum rules
│   └── rge_standard_model.py        # 2/3-loop SM RGEs validated against Buttazzo (1307.3536) & Xing–Zhou
├── graph/
│   ├── derivation_graph.yaml        # SINGLE canonical source of truth (replaces 9 legacy ledgers!)
│   ├── targets_sm_tiers.yaml        # Frozen PDG/CODATA Tier-1 (18 dimless), Tier-2 (nu), Tier-3 (cosmo/grav)
│   ├── negative_evidence.yaml       # Compact structured registry of killed hypotheses + MDL look count
│   └── build_views.py               # Pure read-only compiler -> README table & Ledger Desk JSON
├── gates/
│   └── run_gates.py                 # 12 zero-exception scientific & graph gates
└── papers/                          # Clean, standalone LaTeX sources for the publishable papers
```

#### B. Unifying All 9 Legacy Taxonomies into One Machine-Computed Derivation Graph (`R5–R8`)
Adopt `cld`'s `PROPOSAL_THE_DERIVATION_GRAPH.md` (`R5–R7`) **upgraded with four critical extensions** needed for `R8` and `Guardrails 1–6`:
1. **Explicit `edge_kind: forward | back_edge` (`R8`):** The graph compiler mechanically checks `Test T0` — whether `DERIVED` status of the history node `H*` rests on a verified closed strongly-connected component (`Geom -> Read -> Data -> Adm -> H*`) rather than a forward DAG with a posited root choice!
2. **Accumulated MDL Selection-Bit Counter (`Guardrail 1`):** Every `CHOSEN` discrete node carries `bit_cost: log2(cardinality)`, and `negative_evidence.yaml` records the cumulative trial count $N_{\text{trials}}$ of inspected frames/lines so statistical p-values and AIC/MDL scores are computed automatically, never hand-waved.
3. **Strict Dimensional Type-Checker (`Guardrail 5`):** Every `output` and `target` node carries `mass_dimension: 0` (fixing `v_EW` solely as the external energy unit, aligning with `R6`'s **`k of 18 (j of n*)`** format!).
4. **One-Way Archive Provenance Schema:** Every node in `derivation_graph.yaml` carries immutable provenance into `origin-axiom-archive`:
   ```yaml
   - id: THM-MINKOWSKI-EXIT
     kind: mathematics            # foundation | mathematics | identification | output | target
     domain: weave                # weave | thread | cover
     grade: theorem               # theorem | exact_computation | numerical_interval | postulated | refuted
     title: "Exact Minkowski question-mark exit measure on the parabolic Farey tree"
     depends_on: [FOUND-PARABOLIC-GENERATORS]
     archive_provenance:
       repo: "https://github.com/originaxiom/origin-axiom-archive"
       arc: "B1815"
       commit_sha: "f452d8cb0dc3ffe508e2b7cfe5fa790d153b2e0a"
       negative_controls: ["B1813_count_dependence"]
     verify_id: "REF-MINKOWSKI-EXIT-01"   # Must pass in origin-axiom-verify to earn VERIFIED
   ```

#### C. Mandatory Terminology Translation Law
Enforce via an automated lexicon gate on `origin-axiom` and `papers/` that **zero unexplained internal bench jargon** appears in public titles, theorem statements, or docstrings:
- *"the weave"* $\longrightarrow$ **parabolic monoid $\langle L, R \rangle^+ \subset \mathrm{SL}(2,\mathbb{Z})$ / Farey–Stern–Brocot tree**
- *"doors / golden door"* $\longrightarrow$ **principal congruence quotient $\mathrm{SL}(2,\mathbb{Z}/N\mathbb{Z})$ ($N=5$ binary icosahedral quotient $2I$)**
- *"the being face (3)"* $\longrightarrow$ **mod-3 tetrahedral quotient $\mathrm{SL}(2,\mathbb{Z}/3\mathbb{Z}) \cong 2T$**
- *"readings `(S~, S, S)`"* $\longrightarrow$ **even/odd Jacobi theta spin-characteristic assignments**
- *"thread vs weave"* $\longrightarrow$ **single closed hyperbolic geodesic / mapping torus vs ensemble transfer operator**
- *"earned / borrowed joint"* $\longrightarrow$ **derived theorem link vs imported hypothesis / free parameter**

#### D. The 12 Lean Gates of `origin-axiom` (Replacing the 50 Legacy Bureaucracy Gates)
Delete all 38 historical process/ratchet gates (`harvest-debt`, `relay-debt`, `carry-age`, `review-fires`, `DECLARED_DEBT`, `[PROCESS]` exemptions) and keep **12 zero-waiver gates**:
1. `graph-schema-and-acyclic-or-declared-loop` (validates `derivation_graph.yaml` + `R8` loop vs line classification);
2. `weakest-link-headline` (recomputes `k of 18 (j of n*)` from graph ancestry; fails if typed anywhere by hand);
3. `archive-sha-integrity` (verifies every `archive_provenance` SHA-40 / seal digest is well-formed and immutable);
4. `terminology-standard` (blocks untranslated internal bench slang in `src/`, 'graph/', `papers/`);
5. `framing-and-claim-ceiling` (scans *all* `.md`, `.tex`, `.py`, `.yaml` files for arrival overclaims while score `< 18`);
6. `dimensional-homogeneity` (`Guardrail 5`: all outputs/targets dimensionless; at most one unit anchor);
7. `mdl-trial-accounting` (`Guardrail 1`: charges selection bits & global trial count to every candidate match);
8. `no-serialized-blobs` (blocks `.jsonl`, `.npz`, `.npy`, `.pkl`, and any file `> 250 KB`);
9. `analytic-branch-safety` (blocks raw `mp.jtheta(2, ...)` principal-$q^{1/4}$ and `np.angle` branch-cut clustering without mod-$2\pi$ wrap);
10. `clean-checkout-hermetic` (runs in `git archive` tarball export — **zero `.git` runtime dependency**, closing `B1865`'s `PV9–PV13` & `PV22` permanently!);
11. `verify-package-binding` (every `theorem`/`exact_computation`/`output` node must bind a passing `verify_id` receipt from `origin-axiom-verify`);
12. `gate-mutation-selfcheck` (actually *executes* every gate against planted violations `DG1–DG6` + `MPV-1..MPV-6` on every CI run, closing `PV16`!).

---

### 5.3 Pillar 3 Specification: `origin-axiom-verify` (The Standalone World Verification Package)

> [!IMPORTANT]
> **Why `origin-axiom-verify` Is What Convinces Skeptical Referees Worldwide:** When a bold mathematical or ToE programme hands the world a repository where its own code tests its own code (`Cat 2`) or checks its own saved `.json` (`Cat 1`), referees dismiss it on sight. Handing the world a **`< 2 MB`, `< 60`-second standalone package** where every claim is recomputed from scratch by an **AST-isolated adversarial `@referee`** that shares **zero code** with `origin-axiom` transforms skepticism into instant respect.

#### Architectural Contract of `origin-axiom-verify`
1. **Strict Two-Room Code Isolation (`Guardrail 6`):**
   - 'claims_spec/' contains **only** a declarative JSON/YAML mathematical specification of the exact equations/identities/outputs exported from `origin-axiom` ('graph/derivation_graph.yaml').
   - 'referees/' contains **100% independent from-scratch implementations** using alternative algorithms wherever possible:
     - *Symbolic algebra vs exact modular arithmetic:* e.g., `sympy` polynomial/matrix rings cross-checked against `python-flint` / `Fraction` exact rational arithmetic;
     - *Quadrature / PDE cross-check:* P1 vs P2 finite-element harmonic-map solver on `m004` (`\tau_\infty`), Gauss–Legendre contour quadrature vs $q$-series on puncture norms;
     - *ODE cross-check:* `scipy` `DOP853` (`rtol=1e-13`) vs `mpmath` Taylor-series `odefun` (`30 dps`) on SM RGEs after passing the mandatory Buttazzo (`1307.3536`) & Xing–Zhou (`1804.01925`) benchmark gate (`Guardrail 4`).
2. **Compiled Under `guardrail_dsl` `v1.2` (`MPV-1..MPV-6` Built In):**
   - AST compiler refuses to run if any referee file imports `origin_axiom`, calls `open()`/`json.load()`/`subprocess`, contains a `BOTH-LITERAL` assert (`PV24`), omits 20-trial random Haar unitary basis-scrambling (`< 1e-12`) on flavour observables (`MPV-3`), or returns any `NaN`/`Inf` leaf (`G1`).
3. **One-Command Air-Gapped Execution & Cryptographic Certificate:**
   - Ships with `requirements.lock` (`pip install --no-deps --require-hashes -r requirements.lock`), a 25-line rootless `Dockerfile`, and `flake.nix`.
   - Running `python3 verify_all.py` completes in **`< 60 seconds`** on a standard laptop with zero network access and emits:
     - `VERIFICATION_REPORT.md` (clear pass/fail table of every Pure-Math Theorem, No-Go Theorem, Conditional Bridge, and `k of 18` SM status, with max numerical residuals and Haar scrambling deviations printed explicitly);
     - `VERIFICATION_CERTIFICATE.json` (deterministic SHA-256 hash of environment, referee ASTs, and computed outputs).

---

## 6. Modular Adoption Menu for `main` Seat (`What to Pick & In What Order`)

`main` does not need to adopt this proposal all-or-nothing. Each module below is cleanly separable so `main` can pick the strongest elements across seats:

| Module | What `main` Adopts | Plugs Directly Into `B1861` Wave | Effort | Value |
|---|---|---|---|---|
| **Module A: `MPV-1..MPV-6` + `guardrail_dsl` `v1.2`** | Add the 6 Mathematical-Physics Planted Violations (Haar scrambling, NNLO RGE benchmark, AST `@referee` sandbox, literal-return ban, non-dimensional ledger, MDL bits) alongside `cld`'s `PV9–PV27` fixes | `WP-0.7`, `WP-0.8`, `M3` | `2–3 days` | Eliminates the `52.7%` zero-math-in-test blind spot & RGE/basis bugs permanently |
| **Module B: Post-`B1862` Residual Bug Scrub** | Analytic-sheet $\theta_2$ module + `70`-site `jtheta` sweep + `B1825` addendum (`P-670`); `P-604` $\mathbb{Z}_{6k}$ + `B1859` `{1,4}` errata in `P3`/`metallic_one_object`/`B997`; `B805` + `the_price_is_twelve.py` + `run_suite.sh` (`pytest-xdist`, `OA_SLOW=1`); `B1246` Dirac Clifford `(P,C,T)` fix; `B1855` $\det d\sigma = +1$ note | `WP-0.1`, `WP-0.2`, `WP-0.3` | `2 days` | Makes `origin-axiom` (`main`) 100% green and mathematically clean before freeze |
| **Module C: Prototype `BP-1` (4D Lefschetz + Dai–Freed Loop)** | Sealed data-free computation of 4D Kas–Matsumoto intersection form, Meyer signature, `Spin^c` $w_2$, and APS $\eta_\rho(M_w^3)$ anomaly back-edge on $LR$, $R^2L^2$, $R^3L^3$, and $L^6 R L R$ | `R8–R11`, `WP-1.5`, `WP-2.*` (`B716`/`B1487`/`B1604`/`FK11`) | `3–4 days` | First candidate back-edge that genuinely passes `Test T0` and earns 4D chiral fermions without importing 4D |
| **Module D: Prototype `BP-2` & `BP-3` (Berry–Wilson + Ruelle–Mayer)** | Data-free Kähler–Berry parallel transport between $\sigma$-fixed harmonic fibres (`B1852` + `P-746`) + Ruelle–Mayer $\mathcal{L}_s$ `s=1` Selberg fixed-point operator (`R10` `A-all` + `X:WEIGHT`) | `WP-1.6`, `WP-3.*`, `WP-4.*` | `4 days` | Escapes the falsified single-$\tau$ `B1825`/`B1640` trap & fixes `A-all` weave measure with zero free parameters |
| **Module E: Immediate Tier-1 Pure-Math Harvest** | Package and release the 5 Tier-1A pure-math papers + 1 AI-Governance paper completely decoupled from open SM bridges | Independent of `M2`/`M3` | `1 week` | Secures permanent peer-reviewed mathematical credit immediately |
| **Module F: Execute Three-Pillar Public Repo Split** | Freeze `origin-axiom` → `origin-axiom-archive` (+ Zenodo sweep deposit), launch `<5 MB` standard-terminology `origin-axiom` (12 gates + `R5–R8` `derivation_graph.yaml`), and ship `<2 MB` `<60s` `origin-axiom-verify` | `M1` → `M3` public architecture | `5–7 days` | Delivers a crystal-clear, bulletproof public framework & world verification package |
