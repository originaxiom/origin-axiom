# B1277 — THE VACUUM MANIFOLD OF THE OBJECT'S OWN CLOSING, AND ITS WILSON LINES: the tree-level flat directions of the E₈ theory on Y₃ never reach the Standard Model (E₆ → SO(10) → SU(5) → SU(4)), the closing's own sign characters composed with the SU(2)_L centre are the flat connections that complete SU(5) → SM, and every vacuum with three generations of Q, u^c, e^c keeps SU(5) unbroken

**Date:** 2026-09-06 · **Seat:** cc · **Status:** PROVED (every step exact: the F-flat rule, the paired D-flatness, the stabilizers, the sixteen characters by Fox calculus over ℚ(i), the lattice scan) + NEGATIVE (the closing has no vacuum with the Standard-Model group and three complete generations, with or without Wilson lines) · **Price: unchanged**

## Why this arc

`docs/THE_DESTINATION_LEDGER_2026-09-06.md` §5 named the second item of work: **the tree-level vacuum manifold of
the E₈ theory on Y₃** — D2's space, the space on which the instanton superpotential must act (L205). The same
ledger's D2 row assumed the point on it is chosen by non-perturbative physics; before that can be said, the space
itself must be computed and the question asked whether the Standard Model is a point of it at all. B1273 gave the
theory (e₆ ⊕ u(1)², three 27s carried by the three sign characters χ₁, χ₂, χ₃ of H₁(Y₃) = ℤ₄², three 27̄s, six
flavons, no adjoint chiral), B1276 the one-coupling superpotential, B1252/B1253 the labels. Everything below is
computed from those, `verification/vacuum_manifold.py`, `SELFTEST: PASS`.

## 1. The neutral fields and the monomials ((a), exact)

