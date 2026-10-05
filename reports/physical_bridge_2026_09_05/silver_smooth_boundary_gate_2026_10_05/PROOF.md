# A constructive smooth kinetic domain, with a remaining physical joint

Authored before execution. Conditional argument, same-author finite
checks; no nonauthor analytic acceptance or complete interacting model.

## 1. Full trace and pointwise cyclic algebra

Use oriented orthonormal coframe(n,x,y) on the smooth boundary collar.
Write u=alpha+n wedge beta, with tangential basis(1,x,y,x wedge y).
Let ell_s=span(x+s i y), s=+1 or-1. The coefficient metric and compact
real form make k and its complement reducing, conjugation-stable,
orthogonal subbundles; this uses the supplied A4+A4 background, not just
a dimension count. With the invariant complex trace pairing, set

    A^0=k_C, A^1=ell_s tensor g_C, A^2=ann_trace(k_C) tensor area.
    D_A={alpha in A, beta in A^(perp_H)}.

Tangential dimension is4*248=992, dim A=24+248+224=496. The full trace
is1984-dimensional, D_A is992-dimensional. For each gauge coefficient
the slots are alpha(1,ell), beta(bar ell,area); for each complementary
coefficient alpha(ell,area), beta(1,bar ell). Each has two even and two
odd allowed components. This is a smooth LOCAL trace subbundle.

The degree-two bilinear cyclic pairing vanishes on A: k pairs trivially
with its trace annihilator, ell wedges with itself to zero. It is maximal.
Bracket closure follows from [k,k] subset k, [k,g] subset g and invariance
of the pairing, which implies [k,ann(k)] subset ann(k). The only other
potential nonzero boundary product is [A1,A1]; it vanishes because the
same ell is used for EVERY coefficient. These assertions do not make A
a differential subcomplex: d_t of a general k-valued function escapes
ell. Nor do they compute the fork's cohomological Lagrangian. A smooth
local condition and a finite cohomology condition cannot be identified
without solving the global boundary problem.

## 2. Current, combined reality, and universal principal ellipticity

Q=d_D+d_D* is formally symmetric Dirac-type; flatness, metric Higgs and
curvature enter lower-order terms, not this principal-symbol calculation.
In the displayed trace splitting its normal Green matrix is

    Gamma=[[0,-I],[I,0]].

For a basis S of D_A, S dagger Gamma S=0, rank S=4 per coefficient.
This proves maximal current isotropy. The physical full-form map of
R23/R61 is J conjugation, J=star with degree signs(+,-,-,+). It exchanges
tangential ell with normal bar ell, and gauge scalar with normal area.
It preserves both displayed domains, although bare conjugation exchanges
the helicities. Majorana does NOT force ell to be a real line.

Let xi=x xform+y yform be REAL, nonzero. Its tangential symbol is
q(xi)=i(epsilon(xi)-iota(xi)), with q^2=(x^2+y^2)I. A decaying half-space
solution has beta=-q(xi)alpha/|xi| (the opposite inward convention changes
the sign only). It satisfies D_A precisely when alpha in A and
A dagger q(xi)alpha=0. Use unnormalized bases(1,xform+s i yform) on
the gauge pattern and(xform+s i yform,area) on the complement. In BOTH
cases the restricted2x2 symbol has determinant

    -(x^2+y^2).

This never vanishes at nonzero real xi. Thus the boundary symbol is
complementary to every decaying Cauchy space, not just sampled Fourier
directions. Smoothness, maximal Green isotropy and this ellipticity give
a self-adjoint elliptic realization of Q on the fixed compact smooth
core, by the Dirac boundary framework of Bär--Ballmann. It has compact
resolvent and finite-dimensional kernel. These facts do not compute its
kernel or prove supersymmetry. The symbol proof is invariant under changes
of oriented orthonormal boundary frame; ell_s is a globally defined Hodge
eigenline. A smooth reducing coefficient metric is assumed throughout.

Opposite control: real ell=span(xform) gives restricted determinant-x^2
in the gauge pattern and-y^2 in the complement, and fails at directions
(0,1) and(1,0). Isotropy alone is insufficient. Taking beta in ell instead
of its Hermitian complement fails the current test. Gauge constant0-forms
and their signed Hodge-dual3-forms are retained; in the trivial reducing
k block they extend to global Q-zero sections. No full boson gauge-domain
or massless charged census follows from that observation.

