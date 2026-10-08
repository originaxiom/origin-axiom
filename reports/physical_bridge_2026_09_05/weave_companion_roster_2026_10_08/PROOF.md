# Complete zero roster for the supplied minimal twists

This is an authored conditional analytic argument. Tests check its finite
algebra and local formulas, not an independent global PDE certification.

## Ordinary spin sections on the complete cusp

Write g = Omega^2 |dz|^2, Omega = 1/(r log(1/r)). A positive spin section
is h(z)(dz)^(1/2) in a unitary flat gauge frame. Its squared norm measure
is proportional to |h|^2 dr/log(1/r) dtheta. A negative-chirality zero
section has the conjugate holomorphic description with dual gauge bundle.
The complete unitary Dirac operator uses its canonical complete-manifold
domain. An L2 smooth zero solution belongs to this domain; there is no
freely selected finite-distance boundary projector in this benchmark.

Gauge holonomy -1 requires half-integral Laurent exponents. The term
z^(-1/2) gives integral dr/(r log(1/r)), which diverges, and every more
singular term diverges. The term z^(1/2) is integrable. Angular Fourier
orthogonality excludes cancellation of these divergences. Thus L2 zero
sections use the canonical parabolic extension with both weights1/2.
Its ordinary degree is -1 by Mehta--Seshadri Corollary1.10. Their
Proposition1.12 says the irreducible unitary rho representation is
parabolically stable. Since all weights are equal, every rank-one
subbundle has the same weight1/2: ordinary stability follows with slope
-1/2. Tensoring any degree-zero spin line preserves it. A nonzero section
would saturate to a line subbundle of nonnegative degree, a contradiction.
Consequently BOTH spin chiralities in rho have zero L2 kernel, since the
dual unitary representation is again rho with the same canonical weights.

Important: the canonical extension of the DUAL flat bundle is not the
ordinary dual of the canonical extension. The latter has degree+1;
the former has degree-1 here. Nor does compact H1 of the extension give
the negative spin kernel: the complete-cusp L2 condition differs at the
critical weight. The compact sheaf Euler -1 is not a physical Dirac index.

The four spin structures on the compact elliptic curve are its four
two-torsion lines S, all degree zero and bounding at the removed point.
For a one-dimensional Q8 character chi the peripheral holonomy is+1.
Its spin coefficient has integral exponents: exponent0 is integrable,
negative integer exponents are not. L2 zero sections therefore equal
H0(E,S tensor L_chi). A degree-zero line on an elliptic curve has a
section iff it is trivial, then exactly one. All four Q8 line characters
are the four two-torsion characters of the a,b cycles. Hence the spin
kernel selects chi=S^(-1), with both spin chiralities giving the same
dimension. This is a finite kernel statement even though zero lies in
the essential spectrum of the rho sector.

## Gauge modules rather than dimensions alone

Use H = SU3_colour x SU2_weak x SU3_family. The E8 branching used in the
preceding packet is retained, with 6 = rho tensor 3_family. Rebuilding
the exterior-power characters at a generic H torus and projecting onto
all five Q8 irreducibles gives the multiplicity modules

    V1 = (8,1,1)+(1,3,1)+(1,1,8)+(3,1,6)+(bar3,1,bar6), dim55;
    Vchi = (1,1,1)+(1,1,8)+(3,1,bar3)+(bar3,1,3), dim27,
           for each of the three nontrivial chi;
    Vrho = (3,2,bar3)+(bar3,2,3)+(1,2,8)+2(1,2,1), dim56.

The reference derives these from End(rho tensor3), Lambda2 and Lambda3
using tensor symmetries and integer weight convolution. The native route
uses exact eigenvalue characters and Q8 averaging. Agreement of dimensions
alone is insufficient; every joint torus weight must agree.

The complete scalar module is V1. The preceding compact-cover calculation
gives one-form module F=V1+Vrho for either Hodge type. An ordinary-spin
slot has V1 at trivial S or Vchi at any nontrivial S. In particular it
never has a weak doublet. This proves there is no finite companion zero
mode with the representation R=(1,2,8) carried once by F.

## Reality and the minimal twist comparison

