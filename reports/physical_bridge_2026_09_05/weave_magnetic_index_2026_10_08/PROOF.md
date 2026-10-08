# A bosonic index and magnetic instability on the complete cusp

Authored conditional argument. The supplied parent, metric, embedding,
spin and domain are those pinned in INPUTS.json. The operator defined
here is a BOSONIC residual map, not an unearned physical fermion map.

## Charge lines and the full quadratic form

Use the previous stationary background with R=0 and moment -nZ.
Set k=nq in a nonzero Z-charge q subspace. Its w weight m induces
the unitary connection d-i(m+2k)s, hence the holomorphic Hermitian line

    E_(q,m)=S^(-beta), beta=m+2k.

Q variations u are sections of S tensor E, while complex connection
variations a are E-valued (0,1) forms. This statement concerns their
actual global transition functions, not only the limiting peripheral.
Here S is the trivial extending spin line, with global psi squared=omega.

The sealed full quadratic form and real gauge-orthogonality condition
give, after combining opposite-charge conjugates,

    g6^2 V2_gf(a,u)=norm(B_q(a,u))^2-k*norm(a,u)^2.

The domain norm is integral dxdy kappa(abs(a)^2/2+Omega*abs(u)^2).
In coordinate coefficients the two residuals defining B are

    Dbar u+i[Q,a],
    Dz a-2i*Omega*[Q dagger,u].

Their squared norms carry weights Omega^-1 and1/(2Omega^2).
These factors follow from the previous identity splitting moment plus
gauge divergence; they are not independent choices. As global bundles
B maps Q and connection forms to their derivative residual spaces.
At Q=0 it is, up to unitary phases and positive normalizations,

    dbar_(S tensor E) direct-sum dbar_E dagger.

Thus ind B = ind dbar_(SE) - ind dbar_E, NOT their sum and not a
single holomorphic-section count.

The soft term is fixed by trace invariance:
Tr(Z[u,u dagger])=q Tr(u dagger*u), and
-i[a_x,a_y]=[a,a dagger]/2. Both give -k times THEIR positive kinetic
norms. For k<0 this contribution is positive; at k=0 it vanishes.
R fluctuations are still retained in the parent. Setting delta R=0
is an allowed variational subspace, sufficient for a lower bound on
instability; no positive claim about all fluctuations is made.

## Exact L2 Dolbeault indices of spin powers

Put L_a=S^a for an arbitrary integer a. Near the puncture use a compact
coordinate v, r=abs(v). The spin metric has squared norm comparable to
r*abs(log r), while the complete area is comparable to
dr dtheta/(r*abs(log r)^2). A meromorphic coefficient with pole order p
has L2 radial integrand

    r^(a-2p-1)*abs(log r)^(a-2).

Therefore it is allowed iff a-2p>0, or a-2p=0 AND a<1.
The largest allowed integer pole order is

    b(a)=floor(a/2)                         for a<=0,
    b(a)=ceil(a/2)-1                        for a>=1.

The two formulas agree with the direct inequality for odd a. At a=0
a constant is L2 because the equality logarithm is integrable. At a=2
a first-order pole is NOT L2. Losing these endpoints changes the answer.

Angular Laurent orthogonality with bounded metric comparisons excludes
every term beyond b(a), including essential singularities. Thus L2
holomorphic sections extend meromorphically with precisely that pole
bound. Because S has the global nonvanishing holomorphic section psi,
the coefficients are meromorphic FUNCTIONS on the compact elliptic curve.

Write h(d) for the dimension of functions whose only allowed pole is
of order at most d at the puncture. Then

    h(d)=0 if d<0; h(0)=1; h(d)=d if d>=1.

For the last formula the Weierstrass functions 1,x^i,x^i*y give distinct
pole orders0,2,3,...,d. They span as well: subtract the leading principal
part successively. A residual simple pole is impossible, since
multiplication by the nowhere-zero holomorphic differential omega would
give a meromorphic one-form with a single nonzero residue. Holomorphic
functions on the compact curve are constant. This proves both bounds,
rather than just reusing the preceding lower-bound basis.

The formal adjoint kernel is represented by the Hermitian Hodge map

    b(v) dv tensor e_Ldual
       -> h_L^-1 conjugate(b(v)) dbar v tensor e_L.

Direct differentiation gives partial_v(h_L*a_barv)=0; the norm on each
side is the same integral h_L^-1 abs(b)^2 dxdy up to the fixed common
form factor. Consequently the adjoint kernel is exactly the L2
holomorphic space of K tensor L_a dual=S^(2-a). Completeness and
exhausting cutoffs put these L2 zero solutions in the chosen minimal
graph closure. Conversely, a weak adjoint zero solution is smooth
locally and obeys this holomorphic equation.

It follows, once Fredholmness is established below, that

    J(a)=ind dbar_(S^a)=h(b(a))-h(b(2-a)).

In particular J(-beta)=-ceil(beta/2) and
J(1-beta)=-floor(beta/2) for every beta>=0 (including beta=0).
Their difference is beta mod2. The identity J(a)=-J(2-a)
is an independent duality control. No closed-surface degree formula
can replace these cusp-domain counts.

## Fredholm domains and a legitimate homotopy

For a line S^a, in the holomorphic z=x+iy spin frame the section's
coefficient has angular transition (-1)^a. Its norm is
integral dxdy y^(a-2) abs(f)^2. With t=log y the canonical coefficient
is f=y^((1-a)/2)*v; the first-order radial drift is (1-a)/2.

