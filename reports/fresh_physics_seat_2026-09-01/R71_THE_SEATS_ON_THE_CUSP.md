# R71 — THE SEATS ON THE CUSP: the SM seat's "no", main's parity theorem and this seat's ±2 are one picture; the θ-odd "no" is exact (region swap, no leading-mode assumption); R70 corrected — on the θ-even directions the ±2 is vector-like **or anomalous**, never a spectrum

**Seat:** fresh physics seat (fc) · **Date:** 2026-09-06 · **Status:** seat report + one correction at source (R70 §2 banner), not banked. Scripts `computations/r71_seats_on_the_cusp.py` (run record `..._run.txt`, ~2 min) and `computations/r71_theta_even_pairing.py` (run record, ~3 min); both `SELFTEST: PASS`. Also restored: `computations/r61_fast.py`, the helper R62's script imports, which lived only in this seat's scratchpad — R62 was not reproducible from the branch until this commit (defect, fixed).

Fetched and read at: main `2901ae9f` (B1290 index formula applied, `CC_TO_FC_2026-09-06_THE_QUESTION_MOVED_TO_YOUR_CUSP.md`, B1291 parity theorem), SM-derivation branch `6f077ef2` (B1277 addendum "the arcs and the corners", B1279 symmetries on the SM lines), codex `f7a49536`. Arc numbers below are as they stand on each branch; main's `CC_TO_ALL_SEATS_2026-09-06_ARC_NUMBER_RESERVATION.md` governs any collision.

## 0. What each seat said, and what the object says to all three

The owner asked all seats the same question: *do the two Fix(θ) arcs give χ(∂⁺M) ≠ 0? Arcs cut corners.* Three answers came back on three benches:

| bench | object examined | answer |
|---|---|---|
| SM seat, B1277 addendum | the sign regions on the cusp torus of a **smooth θ-odd** Higgs field (the b₁ class dual to the meridian) | **no**: the leading symmetry-allowed mode is sin(4πx), regions annular, χ(∂⁺M) = 0 — with a caveat if the (±2,0) coefficient vanished (then "±4") |
| main, B1290 + B1291 | the index formula on m004, and the fixed sets of finite-order isometries with one cusp | net = −χ(∂⁺M); annular ∂⁺ gives 0; \|Fix on the cusp\| is even, so 3 is excluded with one cusp; escape ≥ 2 cusps |
| this seat, R69 + R70 | Fix(θ) as a **singular θ-even charge locus** (two arcs, χ = 2) | **yes, ±2** as a count; then (R70) vector-like on the θ-even directions |

All three are right about their object, and they are three faces of one statement, which this report makes exact:

> **On m004 the cusp cannot supply a chiral spectrum by any of the routes examined.** A θ-odd field gives χ(∂⁺M) = 0 identically (§2, exact — no leading-mode assumption). A θ-even singular locus gives a count of ±2, and on every one of 928 θ-even directions tested the resulting left-handed spectrum is either vector-like under the non-abelian unbroken group or carries a nonzero SU(3) cubic anomaly (§3) — so it is not the spectrum of any consistent configuration. The parity theorem (§1) says the same count is ≤ 2 in absolute value on any one-cusped manifold.

> **Banner (R72, 2026-09-06).** §0's headline and §3 hold under the record's *outer* lift of θ to E₆ (θ_D, B353). B353's item (B) shows the involution also lifts *inner* (Ad(ι(N)), type A₅⊕A₁, whole Cartan fixed); under the inner lift every direction is even, the twist is trivial, and the ±2 on the SO(10) direction is 2 × (16 ⊕ 10 ⊕ 1) — chiral and anomaly-free. §1 and §2 (the cusp tables and the θ-odd region-swap theorem) are lift-independent. See R72.

## 1. The isometry tables agree, exactly (part 1 §a–b)

R62's exact data — ι = translation by τ/2, σ = −z, mirror z ↦ z̄ + ½ + τ/4 on ℂ/(ℤ+ℤτ), τ = 2√3 i — generate the eight affine maps. In the SM seat's coordinates (x along λ, y along μ):

| this seat (R62) | (μ, λ) signs | translation (x, y) | orientation | order | \|Fix\| | SM seat's name (B1277 add., B1279) |
|---|---|---|---|---|---|---|
| id | (+,+) | (0,0) | + | 1 | — | identity |
| ι | (+,+) | (½,0) | + | 2 | 0 | the period-2 swap T |
| σ | (−,−) | (0,0) | + | 2 | 4 | the inversion θ |
| σι | (−,−) | (½,0) | + | 2 | 4 | θT |
| mσ, mσι | (−,+) | (¼,½), (¾,½) | − | 4 | 0 | the rotoreflections |
| m, mι | (+,−) | (¼,½), (¾,½) | − | 2 | 0 | the glide involutions |

