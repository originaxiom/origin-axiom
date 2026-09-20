# F04: test the actual rank-four metric, not only an induced rank-two metric

2026-09-20, fork `audit/fork-2026-09-20`, input `7d277ade`.
Fork-local checkpoint, not a shared B allocation, completed banking pass,
independent review, physical chirality result or claim of literary novelty.

## Preregistered question and outcomes

Does the nonsplit rank-four coefficient system V=Sym^3(rho) tensor chi
force every hypothetical smooth source-free harmonic Hermitian metric on
its complete one-cusped base to develop exponentially large angular
variation in its simple-root scales? No finite-energy hypothesis is imposed,
and the metric is NOT assumed induced by a rank-two metric.

Expected outcome A, before execution: yes, with the precise scope in PROOF.
The full flag supplies three globally defined subharmonic heights. Their
positive flux and the three actual peripheral periods yield a coupled
exponential inequality. A3 Cartan weights combine this into a scalar
finite-distance blow-up obstruction unless the angular oscillation is large.
All six complex upper-triangular coordinates remain available throughout.

Outcome B: a representation, equivariance, normalization, energy identity,
variation, weight or countercontrol fails. Preserve the failed version;
repair with a separately sealed version or narrow the conclusion. Passing
finite exact checks does not itself prove the global quantifier.

## Fixed data and hypotheses

- M is the complete, boundaryless, finite-volume, one-cusped hyperbolic
  three-manifold underlying the marked m010 witness. The analytic theorem
  assumes its complete hyperbolic metric; this checkpoint does not provide
  another interval hyperbolicity certificate.
- rho(a)=[[u,1],[0,1-u]], rho(b)=[[-1,u^2],[0,-1]],
  u=(1+i sqrt(3))/2, chi(a)=u, chi(b)=-1.
  Relator aabaBaaBab, mu=AbAA, lambda=babA, capitals inverse, products left
  to right. The marked base and exact cohomological index are prior inputs.
- Symmetric-cube columns are coefficients of
  (a*x+c*y)^(3-j)*(b*x+d*y)^j in x^(3-i)y^i. Then change basis by
  S=diag(1,sqrt(3),sqrt(3),1). All diagonals of the generators have modulus
  one. V(mu)=exp(-J), V(lambda)=exp(J), where J's first superdiagonal is
  (sqrt(3),2,sqrt(3)). The exponential is a degree-three polynomial.
- H is an arbitrary smooth positive Hermitian metric, equivariant by
  H(gamma x)=V(gamma)^(-dagger) H(x) V(gamma)^(-1), solving the source-free
  harmonic equation. Neither finite map energy nor bounded H is assumed.
- Cusp metric dr^2+exp(-2r)h0, flat torus x1,x2 of period one, reference
  area A0, diameter D0, K=|d(x1-x2)|^2_(h0)>0.
- Normalize det H to one by its harmonic central factor; PROOF justifies
  that operation rather than assuming the original determinant is constant.
  Write H=N^dagger diag(exp(t_i)) N with N upper unitriangular, sum t_i=0.
  b_j=sum_(i<=j) t_i; h_i=t_i-t_(i+1), i=1,2,3.
- L=sum_j average_T b_j. Omega_i=average_T h_i-min_T h_i.
  W=(3/2)Omega_1+2 Omega_2+(3/2)Omega_3. The proposed exclusion is
  W=o(exp(2r)), more generally limsup W/L<1, NOT arbitrary angular behavior.

## Already known, and what is being added

F01 directly excludes finite-energy rank-four harmonic metrics and retains
the algebraic index. F03 excludes a controlled infinite-energy rank-two
class, expressly leaving arbitrary rank-four metrics undecided. F02
separates background energy, static action, and the fermion operator domain.
R27's exact coefficient system and R28/R29's alternative source/action
routes are inputs, not rediscoveries. No semisimplification is substituted.

The new step is the direct full-metric flag inequality, not Cholesky theory,
Cartan arithmetic, or the finite-time ODE lemma (already supplied in F03).
Current-file searches for Cholesky/Iwasawa/Toda/flag heights were made with
word boundaries; unrelated number-theoretic Iwasawa and W-algebra Toda
hits are not coverage of this equation. No semantic absence is inferred.
The report-guided all-history sweep remains the broader retrieval receipt.

The publisher's accessible introduction to Wu--Zhang, *Harmonic metrics
and semi-simpleness*, states its main equivalence for a compact base with
arbitrary connection. Its generality about connections does not remove
compactness. Collins--Jacob--Yau, arXiv:1403.7825, concerns punctured curves
with specified parabolic asymptotics. Only its abstract was accessible in
this check; no unexamined theorem from it is used on this 3D cusp.

## Controls sealed before first execution

1. Exact representation relation, full flag, unit diagonal moduli, regular
   unipotent chain and normalized peripheral exponentials.
2. Metric equivariance and invariant leading principal determinants at a
   non-diagonal positive metric; central determinant normalization identity.
3. Full trace metric formula with six independent complex root directions.
   A nontrivial N must distinguish dN*N^-1 from N^-1*dN. This ordering is
   load-bearing and a deliberately wrong version must fail.
4. Diagonal Euler derivatives, positive flag sums, and multiplicities of
   higher roots. No assertion that necessary diagonal equations suffice for
   the full harmonic equation.
5. A3 Cartan inverse weights, exact AM-GM equality and strict countercontrol,
   period norms on a non-square torus and coordinate invariance.
6. The existing harmonic local cusp in the full rank-four representation:
   its flag equations and full matrix tension must vanish; its negative
   outer flux and positive inner-boundary balance remain visible. A wrong
   profile must fail. A zero-period control distinguishes translation from
   rank alone.
7. Determinant normalization must not discard arbitrary central harmonic
   data; generic Cholesky data are not forced into induced-rank-two ratios.
8. Preserve F03's smooth weighted-energy counterexample: it forbids replacing
   a minimum by a mean. Recheck F01-v2, F02 and F03 unchanged as antecedents.

Seal design, full proof, verification code and tests by SHA256 and commit
before execution. No shooting grid, parameter enlargement or empirical
constant is used. Record failures as failures, not by editing frozen code.