## 3. Holomorphic action: a supplied reference subtraction

Let CS(C)=tr(C wedge dC+2/3 C^3), F=dC+C^2. Direct graded variation gives

    delta integral CS=2 integral tr(delta C wedge F)
                      -integral_boundary tr(C wedge delta C).

R60/R70 already own this variation and its affine reference term.
At C=C0+a, the a wedge delta a boundary pairing vanishes for a_t in ell.
The C0 wedge delta a term need not vanish. Keeping it, an explicit
SUPPLIED correction +integral_boundary tr(C0 wedge a) cancels it.
For fixed flat reference C0, the relative functional becomes

    integral tr(a wedge D0 a+2/3 a^3),

up to the constant integral CS(C0), since
CS(C0+a)-CS(C0)=2tr(a F0)+tr(a D0a+2/3a^3)-d tr(C0 a).
This relative construction is covariant if the reference transforms too.
For a fixed reference, restrict to transformations compatible with it,
such as identity near the boundary or internally constant compact k
transformations commuting with C0. Unrestricted large/boundary gauge
invariance, global trivialization, supersymmetric completion and quantized
coefficient are NOT proved by this local transgression calculation.

The pointwise boundary cubic vanishes on a common ell, but bulk E8
interactions are not removed: an SU5 subalgebra already contains
tr(E12[E23,E31])=1 in its fundamental normalization. This is a nonzero
interaction control, not an observed Yukawa. The full normal boson law,
D-term variation and reality-compatible boundary action remain duties.

## 4. Supergauge compensation cannot silently erase invariant data

Work in the reducing abelian Cartan gauge block. The supplied twisted
component variation contains a nonzero multiple of d_t bar(chi) in F_t
(Braun B.7; R61). Absorb that convention-dependent nonzero multiplier
into chi. For a Fourier covector xi its rejected norm under ell_s is

    ||(1-P_s)i xi chi||^2=(x^2+y^2)|chi|^2/2.

The rigid WZ-gauge WHOLE-chiral projector therefore rejects nonconstant
gaugino profiles that the elliptic fermion domain of section2 admits.
Demanding they all be constant removes traces and does not automatically
leave a maximal self-adjoint domain. This is this projector's mismatch,
not a no-go for all boson/gauge-class completions.

Luedeling4.3--4.7 supplies the missing gauge check. Infinitesimally in
the abelian block delta Phi_i=partial_i Lambda and
delta V=i(Lambda-bar Lambda)/2. At linear order

    Z_i=2 partial_i V+i(bar Phi_i-Phi_i).

For Lambda=theta^2 f, delta F_i=partial_i f and
delta V|theta^2=i f/2. Taking f=-chi cancels the displayed i xi chi
auxiliary component in Phi, but leaves WZ gauge and transfers that same
response to V. The theta^2 component

    Z_i|theta^2=2 partial_i(V|theta^2)-i F_i

is unchanged. Discarding V after this compensation is an invalid gauge
operation; an explicit opposite control catches it. A WZ-preserving
parameter has only a real lowest component and cannot do this job.
Thus a gauge-COVARIANT projector on Z has the same rejected response in
this block. A gauge-CLASS law that constrains Phi but allows compensating
vector components might be different; it has NOT been disproved or
completed here. Boundary supergauge invariance of the complete action is
not inherited from the paper's compact winding argument.

Real boundary gauge gradients also intersect nonreal ell only at zero;
internally constant four-dimensional k transformations survive. A finite
cohomology gauge sector does not justify deleting nonzero boundary modes
from a physical fermion operator. This section protects the positive
kinetic construction while locating the precise unfinished joint.

## 5. Scope and continuation

Conditional smooth elliptic/current/reality construction: YES. Actual
global kernel, fork Lagrangian realization, full superfield/boson boundary
closure, complete anomaly/inflow and physical chirality: NOT established.
One smooth-domain positive is not a selected physical theory or a proof
that the foundational principle generates the added choices. Next derive
a coupled gauge-class-compatible boson law and its normal response, or
price an explicit boundary sector, before claiming any particle index.

Primary sources: https://arxiv.org/html/1307.3021v1 (3.2--3.5),
https://arxiv.org/html/1102.0285v1 (4.3--4.7),
https://arxiv.org/html/1812.06072v2 (B.7). The determinant, transgression
application and scoped compensation argument above are authored here.