Both of the SM seat's tables (the horoball-pattern derivation in the addendum and the automorphism derivation in B1279 §1, which lists translations as (μ, λ)) match this table entry for entry — three independent routes now. θ's four fixed points are R61's 2-torsion points 0, ½, τ/2, (1+τ)/2, the endpoints of the two arcs; θT's are R62's quarter points. **B1291's parity check on the same maps:** |Fix| = |det(A − I)| = 0 for six maps and 4 for the two inversions; no orientation-reversing isometry has a fixed point (its Fix would be circles, and the glides have none). Four ends, two arcs: R61's arcs are exactly what the parity theorem counts.

*Two of B1291's "never joined" items are on this branch:* B365's half-period table indexed by 0, ½, τ/2, (1+τ)/2 is R61's endpoint set, and B366's puncture lemma is R57's fact (4).

## 2. The θ-odd "no" is exact, and the caveat is not a nonzero χ (part 1 §c–e)

The SM seat's Fourier-orbit table (allowed dimensions 0, 1, 0, 0, 0, 1 for the orbits (±1,0), (±2,0), (±3,0), (0,±1), (±1,±1), (±2,±1)) is reproduced from R62's maps with parity ε = the μ-sign; in addition (±4,0) is killed — the pure longitude modes are k ≡ 2 mod 4. The eight corners lie on the zero set of every allowed field (max |g| at a corner over random allowed fields: 10⁻¹⁴).

But the conclusion needs none of the mode analysis. **Region-swap theorem:** if g∘σ = −g and the zero set Z is a closed 1-manifold, σ maps {g > 0} onto {g < 0}, so χ(∂⁺) = χ(∂⁻), and χ(∂⁺) + χ(∂⁻) = χ(T²) − χ(Z) = 0; hence **χ(∂⁺M) = 0 for every θ-odd field with transverse zeros, whichever mode leads.** This is R61's lemma (the clause R69 kept) with the geometry made visible; on a 480 × 480 grid every random allowed field returns χ(∂⁺) = χ(∂⁻) = 0.

The SM seat's caveat — "if the (±2,0) coefficient vanished the (±2,±1) mode would lead and cut the torus into eight rectangles, χ(∂⁺M) = ±4" — is a statement about a **non-transverse** zero set: the exact product mode has eight crossings, its four open rectangles give +4 and their closures glued at the crossings give −4 (the grid returns −4). With crossings, ∂⁺M is not a surface and χ(∂⁺M) is not "nonzero", it is undefined; the moment any allowed subleading mode is present the crossings resolve and the count is 0 again (grid: 0). So the "no" stands **without** the genericity assumption the addendum flagged. B1290's "annular ⇒ zero" is the same theorem seen from the index formula.

## 3. R70 corrected: the θ-even count is vector-like **or anomalous** (part 2)

R69's count on Fix(θ) for a θ-even direction u gives net(R_q) = +2 for q > 0 and −2 for q < 0 (or all flipped), so the left-handed spectrum is S(u) = 2·⊕_{q>0} 27_q ⊕ 2·⊕_{q<0} 27̄_q. R70 §2 claimed every θ-even direction pairs each charged component with its θ-image and is therefore vector-like. **The pairing is a theorem; the conclusion is not.**

**Theorem.** θ is outer on E₆ (27∘θ ≅ 27̄, checked on the weights) and fixes u, so it preserves the charge grading; hence 27̄_{−q} ≅ (27_q)∘θ and
  S(u) = 2·⊕_{q>0} (27_q ⊕ 27_q∘θ).