In the Andrews--Dorey charge convention the four independent LEFT fields
have (Q45,QA,QB) equal to (1,1,0),(1,-1,0),(-1,0,1),(-1,0,-1).
The right fields are their Majorana/Hermitian conjugates, not four extra
independent left species. Take R line bundles from the SAME compact spin
line S, so total internal charge q means S^q; a,b in{-1,0,1} specify
QT=Q45+a QA+b QB. Additional flat R line bundles would change the question.

For q=0 the zero module is V1; for q=2 or-2 it is F; for q=1 or-1 it is
the ordinary-spin module above. These identifications refer to the
specified minimally twisted first-order operators. They do not follow
from representation labels alone if curvature/Yukawa/source terms are
changed. All nine choices keep all four slots and all spin structures.

| Twist category | Number of choices | Zero module | Dimensions for S trivial or nontrivial |
|---|---|---|---|
| a=b=0 | 1 | four spin modules | 220 or108 |
| exactly one of a,b nonzero | 4 | V1+F+two spin modules | 276 or220 |
| both nonzero | 4 | two V1+two F | 332 for all S |

The same charge table gives zero, one or two neutral LEFT supercharge
slots, conventionally suggestive of four-dimensional N=0,1,2. It is not
proof that a globally defined interacting curved action preserves them.
Every complete zero roster is self-conjugate under H and therefore under
the colour/weak/family-Cartan SM subgroup used in the preceding packet.
No SM complex chiral excess is obtained in these nine supplied cases.
This excludes neither a different embedding nor a different physical phase.

The unique invariant bilinear of R is skew, epsilon_weak tensor Killing8.
For m copies, a symmetric Weyl mass requires an antisymmetric flavour
matrix. Its parameter space has dimension m(m-1)/2. A single copy cannot
acquire such a quadratic mass at the symmetry-preserving origin; two
copies admit a full-rank symmetric invariant mass. The single-twist
finite roster still has exactly one R. Its at least16 protected complex
coefficients are not sixteen generations. Double twists have two copies:
a mass is gauge-allowed, not thereby generated in a supersymmetric action.

## A finite kernel is not a separated particle spectrum

The cusp gauge -1 eigenspace is rho tensor Vrho, dimension112. The bounding
spin contributes -1, so these ordinary-spin channels have periodic total
vertical holonomy and a zero Fourier mode. After the unitary radial change
the massless spin block is the free first-order derivative on a half-line.
For a translated, dilated compactly supported bump f, its Rayleigh quotient
is (integral |f'|^2/integral |f|^2)/L^2. Translates escaping to infinity
give a Weyl sequence at zero. A polynomial H1 bump suffices; smooth
approximations preserve the limit. This proves zero essential spectrum,
not an infinite-dimensional zero eigenspace and not a physical index zero.

Thus two ordinary-spin slots of a single twist carry 224 zero-angular
gauge fibre channels before the radial coordinate is counted. These are
NOT 224 normalizable four-dimensional particles. Their gauge content
includes R even though their R zero kernel vanishes. Coupling zero modes
to an arbitrarily low-energy continuum cannot be discarded in an isolated
finite effective theory without a justified decoupling mechanism.

For comparison the scalar/form zero-angular block is
[[0,-d/dt+1/2],[d/dt+1/2,0]], squared -d^2/dt^2+1/4. The double-twist
charge table removes ordinary-spin slots, but this local threshold does
not certify its entire global spectrum, interacting action, anomalies or
physical chirality. Twisting twice changes the field content and the
mass pairing at the same time; it is not a free repair of the single twist.

## Sources and remaining physical duties

Mehta--Seshadri primary PDF: https://repository.ias.ac.in/20407/1/305.pdf,
pp213--215, degree and Proposition1.12 proof. Andrews--Dorey primary source:
https://arxiv.org/abs/hep-th/0601098v2, section3 and AppendixA. This proof
applies their statements to the declared cusp operators; neither paper
derives the OA action or the full Standard Model. Local source copy and
hash custody are in INPUTS.json. The browser refetch timed out for the
first paper; the already-downloaded PDF was read, not a search snippet.

The full curved nonabelian action, bosonic Hessian, parent Yukawas, actual
end response and quantum anomaly accounting remain duties of this same
candidate. A supplied W=0 four-dimensional control cannot replace them.
Genesis has not selected these twists or a physical vacuum. The silver
boundary theory remains distinct until an actual common map is exhibited.
