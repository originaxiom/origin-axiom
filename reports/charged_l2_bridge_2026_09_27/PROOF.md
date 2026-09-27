# Complete charged harmonic modes and interior cohomology

Authored before execution, 2026-09-27. This is an analytic argument under
explicit hypotheses, not an independently reviewed theorem or a numerical
PDE solution. Finite controls verify prerequisites and identities only.

## 1. Data and domains

Let M be the fixed complete finite-volume hyperbolic M2 or M6, with its
compact core and torus cusp(s). On a tail use

    g = dr^2 + exp(-2r) h_T.

Take the previously constructed C_z=A0+z beta, z finite, t=exp(z). A0 is
the finite unitary permutation connection. The real diagonal beta is
closed, coclosed, bounded, smooth and rapidly decaying with all derivatives
on each cusp. Its construction gives beta=alpha0+d_A0 f, where alpha0
is compactly supported, closed and diagonal, and f is smooth, bounded,
diagonal and has a parallel constant limit on each cusp.

Let V be a finite-dimensional coefficient induced by E(t), including its
dual or Lambda2(E), and tensor with any unitary flat line L^q. Use the
induced positive metric and the complete L2 domain, NOT an imposed boundary
condition at a finite cutoff. Let D be its flat exterior derivative.
In the A0 plus line frame, D differs from a unitary de Rham differential
by the bounded zero-order term z rho(beta) wedge. Thus Q=D+D^dagger is
a self-adjoint bounded perturbation of the complete unitary de Rham
operator. Smooth cutoffs with uniformly bounded gradient tending to zero
show the minimal and maximal differential domains agree. No singular end
extension or source domain is chosen.

Define H^k_(2)(D) here to mean the HARMONIC kernel

    {u in L2: Du=0, D^dagger u=0 distributionally}.

Elliptic regularity makes its elements smooth. The nonnegative quadratic
form ||Du||^2+||D^dagger u||^2 defines the same Laplacian kernel. A gap
in its degree-one spectrum is NOT assumed.

## 2. The bounded change of frame, with its metric

Since diagonal elements commute, on an end G=exp(z rho(f)) satisfies

    D = G^-1 D_u G,

where D_u is the unitary A0-plus-line differential. Both G and G^-1 are
uniformly bounded for each fixed finite z. If tilde u=G u, the correct
transformed metric is h'=(G^-1)^dagger h G^-1. This metric is uniformly
equivalent to the unitary reference metric in EVERY form degree. An
infinite-order unitary line does not require a finite trivializing cover;
unitary torus Hodge theory applies directly.

In fact f is bounded on all of M and diagonal, so the same global frame
change conjugates D to D_A0,L+z rho(alpha0). That differential is an
exactly unitary connection outside a compact set, though its transformed
metric need not be the unitary metric. This does NOT conjugate away
alpha0 or its nontrivial global holonomy. It is a chain/norm comparison,
not an allowed compact physical gauge transformation.

## 3. The zero-form Green operator, including the H0 kernel

For a unitary coefficient and a compactly supported zero-form v in an
open cusp tail, putting w=exp(-r)v gives the fiberwise Hardy identity

    integral |partial_r v|^2 exp(-2r)
      = integral (|partial_r w|^2+|w|^2)
      >= integral |v|^2 exp(-2r).

Tangential terms are nonnegative. Uniform norm equivalence and section 2
therefore give ||u|| <= C ||Du|| for zero-forms supported sufficiently far
out, with some finite C depending on the fixed coefficient and z. This
does not assert a global lower bound of one or any uniformity as z escapes.

Every global flat section is bounded on each cusp in this frame and hence
L2; conversely a zero-form harmonic section is flat. Thus ker Delta0 is
exactly ordinary H0(M;V), finite-dimensional. There is a positive global
gap on its orthogonal complement. Here are the compactness details:
if not, take normalized u_j orthogonal to this kernel with Du_j -> 0.
Interior elliptic estimates and Rellich give local L2 convergence along a
subsequence to a flat section u. A weak global L2 subsequence has the same
local limit; hence u is L2 and still orthogonal to the kernel, so u=0.
Apply the exterior estimate to chi u_j, where chi is one on a deeper tail
and zero on the core. D(chi u_j)=chi Du_j+d chi u_j tends to zero because
the transition collar is fixed and compact. Both core and tail norms tend
to zero, a contradiction. This proves boundedness of the reduced inverse
G0 on (ker Delta0)^perp. It proves closed range of d0, not of d1.

