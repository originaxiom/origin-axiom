# R20: a source-symmetric pair-free orbit, with the global parent kept explicit

2026-09-08. Path-local research, not a main B arc or a completed physical theory.
Original seal **72e40d9c**; post-failure exact-word control seal **eb9319f3**.
[Design](HOLONOMY_EQUIVARIANCE_DESIGN.md), [prior lookup](HOLONOMY_EQUIVARIANCE_PRIOR.md),
[control design](HOLONOMY_EQUIVARIANCE_WORD_CONTROL_DESIGN.md).

**Result.** In R15--R19's prescribed three-source m202 maximal complex,
the source C3 symmetry permits exactly three rank-one adjoint characters.
Two give the complete three/zero charged kernel and form ONE isometry
orbit; the trivial character retains four/one. Compatibility is now
computed, not assumed from the existence of a Wilson line.

The global form matters. The two pair-free characters are C3-compatible
in **E6/Z3**. None of their nine scalar lifts to simply connected **E6**
is C3-compatible while preserving the same signed Higgs field. This is
a constraint on the scalar transport ansatz, not a no-go for noncentral
connections, symmetry breaking or a completed theory.

## 1. The verified geometry and the failure we did not hide

The original instrument correctly refused an unearned basis transfer.
m202's original triangulation has four tetrahedra; its canonical one
has nine, so their list of direct combinatorial isomorphisms is empty.
The native run stopped there, and six geometry-dependent tests failed.
This is an instrument failure, not evidence against the source route.

The replacement uses the explicit maps already recorded by physics
R72b at 659487bb, in the actual presentation

    pi1(Q) = <a,b | aabbAbAABBaB>,
    r:(a,b)->(b,bA),       r^-1:(a,b)->(Ba,a),
    s:(a,b)->(a,aB),       s^-1:(a,b)->(a,Ba).

Uppercase denotes inverse. Both free-group inverse identities are
checked in both directions, and the substituted relator is freely
conjugate to R or R^-1, including for the inverses. These are actual
group automorphisms, not just matrices with convenient eigenvalues.

