# Same-action real gauge fixing and relative one-loop weights

October 27, 2026. UNREVIEWED authored conditional derivation. No science
execution, numerical determinant, measured-coupling comparison or independent
certificate. Fixed supplied curved action, parallel stationary SM gauge phase,
spin/metric and complete graph law throughout. This is a parity-even one-loop
Gaussian construction; it does not settle the determinant phase, anomalies,
UV completion, supersymmetry breaking or vacuum selection.

## 1. Recover the action rather than infer physics from a cochain

Use weave_curved_action_2026_10_08/PROOF, weave_physical_mass/PROOF and
weave_sm_parallel/PROOF with their actual weighted kinetic metrics. The
background has W'=0 and mu=0. The normalized chiral tangent is the COMPLETE
connection/spin space H_c for (a,u,v), and the gauge-parameter/gaugino space
H_v has the source's gauge kinetic metric. Denote its compact real structure
by C_v; the physical vector takes values in the real part, not an arbitrary
complex gauge quotient.

Let k:H_v->H_c be the infinitesimal physical gauge action normalized with
these metrics. The source's gaugino coupling fixes

  d=sqrt(2) k = D0,
  d epsilon=sqrt(2)(Dbar epsilon,-i[q,epsilon],-i[r,epsilon]). (1)

Let H:H_c->overline(H_c) be the kinetic-normalized W Hessian. The bar
denotes the actual Hermitian-dual/conjugate target, not a second independent
left field. Its bilinear transpose is symmetric. Gauge invariance of W,
differentiated at W'=0 on compactly supported fields, gives

  H d=0.                                                   (2)

This uses the actual affine derivative in k and the retained W surface
primitive; the complete-domain cutoff argument eliminates its surface
error. It is not an identity at an arbitrary off-shell background.

Earlier silver_bosonic_quotient/PROOF already distinguishes real gauge
from moment directions on a DIFFERENT compact boundary problem. That
distinction is reused; neither its inverse nor its boundary conditions
are transferred to this complete surface. The present gauge fixing is
derived directly from (1) and the actual curved action.

## 2. The moment and gauge-fixing squares determine one scalar operator

In canonical fields the scalar kinetic term is

  ||D_mu x-k v_mu||^2, x in H_c, v_mu in H_v,real.           (3)

The source's Kahler metric and its moment map give the normalized
linear moment response m(x)=+/-2 Im(k dagger x); the sign depends on
the already-declared moment convention and drops from its square.
Here Re and Im use C_v and the adjoints use the actual weighted metrics.
Equivariance of the moment map implies

  2 Im<k epsilon,k eta>=0, at mu=0,                         (4)

for real compact gauge parameters: the symplectic pairing is a moment
paired with their Lie bracket, hence zero at this D-flat background. Thus

  P_v=d dagger d=2 k dagger k                               (5)

preserves the compact real structure. Taking Re in its action on a real
parameter does not discard an imaginary mass term. Identity (4) includes
the covariant-derivative part of k and its complete-domain integration
by parts. A nonzero background moment would change this argument.

Define the real Goldstone functional g(x)=2 Re(k dagger x). The mixed
term in (3) is -<v_mu,D_mu g(x)>, or +<D_mu v_mu,g(x)> after the
declared external integration by parts. Add the background Feynman
gauge term

  (1/2)||F||^2, F=D_mu v_mu-g(x).                          (6)

Its cross term cancels that mixing exactly. On a real gauge parameter,
delta v_mu=D_mu epsilon and delta x=k epsilon, so

  delta F=(D_mu D_mu-P_v)epsilon.

The Faddeev-Popov operator, with the harmless overall sign removed, is

  O_gh=-D_mu D_mu+P_v.                                    (7)

The moment energy plus the Goldstone gauge-fixing energy is

  (1/2)||m(x)||^2+(1/2)||g(x)||^2
       =2||k dagger x||^2=||d dagger x||^2.                (8)

At W'=0 the F-potential Hessian is ||H x||^2. Consequently the full
gauge-fixed internal complex-scalar quadratic form is

  Q_c(x)=||H x||^2+||d dagger x||^2,
  P_c=H dagger H+d d dagger.                              (9)

It includes the Goldstone scalar; it is not the Hessian after quotienting
by every complex primitive. The bosonic vector and complex Grassmann FP
pair use P_v. In flat external spacetime their quadratic operators are

  O_vec,mu nu=(-D_4^2+P_v)delta_mu nu-2 F_mu nu,
  O_c=-D_4^2+P_c, O_gh=-D_4^2+P_v,                        (10)

where F_mu nu acts in the actual gauge representation, with anti-Hermitian
connection convention. Its gyromagnetic coefficient is the Yang-Mills
quadratic coefficient, not an adjustable field charge. The auxiliary
Gaussians have field-independent kinetic metrics in this construction;
their determinants carry no external F^2 insertion.

## 3. The fermion square fixes the same internal operators and domains

In kinetic-orthonormal frames the actual symmetric left-Weyl mass
bilinear has the block form

  M=[[0,d dagger],[bar d,H]].                              (11)

