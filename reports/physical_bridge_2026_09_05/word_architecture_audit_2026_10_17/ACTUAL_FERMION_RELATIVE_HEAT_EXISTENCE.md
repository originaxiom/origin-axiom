# Relative heat existence for the specified parallel-phase fermion operator

October 27, 2026. UNREVIEWED author proof, conditional on the specified
curved-action/parallel-phase construction and its complete graph realization.
No scientific execution, numerical determinant, gauge threshold value or
independent acceptance. This supplies an analytic successor to the sufficient
hypotheses in RELATIVE_HEAT_ADMISSION_AND_SCALE_DEPENDENCE.md. It does not
replace the physical spin/ghost measure by a fermion-only answer.

## 1. Quantifier and recovered source data

For each FIXED smooth compactly supported flat Y connection C in the
stationary parallel SM gauge phase, and each FIXED charge sector of its
full doubled physical fermion operator, compare D_q with D_0 on the same
complete surface, Hermitian bundle and Hilbert space. Here q labels the
charge coupled to C, not a newly chosen mass. The source is
weave_sm_parallel_2026_10_08/PROOF.md, with its actual action and fermion
map in weave_curved_action and weave_physical_mass, personally reread.
All four Weyl slots, their adjoints and every angular channel are retained.

The source supplies the following data, rather than a scalar proxy:

* D_q is the symmetric doubled mass operator on its complete graph closure;
  its first-order principal symbol has bounded propagation speed in the
  actual metric. The normalized derivative maps in the source have bounded
  orthonormal coefficients; the spin and Higgs terms are zeroth order.
* D_q=D_0+K_q, where K_q is a smooth Hermitian endomorphism supported in a
  fixed compact set. It is the actual minimal-coupling change due to C.
  The flat line is represented on the same topologically trivial line;
  no changed domain or singular transition is introduced.
* The source's complete square has essential spectrum starting at 1/4.
  Smooth compact-core Wilson changes preserve this gap and Fredholmness.
  Individual light multiplicities are NOT supplied by this statement.
* Locally C=df. The scalar unitary gauge change exp(i q f) conjugates the
  entire charged-sector operator to its untwisted counterpart, including
  its spin, structure connection and Higgs terms. It commutes with those
  structure terms. The sign of the exponential follows the source's
  covariant-derivative convention and does not affect the conjugacy claim.

The complete finite-area cusp has no uniform positive injectivity radius.
The argument below does not assume one. It uses compact-set elliptic
regularity and finite propagation of the actual first-order operators.
The root system, metric, spin line, action, background and Wilson family
remain supplied inputs. This is a conditional-model theorem, not a
foundational selection of them.

## 2. Compactly localized heat is trace class

Put P_j=D_j^2>=0. For any smooth compactly supported scalar cutoff chi
and integer m with 2m>dim Sigma, local elliptic estimates give a bounded
map

  chi(P_j+1)^(-m): L2 -> H^(2m)(K),                       (1)

with support in the interior of a fixed compact smooth region K. One
obtains (1) by iterating interior elliptic estimates on nested compact
neighborhoods; (P_j+1)^(-m) controls P_j^r for 0<=r<=m by the spectral
theorem. Extend the compactly supported output to a closed double of K.
The Sobolev inclusion H^(2m)->L2 on that closed two-dimensional manifold
has singular values O(n^(-2m/dim Sigma)), a summable sequence. Consequently
chi(P_j+1)^(-m) is trace class as an operator into the original L2 space.
The double is an auxiliary factorization, not a physical boundary.

By spectral calculus,

  chi exp(-tP_j)
    =chi(P_j+1)^(-m) (P_j+1)^m exp(-tP_j)                 (2)

is trace class for every t>0, with trace norm locally uniformly bounded
in t away from zero. Its adjoint exp(-tP_j)chi is trace class too.
No ordinary unlocalized heat trace was assumed finite.

For any first-order differential operator V supported in a compact
region, the local first-order elliptic estimate for D_j also gives

  ||V exp(-uP_j)|| <= A(1+u^(-1/2)),                     (3)

since ||D_j exp(-uD_j^2)|| <= const u^(-1/2). Apply the same estimate
to V dagger to bound exp(-uP_j)V. Constants may depend on the compact
region, charge, background and operator. No uniform claim over a
degenerating metric or Wilson family is made.

