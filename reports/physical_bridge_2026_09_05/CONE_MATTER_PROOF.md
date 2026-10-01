# Exact exterior matter profiles in one cone action

October 1, 2026. R74 authored conditional argument, frozen before finite
controls. Supplied metric/action/parent, not independent proof acceptance.

## 1. Actual coefficient and central twist

R66 has C_r=h'H, C_x=tN, C_y=kZ+beta t^2P, t=exp(-h), k=log(q),
beta=6/(q-q^-1), N=E02+E23, P=N^2, H=diag(1,0,0,-1),
Z=diag(1,-3,1,1). The exact branch satisfies v=h_s->0, t->0,
v_s=v-(alpha t^2+beta^2 t^4/alpha)/2, s=-log(r).
The supplied split defining five is diag(C,0). A central meridian
twist diag(-I4,1) commutes with it. R40/R59 identify Lambda2(W)
with the coefficient of a supplied parent gauge matter sector.

In the orthonormal wedge basis e_i wedge e_j, i<j, define the LIE
action rho(X)(u wedge w)=Xu wedge w+u wedge Xw. This preserves
commutators and adjoints. It is not the GROUP action Lambda2(g).
Write n=rho(N),p=rho(P),z=rho(Z),h0=rho(H).
The six has charges+2,-2, three each; it is orthogonally reducing
for all C_i and their adjoints, and is periodic under the central
twist because (-1)^2=1. The remaining four in Lambda2(W) has a
minus sign and half-integral meridian frequencies. It is not added
to a periodic zero-mode count. A mu=+/-i twist instead makes the six
antiperiodic and is NOT within this periodic block quantifier.

At every positive radius its longitude has eigenvalues q^2,q^-2,
three each, so longitude-I is invertible. The torus Koszul complex
is contracted by that inverse: all boundary cohomology vanishes.
This matches the acyclicity mechanism of B1509, not its global
nonsplit representation or its interior index.

## 2. Exact Q graph witnesses despite that acyclicity

Use R68 Q=Gamma(partial_r+A/r) on48 normalized form components,
with positive L2(dr) coefficient metric and actual rho(C).
For the ZERO periodic Fourier block, the limit has z_y=kz/sqrt(alpha),
z_x=0,K=0. Choose the aspect alpha=9k^2, explicitly as an input.
Then each coefficient has lambda=4/9 and eta=1/3. Its limiting
angular eigenvalues are -4/3,-1/3,+1/3,+4/3, each of multiplicity12.
The actual tail R(s)=A(s)-A_infinity has norm bounded by

    2|v|+4sqrt(alpha)t+4|beta|t^2/sqrt(alpha)->0.     (1)

The wedge representation bounds ||rho(X)||<=2||X|| justify (1).
For each fixed q choose a tail with norm<=1/256. No uniform radius
or physical scale is predicted.

Reuse R72's explicit weighted stable/unstable integral contraction
with shifts theta=3/4,-3/4 and decay weight gamma=1/3. Stable and
unstable gaps are (5/12,7/12) and (7/12,5/12). The convolution sums
are12+12/11=144/11 and4+4/3=16/3; after multiplication by1/256
the contractions are9/176 and1/48. Both are strictly below one.
Projection of the initial value onto the stable space is the seed,
so the constructed exact spaces Sl,Sf have dimensions36,12.
Their envelopes are O(exp(5s/12)) and O(exp(-13s/12)), respectively.
The converse integral identity gives Sf subset Sl.

All Sl are L2(dr): exp(-s)exp(5s/6) is integrable. J=-Gamma is
nondegenerate, and A^H J+JA=0. Thus exact solution current is
constant. Sf paired with Sl tends to zero as exp(-2s/3), so Sf
is the12-dimensional annihilator of Sl and its radical. The quotient
has rank24. The Hermitian form is iJ, not the anti-Hermitian J;
its ambient signature is(24,24), and the isotropic radical of dimension12
leaves quotient signature(12,12).
Outer cutoffs put Sl in Dmax(Q). Graph continuity of Green pairing
excludes nonradical classes from Dmin. Sf=O(r^(13/12)) is minimal
by an apex cutoff whose squared graph error is O(epsilon^(7/6)).
Therefore Sl/Sf injects as a24-dimensional NONDEGENERATE WITNESSED
subspace of Dmax/Dmin. This is not the whole quotient or a chosen
self-adjoint domain, and says nothing yet about chiral particles.

The numerical metric choice is not innocuous. At q=17+/-12sqrt2,
|k|>3 (q_plus>32>e^3 and q_minus=q_plus^-1). At alpha=1 the
zero-Fourier six has lambda=4k^2>36>3/4 and misses the limiting
critical window. At alpha=9k^2 it enters. Other Fourier modes and
other metrics require their own domains; cohomology is the same.

