# Free boundary fluctuations and the complete degree count

October 4, 2026. Authored conditional analysis; independent specialist
acceptance is not claimed. Symbolic controls can expose sign and algebra
errors but cannot by themselves establish the analytic statements below.

## The action and positive complex directions

Take a smooth compact connected X with nonempty smooth boundary, fixed
Riemannian metric and positive fibre metric. Let C=A+Psi be a flat SL(n,C)
connection with mu=d_A^*Psi=0. The retained action has potential

    V=c integral_X (|F_C|^2+|mu|^2), c>0.

This is R76/R81/R83's supplied residual functional. At F=mu=0 every first
variation vanishes, including free boundary variations. That fact does not
impose Psi(n)=0. The harmonic-map energy integral |Psi|^2 is a different
functional with different free boundary variation and must not replace V.

For Hermitian trace-free s, g=exp(epsilon s) acts by C_g=g^-1 C g+g^-1 dg.
At epsilon zero,

    delta C=d_C s,
    delta A=[Psi,s],       delta Psi=d_A s,
    delta F_C=[F_C,s],
    delta mu=L s=d_A^*d_A s+sum_i[Psi_i,[Psi_i,s]].

The last identity follows by differentiating the connection in the adjoint
as well as Psi: delta(d_A^*Psi)=d_A^*delta Psi-sum[delta A_i,Psi_i].
In an orthonormal frame this yields the displayed sign. Covariance supplies
the same formula globally, with the Levi-Civita connection included in the
formal adjoint. For Hermitian s, [Psi_i,s] is anti-Hermitian and

    tr(s[Psi_i,[Psi_i,s]])=tr([Psi_i,s]^dagger[Psi_i,s]) >= 0.

At the background, the Hessian bilinear form is twice c times the inner
product of linear residuals. Thus Ls=0 gives a Hessian null direction
(delta A,delta Psi) with zero curvature and moment residuals. This is an
actual null direction of the bare Hessian, not merely a zero frozen quartic.

## Boundary data and the gauge quotient

L is a real, strongly elliptic, formally self-adjoint operator on Hermitian
trace-free endomorphisms. For zero boundary values its quadratic form is

    integral_X (|d_A s|^2+sum_i|[Psi_i,s]|^2).

The covariant Kato inequality and scalar Dirichlet Poincare inequality make
it coercive. Lax-Milgram and elliptic regularity therefore give a unique
smooth solution of Ls=0 for every smooth Hermitian trace-free boundary value.
This uses standard elliptic theory on a smooth compact boundary; no infinite
end theorem or assumption of semisimplicity is inserted. The boundary data
space is infinite-dimensional for a three-dimensional core. Zero Dirichlet
data give s=0, so releasing that datum is an essential change of problem.

It is necessary to distinguish these directions from gauge. A compact gauge
parameter xi is anti-Hermitian. If d_C s=d_C xi, then d_C(s-xi)=0. The space
of parallel complex trace-free endomorphisms is finite-dimensional on
connected X, bounded by 2(n^2-1) in real dimension. Taking the Hermitian part
determines s from s-xi. Therefore at most a finite-dimensional subspace of
the infinite solution space can become compact gauge (including zero fields).
Even allowing arbitrary compact boundary gauge transformations leaves an
infinite-dimensional quotient of Hessian null directions.

The same conclusion persists in the retained faithful E8 parent. The
structure subalgebra and its invariant complement are preserved by d_C;
the compact-compatible orthogonal projection maps a hypothetical full-parent
compact gauge primitive to a compact primitive in the structure subalgebra.
Thus a direction non-gauge there is not erased by the larger parent. This
uses the supplied regular embedding, not a new derivation of E8.

Each surviving smooth direction has finite positive norm on compact X.
Its norm obeys, for Ls=0,

    norm(delta A)^2+norm(delta Psi)^2
      = integral_boundary tr(s nabla_n^A s).

This is the Dirichlet-to-Neumann pairing. It is a kinetic norm, not a bulk
potential or mass. The bare Hessian with these unrestricted traces cannot
be a Fredholm finite-zero-mode problem after the stated compact gauge
quotient. A chosen self-adjoint extension that removes directions changes
the domain and must be supplied by the physical completion.

This argument concerns the infinitesimal Hessian. It does not need an
unproved open chart of flat representations or interchange a spectral
limit with a derivative. Integrating all these directions into a smooth
nonlinear family is a separate assertion not required here.

