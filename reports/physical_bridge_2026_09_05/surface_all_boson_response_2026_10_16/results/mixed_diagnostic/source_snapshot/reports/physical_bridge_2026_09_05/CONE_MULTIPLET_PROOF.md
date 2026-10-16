# Neutral multiplet traces and the physical end datum

October 1, 2026. R70 authored argument, frozen before execution.
Conditional on R66's supplied connection, cone metric and twisted action.
The proof is not independently reviewed by finite matrix controls.

## 1. A first-order period cannot be canceled by complementary matrices

Reuse N,P,H,Z from R66, tr(Z^2)=12, [Z,C_i]=0 at every r>0.
Let M_gamma be a based peripheral monodromy and U(s) its transport.
For any smooth matrix one-form variation eta along a period-one loop,
the convention M=exp(C_i) gives

    M_gamma^-1 delta M_gamma = integral U(s)^-1 eta_s U(s) ds,
    tr(Z M_gamma^-1 delta M_gamma) = integral tr(Z eta_s) ds. (1)

The second identity uses [Z,U(s)]=0; no flatness of eta is assumed.
A sign-reversed transport convention reverses both sides and has the
same zero condition. A similarity tangent delta M=[X,M] has zero left
side because M commutes with Z. A periodic infinitesimal gauge change
eta=d_C xi gives a total derivative on the right. Thus fixed peripheral
conjugacy forces each such loop's Z period to vanish. Off-Z matrix
variations have zero right side and cannot compensate at FIRST ORDER.
This does not prove a finite nonlinear orbit classification.

To infer the torus-averaged harmonic trace, impose the loop condition
for the parallel family of each peripheral loop and average it, or
restrict to linearized flat variations (then the projected form is
closed and its periods are independent of the parallel basepoint).
Fixing just TWO based loops for a general nonflat variation is weaker:
Z(1-cos(2pi y))dx vanishes along those loops based at (0,0), but has a
nonzero torus average. It is not a finite-graph apex comparator; its
nonzero angular derivative has divergent cone norm. This distinction
prevents a topological loop convention becoming an analytic domain law.

Apply the averaged condition at each regulator, or impose the limiting
version of these two averaged linearized periods as an apex boundary
law. The latter requires the H1 neutral trace; it is not deduced from a vague assertion
that the limiting unipotent matrix is identity. The weight Z and the
simultaneous peripheral trivialization are transported together. This
is a tangent annihilator, not a new global observable under arbitrary
changes of the full representation.

For eta=Z(v_x dx+v_y dy), (1) equals 12 v_x and 12 v_y.
Hence the fixed-period apex law is v(0)=0. In R67's X0 the same zero
trace follows directly from the exact neutral graph's H1 closure.
Compact gauge transformations cannot remove a nonzero neutral period.

## 2. The necessary superfield map makes the mismatch precise

In the ADOPTED twisted SYM model, Braun et al. eq. 2.14 and B.5 relate
the complex boson C=phi+iW to the one-form fermion by a nonzero
constant multiple of epsilon psi; the conjugate supercharge does the
same for C dagger and psi-bar. Eq. 2.43 and A.13--A.17 supply the
Hodge/conjugation packaging. These are model inputs, not genesis laws.
https://arxiv.org/abs/1812.06072v2

On R68's exactly reducing Z-valued harmonic one-form block, write the
normalized fermion trace as (a,b) in C^2 direct-sum C^2; b represents
the Hodge-dual conjugate one-form. Put Hlink=diag(alpha,1/alpha),
S=-Omega Hlink. The two scalar-profile projections are a and S^-1 b,
up to irrelevant nonzero signs/phases. Both scalar traces zero thus
requires a=b=0. The stacked map has rank four. Equivalently, imposing
a=0 together with R68's reality C(a,b)=(S conjugate b,-S conjugate a)
also forces b=0. The Weyl spinor factor does not change this constraint.

But the neutral Q0=Gamma partial_r has the nondegenerate Green form

    G=[[0,Hlink],[-Hlink,0]].

A zero trace subspace is not maximal current-isotropic. More directly,
cutoff constant neutral forms near the apex belong to the adjoint
domain of any bulk domain whose entire neutral trace is zero, but not
to that domain. Their support avoids the core and the other endpoint.
The exact orthogonal reduction makes their Green pairing with all
complementary coefficients zero. Coupling only the complementary
bulk boundary channels cannot repair this specific missing trace.

