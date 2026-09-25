# R46 authored canonical-background interaction argument

This is a scoped mathematical application with named external inputs,
not independent PDE verification or a derived physical parent. R42/R44
provide the actual smooth complete canonical background and its all-jet
end control. R45 supplies the actual E8 branching and complete domains.
F13's exact six calculation is a separately reproduced input; its
hyperbolic metric estimates are NOT transferred onto this metric.

## 1. The shrinking cycle supplies the missing decay

In R44's moving frame F the positive coefficient norm is uniformly
comparable to Euclidean and the actual Blaschke base satisfies

    h asymp dR^2/R^2 + dx^2/R + dt^2,
    dvol asymp R^(-3/2) dR dx dt.

For E_chi, write T_x=partial_x+N/sqrt(R). Sections obey a scalar
quasiperiodic condition with phase chi (using chi^-1 instead changes
the sign of the shifted lattice and none of the estimates). For chi!=1,
every frequency has |omega|>=delta_chi>0. Since N^3=0,

    T_x^-1=(i omega)^-1 I -(i omega)^-2 N/sqrt(R)
                          +(i omega)^-3 N^2/R.                 (1)

The dual uses -N^T. The induced six has nilpotence degree at most three,
so the same terminating series works if its OWN scalar twist is nontrivial.
Uniform Parseval bounds in the comparison norms transfer to the actual
x,t-dependent metric by two-sided norm equivalence. In every exterior
degree the contraction i_x has norm at most C/sqrt(R). Hence

    K_x=i_x T_x^-1,       ||K_x||_(R>R0)<=C/sqrt(R0).           (2)

The constants may depend on fixed q and chi. The radial identity
partial_R Bx+[BR,Bx]=0, and [Bt,Bx]=0, imply [d_B,T_x]=0.
Together with {d_B,i_x}=T_x this gives d_B K_x+K_x d_B=I on the
FULL end complex, not only on each torus. K_x preserves radial support.
On maximal graph domains it extends distributionally, as in R44.
For chi=1 and omega=0, Bx is singular and (1) does not exist.
All exceptional defining/dual characters (-1,+i,-i) avoid that case.
At p14 the six character is -1; at p34 it is +1 and (2) is not asserted
for the six. Covers on which the phase becomes trivial also require
a separate argument. This is not a whole-parent confinement theorem.

## 2. Complete-domain coercivity and charged decay

Let Q=d_B+d_B^dagger and q_B(v)=||Qv||^2 on the complete graph domain.
R44/R45 establish minimal=maximal domains using complete cutoffs;
no end boundary condition is silently installed. Pair the homotopy
identity with a form supported above R0. Integration by parts gives

    ||v|| <= C R0^(-1/2)(||d_Bv||+||d_B^dagger v||),
    q_B(v)>=c R0 ||v||^2.                                  (3)

Put z=sqrt(R), a notation for height, NOT the old hyperbolic metric.
The metric has |dz|^2<=C z^2. A dyadic partition in z with sum eta_j^2=1
has uniformly bounded gradients. The Dirac commutator is Clifford
multiplication c(df)=epsilon(df)-iota(df); thus the IMS identity is

    sum q_B(eta_j v)=q_B(v)+integral sum |d eta_j|^2 |v|^2.

Apply (3) on each annulus and enlarge the starting height to absorb
the bounded last term. This proves on a sufficiently deep tail

    integral z^2 |v|^2 <= A q_B(v).                         (4)

It also proves compactness of the graph-domain inclusion in L2 for
THESE nontrivially twisted coefficients: (3) makes bounded graph-norm
tails uniformly small, and elliptic Rellich compactness handles the
compact core. Q has compact resolvent there. No such claim is made
for the full parent, its neutral sector, or the p34 six by this proof.

For an L2 harmonic form alpha use f_T=eta exp(epsilon min(z,T)).
For fixed T this bounded Lipschitz multiplier preserves the complete
domain. Q(f_T alpha)=c(df_T)alpha. Inequality (4) and
|d exp(epsilon z)|^2<=C epsilon^2 z^2 exp(2 epsilon z) give

    integral z^2 f_T^2 |alpha|^2
      <=2AC epsilon^2 integral z^2 f_T^2 |alpha|^2+C_eta.

Choose epsilon>0 small and take T to infinity. Consequently
integral z^2 exp(2 epsilon z)|alpha|^2 is finite. This uses the canonical
gradient/volume, not F13's former-base exponential by analogy.

Weighted L2 alone is insufficient on a collapsing end. At height R_p
take an embedded ball of radius b/sqrt(R_p), with fixed small b.
The R44 two-sided metric bounds give this injectivity scale: any deck
displacement in the period rectangle costs at least this order; leaving
a fixed relative radial band costs a fixed positive distance. Its doubled
ball can be lifted to the normalized pointed projective chart used in
R44 section 4. There the normalized domains and every finite jet of the
Cheng--Yau solution converge uniformly to the positive product-cone
solution. In a constant normalized flat frame both base and coefficient
metrics therefore have uniform local smooth bounds, also after the
additional small-ball rescaling. This is stronger than C0 equivalence;
it uses precisely R44's cited Benoist--Hulin all-jet theorem. Induced
dual/exterior metrics inherit these bounds. Standard local elliptic
estimates for Q then yield

    |alpha(p)| <= C R_p^(3/4) ||alpha||_(L2(ball))
               <= C' R_p^(3/4) exp(-epsilon sqrt(R_p)).      (5)

