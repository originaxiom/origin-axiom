# F10: a real escape from flat sector pairing, with its changed cusp included

September 21, 2026. Local branch `audit/fork-2026-09-20`.

## Verdict

There is an explicit global representation curve through F08's balanced
coefficient that removes BOTH invertible flat linear and antilinear maps
from the coefficient bundle to its dual. Its actual peripheral holonomy
also admits an exact noncommuting solution of the adopted parent gauge
equations on a cusp tail. These are constructive results, not just a
suggestion to break a symmetry.

The same calculation exposes the cost: every positive Hermitian metric
on this deformed flat cusp has infinite Higgs norm in the fixed hyperbolic
base metric. The explicit tail nevertheless has zero classical residual
potential. Moreover, ordinary whole-core cohomology still has equal
degree-one dimensions in the dual sectors. Neither of these statements
alone determines the physical normalizable spectrum.

Thus this checkpoint supplies a candidate background sector and a precise
test of its admissibility, NOT a chiral vacuum or a completed TOE. In
particular, the symmetry escape is not retracted merely because a
different invariant remains zero.

## 1. What was reused, and what was connected here

The representation is Ballas' known real-projective figure-eight family,
not a new family discovered in this fork. His nearby geometric theorem
gives properly convex structures with finite Busemann volume. That volume
is not the Higgs norm or the gauge action used here.
[Ballas, author manuscript, Theorem 1.1 and section 6](https://web.math.ucsb.edu/~sballas/research/documents/propconvfig8.pdf).

The repository already names these convex-projective families in
[the old SL4 paper README](../../papers/sl4_dehn_filling/README.md).
Its superseded component language is not imported. Nor is its distinct
finite-order-meridian slice identified with Ballas' unipotent-meridian
curve. No absent-from-all-branches or literature-novelty claim is made.

The application here connects the published matrices to F08 by an actual
invertible simultaneous intertwiner at the geometric point, and then
tests their changed peripheral data against the same adopted parent
equations. The E8 parent, embedding, positive kinetic metric, hyperbolic
base and deformation parameter remain supplied, not derived from the
object. A global gauge solution away from that point is not supplied by
the projective-geometry theorem.

## 2. The pairing escape is exact

Put q=2t>0 in the author's two determinant-one generator matrices; q=1
is the hyperbolic point. Recompute the longitude from its group word,
rather than copying a printed entry with an unbound symbol. The exact
characteristic polynomial and trace witness are

    char(Lambda) = (X-q)^3 (X-q^-3),
    tr(Lambda)-tr(Lambda^-1) = -(q-q^-1)^3.

For q!=1 the trace witness forbids an invertible flat linear E -> E*
map. Since these matrices are real, it also forbids an invertible flat
ANTILINEAR map. This is stronger than merely trying F08's particular J
and seeing it fail. All references to a forbidden bundle map in this
checkpoint mean an invertible bundle isomorphism; noninvertible maps
are not excluded by that trace argument.

The conclusion survives the scalar fourth-root twists considered in
F08: a knot-group character is trivial on the longitude. It also survives
restriction to finite covers, whose cusp subgroups contain conjugates
of positive longitude powers. The corresponding trace witness is
-(q^d-q^-d)^3. These are explicit pullbacks, not a claim about every
member or representation in the full arithmetic class.

Crucially, the paper's later PROJECTIVE rescaling Lambda/q cannot be
used as the same linear bundle: its determinant is q^-4 and it restores
three unit eigenvalues. Doing so would discard exactly the end data
that this calculation needs. No base-isometry-induced, nonlocal or
interacting spectral equivalence has been ruled out.

## 3. A full local equation solution, not a commuting proxy

An explicit change of basis brings the peripheral pair to

    M = exp(N),       Lambda = q^D (I + beta P),
    N = E02 + E23,    P = N^2 = E03,
    D = diag(1,-3,1,1),    beta = 6/(q-q^-1).

The sealed symbolic producer gives the exact conjugator determinant

    det(P0) = -(q+1)^2/4.

This verifies invertibility for the ENTIRE positive q!=1 domain where
the displayed projector construction is defined, not merely the three
sampled parameters. A separate read-only hand reviewer obtained the
same determinant from the nilpotent chain; this is an analytic check,
not an independent implementation or external theorem acceptance.

On the rectangular hyperbolic cusp metric

    g = z^-2 (dx^2 + L^2 dy^2 + dz^2),

with unit-period x,y and L>0, define k=log(q), H=diag(1,0,0,-1) and

    f^2 = z^2/4 - beta^2/L^2,       z > 2|beta|/L,
    Cx = -N/f,
    Cy = -k D - beta P/f^2,
    Cz = (f'/f) H.

All flatness and moment equations vanish as full matrices. Splitting C
into its antisymmetric and symmetric parts gives A and Psi in a positive
orthonormal coefficient frame. The parallel holonomies are conjugate to
the ACTUAL deformed peripheral pair above. Embedding the traceless
connection in the adopted parent preserves the equations; no additional
scalar current was inserted.

This is a smooth TAIL, not a completed core or a singularity prescription.
Choose the lower cutoff strictly above 2|beta|/L. There is no demonstrated
global harmonic metric, core matching, unbroken-gauge calculation for
the completed deformed vacuum, or global physical mode count here. The
normal-form coordinates and cutoff have a nonuniform q->1 limit; this
must not be called a small finite-norm physical fluctuation merely
because the holonomy matrices approach the geometric point.

## 4. Three different tests, kept separate

| Test | Result in the declared scope |
|---|---|
| Flatness and moment residuals on the explicit tail | Exactly zero. |
| Integral of the positive defining-four Higgs norm on the tail | Infinite for q!=1. |
| Ordinary H1 dimension difference between E and E* on a compact core with these whole torus ends | Zero; individual dimensions not computed. |
| Normalizable physical charged spectrum and interactions of a complete vacuum | Not computed by these results. |

The explicit norm density per dx dy dz is

    L/(z f^2) + 12 k^2/(L z)
      + beta^2/(2L z f^4) + 2L(f'/f)^2/z.

Its leading term is 12 k^2/(L z), while the remainder starts with
6L/z^3. The logarithmic divergence is not an unfortunate metric choice.
For any smooth positive Hermitian metric, parallel transport of a
holonomy eigenvector bounds the integral of |Psi|^2 on each unit-log-z
slab below by a positive constant when an eigenvalue has modulus !=1.
The proof uses no harmonicity or bounded-asymptotic-metric assumption.

That norm is NOT the residual-square static potential. Their difference
was already present in R28 and recovered in the report-guided sweep;
this is a new concrete noncommuting application. Boundary terms,
backreaction and fluctuation kinetic norms still require the actual
physical action. Infinite background norm alone is not a universal
physical exclusion; zero residual potential alone is not admission.

Separately, all four longitude eigenvalues differ from one, with

    det(Lambda-I) = -(q-1)^4 (q^2+q+1)/q^3.

An explicit chain contraction makes the whole torus local system acyclic.
Euler characteristic and Poincare--Lefschetz duality on the finite core
then imply dim H1(E)=dim H2(E)=dim H1(E*). This dimension equality does
not restore the forbidden flat bundle isomorphism. It is not a physical
L2 theorem or a statement about selected boundary discs. A countercontrol
with a trivial summand confirms that one off-unit eigenvalue by itself
would NOT suffice to conclude boundary acyclicity.

## 5. Next discriminator, in order

1. Determine the action's admissible fixed end data and boundary variation
   law for this tail. If finite Higgs norm is required, this entire
   q!=1 family fails that requirement; if not, use the actual alternative
   conditions without silently importing the finite-norm theorem.
2. Establish the cusp fluctuation complex and whether its physical L2
   cohomology agrees with the ordinary core cohomology computed above.
   Such an identification, if earned, could transfer the equal-dimension
   constraint; it must not be presumed from acyclicity alone.
3. For an admissible and promising spectrum, solve the global compact-core
   matching problem with the same holonomy and action, then check surviving
   gauge symmetry, all parent interaction channels and quantum anomalies.

These are successive tests, not claims that a complete chiral theory is
already hidden in the displayed matrices. There is still no derived
four-dimensional gravity, selected physical deformation, measured
coupling prediction or complete TOE at this checkpoint.

**Follow-through F11:** the [full cusp L2 calculation](../projective_cusp_spectrum_2026_09_21/FINDINGS.md)
has now established the proposed cohomology comparison for smooth complete
realizations with these exact or uniformly equivalent end norms. An explicit
bounded contraction includes the radial direction and implies compact
resolvent. Dual zero-mode multiplicities agree, but need not vanish: a
full-parameter Fox calculation found discrete nongeometric exceptions at
the nontrivial central twists, contrary to its initial expectation. At
q=17 +/- 12 sqrt(2) for chi=-1 and q=7 +/- 4 sqrt(3) for chi=+/-i,
there is one normalizable coefficient one-form in each dual sector.
Global harmonic-metric existence in this class remains a distinct duty;
these are not yet physical chiral vacua. F10's frozen science is unchanged.

## Verification and custody

Science was hashed and committed before execution at **ee0d62ea**.
**20 new exact checks passed on their first run; 176 unchanged antecedent
and parent-vertex checks passed**, with one optional-GUI warning. The
scientific and transitive producer hashes remain unchanged. No new
failure was erased or repaired, and older failed test versions remain
preserved. This is not full-repository or governance-suite certification.

[Design](DESIGN.md), [authored proof](PROOF.md), [producer](verify.py),
[tests](test_verify.py), [execution and reading receipt](RECHECKS.md).
No shared B allocation, other-seat modification, all-head freshness
claim, push, publication or independent main banking is included.