Therefore X0 (or the specified fixed-period apex law) cannot be combined
with a bulk-only self-adjoint fermion preserving BOTH conjugate
superfield profile maps at this end. This is a necessary local test,
not a theorem excluding physics, chirality or supersymmetry breaking.
Adding end Hilbert degrees of freedom, changing the bosonic end law,
changing metric/action, or preserving a smaller symmetry changes the
hypotheses and requires its own analysis. A relative domain a=0,b free
is maximal current-isotropic and self-adjoint in this block; it fails
the same-sector combined reality and the other scalar-profile map.
That countercontrol prevents equating self-adjointness with full 4d N=1.

## 3. A finite-action positive outside the sufficient L4 class

Take any v=(v_x,v_y) in H1((0,R);C^2), with the outer data treated
explicitly, and a_v=Z(v_x dx+v_y dy). Exact commutation with C and C
dagger gives

    F_(C+a_v)=Z dr wedge (v_x' dx+v_y' dy),
    I_(C+a_v)=0,                                        (2)
    r^2 |a_v|^2=12 v dagger Hlink v,
    r^2 |F_(C+a_v)|^2=12 v' dagger Hlink v'.             (3)

Both norms are integrable. The actual residual-square potential is
24/g7^2 times integral v' dagger Hlink v' dr in this normalization.
Self-brackets vanish, so an L4 requirement on a_v is unnecessary.
A constant nonzero v has zero residuals but changes holonomy; a smooth
cutoff equal to that value near zero has finite action and a nonzero
trace. Its L4 density is 144(v dagger Hlink v)^2/r^2 and diverges.
This is not an admitted fluctuation under the FIXED-period law of §1.

The construction can include nonzero matrix products without asserting
a full physical end theory. Let b belong to R67's X0 and additionally
b/r in L2 (norms in the same cone metric). H1 on the finite interval
bounds ||v||_infinity. Every cross bracket with a_v or a_v dagger obeys

    ||[a_v,b]||_2 <= const ||v||_infinity ||b/r||_2.     (4)

The same estimate holds for the moment quadratic terms. Self-products
of b are L2 by its L4 norm. Linear terms are in L2 by the actual d_C and
adjoint graph norms. Thus V(C+a_v+b) is a finite nonnegative C1
polynomial in the declared pair norm H1(v)+X0(b)+||b/r||_2, and C is
stationary at zero residual. The pair parametrization may be redundant;
it is a sufficient class, not a counted input/vacuum space. Compactly
supported b and compact gauge changes give nonzero interior controls.
No automatic admission of every maximal charged fermion/boson channel
is asserted; the extra weighted norm is a declared restriction.

## 4. A line passes necessary matching but leaves a genuine end duty

Allowing neutral bosonic apex trace in a chosen complex line W, its
conjugate lies in conjugate W. Hodge packaging gives S conjugate W =
W-perpendicular (Hermitian Hlink). The fermion trace then lies in
L_W=W direct-sum W-perpendicular, exactly R68's self-adjoint/reality
domain. These necessary algebraic tests pass for every complex line.
They do not prove full nonlinear/gauge/superfield derivative closure.

For the isolated neutral boson the closed energy form is integral
v' dagger Hlink v' dr with v(0) in W. Variation gives the additional
natural condition v'(0) in W-perpendicular for its second-order
realization, with independently declared outer data. This is also the
degree-one square of the R68 block Q. Equality of this restricted square
does not prove the whole physical action's supersymmetry or spectrum.

The holomorphic action is a separate requirement. At the boundary,
C_x=tN+v_x Z, C_y=kZ+beta t^2 P+v_y Z. R60's one-form becomes

    theta=-tr(C wedge delta C)
          =12[(k+v_y) delta v_x-v_x delta v_y].          (5)

On v=z w with W=span(w), its quadratic part vanishes, but
theta=12k w_x delta z. A longitude-only line w_x=0 passes with no
neutral counterterm; the helicity lines of R68 do not when k!=0.
A specified local linear term -12k v_x cancels (5) on any such line.
Its coefficient is the supplied background k and it is an ADDED end
functional. No globally gauge-invariant/supersymmetric completion or
principle selection is proved. No counterterm is needed if the actual
allowed variations instead set delta v_x=0; that too is a boundary law.

The lesson is not that one sector is dead. It is that a bosonic domain,
a first-order fermion domain, peripheral conjugacy and the holomorphic
boundary variation are separate parts of ONE admission problem. A
consistent end law must resolve them explicitly before an index is read
as chiral matter. Full charged-channel closure, global core matching,
same-parent physical realization, quantum consistency and derivation of
the action/metric/end data remain mission duties.
