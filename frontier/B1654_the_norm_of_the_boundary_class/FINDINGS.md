# B1654 — THE NORM OF THE BOUNDARY CLASS: the parity Higgs's only massless mode needs an end cutoff; under equal canonical amplitudes the cutoff's log cancels by Jacobi, and the first generation's lift is D(τ)/(2πL), with D = ∫ Σ_r R_r²|S_r|² finite, zero at τ = ω and falling like Im τ·|q| at the cusp; under equal framed data there is no lift

**Verdict: PROVED.** Every cell holds as sealed. cc (main), 2026-10-15.

> *Sharpened 2026-10-16 (S141). The cusp law in §2 holds as written on Re τ = 0 and its integer translates. That is where its cells test it (τ = 4i, 5i). For τ = x + iy the leading term is D/(q‖R‖²) ≈ e^{−iπx/2}[8π²y + 4π(1 + e^{−2πix}) − 32π ln 2], with q = e^{iπτ}. So ∣D∣/‖R‖² falls as ∣q∣·∣8π²y + 4π(1 + e^{−2πix}) − 32π ln 2∣. The factor 8π²·Im τ·∣q∣ is unchanged; only the constant depends on Re τ. Checked by `papers/P9_what_a_grammar_fixes/checks/cusp_law.py`, with this arc's own route A: relative deviation 2.8 × 10⁻⁵ at y = 4 and 1.2 × 10⁻⁶ at y = 5, at x = 0, 3/10, 1/2, 1. The slip was reported by two lines of work reading the paper (the SM seat's §149, the web seat's paper read). No verdict changes.*
- Sealed `155959126` (sha256 9572fd2c) before the run. The output was committed unread at `cd3c046ae` (one run, 88 s,
  exit 0).
- No data. **0 of 19.**
- POINT_REGISTER P-151, the first arc of C at the owner's "B then C" (P-150). It bears on P-129's second half and P-146.

## 0. Seen first

As sealed:
- `VERDICT topic-sweep /tame higgs|…|higgs.s profile/: 7 of 1425 arcs on main match (NEGATIVE 2, PROVED 5)`;
- `VERDICT topic-sweep /boundary class|…|one normali[sz]ation/: 9 of 1425 arcs on main match`.

None normalises the boundary class.
- **Read before the seal:** the SM seat's C0 (a (0, 1) Higgs; no normalizable massless Higgs carries a parity; "one
  normalisation serves all three"), §107, §110, W61, W72 and W73; the web seat's T-NORM, step 3a and its audit of its
  negatives; B1642–B1653; B1651's second addendum.
- **Literature:** the Szegő kernels of the even spin structures; S_r² = ℘ − e_r; Jacobi's identity; Kaluza–Klein
  normalisation; regularised norms of non-L² harmonic forms. Nothing here is claimed as new mathematics. What is new on
  the record is the cancellation, its function D(τ), and what it does to the first generation.

## 0b. Disclosed

In full in the preregistration's §0b. In brief:
- **Main's exploration** saw the values the cells read: c_r and D at the six named points, the cusp trend, and a coarse
  grid.
- **Two passes of read-only reviewing agents** before the seal.
  - The first found that N4's control (a) vanished at τ = i (fixed), plus robustness and text items. It also found the
    cutoff-free form of D and the closed-form cusp constant K.
  - The second found boolean flags written as strings, output paths, provenance, and the blindness ledger, all fixed.
  - Between them they replicated N0, N3, N4, N5(a, b) and N6 before the seal; those cells were not blind.
- **Main caught one error of its own revision before the seal.** The O(1) term of Σ R_r²|S_r|² near the puncture is
  bounded, not O(|z|²).
- The reviewers' scripts and the v1 draft are kept beside the seal.

## 1. The sealed run (`verification/the_norm_of_the_boundary_class.py`, unchanged; `.json`, `_run.txt`)

**N0, plumbing** (void below threshold):

| check | value |
|---|---|
| numpy series against jtheta | 3.3 × 10⁻¹⁶ |
| S_r² − S_s² constant in z | 2.2 × 10⁻³⁹ |
| θ₁′(0) against 2πη³ | 9.2 × 10⁻⁴¹ |
| R·R (40 digits; numpy) | 1.1 × 10⁻⁴²; 2.7 × 10⁻¹⁶ |
| the channel assignment against B1651's pairing | 5.1 × 10⁻¹⁶ |

