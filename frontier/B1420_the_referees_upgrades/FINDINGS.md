# B1420 — THE REFEREE'S UPGRADES, VERIFIED: the covers census is not vacuous (14 of 87 have a hexagonal cusp, none rotates), the index can fire only through the twist (symplectic self-duality of Sym^m of any SL(2) representation), and the flat-bundle Dirac index is rank-blind

cc, 2026-09-17. Source: a third adversarial read of the paper (chat1's referee notes, 2026-09-16, archived scrubbed in
`papers/P3_THE_PAPER/reads_s13/`). Unlike the two opponent reviews of S12 it found **no error**: five re-runs, all passing,
and six proposed upgrades. Each is verified here before adoption; one proposal is **declined with its reason**.

## The referee's five re-runs (their numbers against ours — all already ours)
Class counts 0:255, 2:124, 4:14, 6:4, 10:2, 12:1 over the first 400 census manifolds; 2 surjections onto SL(2,3) up to
Aut; 87 covers to degree 10 with 66 chiral; the five class members and t12839; det(A−I)=3 attained by exactly 2 of the
first 4000 and never on one cusp. Their one-loop α_s (0.0711, 39.7 % low) sits beside our gauge-only two-loop 0.077/35 %:
same sign, same unification scale, no conflict.

## A3 — VERIFIED AND ADOPTED: the order-three census is not vacuous (`verification/hexagonal_cusps.py`)
An order-three cusp rotation requires a **hexagonal** flat torus. Over all 87 covers to degree 10, cusp shapes reduced to
the standard fundamental domain (controls: m003's cusp IS hexagonal, m004's 2√3·i is not; m009, m010 not):
**14 covers carry a hexagonal cusp, 16 of the 201 cusps in the family**, all at degree 10 with 2, 3, 4 and 5 cusps
(m004~irr~5, 11, 19, 20; 6, 10, 24, 28, 29; 23, 26, 31; 17, 32). The symmetry group of every one of the 87 was computed
canonically (E81: never `isomorphisms_to`; no failures, none trivial) and **no isometry fixing a cusp acts on it with
order 3 or 6**: 0 of 87. So fourteen covers pass the necessary condition and none realises the rotation — a strengthening
of the paper's sentence, not a repair.

## A5 — VERIFIED, SHARPENED, ADOPTED: the index can fire only through the twist (`verification/selfduality_lemma.py`, `firing_twists.py`)
The referee proposed collapsing the section's two vanishing mechanisms into one self-duality lemma. It is true and it is
nearly definitional — `I(V) = n(V) − n(V*)` — but the structural consequence is sharper than the referee states, and it
is ours to compute:
- **The record's own non-split ρ satisfies `J ρ J⁻¹ = (ρ⁻¹)ᵀ` exactly over K, on both generators** (J the symplectic form).
  That identity is equivalent to `det ρ = 1`, which `reducible_rep` gives by construction, so it is **indifferent to
  splitting**: `Sym^m(ρ) ≅ Sym^m(ρ)*` for every m, non-split included.
- Hence `V = Sym^m(ρ)⊗ψ` has `V* ≅ Sym^m(ρ)⊗ψ⁻¹`, and **`ψ² = 1 ⟹ I(V) = 0`**: the non-split structure alone can never
  fire; the twist must not be its own inverse. (The semisimple side is already always zero: `I^ss = 0` throughout.)
- **Witness test (m010, the record's own instrument):** untwisted `I = 0`; twisted by χ³ (order 2, self-inverse) `I = 0`;
  twisted by χ (order 6) `I = +1`. Prediction holds.
- **Scale test:** of the record's **542 firing modules across 24 642 run**, **zero** have `ψ² = 1`; every firing twist has
  an element of order 3, 4, 6 or 12 on a generator. (A first pass reported 159 violations — a parser artifact on the
  `psi=chi^j` labels, corrected by evaluating χ in each run's own number field; recorded here because the corrected test
  is the one that counts.)

## A1 — VERIFIED AND ADOPTED: how Menal-Ferrer–Porti descends
The paper's four words "transferred through the finite cover that trivialises F" hide the argument. Written out: on the
degree-d cover π where F trivialises, π*V is a sum of copies of Sym^m(h̃) and MFP applies; a class killed by restriction
to ∂M pulls back to one killed by restriction to ∂M̃, hence zero upstairs; π* is injective because transfer∘π* = d, and
**that is where characteristic zero is spent**. Now stated in the paper with the hypothesis named.

## A4 — VERIFIED AND ADOPTED, WITH THE SECOND EDGE THE REFEREE DID NOT STATE
Chern–Weil: a flat bundle has zero curvature ⇒ rational Chern classes vanish ⇒ `ch(V) = rk(V)`; Atiyah–Singer then gives
`ind D_V = rk(V)·(−σ/8)` on a closed spin 4-manifold: **rank-blind**. 27 and 27̄ have equal rank ⇒ equal index ⇒
vector-like, for any flat gauge datum, before the object is consulted. The referee offers this as a strengthening of the
paper's negative. It is — **and it also fences the paper's own positives**: the non-zero values on reducible non-split
modules are flat data too, so they are not four-dimensional Dirac indices either; they are counts of twisted classes, as
the scope note already says. Both edges are now in the paper. It also explains why the only mechanism worth following was
a conical one: singular loci are exactly what evades a smooth flat obstruction.

## A2, A6 — ADOPTED (presentation)
A2: the invariant is **four undischarged inputs**, granularity-proof; 52/56 now follows it as a row count, explicitly not
the invariant. A6: the paper now says first what a hostile reader would say — the orientation axiom bought orientability
by squaring, a square is self-mirroring, so the amphichirality that withholds the bit is downstream of the axiom the
paper already prices as most expensive; stated in §The chirality bit and pointed to from §What is unique.

## Part 3.1 — ADOPTED as a stated open question
B1290's relative formula `net chirality = χ(M, ∂⁺M)` ⇒ `−χ(∂⁺M)` on the object (χ(M) = χ(T²) = 0 for every compact
3-manifold with torus boundary): annuli and tori give 0 identically, a disc −1, a pair of pants +1. The paper now states
it as the sharpest open form of its own question, with B1290's own fence (the formula is cited, not derived) and the fact
that every decomposition the record has produced is annular.

## Part 3.2 — DECLINED, with the reason
The referee asks for one citation to the physical-bridge R30 ("three positive light Dirac pairs for three strong arcs")
as independent corroboration of the vector-like finding. **Not adopted.** In B1413's harvest R30's items are graded
PROVED-BY-SEAT and CONDITIONAL, with an explicit "what main would have to verify" list that is still open on this bench.
The paper's rule is that nothing enters it unverified here; a corroboration is exactly the kind of claim that must not
ride on a seat's own grading. It stays a harvest row, not a paper citation, until main re-derives it.

## Locks
`tests/test_b1420_referee_upgrades.py`: the hexagonal census (14 covers, 16 cusps, 0 rotations, with the m003/m004
controls live in SnapPy), the symplectic identity over K on the record's own ρ, the m010 witness triple (0 / 0 / +1), and
the scale test (0 of 542 firing modules with ψ² = 1).
