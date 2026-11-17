# W-A2: postulate D, derived as far as the ground goes. The record's lines of order 5 match the Weyl operators of level 5's Weil space: the Weil representation moves the operators by the record's own transport rule, up to a linear identification of 𝔽₅² (the identity in W-A1's conventions). The fibre's flux-5 zero modes carry that module, split 3 + 2 by the centre. The act fixes exactly one line at p = 5 and at no other prime below 60. The frame's generations sit on the fibre's 2-torsion, of level a power of 2, not on the Weil 3, so colour and families do not collide. No failure criterion fires; each was decided in advance by standard theory or the record. What stays counted: the flux on the fibre, gauging SU(W), the chirality, and the Higgs's place; four bits for D's one entry, so the count does not fall

**From:** the web seat (chat1). **To:** main (cc). **Kind:** `result:`, data-free. It closes card W-A2
(`relays/cards/CHAT1_W-A2_deriving_postulate_d.md`, e9f999307), opened at the author's request. Main will recompute.

**How it was checked.**
- Computed once; expectations and failure criteria committed first (the card, before any computation).
- `wa2_checks.py` was sealed before its run, and its output was committed before it was read.
- Recomputed independently by the referee (A to E, on the referee's own code).
- It computes algebra and theta series only: no frame output, no data.
- Not tested against planted errors.
- **The failure criteria were weak.** Each was decided in advance by standard theory or the record:
  - F1 by the discriminant (B1884);
  - F2 by the Weil split's dimensions (B1951's control);
  - F3 by B1935 § 3;
  - F4 by the Weil representation's defining property;
  - F5 by the standard theta functions.

  That none fires shows the computation is right, not that D passed a test.

## 1. Results

| part | result |
|---|---|
| A, the level | Below 60, the act LR = [[2, 1], [1, 1]] fixes 2 lines at p ≡ ±1 mod 5 (11, 19, 29, 31, 41, 59), none at the other primes, and **exactly one at p = 5 only** (the referee: the (5\|p) rule holds for every prime below 2000; B1884 has the unique line to level 200) |
| B, the lines as W's operators | the 25 Weyl operators X^a Z^b are HS-orthogonal, and XZ = ζ⁻¹ZX. Conjugation by W-A1's Weil representation maps each to a phase times W(M_g v), with M_g linear on all 25. **M_T = [[1, 0], [4, 1]] and M_S = [[0, 4], [1, 0]]: the record's transport, T: (a, b) ↦ (a, b − a) and S: (a, b) ↦ (−b, a) (B1724).** For W-A1's ρ in the labelling X^a Z^b the identification is the identity. It is diag(1, 4) for the conjugate ρ (k = 3), diag(1, 2) for the other Weil class (k = 1), and a swap for the labelling Z^a X^b (the referee). Some identification exists for every Weil representation, so F4 could not fire. The square class of its determinant picks the Weil class. M₋I = −1 |
| C, the fibre's flux-5 zero modes | ψ_j(u, τ) = Σ_n exp(πi·5τ(n + j/5)² + 2πi·5u(n + j/5)), j = 0..4: degree-5 quasi-periodic; u ↦ u + 1/5 acts as Z, and u ↦ u + τ/5 as X up to a factor common to all j; u ↦ −u maps ψ_j to ψ_{−j}; rank 5. **Parity split: 3 even, 2 odd.** The referee adds (computed once): T² acts as diag(ζ^(j²)) and S as the kernel ψ(−jk)/√5, the non-residue Weil class |
| D, families against colour | the frame's Higgs-direction triplet, the card's stand-in for the generation triplet, has T-eigenphases 1/8, 3/8, 7/8 (level 8, as B1935 § 3); the Weil 3 has 0, 2/5, 3/5 (level 5). The triplet's permutation parts under T and S generate S₃ = SL(2, 𝔽₂) on three points. The frame's quaternion units {1, Q_I, Q_J, Q_K} are HS-orthogonal; Q_I, Q_J and Q_K square to −1 and anticommute pairwise: **the level-2 Weyl operators, up to phases** |
| E, the rivals | see § 3 |
| **failure criteria** | **F1, F2, F3, F4 and F5: none holds** (each decided in advance; see "How it was checked") |

## 2. The derivation, step by step, and what each step rests on

**Step 1. The level.**
- **[E] GENESIS SE3** already takes the ground's level to be the prime of the act's discriminant: LR's characteristic
  polynomial x² − 3x + 1 has discriminant 5.
- **[E] (A) Re-checked.** 5 is the one prime below 60 at which the act fixes exactly one line. The record already has
  this: at level 5 exactly one line is kept, and at no other level to 200 (B1884, cited in GENESIS SE3).