| cell | prediction | prior | result |
|---|---|---|---|
| **N1**, the universal log | ε-spread < 10⁻⁹; the residue-2 control drifts by 6π·log 10 per decade | 99% | **HOLDS:** spread 1.9 × 10⁻¹¹; control/6π in [1 − 1.3 × 10⁻¹⁵, 1 + 1.7 × 10⁻¹²] |
| **N2**, two routes | c_r by A and B agree < 10⁻⁸ at six points | 95% | **HOLDS:** 1.2 × 10⁻¹⁰ |
| **N2b**, D without a cutoff | ∫_P Σ R_r²\|S_r\|² = Σ c_r R_r² < 10⁻¹⁰\|R\|² | 97% | **HOLDS:** 1.6 × 10⁻¹⁴ |
| **N3**, symmetry | ω: c₂ = c₃ = c₄; i: c₂ = c₄, \|c₃ − c₂\| > 1; control at t1: all differ > 0.1 | 99% | **HOLDS:** 1.4 × 10⁻¹⁴; 0.0 and 2.178; 1.019 |
| **N4**, the cancellation made visible | u·u independent of L and equal to D; the channel-3 cutoff shifts it by −2π·ln2·R_k²; R′ grows with L | 99% (a demonstration) | **HOLDS:** ≤ 3.3 × 10⁻¹⁶; shifts 0.43–12.3 \|R\|², signed to 3.7 × 10⁻¹⁵; R′'s slope 1.0 |
| **N5**, D's zero and its cusp | (a) \|D(ω)\| < 10⁻¹⁰\|R\|²; (b) > 0.1 at i, t1, t2; (c) grid > 0.05 away from the corners, and the corner control in [1.8, 3.4]; (d) slope 8π² within 10⁻³, deviation from K < 2 × 10⁻³ at 5i | 88% | **HOLDS:** 4.5 × 10⁻¹⁵; 0.414; far minimum 0.162 at (±0.5, 2.0), corner slopes 2.70 and 2.93 at the four nodes; slope 8π² × 1.00009, deviation −4.2 × 10⁻⁴ |
| **N6**, the masses | (a) m₁ = 0 at ω; (b) m₁ = 0 under P4′; (c) L·m₁/m₃ → the limit within 2%; (d) the angle ∝ 1/L within 3%, the GST ratio halving 0.5 ± 0.05 | 90% | **HOLDS:** ≤ 2.5 × 10⁻¹⁶; ≤ 1.9 × 10⁻¹⁶; ≤ 1.8 × 10⁻⁴; 0.9995–1.0064; 0.4999–0.5034 |

**D at the named points** (D/|R|², by the cutoff sum and, identically, by the direct integral):

| ω | i | t1 = 0.13+1.07i | t2 = 0.3+1.6i | t3 = 2.2i | t4 = 3.0i |
|---|---|---|---|---|---|
| 0 (4.5 × 10⁻¹⁵) | 1.0888 | 0.9956 − 0.0289i | 0.3965 + 0.1187i | 0.1277 | 0.0155 |

**The cusp.** D/(q|R|²) = 271.27 at 4i and 350.23 at 5i, against 8π²y + K with K = 8π(1 − 4 ln 2) = −44.550.

## 2. The read-outs

- **The channel norms** c_r(τ) at the six points are in N2's record. At ω they are all −2.94582; at i, c₂ = c₄ = −1.70156
  and c₃ = −3.87915.
