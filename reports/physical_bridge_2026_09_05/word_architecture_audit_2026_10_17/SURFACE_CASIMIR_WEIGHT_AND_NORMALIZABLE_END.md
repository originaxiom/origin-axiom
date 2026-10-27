# The physical surface invariant has weight six, with a conditional norm selector

October 27, 2026. UNREVIEWED author hand derivation and source recovery.
No scientific import, collection, solver, symbolic engine or experiment.
This checks the applicability of the preceding compact-orbit selector
against the SAME supplied surface parent. It is not a completed surface
solution, a selected E8 vacuum or an execution certificate.

## 1. Recover the actual field before using a scalar modular theorem

The source already fixes the relevant geometry: surface_global_spin,
surface_parent_dictionary, and HODGE_GEOMETRY_REDUCTION_AND_FIBRE_MAP
derive the full canonical weight three. Their formulas are reused,
not discovered here. In the conventional BHV parent the Higgs is

    Phi in H0(X,K_X tensor ad(P)),

where X is the complex TWO-dimensional elliptic total space. The
original curve parent instead has two spin-valued fields; neither
that parent nor a relative one-form can be substituted silently.
For the compact-cover candidate replace a fibre by its specified
branched Y and retain the actual geometric total-family maps.

I personally reread BHV (0802.3391), equations 3.19-3.23 and
3.39-3.41 with their explanatory paragraphs:
https://arxiv.org/html/0802.3391
The source supplies the effective field theory; genesis has not derived
it. Surface_variational_join explicitly preserves the distinction
between a local equation map and the full action identification.

For j=C tau+D the retained modular coordinates give

    d tau'=j^(-2)d tau,
    d tau' wedge dz'=j^(-3)d tau wedge dz.         (1)

The extra d tau term in dz' drops out of this wedge. Removing d tau
from Phi is a base-line twist; it is not a neutral contraction with
a globally fixed vector. A normal-frame scalar normalization also
depends on the metric and is not holomorphic coefficient equality.

## 2. The invariant's holomorphy and weight follow from this parent

Use the complex invariant bilinear form extending the positive compact
pairing, with a declared common normalization. Define the quadratic
Casimir as a SYMMETRIC tensor of canonical forms,

    Q2(Phi)=kappa(Phi tensor Phi) in K_X^2.        (2)

This is NOT the exterior wedge Phi wedge Phi, which would vanish by
degree. For an admitted holomorphic background, gauge invariance and
Dbar_A Phi=0 imply

    dbar Q2=2 kappa(Dbar_A Phi tensor Phi)=0.       (3)

The gauge-connection commutators cancel by invariance of kappa. Thus
base holomorphy of this invariant need not be added independently
WHEN the actual full surface F-equation holds. Holomorphy on each
isolated fibre alone would not imply (3) in the base direction.

Full compact gauge conjugation leaves (2) invariant, including inner
based/deck compensators. In the canonical parent with no extra scalar
line, (2) has no additional character beyond K_X^2. Additional admitted
R/flat lines must be carried if the model changes that field assignment.

Assume Phi is smooth on the specified completed Y fibre and equivariant
under its Q8 deck action. The preceding invariant-quadratic descent
therefore applies to the fibre part of (2): locally

    Q2=c(tau) (d tau)^2 pi^*(dz^2),
    c(gamma tau)=j^6 c(tau).                     (4)

The coefficient is WEIGHT SIX, not weight two. The preceding M2=0
corollary remains correct for its explicitly untwisted relative curve
problem; it is not the physical surface corollary. This is an
applicability correction, not evidence that the curve proof is false.
Neither determinant of a Yukawa matrix nor a Lie algebra named E6
is identified with the modular form E_6 below.

With trivial character and holomorphic cusp extension, the existing
scalar ring gives

    c=C0 E_6(tau), C0 in C.                      (5)

Weight six has one basis monomial, unlike weight two. This retains a
complex amplitude unless a real end/norm/dynamical law removes it.
Equations (3)-(4) derive two previously conditional requirements from
the supplied parent; they do not derive that parent from foundations.

## 3. A genuine whole-surface L2 condition is stronger than bounded c

Suppose, as an ADDITIONAL ADMISSIBILITY CONDITION, the entire background
Phi has finite positive L2 norm on the modular total space. This is
not inferred from finite residual energy, nor from L2 variations about
a possibly nonnormalizable reference background.

For a Kähler metric in complex dimension two, a top holomorphic form
has its inverse determinant metric in its squared norm; multiplication
by dvol cancels that determinant. In a unitary gauge frame, writing
Phi=P d tau wedge dw, this gives a fixed positive conventional factor
times kappa(P^dagger P)d^2tau d^2w. Mixed horizontal/fibre metric terms
do not invalidate this determinant identity.

In an orthonormal compact-real coefficient basis, the elementary
inequality |sum z_a^2|<=sum |z_a|^2 yields

    |kappa(P P)| <= kappa(P^dagger P).            (6)

