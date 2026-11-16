# The four physical slots and their complete-domain transport

2026-11-16. Author hand derivation under P-C3a, scope 7b185aa30. Independent
proof review is pending. No scientific module, collection, CAS or test ran.
The exact source pins and reading scope accompany this continuation.

## 1. Fixed physical problem

Use the existing compact E8 action on the complete punctured elliptic
surface, its extending spin line, positive field metrics and full physical
mass map. Its left Weyl coefficients are lambda,a,u,v. The connection
fluctuation a is the coefficient of a (0,1) form. The pair xi=(u,v) is a
spin/flavour doublet. Keep the gauge algebra, trace and supplied unitary
symplectic flavour connection on every gauge coefficient.

Write the background spin pair as Phi=(q,r), and set

    p=(p1,p2), p1=Dbar u+i[q,a], p2=Dbar v+i[r,a],
    t=[q,v]-[r,u], J=[[0,1],[-1,0]].

The source mass map has the four rows

    M(lambda,a,xi)=(D0^dagger(a,xi),
                    2i t+sqrt(2) Dz lambda,
                    J p/Omega-sqrt(2)i[Phi^dagger,lambda]).       (1)

The final displayed entry is a two-component row. In it the dagger
conjugates each background component in the source convention. The first
row is

    D0^dagger=-(Dz a-2i Omega([q^dagger,u]+[r^dagger,v]))
                       /(sqrt(2) Omega^2).

Retain the source density metrics (Omega^2,1/2,Omega,Omega). The target
in (1) is the trace-dual conjugate Hilbert bundle specified by the mass
proof. Its form and spin transformations will be derived below.

## 2. Derive the local maps with their arguments

Let z'=f(z) be an orientation-preserving biholomorphic isometry between
the two declared surface metrics. Put d=f'(z), with d nowhere zero, and
write all following identities at corresponding points z'=f(z). Then

    Omega'=Omega/|d|, dx'dy'=|d|^2 dxdy.

Choose the actual spin lift s, with s^2=d^-1, and retain its product law.
Let V be the constant SU2 flavour intertwiner and G a smooth compact gauge
map between the actual bundles. The transformed background connection is

    A'=bar(d)^-1 (G A G^-1-i(Dbar_partial G)G^-1),
    Phi'=s V Ad_G Phi.                                      (2)

Here Dbar_partial=partial_x+i partial_y. Equation (2) includes the affine
gauge term. For connection fluctuations the derivative term subtracts out
between the two backgrounds. The source maps are therefore

    lambda'(f z)=Ad_G lambda(z),
    a'(f z)=bar(d)^-1 Ad_G a(z),
    xi'(f z)=s V Ad_G xi(z).                                (3)

These maps act on fields evaluated at f^-1 on the target surface. In
unitary internal frames set a_hat=a/Omega, xi_hat=xi/sqrt(Omega) and
eta=|d|^(1/2)s. Their phases are

    input: lambda -> Ad_G lambda,
           a_hat -> eta^-2 Ad_G a_hat,
           xi_hat -> eta V Ad_G xi_hat.                     (4)

The absolute value of eta is one. Substitution in each source kinetic
integral proves isometry. For example, the spin density obtains factors
|d|^-1 from Omega', |d|^-1 from |s|^2 and |d|^2 from the area change.
The form density has the same cancellation using |bar(d)^-1|^2. The
scalar gaugino uses Omega'^2 and the area factor.

## 3. Derive the target from every row of the operator

Covariant differentiation of (2)-(3), including the affine term, gives

    p'=s/bar(d) V Ad_G p,
    t'=d^-1 Ad_G t,
    (D0^dagger)'(a',xi')=Ad_G D0^dagger(a,xi).               (5)

For the first identity, Dbar_partial s=0 in the holomorphic spin chart.
For the second, the spin square is d^-1 and det V=1. For the last, Dz a
has factor |d|^-2. The contracted matter term Omega Phi^dagger xi has
the same factor because V is unitary. Division by Omega'^2 cancels it.

The second row of (1) has factor d^-1, since both t and Dz lambda do.
For the spin rows, use

    J V=V^-T J, V^-T=bar(V),
    |d| s/bar(d)=bar(s).

Consequently the actual trace-dual target maps are

    output: b_lambda'(f z)=Ad_G b_lambda(z),
            b_a'(f z)=d^-1 Ad_G b_a(z),
            b_xi'(f z)=bar(s) bar(V) Ad_G b_xi(z).          (6)

The conjugate-background gaugino term in (1) has exactly the last factor
in (6). Every row, including the gaugino couplings, is carried. In unitary
frames the target phases are (1,eta^2,bar(eta)bar(V)), together with Ad_G.
Their absolute values preserve the target's actual weighted metric.

Denote (3) by U_in and (6) by U_out, including their arguments. The result is

    M' U_in=U_out M                                           (7)

on compactly supported smooth fields. A holomorphic form phase and its
trace-dual phase enter (7) on opposite sides. The source's existing
isometries Uin,Uout relating M to its complex transport by the same tensor
rules. Their names in that earlier proof are separate from the present
geometric maps U_in,U_out.

