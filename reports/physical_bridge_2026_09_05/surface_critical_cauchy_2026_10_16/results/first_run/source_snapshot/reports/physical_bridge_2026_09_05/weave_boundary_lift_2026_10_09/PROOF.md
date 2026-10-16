# Angular admission distinguishes two boundary prescriptions

Conditional analysis of the supplied curved E8 parent, at a finite
cusp cut with all angular sectors restored. The finite cut and the
contrasting boundary pairing are additional inputs, not genesis outputs.

## The actual principal map

In the physical order (lambda,a,u,v), kinetic normalization at an
orthonormal point is H=diag(1,1/sqrt(2),1,1). Let P act on target rows
as(row1,-row0,-row3,row2). The previous physical mass formula gives

    P H M H^-1 = partial_x + J partial_y + lower order,
    J=diag(-i,-i,i,i).

At an outward y-normal collar point, identify the target with the source
by J dagger. Set R=diag(1,1,-1,-1), K=J dagger=i R. Then the normal
principal mass is partial_t+K partial_theta. Positive metric factors
are absorbed into the real angular covector; at cusp height t its
physical value is exp(t) times the coordinate momentum.

This is a unitary identification of the target, not deletion of slots.
On the full charge-q Dirac packaging, the original block expression is
[[M,Dminus],[Dplus,Mdagger]]. Simultaneously changing target and right
frames gives [[Mnormal,Dminus],[Dplus,Mnormaldagger]]; the external
kinetic matrices are unchanged. Gamma5=+ on the source. Thus

    Dprincipal=gamma5 partial_t+Dslash4+K partial_theta,
    H(p,r)=gamma5 Dslash4(p)-gamma5 R r,
    Hdagger=H, H^2=(abs(p)^2+r^2)I.

The adjoint problem has radial tangential symbol
Hadj(p,r)=gamma5 Dslash4(p)+gamma5 R r. This extra angular term COMMUTES
with gamma5; omitting it was legitimate only in the old normal theory.
The full symbol remains elliptic. Normal mass and connection terms
are lower order at this finite boundary and cannot repair a failed
principal complementing condition.

## A charged extreme prevents the unchanged local lift

Use the actual principal-spin j=0 block, present at charge Z=5 and
its conjugate. Its scalar/form fields lambda,a are periodic at the
cusp; its u,v spin fields are antiperiodic. Put k=nq and y=exp(t).
The physical kinetic normalization in dxdt is

    lambda=sqrt(y) f_lambda, a=sqrt(2/y) f_a, u=f_u, v=f_v.

The canonical target derivatives in the first two slots are
sqrt(y) Dz(sqrt(y) f_lambda) and
y^(3/2) Dz(y^-1/2 f_a). Here Dz=partial_x-i partial_y+i k/y.
After the normal target phase i, their masses are

    mu_lambda=1/2-k, mu_a=-1/2-k.

These are precisely the two j=0 extreme masses of the previous coupled
calculation. At zero flux the balanced reference therefore admits
gamma5=+ on lambda and gamma5=- on a. Both slots have R=+1.

Take p=0, r>0 and any nonzero positive-chirality lambda spinor v.
Its principal radial Hamiltonian eigenvalue is -r. Therefore
Psi(t)=exp(r(t-T))v solves (partial_t+H)Psi=0 and decays inward for
t<T. The reference admits its trace. The a slot gives the opposite
angular-sign witness. Ignoring r would miss both.

This is not only a failure of one guessed extension. If a smooth
pointwise boundary subspace reproduces the old allowed horizontal
lambda traces, it contains v at every point: those horizontal sections
have nonzero constant fiber value. The same v belongs to the decaying
Cauchy space at covector(p=0,r>0). Hence ANY pointwise extension that
preserves this exact allowed trace fails the complementing condition.
Allowing angular-dependent local coefficients does not remove this
pointwise intersection. A changed horizontal trace, nonlocal condition,
additional fields or another end problem is outside this statement.

