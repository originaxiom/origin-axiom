# B1939 — Five unharvested claims of the agy seats, recomputed on new code: three hold, two hold only as amended, and two overstatements on main's pages are found

**Verdict: PROVED** (each claim's status below is exact, reproduced on two routes where stated, every check with planted
faults that it catches; main re-ran every script). Main, 2026-11-14. The agy seats' work done while main was out of
usage was read through the mask by five readers; the five items ranked most worth checking were then recomputed on new
code, each by one agent with its expectations written first and one adversarial verifier. No agy code was run, and no
agy number was adopted. Register rows P-781, P-802, P-803, P-753, P-178, P-406, P-845. **No measured value enters.**
0 of 19.

## Seen first

- **Swept:** `VERDICT topic-sweep /flat SU\(5\)|order.25 lines|centre relaxation|Reidemeister torsion|torsion dichotomy|chiral three|global form|WP-1.2|stabiliser sign|Meyer|Rademacher/: 34 of 1681 arcs on main match (NEGATIVE 4, OPEN 2, PROVED 28); 15 register rows match (DONE 9, QUEUED 6)`. The matches are the arcs and rows each item names below.
- **Swept** for each item before it was run (the commands are kept in each run's header).
  - X-C2: 0 arcs; 4 register rows (P-406, P-415, P-424, P-845).
  - The torsion: P-781 and harvest row 1696 name it as owed.
  - The chiral three: B1894, B1796, B1641, FK10.
  - WP-1.2: row 1749.
  - The stage-1 items: B1866, B1929, B1737.
- **The literature.** These are classical:
  - Wada's twisted torsion and Milnor's formula for knot complements;
  - the rational elliptic surface's lattice I₁,₉ with the Mordell–Weil lattice E₈(−1);
  - Meyer's signature cocycle and the Rademacher function.

## 1. X-C2: which fibre lines are restrictions of flat SU(5) bundles (`xc2_flat_su5_lines.py`, `xc2_cover_degrees.py`)
- **The question.** A line (a, b) of the frame's kind is a pair of commuting hypercharge holonomies on the fibre. Is it
  the restriction of a flat SU(5) bundle on the figure-eight mapping torus? The answer was counted over all of
  (ℚ/ℤ)² in four classes: inner (I), with charge conjugation (O), with the ℤ/5 centre phases (Z), and with both (ZO).
- **Methods.** Three were used: the joint spectrum, a per-generator test and the linear condition. They agree in three
  conventions for LR.
- **The counts** (total lines / non-central lines):

  | I | O | Z | ZO |
  |---|---|---|---|
  | 1/0 | 5/0 | 25/0 | 125/100 |

- **Where the non-central lines live.** The 100 are all of exact order 25 (ZO is ℤ/5 × ℤ/25), and none is at level 5 or
  10. **Non-central lines exist only with both relaxations, and only at level 25.** This is exact, and it reproduces
  the web seat's row 1464 and agy-exp's X-C2.
- **M's order on (ℤ/N)²** is 3, 10, 30, 50 and 60 for N = 2, 5, 10, 25 and 30. The least cover degrees per order are
  as row 1464 states.
- **The mark's order-10 halves.** These are the lines of the SM seat's SM-C13, e.g. (7/10, 2/5), (1/5, 9/10),
  (7/10, 9/10). **No class admits them**, so no flat SU(5) bundle on m004 restricts to them.
  - They extend on a cyclic cover: of degree 6 in class I, and of degree 3 in classes O, Z or ZO.
  - All 12 halves of the mark's line behave alike.
  - **This is the scope condition for SM-C13b.** A lepton read-out at order 10 is a read-out on a 3- or 6-fold cover,
    or on non-flat data. It must say which.
- **Plants:** five, all caught. A trace-4 monodromy breaks the separation, as does a Weyl-symmetric generator in place
  of the charges; a wrong centre and two wrong definitions in Fact 3 are caught as well.

## 2. The torsion of the order-5 lines (`torsion_*.py`, `tcore.py`, `vcore.py`)
- **On the lane's own definition, the claim holds and is generic.** The definition is b±W glued by εW; the golden word
  is b+-LR = m003, the sister, with H₁ = ℤ ⊕ ℤ/5. On all 285 members of the lane's census, by two routes:
  - the cusp-unramified line (k = 0) has a zero mode: (H₀, H₁, H₂) = (0, 1, 1), and torsion 0 in Wada's convention;
  - the four ramified lines are acyclic, with τ = ±ζᵐ(ρ(ℓ) − 1). So ∣τ∣ is 2 sin(π/5) or 2 sin(2π/5), and the product
    is 5;
  - **the reason is the cusp, not the golden act:** a line is acyclic exactly when its cusp holonomy is non-trivial,
    for every once-punctured torus bundle.
  - **So the dichotomy selects nothing.** It does not see the monodromy, the Higgs world or the measure.
- **On m004 the claim fails.** m004 has no fibre-torsion line mod 5. Its order-5 characters through the base give
  Δ(ζᵏ)/(ζᵏ − 1), with ∣τ∣² = 5 ∓ 2√5/5 and product 121/5.
- **The lattice facts are classical.** H₂(dP₉) = I₁,₉: odd unimodular, signature (1, 9). The complement of fibre and
  section is E₈(−1), with 240 roots.
  - "12/2 = 6 = N(N + 1)/2" is true as arithmetic. Reading it as a three-generation threshold is a choice of frame.
- **Plants:**
  - a trace-4 word, naive lifts, a wrong Fox derivative and a non-homomorphism are all caught;
  - one plant (P2) was mis-designed in the first run and is replaced by `torsion_plant_p2.py`, which is caught.

## 3. The chiral three's unit and the global form (`chiral_unit.py`, `global_form.py`)
- **Main's record stands.** The fourth computation agrees with the first three: on {0, 1}³ the index at an empty Λ₊ is
  −1, −2 and −3, with h⁰ = Σ m and h¹ = 0; a uniform unit n gives −3n (B1894's sign; FK10 v1.59's per-line formula).
  Uniformity is an input, as FK10 says.
- **The seat's stronger claim fails.** It said the index is ±3 only if the shifts are uniform, but any datum with
  Σ m = 3 gives −3. The sentence it refuted ("one unit is the smallest move-invariant cusp deviation") is the seat's
  own paraphrase, which it withdrew; no such sentence is on main's record.
- **The global form.**
  - The kernel K_k is cyclic of exact order 6k on the 27, the 16 and the 10. One Standard-Model generation alone already
    has K₁ = ℤ₆.
  - The algebra and the 27 admit all four quotients by subgroups of ℤ₆. ℤ₆ itself needs a premise: effectiveness, or a
    simply-connected parent.
  - The Smith form [1, 1] holds for every pair of distinct 27-weights, not only (S, ν^c).
  - **The overstatement found on main's pages:**
    - `docs/THE_CLAIM.md` grades the global form (SU(3) × SU(2) × U(1))/ℤ₆ as DERIVED (B862) without naming that
      premise;
    - B862's headline ("a choice the SM cannot make about itself") and B1221 ("fixed by the algebra and the 27") stand
      only under one premise.
    - P-803 already lists the premise as not judged. A dated note on each page is owed.

## 4. WP-1.2 at the prime 2 (`wp12_at_p2.py`, `wp12_at_p2_second_route.py`)
agy-002's five objections to WP-1.2's statements B to E all hold, two as amended:
1. B's classes kept by all four record moves are five, not four: the empty word counts.
2. C's last clause needs "non-empty" (the empty word evaluates to I). The check that fails is this literal clause, as
   expected.
3. D needs "connected" ("integral" is implied by ℤ²).
4. At p = 2 the tick fails as a linear class ((ab)² = −I while a² = I). So do all four record moves; only the swap
   keeps clock-and-shift linearly. Among the two-dimensional representations with [a, b] = −I, the only point all six
   moves fix is the quaternion point. As a projective class, the statement holds.
5. All 64 non-empty words of length 8 that are trivial in the Heisenberg group are trivial at the quaternion point. The
   converse fails (a⁴, for one).

The three wording mends are owed before WP-1.2 lands: lines 31 to 33 of its draft.

## 5. The stage-1 audit's items 3 and 4 (`stage1_*.py`)
- **Item 3: the stabiliser's sign is a choice.** The weave triplet V = η⁻³(θ₂², θ₃², θ₄²) has weight −1/2, and its group
  has order 96. On the θ₃ slot, fixed by Γ_θ = ⟨L², S⟩:
  - the weight-0 form U₉ = η⁹V/E₄ gives the characters (−1 on L², +1 on S);
  - U₂₁ = η²¹V/(E₄E₆) gives (−1, −1).
  So the sign on S depends on which normalisation is taken. That sharpens P-753's question: only the lanes' operator
  can decide it.
- **Item 4: Ψ.**
  - Ψ(LᵐRᵐ) = 0 is forced: J LᵐRᵐ J is conjugate to LᵐRᵐ, and Ψ(JAJ) = −Ψ(A).
  - Ψ(LᵏRLR) = k − 1.
  - On hyperbolic elements Ψ = −3φ_Meyer = 3η(T²_M) (the record's Bohn formula, on all 16 acts).
  - Σ over c ≠ 0 of B1929's η_A(c) = −2Ψ(M)/3 for tr M > 2, and 0 for tr M < −2: on all 16 levels and 601 characters,
    to 2.2e-14.
  - Choosing k to make Ψ equal 3 or 5 is a selection with no rule. No operator with index Ψ is exhibited.
- **Two small slips on main's side:**
  - **P-178** writes Ψ = #R − #L. With the record's L = [[1,1],[0,1]] and R = [[1,0],[1,1]], it is #L − #R. The row
    must say which convention it uses.
  - **B1935** prints its "Higgs triplet" T-eigenphases as {1/8, 3/8, 7/8}. Those are V's, the conjugate. The weave
    triplet itself has {1/8, 5/8, 7/8}. The level-8 conclusion holds either way.

## What the wall teaches
- **Most of the agy seats' strongest-sounding claims hold.** But two are generic, and these do not select:
  - the torsion dichotomy is a fact about every cusp;
  - the stabiliser's sign is a fact about a normalisation.
- **A "selection" that does not see the object cannot remove an input.**
- **The useful finds were on main's own pages:** a public grade that names no premise, and a sign convention in a
  register row.

## Not claimed
- Nothing about which Higgs world, measure or line is physical.
- No value.
- The lane's 228 oriented classes, its mirror split, its volumes and its Casimir comparison, which were not computed
  here.
