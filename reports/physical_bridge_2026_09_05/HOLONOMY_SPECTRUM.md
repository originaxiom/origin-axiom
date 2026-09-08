# R19: the extra pair is holonomy-dependent; quantum consistency is still owed

2026-09-08. Path-local research result, not a global B arc or a TOE claim.
Pre-execution seal: **ce08c24b**. [Design](HOLONOMY_SPECTRUM_DESIGN.md),
[retrieval](HOLONOMY_SPECTRUM_PRIOR.md), [pre-execution checks](HOLONOMY_SPECTRUM_PREEXEC.txt).

**Result.** Keep R15's prescribed three-source m202 geometry, scalar
field and compact E6 Cartan direction, and R18's strong-source maximal
complex. Allow a commuting unitary flat connection extending across
the source arcs. Generic adjoint holonomy gives **three positive-charge
spinor H1 modes and no negative-charge conjugate H1 modes**. Trivial
holonomy and an explicit nontrivial exceptional locus retain four/one.
This removes the extra pair in a changed operator; it neither predicts
a physical mass nor selects that operator from the originating object.

The same calculation prices two physical duties: every nonzero continuous
abelian holonomy deformation has a non-normalizable cusp period, and
the net-three spectrum has an extra-U(1) gauge anomaly if treated as a
standalone dynamical four-dimensional spectrum without completion.
The positive mode-count result is not discarded by these duties.

## 1. Which earlier results are being joined

The Alexander polynomial is **already present** in the SM seat's B1282
addendum and `verification/siblings_faces.py`, pinned at d1a91c7a.
That branch-qualified B1282 is not a newly allocated main arc. The
producer itself, not just its headline, is re-executed by extracting its
named pure function without running its unrelated top-level census.
B787's integer group-ring Fox functions supply a second producer;
triangular cocycle multiplication and native SnapPy provide further checks.

[R15](GLOBAL_SINGULAR.md) supplies the prescribed global scalar field
and the E6-adjoint spinor branching. [R18](WEIGHTED_COHOMOLOGY.md)
supplies the weighted-complex comparison for trivial gauge transport.
[B864](../../frontier/B864_anomaly_ledger/FINDINGS.md) already gives the
charge-one spinor's anomaly. Its qualified computation is retained:
hypercharge uniqueness over fifteen fields is not uniqueness over a
sixteen-field generation including the right-handed neutrino.