- **The first generation under the canonical end condition** (P4), at L = 2560 against the limit
  |a·a|·|D|·|a·R|/(2πσ₁²σ₂):

  | τ | direction | L·m₁/m₃ → | m₂/m₃ | m₁/m₃ at L = 40 |
  |---|---|---|---|---|
  | i | random 1–3 | 0.159, 0.143, 0.126 | 0.57, 0.27, 0.58 | 3.2–4.0 × 10⁻³ |
  | i | near the cone | 0.171 | 0.0188 | 4.3 × 10⁻³ |
  | t1 | random 1–3 | 0.144, 0.136, 0.114 | 0.55, 0.27, 0.55 | 2.9–3.6 × 10⁻³ |
  | t1 | near the cone | 0.159 | 0.0745 | 4.0 × 10⁻³ |

  - In the bulk of the domain the lift is about 0.15/L.
  - It is smaller only near ω, where D vanishes linearly (2.70–2.93 per unit distance at the grid's corner nodes), or
    toward the cusp, as Im τ·|q|.

## 3. What it says

- **C's first candidate is gone, and its question is answered.** The parity Higgs's only massless mode is the boundary
  class (C0), and its norm needs an end cutoff. What the zero does depends on which end condition is physical:
  - **Equal framed data** (P4′, C0's "one normalisation serves all three") give u = R, and the first generation stays
    massless at every τ.
  - **Equal canonical amplitudes** (P4) give u_r = √(2πL + c_r)·R_r. The cutoff's log cancels by Jacobi (R·R = 0), and
    the lift is u·u = D(τ), a finite function of τ alone.
- **D is canonical.** It needs no cutoff: D = ∫_P Σ_r R_r²|S_r|² dA, with a bounded integrand, because Jacobi removes the
  1/|z|² and O6 removes one of the two O(1) terms. It does not depend on the cutoff's shape or the coordinate's scale.
  |D|/|R|² is modular invariant (by hand, and checked by the reviewers at several images; not a sealed cell).
- **D vanishes at τ = ω**, the record's symmetric point, where the order-3 move makes the three norms equal. There the
  two end conditions agree, and the first generation is massless under both. That is B990's law once more: the
  symmetric point gives no lift. Elsewhere in the domain |D|/|R|² is of order one. Toward the cusp it falls as
  |q|(8π²·Im τ + 8π(1 − 4 ln 2)).
- **So under the canonical end condition, the first generation's lift is small for two reasons:** the end datum L
  (m₁/m₃ ≈ 0.15/L in the bulk), and τ's distance from ω or from the cusp. This is a lift that stays small, as the web
  seat's audit says P-128 needs. It costs one end datum, L, instead of three framed data.
- **The lift is diagonal along R.** The light state's angle from R is of the order of its own mass ratio (∝ 1/L), not its
  square root, so this lift is not the Gatto–Sartori–Tonin texture. Context, not a test: nature's θ_C ≈ √(m_d/m_s) is
  that texture. If GST is nature's, the canonical end condition alone does not give the Cabibbo angle (P-129).
- **T-NORM for the matter (§1.11 of the preregistration, by hand):** the generations live in different flat bundles,
  so their physical L² metric is ‖F‖²·I₃. Only the Higgs needs a cut.
- **What it does not show:**
  - which end condition is physical (P4, P4′ or P4″): the parent's clauses 4 and 6;
  - L, τ, or the Higgs's direction;
  - whether the vacuum factorises;
  - anything with a hypercharge line (the next arc: the twisted channels per sector, whose L-independent ratios across
    sectors are the first place a structural number could appear);
  - any value.

## 4. Credit

- **The SM seat:** C0, the boundary class and "one normalisation serves all three", which framed this arc; and §107's
  log divergence.
- **The web seat:** T-NORM, and the audit that named what P-128 needs: a lift that stays small.
- **Main's two read-only reviewing agents:**
  - the first: N4's design error, the cutoff-free D, the closed-form cusp constant, the robustness fixes;
  - the second: the flags, the paths, the provenance, and an honest blindness ledger.

## 5. Next

The twisted channels, per sector (the next C arc). With a flat hypercharge line, B1653's twisted pairing gives each
sector its own channel kernels and its own D. The ratios of the first generation's lifts across up, down and leptons do
not depend on L. They are the first place this frame could give a structural number. They also bear on the parent's
clause 7, splitting the down quarks from the charged leptons.

## Addendum (2026-10-16, Review 64): four reviewer helpers changed after the seal, already disclosed, now in the seal check's form

- Four helper scripts kept beside the seal were changed after it, at S131 (`bc9c815ec`):
  - `verification/before_the_seal/review/pre.py`;
  - `verification/before_the_seal/review/s23_names.py`;
  - `verification/before_the_seal/review2/blocks.py`;
  - `verification/before_the_seal/review2/pre2.py`.
- **What changed.** Each read the instrument from the draft room by an absolute path (an E80 instance), which also broke
  the no-absolute-paths rule. The repair points them at the arc's own copy by a relative path, and nothing else in them
  changed. The sealed instrument, the preregistration and the output are untouched.
- **S131 disclosed it** in `ARTIFACT_HASHES.txt`, with a dated comment and the four current hashes. The sealed hashes,
  however, stayed on plain lines, and this page did not name the files. Review 64's seal check (R61-4's rule) therefore
  read the change as undisclosed.
- **The repair.** The sealed hashes are now `# sealed at` lines, and this addendum names the files. Nothing else changed.