For a smooth compactly supported closed one-form alpha0, D^dagger alpha0
is orthogonal to every flat zero-form. Set

    f0 = -G0 D^dagger alpha0,
    u = alpha0 + D f0.

Then f0 and Df0 are L2, u is closed and coclosed, and elliptic regularity
makes both smooth. Its ordinary class is [alpha0]. This constructs a
harmonic representative for each interior class: on a compact core the
interior image im(H1_c -> H1) equals ker(H1(M) -> H1(boundary)), and a class
in this kernel admits a compactly supported closed representative.

## 4. An L2 closed one-form has zero boundary class

On an end transform by G and write tilde u=a(r)dr+b(r), with b tangential.
Flatness and D_u tilde u=0 imply

    d_T b=0,   partial_r b=d_T a.

Project b to the harmonic one-forms of the compact unitary torus. The
projected vector p is constant in r because projection kills d_T a.
For a tangential one-form the inverse metric exp(2r) exactly cancels the
volume exp(-2r). Consequently

    ||tilde u||^2 >= integral_R^infinity ||p||^2_T dr.

Norm equivalence ensures the left side is finite, so p=0. Thus the torus
cohomology class vanishes on every end. The ordinary class of every L2
harmonic one-form belongs to H1_interior. This argument explicitly handles
invariant torus channels; it does not assert peripheral acyclicity.

## 5. No ordinary-exact L2 harmonic mode is missed

Suppose u=Dv is smooth, L2 and ordinary-exact, initially with no assumed
integrability of the smooth primitive v. Set tilde v=Gv on a cusp and
w=exp(-r) tilde v, in the Hilbert space of unitary torus L2 sections.
Since the radial derivative of tilde v is the radial component of Gu,

    g(r)=exp(-r) partial_r tilde v(r) is in L2(dr),
    w'+w=g.

For any fixed smooth collar slice R, variation of constants gives

    w(r)=exp(-(r-R)) w(R)
          + integral_R^r exp(-(r-s)) g(s) ds,
    ||w||_L2 <= ||w(R)||/sqrt(2) + ||g||_L2.

The last estimate is the Hilbert-valued Young inequality with L1 norm one
for the one-sided exponential kernel. It needs no limit of v at infinity.
The compact slice term is finite. Thus tilde v, and therefore v, is L2
on every cusp; smoothness handles the core. Since Dv=u is L2, complete
cutoffs place v in Dom(D0). If u is also coclosed,

    ||u||^2 = <u,Dv> = <D^dagger u,v> = 0.

This is the missing injectivity statement. It does not use a gap in degree
one or a bounded inverse for that Laplacian.

Combining sections 3--5, the ordinary-class map is an isomorphism

    H^1_(2)(M;D)  -->  im[H1_c(M;V) -> H1(M;V)].             (A)

It is finite-dimensional. A normalizable eigenkernel at a zero essential
threshold is allowed; finite dimension is not spectral isolation. This is
a standard-mechanism application, not a new general Hodge-theory discovery.

## 6. Actual duals, H0/H3 and the physical grading

The Hermitian Riesz map followed by the oriented Hodge star is an
antiunitary map between V-valued k-forms and V*-valued (3-k)-forms. The
coefficient on the right is the actual contragredient flat bundle, with
its induced dual metric. Integration by parts with the flat evaluation
pairing intertwines D with the dual formal adjoint, up to degree signs.
Complete cutoffs extend the identity to the kernel domains. Thus

    dim H^2_(2)(V)=dim H^1_(2)(V*),
    dim H^3_(2)(V)=dim H^0_(2)(V*)=a0(V*).                 (B)

Conjugating matrix entries alone is not the dual away from a unitary
point. The producer checks this distinction on actual t=2 coefficients.

There is a further equality for THIS harmonic background and unitary L.
Write D=d_A+Psi with A unitary and Psi Hermitian in the coefficient. The
moment equation is d_A^dagger Psi=0, including after the representation
and unitary line twist. On zero-forms, the cross derivatives cancel:

    Delta_D,0 = d_A^dagger d_A + sum_i Psi_i^2
                        + (d_A^dagger Psi).

