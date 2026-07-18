# W2 DESIGN NOTE — the Γ(5) side (main seat, 2026-07-18)
# Status: DESIGN-STAGE (pre-prereg; no cell has run; no coefficient has
# been compared). Answers the repaired design question and cc2's
# unsatisfiability flag. For cross-check before PREREG_W2 seals.

## D1 — THE FLAT-LEVEL KILL (theorem-grade; the promised "no compatible
## grading" branch, delivered in growth form)

The two natural gradings on genuinely modular (flat) spaces both fail,
for different and exhaustive reasons:

- The cusp q-grading is not W-stable: the order-10 lift is elliptic and
  centralizes no parabolic, so it preserves no single cusp's q-filtration
  (the banked obstruction).
- Every W-STABLE candidate has growth too small. The total-pole-order
  filtration on weakly holomorphic weight-1/5 forms IS W-stable (W
  permutes cusps, preserves max pole order) and its graded pieces are
  finite — but Riemann–Roch makes dim gr_n eventually CONSTANT
  (≈ #cusps = 12), so every twisted-character coefficient is bounded
  by a constant. The weight grading on the full ring ⊕_k M_k(Γ(5)) is
  W-stable with dim M_k growing LINEARLY. The banked targets grow
  partition-like (coefficient 3402 by n = 40, per the sealed design
  doc). Bounded or linear graded dimensions can never carry
  partition-like coefficients.

CONSEQUENCE: the Γ(5) route at the flat level is structurally DEAD —
not because the shared invariant [W, D] = 0 (W non-central) is
unsatisfiable there, but because every satisfying instance has
Riemann–Roch-bounded growth. This is the clean kill branch, and it is
the same statement as cc2's slope-scrambling wall read through growth:
the flat objects are too small, on both routes.

## D2 — THE INVARIANT IS SATISFIABLE (canonically) ONE LEVEL UP

The shared invariant is NOT unsatisfiable in general: a finite-order
operator W on any graded space V lifts canonically to the symmetric
algebra Sym(V), commutes with the induced total grading, and is
non-central whenever it is nontrivial on V. Sym of a space with
linearly growing graded dimensions has PARTITION-LIKE graded growth —
exactly the growth class the targets demand and the only construction
level where D1's kill does not bite. cc2's unsatisfiability worry and
my flat kill together POINT at this level rather than closing the leg:
the functor, if it exists, lives on an exponentiated (Fock/Sym-type)
object, not a flat one. (This is also exactly where cc2's chiral-module
route already lives — a Verma module is Sym of raising operators — so
the two routes meet here rather than running parallel.)

## D3 — THE MOLIEN CANDIDATE (the design proposal; every step named
## before any run)

For a finite-order W on graded V lifted to Sym(V), the twisted
character is the MOLIEN SERIES: tr_{Sym V}(W q^D) =
Π_{n,j} (1 − λ_{n,j} q^n)^{−1} over the eigenvalues λ_{n,j} of W on
the graded piece V_n — an infinite PRODUCT determined entirely by the
eigenvalue distribution. Three structural matches, stated as design
motivation only:

1. The banked targets' RR factors have the famous mod-5 product form
   (exponents supported on 5n±1 for one stream, 5n±2 for the other).
   A Molien product of an order-10 (order-5 projective) operator
   selects q-powers exactly by the eigenvalue class on each graded
   piece — a mod-5 selection pattern is the GENERIC shape of such a
   product. RR is NOT an input to the construction: the inputs are the
   Fox/holonomy-derived W and Riemann–Roch geometry alone, so a match
   would bank as GENERATION under the sealed labels.
2. tr σ(A₁) = φ (the banked golden-rotation law) puts W over ℚ(√5),
   not ℚ. Its eigenvalue data therefore comes as a GALOIS-CONJUGATE
   PAIR, giving a conjugate pair of Molien series — and the banked
   target is a DOUBLET (F₁, F₂). The doublet structure is forced by
   the construction, not fitted.
3. Integrality: Galois-paired Molien series of a finite-order operator
   on a lattice-defined graded space have coefficients in the ring of
   integers (ℤ[φ], descending to ℤ on the paired combination) —
   integers by structure, not cancellation. This satisfies the sealed
   integrality requirement by design.

VACUITY GATE (sealed requirement, checked at design stage): W is
non-central on V (it mixes forms within each weight), the lift is
non-central on Sym(V), and the criterion can fail — a wrong eigenvalue
distribution produces a wrong product (e.g. mod-10 support, wrong
classes, or wrong multiplicities). Not a scalar-dressed character.

## THE PINNED CELL (for PREREG_W2; does not run until sealed)

Compute exactly, in order, each step two-outcome:
(i) the eigenvalues of the order-10 lift σ(A₁) on the graded pieces of
the chosen Γ(5) object (the weight tower through the weight-1/5
system), exactly over ℚ(√5), for enough graded pieces to reach q^40;
(ii) THE SUPPORT PRE-TEST (first falsifier, per the sealed design doc):
the Molien product's q-support classes mod 1 after the sealed η^{48/5}
bookkeeping, REQUIRED to meet {2/5, 3/5} — computed on the same side of
the η-convention as the comparison, before any coefficient comparison;
(iii) coefficient comparison against the banked W33 targets to ≥ 100
coefficients, both Galois conjugates against both doublet components.
MATCH / STRUCTURED NEAR-MISS (exact mismatch banked) / NO-GO (kill
pattern banked alongside wave 1's seven).

Open design items for cc2's cross-check: (a) the exact choice of
graded V (the weight tower vs the vector-valued weight-1/5 system's
module over the ring — the note proposes the latter as primary, the
former as control); (b) whether their route (b) skein object carries
the same Sym-level structure with the Möbius slope action becoming
tractable on the exponentiated object; (c) whether D1's growth kill
reads verbatim on their flat skein module (multicurve bases also grow
polynomially at fixed complexity — if so, the same one-level-up move
is forced on both routes, which would itself be a two-route law).