The bar includes the genuine compact/dual structures. Transposes below
are formal bilinear transposes INCLUDING derivative integration by parts.
From H^T=H and Hd=0 one gets d^T H=0 and H dagger bar d=0. Therefore

  M dagger M=diag(overline(d dagger d),P_c)
            =diag(P_v,P_c),                               (12)

where the last equality uses the realness (4) in the gauge sector.
The compact real structure can exchange a representation with its
conjugate; this is not an assertion that a fixed charged block has
entrywise real coefficients or permission to discard its partner.
This exhibits the map, rather than matching scalar/fermion dimensions.
It also checks the factor sqrt(2) in (1): changing that factor without
the source moment/kinetic coefficients breaks (8)-(12).

Use the closures of these nonnegative forms on compactly supported
smooth fields. On that core (12) is an equality of quadratic forms;
the mass graph norm is the orthogonal sum of the two displayed form
norms. Its completion therefore gives those SAME P_v,P_c realizations
as reducing sectors of M dagger M, with no separately assigned end
condition. P_v is also the complete-form ghost mass operator in (7).
The complete-surface gauge fixing adds no wall at a finite cusp circle.

The previous ACTUAL_FERMION_RELATIVE_HEAT_EXISTENCE proof concerns the
doubled D^2, containing M dagger M and M M dagger. Compress its relative
heat operator by the fixed left-sector projection and then by the
gauge/chiral projections of (12). Hence each

  r_v(q;s)=Tr(exp(-sP_v,q)-exp(-sP_v,0)),
  r_c(q;s)=Tr(exp(-sP_c,q)-exp(-sP_c,0))                   (13)

is trace class, all-orders small as s->0, and approaches its actual
kernel difference exponentially as s->infinity. The same compact-to-tail
kernel estimates apply to these reducing sectors. A finite direct-sum
compression does not introduce a new continuum estimate.

Do NOT use the trace of the entire doubled D^2 as one Weyl trace: that
would count the dual block again. Equation (12) is the left roster used
below. Both conjugate gauge representations in that roster are retained;
no additional conjugacy factor is inserted after their indices are summed.

## 4. Derive the four-dimensional weights

Write the flat-space heat coefficient as
tr[(1/2)E^2+(1/12)Omega_mu nu Omega_mu nu], with the integrated
derivative discarded only under the declared external falloff. The
endomorphisms are E=0 for scalars/ghosts, E=(1/2)gamma_mu nu Omega_mu nu
for spinors, and E_mu nu=2 Omega_mu nu for vectors. Gamma tracing gives
Dirac coefficient -2/3; vector tracing gives -5/3. Include the Gaussian
log-determinant weights:

| Field | Heat coefficient | log-det weight | Product |
|---|---:|---:|---:|
| Complex scalar | 1/12 | 1 | 1/12 |
| Weyl fermion | -2/3 (Dirac trace) | -1/4 | 1/6 |
| Real vector | -5/3 | 1/2 | -5/6 |
| Complex FP pair | 1/12 | -1 | -1/12 |

Thus scalar+Weyl gives 1/4 on P_c; vector+FP+gaugino gives -3/4
on P_v. Normalizing to one chiral index gives the FIXED weights +1,-3.
Primary comparisons personally checked: Vassilevich hep-th/0306138,
(3.26)-(3.28), (3.42)-(3.53), (4.25)-(4.34);
https://arxiv.org/pdf/hep-th/0306138. Martin--Vaughn (2.1)-(2.3)
independently recovers beta_g=g^3[S(R)-3C(G)]/(16 pi^2):
https://arxiv.org/pdf/hep-ph/9311340. No full-paper reading claimed.

## 5. A same-action relative F^2 kernel and its light matching

The external unbroken SM connection is internally parallel and commutes
with the structure background and Y Wilson field. Its generators commute
with d,H and their domains. The four-dimensional heat calculation
therefore factors from (13). For either normalized gauge difference,
use the charge coefficients c_R,q ALREADY derived in
WILSON_CHARGE_RESOLVED_RELATIVE_THRESHOLD_MAP.md and form

  B_ab(s)=sum_(R,q) c_R,q [r_c(R,q;s)-3 r_v(R,q;s)].        (14)

The internal function differs by representation and sector; +1,-3 are
not permission to replace it by a common scalar eta determinant. The
coefficients sum to zero within each complete SU5 representation, so
the common q=0 reference cancels before any infinite trace is taken.
All quantities in (14) are finite relative traces on the SAME action,
metric, stationary background and complete domain.

Define

  h_ab=sum c_R,q [dim ker P_c,R,q-3 dim ker P_v,R,q].       (15)

The zero-Wilson reference kernels cancel as well. P_c zero modes satisfy
H x=0 and d dagger x=0 and are massless chiral profiles. P_v zero modes
have d epsilon=0 and generate massless vector multiplets. Thus (15) is
the normalized one-loop light beta-coefficient difference in THIS N=1
model, not a chiral-generation index. It is not obtained from the end
threshold histogram or from net kernel-minus-cokernel data alone.

Equation (13) makes the following integral convergent for mu>0:

  I_ab(mu)=-integral_0^infinity
       [B_ab(s)-h_ab(1-exp(-mu^2 s))] ds/s.                (16)