## 3. The relative heat OPERATOR is trace class

K_q maps Dom D_0 continuously into itself by the compact-set elliptic
estimate. Thus Dom D_q=Dom D_0 and Dom P_q=Dom P_0: for f in the first
domain, D_q f=D_0 f+K_q f belongs to it exactly when D_0 f does.
On this common square domain,

  V=P_q-P_0=D_0 K_q+K_q D_0+K_q^2                       (4)

is first order with compact support. Choose chi=1 on a neighborhood of
all its coefficients. Then V=chi V=V chi, including the differentiated
cutoff term, because d chi vanishes on that neighborhood.

Duhamel's identity is

  exp(-tP_q)-exp(-tP_0)
    =-integral_0^t exp(-(t-u)P_q)V exp(-uP_0) du.          (5)

For 0<u<=t/2, factor the integrand as

  [exp(-(t-u)P_q)chi] [V exp(-uP_0)].

The first factor has uniformly bounded trace norm by (2), and the second
has norm bounded by A(1+u^(-1/2)) by (3). For t/2<=u<t use instead

  [exp(-(t-u)P_q)V] [chi exp(-uP_0)].

The trace norm is bounded by A_t(1+(t-u)^(-1/2)). Both endpoint bounds
are integrable. Hence (5) is a trace-norm Bochner integral. The usual
weak Duhamel identity on smooth vectors, followed by these bounds and
density, identifies it with the actual semigroup difference. In particular

  exp(-tP_q)-exp(-tP_0) is trace class, t>0.               (6)

Its trace norm is uniformly bounded for t in any compact subinterval
of (0,infinity). This proves more than integrability of a diagonal
supertrace and does not use graded cancellation.

## 4. Global small-time cancellation without a cusp volume estimate

On a compact region, local heat asymptotics are uniform. Local unitary
conjugacy makes every fibre-traced heat coefficient equal for P_q,P_0.
Thus the integral of their diagonal trace difference over any fixed
compact region is O(t^N) for every N.

To control its complement, choose a scalar psi supported where P_q=P_0,
zero near the core perturbation, and equal to one sufficiently far in
the cusp. Its derivative support Z is compact. Choose a farther tail W
at positive propagation distance rho from a small neighborhood of Z.
There is an exact operator identity

  exp(-tP_q)psi-psi exp(-tP_0)
    =-integral_0^t exp(-(t-u)P_q)[P_0,psi]exp(-uP_0) du.   (7)

For x=y in W, its left kernel is exactly the relative diagonal kernel.
The commutator on the right is first order supported in Z. The
compact-to-separated-region L2 heat-kernel estimates for D_j^2, including
one derivative at z in Z, have the form

  ||A_z K_j(u,z,.)||_(L2(W)) <= B u^(-M) exp(-c rho^2/u), (8)

for fixed positive c and finite M, uniformly for z in Z and small u.
These follow from bounded wave propagation, the Gaussian Fourier
transform of exp(-u D_j^2), and local elliptic estimates at Z. In
particular the constants do not require global bounded geometry at W.

Use kernel self-adjointness to place the compact variable of the first
factor at z. Cauchy-Schwarz in x over the ENTIRE W and integration in
z over Z bound the absolute integrated relative diagonal from (7) by

  B' integral_0^t (u(t-u))^(-M')
       exp[-c' rho^2/u-c' rho^2/(t-u)] du.                (9)

The exponent suppresses both endpoints; (9) is O(t^N) for every N.
This integrated L2 argument already includes the whole collapsing cusp,
rather than multiplying an unjustified uniform pointwise bound by its
volume. Together with the compact-region result it proves

  r_q(t)=Tr(exp(-tP_q)-exp(-tP_0))=O(t^N), all N.         (10)

For completeness the trace is the integral used here: compress the
trace-class operator (6) by exhausting compact cutoffs. The compressed
traces are their smoothing diagonal integrals. Strong cutoff convergence
implies convergence in trace norm after multiplication by a trace-class
operator; absolute integrability from (7)-(9) identifies the limit with
the full diagonal integral. No cyclicity of a divergent trace is used.

