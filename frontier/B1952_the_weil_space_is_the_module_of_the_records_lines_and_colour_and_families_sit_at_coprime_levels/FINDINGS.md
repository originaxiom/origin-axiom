# B1952 — The Weil space is the module of the record's lines and of the fibre's flux-5 zero modes; colour and families sit at coprime levels; postulate D becomes four counted bits

**Verdict: PROVED** (the computed statements; exact algebra and theta series, the web seat's W-A2 recomputed on main's
own code, with one step added on the frame itself). Main, 2026-11-17. What it means for postulate D is a reading, the
web seat's, stated as such below. No measured number is used. Register row P-863. **0 of 19.**

## Seen first

- **Swept:** `VERDICT topic-sweep /Weyl operator|Heisenberg|magnetic translation|zero modes?|flux[- ]5|Stone.von Neumann|2-torsion|even spin structures|level[- ]2 Weyl|generation blocks/: 41 of 1693 arcs on main match (NEGATIVE 5, PROVED 36); 44 register rows match (DONE 33, LEAD 1, QUEUED 10)`.
- **What the record already holds:**
  - **B1884:** the act fixes exactly one line at level 5 and at no other level to 200 (GENESIS SE3 cites it).
  - **B1724:** the record's transport of the lines of order 5, T: (a, b) ↦ (a, b − a) and S: (a, b) ↦ (−b, a).
  - **B1934, B1935 § 3:** level 5's Weil representation splits 3 + 2; the frame's modular triplets are its channels
    (level 2) and its Higgs direction (level 8), and the icosahedral triplet plays no role in frame C as built.
  - **B1644:** the generations are indexed by the three imaginary quaternion units.
  - **B1951:** the Weil centre's dictionary under postulate D, and the control at rival primes.
- **What is new** (the web seat's W-A2, harvest row 1852; recomputed here): the lines of order 5 are the Weyl
  operators of the Weil space; the fibre's flux-5 zero modes carry it; the rivals' anomalies. Main's addition is
  part F: how the generation blocks move, computed on frame C.
- **The literature:** the Weil representation's defining property and Stone–von Neumann (standard); the parity split
  (M + 1)/2 and (M − 1)/2 of the zero modes on a magnetized torus orbifold (Abe, Kobayashi and Ohki, arXiv:0806.4748);
  the breaking of SU(5) by an orbifold parity (Kawamura, hep-ph/0012125). The web seat's referee checked both papers;
  main has not.

## The results (`verification/wa2_on_main.py`)

| part | result |
|---|---|
| A, the level | below 2000 the act LR = [[2, 1], [1, 1]] fixes exactly one line of 𝔽_p² at p = 5 only; two lines exactly when p ≡ ±1 mod 5; none otherwise |
| B, the lines as operators | the 25 operators X^a Z^b on ℂ⁵ are orthogonal, and XZ = ζ⁻¹ZX. Conjugation by B1951's Weil representation moves them by a linear map of 𝔽₅²: ρ(T) sends (a, b) to (a, b − a) and ρ(S) sends it to (−b, a). **That is the record's transport of the lines** (B1724), in this labelling |
| C, the fibre's zero modes | the five theta functions of degree 5 on the fibre: u ↦ u + 1/5 acts as Z (8e-31), u ↦ u + τ/5 as X up to one common factor (1e-30), u ↦ −u sends ψ_j to ψ_(−j) (2e-30); rank 5; **parity split 3 + 2** |
| D, the frame's level-2 structure | the frame's quaternion units square to −1, anticommute and are orthogonal: the level-2 Weyl operators up to phases. The Higgs direction's triplet moves under τ ↦ τ + 1 by a constant unitary with phases **1/8, 3/8, 7/8**. The Weil representation's T-phases are **0, 2/5, 3/5** |
| E, the rivals | at p = 3 the even exterior powers are anomalous (ΣY³ = 6, SU(2)²Y = −1/2); at 5, 7, 11, 13 the four sums vanish. The act fixes 0, 1, 0, 2, 0 lines at p = 3, 5, 7, 11, 13 |
| **F, the generation blocks on the frame** (main's addition) | on frame C (down sector, reading S, six points of order 5, at 0.13 + 1.7i), the left unitary U_L with Y(τ + 1, w)Y(τ + 1, w)† = U_L·Y(τ, w′)Y(τ, w′)†·U_L† is fixed up to a phase (the system's smallest singular values are 2e-16, then 0.05). **It is a permutation of the three blocks with phases** (it exchanges two blocks and keeps the third), and its eigenphases are spaced by 1/4, 1/4 and 1/2: of order 4 up to an overall phase |

## What it means

- **Colour and families do not collide.** The web seat's W-A1 noted a conflict: the frame uses a triplet for the
  generations, and the Weil dictionary uses the Weil triplet as colour.
  - They are different triplets. The Weil triplet is of level 5. The frame's generation blocks move at level 4 (part
    F), its Higgs direction at level 8, its units at level 2.
  - Those levels are powers of 2 and coprime to 5, so the modular group acts on the two structures independently.
  - Part F computes on the frame what the web seat's referee derived by algebra. It is one generator, one sector and
    one reading.
