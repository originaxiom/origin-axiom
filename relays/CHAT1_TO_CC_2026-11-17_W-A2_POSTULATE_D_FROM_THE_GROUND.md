# W-A2: postulate D, derived as far as the ground goes. The record's lines of order 5 are exactly the Weyl operators of level 5's Weil space: the Weil representation moves them by the record's own transport rule, with no relabelling. The fibre's flux-5 zero modes carry that module, split 3 + 2 by the centre. The act fixes exactly one line at p = 5 and at no other prime below 60. The frame's generation triplet is a level-2 object, not the Weil 3, so colour and families do not collide. No failure criterion fires. What stays counted: the flux at the puncture, gauging SU(W), the chirality, and the Higgs's place

**From:** the web seat (chat1). **To:** main (cc). **Kind:** `result:`, data-free. It closes card W-A2
(`relays/cards/CHAT1_W-A2_deriving_postulate_d.md`, e9f999307), opened at the author's request. Main will recompute.

**How it was checked.** Computed once; expectations and failure criteria committed first (the card, before any
computation).
- `wa2_checks.py` was sealed before its run, and its output was committed before it was read.
- It computes algebra and theta series only: no frame output, no data.

## 1. Results

| part | result |
|---|---|
| A, the level | Below 60, the act LR = [[2, 1], [1, 1]] fixes 2 lines at p ≡ ±1 mod 5 (11, 19, 29, 31, 41, 59), none at the other primes, and **exactly one at p = 5 only** |
| B, the lines as W's operators | the 25 Weyl operators X^a Z^b are HS-orthogonal, and XZ = ζ⁻¹ZX. Conjugation by W-A1's Weil representation maps each to a phase times W(M_g v), with M_g linear on all 25. **M_T = [[1, 0], [4, 1]] and M_S = [[0, 4], [1, 0]]: exactly the record's transport, T: (a, b) ↦ (a, b − a) and S: (a, b) ↦ (−b, a) (B1724), with the identity as the identification.** M₋I = −1 |
| C, the fibre's flux-5 zero modes | ψ_j(u, τ) = Σ_n exp(πi·5τ(n + j/5)² + 2πi·5u(n + j/5)), j = 0..4: degree-5 quasi-periodic; u ↦ u + 1/5 acts as Z, and u ↦ u + τ/5 as X up to a factor common to all j; u ↦ −u maps ψ_j to ψ_{−j}; rank 5. **Parity split: 3 even, 2 odd** |
| D, families against colour | the frame's generation triplet has T-eigenphases 1/8, 3/8, 7/8 (level 8, as B1935 § 3); the Weil 3 has 0, 2/5, 3/5 (level 5). The triplet's permutation parts under T and S generate S₃ = SL(2, 𝔽₂) on three points. The frame's quaternion units {1, Q_I, Q_J, Q_K} are HS-orthogonal, square to −1 and anticommute pairwise: **the level-2 Weyl operators, up to phases** |
| E, the rivals | see § 3 |
| **failure criteria** | **F1, F2, F3, F4 and F5: none holds** |

## 2. The derivation, step by step, and what each step rests on

**Step 1. The level.**
- **[E] GENESIS SE3** already takes the ground's level to be the prime of the act's discriminant: LR's characteristic
  polynomial x² − 3x + 1 has discriminant 5.
- **[E] (A) A second characterisation.** 5 is the one prime below 60 at which the act fixes exactly one line.
- **[E] (standard number theory) It is so for all primes.** The act fixes two lines when x² − 3x + 1 splits mod p,
  which is when (5|p) = +1, that is p ≡ ±1 mod 5. It fixes none when the polynomial is irreducible. It fixes exactly one
  only at the ramified prime, 5.
- **[J]** So "the level is where the act names a unique line" and "the level is the act's discriminant" agree. B1943's
  line is that unique line.

**Step 2. The Weil space is the module of the record's lines.**
- **[E] (B)** The record's 24 lines of order 5 are the 24 non-trivial Weyl operators X^a Z^b of ℂ⁵. The Weil
  representation moves them by exactly the record's own transport rule, with the identity as the identification. So the
  record's level-5 combinatorics is the conjugation action on the operators of W.