Away from ramification, (4) has fibre coefficient
c(tau)(dz/dw)^2. Integrating (6) over Y gives

    integral_Y kappa(P^dagger P)d^2w
       >= constant * |c(tau)| integral_Y pi^*(d^2z)
       = constant * 8y |c(tau)|, y=Im tau.       (7)

The pullback density is |dz/dw|^2 d^2w, not the square root of this
density; ramification points have measure zero. The area of the marked
elliptic period cell in the z coordinate is y and the degree is eight.
All common trace/norm factors stay positive; their values do not affect
convergence. The smooth-cover physical metric remains a supplied
completion, but its arbitrary scale cannot repair this norm divergence.

Consequently finite L2 of Phi implies the cusp bound

    integral_(y>Y) integral_(-1/2)^(1/2)
                  y |c(x+iy)| dxdy < infinity.  (8)

It is consistent with the weight-six law: y|c|dxdy is modular invariant.
No auxiliary mass, fitted exponent or finite counterterm is inserted.

For trivial T-character, holomorphic c is periodic. Its Laurent/Fourier
coefficients satisfy, at every cusp height,

    |a_n| exp(-2pi n y) <= integral_0^1 |c(x+iy)|dx.

Any nonzero a_n with n<=0 contradicts (8), including a nonzero constant
term. Thus (8) forces c to be a weight-six CUSP form, even without first
assuming boundedness at the cusp. But S6(SL2Z)=0. Therefore

    finite-L2 whole Phi + canonical untwisted global F-equations
    + full modular/deck equivariance => Q2(Phi)=0. (9)

This is a conditional end-law consequence, not a global existence proof.
It rules out the nonzero C0 E_6 option within those hypotheses. In the
specific rank-two root section Q2 is proportional to q, so q=0 selects
its nilpotent orbit. In full complex E8, a zero quadratic Casimir ALONE
does not imply nilpotence: the other invariant polynomials remain.
Nor does (9) say Phi=0; nilpotent fields can be nonzero.

## 4. Rejecting controls and the actual remaining input

The norm assumption cannot be weakened to finite action without a proof:
zero residuals can have zero residual-square energy and divergent field
norm. The existing local nonzero core and its finite normal-cutoff
variations prove neither (8) nor a global finite norm of that background.
The earlier curve parent's complete L2 law is for different spin fields;
it cannot pay the surface-background assumption by transfer.

There is also an explicit character control. From the classical eta
product and modular laws,

    eta(tau+1)^12=-eta(tau)^12,
    eta(-1/tau)^12=-tau^6 eta(tau)^12,
    |eta(tau)^12| ~ exp(-pi y).

Thus eta^12 is a nonzero weight-six cusp form WITH a character,
and it satisfies the necessary integral (8). It is not a scalar form
of trivial character. This does not construct an admitted Phi with
that Casimir, but rejects any extension of the scalar vanishing to
all R/flat lifts. Those lifts need their actual action, not a name.
An allowed proper subgroup, extra fibre defects/poles, broken-state
family or different background norm may also change the conclusion.
In particular a nonconstant warp/dilaton/kinetic weight would have to
be retained in the physical norm; (8) uses the stated unwarped Kähler
top-form norm and a common positive coupling, not an arbitrary new
weight that damps the cusp.
None is excluded by (9).

The eta product and modular law were personally checked in DLMF
27.14.12 and 27.14.14 / 23.18.5:
https://dlmf.nist.gov/27.14
https://dlmf.nist.gov/23.18
The scalar weight-six dimension/cusp statement reuses the previously
read classical dimension formula and main's B1691 Mbasis convention.
No new numerical value comparison or literature-wide novelty claim.

## 5. Before/after and the next physical question

| Duty | Derived conditionally here | Still requires actual construction |
|---|---|---|
| Base holomorphy of the quadratic invariant | Follows from the full Dbar_A Phi=0 equation | A full background satisfying that equation |
| Its modular weight/character | Six and no extra character for honest K_X tensor ad(P) | Canonical physical assignment, based lift and any additional lines |
| Holomorphic bounded scalar coefficient | One C0 E_6 family | Genuine cusp/domain/state law |
| Finite-L2 whole-field sector | Necessarily Q2=0; rank-two section then q=0 | Whether that sector is the admitted physical vacuum class; nonzero global existence |

The next duty is to derive or explicitly price the global background
admissibility from the actual variational/kinetic construction: is Phi
itself normalizable, or is a nonnormalizable reference/source allowed
while only its fluctuations are normalizable? Preserve the full source
response in the latter case. Then solve the coupled moment/mixed
equations and global charged lift on the retained branch before any
mode count. No SM three-generation or gravity obligation is discharged.
This note is outside all earlier reviews and marks no foundational
input paid. The full mission remains unfinished.