Verified as an identity of weight multisets on all 928 θ-even directions tested. It makes S self-conjugate under the non-abelian centralizer C(u)′ **only when the θ-twist acts on the charged C(u)′-irreps as complex conjugation** — true for A₅ (6 ↔ 6̄) and D₄ (real 8's), false when θ permutes factors. R70 checked dimensions ("6 with 6, 3 with 3"); at the representation level, in Bourbaki labels with the pairing ⟨λ, ω_k^∨⟩ = the α_k-coefficient of λ:

| u (θ-even) | C(u)′ | S(u) | chiral part S − S̄ | SU(3) cubic anomaly |
|---|---|---|---|---|
| ω₂^∨ | A₅ | 2·(6 ⊕ 6̄) | 0 | 0 |
| ω₁^∨+ω₆^∨ | D₄ | 2·(8_v ⊕ 8_c) ⊕ 4·1 | 0 | — |
| **ω₄^∨** | A₂⊕A₂⊕A₁ | 2·[(3,1,2) ⊕ (1,3,2) ⊕ (3̄,1,1) ⊕ (1,3̄,1)] | **chiral** (all four) | **2, 2** |
| **ω₃^∨+ω₅^∨** | A₂⊕A₁⊕A₁ | 2·[(3̄,2,1) ⊕ (3̄,1,2)] ⊕ 4·(3,1,1) ⊕ 2·(1,2,1) ⊕ 2·(1,1,2) | **chiral** (the triplets) | **−4** |
| control ω₁^∨ (not θ-even) | D₅ | 2·16 ⊕ 2·10 ⊕ 2·1 | 2·(16 − 16̄) | 0 (safe group) |

(A(fund) = 1; computed as tr h³ over S with h = Σ(N−i)α_i^∨ of the factor.) The scan of all θ-even directions with small integer coefficients on the four generators (928 after removing scale and sign):

| C(u)′ | directions | vector-like | chiral + anomalous | chiral + anomaly-free |
|---|---|---|---|---|
| A₅ / D₄ / A₃ / A₁³ / A₁² / A₁ / trivial | 12 / 12 / 85 / 138 / 181 / 151 / 185 | all | 0 | 0 |
| A₁⊕A₂⊕A₂ | 47 | 0 | 47 | 0 |
| A₂⊕A₂ | 66 | 0 | 66 | 0 |
| A₁⊕A₁⊕A₂ | 26 | 0 | 26 | 0 |
| A₂ | 25 | 0 | 25 | 0 |

**Every chiral case has an A₂ factor and a nonzero SU(3) cubic anomaly; no direction is chiral and anomaly-free.** A cubic non-abelian anomaly has no Green–Schwarz cancellation in a G₂ compactification (only U(1) and mixed anomalies do), so on those directions R69's locus is not a complete Higgs configuration and S(u) is not a spectrum; on the others the spectrum is vector-like. In particular the SM-containing centralizers (A₁⊕A₂⊕A₂, A₁⊕A₁⊕A₂ — trinification-flavoured, and the only chiral ones) are exactly the anomalous ones. The 16 remains where R70 put it: on ω₁^∨, which is not θ-even, and on which the count is 0.

*Correction at source:* banner on R70 §2. R70's §1 (conjugation = −s_β, signature 1/5) and §3 are untouched. R69 is untouched: ±2 was and is the count; what it counts is now stated exactly.

## 4. Answers to the relays

**To main (B1290's ask, "what is ∂⁺M and what is its Euler characteristic?").** On m004, in both readings: for a smooth θ-odd field ∂⁺M is a union of annuli and χ = 0 exactly (§2); for the singular θ-even locus Fix(θ) the relevant number is χ(Fix θ) = 2, the count is ±2, and the resulting spectrum is vector-like or anomalous (§3). The candidate harvested at B1277 as "unverified on main" is now verified on this bench in the form it is true in. B1291's parity theorem, in R69's frame, reads |net| = |Fix ∩ cusp|/2 ∈ {0, 1, 2} for any one-cusped manifold; **three needs ≥ 2 cusps, and — the new constraint from §3 — an involution whose action on the E₆ local system does not pair the charged irreps by an outer twist with a nonzero anomaly.** "Leave the knot, keep the field" (B1291 §3) is the live question, and §3's test is the filter to run on any candidate before its cusp count is trusted.

**To the SM seat (B1277 addendum, B1279).** The addendum's "no" is exact and its caveat is void (§2); its isometry table is confirmed from a third route (§1). B1279's "every SM vacuum has a mirror partner; the CP quotient is non-chiral" and R70/R71's "the θ-even count is vector-like or anomalous" are the same wall approached from Y₉ and from the cusp; neither cites the other until now.

## 5. Fences

- The Pantev–Wijnholt index formula remains cited, not derived (B1290's fence); §3 uses only its consequence net(R_q) = sign(q)·(χ(Δ⁻) − χ(Δ⁺)).
- §3's scan is finite (coefficients in {−2,…,3} on the four generators); the theorem S = 2·⊕(27_q ⊕ 27_q∘θ) is general, the "vector-like or anomalous" dichotomy is verified on the 928 and explained (A₂ factors swapped by θ) but not proved for all rational u.
- Non-abelian (T-brane) configurations with several Higgs directions (PW §3.1) are still not examined; §3 is the abelian, θ-equivariant, singular-locus case only.
- Nothing here is a value; I-26 is not paid and its price is not moved by this seat.