The colour-singlet, electrically neutral components of the 27 under the derived descent (SU(3)_c weights zero,
T₃ + Y = 0): **N** (the SO(10) singlet), **ν^c**, **h_u⁰** (T₃ = −½, Y = ½), **h_d⁰** and **ν** (T₃ = ½, Y = −½) —
five per 27. With their 27̄ conjugates and the six flavons S_ij: 36 fields. The cubic W restricted to them has
**56 monomials**: 12 of type 27³ (the two neutral zero-sum triples of one 27, **N h_d⁰ h_u⁰** — the μ-term — and
**h_u⁰ ν ν^c** — the Dirac neutrino term — each spread over the six generation orderings, one field per
generation: B1273's |ε_ijk|), 12 of type 27̄³, 30 of type S_ij 27_j·27̄_i, 2 of type S S S.

## 2. The tree-level vacuum manifold ((b), (c), exact)

**Rules.** For a cubic with squarefree monomials the coordinate subspace "the fields of A on, all others zero" is
F-flat at its generic point iff no monomial contains two fields of A (distinct squarefree monomials are linearly
independent). A 27_g switched on together with its own conjugate, 27̄_g = conj(27_g), is D-flat for **every**
vector in the 27 — the holomorphic invariant 27_g·27̄_g has gradient conj(27_g) (Buccella–Derendinger–Ferrara–
Savoy; Luty–Taylor) — and the same for (S_ij, S_ji); so the 18 pair-directions are exactly D-flat and the maximal
F-flat paired branches are the maximal independent sets of the co-occurrence graph on them. The field-level scan
(951 maximal F-flat sets, each tested by a Cartan-charge linear programme with all magnitudes positive) finds
**no unpaired candidate at all**: the paired branches are the whole tree-level manifold at the coordinate level.

**The nine maximal branches.**

| branch | pairs on | unbroken e₆-part | unbroken rank (of 8) |
|---|---|---|---|
| one generation's whole neutral set + the flavon pair of the other two: {N_g, ν^c_g, h_u⁰_g, h_d⁰_g, ν_g} ∪ {S_jk, S_kj} (×3) | 6 | **su(4)** (dim 15) | 3 |
| {N_g, h_d⁰_g} ∪ {ν^c_h, ν_h}, g ≠ h (×6) | 4 | **su(4)** (dim 15) | 4 (one u(1) mixed with the family torus) |

Sub-branches of one generation: ⟨N⟩ alone → **so(10) ⊕ u(1)** (rank 7 of 8); ⟨N⟩, ⟨ν^c⟩ → **su(5)** (rank 6);
all five → su(4). Three facts follow, none of them the seat's expectation before the run:

1. **Every maximal branch mixes the rank-reducing VEVs (N, ν^c) with the electroweak ones (h_u⁰, h_d⁰, ν)** —
   9 of 9. The cubic couples one field from each of three *distinct* generations (|ε_ijk|), so within one
   generation nothing is coupled: a whole generation's neutral set is flat. The tree-level manifold does not
   separate the GUT scale from the electroweak scale; the hierarchy ⟨N⟩ ≫ ⟨h⟩ is not a tree-level statement of
   the closing (the seat expected F_{H_u} = λ S H_d to forbid it; it forbids only ⟨S_i⟩⟨H_d,j⟩ with i ≠ j).
2. **The rank-reducing VEVs live in exactly one generation** on every branch (F_{S_ij} = 27_j·27̄_i pairs the
   generations): a second generation's N or ν^c is never flat alongside the first.
3. **The Standard Model is not a point of the tree-level manifold.** The neutral VEVs run E₆ → SO(10) → SU(5) →
   **SU(4)**: after ⟨N⟩, ⟨ν^c⟩ the surviving SU(5) is broken by the doublet VEVs in its 5 to SU(4) ⊃ SU(3)_c ×
   U(1)_em, never through SU(3) × SU(2) × U(1)_Y. The step SU(5) → SM is not a VEV of the 27 with the derived Y
   (B1269's double-centralizer law from the other side: it needs an adjoint direction, and the closing has none,
   b₁ = 0).

## 3. The Wilson lines of the closing ((d), exact)

The closing supplies flat connections through π₁(Y₃) = F(2,6), H₁ = ℤ₄²: the three sign characters already carry
the three generations (B1273). What can they do on the E₆ side?

- **z_L = (−1)^{2T₃}**, the centre of SU(2)_L, equals **(−1)^{6Y}** on every component of the 27 (15 even, 12
  odd); it is an involution of E₆ of type **A₁A₅** (centralizer dim 38 = SU(2) × SU(6)), and its joint stabilizer
  with ⟨N⟩, ⟨ν^c⟩ is **exactly the Standard Model**: Cartan 4 + the 8 roots of colour A₂ and weak A₁. So the flat
  connection **W = z_L ∘ χ_j** (one of the three sign characters composed with the SU(2)_L centre; the ℤ/3 deck
  group permutes the three, so the choice is unique up to the closing's own symmetry) together with the (N, ν^c)
  VEVs of any generation leaves su(3) ⊕ su(2) ⊕ u(1)_Y (⊕ two u(1)s mixed with the family torus) unbroken. **This
  is the first vacuum of the programme with the Standard-Model group** — and its price is read off next.
- **The SM's commutant in e₆** — B1269's c(s), dim 5 — is identified: the three Cartan directions orthogonal to
  colour and T₃, plus the two roots ±β orthogonal to the whole SM Cartan: **su(2)_β ⊕ u(1)²**, su(2)_β the SU(2)
  of the maximal subgroup SU(6) × SU(2), whose doublets in the 27 are **(d^c, D̄) ×3, (L, H_d) ×2, (ν^c, S) ×1**
  and whose singlets are **Q, u^c, e^c (the 10 of SU(5)), D, H_u**.
- **The sixteen characters of H₁(Y₃)** (Fox calculus on B1273's presentation, exact over ℚ(i)): h¹ = 1 for the
  three sign characters, h¹ = 0 for the trivial one and for all twelve of order 4 (they are non-trivial on the
  translation lattice of the flat manifold). Hence χ_i ψ has h¹ = 1 for all three i **iff ψ = 1**.
- **The 64 torus elements of order dividing 4 that commute with the SM**: the ones acting trivially on the 10
  are exactly the four exp(2πi k β^∨/4) of su(2)_β's torus. Every root of SU(5) connects two weights of the 10,
  so an element trivial on the 10 commutes with SU(5).
- **The spectra.** W = z_L ∘ χ_j: generation j loses its SU(2)_L doublets (Q, L, H_u, H_d: 12 states), the other
  two keep all 27, 40 E₆-adjoint chirals appear from the z_L-odd roots (the (2,20) of SU(2) × SU(6), vector-
  like), the flavons are unchanged — **two generations of Q and L, three of u^c, d^c, e^c**. W = (−1_β) ∘ χ_j:
  generation j loses its su(2)_β doublets (d^c, D̄, L, H_d, ν^c, S), Q, u^c, e^c keep three generations, but the
  joint stabilizer with ⟨N⟩, ⟨ν^c⟩ is **SU(5)**, not the SM.

**Theorem (the closing has no Standard-Model vacuum with three generations).** Let a vacuum of the E₈ theory on
Y₃ consist of tree-level VEVs of the neutral fields and a flat E₆ connection W, with unbroken group containing
the derived SM and with three generations of Q, u^c and e^c among its zero modes. Then the unbroken group
contains SU(5). *Proof.* SM ⊆ unbroken forces the VEVs into the SM singlets N, ν^c (stabilizer SU(5)) and the
image of W into the commutant C(SM) = SU(2)_β · A, A abelian. Q, u^c, e^c are su(2)_β-singlets, so W acts on
them through the abelian quotient, i.e. by characters ψ_c of H₁ = ℤ₄², and their multiplicities are
h¹(Y₃; χ_i ⊗ ψ_c) ∈ {0, 1}. Three generations means all three are 1, which happens iff ψ_c = 1. So W is trivial
on the 10 of SU(5), whose weights every SU(5) root connects; hence W commutes with SU(5), and the unbroken group
is SU(5) ∩ centralizer(W) ⊇ SU(5). ∎ The theorem covers non-abelian Wilson lines (images in SU(2)_β) as well as
abelian ones; it uses only h¹ of the sixteen characters, the su(2)_β decomposition and the lattice scan, all
computed. It is B952/B955's rank obstruction and B1269's double-centralizer law joined to the closing's own
characters: **on Y₃ the Standard-Model group and three complete generations exclude each other.**

## 4. L204 — the object's own abelian local systems ((e), exact)

Pantev–Wijnholt count net chirality by χ(M, ∂⁺M). On the cusped object every candidate ∂⁺ ⊆ T² (empty, an
annulus, the torus) has χ = 0, so χ(M, ∂⁺M) = 0 whatever the sign structure of the Higgs field on the cusp —
B1268's bound seen once more. The refinement is the Novikov complex of the b₁ class: for the abelian local system
a, b ↦ t the Fox row of the relator is (−(t² − 3t + 1)/t, (t² − 3t + 1)/t), so **H¹(m004; ℂ_t) ≠ 0 (t ≠ 1) exactly
at the Alexander roots t = φ^{±2}** — real, off the unit circle. **No unitary abelian holonomy on the cusp carries
a class**: the object's zero modes sit at the golden values only, where the connection is not unitary. N = 0 for
every unitary Wilson line on the cusp, by computation.

## 5. Ledger — what this changes in the destination

- **D2's space is explicit**: nine branches, all mixing the rank-reducing and the electroweak VEVs, the rank-
  reducing ones in one generation. The "point on it" is not only non-perturbative, it must also separate scales
  that the tree level does not.
- **The SM point exists, but off the tree-level manifold**: W = z_L ∘ χ_j plus ⟨N_g⟩, ⟨ν^c_g⟩ — the closing's own
  sign character doing SU(5) → SM — at the cost of one generation's doublets. **Two generations of Q and L is
  the closing's Standard Model.**
- **The Wilson-line route on Y₃ is closed by theorem**: three generations of Q, u^c, e^c ⟹ SU(5) unbroken. This
  is a property of the closed closing (whose zero modes are the three sign characters and nothing else, and
  which is vector-like anyway, B1260); the chiral closing named in the destination ledger is still the object to
  construct. The theorem tells that closing what it must not be: a manifold whose SM-preserving Wilson lines act
  on the 10 only through characters with h¹ ∈ {0, 1} per generation.
- L204: closed as N = 0 for every unitary abelian holonomy on the cusp; the golden zero modes are the Novikov
  statement of the Alexander polynomial.
- Chirality: N = 0 (closed); values: 0 of 19; price unchanged.

## Controls (MB12)

- The F-flat rule is exact for coordinate subspaces; the D-flat pairing is exact (holomorphic invariants); the
  scan for unpaired branches is a necessary-condition LP and finds none — so nothing is asserted about non-
  coordinate flat directions except that the coordinate ones are all paired.
- The stabilizer rule (⟨w, α⟩ ≠ 0 kills E_α for a paired VEV) was cross-checked on ⟨N⟩ → so(10), ⟨N⟩ + ⟨ν^c⟩ →
  su(5), i.e. against the descent it must reproduce; an earlier draft counted only w + α (not w − α) and reported
  a rank-3 algebra with 28 roots — impossible for rank 3, which is how the error was caught.
- The seat's stated expectations before the run (no branch mixing scales; the SM's commutant abelian) were both
  wrong and both corrected by the computation; the theorem was restated to cover the su(2)_β it found (B1269's
  dim c(s) = 5 was the corpus's warning, read only after the assertion failed).
- The characters' h¹ are computed for all sixteen (three 1s), not read off; the lattice scan is over all 4⁶
  torus elements; every SU(5) root is checked to connect two weights of the 10.
- The T₃ sign is a convention (the Weyl conjugate gives the same manifold); the choice of sign character is a
  deck-group orbit.

## Verification

`verification/vacuum_manifold.py` (exact; ~3 min; `SELFTEST: PASS`), run record `verification/vacuum_manifold_run.txt`.
Lock: `tests/test_b1277_the_vacuum_manifold_of_the_closing.py` (the Wilson-line and local-system parts fast, the
full manifold slow-marked).
Feeds on: B1273 (the theory on Y₃, its presentation, the three characters), B1276/B1275 (the operators), B1252/B1253
(the labels and Y), B1269 (c(s) dim 5, the double-centralizer law), B1271 §3 (rank 6 → 4 by the two singlets),
B952/B955 (the rank obstruction; abelian holonomy on the knot complement), B1079 (the Wilson menu), B1260/B1268
(N = 0 on closed manifolds, the cusp bound). Literature: Buccella–Derendinger–Ferrara–Savoy, *Phys. Lett. B* 115
(1982) 375 and Luty–Taylor, *Phys. Rev. D* 53 (1996) 3399 (D-flatness by holomorphic invariants); Pantev–Wijnholt,
arXiv:0905.1968 (χ(M, ∂⁺M)); the Hantzsche–Wendt manifold's characters (nontrivial on the translations ⇒ acyclic).
Registers no identification change.
