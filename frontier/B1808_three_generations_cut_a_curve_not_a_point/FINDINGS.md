# B1808 — THREE GENERATIONS CUT A CURVE, NOT A POINT (P-419, SELECTION BY INVERSION, IN B1804's HOLOMORPHIC FLUX FRAME; DATA-FREE): ONE LR-INVARIANT FLUX WITH INDEX −3 IS OF TYPE (1,1) EXACTLY ON A CURVE OF HIRZEBRUCH–ZAGIER FORM. A POINT NEEDS A SECOND FLUX, WHOSE INTEGERS ARE FREE, AND SUCH POINTS ARE INFINITELY MANY; THREE OR MORE INDEPENDENT FLUXES HAVE NO COMMON POINT. THE SAME HOLDS FOR EVERY NULL MATRIX TESTED, AND FOR EVERY GENERATION NUMBER. χ(L) IS NEGATIVE FOR EVERY INVARIANT (1,1) FLUX ON EVERY LR-HOLOMORPHIC COMPONENT; IN ONE FIXED ORIENTATION OF T⁴ THE INDEX IS −3 ON ℍ × ℍ AND +3 ON ℍ × ℍ⁻, SO THE HAND IS CHOSEN

**Verdict: NEGATIVE** for "the Standard Model's discrete datum 'three generations' selects the moduli" in this frame.
- The structure is **PROVED**: a lattice argument (§ 3), checked by computation (exact lattices and Möbius maps; points by
  floating-point roots, recounted exactly by the referee).
- The prediction was written on the frame card before the run (`verification/FRAME_CARD.md`: "infinite", prior 85%).

**What the result is.** It is a short corollary of B1804 § 4 together with U ⊂ Λ_A, which makes "three" play no special
role (§ 4). It is reported because P-419 is the owner's main line, and this frame was the one where flux pairs force
isolated points.

Data-free; none of the 19. cc (main), 2026-10-29, P-419. It is the first arc under WORKING_RULES' rule of 2026-10-29: the
frame card is its first file. Corrected before landing at its hostile referee (§ 6).

**0 of 19.**

## 1. The frame and the question (the card, in brief)

- **The frame (B1804 § 4).** T⁴ with A ⊗ I on H¹ = W ⊗ H. The complex structures on which A acts holomorphically are
  (τ₁, τ₂): abelian surfaces with real multiplication by ℤ[φ].
  - The period map Ω ↔ (1, τ₁) ⊗ (1, τ₂) (Segre) is injective.
  - Its image is the period domain of (Λ_A, Q): ℍ × ℍ and its conjugate ℍ⁻ × ℍ⁻.
  - The mixed components ℍ × ℍ⁻ and ℍ⁻ × ℍ form the period domain of (Λ_A, −Q). (The referee's q1, q3.)
- **The object's conditions.** LR-invariance (FORCED by the monodromy). Type (1,1) (holomorphy: the supersymmetric
  F-term choice, CHOSEN with the frame).
- **The inverted datum.** One matter line bundle L with ∣χ(L)∣ = 3, where χ(L) = c₁(L)²/2 (Riemann–Roch on an abelian
  surface). Reading the T⁴ index as the 4D generation number is CHOSEN (cf. I-34, UNEARNED).
- **The null, fixed in advance.** B_t = [[0, −1], [1, t]] for t = 4, 5, 6, 7.

## 2. Computed (`verification/three_generations_in_f2h.py` → `.json`; Λ_A by PARI's matkerint)

