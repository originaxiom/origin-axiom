# The full two field complex and physical instability

Authored conditional argument in the pinned parent. All metric, spin,
embedding, action and complete-domain inputs remain supplied. The extra
degree-three slot below is analytical bookkeeping, NOT a physical field.

## Background and actual quadratic action

Let q,r be holomorphic spin coefficients of Q,R, and let u,v be their
variations. Write a=a_x+i a_y, f1=D_x a_y-D_y a_x, and k=nq_charge.
The stationary background is

    A=s(w+2nZ), Q=Q_principal+c*psi*Z, R=d*psi*Z.

Its F residuals vanish, and its moment m0=-nZ*Omega^2 is parallel and
commutes with Q,R. The prior global spin-section proof admits both
neutral fields with finite graph and quartic norms. Their addition does
not change the stationary energy pi*n^2*kappa(Z^2)/g6^2.

Define

    M1=f1+Omega*([u,q dagger]+[q,u dagger]
                         +[v,r dagger]+[r,v dagger]),
    M2=-i[a_x,a_y]+Omega*([u,u dagger]+[v,v dagger]).

The coefficient of the squared path amplitude in the FULL potential is

    g6^2 V2 = integral dxdy kappa[
      Omega^-1*(|Dbar u+i[q,a]|^2+|Dbar v+i[r,a]|^2)
      +2|[q,v]-[r,u]|^2
      +M1^2/(2Omega^2)+m0*M2/Omega^2 ].

The unchanged positive kinetic norm is integral dxdy kappa[
|a|^2/2+Omega*(|u|^2+|v|^2)]. Its real gauge-orthogonal condition is

    G1=D_x a_x+D_y a_y
          -i*Omega*([q dagger,u]+[q,u dagger]
                             +[r dagger,v]+[r,v dagger])=0.

The previous conjugate-pair identity for moment plus gauge square holds
with P=Omega*([q dagger,u]+[r dagger,v]) and the corresponding
opposite-charge adjoint U. No independent opposite-charge variable is
identified with its partner. In a charge block, the moment soft term
remains -k times the WHOLE a/u/v kinetic norm.

## The actual elliptic complex and its metrics

Fix a Z-charge subbundle E, containing all its principal weights.
Write K=S^2 and barK for (0,1) forms. The graded bundles are

    C0=E,
    C1=(E tensor barK) + (E tensor S) + (E tensor S),
    C2=(E tensor S tensor barK) + (E tensor S tensor barK)
                                      + (E tensor K),
    C3=E tensor K tensor barK.

Their coordinate Hermitian norm densities, including dxdy, are

    C0: Omega^2;
    C1: diag(1/2,Omega,Omega);
    C2: diag(Omega^-1,Omega^-1,2);
    C3: 2Omega^-2.

E's Hermitian metric multiplies each entry. C1 is exactly the physical
kinetic metric. C2 is exactly the three F-residual norm metric.
C0 fixes the gauge parameter normalization. The C3 choice makes a
convenient elliptic Hodge completion; changing a positive normalization
there does not create a physical degree of freedom.

For epsilon in C0 and (p1,p2,t) in C2, set

    D0 epsilon=sqrt(2)*(Dbar epsilon,-i[q,epsilon],-i[r,epsilon]),
    D1(a,u,v)=(Dbar u+i[q,a], Dbar v+i[r,a], [q,v]-[r,u]),
    D2(p1,p2,t)=Dbar t-[q,p2]+[r,p1].

D0 is the complexified actual gauge tangent with a common harmless
normalization. D1 is the linearized F map. D2 is its differential
relation, not an imposed new equation of motion. Leibniz and Jacobi
give D1D0=D2D1=0 because Dbar q=Dbar r=[q,r]=0. Curvature is of
type(1,1) on a curve; it does not produce a (0,2) defect.

Using the displayed metrics, the C0 adjoint is

    D0 dagger(a,u,v)
       =-[Dz a-2i*Omega*([q dagger,u]+[r dagger,v])]
                                                    /(sqrt(2)*Omega^2).

Together with the full conjugate-pair identity this gives

    g6^2 V2_gf(x)=|D0 dagger x|^2+|D1 x|^2-k*|x|^2,

where x=(a,u,v) and all norms have their declared metrics.
Gauge fixing adds a nonnegative square; it does not alter the bare
theory on the physical gauge slice.