If a is even the zero angular channel has a nonzero half-integral drift.
If a is odd, the antiperiodic circle has no zero angular channel.
Every nonzero angular square has positive frequency-square*y^2 leading
growth with only lower-order linear-y terms. Each fixed integer a
therefore gives a Fredholm complete Dolbeault operator. Cutting off the
compact core and local ellipticity cannot add essential spectrum at
zero. This proves closed range as well as finite kernel/cokernel.

For the coupled principal background, scale the principal coefficient
by t0 in[0,1], holding A_n fixed. This is an OPERATOR homotopy, not a
claim that the intermediate fields are stationary. Its zero-angular
paired blocks, in the already checked kinetic coordinates, are

    [[partial_t+d,t0*b],[-t0*b,-partial_t+d]],
    d=k+(m+1)/2, b^2=(j-m)(j+m+1)/2, m even.

Their squares have threshold d^2+t0^2*b^2>=1/4. Keep the upper A
extreme with drift k+(j+1)/2 for even j and lower Q extreme with
drift k-j/2 for odd j; both are nonzero half-integers too. Nonzero angular sectors confine
uniformly on this finite homotopy. Thus it remains Fredholm at every
integer n, including the first flux whose BOSONIC Hessian, after the
soft shift, has negative essential spectrum. Those are different tests.

All zeroth-order coefficients are bounded in orthonormal frames. The
first-order domains are fixed complete graph domains; minimal and
maximal realizations agree by complete cutoffs for the associated
Dirac systems. The homotopy is norm-continuous as a bounded map from
that graph space to L2.

Now restore any finite c. The additional c*psi*Z is bounded and tends
to zero at the cusp in physical norm. Multiplication is graph-compact
by local elliptic estimates/Rellich on each compact core and arbitrarily
small tail norm. Hence ind B_q(c)=ind B_q(0). This is not the false
claim that all constant principal fields are graph-compact.

Combining the homotopy with the line index gives

    ind B_q(c)=sum_m multiplicity(q,m)*
                  [J(1-m-2nq)-J(-m-2nq)].

It is valid without calculating any particular mixed zero-mode profile.

## The complete charge count

For k=nq>0 in the actual E8 roster, beta=m+2k>=0 at every weight,
for ALL nonzero integer n. The smallest case is abs(q)=1,j=2,k=1,
where beta=0 occurs at m=-2 and contributes ZERO, not a spurious one.
The other charged modules are those derived in the preceding packet:

    abs(q)=1:6 V2; 2:3(V1+V3); 3:2(V1+V3);
    abs(q)=4:3 V2; 5:6 V0; 6:V2.

Since 2k is even, the index contribution is one precisely at odd m.
Therefore the charge-resolved lower bounds for k>0 are

    abs(q)     1   2   3   4   5   6
    ind B_q   12  18  12   6   0   2

and their sum is50. Negative n uses negative q and the conjugate
representations. The root route and the independent SU5 tensor route
both check the entire248, then compute the line indices themselves.
Finite flux tables are controls; the beta inequality and parity prove
the all-integer result.

This index is a lower bound on dim ker B_q, not an equality. It is
also NOT the four-slot physical Weyl index; no such map is identified.

## From the index to admissible physical negative directions

Choose a finite subspace of ker B_q of dimension ind B_q when this is
positive. On it the gauge-fixed quadratic form is exactly -k times
the positive kinetic norm. This already proves a negative subspace
in the closed form domain.

To avoid assuming extra pointwise decay or L4 regularity of those
abstract kernels, approximate a basis by compactly supported smooth
sections in the defining graph norm. In this finite-dimensional
subspace the Gram and B-energy matrices converge uniformly to the
identity and zero. For sufficiently accurate approximations the entire
span is strictly negative. Every approximant and its nonlinear field
path have finite derivative and quartic norms because the support
is compact.

The bare physical quadratic form is the gauge-fixed form MINUS its
nonnegative gauge-fixing square. It is therefore negative on the same
span. At a stationary gauge-invariant background it vanishes on gauge
tangents and pairs them with zero. Hence the negative span injects
into the physical gauge quotient. No negative direction can be merely
a gauge artifact or an inadmissible non-L2 variation.

This proves at least50 COMPLEX physical negative directions (a real
negative subspace of dimension at least100) for
every nonzero integer n and every finite c in this R=0 family.
It is not a full Morse count. At abs(n)=1 the earlier infinite
essential instability is stronger. At abs(n)>=2 it resolves the
previously open discrete-stability question: no finite neutral
amplitude stabilizes this family despite its positive essential bottom.

At n=0 there is no negative moment shift. The existing neutral SM
minimum and zero charged-index result are preserved, not refuted.

## An existing second-field hatch is not closed

The same action already contains R. For any finite c,d,

    Q=Q_principal+c*psi*Z, R=d*psi*Z, A=A_n

still has vanishing F residuals and moment -nZ. Both spin sections are
admitted by the same global norm argument; R commutes with Q and its
own adjoint. The moment is parallel and commutes with both fields,
so full stationarity holds. No new field or boundary functional is
being invented here.

However, the linearized commutator residual now contains

    [delta Q,R]+[Q,delta R],

and the R-derivative residual contains the connection variation
-i[delta A,R]. They do not vanish on the old A/Q kernel. Thus the
R=0 identity used for its negative subspace does not by itself settle
the coupled two-field Hessian. Testing that admitted family is a
separate bounded question, with the first-flux end obstruction retained.

No closure extends to all central-field pairs, other asymptotics,
sources, domains, actions or the full architecture. No chiral spectrum,
anomaly result, parameter-free action, quantum theory, gravity, observer
or qualia mechanism has been derived.
