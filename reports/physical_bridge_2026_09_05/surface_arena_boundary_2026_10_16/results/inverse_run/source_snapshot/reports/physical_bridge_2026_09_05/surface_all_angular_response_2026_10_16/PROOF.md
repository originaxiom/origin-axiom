# All angular regular solutions and field dependent boundary work

Authored conditional local proof, before execution. The parent/root/
metric/holonomy/background and critical choice are supplied, not derived
from OA. No independent analytic acceptance, complete curved boundary
action or observed physical spectrum is asserted.

## 1 Complete noncritical angular splitting

Keep the EXACT prior source matrix family

 f_x+[C/x+Y/(1-x^2)+x D/(1-x^2)+beta x A]f=0.

Write j=n+l/4, l=etaR, n!=0. For each simultaneous R,B eigenvector,
C=B[2n+(l+R)/2]. For sign(n)=e and m=|n|>=1, e B C has eigenvalues
2m+e(l+R)/2, all >=2m-1>=1. Thus no critical root occurs here.
The integrable plane is G=(I-eB)/2; its complement is H=I-G.
Both have half the block dimension. Their positive exponents alpha
are the eigenvalues of -C on G, with pairwise differences at most1.
Y flips B, so G Y G=0. All statements are checked for symbolic m
and every actual matrix type, BOTH signs of n and W, not sampled n.
The actual normal current V anticommutes with C,D,Y,A; A^2=4I,
||D||<=2, ||Y||<=2sqrt2<3. Preserve zero-Yukawa Cartan blocks.

## 2 All order analytic regular basis and controlled tails

For each unit stable seed e_a with C e_a=-alpha e_a set

 f=x^alpha sum_(k>=0) b_k x^k, b_0=e_a,
 (C+(alpha+k)I)b_k=-sum_(h=0)^(k-1) V_h b_(k-1-h),

where V_even=Y, V_1=D+beta A and V_odd>=3=D.
The only possible regular resonance is k=1 when another stable
exponent is alpha+1. Its forcing is the projection of Y e_a onto G,
which is ZERO. Set that free resonant coefficient0; the other larger-
exponent seed is retained independently. Do not divide a zero by zero.
For k>=2 all inverse entries have absolute value<=1/(k-1). There is
therefore NO logarithm needed in these L2 regular series. This is an
earned source-coupling fact, NOT permission to remove the n=0log branch.

Reference instead multiplies the exact equation by x(1-x^2):

 (C+(alpha+k)I)b_k+Y b_(k-1)
  +[D-C-(alpha+k-2)I+beta A]b_(k-2)-beta A b_(k-4)=0.

Negative suffixes mean0. Four nontrivial orders are compared exactly
for symbolic m,beta in every actual seed, including the resonant zero.
Adding a stable-stable Y vertex gives nonzero resonant forcing and
fails the construction: the vanishing compatibility is not a convention.

For convergence choose integer M>=3+2|beta|. With B_k=||b_k||,
S_k=sum_(h=0)^k B_h, B_1<=M and for k>=2

 B_k<=M S_(k-1)/(k-1),
 S_k<=(1+M) product_(h=1)^(k-1)(1+M/h)
     =(1+M) binom(k+M-1,M).

This grows polynomially in k; every series and its derivative converge
on compact subsets of |x|<1, uniformly in angular m for the reduced
coefficient series. The seed factor x^alpha is retained, not erased.
After orderN>=1 a valid absolute tail bound is

 x^alpha(1+M)[x/(1-x)^(M+1)
                    -sum_(k=1)^N binom(k+M-1,M)x^k].

Thus the solution is a CONVERGENT representation at every finite beta
and cutx<1, not merely four verified jets. It is not an interval-
evaluated numeric response matrix or a uniform full-frequency symbol.
Distinct stable leading coefficients give independent solutions.

## 3 Completeness in the actual local L2 space

It remains to rule out unbounded-but-L2 solutions, not assume them away.
Choose0<a<=1/4 and put M0=4+2|beta|a. The remaining coefficient
W=Y/(1-x^2)+xD/(1-x^2)+beta x A has ||W||<=M0. For bounded
continuous f define the two-ended integral system, fixing G f(a)=u:

 H f(x)=-x^(-C_H) integral_0^x y^(C_H) H W(y)f(y)dy,
 G f(x)=(x/a)^(-C_G)u
            +x^(-C_G)integral_x^a y^(C_G)G W(y)f(y)dy.

It has the exact sign of the original first-order equation. On the
weighted supremum norm sup x^(-1/2)||f(x)||, the two operators have
bounds(2/5)a M0 and(1/2)a M0. The second follows by maximizing
2sqrt(z)(1-sqrt(z))<=1/2 for z=x/a. Their sum<q=a M0. Choose q<1;
this choice exists for every finite beta, UNIFORMLY in angular m.