Height sqrt(R) varies by a bounded amount on this ball, since
|d sqrt(R)|<=C sqrt(R). The extra weighted-L2 power was harmlessly
dropped in (5). Compact-core regularity completes boundedness.
Thus every exceptional defining/dual harmonic form is in L-infinity
and in Lp for all p>=2, in particular L4. Neither finite volume nor
normalizability alone proves this: the scalar function R^(3/16) is
L2 but not L4 for the canonical density R^(-3/2)dR.

## 3. The actual six is gapped on this metric

W=exterior^2 E_chi is the coefficient of (10,6) in the supplied parent,
not an independently twisted six. F13's exact two-generator complex is
B:C6->C12, J:C12->C6. Its pre-existing witness claims are:

| locus | actual six character | rank B, rank J | B and J minors modulo p |
|---|---|---|---|
| q^2-14q+1 | -1 | 6,6 | 64; 24064 |
| q^2-34q+1 | +1 | 6,6 | -18q-18; 2822400-80640q |

Rerun those sources unchanged, including independent affine composition,
relation/JB checks, both field embeddings, opposite-character and trivial
coefficient controls. Conditional on their successful reception, H1(W)=0.
No defining/dual exceptional rank is re-counted here.

R45 supplies the six's NONZERO longitude weights +/-2, a bounded full-end
homotopy on the actual canonical norm, closed ranges and
H_L2^1(W)=H_c^1(W)=H^1(W). Combining these yields a positive spectral
gap delta_W>0 on its complete one-form Laplacian. Compact resolvent is
NOT needed for this deduction: the exterior coercive bound plus compact
core gives Fredholmness at zero; the exact calculation removes the kernel.
The p34 trivial meridian twist does not break this longitude argument.
No numerical lower bound, uniform-q bound or full parent mass gap follows.

## 4. Spend the result in the supplied action, not a new model

The source is Braun et al., 1812.06072v2, (2.9)--(2.18), (B.12)--(B.14):
https://arxiv.org/html/1812.06072v2 . It remains an external choice.
In form norms V=2/g7^2 (||F_C||^2+||mu||^2), C=A+Psi, mu=delta_A Psi.
This is a residual-square potential, distinct from Higgs energy.
The canonical background solves both residual equations. For u=a+psi,

    F(C+u)=d_Cu+u wedge u,
    mu(C+u)=M(u)-sum[a_i,psi_i],
    M(u)=delta_A psi+sum[Psi_i,a_i],
    G(u)=delta_A a+sum[Psi_i,psi_i].

The real orthogonal split of d_C^dagger u is G+M. Adding the compact
background-gauge term 2||G||^2/g7^2 gives quadratic Taylor potential
2/g7^2(||d_Cu||^2+||d_C^dagger u||^2). With the source's scalar kinetic
normalization this is the operator 2 Delta, not an arbitrary mass fit.
F13's first-jet/sign/normalization tests are rerun; they are finite controls
on a generally derived identity, not a whole-parent propagator audit.

The sufficient nonlinear space X=Dom(Q) intersect L4 has norm
||u||_2+||Qu||_2+||u||_4. The compact-invariant bracket obeys uniform
pointwise bounds, so both nonlinear residuals lie in L2 and V is a
finite C1 polynomial on X. Complete cutoffs and local elliptic smoothing
give compact smooth approximants in the graph and L4 norms; no end flux
survives in this chosen class. Equation (5) puts the earned charged
zero modes in X. This is not selection of a unique physical end law.

For charged profiles alpha,beta the actual parent volume/exterior and
Spin(10) contraction has J=*(alpha wedge beta) in the appropriate six
(or its determinant-one volume-dual). Holder gives
||J||_2<=C||alpha||_4||beta||_4. The positive Euclidean scalar-block
response is therefore well-defined and finite:

    0<=<J,(p^2+2 Delta_W)^-1 J>
       <=||J||_2^2/(p^2+2 delta_W),             p^2>=0.       (6)

This establishes an admissible channel on the SAME finite-Higgs-energy
canonical background, not a nonzero or asymmetric interaction.
A nonzero decomposable profile can have zero self-source. Actual J,
normalized response tensors, base-isometry plus duality constraints,
gauge-vector/ghost/Ward completion and quantum phases require more work.
The paired modes do not become chiral because an inverse exists.

## 5. Boundaries of the result

The neutral/adjoint global H1 and q-variation kinetic norm remain live;
trivial meridian characters are not covered by (1)--(5). F13's uniqueness
on its former fixed hyperbolic base is not rebranded as uniqueness or
selection of the canonical geometry. The supplied parent, exceptional
q and twist, SM breaking, physical chiral spectrum, anomaly/end completion,
scales, gravity and TOE remain separate obligations. R40/R41's noncentral
source route stays registered. Finite test success does not independently
certify R42/R44's global hypotheses or this authored analytic argument.