- **[E] (standard) Stone–von Neumann.** Up to equivalence, W is the unique irreducible module in which these operators
  commute up to the Weil pairing (ζ = e^(2πi/5) here). The central character's class (k a residue or not, B1934's two
  Weil representations) is the one choice left. Both classes give the same split (W-A1's referee; E below).
- **[J] What this step needs, and where the object offers it.** The lines must act projectively: commuting up to ζ ≠ 1,
  not as frame C's commuting flat twists.
  - On a closed torus that is impossible for flat connections, because the commutator of the two cycles is trivial.
  - On the once-punctured fibre, the commutator is the loop around the puncture, which may carry a central holonomy ζ.
  - So the projective option exists because the fibre is punctured. It is equivalent to a flux of 5 through the fibre.
    That the object carries it is **one counted bit**: flux or flat.

**Step 3. The lead: the fibre's zero modes, second-quantised.**
- **[E] (C)** With flux 5 on the fibre torus, the zero modes are the five theta functions ψ_j. Translations by 5-torsion
  points act on them as Z and X, which is the Heisenberg module W.
- **[E] (C)** The elliptic involution u ↦ −u, the centre −I of SL(2, ℤ), splits them 3 + 2. That is ρ(−I)'s split.
- **[E] (outside) This is the known split for a magnetized T²/ℤ₂ orbifold of flux 5** (Abe, Kobayashi and Ohki,
  "Magnetized orbifold models", arXiv:0806.4748). There the even modes are usually read as families. Here the
  centre's split is read as colour against weak.
- **[J]** Fermions in those five modes, second-quantised, give Λ*(W): 32 states, split 16 + 16 by fermion parity. That
  is D's matter space, without typing it in. What remains is the choice of which parity is matter: **one counted bit**,
  the chirality.

**Step 4. The gauge group.**
- **[E] W-A1, B1951.** The unitary determinant-one maps of W commuting with ρ(−I) form S(U(3) × U(2)) =
  (SU(3) × SU(2) × U(1))/ℤ₆. On Λ^even, that group's hypercharge gives one generation with the record's values.
- **[J]** This is orbifold-parity breaking of SU(5): the parity diag(+, +, +, −, −) of Kawamura's "Triplet-doublet
  splitting, proton stability and extra dimension" (hep-ph/0012125).
  - Kawamura chooses that parity by hand. Here it is the object's centre, the elliptic involution of every fibre, acting
    on the zero modes.
  - What remains is to gauge SU(W) at all: **counted**.

**Step 5. Families.**
- **[E] (D)** The frame's generation index runs over the three imaginary quaternion units. These are the level-2 Weyl
  operators: the three non-zero 2-torsion points of the fibre, equivalently its three even spin structures.
  - The modular group permutes them as S₃ = SL(2, 𝔽₂), with phases of level 8 (B1935 § 3).
  - The Weil 3 is of level 5. They are different triplets.
- **[J]** Levels 8 and 5 are coprime, so by the Chinese remainder theorem the two structures are independent. Colour
  (level 5) and families (level 2) both stand.
- **[J] Three is the count of even spin structures on a torus**, 2^(g−1)(2^g + 1) = 3 at genus g = 1, or equally of non-zero 2-torsion
  points, 2² − 1. In the frame that count is not chosen.
- **[E] (D) This answers B1934's open item.** B1934 asks whether the icosahedral triplet is the frame's generation
  triplet ("a computation still to do"). It is not: the generation triplet is of level 8, as B1935 § 3 also found.
- **[J] A hypothesis for the matter space with families:** Λ^even(W₅) ⊗ Im(ℍ). That is the level-5 Fock space times the
  level-2 triplet: the object's two primes, the act's discriminant 5 and the spin structures' 2. It is not derived here.

## 3. The rivals

| p | the Weil split | the commutant | the group | U(1) anomalies of Λ^even (ΣY, ΣY³, SU(m)²Y, SU(n)²Y) | the act's fixed lines | SU(3) × SU(2) × U(1) |
|---|---|---|---|---|---|---|
| 3 | 2 + 1 | 2 | S(U(2) × U(1)) | 0, **6**, **−1/2**, 0 | 0 | no |
| **5** | **3 + 2** | 2 | **S(U(3) × U(2))** | 0, 0, 0, 0 | **1** | **yes** |
| 7 | 4 + 3 | 2 | S(U(4) × U(3)) | 0, 0, 0, 0 | 0 | no |
| 11 | 6 + 5 | 2 | S(U(6) × U(5)) | 0, 0, 0, 0 | 2 | no |
| 13 | 7 + 6 | 2 | S(U(7) × U(6)) | 0, 0, 0, 0 | 0 | no |

- **[E]** The same construction at the rivals gives other groups, as main found (B1951's control). At p = 3 the even
  half is also anomalous.
- **[E]** At no rival does the act name a unique line.
- **[J] The two criteria single out the same prime:** the one prime where the act fixes exactly one line, and the one
  prime where the centre's split gives the Standard Model's group.

## 4. What D becomes

**[J] D cannot be derived from the ground alone. It reduces to a short counted list, and its content follows:**

| D's clause (W-A1) | now |
|---|---|
| the matter space is Λ*(W) | follows from the flux-5 zero modes, second-quantised (steps 2 and 3), given **the flux bit** (a central holonomy of order 5 at the puncture, rather than frame C's flat twists); its order 5 is SE3's |
| matter is the even half | **the chirality bit**, counted |
| the Higgs is the odd half | **does not stand as written**: the odd half of a fermionic Fock space is fermionic. The Higgs fits as a boson valued in W, its doublet in Λ¹ with 6Y = 3 (W-A1, D7). Counted |
| the gauge group is the commutant of ρ(−I) in SU(W) | follows from the object's centre (step 4), given **gauging SU(W)**, counted |
| (implicit) the central character's class | two Weil representations; both give the same split and content. Immaterial to D's content; the hand (B1934) may fix it |
| (new) families | the level-2 structure the frame already uses (step 5); independent of colour; the count 3 is forced by the fibre |

**What would close the remaining bits:**
- **The flux.** Is there an object-internal reason for a central holonomy of order 5 at the puncture? The puncture is
  m004's cusp; whether its geometry (the cusp field, the cusp shape) carries that holonomy is open.
- **The couplings.** Rebuild the couplings on Λ^even(W) ⊗ Im(ℍ) as Heisenberg-covariant overlaps of the zero modes
  (magnetized-torus type), and see whether frame C's quaternion contraction is their level-2 shadow. That needs its own
  card.

## 5. Typed

| statement | how checked |
|---|---|
| the act fixes exactly one line only at p = 5, below 60 | computed once; expectations committed first |
| the same for all primes | [E] standard (the splitting of x² − 3x + 1) |
| the record's lines are W's Weyl operators, moved by the record's own transport | computed once; expectations committed first (F4) |
| W is the unique module up to the central character's class | [E] standard (Stone–von Neumann) |
| the flux-5 zero modes carry W, split 3 + 2 by the centre | computed once; expectations committed first (F5) |
| the frame's generation triplet is of level 8 and is the level-2 Weyl structure; the Weil 3 is of level 5 | computed once; expectations committed first (F3) |
| the rivals give other groups, and the act names no unique line there | computed once; expectations committed first (F2) |
| D reduces to the flux bit, the chirality, gauging SU(W) and the Higgs's place | a reading |
| matter with families as Λ^even(W) ⊗ Im(ℍ) | a hypothesis |

## 6. Files

`relays/chat1_2026-11-17_wa2/`: `wa2_checks.py` (sealed), `SCRIPT_SHA256.txt`, `wa2_checks_out.txt`,
`wa2_checks_err.txt` (empty).

This note was pushed before its referee read finished, following the author's word of 2026-11-15 on untracked notes.
The read's corrections follow in a later commit.

0 of 19.
