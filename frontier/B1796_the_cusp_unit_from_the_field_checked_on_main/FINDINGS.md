# B1796 — THE CUSP UNIT FROM THE FIELD, CHECKED ON MAIN (C8; P-288, P-298, R71-3): THE SM SEAT'S W130, AS FAR AS CHECKED, AND ITS W123 (THE EXACT ROUTE) HOLD. THE FIBRE'S FUCHSIAN POINT (3, 3, 3) — THE MODULAR TORUS — IS NOT UNITARY, SO ITS HIGGS FIELD IS NOWHERE ZERO. m UNITS OF END DATA ON THE THREE EIGENLINES GIVE A WEIGHT-3/2 HIGGS SPACE OF DIMENSION max(0, m_P + m_M + m_N) ON EVERY VECTOR CHECKED — 3n FOR O(nδ). SO FK10'S UNIT REDUCES TO THE FIELD'S EXISTENCE, A TYPE IDENTIFICATION, UNIFORM END DATA AND THE LEAST REMAINDER, NONE DERIVED

**Verdict: PROVED** (a verification on main of the claims listed in § 1 and § 2, from definitions and with main's own
code; no data). cc (main), 2026-10-28. It pays an item carried since Review 68 (R68-6 → R69-6 → R70-3 → R71-3; P-298),
with P-288, the completion map's C8. Corrected before landing at its hostile referee (§ 5). **0 of 19.**

## 1. W130: what main checked, from definitions (`verification/w130_check.py`; the seat's code not read)

- **The point.** (3, 3, 3) is a Fuchsian character of the once-punctured torus: the modular torus ℍ/Γ′, with
  Γ′ = SL(2, ℤ)′ and a hexagonal conformal structure. The Fuchsian locus {x² + y² + z² = xyz, all > 2} is
  two-dimensional; for example (2√2, 2√2, 4) is the square torus. Nothing below depends on the choice.
  - κ = x² + y² + z² − xyz − 2 = −2, so the commutator is parabolic.
  - An explicit pair: A = [[1, 1], [1, 2]], B = [[1, −1], [−1, 2]]. Both lie in SL(2, ℤ)′, with traces 3, 3 and
    tr AB = 3.
  - Their commutator is [[−1, 0], [−6, −1]], −1 times a unipotent: a cusp of width 6. This matrix is in the seat's W130
    (its H1, "the puncture").
- **Not unitary.** A's eigenvalues (3 ± √5)/2 are off the unit circle. Every element of a conjugate of SU(2) has trace
  2 cos t ∈ [−2, 2], so no positive-definite Hermitian form is preserved. (A and B lie in SL(2, ℝ), so they do preserve
  an indefinite one, [[0, i], [−i, 0]].)
- **So the field cannot vanish.** This needs no deep theorem: for any Hermitian metric h, the flat connection splits as
  D = ∇_h + Ψ_h, and Ψ_h = 0 iff D preserves h. A non-unitary holonomy therefore gives Ψ_h ≢ 0 for every h, and in
  particular for the harmonic one (non-abelian Hodge: Hitchin, Donaldson, Corlette, and Simpson 1990 for the tame
  punctured case). For the uniformisation ∣Φ∣ is constant, so the field is nowhere zero.