No commutativity between Psi_i and a test vector or connection matrix is
assumed here. A flat L2 zero-form therefore satisfies d_A v=0 and Psi v=0.
Justification on the complete space uses the bounded Psi, complete cutoffs
and the same quadratic-form identity; Dv=0 already implies d_Av is L2.
Hermitian dualization maps these simultaneous kernels to those of V*.
Consequently a0(V)=a0(V*). This is NOT assumed for arbitrary nonunitary or
nonsplit flat coefficients. It is earned by this positive harmonic model.

If n(V) denotes the already-computed ordinary interior dimension, equations
(A),(B) give the harmonic-degree census

    (b0,b1,b2,b3) = (a0(V), n(V), n(V*), a0(V*)).          (C)

In the supplied twisted gauge action, the internal fermion mass-squared
operator on the one-form component is 2 Delta_D,1; opposite four-dimensional
chirality has the degree-two component of this same complex. Degrees three
and zero give the other fermionic components. These LOCAL differential
and positive-norm identities are the ones read in Braun et al., equations
2.34--2.49. The paper's compact Hodge assertion is not the noncompact proof;
sections 1--5 above supply the separate complete-domain argument.

Choose left-minus-right convention. The net harmonic fermion multiplicity
is (b1+b3)-(b0+b2)=n(V)-n(V*) because the H0 terms cancel. The overall sign
can reverse with chirality convention, without changing a zero result.
At enhanced gauge symmetry H0 modes must be organized into the actual gauge
multiplets; do not label them extra generations. Their presence has not
been erased from (C).

If essential spectrum contains zero this finite kernel difference is NOT
a Fredholm index, and no protection under arbitrary perturbations follows.
Nor does the kernel calculation establish a separated four-dimensional
effective theory. It identifies normalizable linear zero modes of the
declared higher-dimensional action, not physical particles in our universe.

## 7. What the existing all-parameter certificate now implies

For the two literal E(t) families with no hypercharge line, the earlier
all-t exact certificate gives on M6

    t=1: n(E)=n(E*)=1;
    t=-1,i,-i: n(E)=n(E*)=2;
    all other nonzero t: n(E)=n(E*)=0.

These now identify degree-one/two L2 charged kernels in this same supplied
background. They are vector-like, not three generations. The t=1 point
also has a0(E)=a0(E*)=1. Its complete gauge enhancement remains a separate
full-parent question. No fiber dimension was interpreted as a mode count.

For an honest common unitary line L in all Standard Model sectors, the
already-complete common-line result says:

* L(mu)!=1: the required Q coefficient E L has zero ordinary interior
  difference (acyclic torus in this coefficient, not in the whole parent).
* L(mu)=1: the required u coefficient E L^-4 has zero ordinary interior
  difference for every t and every such line; all 320 meridian-trivial
  characters were included by the previous exact reduction.

By (A)--(C), this failure of a simultaneous net-three target now holds
also for the normalizable linear fermion zero modes of this declared
smooth source-free harmonic model. We do NOT claim that all five sector
indices have been classified, nor that all SL5 representations, nonliftable
quotients, singular-source domains, end laws, interacting mirror-removal
mechanisms or physical completions fail. The old nonsplit ordinary positives
remain mathematical results with different admissibility duties.

## 8. Next obligations and sources

Compute the full-parent unbroken gauge algebra, including special parameters
and line twists, before a complete multiplet interpretation. Calculate actual
normalized couplings and determine what reduction, if any, is controlled in
the presence of the known gapless neutral sector. Any new chirality mechanism
must carry its own source/domain/action/metric assumptions. Deriving this
parent and spacetime from the framework, quantum consistency, gravity and
observational tests remain open. This is not a TOE or a guaranteed route to one.

Primary action source: Braun, Cizel, Huebner, Schaefer-Nameki,
[Higgs Bundles for M-theory on G2-Manifolds](https://arxiv.org/html/1812.06072v2),
sections 2.3--2.4 read personally and sectionally on 2026-09-27. No full-paper
reading or independent specialist acceptance is claimed in this package.
The metric/action/domain are supplied inputs. The complete analytic
comparison is authored here and may require specialist correction.