- **The record's lines of order 5 are the Weil space's operators** (part B). Any Weil representation moves its Weyl
  operators by some linear map, so this could not have failed; what it gives is the identification, in which the
  record's transport rule is the conjugation action.
- **The fibre's flux-5 zero modes carry that module** (part C), split 3 + 2 by the elliptic involution, which is the
  centre −I. Second-quantised, five modes give Λ*(ℂ⁵): 32 states, 16 + 16 by fermion parity.
- **Two tests name the same prime** (parts A and E): the one prime where the act fixes exactly one line, and the one
  prime where the centre's split gives the Standard Model's group. They are not two independent supports for the level:
  a repeated root mod p is p dividing the discriminant, which is SE3's own condition.

## What postulate D becomes (the web seat's reading, accepted as a reading)

D cannot be derived from the ground alone. Its one counted entry of three clauses becomes four counted bits, each
narrower than the clause it replaces. **The count does not fall.**

| D's clause (B1951) | now |
|---|---|
| the matter space is Λ*(W) | follows from the flux-5 zero modes, second-quantised, given **the flux bit** (a line bundle of degree 5 on the fibre, or a rank-5 bundle with holonomy ζ around the puncture, in place of frame C's flat twists) and the reading that the modes' Fock space labels matter's states |
| matter is the even half | **the chirality bit** |
| the Higgs is the odd half | **withdrawn by its author.** The odd half is the even half's conjugate, the other chirality of the same fermion, and not a boson. The Higgs fits as a boson valued in W, its doublet with 6Y = 3. Counted |
| the gauge group is the commutant of ρ(−I) | follows from the object's centre, given **that SU(W) is gauged at all** |
| families | the frame's level-2 structure, independent of colour; three is the count of non-zero 2-torsion points of the fibre, once the generations are placed there, which the frame chose |

- **The web seat's own caution, which main shares:** its five failure criteria were weak. Each was decided in advance
  by standard theory or by the record, so that none fired shows the computation is right, not that D passed a test.
- **B1951's statement of postulate D is corrected by this:** its Higgs clause does not stand (a dated note there).

## What is open

- **The flux bit.** Is there a reason inside the object for flux 5 on the fibre, or for a rank-5 bundle whose holonomy
  around the puncture is ζ? The puncture is the manifold's cusp.
- **The couplings.** Rebuild them on Λ^even(W) ⊗ Im(ℍ) as overlaps of the zero modes, and see whether frame C's
  quaternion contraction is their level-2 shadow. This is P-861's direction, and it needs its own card.
- **The scoreboard's entry** for D in place of the joints it replaces (P-863 (a)) is not yet made.

## Added 2026-11-17 (B1955): the flux bit

The first open item above is answered in part. The knot's dihedral cover, which exists only at p = 5, supplies the
module and the parity with no flux: W is the functions on its five sheets. So the flux bit is replaced by a fact about
the knot. The reading that came with it, that the Fock space of W labels matter, is not supplied by the cover and stays
counted. The count is not changed.

## Not claimed

- That postulate D is derived, or that the count of inputs has fallen.
- That three families are derived: the count follows from a placement the frame chose.
- Part F under S, in the up sector, or in the other reading.
- Any value, and any comparison with data.