## 4. The full interaction and measuring maps travel with (7)

The complete antisymmetric superpotential uses the two spin factors and
one Dbar factor. Its coordinate density gains s^2/bar(d)=|d|^-2, canceled
by the Jacobian. At a cut, its partially integrated bulk expression and
boundary primitive must be transformed together.

For the bosonic moment mu=F+Omega sum[Phi,Phi^dagger], the actual curvature
law gives mu'=|d|^-2 Ad_G mu. Each positive-potential density in the
source action gains the same |d|^-2. The derivative terms use
Omega'^-1|Dbar'Phi'|^2, the commutator term uses s^2, and the moment square
uses mu'^2/(2 Omega'^2). The measure cancels that factor in every term.
Thus finite-action field and variation classes, with their nonlinear
integrability conditions, transport together in this fixed-parameter
classical parent.

The supplied cubic is i/G_action integral kappa(a,[u,v]). Equations
(2)-(3) multiply its coefficient density by bar(d)^-1 s^2=|d|^-2.
The area Jacobian cancels this factor, and det V and gauge invariance of
kappa preserve the bracket contraction. Polarization therefore transports
the full cubic, including every companion mode. The common action scale
is held fixed throughout this comparison.

The gauge tangent maps by Ad_G on its scalar parameter and by U_in on
its field slots. Unitarity transports its Hermitian adjoint and actual
gauge-orthogonal slice. The gaugino remains a physical Weyl field.

For a parallel unbroken gauge generator T, transport it to Ad_G T at the
target. The raw kinetic current and the mode Gram then transform together.
On orthonormal mode spaces their normalized current operators are related
by U_in conjugation. The internally integrated vector normalization is
preserved by the same surface isometry and invariant trace. A weak
generator broken in this U3 background retains its massive and Goldstone
response duty.

## 5. Complete graph domains and actual adjoints

Let D_min(M) be the graph closure of the compact-support core in the
declared source and target Hilbert spaces. A proper surface isometry and
smooth bundle isometries in (3),(6) map that core onto the target core.
Equation (7) gives the exact graph-norm identity

    ||U_in x||^2+||M' U_in x||^2=||x||^2+||M x||^2.          (8)

Taking completions gives U_in D_min(M)=D_min(M'). Testing distributions
against the transported smooth core also gives the maximal-domain map.
By unitarity, (7) implies

    M'^dagger U_out=U_in M^dagger.

Thus both kernel and adjoint kernel, all conjugate-charge sectors and
their gauge representations transport. Where a block is Fredholm its
representation-valued index is preserved. Where a block has essential
spectrum at zero its continuum is transported as well.

For the doubled operator D=[[0,M^dagger],[M,0]], the unitary is
diag(U_in,U_out). This gives D' U=U D on the actual graph closures. The
complete self-adjoint realization uses the existing completeness/cutoff
hypotheses of the physical source. This transport argument preserves
those hypotheses and supplies no additional boundary parameter.

At an artificial smooth cut, Green's identity applied before and after
U transports the normal principal symbol and induced boundary measure.
Its boundary pairing agrees under the induced trace map. A specified
boundary subspace Lambda consequently maps to its actual U-boundary
image. Its rank or its physical selection remains a separate question.

If an exterior Poisson operator K(E) exists in a resolvent region, the
same uniqueness argument gives K'(E) U_boundary=U K(E). In particular its
positive norm K(E)^dagger K(E) transports with the boundary traces. This
keeps the norm carried by the energy-dependent response. The source's
quaternion centralizer continuum still needs its limiting-response
analysis at zero.

## 6. Hand rejecting controls

For z'=i z, take V=G=I and the corresponding spin lift s=exp(-i pi/4).
The input form has phase i, while the target form has phase -i. A nonzero
Dz lambda in the second row transforms by -i. Replacing U_out by U_in
there gives the opposite sign. This distinguishes the two target types
on an actual derivative row.

For z'=2z, Omega'=Omega/2, a'=a/2 and xi'=xi/sqrt(2). The area factor
is four, giving the original three kinetic integrals. Keeping a fixed
would multiply its norm by four. Keeping the raw spin norm fixed while
changing Omega also changes its kinetic integral.

For nonconstant compact gauge G, differentiation of Ad_G x creates
[Dbar_partial G G^-1,Ad_G x]. The affine term in (2) cancels exactly that
commutator. Omitting it leaves a local operator error whenever that
commutator is nonzero.

These are hand controls. Their independently reviewed scientific checks
remain a future execution package. The earlier sealed twelve-method
checker is unchanged by this continuation.

## 7. Result and remaining scope

The supplied action determines (3),(6) and the complete-domain map (8).
The companion marked-family proof constructs their geometric and spin
data for the declared family. The inner-action proof then evaluates
their actual residual on the retained half-root cohomology.

The physical parent, metric, spin/flat assignment and gauge embedding
remain the original inputs. An identification with a modular-base
operator requires its own field and domain map. These conditional
identities provide a physical transport calculation for that next test.