## Exact Fourier comparator and a boundary penalty

For a transparent comparator use X=T2 times [0,L], flat metric, torus
coordinates of period 2pi and normalized torus volume one. Let
T=diag(1,-1), so tr(T^2)=2. At C=0 take

    f_k(r,x)=sinh(k r)/sinh(k L) cos(k x),    k=1,2,...,
    C_epsilon=epsilon T df_k.

This is globally defined and flat, with mu=-epsilon T Delta f_k=0. Its
monodromy is trivial. Compact gauge variation of Psi at Psi=0 vanishes,
whereas T df_k is nonzero Hermitian. Different k are independent and
orthogonal by Fourier orthogonality. The exact field norm is

    G_k=integral_X tr(T^2)|df_k|^2=k coth(k L)>0.

Arbitrary real linear combinations remain harmonic. Fixing f to zero at
both ends removes these directions by uniqueness. On a closed flat torus,
a harmonic scalar is constant and df=0. The k=0 profile r/L has nonzero
normal Higgs and norm 2/L; it should not be lost by taking a formula whose
cosine normalization was derived only for k>0.

As an explicitly added comparator, take

    B_beta=(beta/2) integral_boundary |Psi_tangent|^2, beta>0.

It is invariant under compact gauge transformations. In the comparator,
B_beta(C_epsilon)=beta epsilon^2 k^2/2; the normal constant k=0 direction
survives. For the abelian Higgs sector the full nonnegative quadratic form
is |dPsi|^2+|d^*Psi|^2 plus this boundary penalty. Its zero kernel consists
of relative harmonic one-forms (closed, coclosed, zero tangential trace),
which is finite-dimensional. For T2 times interval it is one-dimensional,
represented by dr, per retained Cartan generator. This is a kernel claim,
not a computed positive spectrum or a proof of supersymmetric completion.

This illustrates a real way a boundary term can remove the uncontrolled
zero directions. It introduces beta and a boundary law. It has not been
derived from OA, and on a nonsplit silver background its own variation
may prevent that background from remaining stationary. Neither its
quadratic coefficient divided by G_k nor the frozen profile is a physical
mass calculation. No such quotient will be reported as a particle mass.

## All four degrees on the silver pairs

Reuse the exact silver profiles on a connected compact oriented three-manifold
with nonempty torus boundary. For a rank-d flat local system E, chi(X;E)=0,
H3(X;E)=0 and H0(X,boundary;E)=0. Poincare-Lefschetz with the actual dual gives

    absolute: (a0, h1, h1-a0, 0),
    relative: (0, h1_dual-a0_dual, h1_dual, a0_dual).

The supplied twisted fermion grading has odd-minus-even count
(b1+b3)-(b0+b2). It is zero for each of these two uniform de Rham domains,
including both actual dual orders and the exterior coefficient. This is
the known torus-boundary Euler mechanism applied to the verified nonsplit
bundle, not a new universal chirality obstruction. The relation
h2_absolute(E)=h1_relative(E dual) means replacing degree two by absolute
H1(E dual) is generally wrong on a boundary problem.

For the interior image, H0 and H3 images vanish, and the perfect image
pairing gives dimensions (0,n(E),n(E dual),0). This produces the retained
(-1,-1) difference. The image is a cohomological construction; these
dimensions alone do not define an elliptic fermion boundary domain.

The action's free-boundary null directions are in the adjoint deformation
sector. The silver charged degree table is a different necessary check.
They cannot be combined as a single complete spectrum: the former uses
unrestricted traces, the latter uses specified absolute/relative domains.

## Primary source and scope

The supplied complex connection, harmonic-metric moment equation and D-term
potential are reviewed in Pantev-Wijnholt, arXiv:0905.1968v1, section 2.3,
equations 2.21 through 2.27. That paper later restricts to commuting Higgs
fields; we do not cite it as a theorem about our noncommuting candidates.
Wu-Zhang arXiv:2109.01776v1 Proposition 3.3 and its proof supply compact
Dirichlet existence, already applied in the preceding packet. The Jacobi,
gauge-quotient and boundary-kernel arguments above are authored here.
Those primary passages were read, not the full papers on this turn.

The full goal remains active. A justified boundary or joined completion
must both control these fluctuations and admit the desired charged domain,
then establish interactions, anomalies, physical scales and three complete
generations. This packet supplies a sharper test of that completion, not
an arbitrary boundary term as the answer to the parameter-free problem.