Use the odd-to-even Hodge map

    T: C1+C3 -> C0+C2,
    T(x,sigma)=(D0 dagger x, D1 x+D2 dagger sigma).

The complex identity makes the cross term vanish:

    |T(x,sigma)|^2
       =|D0 dagger x|^2+|D1 x|^2+|D2 dagger sigma|^2.

Its kernel is H1 direct-sum H3, with
H1=ker D0 dagger intersect ker D1 and H3=ker D2 dagger.
The index cannot be read as physical negative directions until H3 is
controlled. The adjoint kernel contains H0 and H2, not a discarded
negative population.

## Complete domains and Fredholmness of both shifted blocks

Take compactly supported smooth sections and their complete first-order
graph closures. The Hodge operator has Dirac-type principal symbol
after the stated positive normalizations. Spin and magnetic connections
are unitary; the Higgs coefficients are bounded in orthonormal frames.
Complete cutoffs identify minimal and maximal Dirac realizations.
The differential relations, adjoints and Hodge norm identity extend
from compact support to these domains, without a finite-circle boundary
condition or an ignored flux term.

First set c=d=0. The complex splits into the single-Q complex
E -> S tensor E and its S-tensor copy shifted one degree. The first
uses the old A/Q map; the second contributes its appropriate adjoint.
For spin shift h=0,1, let j be a principal spin, m=-j,...,j, k=nq.
The scalar line in the single-Q complex is S^(h-m-2k).

Admissible zero-angular pairs have m-h even, m<j. Their canonical
blocks, up to constant unitary row phases, are

    [[partial_t+delta,b],[-b,-partial_t+delta]],
    delta=k+(m+1-h)/2,
    b^2=(j-m)(j+m+1)/2.

Here t=log y. These follow from the actual Dolbeault metric of
S^(h-m-2k), whose radial drift is(1-h+m+2k)/2, and the same normalized
principal multiplication E_raise/sqrt(2). Tensoring by S shifts the
spin connection and the angular parity together; it is not an
arbitrary change of a mass formula.

The h=1 block can also be derived directly from the second half of the
declared complex, rather than guessed by a shift. For odd m write the
physical R variation as v(t), and a C3 coefficient at weight m+1 as
sigma=alpha/(sqrt(2)*y^(3/2)). The two output residuals are

    i*(v_y+(m+2k)*v/(2y))-ell*alpha/(sqrt(2)*y),
    ell*v/(2sqrt(y))
       +i*(y^2*sigma_y+(3-m-2k)*y*sigma/2),

where ell^2=(j-m)(j+m+1). Multiplying the first by y and the second
by sqrt(2y) normalizes their actual C2 norms. The result is
i*(partial_t+delta)v-b*alpha and
b*v+i*(partial_t-delta)alpha. Constant row/column phases give the
displayed block (or its adjoint). The C3 kinetic density becomes
abs(alpha)^2 dt. These substitutions and adjoints are checked explicitly.

Keep the upper A_j extreme when j-h is even, with drift
k+(j+1-h)/2, and the lower Q_-j extreme when j+h is odd, with drift
k-(j+h)/2. Every retained drift is a nonzero half-integer. Scaling
the principal coefficient by tau in[0,1] gives squared thresholds
delta^2+tau^2*b^2>=1/4, including the unpaired extremes.

Nonzero angular sectors have positive frequency-square*y^2 growth,
with bounded lower-order linear-y coefficients for each fixed n and
the finite full E8 roster. Their minimum nonzero frequency is1/2.
They confine uniformly through this principal homotopy. The compact
core cannot add essential spectrum at zero. Both shifted blocks, hence
T, are Fredholm throughout. This is an OPERATOR homotopy, not a family
of stationary backgrounds.

The finite c,d additions have coefficients proportional to the
physical psi, which behaves as sqrt(y)*exp(-pi*y/ell) and tends to zero.
They are bounded graph-compact first-order-operator perturbations, by
local ellipticity/Rellich and small tail norm. Thus ind T is unchanged
for every finite pair. No principal constant field is called compact.

## Exact global index and the endpoint

Let J(a) be the already derived COMPLETE L2 Dolbeault index of S^a:

    b(a)=floor(a/2) for a<=0, ceil(a/2)-1 for a>=1;
    h(D)=0 for D<0, 1 for D=0, D for D>=1;
    J(a)=h(b(a))-h(b(2-a)).