Gauge holonomy affecting matter cohomology is standard, not a new
physical mechanism: [Pantev--Wijnholt](https://arxiv.org/pdf/0905.1968),
sections 3.7 and 3.10, explicitly incorporate flat spectral line bundles.
The work here is the full character classification and weighted-domain
join for this declared sourced background, with its anomaly/input costs.

## 2. Analytic comparison with a unitary flat bundle

Let Q be the compact core before drilling and let k>0 disjoint proper
geodesic arcs obey R15's source hypotheses. Their neighbourhoods are
N=disjoint union of D^2 x I. Let C be the exterior, T the lateral tube
annuli, and E the remaining external boundary; T and E meet along their
cap circles. Use the complete metric and source field of R15--R18,
positive cusp endpoint totals, and every effective strength abs(q) beta>=1.
The actual source locus, amplitudes and maximal domain remain inputs.

Choose a unitary flat line bundle L on Q, restricted to the drilled
manifold. In particular its new source meridians have holonomy one;
this does not require trivial holonomy on the original cusp torus.
Denote its covariant exterior differential by d_A and put H=qF. Then

    exp(H) (d_A+dH wedge) exp(-H) = d_A.

As in R18 this is a unitary identification with the Hilbert space
weighted by exp(-2H), NOT bounded similarity on the old unweighted
space. The globally bounded real corrector in F changes this weight
by equivalent factors and does not change the maximal covariant graph
domain as a set.

On each product end, radial parallel transport identifies L with the
pullback of the bundle on a transverse slice. Flatness makes the
tangential connection independent of radius; unitarity preserves fibre
norms exactly. Thus d_A splits as the radial derivative and a fixed
covariant tangential differential. R18's forward/backward radial
integrals commute with that tangential differential with the usual
graded signs. Their Hardy/Volterra bounds are unchanged, including
the angular form weights and the whole punctured-torus cusp estimates.
No globally periodic scalar trivialization is assumed, and no angular
partition of unity with growing derivative is introduced at infinity.

The same weak distributional trace proof applies after testing in
parallel local frames. Relative ends force the zero trace; at absolute
ends average the projection and homotopy over the same regular slab.
The cutoff identity retains its derivative term. Truncate the whole
cusps before the finite-height line collars, retaining the cap condition
at their corners. These operations give bounded covariant chain maps
to the compact mixed-boundary complex. On that compact core the standard
mixed de Rham parametrix applies in unitary parallel local frames.
Its finite-rank projection, composed with the end maps as in R18,
annihilates exact forms and supplies closed range. Therefore the full
cohomology, hence the harmonic kernel of this Hilbert complex, is

    H*(C,T;L_chi)          for q=+1,
    H*(C,E;L_chi^-1)       for q=-1.

This is the analytic extension of R18, not an inference from a finite
matrix or index. The eight local form checks test flat nilpotence,
covariant homotopy and weighted conjugacy; a curved-connection mutant
fails. The ten unchanged R18 tests also pass. Those tests do not replace
the domain argument or constitute independent mathematical review.

## 3. The finite pair, without an unnecessary absolute-exterior assumption

The decomposition Q=C union N is excisive after the usual collar
thickening, with overlap homotopy equivalent to T. Consequently

    H*(C,T;L) = H*(Q,N;L).

Each component of N is contractible. Thus H0(N;L)=C^k and its higher
groups vanish. A parallel section on connected Q that vanishes on a
nonempty N is zero, so H0(Q;L)->H0(N;L) is injective. The exact sequence
of the pair gives, degree by degree,

    b(C,T;L)=(0, k-b0(Q;L)+b1(Q;L), b2(Q;L), b3(Q;L)).

This relative formula does not need the primitive nonzero arc-intersection
vector used in R15's separate calculation of the ABSOLUTE exterior.
The stronger hypotheses of that calculation are not imported by habit.
Complementary-boundary Poincare--Lefschetz duality gives

    H^j(C,E;L^-1) = H^(3-j)(C,T;L)^*.

The k=0 tests are ordinary-base cochain controls, not claims of a
zero-source background satisfying the strong positive-source hypotheses.

## 4. The actual m202 character calculation, all characters

SnapPy returns generators a,b and the single relator
R=aabbAbAABBaB. Both exponent sums are zero, so the full unitary
character space is (x,y) in U(1)^2, with a->x and b->y.

A presentation complex is not automatically a model for manifold
cohomology. Here R is cyclically reduced and has no proper word period;
all possible proper periods are checked. The one-relator asphericity
theorem makes this presentation complex a K(pi,1), just as the complete
hyperbolic manifold is. See [Dyer--Vasquez, Theorem 2.1](https://doi.org/10.1017/S1446788700015147).
The native run also verifies m202's hyperbolic structure with positive
shape intervals at 100 and 212 bits. This does not certify the chosen
source arcs or an E6/G2 physical realization of them.

With

    P=x^2*y+x^2+x*y^2+x*y+x+y^2+y,

the exact covariant cochain complex is

    C --delta0--> C^2 --delta1--> C,
    delta0=(x-1,y-1)^t,
    delta1=(-(y-1)P/x, (x-1)P/x).

All four calculations agree on P, up to the declared overall sign or
Laurent unit. The native polynomial agrees in the unchanged a,b basis;
the other recorded matches are its swap/inversion symmetries. The
group-ring fundamental identity delta1 delta0=0 is checked symbolically;
omitting a Fox term violates it. Hence:

| Character | Base b0,b1,b2,b3 | Three-arc (C,T) | Complementary (C,E), dual character |
|---|---|---|---|
| x=y=1 | (1,2,1,0) | (0,4,1,0) | (0,1,4,0) |
| nontrivial, P not zero | (0,0,0,0) | (0,3,0,0) | (0,0,3,0) |
| nontrivial, P=0 | (0,1,1,0) | (0,4,1,0) | (0,1,4,0) |

This classification is exact on the entire character torus: away from
the trivial character delta0 has rank one; delta1 has rank one exactly
when P is nonzero. It is not extrapolated from a finite grid.

For unitary x,y,

    P/(xy)=1+x+x^-1+y+y^-1+x/y+y/x=|1+x+y|^2-2.

Thus the exceptional set is explicit. Its complement, also excluding
the trivial character, is open dense. Simultaneous inversion preserves
the classification. In particular each of (-1,1),(1,-1),(-1,-1) gives
three/zero. All eight nontrivial order-dividing-three characters do too.
But x=y=(-3 +/- i sqrt(7))/4 are nontrivial UNITARY exceptions and
retain four/one; the independent Sage number-field calculation confirms
their ranks exactly. "Every nontrivial Wilson line removes the pair"
would be false.

The relative mapping-cone calculation uses degree dimensions (1,2+k,1,0),
d0=(x-1,y-1,t1,...,tk)^t and d1=(delta1,0,...,0). Unitary fibre
identifications ti do not change the answer. Its actual matrix ranks
agree with the separate exact-sequence formula for every tested k.
The 31 character rows are predeclared CONTROLS (including repeated
trivial characters across grids), not a census or vacuum count.

Our sign convention is N16-Nbar16=h1(C,T)-h2(C,T)=3, whereas
chi(C,T)=-3. No Euler sign is silently equated to a particle count.

## 5. A genuine compact-parent flat connection, with its price

The actual R15 Cartan computation reproduces E6's 72 roots and

    78 = 45_0 + 1_0 + 16_(+1) + conjugate16_(-1)

under u=omega_1^vee. In the simple-coroot basis,

    u=(4/3, 1, 5/3, 2, 4/3, 2/3).

In simply connected compact E6, 3u is a cocharacter; u is not.
Consequently rho(a)=exp(i*pi*u), rho(b)=1 realizes (-1,1) on the
charged adjoint, but its parent order is SIX, not two. The parent
representation is genuine: the commuting images satisfy R because
its exponent sums vanish. This example does not infer a physical
global gauge quotient from adjoint phases alone.

Locally a closed real one-form connection in direction u has F_A=0
and commutes with phi=u dF. Thus the same commuting BPS equations and
source field remain satisfied. The Lie algebra of the commutant stays
D5+u1: this does not contradict B953/B955/B956 rank preservation.
An arbitrary character need not preserve every source-permuting
isometry; neither that equivariance nor object selection is inferred.

The actual cusp peripheral words have exponent rows

    (-2,3), (1,2), (-1,3), (-3,2),

a rank-two restriction map. Every nonzero infinitesimal abelian
holonomy change therefore has a nonzero period on at least one cusp.
R13's period lower bound then makes its one-form norm infinite on
the complete canonical hyperbolic end. Direct radial controls give
integral_S^infinity 1 ds=infinity for the tangential-period one-form,
versus exp(-2S)/2 for a constant zero-form. This is the distinction
between a fixed flat background and a normalizable dynamical Wilson
modulus. Zero curvature alone does not remove the distinction.

No pole mass, low-energy mass scale or generated pair-mass coupling
has been calculated here. The kernel changes because the operator's
flat holonomy changes. Giving an otherwise unmodified W=0 kernel an
arbitrary mass parameter is not what this calculation does.

## 6. The anomaly is carried by the net three, not by the extra pair

Using the actual charged roots, the D5 spinor/vector quadratic trace
ratio is two, and the pure D5 cubic trace is zero. In the u-charge
normalization above and T(10)=1, both four/one and three/zero have

    (Tr u, Tr u^3, Spin(10)^2-u) = (48,48,6).

One vectorlike pair gives zero in all three entries. Removing it
therefore does not cure these anomalies. This is B864's charge-one
spinor calculation reproduced and applied to the actual R15/R19
spectrum, not a new anomaly law or an anomaly of SM hypercharge.

Normalization is checked with the E6 fundamental representation too.
The dominant omega_1 is minuscule (its pairings with the roots are
0,+/-1), so its 27-element Weyl orbit is the full weight set, each with
multiplicity one. It gives u charges

    conjugate16_(1/3) + 10_(-2/3) + 1_(4/3)

when the positive ADJOINT sector is named 16 as above. Indeed the
D5-dominant spinor weight u-alpha_1 of the 27 projects to minus the
D5 projection of alpha_1 in the positive adjoint sector. The Weyl
orbits are dual. Conventional labels can conjugate both names; the
charge dimensions and anomaly calculation do not depend on that naming.

With psi=3u these become the familiar 1,-2,4, and the full 27 has zero
linear, cubic and mixed anomaly, as B864 states. This is NOT the
charge pattern of an adjoint-origin 16_(+1) under u. Nor can adding
an anomaly-free complete 27 cancel a pre-existing nonzero anomaly.
Rescaling u to the integral cocharacter changes anomaly coefficients
homogeneously, not whether they vanish.

In the canonical seven-dimensional gauge action a commuting constant
gauge zero-mode has finite internal norm on finite-volume Q; the removed
lines have zero volume. Flat A and commuting phi do not Higgs this
extra U(1). Consequently its dynamical status cannot simply be borrowed
from a different infinite-volume local model in which it is absent.
The standalone four-dimensional truncation containing this massless
U(1) and just these charged fermions is anomalous unless completed.

Inflow and massive/Green--Schwarz U(1) mechanisms are known options,
not excluded routes. [Pantev--Wijnholt, section 3.4](https://arxiv.org/pdf/0905.1968)
discuss them explicitly. [Witten](https://arxiv.org/pdf/hep-th/0108165),
equations (2.7) and (3.11)--(3.14), relates abelian/mixed inflow to
actual internal forms and their boundary integrals. Applying those
mechanisms here requires that geometry, field content and coefficients;
naming them does not supply the missing completion. Pure D5 cubic
vanishing is not certification of all local/global quantum anomalies.

## 7. What has advanced, what has not, and the next physical calculation

The result discharges the extra-pair persistence question in the stated
unitary strong-source maximal class: the pair is absent off the explicit
exceptional locus, not an unavoidable obstruction of this model.
R18's W=0 four/one statement is preserved exactly, not retracted.

The remaining load-bearing duties are:

1. Derive or justify the actual source manifold, disjoint geodesic arcs,
   density strengths, compact parent, physical fibre/domain and holonomy
   from the program's source. Compute the source isometries' action on
   the character torus before claiming a symmetry-compatible choice.
   Three input arcs still enter the general generic answer k/zero.
2. Construct the extra-U(1) anomaly/defect completion in the SAME action,
   with its internal forms, allowed gauge transformations and coefficients
   checked. A formal cancellation by an added field is not its derivation.
3. Establish the physical Lorentz/chirality dictionary, interactions,
   gauge breaking and a controlled four-dimensional limit. R17's neutral
   low-energy cusp channel is not removed by a Wilson line under which
   the neutral sector is uncharged; a separated finite 4D EFT does not
   follow from the charged-kernel count alone.
4. Connect the actual matter construction to dynamical gravity and a
   discriminating observable, without changing parents or input budgets
   between headlines. The certified partial-filling boundary route is
   retained; it has not been composed with this source model.

These are scoped obligations, not assertions that the repository has
no relevant ingredients or that the full TOE goal is impossible.

## 8. Reproduction, failure custody and banking

[Symbolic first run](holonomy_spectrum_first_run.json): exit 0, 7.411 s.
[Native first run](holonomy_spectrum_native_first_run.json): exit 0,
0.653 s after startup; Sage 10.7/SnapPy 3.3.2, exact number-field
controls and positive interval hyperbolicity at both precisions.
Both JSON captures parse completely; neither needed a repaired rerun.
[Focused tests](HOLONOMY_SPECTRUM_CHECKS.txt): 25 passed (15 new + 10
unchanged R18), one optional-GUI warning, 20.12 s.
[Broad regression](HOLONOMY_SPECTRUM_REGRESSION.txt): 36 enumerated
files, 237 passed, 7 failed, 8 errors, one warning, 289.83 s.
Every failed/error test ID matches R18. Older sources/tests remain
unchanged with their separate successful controls; no failure is hidden.
Environment path prefixes alone are redacted in the public regression
receipt; its raw tool capture is retained in the named local excluded file.

The entire tree was quiescent during scientific and certifying runs.
R19's literal provenance fields and the existing sealed digests were
checked BEFORE execution. The older global provenance failure was
reported then, not waived. No B number, independent receiving-seat
acceptance, full-repository green or main banking is claimed. Reporting
gates give 27 pass / 3 fail, with review due at 116 merges. The failures
are the retained attribution footprint, two old static-vacuity flags,
and older literal-provenance omissions; seal digests and document
currency pass. See HOLONOMY_SPECTRUM_GATES.txt. The earlier reporting
handle was missing on resumption, with no live gate process; this is
an observed replacement pass, not recovered output or a scientific rerun.
The staged whitespace check also flags five trailing spaces copied from
pytest in the preserved regression receipt; the authored-file check passes.

The 2026-09-08 all-head refetch advances the SM seat to 3f4ce9af.
Its incoming B1300--B1302 concern Wilson-line thinning and tree-level
mass ranks on the CLOSED Y9/Y12 tower and retain their vector-like
qualification. Their progress-log entries and change list were read,
not independently verified or merged. They are not a completion of
this different, sourced-background construction. R19's polynomial
producer remains pinned to d1a91c7a.