Their twelve composites r^k s^e (0<=k<6, e=0,1) have twelve distinct
H1 matrices. They are distinct OUTER automorphisms, since inner maps
act trivially on H1. Rigidity realizes them by isometries:
[Prasad, Theorems A/B](https://doi.org/10.1007/BF01418789).
Separately, verified canonical retriangulation and complete
combinatorial enumeration give exactly twelve isometries. The matching
lower and upper counts prove completeness in the original a,b basis,
without any guessed original-to-canonical map.
The [official API specification](https://snappy.computop.org/manifold.html#snappy.Manifold.canonical_retriangulation)
states the certification/combinatorial route used here.

Both requested precision runs, 100 and 212 bits, return canonical
decorated isosig

    jLLzzQQccdffihhiiqffofafoaa_BBBabBaB.

The canonical cells are tetrahedra, with no finite vertices. All twelve
isometries preserve orientation. The faithful canonical cusp action
has two order-three elements, each preserving both cusps and fixing
three torus points on each. This upgrades R15's SOFTWARE-only
isometry enumeration; it does not certify source amplitudes, a full
G2 metric, or additional closed fixed components.

A separate numerical symmetry enumeration in the original triangulation
satisfies BOTH exact peripheral descent equations and gives the same
twelve H1 matrices. That secondary peripheral table is explicitly
not itself an interval certificate. It is not the foundation of the
complete-action proof. Verified m004 has eight isometries and therefore
no order-three element; this is a comparator, not a universal chirality
closure.

## 2. Complete character classification under the source symmetry

The exact H1 generators, acting on exponent columns, are

    R = [[0,-1],[1,1]],       S = [[1,1],[0,-1]],
    R^6 = S^2 = I,           S R S = R^-1.

Thus the action is faithful D6, order twelve. Its C3 is normal and
unique. The independent R72b map a->B,b->aB cubes to the identity on
the FREE generators and has the other nonidentity C3 matrix.

For a character with a->exp(2*pi*i*h_a), b->exp(2*pi*i*h_b), pullback
is h->A^t h. Circle period p means

    (A^t-I) h in p Z^2.

If d=abs(det(A-I)) is nonzero, the adjugate formula puts every fixed
point on the p/d grid modulo p. The resulting enumeration is exhaustive
over the CONTINUOUS torus, not a finite-sample conjecture. Its size is
d, the lattice index. Inversion's four fixed points and the rejection
of the identity's continuous fixed locus check both sides.

For p=1 the C3-fixed characters are, with zeta=exp(2*pi*i/3),

| Character (a,b) | H*(C,T;L) | H*(C,E;L^-1) | Isometry orbit size |
|---|---|---|---|
| (1,1) | (0,4,1,0) | (0,1,4,0) | 1 |
| (zeta,zeta^-1) | (0,3,0,0) | (0,0,3,0) | 2 |
| (zeta^-1,zeta) | (0,3,0,0) | (0,0,3,0) | same orbit |

These are R19's unchanged exact cohomology matrices, with the same
positive-source strengths abs(q)*beta>=1 and maximal domain.
At each nontrivial point P=-2, so neither lies on the exceptional
Alexander locus. All twelve actions preserve P/(xy) identically.
The two good characters each have a six-element S3 stabilizer, with
element orders 1,2,2,2,3,3. R19's example (-1,1) is NOT C3-invariant;
its orbit consists of all three nontrivial order-two characters.

The full sixfold symmetry, hence full D6, fixes only the trivial
scalar character: det(R-I)=1. A symmetric action can nevertheless
permute its vacua. We have not required all vacua to preserve every
symmetry, nor proven which internal isometries are gauge redundancies
in a completed theory. In particular two character representatives
are not automatically two physically inequivalent vacua.

The pair is holonomy-conjugate, NOT a pair of geometrically mirrored
manifolds or opposite fermion chiralities. All these isometries
preserve orientation, and both characters give three modes in the
SAME positive-charge sector for the same signed source.

## 3. The compact-parent lift: where the factor three enters

Use the ACTUAL R19 Cartan direction

    u=omega_1^vee=(4/3,1,5/3,2,4/3,2/3)

in simple-coroot coordinates. Simply connected E6 has cocharacter
lattice equal to the coroot lattice; the scalar subgroup exp(2*pi*i*h*u)
has period p=3. In E6/Z3, u is already a cocharacter and p=1.
The complete root and fundamental-weight orbits independently check
the distinction: exp(2*pi*i*u) is identity on every adjoint root
space but acts as exp(2*pi*i/3) on all 27 fundamental weights.

For p=3 the C3-fixed scalar parent holonomies are exactly

    h=(0,0), (1,2), (2,1) modulo 3.

All are central and induce trivial adjoint characters, hence four/one.
Every p=1 character has nine scalar lifts h+(i,j) modulo three.
All nine are enumerated. For either nontrivial C3-fixed character,
NONE has (A^t-I)h=0 modulo three. Its defect is central: invisible to
the adjoint, visible to the fundamental 27. This is why merely
checking adjoint phases would falsely certify the parent lift.

For example the recorded C3 matrix is A=[[-1,-1],[1,0]].
At h=(1/3,2/3), its defect (A^t-I)h=(0,-1); all other lifts retain
a nonzero defect modulo three. For h=(0,0), precisely three of the
nine parent lifts are invariant, recovering the central fixed locus.

This obstruction cannot be removed by an inner gauge lift that
preserves phi=u dF. Where dF is nonzero such a lift centralizes u,
and therefore commutes with every exp(t*u); conjugation cannot change
these scalar holonomies. Noncentral transport is a different,
unexcluded ansatz. Flipping u or the source sign also changes the
declared background rather than silently repairing this one.

The adjoint-parent option is positive at its stated scope: the entire
78 descends to E6/Z3, so its charged D5 spinor subspaces define genuine
representations of the unbroken subgroup. The absence of a fundamental
27 does NOT mean absence of all spinor matter. This retains
[B960's actual root-lattice fact](../../frontier/B960_l136_adjoint/FINDINGS.md)
without extending its 27-specific restriction into a false universal kill.

It also imposes a real compatibility cost. The fundamental-27 Higgs
fields of R4--R10 cannot simply be appended as ordinary representations
of this adjoint parent. Their old conditional action remains valid
in its own simply connected model; composing it with this quotient
requires a different, explicitly justified completion.

## 4. Symmetry compatibility is not a source law or an orbifold spectrum

C3 fixes the source arcs pointwise. Averaging the R15 scalar solution
over C3 preserves the source densities, strong asymptotics and linear
field equation, giving an invariant dF. On the undrilled Q the flat
connection is smooth across the sources and C3 has fixed points.
The based semidirect product then constructs an equivariant line
system for each invariant character. A rank-one fibre lift still has
three possible C3 phases; that is not a classification of all
principal-gauge-bundle lifts.

No quotient Q/C3 and NO projection onto invariant modes is performed.
Our three/zero result is the full kernel on the original sourced Q.
An orbifold invariant-subspace count would require a separate
calculation including the chosen fibre action.

The completed sub-duty is precisely:

> Within the prescribed scalar-holonomy source model, the full C3-compatible
> character locus and its compact-parent lift obstruction are computed;
> a pair-free isometry orbit survives in the adjoint parent.

This does not close PB-BOUNDARY or select its global form. Requiring
C3 invariance, selecting its nontrivial orbit, choosing m202 and the
source strengths/domain, and assigning physical fermion meaning are
not derived by this calculation. Symmetry supplies a finite menu
conditional on those requirements, not a dynamical preference.

## 5. The next physical calculation, on the same path

The immediate obligation is now an anomaly/defect completion with
the **actual global gauge group and charge lattice** retained.
R19's (Tr u,Tr u^3,Spin10^2-u)=(48,48,6) persists. The commuting
constant gauge mode remains finite-norm; calling the U1 nondynamical
without an action/domain argument is not a cancellation. A
Green--Schwarz or inflow mechanism needs real fields, allowed gauge
transformations, quantized coefficients and kinetic terms in THIS
background. Changing a group label or adding an anomaly-free 27
does not supply those ingredients.

In parallel, determine whether a noncentral simply connected
connection can preserve the source symmetry and give the desired
spectrum without this scalar-lift restriction. That is an alternative
within the same source path, not ruled out by R20.

Retain the non-normalizable holonomy variations, neutral low-energy
cusp channel, physical source/domain selection, Higgs/interaction
completion and common dynamical gravity. No mass, coupling or empirical
observable is predicted here, and the full TOE goal remains unachieved.

## 6. Evidence, failures and banking

The [word-control first run](holonomy_equivariance_word_control_first_run.json)
succeeds, exit 0, 2.051 s after startup. Both requested geometry
certifications pass; the exact character/parent calculation is complete.
[Nine new controls plus R19/R18](HOLONOMY_EQUIVARIANCE_CHECKS.txt):
34 passed, one optional-GUI warning, 20.73 s. The original
[basis-transfer failure](HOLONOMY_EQUIVARIANCE_FAILURE.txt), its code
and six failed tests are retained unchanged.

The [38-file broad regression](HOLONOMY_EQUIVARIANCE_REGRESSION.txt)
returns 250 passed, 13 failed, 8 errors, one warning in 267.36 s.
Its failed/error set is exactly R19's fifteen entries plus the six
original R20 basis-transfer failures. The successful control does
not rewrite that history or imply complete-repository green.
Only environment prefixes are redacted in public transcripts;
byte-faithful raw captures remain in explicitly excluded local files.
The native capture's leading deprecation warning is retained separately
from its complete JSON; parsing it required no scientific rerun.

Source and tests were sealed before each first execution, and remained
unchanged during all runs. No new B ID, source-branch merge, PR,
independent receiving-seat review or main banking is claimed.
Reporting-time governance: 27 pass / 3 fail, review due at 119 merges.
The attribution, static-vacuity and older literal-provenance debts are
retained; sealed digests and reader-currency checks pass. Receipt:
HOLONOMY_EQUIVARIANCE_GATES.txt. Authored staged whitespace passes;
captured pytest trailing spaces in the regression are not normalized.