This uses the Hermitian Hodge adjoint, precise logarithmic equality
endpoints, global Weierstrass pole basis and single-residue upper bound.
Those authored global steps and finite safeguards are pinned, not
replaced by a compact-surface degree or a new fitted formula.

At the zero-Higgs endpoint of the gapped operator homotopy, T consists
of two spin-shifted Dolbeault maps and two adjoint maps. Therefore

    ind T_q = sum_m multiplicity(q,m) *
          [2J(1-beta)-J(-beta)-J(2-beta)], beta=m+2nq.

Call the bracket I(beta). Direct use of the exact endpoints gives

    I(0)=0,
    I(beta)=-sign(beta)*(-1)^beta for nonzero integer beta.

For k=nq>0 in the actual E8 roster, beta>=0. For abs(n)>=2 it is
strictly positive at every charged weight. Summing the entire root
roster, or independently the SU5 tensor branching, gives

    abs(q)     1   2   3   4   5   6
    ind T_q   -6   6   4  -3  -6  -1       (k>0, abs(n)>=2).

At abs(n)=1 the abs(q)=1 entry is0, because its lowest beta is0;
all other entries stay as displayed. Negative flux uses negative q.
At n=0 every charge block has index zero by the oddness of I and
the symmetric principal-weight roster. Finite flux tables are only
controls; parity and the weight bound give the all-integer result.

Negative or zero entries are not stability results. They do not
exclude kernels. Positive entries also still include the possible
auxiliary H3 unless the next step is supplied.

## Removing the auxiliary kernel and earning physical negative modes

If d!=0 and q!=0, the FIRST component of D2 dagger sigma is a
positive metric factor times [r dagger,sigma]. On the charge-q
subbundle, r=d*psi*Z acts as the scalar q*d*psi. It is nonzero at
EVERY interior point: psi is a nowhere-zero holomorphic section of
the trivial extending spin line. Consequently D2 dagger sigma=0
implies sigma=0, including for weak L2 solutions by local ellipticity.
There is no needed uniform positive bound at infinity.

Thus H3=0 for d!=0. It follows that

    dim H1 = dim ker T >= ind T.

The positive q=sign(n)*2 and q=sign(n)*3 blocks force at least6 and4
complex degree-one modes. On H1 the actual gauge-fixed Hessian is
exactly -nq times the positive physical kinetic norm. The old compact
graph approximation argument then supplies finite-dimensional negative
subspaces of smooth compactly supported variations with finite quartic
nonlinear paths. Removing the nonnegative gauge-fixing term preserves
the negative sign; stationary gauge invariance makes these directions
inject into the physical gauge quotient.

Hence this family has at least10 COMPLEX physical negative directions
for every nonzero integer n, all finite c and all finite d!=0.
For d=0 the preceding50 lower bound applies. Together they imply a
uniform lower bound of10 for all finite c,d in the stated family.
The first-flux infinite Morse result is stronger there and survives
both decaying neutral fields. No full Morse count is claimed.

The H3 argument fails at d=0; it is not silently assumed there.
Likewise, neither the dimension of the complex nor its index is
identified with the physical four-Weyl mass map or particle generations.

## Flavor symmetry and positives retained

A constant SU2 acting on(Q,R) preserves the equal spin metrics, the
sum of moments and W (determinant one). In the independent
principal/neutral directions, the coefficient matrix is

    [[1/2,c],[0,d]]

when the principal raising section is normalized before its1/2.
Its determinant is d/2. If d!=0 no invertible flavor rotation can make
the two field profiles proportional or erase R everywhere. The above
test treats a genuine extension, not a disguised R=0 model.

At n=0 every residual is zero, so the FULL physical Hessian is
nonnegative for every finite c,d. If(c,d)!=0 the connected commutant
is S(U3 x U2): the principal triple and Z both act, with their
asymptotically distinct norms separating the invariance conditions.
At c=d=0 it is the old SU5 control. The norm depends on
abs(c)^2+abs(d)^2, leaving unselected flat data rather than a selected
vacuum. A fixed-domain graph-compact deformation of the same gapped
fermion operator preserves its zero charged index; individual kernels
can jump.

No result excludes other end classes, nonzero-F stationary phases,
sources, different domains/parents or the generated architecture.
The next physical candidate must change a hypothesis of this
obstruction, not relabel its index as chirality or repeat its amplitude
scan. Foundation-to-action selection, full interacting chiral spectrum,
anomalies, quantum consistency, gravity and any observer/qualia
identification remain unearned here.