- **[E] (not independently checked; standard number theory) It is so for all primes.** The act fixes two lines when
  x² − 3x + 1 splits mod p, which is when (5|p) = +1, that is p ≡ ±1 mod 5. It fixes none when the polynomial is
  irreducible. It fixes exactly one only at the ramified prime, 5.
- **[E]** So "the level is where the act names a unique line" and "the level is the act's discriminant" are one
  condition: a repeated root mod p is p dividing the discriminant. They are not two independent supports. B1943's line
  for LR, {k(1, 2)/5}, is that unique line.

**Step 2. The Weil space is the module of the record's lines.**
- **[E] (B)** The record's 24 lines of order 5 match the 24 non-trivial Weyl operators X^a Z^b of ℂ⁵, up to phase. The
  Weil representation moves the operators by the record's own transport rule, up to a linear identification of 𝔽₅²
  (the identity in W-A1's conventions). Some identification exists for any Weil representation; the square class of
  its determinant picks the Weil class (the referee).
- **[J]** So the record's level-5 combinatorics is the conjugation action on the operators of W, read up to phases.
  - The record's rule keeps the point w = ατ + b fixed (B1724's `covariance.py`): it is a passive relabelling. Whether
    the match is the representation or its inverse is therefore a convention too (the referee).
- **[E] (not independently checked; standard) Stone–von Neumann.** Up to equivalence, W is the unique irreducible
  module in which these operators commute up to the Weil pairing (ζ = e^(2πi/5) here).
  - The central character's class (k a residue or not, B1934's two Weil representations) is the one choice left
    without the flux.
  - Given the flux (step 3), it is fixed: the flux-5 zero modes realise the non-residue class, W-A1's. T² acts on them
    as diag(ζ^(j²)) and S as the kernel ψ(−jk)/√5 (the referee, computed once).
  - Both classes give the same split (W-A1's referee; E below).
- **[J] What this step needs, and where the object offers it.** The lines must act projectively: commuting up to
  ζ ≠ 1, not as frame C's commuting flat twists. Two realisations do it.
  - **Flux:** a line bundle of degree 5 on the fibre. Its magnetic translations by 5-torsion points commute up to ζ.
    This is part C, and it needs no puncture.
  - **A twisted flat bundle:** holonomies X and Z of a flat PU(5) bundle with 't Hooft twist ζ.
    - On the once-punctured fibre this is a flat U(5) bundle whose holonomy around the puncture is ζ.
    - A flat U(5) bundle on the closed torus cannot do it.
  - Frame C's flat U(1) twists are neither: abelian holonomies commute on the punctured fibre too.
  - The two realisations are related by the Fourier–Mukai transform: a line bundle of degree 5 goes to a rank-5
    bundle of degree ∓1. They are not the same object.
  - That the object carries one of them is **one counted bit**: flux or flat.

**Step 3. The lead: the fibre's zero modes, second-quantised.**
- **[E] (C)** With flux 5 on the fibre torus, the zero modes are the five theta functions ψ_j. Translations by
  5-torsion points act on them as Z and X, which is the Heisenberg module W.
- **[E] (C)** The elliptic involution u ↦ −u, the centre −I of SL(2, ℤ), splits them 3 + 2. That is ρ(−I)'s split.
- **[E] (checked outside the project) This is the known split for a magnetized T²/ℤ₂ orbifold of flux 5** (Abe,
  Kobayashi and Ohki, "Magnetized orbifold models", arXiv:0806.4748, Table 1: for odd flux M, (M + 1)/2 even and
  (M − 1)/2 odd). There the even modes are read as families. Here the centre's split is read as colour against weak.
- **[J]** Fermions in those five modes, second-quantised, give Λ*(W): 32 states, split 16 + 16 by fermion parity.
  - That is D's matter space, given one reading: the zero modes' Fock space, not their one-particle space, labels
    matter's states.
  - In the usual Kaluza–Klein reading (Abe, Kobayashi and Ohki) the five modes are five copies of one field. The
    reading goes with the flux bit.
  - Fermion parity on Λ*(W) is the chirality of Spin(10)'s spinor: Λ^even is the 16, Λ^odd the 16̄.
  - What remains is the choice of which half is matter: **one counted bit**, the chirality.
  - Alone, that bit is a convention (Λ^odd ≅ (Λ^even)*, the conjugate generation), unless it is tied to another
    handedness in the object, such as its orientation (SE2).

**Step 4. The gauge group.**
- **[E] W-A1, B1951.** The unitary determinant-one maps of W commuting with ρ(−I) form S(U(3) × U(2)) =
  (SU(3) × SU(2) × U(1))/ℤ₆. On Λ^even, that group's hypercharge gives one generation with the record's values.
- **[J]** This is orbifold-parity breaking of SU(5): the parity P′ = diag(−1, −1, −1, +1, +1) of Kawamura's
  "Triplet-doublet splitting, proton stability and extra dimension" (hep-ph/0012125). It is ρ(−I) up to an overall
  sign, which leaves the commutant unchanged. Kawamura's doublet is the even block.
  - Kawamura chooses that parity by hand; the paper leaves its origin open (the referee). Here it is the object's centre, the elliptic
    involution of every fibre, acting on the zero modes.
  - What remains is to gauge SU(W) at all: **counted**.

**Step 5. Families.**
- **[E] (D)** The frame's generation index runs over the three imaginary quaternion units (BLOCKS, B1644). Up to phases
  they are the level-2 Weyl operators.
  - **[J]** They are labelled by the three non-zero 2-torsion points of the fibre, equivalently its three even spin
    structures.
  - **The record gives the blocks no modular transformation of their own.** B1724 checks only that the outputs are
    invariant.
    - The level-8 phases 1/8, 3/8, 7/8 are the Higgs direction's (B1935 § 3), which part D tested as the card's
      stand-in.
    - There T is e^(iπ/4) times a 90° rotation of Im(ℍ).
  - **[J] The referee's algebra on the frame's coupling formula** (not computed on the frame): with the Higgs and the
    channels moving as B1724 and B1935 § 1 (as scoped) record, the coupling moves as Y ↦ e^(iπ/4) Rᵀ Y R.
    - R is a real signed permutation of the blocks.
    - The blocks' T-eigenphases are therefore 0, 1/4 and 3/4.
    - T and S generate the octahedral group S₄ (level 4), whose permutation part is S₃ = SL(2, 𝔽₂).
  - The Weil 3 is of level 5. They are different triplets.
- **[J]** The families' levels are powers of 2: 2 for the permutation part, 4 for the blocks, 8 for the Higgs
  direction. All are coprime to 5, so by the Chinese remainder theorem the modular group acts on the two structures
  independently. Colour (level 5) and families do not collide.
- **[J] Three is the count of even spin structures on a torus**, 2^(g−1)(2^g + 1) = 3 at genus g = 1, or equally of
  non-zero 2-torsion points, 2² − 1. In the frame the count follows from indexing the generations by the imaginary
  quaternion units, which is itself counted (W-A1's audit: generations, typed in).
- **[E] B1934's open item was already settled by B1935 § 3.** B1934 asks whether the icosahedral triplet is the
  frame's generation triplet ("a computation still to do"). B1935 § 3 found that it plays no role in frame C as built:
  the frame's modular triplets are its channels (level 2) and its Higgs direction (level 8). Part D agrees. Its level-8
  phases are B1935 § 3's Higgs-direction phases. The blocks are of level 2 or 4 and never of level 5.
- **[J] A hypothesis for the matter space with families:** Λ^even(W₅) ⊗ Im(ℍ). That is the level-5 Fock space times
  the level-2 triplet: the object's two primes, the act's discriminant 5 and the spin structures' 2. It is not derived
  here.

## 3. The rivals

Hypercharge is normalised as Y = (p − 1)/2 on the larger (even) block and −(p + 1)/2 on the smaller, traceless; at
p = 5 that is −6Y.

| p | the Weil split | the commutant | the group | U(1) anomalies of Λ^even (ΣY, ΣY³, SU(m)²Y, SU(n)²Y) | the act's fixed lines | SU(3) × SU(2) × U(1) |
|---|---|---|---|---|---|---|
| 3 | 2 + 1 | 2 | S(U(2) × U(1)) | 0, **6**, **−1/2**, 0 | 0 | no |
| **5** | **3 + 2** | 2 | **S(U(3) × U(2))** | 0, 0, 0, 0 | **1** | **yes** |
| 7 | 4 + 3 | 2 | S(U(4) × U(3)) | 0, 0, 0, 0 | 0 | no |
| 11 | 6 + 5 | 2 | S(U(6) × U(5)) | 0, 0, 0, 0 | 2 | no |
| 13 | 7 + 6 | 2 | S(U(7) × U(6)) | 0, 0, 0, 0 | 0 | no |

- **[E]** The same construction at the rivals gives other groups, as main found (B1951's control). At p = 3 the even
  half is also anomalous.
  - The reason (the referee; not independently checked, standard): Λ^even(ℂ^N) is a half-spinor of SO(2N). At N = 3,
    SO(6) ≅ SU(4) and the half-spinor is the anomalous 4. For N ≥ 4, SO(2N) has no cubic anomaly, so the other zeros
    are forced.
- **[E]** At no rival does the act name a unique line.
- **[J] The two criteria single out the same prime:** the one prime where the act fixes exactly one line, and the one
  prime where the centre's split gives the Standard Model's group. B1951 already makes this point (the referee).

## 4. What D becomes

**[J] D cannot be derived from the ground alone. Its one counted entry of three clauses becomes four counted bits,
each narrower than the clause it replaces: the flux (with the Fock-space reading), the chirality, gauging SU(W) and the
Higgs's place. The count does not fall. Its content follows from them:**

| D's clause (W-A1) | now |
|---|---|
| the matter space is Λ*(W) | follows from the flux-5 zero modes, second-quantised (steps 2 and 3), given **the flux bit** (a line bundle of degree 5 on the fibre, or its flat counterpart, a rank-5 bundle with holonomy ζ around the puncture, rather than frame C's flat U(1) twists) and the reading that the zero modes' Fock space labels matter's states; its order 5 is SE3's |
| matter is the even half | **the chirality bit**, counted |
| the Higgs is the odd half | **does not stand as written**: in this reading Λ*(W) is a spinor module, and its halves are the two chiralities of one fermion. The odd half is the even half's conjugate, matter's CPT partner, not a separate boson. Fock-space parity alone does not set statistics; if it did, the even half would be bosonic. The Higgs fits as a boson valued in W, its doublet in Λ¹ with 6Y = 3 (W-A1, D7). Counted |
| the gauge group is the commutant of ρ(−I) in SU(W) | follows from the object's centre (step 4), given **gauging SU(W)**, counted |
| (implicit) the central character's class | two Weil representations; both give the same split and content. Immaterial to D's content. Given the flux bit, it is fixed: the flux-5 zero modes realise the non-residue class (the referee) |
| (new) families | the level-2 structure the frame already uses (step 5); independent of colour; the count 3 is 2² − 1 once the generations are put on the fibre's level-2 structure, a choice the frame made (counted) |

**What would close the remaining bits:**
- **The flux.** Is there an object-internal reason for flux 5 on the fibre, or for a rank-5 bundle with holonomy ζ
  around the puncture? A U(1) holonomy there cannot do it: it is trivial when flat, and e^(2πi·5) = 1 under a flux of
  5. The puncture is m004's cusp. Whether its geometry (the cusp field, the cusp shape) carries the rank-5 holonomy is
  open.
- **The couplings.** Rebuild the couplings on Λ^even(W) ⊗ Im(ℍ) as Heisenberg-covariant overlaps of the zero modes
  (magnetized-torus type), and see whether frame C's quaternion contraction is their level-2 shadow. That needs its own
  card.

## 5. Typed

| statement | how checked |
|---|---|
| the act fixes exactly one line only at p = 5, below 60 | computed once; expectations committed first; recomputed independently (the referee, every prime below 2000); already on record (B1884, to level 200) |
| the same for all primes | not independently checked (standard: the splitting of x² − 3x + 1) |
| the Weil representation moves W's Weyl operators by the record's transport, up to a linear identification (the identity in W-A1's conventions) | computed once; expectations committed first (F4); recomputed independently (the referee, all four Weil representations and both orderings) |
| W is the unique module up to the central character's class | not independently checked (standard: Stone–von Neumann) |
| the flux-5 zero modes carry W, split 3 + 2 by the centre | computed once; expectations committed first (F5); recomputed independently (the referee); checked outside the project (Abe, Kobayashi and Ohki, Table 1) |
| the flux-5 zero modes realise the non-residue Weil class | computed once (the referee) |
| the frame's Higgs direction is of level 8; its quaternion units are the level-2 Weyl operators up to phase; the Weil 3 is of level 5 | computed once; expectations committed first (F3); recomputed independently (the referee) |
| the generation blocks move by real signed permutations (level 4) | a reading (the referee's algebra; not computed on the frame) |
| the rivals give other groups, and the act names no unique line there | computed once; expectations committed first (F2); recomputed independently (the referee) |
| D becomes four counted bits: the flux (with the Fock-space reading), the chirality, gauging SU(W) and the Higgs's place | a reading |
| matter with families as Λ^even(W) ⊗ Im(ℍ) | a hypothesis |

## 6. Files

`relays/chat1_2026-11-17_wa2/`: `wa2_checks.py` (sealed), `SCRIPT_SHA256.txt`, `wa2_checks_out.txt`,
`wa2_checks_err.txt` (empty).

This note was pushed before its referee read finished, following the author's word of 2026-11-15 on untracked notes;
the read's corrections are applied in this version. None changes a computed result. They change the framing:
- the identification is a convention, and the failure criteria were weak;
- the flux realisation needs no puncture;
- the Fock-space reading is a counted step;
- part D's triplet is the Higgs direction's;
- the count of counted entries does not fall.

The first version's commit message (f356ec81a) says "D reduces to the flux bit, …"; "becomes four counted bits" is the
corrected wording.

0 of 19.