## A different local kinetic boundary is constructive

For a supplied smooth unitary map B between the two two-slot bundles,
set

    Sigma=[[0,B],[Bdagger,0]], mathcalB=gamma5 tensor Sigma,
    allowed trace = eigenspace(mathcalB,+1).

Then Sigma is Hermitian, Sigma^2=1 and anticommutes with R.
Consequently mathcalB anticommutes with BOTH H(p,r) and Hadj(p,r)
for every covector. Each nonzero symbol has eigenvalues
+/-sqrt(abs(p)^2+r^2). No decaying eigenvector can also have fixed
mathcalB eigenvalue. This proves the complementing condition for the
operator and its adjoint, not just a finite direction sample.

The trace has half the full rank. The adjoint trace is mathcalB=-1,
since mathcalB commutes with gamma5 and the Euclidean Green form is
gamma5. In Lorentzian signature gamma0 anticommutes with gamma5,
so Pplus gamma0 gamma5 Pplus=0. It is maximal current-isotropic.
This is a kinetic admissibility statement; no boson variation is removed.

## The spin seam and conjugate fields are retained

Use angular coordinate theta of period2pi. In the chosen unitary
cut frame the common adjoint gauge transition is G, and the four
slot transition is diag(G,G,-G,-G), with bounding spin in u,v.
The following SUPPLIED choice descends:

    B(theta)=i diag(exp(i theta/2),exp(-i theta/2)).

It is unitary, B(theta+2pi)=-B(theta), so Sigma transforms by
R Sigma R at the seam, including all derivatives. Common gauge
transitions cancel in this slot map. Multiplication by it commutes
pointwise with every common adjoint gauge action, even when the
gauge transformation depends on the boundary position. This does
not settle the bosonic boundary equations or supersymmetric closure.

Reality is not imposed by independently adding right fields.
The same kinetic and normal target transformations give

    V=Jdagger P=diag(-sigma2,-sigma2),
    right_normal(q)=V conjugate(left(-q)),

with the conventional external two-spinor conjugation understood.
Thus the required condition on the internal projector is

    V conjugate(Sigma) V = -Sigma.

Our B(theta) satisfies it. Left allowed traces at charge -q then give
right allowed traces at q, and conversely. The check does not equate
opposite-charge independent LEFT fields or double their antiparticles.
The scalar choice B=exp(i theta/2)I has the correct seam but fails this
condition; the constant B=iI satisfies reality but fails the spin seam.
These controls separate locality, bundle descent and physical reality.

The gauge transition G need not be scalar or diagonal: the slot map
is tensored with the identity on the full248. The spin seam is the
stated cusp trivialization of the supplied parent; no different
global spin structure has been silently selected.

## No old charged count transfers to the new boundary

Sigma exchanges the periodic scalar/form and antiperiodic spin slots.
In particular it does not admit a pure lambda horizontal trace.
Its half-frequency multiplication couples the old zero-angular sector
to previously nonzero angular sectors. The subspace on which the old
normal reference and its anomaly were counted is not preserved.

Therefore this positive is a different, supplied local kinetic
boundary law. It is not a lift with the old spectrum; no net chirality,
anomaly cancellation or full determinant is inferred for it. A finite
cusp cut also changes the original complete-domain problem. The
complete action must supply compatible bosonic equations and stationary
backgrounds before a physical spectrum can be claimed.

The boundary criterion and Euclidean/Lorentzian distinction are those
of Witten--Yonekura section2.1,
https://arxiv.org/html/1909.08775. The explicit angular reconstruction,
unchanged-reference obstruction and spin/reality-compatible counterexample
are authored conditional arguments. The separate silver smooth-boundary
positive belongs to its own parent and is not identified with this one.

Next compute the boundary variation of the SAME interacting curved
action under this pairing, or investigate a fully specified nonlocal/
relative end completion. Keep both endpoints and all charged states.
Stability, physical families, parameter-free selection and gravity
remain independent requirements of the full SM/TOE objective.