In this explicitly declared proper-time matching prescription the
one-loop parity-even kinetic correction is

  Delta(alpha_a^-1-alpha_b^-1)=-I_ab(mu)/(4 pi).           (17)

The sign follows from log det=-integral heat/s, anti-Hermitian
Omega_mu nu=-i F_mu nu, and the classical density F_a^2/(4g_a^2).
As an independent sign control a heavy multiplet of index b gives
alpha_low^-1-alpha_high^-1=-b log(M^2/mu^2)/(4 pi), matching
d alpha^-1/d log(mu)=-b/(2 pi).

The preceding scale lemma now has physical weights, not a raw fermion
count:

  d I_ab/d log(mu^2)=h_ab,
  d Delta_ab/d log(mu)=-h_ab/(2 pi).                       (18)

The resulting logarithm agrees with the retained light model's running.
A different admissible matching switch shifts the finite term by a
fixed constant times h_ab; its convention must be shared with the light
EFT. When h_ab=0 that switch and common internal-scale dependence cancel.
No independent correction may be fitted to each gauge factor.

These are the leading external F^2 coefficients with external momentum
taken below the retained heavy gaps. Higher derivative operators and
light nonlocal amplitudes are separate. The definition fixes a Feynman
background gauge and a matching scheme; it is not a proof that arbitrary
off-shell gauges yield identical finite effective actions. No claim of
a UV-complete six-dimensional quantum parent follows from this Gaussian
relative calculation. Its gauge-covariant local F^2 terms are universal
in the parent SU5 normalization as already proved.

## 6. Recover the actual massless VECTOR kernel

One part of (15) can already be determined, rather than left as an
unspecified future count. If P_v epsilon=0, its nonnegative form gives
d epsilon=0. Realness (4) allows real and imaginary compact-real parts
of epsilon to be treated separately. Elliptic regularity makes them
smooth. For a Hermitian part, Dbar_A epsilon=0 and its actual dagger
give both covariant real derivatives zero. Also [q,epsilon]=0 implies
[q dagger,epsilon]=0. Thus a zero mode is a parallel compact gauge
generator commuting with the FULL principal triple, not just H.

The recovered parallel-phase proof exhibits its commutant as su5_g.
Parallel transport with the actual Wilson character then retains its
centralizer s(u3+u2). Conversely these generators are parallel, annihilated
by d, and have finite norm because area(Sigma)=2 pi; the complete graph
cutoffs admit them. Therefore

  ker P_v=(su3+su2+u1)_C                                  (19)

for the source's noncentral 3+2 holonomy. There are no additional massive
structure-sector gauge zero modes. This is an operator-kernel argument,
not an inference from a matching dimension. A central holonomy restores
the full su5 kernel and is a separate recovery control.

With the already-fixed SU5 normalization, these massless vector
multiplets have

  (b1,b2,b3)_vector=(0,-6,-9),
  (h21,h31)_vector=(-6,-9).                               (20)

The chiral contribution remains the ACTUAL ker P_c; it is not fixed
by (19), the vanishing charged index or the fermion end histogram.
Internally constant gauge-profile modes are not deleted as gauge-volume
zeros: their four-dimensional vector fields contribute to (20). A
global zero-momentum FP gauge-volume factor is treated separately from
the physical light multiplet's running.

## 7. Controls, remaining freedom and next work

* At central Wilson holonomy B_ab(s)=0 within every complete SU5 factor
  for each fixed s. The heavy matching integral need not be continuous
  through an additional light zero crossing: the EFT field content then
  changes. Do not demand a false uniform infrared limit.
* Removing the ghost changes -3 to -8/3. Treating the gaugino as a ghost
  or tracing both doubled fermion blocks also fails the spin table.
* A finite massive-vector super-Higgs control has an eaten chiral with
  the same mass; +1-3=-2 per real gauge-index roster. This is a finite
  control, NOT permission to equate arbitrary infinite traces after a
  q-dependent nonlocal polar decomposition of d.
* The earlier cochain 1:2:1 trace cancellation is not (14). Its valid
  algebra is preserved; it does not include the external spin weights.

The bosonic/ghost quadratic operators and relative one-loop weights
are now derived at author-proof level from this SAME action and graph
law. Brignole hep-th/0001121, (17)-(20), was also personally checked
as a finite-dimensional vector-metric/mass comparison; its Landau-gauge
Kahler-potential determinant is not used as our F^2 or cusp theorem.
Source: https://arxiv.org/pdf/hep-th/0001121. No full-paper reading claimed.

Still to do for a numerical prediction in this model: independent review
of the operator and measure argument; actual light CHIRAL multiplicities;
global spectral evaluation of (14), including the compact core; and a
source-complete admitted numerical design if a numerical route is used.
No Wilson character, metric shape, physical mass scale, vacuum or state
distribution has been selected by (14)-(18). Absolute common coupling,
genesis-to-action derivation, supersymmetry breaking, anomaly/phase
completion, three chiral generations and gravity remain distinct duties.
The recovered phase's zero complex charged index keeps its original
scope. No old failed result or seal is changed by this successor.
