# F04 authored argument: positive flag flux in the full coefficient bundle

This pre-execution candidate is an authored proof with exact controls, not
an independently reviewed theorem or a claim of novelty in the literature.
The assumptions and symbols are fixed in DESIGN. Laplacians have convention
Delta=div grad. The source has exactly one cusp and no finite-distance
boundary, singularity or additional current.

## 1. The flag and its actual cusp action

The normalized symmetric cube of the two upper-triangular rho generators,
multiplied by chi, is upper triangular with all diagonal entries of modulus
one. Hence the entire image preserves the standard full flag and has
unit-modulus diagonal characters. The regular unipotent V(b) has
ranks (V(b)-I)^j=(3,2,1,0); its kernels give the same flag. This is data of
the coefficient system, not a flag chosen to fit a desired metric.

In the fixed normalization,

    V(mu)=exp(-J),   V(lambda)=exp(J),
    J_12=sqrt(3), J_23=2, J_34=sqrt(3),   J^4=0.       (1)

All other J entries are zero. These finite polynomial exponentials are
checked from the marked words, not inferred from the desired period.

## 2. Remove the central factor without assuming finite energy

On the universal cover use a flat frame. For a positive Hermitian matrix H
the symmetric-space metric is Tr((H^-1 dH)^2), with cotangent indices
contracted against the source metric. Its harmonic equation is

    div(H^-1 dH)=0,
    equivalently Delta H=sum_alpha H_alpha H^-1 H_alpha.  (2)

Here alpha denotes a source orthonormal frame; the Laplacian includes its
Levi-Civita correction. One can also obtain (2) from D=d=A+Psi, with
A=(1/2)H^-1 dH and Psi=-(1/2)H^-1 dH: the same-index commutator in
d_A^*Psi vanishes. Compactly supported variations suffice; infinite total
energy does not obstruct the local equation.

Let w=log det H. Since |det V(gamma)|=1, w descends to M. Taking the trace
in (2) gives Delta w=0. Define H0=exp(-w/4)H. Direct differentiation gives

    H0^-1 dH0=H^-1 dH-(dw/4)I.                         (3)

Consequently H0 is again harmonic and equivariant, and det H0=1. No energy
or growth assumption on w was used. Henceforth H means H0. The simple-root
quantities below are unchanged by the normalization. A rapidly varying
central scale cannot alter the trace-free inequality.

## 3. Coordinates covering every positive determinant-one metric

Unique triangular factorization gives

    H=N^dagger D N,  D=diag(exp(t_1),...,exp(t_4)),
    N upper unitriangular,  t_i real,  sum_i t_i=0.     (4)

There are three independent real t_i and six independent complex entries
of N: all 15 real metric degrees of freedom are included. No principal
SL2 restriction or diagonal-metric ansatz has been imposed.

Write b_r=log det H_[1:r,1:r]=sum_(i<=r)t_i, r=1,2,3,
and b_0=b_4=0. Upper triangularity of V and unit diagonal moduli make every
b_r, hence every t_i, globally defined. More explicitly, with delta the
diagonal of V(gamma), the equivariance rule gives

    D(gamma x)=D(x),   N(gamma x)=delta N(x)V(gamma)^-1. (5)

This follows by substituting in (4), using delta^dagger D delta=D, and
uniqueness of the unitriangular factor. In particular, on the two peripheral
generators delta=I. For n_i=N_(i,i+1) and a=(sqrt(3),2,sqrt(3)), (1) implies

    n_i(x+e1)=n_i(x)+a_i,
    n_i(x+e2)=n_i(x)-a_i,
    n_i=a_i(x1-x2)+periodic function.                 (6)

Other entries may have nonlinear transformation laws; none are set to zero.

## 4. Derive the full metric and its positive flag equations

Put theta=dN N^-1 (RIGHT Maurer--Cartan form). Conjugating the matrix
one-form H^-1dH by N yields

    D^-1dD + D^-1 theta^dagger D + theta.

Taking the trace of its square gives exactly

    |dH|_X^2=sum_i |dt_i|^2
           +2 sum_(i<j) exp(t_i-t_j)|theta_ij|^2.     (7)

The simple-root entries of theta are dn_i. Higher entries contain the
usual products of N and dN. In particular replacing theta by N^-1dN in
(7) is not valid; the nontrivial-N countercontrol tests this distinction.

The half-energy density is one half of the diagonal term in (7) plus the
sum of root terms. Varying t_i while holding all entries of N free and fixed
in that variation gives the necessary equations

    Delta t_i = sum_(j>i) exp(t_i-t_j)|theta_ij|^2
              -sum_(k<i) exp(t_k-t_i)|theta_ki|^2.     (8)

The determinant constraint adds no multiplier: both sides summed over i
vanish. These are necessary equations for a full harmonic metric, not a
claim that its independent off-diagonal equations have been solved.
Summing (8) through r cancels internal roots and leaves

    Delta b_r=q_r,
    q_r=sum_(i<=r<j) exp(t_i-t_j)|theta_ij|^2 >=0.     (9)

These densities are globally defined (also evident from Delta b_r). In
the sum q=sum_r q_r each root term has multiplicity j-i; higher roots
cannot cancel the positive simple-root terms.

## 5. Compact-core flux forces the mean upward

Use the fixed h0 torus average, denoted by a bar, and set
L=bar b_1+bar b_2+bar b_3. Compact truncations M_R give

    A0 exp(-2R)L'(R)=Q(R),   Q(R)=integral_(M_R) q.   (10)

The periods (6) imply q is positive somewhere. Choose any R0 containing
positive mass Q0=Q(R0)>0. Nonnegativity and (10) imply, for r>=R0,

    L'(r)>=Q0 exp(2r)/A0,
    L(r)>=L(R0)+Q0/(2A0)*(exp(2r)-exp(2R0)).          (11)