| matrix | Λ_A (rank 4) | det, signature | Q(w) = ∓6 classes (coefficients ≤ 3) | the (1,1) locus of a Q(w) = −6 class | of a Q(w) = +6 class (χ = +3 in ℍ × ℍ's orientation) | points on one Q(w) = −6 curve with a second class (coefficients ≤ 2): (w, u) pairs → distinct points | distinct saturated NS determinants (range) |
|---|---|---|---|---|---|---|---|
| LR | U ⊕ [[2, 1], [1, −2]] | 5, (2, 2) | 184 | a curve in ℍ × ℍ | a curve in ℍ × ℍ⁻ | 168 → **48** | **14** (3–60) |
| B₄ | U ⊕ [[2, 0], [0, −6]] | 12, (2, 2) | 194 | in ℍ × ℍ | in ℍ × ℍ⁻ | 138 → **62** | **21** (3–159) |
| B₅ | U ⊕ [[2, −1], [−1, −10]] | 21, (2, 2) | 156 | in ℍ × ℍ | in ℍ × ℍ⁻ | 364 → **110** | **36** (11–252) |
| B₆ | U ⊕ [[2, 0], [0, −16]] | 32, (2, 2) | 72 | in ℍ × ℍ | in ℍ × ℍ⁻ | 430 → **135** | **37** (12–383) |
| B₇ | U ⊕ [[2, −1], [−1, −22]] | 45, (2, 2) | 76 | in ℍ × ℍ | in ℍ × ℍ⁻ | 442 → **141** | **46** (11–540) |

- **The locus.** Each class w imposes w ∧ Ω = 0, i.e. τ₂ = M_w(τ₁), a Möbius map with
  det M_w = −(det Λ_A / 2)·Q(w) (an identity, the referee's q1). Its sign decides the component.
- **The last two columns** are the referee's exact recount (q2, q5). Main's script counted (w, u) pairs and printed
  det Gram(w, u), unsaturated and truncated to 40 values.
- **Disclosed.**
  - The first launch took the first class with ∣Q∣ = 6, which for four matrices had Q = +6. Its "no points" was that
    class's empty locus in ℍ × ℍ.
  - Its B₄ count of 160 included 22 spurious points from degenerate pairs (Gram determinant 0: a real double root split by
    rounding).
  - The script was corrected; the first launch's output is kept, its script is not (saved one second after that run).
  - The card's steps 3–4 (saturation, the CM field, tabulation by ∣det G∣) were done by the referee's recount, not by
    main's script.

## 3. Why (the lattice argument)

1. **The period is invariant.** Ω = dz₊ ∧ dz₋ is A-invariant, so the family is (one component pair of) the period domain
   of Λ_A, which has signature (2, 2).
2. **The invariant (1,1) classes at a point** are the orthogonal complement of the positive plane ⟨Re Ω, Im Ω⟩, a
   negative-definite plane in each component's complex orientation. A class with c₁² > 0 would make ±L an A-invariant
   polarisation, which a positive-entropy A forbids (B1804 r5). So **χ(L) = c₁(L)²/2 < 0 for every invariant (1,1)
   flux, on every A-holomorphic component.**
   - At a point of the curve the Hermitian form of c₁(L) has signature (1, 1), so h⁰ = h² = 0 and h¹ = ∣χ∣ (Mumford's
     index theorem; the referee): no vector-like pairs inside the bundle.
3. **Each class with Q(w) = −6 is (1,1) exactly on the complex curve {Ω·w = 0}**, of Hirzebruch–Zagier form
   aτ₁τ₂ + μ′τ₁ + μτ₂ + b = 0 with μ ∈ ℤ[φ]. It cuts the family to that curve and no further.
4. **A point needs a second class.** At an isolated point NS_A has rank 2 (it cannot be more: it is negative definite
   inside a signature-(2, 2) lattice), and it is the saturation of ⟨w, u⟩. Conversely, every negative-definite rank-2
   sublattice containing w fixes Ω up to conjugation.
   - w^⊥ ∩ Λ_A has signature (2, 1) and infinitely many primitive negative directions u′. Distinct planes give distinct
     points.
   - det NS = 6∣Q(u′)∣/k², with k = [NS : ℤw ⊕ ℤu′] dividing 6, so det NS ≥ ∣Q(u′)∣/6 is unbounded. The points stay
     infinite modulo any isometry group.
   - Three or more linearly independent invariant fluxes have no common (1,1) point (rank ≤ 2).
5. **The hand.** The complex orientation agrees with the fixed e₀₁₂₃ on ℍ × ℍ and ℍ⁻ × ℍ⁻, and is opposite on the mixed
   components. So the index in the fixed orientation, Q(w)/2, is −3 on the first pair and +3 on the second.
   - The 4D hand depends on how T⁴'s orientation is tied to 4D's: it is CHOSEN, together with the component.
   - For LR, and not for B₄–B₇, the components are exchanged by γ = M ⊗ E_xx + I ⊗ E_yy. Here M = [[0, 1], [1, 1]],
     M² = LR and det γ = −1; γ commutes with LR ⊗ I and reverses Q on Λ_A (the referee's q3).
   - For B₄–B₇, Λ_A ≇ Λ_A(−1). Their Q = ∓6 counts in the box are unequal; LR's are 92 and 92.

## 4. What it means

- **Selection by inversion fails in this frame.** The generation count confines the moduli to a curve. A point needs a
  second flux with free integers (B1804), and such points are infinitely many. Three or more independent fluxes have no
  common point.
- **"Three" plays no special role.** U ⊂ Λ_A represents every even integer, so every generation number gives the same
  structure. The negative is a short corollary of B1804 § 4 together with U ⊂ Λ_A.
- **Not specific to the object.** The structure is the same for every null matrix tested (E20). For LR alone, the two
  orientations are exchanged by LR's own square root.
- **The hand is CHOSEN.**
- **Bearing on P-425 (the referee's note, not a selection).**
  - On w's curve, the least saturated NS determinant is 3: the lattice A₂(−1), B1804's point with CM by
    ℚ(√5, √−3) (the record's compositum).
  - A₂(−1) holds three pairs of norm −6 vectors, so that point lies on Q = −6 curves. It is one of infinitely many such
    points.
- **What it does not touch.**
  - The Yukawas.
  - Further discrete data (the doublet–triplet split, matter parity).
  - The frame's missing invariant Kähler class. Note: the real-multiplication plane gives Kähler classes with J·F = 0
    for every invariant flux; what fails is only A-invariance of J (the referee's q6; read B1804's "D-term half
    unavailable" that way).
- **For P-419:** this frame is closed for "the generation count". The card list's other frames remain: F-theory matter
  curves and an E₆ meeting point (P-415).
- **0 of 19.**

## 5. Scope

- One U(1) bundle, on the LR-holomorphic components.
- The T⁴ index as the 4D generation number is CHOSEN (cf. I-34). On T⁴ alone, 8D SYM's bulk matter is vector-like
  (N = 2); a chiral count needs a completion (e.g. a mixed sector on T⁴ × T², Cremades–Ibáñez–Marchesano), to be read at
  source.
- "Hirzebruch–Zagier" is the form of the equation. The referee's reading N = det M_w = 15, i.e. T₁₅ in van der Geer's
  normalisation, is a lead to check at source, not a claim.

## 6. The referee (hostile, read-only; `verification/referee/`)

**Its verdict:** BLOCK on one finding, then PASS WITH CORRECTIONS. All applied.

**Verified by it, with code independent of main's:**
- Λ_A (det t² − 4, signature (2, 2), U ⊂ Λ_A);
- the class counts;
- the example points (to 10⁻¹⁰);
- the period map;
- orientation under conjugation;
- the point argument, which has no gap.

**Blocking: "the chirality's sign is opposite between the components"** was false for χ. χ < 0 on every component; what
flips is Q(w)/2 in a fixed orientation (§ 3.5).

**Corrections:**
- the last column (pairs, not points; saturated determinants; B₇'s truncation);
- the index bound (index²);
- the physics scope (C3);
- "exact" → "by computation", with two further disclosures;
- det M_w as an identity;
- § 4's wording;
- the Seen first.

**Main's verification:** the referee's q1–q4 regenerate byte-identically on main, and q5 and q6 rerun with their stdout
kept. The hand's correction was checked by hand: Hodge index in each component's own complex orientation.

## Seen first

`VERDICT topic-sweep /Hirzebruch|Noether.Lefschetz|three generations.{0,40}flux|magneti[sz]ed/ (full text): 7 arcs, 3
register rows` (P-095, P-401, P-419).

**Bearing on it:**
- B1804 (the frame);
- B1496 (three as an index obtained by selection);
- B1794 (bundles on the 3-manifold frame);
- B1800 (three from flux-one Wilson lines on T², not flux three);
- THE_WEAVE's W46 (a 4D index of ±3 on M₁,₂, given the cusp unit);
- I-34 (the index read as the generation count, UNEARNED);
- P-401, P-419, P-425.

None computed the generation count's locus in this frame.

**Literature:**
- Donagi–Wijnholt (arXiv:0904.1218);
- Hirzebruch–Zagier cycles (form only);
- Cremades–Ibáñez–Marchesano (scope only).