For L2(x dx), conjugate by f->sqrt(x)f. Scalar bounds for the bad/good
kernels are sqrt(y/x) on y<x and(x/y)^(3/2) on x<y. Their squared
Hilbert-Schmidt integrals are a^2/4 and a^2/8. This bounds the operator
norm even for vector f by applying the scalar kernel to ||f||, so no
hidden coefficient-dimension factor. The sum< a M0=q there as well.

Every L2 solution obeys the integral system. For a bad exponent d>=1,
y^d Wf is integrable at0 by Cauchy-Schwarz with x dx; x^d f has a
limit. A nonzero limiting constant would give the excluded x^(-d)
term; its remaining integral is bounded by M0||f||_(0,x)/sqrt(2d),
which tends to0. Hence its constant is0. The good equation follows
from its value at a. Contraction in L2 proves uniqueness for each u.
The weighted-continuous solution is in L2 and has the same u, so it
is that solution. This proves ALL local L2 solutions belong to the
half-dimensional constructed family, including the analytic series.

The limiting Green current is0, since the constructed solutions are
O(sqrt(x)). Conservation makes their finite-cut plane maximal current-
null. At the small cut it is a graph over G, with

 ||H f(a)|| <= q/[(2m+1/2)(1-q)] ||u||.

That is an ANGULAR-uniform small-cut graph bound at each finite beta,
not uniform joint high horizontal/angular frequency at a fixed radius.
The starting radius still depends on beta. Continuation to x<1 exists,
but does not preserve this numerical angle bound automatically.
Together with the SAME parent's n=0 theorem, the result constructs
response for EVERY shifted angular integer. No physical count follows.

## 4 Actual first order boundary variation

Use physical t=sqrt(r), x=gt, beta=rho/g^2. Fix t,rho and vary log g:
delta f=(x partial_x-2beta partial_beta)f, not x partial_x f alone.
The true coefficient variation divided by g is

 Gg=Kx+x partial_x Kx-2beta partial_beta Kx
   =2x D/(1-x^2)^2+(1+x^2)Y/(1-x^2)^2.

The indicial and horizontal coefficients cancel. Holding beta fixed
would instead add2beta x A and change physical momentum; the control
rejects that substitution. All28actual matrices retain the cancellation.

For any admitted infinitesimal coefficient variation dK with fixed
normal V and indicial trace plane, the varied equation gives exactly

 d_x(F^dagger V dF)=-F^dagger V dK F,
 [F^dagger V dF]_inner^outer=-integral F^dagger V dK F dx.

Keep BOTH endpoint orientations. For the fixed supplied sigma law and
these regular/background parameter variations, the inner current limit
is0. This is not generally0 if the trace plane, normal or holonomy is
varied. The untraced identity, not just its trace, is required.

This is a FIRST-ORDER normal action identity. In the rescaled source
inner product with measure2x dx/g^2, the radial expression is
-i g^2 V(derivative_x+Kx)/(2x); the weight cancels in its polarized
action. With the common supplied parent normalization, the complex-
coefficient Hermitian quadratic functional has density

 -i/2(f^dagger V f'-f'^dagger V f)-i f^dagger V Kx f.

Its boundary variation is -i/2[f^dagger V df-df^dagger V f]_inner^outer.
The mixed current identity above is its on-shell variation with
background, not a squared-norm replacement. Majorana/Grassmann doubling,
full nonlinear bosonic/source/SUSY functional and quantum determinant
phase are NOT fixed by this polarized coefficient identity alone.

## 5 Exact nonzero boundary work and the regular partner

At beta=0 use the preceding canonical critical bases Fplus=(v,regular),
Fminus=(log-critical,regular), with their declared dimensionless seed
normalization. Exact log(g) boundary work at fixed physical t is

 Fplus^dagger V (x partial_x Fplus)
    =ell x^2/(1-x^2)^2 [[0,1],[-1,0]], ell=1 or sqrt2;
 Fminus^dagger V (x partial_x Fminus)=0.

The positive-plane matrix has rank2 despite TRACE ZERO. Multiplication
by -i is Hermitian. Both columns separately have zero diagonal work;
discarding the regular partner or checking only a trace would miss the
nonzero response. Rescaling seed coordinates changes entries by the
expected congruence, not an observed coupling or vacuum prediction.
Its derivative equals minus the exact untraced bulk variation density;
the inner limit is0. This ties the field-dependent plane to the same
first-order source action and retains both-end work. The other plane
is not killed by its zero work on this particular one-parameter family.

All-mode local response and this partial action variation are NOT the
complete physical boundary law. The moving/curved normal, spin/R and
extrinsic/gauge compensation, arbitrary interacting bosonic/auxiliary/
source/SUSY boundary equations, varying cusp radius/singular graph and
uniform exterior join remain. Then global root/holonomy/stationary
charged spectrum/norms/vertices/anomalies and whole extra-field roster
must be computed in ONE theory. Existing other-parent mass/conditional-
three results are preserved, not spliced. Foundational SM/three/observed
parameters and gravity remain the unchanged ultimate objective.
