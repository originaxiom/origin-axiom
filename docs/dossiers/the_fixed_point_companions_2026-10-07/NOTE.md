# The fixed-point companions: every word state's canonical several-ended cover, and where F-HE's three can live on them

cc (the SM-derivation seat), 2026-10-07. **Structure and proofs only. No count is read at any class.** Written for main's
GENESIS FK14 (does the genesis generate states with several ends, or are generations not ends?) and for the owner's ruling on main's
recommendation to pause the cover search. Nothing here is sealed, and no arc builds on it until FK14 is ruled.

## 1. The companion

**Proposition 1.** Let M = T₁ ×_φ S¹ be a word state: T₁ the once-punctured torus, φ hyperbolic in ±SL(2, ℤ) acting on
T² = ℝ²/ℤ² and fixing the puncture 0.
- H₁(M) = ℤ⟨t⟩ ⊕ coker(φ − I), and the peripheral subgroup maps onto ℤ⟨t⟩: the fibre's boundary is a commutator, and t can
  be taken at the puncture. So the cusp-trivial characters of M are exactly the characters of coker(φ − I).
- Let N be the cover along all of them: ψ: π₁M → coker(φ − I), ψ(t) = 0. Then N is the mapping torus of φ on T² with every
  fixed point of φ punctured:
  N ≅ (T² − Fix φ) ×_φ S¹.
- So N has |Fix φ| = |det(φ − I)| = |2 − tr φ| cusps, one for each fixed point, and its deck group is Fix φ ≅ coker(φ − I),
  acting by translations.
- N is the maximal abelian cover of M to which the cusp lifts. It is determined by M alone. Call it **M's companion**.

*Proof.*
- ψ is a homomorphism because φ acts as the identity on coker(φ − I).
- Restricted to the fibre, ker ψ is the cover T′ = ℝ²/(φ − I)ℤ² of T², punctured at the lattice points ℤ²/(φ − I)ℤ².
- Because ψ(t) = 0, N is the mapping torus of the lift of φ fixing the base point. That lift is φ acting on T′. It fixes
  every puncture, because φ ≡ I on ℤ²/(φ − I)ℤ².
- The linear map (φ − I)⁻¹ carries T′ to T², the punctures to (φ − I)⁻¹ℤ²/ℤ² = Fix φ, and commutes with φ. □

**The four states on record.**

| state | monodromy | ∣2 − tr φ∣ | the companion (`companions.py`) | H₁ | symmetries on the ends |
|---|---|---|---|---|---|
| m004 | +LR | 1 | m004 itself | ℤ | — |
| m003 | −LR | 5 | o10_150729 = S³ − L10n113, volume 5 vol(m003) | ℤ⁵ | ℤ/2 × S₅: all 120 permutations; the 60 kept by orientation-preserving isometries, A₅ |
| m136 | +LLRR | 4 | S³ − L14n62847, volume 4 vol(m136) | ℤ⁴ | order 32: 8 permutations (4 orientation-preserving) |
| m135 | −LLRR | 8 | not in SnapPy's census, volume 8 vol(m135) | ℤ⁸ | order 256: 128 permutations (64 orientation-preserving) |

- In each row, SnapPy lists every cover of degree ∣2 − tr φ∣. Exactly one has that many cusps, so it is the companion.
- m003's companion is the 5-fold cyclic cover along the golden order: m003's ℤ/5 is coker(−LR − I). It is the link
  complement S³ − L10n113. Its components link in a pentagon, and its isometries realise every permutation of its five ends.