## 3. Exact degree-one profiles with separate residuals and products

Q cancellation alone is insufficient. Solve the scalar equation
delta_C d_C phi=0 with phi=f(s) in the same six. Direct metric
adjunction, including the radial h'H coefficient, gives

    f_ss-f_s-B(s)f=0,
    B=(v-v_s)h0+v^2 h0^2+alpha t^2 n^H n
                  +(kz+beta t^2p)^H(kz+beta t^2p)/alpha. (2)

B tends to(4/9)I6. No diagonal/abelian substitution is made in (2).
Set y=(f,f_s); its matrix is [[0,I],[B,I]]. The constant eigenframe

    W=[[I,I],[-I/3,4I/3]],
    W^-1=[[4I/5,-3I/5],[I/5,3I/5]]

diagonalizes the limit to(-I/3,4I/3). In this frame the perturbation
norm is at most(6/5)||B-(4/9)I||. This tends to zero; an explicit
sufficient bound is

    2|v-v_s|+4v^2+4alpha t^2
           +8|k beta|t^2/alpha+4beta^2 t^4/alpha.   (3)

Choose a tail with the transformed perturbation<=1/1024. An explicit
stable/unstable contraction at weight7/24 has convolution sum
24+8/13=320/13 and contraction5/208<1. It constructs six exact
solutions with both f and f_s=O(exp(-7s/24)). The seed maps injectively.

Let a=d_C phi. Flatness gives d_C a=0, and (2) gives delta_C a=0.
In normalized form coefficients,

    a_x=sqrt(alpha)t n f,
    a_y=(kz+beta t^2p)f/sqrt(alpha),
    a_r=-f_s-v h0 f.

These are O(r^(7/24)); a has pure total degree one. The limiting
a_y coefficient is invertible, so a=0 implies f=0 on a tail.
Hence the six profiles are independent. They lie in Sl, but none
is a nonzero Sf profile: if a were O(r^(13/12)), invertibility of
a_y and the radial identity would give the same bound on f,f_s.
After shift -3/4 the scalar limiting matrix has only positive
eigenvalues,5/12 and25/12. The future-only integral contraction,
with no stable seed and sufficiently small tail, admits only zero
such decaying solutions. Thus these six inject into Sl/Sf.
Pure degree-one data pair to zero under J; this is an isotropic
six-plane, not the required maximal12-plane or selected full end law.

Their physical point norm is O(r^(7/24-1)). Kinetic radial density
is O(r^(7/12)), and L4 density is O(r^(7/6-2))=O(r^(-5/6)); both
integrate at zero. Smooth outer cutoff adds regular, compact-annulus
residuals. The cut profiles therefore have separate maximal d/delta
graph norms AND finite L4 products. No polynomial asymptotic residual
or finite cutoff extrapolation is used to prove exact harmonicity.

Embed them through R40/R59's supplied parent coefficient map. A finite
dimensional positive parent norm and bounded brackets give the same
Holder estimate as R67: quadratic residuals of such L4 fields are L2.
On the separate MAXIMAL graph-plus-L4 class the residual-square action
is a finite C1 polynomial about the zero-residual background. This is
a sufficient finite-action class, NOT R67's compact-support closure
X0 or a derived physical end law. The witnessed nonminimal profiles
show the distinction. Compact gauge/end variation and full supercharge
derivative closure must still be imposed on the same parent fields.
These a are locally complex-exact. No compact gauge quotient or global
massless-mode count follows from their six-dimensional local seed space.

## 4. B1509 scope and physical consequence

Proposition E counts W subset H1(T;V) with its annihilator in the dual
cohomology. That is a coherent cohomological prescription, not by itself
the classification of analytic cone end domains when the relevant
spectral gap is absent. R63 already banked this distinction. The present
changing exterior coefficient realizes it with separate derivative and
finite-product positives, rather than mere frozen angular slots.

Nothing here refutes B1509's rank-five nonsplit index or supplies its
source. The background here is split, on the supplied cone instead of
the complete Blaschke end. No global match to its extension, admissible
end selector, extra5bar particle, anomaly cancellation or generation
is proved. An anomaly inflow term is also not automatically a particle.
The new aspect is a priced choice, not a physical prediction.

The necessary next task is to derive an interacting end/gauge/superfield
law and match an actual parent/core/source configuration, then compute
the normalizable spectrum and anomalies of that ONE theory. No new
identification ledger status, SM value or TOE completion is claimed.