- **Its size, with the convention stated.**
  - The setting: on the punctured torus the SL(2) Higgs bundle is parabolic, with weight ½ at the puncture.
    K^½ ⊕ K^−½ is the closed-surface description, and the computation below is local.
  - Hitchin's equation on the first line, with h = diag(μ^−½, μ^½) and Φ the unit section, is the Liouville equation.
    The ansatz μ = k v^p forces p = −2 and k = ¼, i.e. curvature −4, Hitchin's own value.
  - The wrong sign of [Φ, Φ*] has no positive solution.
  - In curvature −1 units the size depends on how a 1-form is normed (the referee's table, `verification/referee/
    w130_ref_run.txt`):

    | convention | ∣Φ∣² | ∫∣Φ∣² |
    |---|---|---|
    | ∣dz∣² = 1/λ (the seat's and this arc's) | ¼ | π/2 = π(−χ/2) |
    | the Riemannian norm, ∣dz∣² = 2/λ | ½ | π |
    | Hitchin's ‖Φ‖² = 2i∫tr Φ ∧ Φ* | 1 | 2π |

  - **The convention-free statement:** 2i·tr(Φ ∧ Φ*) is the hyperbolic area form pointwise, i.e. the harmonic map is the
    identity isometry.
- **Not checked on main:**
  - the seat's 5 461 images and five other Fuchsian points;
  - that the quaternion point and the matter's flat data are unitary;
  - "exactly one field";
  - its H3 (closing the hole forces Φ = 0) and H4 (the doublet).

  The web seat's independent check (row 1310) covers H0–H4. Main's check is H0 (Hitchin's equation), H1 (the puncture)
  and H2's size.

## 2. W123: checked with main's own code (`verification/w123_check.py`; B1691's module, B1700's conventions)

**The setting.** A weight-3/2 section of ρ_T (= ρ_R, B1634) is f₀R + f₁∂R + f₂∂²R with f_j ∈ M_* (B1691's free module,
complete since W(R, ∂R, ∂²R) = 8η⁹ is nowhere zero). With m_P, m_M, m_N units of end data on the eigenlines P, M = v₊ and
N, its orders in x = q^⅛ must be at least (1, 7, 3) − 8m (B1700's canonical exponents). Building at weight 3/2 + 12N with
N = max(0, max m) is enough: negative entries only raise the bounds, and the referee's recomputation at N + 2 gives the
same dimension.

**The results, exact over ℚ(i):**

| end data | dimension of the weight-3/2 Higgs space |
|---|---|
| uniform, O(nδ), n = 0, 1, 2, 3, 4 | 0, 3, 6, 9, 12 — **3n** |
| per line, all 64 vectors m ∈ {−1, 0, 1, 2}³ | **max(0, m_P + m_M + m_N)** in every case |

**Two independent reproductions** (the referee's, `verification/referee/`):
- *Its own q-series code, using no B1691 code:*
  - n ≤ 6 gives 3n;
  - all 1 000 vectors in {−4, …, 5}³ match;
  - 345 unbalanced vectors up to (12, −12, 0), (12, −6, −6) and (12, 12, −24) match.
- *An independent theta-polynomial route,* with no free module: G = θ₂θ₃θ₄·F as polynomials in θ²'s modulo Jacobi's
  relation, with the S and T laws imposed directly.
  - The dimension of the equivariant space equals the free-module count at every weight from −1/2 to 51/2.
  - The 64-entry table matches.
  - Its control (the S sign flipped) drops every count to 0, so the route can fail.

**Why 3n for every n:**
- the candidates number dim M_{12n+2} + dim M_{12n} + dim M_{12n−2} = n + (n + 1) + n = 3n + 1;
- on P and N the orders already meet the bounds: R, ∂R and ∂²R have orders (1, −1, 3), (1, −1, 3) and (9, −1, 3);
- on M every power is ≡ 7 (mod 8), so the one condition is the coefficient of x⁻¹;
- that condition has rank one, since ∂R·E₄^{3n} carries it;
- so the dimension is 3n. With B1641's χ_{3/2}(ρ_T) = 0, this is Riemann–Roch with no h¹ correction.

**Half of the per-line formula is proved for every m** (the referee's argument): Σm ≤ 0 ⇒ d = 0.
- The Wronskian of a section F has weight 21/2, so its order at the cusp is ≤ 7/8.
- But that order is at least the sum of F's line orders, ≥ 11/8 − Σm.
- So for Σm ≤ 0 the Wronskian vanishes identically, which forces a constant linear relation among F's components.
- ρ_T is irreducible, so no such relation exists: the T-eigenvalues are distinct and S moves P off every eigenline.

**Not proved in general:** d = Σm for Σm > 0 (h¹ = 0). It holds on every vector computed.

**The seat's history, disclosed.**
- The seat's table that main matches is its exact second route, post hoc and labelled so. This is its commit
  9a6e39c01, the dossier file the_higgs_route_exact.json on the seat's branch, sha256 9f50ff38…, kept here as
  `verification/seat_the_higgs_route_exact.json` and read as data.
- The seat's original run disagreed on 19 of the 64 entries, e.g. (2, 0, 0): run 3, exact 2.
- Its reading was reversed the same day, from "route 1 does not force three" to "n = 1 and three".
- **Main agrees with the exact route, not the original run.**
- The agreement is order-independent: the formula is symmetric, and the seat puts v₊ last.

## 3. The chain, and what it rests on

**As mathematics:**
- the point's field is nowhere zero (§ 1);
- a non-zero weight-3/2 Higgs needs end data with m_P + m_M + m_N ≥ 1 (§ 2);
- the least per-line datum gives one dimension: ∂R with the unit on v₊ alone, B1700;
- the least datum that distinguishes no eigenline is O(δ), and its space is three-dimensional. That space is the sheaf
  whose index is W46's three (B1641, −χ_{27/2}(ρ_T) = −3), and it contains ∂R (B1700). B1700 tagged the Higgs/zero-mode
  coincidence "a reading, not a claim". Any per-line datum with Σm = 3 also gives three; O(δ) is the uniform one.

**So FK10's tagged unit (GENESIS v1.39) follows from, and in that sense reduces to, the following. None of them is derived
here.**
1. **The field's existence — FK15 proper.** It is OPEN (GENESIS FK15): settled only by a derivation from PF1–PF3 or by
   adopting PF4. W130's "forced" is PF1 read on the fibre's rest state, which is the seat's reading.
2. **The type identification.** W130's field is End E ⊗ K on the fibre. The section is a weight-3/2 vector-valued form of
   ρ_T on the τ-line. That the first's non-vanishing forces the second to be non-zero is not shown.
3. **Uniform end data:** O(nδ) rather than a choice per eigenline.
4. **The least remainder:** n = 1 as the minimum.

**And under the record's standing conditions:**
- **given Λ** (GENESIS FK10; B1700);
- **the record's hand,** not derived (GENESIS v1.41, v1.42; B1640). For the conjugate hand weight 3/2 is not allowed at
  all: there is no space and no three.

**That the three are generations** is FK11. On M₁,₂ GENESIS v1.39 says FK11's earning condition is met conditionally,
given Λ and the unit. B1604's unearnability concerns threads and covers of threads. P-298 and row 1309 name FK11 here as
the map from the fibre's SL(2) to the weak SU(2).

**No input removed. 0 of 19.**

## 4. What it means

- **R71-3 is paid,** carried four reviews: main's own check of W130's points above.
- **P-288's verification half is paid:** W123's exact route, the per-line table, the proof of its Σm ≤ 0 half, and two
  independent reproductions.
- **Its GENESIS half** — that FK10 reduces to (1)–(4) under the standing conditions — is a foundation-document sentence.
  It goes to a GENESIS amendment through adoption/amend.py, carried by P-288, and is not written here.
- **For P-401 and B1794.** B1794's scope is L250's frame; it found no rational class in that frame's bulk. This arc joins
  the record's end-integer results:
  - B1290: net chirality = −χ(∂⁺M), "a question about the cusp";
  - B1487 and B1491 with FK14: generations counted by ends;
  - B1708, B1710 and B1715 with FK10 v1.53–v1.54: units of end data on the closed 4d vacua in multiples of 12;
  - the seat's W127: the least replacement at the empty end fixes I = −1.

  Here the end datum is fixed as the least for which the field can exist, and three follows exactly — a reduction of a
  postulate, not a derivation.

## 5. The referee (hostile, read-only; `audit/referee_b1796/`, scripts kept in `verification/referee/`)

The mathematics holds. Both scripts rerun byte-identical, and two independent routes reproduce W123.

**Blocking, applied:**
1. The draft's "the one place on the record where an integer is fixed at the end" was false on the record. It is replaced
   by the list in § 4.
2. "FK10 is equivalent to three things" was false (FK10 does not imply them). It now reads "follows from / reduces to".

**Corrections, applied:**
3. Only positive-definite forms are excluded.
4. *A* Fuchsian point, the modular torus.
5. The size's convention, with the invariant statement.
6. The parabolic structure at the puncture.
7. The commutator matrix is W130's, not W128's; row 1309 is W130's.
8. The scope of what main checked of W130.
9. W123's history: the exact route, the original run's 19 disagreements, the same-day reversal.
10. The formula's range, and the proof of its Σm ≤ 0 half.
11. "Three needs O(δ)" was false by the formula. Any Σm = 3 gives three; O(δ) is the uniform least datum.
12. The chain's conditions: FK15 split from the type identification; given Λ and the hand added; FK11 as GENESIS v1.39
    has it.
13. The GENESIS vehicle is P-288, not P-237 (DONE, v1.52).

**Notes, applied:**
- non-abelian Hodge is not needed for "cannot vanish";
- the glosses: B1629's "not dynamical" in GENESIS v1.44's scoped form; W45 verified in B1632 and B1634; "one generation"
  is W123's wording.

## Seen first

`VERDICT topic-sweep /cusp unit|unit of end data|end data|O\(n.?δ\)|W123|W130|non-abelian Hodge|uniformi[sz]ing Higgs|least remainder|FK10|FK15/ (full text, aliases: the cusp's unit): 87 of 1543 arcs on main match (NEGATIVE 19, PROVED 67, no verdict file 1); 44 register rows match (DONE 27, LEAD 1, QUEUED 16)`.
- **Bearing on it:**
  - B1290 (net chirality at the cusp);
  - B1487 and B1491 (FK14);
  - B1604 (FK11 on threads);
  - B1629 (GENESIS v1.44's scoped form);
  - B1632 and B1634 (W45; ρ_T = ρ_R);
  - B1640 (the hand);
  - B1641 (W46; χ_{3/2} = 0);
  - B1691 (the free module);
  - B1700 (n = 1 exactly; ∂R in the unit's space);
  - B1708, B1710 and B1715 (units in multiples of 12);
  - B1794 (L250's frame).
- **The register:** P-288, P-298; the completion map's C8.
- **The SM seat:** W123 (row 1301), W127 (row 1307), W130 (row 1309). **The web seat's check:** row 1310.
- **Literature:**
  - non-abelian Hodge: Hitchin 1987, Donaldson 1987, Corlette 1988, Simpson 1990 (tame, punctured);
  - the free module of vector-valued modular forms: Marks and Mason; Bantay and Gannon.

## Files

- `verification/w130_check.py` → `w130_check_run.txt`.
- `verification/w123_check.py` → `w123_check_run.txt`, reading `seat_the_higgs_route_exact.json` (the seat's output, as
  data).
- `verification/referee/`:
  - `w130_ref.py` → `w130_ref_run.txt`;
  - `fm_route.py` → `fm_route_run.txt`;
  - `fm_extremes.py` → `fm_extremes_run.txt`;
  - `theta_poly_route.py` → `theta_poly_run.txt`;
  - `theta_poly_control.py` → `theta_poly_control_run.txt`.

The lock: `tests/test_b1796_the_cusp_unit_from_the_field_checked_on_main.py`.