Thus L is eventually positive and increasing. This is only Stokes on
compact domains; no total-energy integrability or condition at infinity
has been inserted. Extra cusps, sources or inner boundaries would change
(10) and are not covered by this theorem.

## 6. The Cartan-weighted peripheral inequality

Define h_i=t_i-t_(i+1)=2b_i-b_(i-1)-b_(i+1). Thus h=C b, where C is the
A3 Cartan matrix. The positive vector

    v=C^-1(1,1,1)^T=(3/2,2,3/2),  sum_i v_i=5        (12)

satisfies v dot h=sum b. Define the downward torus oscillations
Omega_i=bar h_i-min_T h_i>=0 and W=sum_i v_i Omega_i. Every quantity in
this definition is allowed to vary with r.

From (6), orthogonality of a constant covector to derivatives of periodic
functions on the flat torus gives

    average |d_T n_i|^2_(h0) >= a_i^2 K,
    (a_1^2,a_2^2,a_3^2)=(3,4,3),  K>0.             (13)

Average (9), discard nonnegative higher-root and radial contributions,
and bound each exp(h_i) by its minimum. The cusp Laplacian then gives

    L''-2L' >= exp(2r) sum_i a_i^2 K
                         *exp(bar h_i-Omega_i).     (14)

Let alpha_i=v_i/5=(3/10,2/5,3/10). The coefficients satisfy
a_i^2 K/alpha_i=10K. Weighted AM-GM, or convexity of exp, yields

    sum_i a_i^2 K exp(z_i) >=10K exp(sum_i alpha_i z_i).

Using (12), equation (14) becomes the full rank-four bound

    L''-2L' >=10K exp(2r+(L-W)/5).                  (15)

This conclusion did not set the mixing coordinates to their induced
rank-two values. Their extra terms have the right sign to be dropped.
It also did not replace a minimum by a mean; that unjustified replacement
is refuted by the smooth countercontrol in F03 section 5.

## 7. What is excluded, and what is not

If limsup W/L<1, there are epsilon>0 and r1 with L-W>=epsilon L for every
r>=r1. With L'>0, (15) implies

    L''>=10K exp(2r1)*exp((epsilon/5)L).

For any u'>0 and u''>=kappa exp(pu), kappa,p>0, multiplication by 2u'
gives u'^2>=u_0'^2+(2kappa/p)(exp(pu)-exp(pu0)). Integration bounds its
lifetime by pi exp(-p*u0/2)/sqrt(2*kappa*p), contradicting existence on
a full half-line. This elementary comparison and its exact solution
were supplied in F03 section 3, which is reused, not replaced.

Therefore EVERY hypothetical global full rank-four harmonic metric here
must satisfy

    limsup W/L >=1,
    limsup exp(-2r) W(r) >= Q0/(2A0)>0.             (16)

The second bound follows on a sequence approaching the first limsup, using
(11). It holds for each fixed positive Q0. In particular W=o(exp(2r)) is
excluded, including bounded or polynomial angular root-height oscillation.
These are sequential necessary bounds, not asymptotic solutions or uniform
lower bounds on every high torus.

For an additional geometric cost, (7) implies |dh_i|<=sqrt(2)|dH|_X.
Shortest paths in the reference torus give
Omega_i<=sqrt(2)D0 exp(-r) sup_T |dH|_X. Summing the weights in (12),

    limsup exp(-3r) sup_T |dH|_X
                 >=Q0/(10 sqrt(2) A0 D0)>0.         (17)

The norm here is explicitly the trace symmetric-space norm (7), not a
physical energy density with an unproved normalization. It applies to the
determinant-normalized metric; the original has at least that norm, since
the central and trace-free currents are orthogonal. No gravitational or
UV exclusion is inferred solely from this growth.

Constant upper-triangular changes of the fixed flag frame shift flag heights
and simple-root heights by constants. They leave Omega_i unchanged and do
not affect the limsup/exclusion class. Constants K in (15) refer to the
explicit marked normalized frame; there is no claim of a frame-independent
numerical physical coupling.

## 8. Positive local solution and failure boundaries

The old local cusp is still a solution in the full bundle. Set

    b=-r+(1/2)log(2/K),  z=-x1+x2,
    (t_1,t_2,t_3,t_4)=(3b,b,-b,-3b),
    N=exp(-zJ).

Then theta=-J dz, the flag heights are (3b,4b,3b), q_r=(6,8,6),
L=10b, W=0, and both sides of (15) equal 20. The full matrix harmonic
equation (not only the diagonal equations) is among the exact controls.
The outer flux in (10) is -10 A0 exp(-2R), not positive. On a local slab
its inner boundary contributes +10 A0 and balances the bulk source.
This preserves the local positive; it is not a global source-free example.

With J=0 there are local diagonal harmonic profiles proportional to
exp(2r), so a rank-four label alone supplies no obstruction. Conversely,
generic D and N in (4) do not obey the induced ratios above, but equations
(7)--(15) still apply to them.

F04 does NOT exclude W growing as required in (16), and does not establish
existence in that class. It does NOT exclude coupled equations with a
representation-valued source or a different base/action. It does NOT turn
the exact algebraic I(V)=1 into a physical L2 chiral index. Neither
semisimplification nor an arbitrary averaging prescription is an allowed
substitute for that coefficient system.

The concrete advance beyond F03 is removal of the induced-rank-two metric
assumption. The remaining physical decision is whether the actual parent
action permits the required angular behavior or instead supplies a
compensating current, and then whether that same background has the correct
normalizable spectrum, anomalies, interactions and gravitational dynamics.