Personally checked Lesch, dg-ga/9607005, III: Lemma3.1.9;
Definition3.2.1 and Corollary3.2.6; Propositions3.3.1-3.3.4; and the
complete Section3.4. Its compact-to-far L2 estimates support (8).
Theorem3.4.3 controls relative diagonal tails; it is not substituted for
the operator trace-class proof (1)-(6). No full-book reading claimed.
Primary: https://arxiv.org/pdf/dg-ga/9607005 (access October27).

## 5. The actual spectral gap supplies the large-time condition

For fixed q, Fredholmness gives finite-rank kernel projection H_q and
a positive gap delta_q on its orthogonal complement. It need NOT equal
the essential threshold 1/4: there may be smaller positive core modes.
The same holds at q=0. Set

  A=exp(-P_q)-H_q, B=exp(-P_0)-H_0.

Their operator norms are at most r<1. By (6), A-B is trace class.
For integer n>=1 the noncommutative telescoping identity gives

  A^n-B^n=sum_(k=0)^(n-1) A^k(A-B)B^(n-1-k),
  ||A^n-B^n||_1 <= n r^(n-1)||A-B||_1.                  (11)

For arbitrary large t=n+s with 1<=s<2, multiply (11) by the bounded
positive-spectrum heat factor at s, adding the difference of those
two s factors. That difference is trace class uniformly for s in[1,2]
by (5)-(6) and the finite-rank kernel projections. It follows that

  ||exp(-tP_q)-H_q-exp(-tP_0)+H_0||_1
      <= C(1+n)r^(n-1)=O(exp(-delta' t))                 (12)

for any fixed sufficiently small delta'>0. Taking traces proves

  r_q(t)=dim ker P_q-dim ker P_0+O(exp(-delta't)).         (13)

This proves the required IR bound, not merely a heuristic gap argument.
It gives no lower bound uniform through a light-mode crossing. At such
a crossing the fixed-background proof still applies, but uniform heavy
matching across the crossing requires changing the EFT light split.

## 6. Two controls on what was actually removed

Two compactly supported flat representatives with the same character
are related by a smooth single-valued unitary gauge transformation
(constant on the connected far end, up to an irrelevant constant phase).
It carries the complete graph domain and conjugates the full operator.
The fibre trace of its heat diagonal is unchanged. Since each relative
diagonal integral has just been shown absolutely convergent, the two
relative heat traces and determinants agree. The compact-core choice
of representative is therefore not a hidden new parameter. This does
not identify different Wilson characters or different metric shapes.

As a rejecting analytic control, compact support ALONE is insufficient
for (10). For a scalar Laplacian plus a smooth compactly supported
potential W on a surface, the local expansion instead gives

  Tr(exp(-t(P+W))-exp(-tP))
    =-(1/(4 pi)) integral W dvol + O(t),                 (14)

in the usual unit-principal-symbol convention. A nonzero nonnegative W
has a nonzero constant term. The trace-class argument still works, but
the flat-to-all-orders ultraviolet conclusion fails. For our operators
that stronger cancellation comes from the explicit local gauge
conjugacy of the ENTIRE Higgs/spin/connection operator, not just from
saying that the perturbation lives in the core.

## 7. Precise progress and physical limitation

Within the source construction above, (6), (10), (13) supply A-C for
the actual full fermion-square relative determinant. The preceding
relative-zeta and matching-integral construction therefore has its
analytic hypotheses discharged at authored-proof level for this sector,
subject to independent review of this proof AND the recovered operator
construction. It is no longer justified to leave that particular task
as just a proposed scalar/cusp estimate.

This does not calculate a geometric determinant value, a light kernel
multiplicity, the physical F^2 insertion or full boson/ghost loop weights.
The gauge-fixed bosonic Hessian and ghost operator must be derived on
compatible domains; a cochain heat cancellation cannot replace them.
No supersymmetric spectrum cancellation is asserted from field names.
The existing supplied model still has zero net complex charged index
in this smooth fixed-end phase. The theorem neither fixes that phase
to be the observed vacuum nor excludes other admitted end/source laws.

Before: relative normalization/scale lemmas required unproved global
heat hypotheses for the actual fermion sector. After: compact elliptic
factorization, off-diagonal L2 propagation and a trace-norm gap argument
prove them under the explicit source assumptions, without a radial
cutoff subtraction or extra reflecting boundary. Remaining inputs and
the full SM/three-generation/gravity goal are unchanged. This is a
conditional analytic reduction, not a completed physical prediction,
new execution permission, banked theorem or independent certificate.