- main's B1483 read o10_150729 (R4: five cusps at CS 1/4, no mirror-invariant spin structure).
- This seat's N₄₅ (sm:B1540) is a degree-9 cover of it. π₁(N₄₅) = π₁(d9.2) ∩ ker χ, and χ is the cusp-trivial order-5
  character of m003 (it is trivial on d9.2's cusp, and 9 is prime to 5). Both have five cusps, so N₄₅'s five ends lie one
  over each end of m003's companion.
- sm:B1538's population contains all three companions: m003's D5.5-2-1.w4, m136's D4.2-0-2.w0 and m135's D8.4-2-2.w5. Each
  is the unique cover of its degree with that many cusps. Its room census found room three only on four other covers.

## 2. Where three can live on the companions

**Proposition 2 (the ends of the companions).** By the Smith form of H₁ modulo the peripheral subgroups (`companions.py`):
- **m003's companion:**
  - the peripheral subgroups of any three cusps generate H₁, so a non-trivial character is trivial on at most two cusps;
  - on any two cusps the characters trivial there form a circle;
  - checked a second way against L10n113's linking matrix.
- **m136's companion:** the same for any three cusps. On any two, finitely many characters (orders 2 and 4).
- **m135's companion:**
  - on any three cusps the characters trivial there form a 2-torus (free rank 2, no torsion, for all 56 triples);
  - on four cusps: a circle for 32 of the 70 sets, a 2-torus for 2, one character of order 2 for 4, and none for 32.
- **On all three,** H₁ is free of rank equal to the number of cusps, so n(1) = b₁ − cusps = 0.

**Proposition 3 (no three on the companions of m003 and m136).** On the companion N of m003 or of m136, at every member ν of
finite order and every class c ≠ 0 of sm:B1515's frame, (I(W₁), I(Λ²W₁)) ≠ (−3, −3), and the same in the other order.

*Proof.*
- By sm:B1545's Lemma F′, I(W₁) = −3 needs m_A ≥ 3 − b0 + k ≥ 3 − b0.
- **b0 = 0 (ν⁴ ≠ 1).** ν is trivial on three cusps, so ν = 1 by Proposition 2, which contradicts ν⁴ ≠ 1.
- **b0 = 1 (ν⁴ = 1).** Theorem C (iii) (sm:B1535) needs b0 + n(ν⁴) = 1 + n(1) = 1 ≥ 3, which is false.
- **The other order.** W₂* = W₁(ν̄, c′), and ν̄ has the same m_A and b0. □

The same argument bounds the count on these two companions:
- at most one generation at members with ν⁴ = 1;
- at most two elsewhere (m_A ≤ 2, b0 = 0).

**Consequence for GENESIS FK14 (a reading, not a ruling).** If the genesis's several-ended states are the companions, so that a
state's ends are its monodromy's fixed points, then on the four states on record F-HE's three is:
- excluded on m004 (one end, main's T3);
- excluded on m003 (five ends) and on m136 (four ends), by Proposition 3;
- open only on m135's eight-ended companion. There the ends condition can be met, and Theorem C's room needs n(ν⁴) ≥ 3 at
  b0 = 0. sm:B1538's census, within its scope, found no room three there.

**N₄₅ is not a companion.** It is a degree-9 cover of m003's companion through d9.2, and d9.2 was chosen by room. Its room
(n(1) = 4, against 0 on the companion) comes from that degree-9 step.

## 3. An observation, not a claim

- **The fact.** m003's companion has five ends. Its isometries act on them as S₅, and the orientation-preserving ones as
  A₅ ≅ PSL(2, F₅), the icosahedral group.
- **Where A₅ appears in the literature.**
  - It is the family symmetry of the golden-ratio models of lepton mixing: L. L. Everett and A. J. Stuart,
    arXiv:0812.1057; F. Feruglio and A. Paris, arXiv:1101.0393. Both abstracts were read 2026-10-07.
  - Γ₅ ≅ A₅ is the level-5 finite modular group of the modular flavour models (this record's B660 literature gate, s1_gamma5).
  - The record's sweep of the golden-ratio solar-angle family is B659.
- **Where S₅ appears.** It is also the Weyl group of SU(5), main's SU(5)′. A three in F-HE on N₄₅ would split the five ends
  into three where the class vanishes and two where it lives (sm:B1547's Corollary 1). That is the shape of
  S₃ × S₂ ⊂ S₅.
- **The fence.** Nothing here connects any of these to the frame's count, and no arc uses them.

## Update, 2026-10-07: Proposition 1's description, checked on H₁

Main's relay of 2026-10-07 (with B1494) remarks that "as 'the mapping torus of φ with every fixed point punctured' the
companion would carry torsion |det(φ − I)| in H₁", while the built companions have H₁ free.
- **The two descriptions are one manifold.** The proof above gives the diffeomorphism: (φ − I)⁻¹ carries (T′, its |T|
  lattice punctures, φ) to (T², Fix φ, φ).
- **Where the torsion comes from.** It appears only if φ is taken to act on H₁(T² − Fix φ) as φ ⊕ 1. In fact the image of
  a fibre loop picks up puncture loops. In a basis adapted to the punctures, f_* = [[φ′, 0], [C, I]] with C ≠ 0.
- **Checked on +LLLR.** φ′ = [[1, 3], [1, 4]] and C = [[0, −2], [0, −1]].
  - f_* − 1 has Smith form (1, 1, 0, 0), so H₁ = ℤ³.
  - With C set to zero it has (1, 3, 0, 0): main's ℤ/3.
- **Checked on every generated state to twelve ends** (`prop1_homology.py` → `prop1_homology.json`, from sm:B1538's cover
  code).
  - H₁ is free on all 27 companions.
  - With the corrections dropped, the torsion coker(φ − I) appears on every one with more than one end.
- **So the description stands.** Main's remark is the computation without the corrections. The end counts and everything
  computed on the cover were never in question.

## Files

- `companions.py` → `companions.json` (SnapPy; structure only; a few minutes).
- `prop1_homology.py` → `prop1_homology.json` (sm:B1538's cover code; sympy's Smith form; seconds).
