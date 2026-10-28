# Parallel-phase chiral kernels and their light running

October 27, 2026. UNREVIEWED authored analytic derivation. No science
producer, CAS, numerical spectrum or test execution. This is the actual
quadratic chiral kernel in the specified curved-action parallel phase,
conditional on the recovered action/operator/complete-domain construction.
It is not a three-generation claim or a classification of the full generated
architecture. Neither the supplied carrier nor the Wilson character is
selected from genesis here.

## 1. Quantifier, source recovery and the physical zero equations

Fix the source's complete hyperbolic once-punctured elliptic curve Sigma,
an extending spin line S, and the R=0, Q-principal parallel background
with a flat Y connection C supported in the compact core. The source's
SU5_g x SU5_b branching, principal irreducible modules V_j and actual
weighted complex are retained. On a gauge charge sector let L denote
the unitary flat line with that charge's C character. Its peripheral
holonomy is trivial and it extends flatly over the compactification X.

Personally reread weave_two_neutral_index/PROOF (full complex and norms),
weave_magnetic_index/PROOF (exact L2 line kernels and endpoint proof),
weave_neutral_stability/PROOF (spin extension and holomorphic sections),
weave_sm_parallel/PROOF and the actual physical mass map. These already
supply the ingredients used here; the older complete index is not a
substitute for the total kernel count. The locator already_banked query
"parallel Wilson chiral kernel" returned broad older hits, including
B956, whose analysis was read. No corpus-wide absence or novelty claim
is made from that search. CANONICAL_CUSP_PROOF section5 already uses a
bounded homotopy on a DIFFERENT geometry; its operator is not reused.

At this F/D-flat background the same-action scalar operator is

  P_c=H dagger H+D0 D0 dagger,
  ker P_c=ker D1 intersect ker D0 dagger.                   (1)

The physical W Hessian H has the same zero space as the full linear F
map D1 under the source's actual target isometry. Thus (1) is degree-one
harmonic cohomology of the COMPLETE two-spin-field complex. Degree-three
is analytical bookkeeping and is not counted as a chiral matter field.
The gauge/gaugino kernel is counted separately by P_v=D0 dagger D0.

## 2. Contract the actual paired modules without changing the L2 domain

For a principal V_j, let H_pr be its compact triple grading (distinct
from the W Hessian H above). The w=H_pr/2 weights are m=-j,...,j and their actual
holomorphic lines are

  E_m=S^(-m) tensor L.                                    (2)

The full Q background is parallel in S tensor End(E). Raising sends
E_m to S E_(m+1), m<j. These are the SAME line S^(-m)L, with a nonzero
constant coefficient proportional to sqrt((j-m)(j+m+1)). This is an
exhibited bundle map, not equality of dimensions or limiting holonomies.
The induced Hermitian metrics make it a bounded isomorphism with bounded
inverse on the actual L2 sections, and on their (0,1)-form partners.

For example, in the source's z frame E_m has metric Omega^m; the source
and target section densities are respectively Omega^2 Omega^m and
Omega Omega^(m+1), which agree. For the form partner the remaining
normalization ratios are fixed constants. The four paired density checks,
including the shifted B complex, are explicitly

| Source slot | Source density | Target slot | Target density |
|---|---|---|---|
| epsilon_m | Omega^(m+2) | u_(m+1) | Omega^(m+2) |
| a_m | Omega^m/2 | p1_(m+1) | Omega^m |
| v_m | Omega^(m+1) | t_(m+1) | 2 Omega^(m+1) |
| p2_m | Omega^(m-1) | sigma_(m+1) | 2 Omega^(m-1) |

Thus both directions are bounded in every degree. No inverse of a decaying
neutral section or an unbounded cusp frame has been inserted.

At R=0 the entire complex is the direct sum of the Dolbeault total
complexes of

  A: E -> S E,
  B: S E -> K E, shifted UP by one total degree.            (3)

Both arrows are the SAME principal raising map. This follows directly
from D0=(Dbar,-i ad Q,0), D1=(Dbar u+i[Q,a],Dbar v,[Q,v]) and
D2=Dbar t-[Q,p2], up to the source's constant norm factors/phases.
The covariant Dolbeault connection preserves every weight in (2).
There is no unstated differential between different surviving extremes.

Here is a domain check for each non-extreme pair. Write its holomorphic
isomorphism as T:U->V. In total degree n use (alpha,beta) in
U^(0,n)+V^(0,n-1), differential

  delta(alpha,beta)=(dbar alpha,T alpha-dbar beta),
  h(alpha,beta)=(T^(-1) beta,0).

Holomorphicity gives delta h+h delta=1 on compactly supported smooth
sections. All degrees have bounded h in the physical norms. If f_n
approaches f in the minimal differential graph norm, h f_n approaches
h f and delta h f_n=f_n-h delta f_n converges. The identity therefore
extends to the SAME complete differential domain. This pair has zero
cohomology. The source's gapped Hodge realization identifies cohomology
with its harmonic kernel. This excludes extra paired zero modes without
deleting their nonzero spectrum or interactions.

The only remaining line complexes are

  A input extreme:  S^(-j)L, degree0;
  A output extreme: S^(j+1)L, degree1;
  B input extreme:  S^(1-j)L, total degree1;
  B output extreme: S^(j+2)L, total degree2.               (4)

Consequently the PHYSICAL chiral count per gauge component is

  N_j(L)=h1_L2(S^(-j)L)+h0_L2(S^(j+1)L)
                         +h0_L2(S^(1-j)L)
        =h0_L2(S^(j+2)L^(-1))+h0_L2(S^(j+1)L)
                         +h0_L2(S^(1-j)L).               (5)

The second equality uses the source's actual Hermitian Hodge map, not
a compact-surface Euler characteristic. Explicit representatives are
A_j harmonic as an E_j-valued (0,1) form, u_(-j) holomorphic, and v_j
holomorphic, respectively. The raising/lowering endpoint actions make
each satisfy (1). They have the source's finite positive kinetic norms.
The bounded contraction proves completeness, not just a lower bound.

The same reduction gives

  dim ker P_v=h0_L2(S^(-j)L),
  dim H3=h1_L2(S^(j+2)L)=h0_L2(S^(-j)L^(-1)).             (6)

Their equality below is a gauge/dual control, not permission to count
H3 as an additional independent physical chiral field.

## 3. Preserve the cusp equality endpoints and flat-character exceptions

Let eta be the compact extension of S, so eta^2=O_X. The source's local
spin metric is comparable to r|log r|. A pole of order p in S^a L has
radial L2 integrand r^(a-2p-1)|log r|^(a-2). Since L is flat and trivial
on the far end, it changes no exponent. The exact pole bound remains

  b(a)=floor(a/2), a<=0;
       ceil(a/2)-1, a>=1.                                (7)

In particular b(0)=b(1)=b(2)=0: the logarithmic endpoints must not be
replaced by an ordinary compact degree a/2. Laurent orthogonality
excludes forbidden poles and essential singularities as in the source.
Thus

  h0_L2(S^a L)=h0(X,eta^a L tensor O_X(b(a)p)).             (8)

For any degree-zero line F on an elliptic curve define

  H(d,F)=0 if d<0;
         1 if d=0 and F=O, otherwise0 at d=0;
         d if d>0.                                      (9)

For d=0 a nonzero section has no zeros and trivializes F. For d>0,
Riemann-Roch and K_X=O identify h1 with sections of a negative-degree
dual line, hence zero; h0=d. The negative-degree case follows from the
effective zero divisor of a hypothetical section. The primary general
formula/duality was personally checked in Stacks Lemma53.5.2:
https://stacks.math.columbia.edu/tag/0B5B. The cusp extension (7)-(8)
is our recovered local argument, not an application of RR on an open
surface. No whole-book reading is claimed.

Substitution in (5)-(6) gives the following exact symbolic table through
the ENTIRE j=0,...,4 E8 roster. Let delta(F)=1 for a trivial compact
degree-zero line and0 otherwise:

| j | Physical chiral count N_j(L) | Gauge count |
|---|---|---|
| 0 | delta(L)+2 delta(eta L) | delta(L) |
| 1 | 1+2 delta(L) | 0 |
| 2 | 2 | 0 |
| 3 | 3 | 0 |
| 4 | 4 | 0 |

For j>=2 the same computation gives N_j=j, since the two positive
pole bounds sum to j and the third bound is negative. At j=1 there
is a real jump at a trivial character. At j=0 the spin exception is
distinct: eta L can be trivial without L being trivial. For a unitary
flat line on compact X, holomorphic triviality is equivalent to trivial
unitary character: a nowhere-zero holomorphic section has harmonic
log norm, constant by compactness, and is parallel. Thus the exception
conditions are actual holonomy conditions, not extra fitted numbers.

Both N_j(L)=N_j(L^(-1)) and equality of the two counts in (6) follow
directly (eta has order at most2). These recover the already-proved zero
net charged index while determining additional information: TOTAL modes.

## 4. Apply it to the SOURCE'S order-seven SM Wilson character

On5_g put Q_Y=6Y=diag(-2,-2,-2,3,3), distinguished from the Higgs Q.
The actual source chooses holonomy exp(i theta Q_Y), theta=4pi/7 on a
and trivial on b. For every nonzero
charge appearing here, |q|<=6, L_q has order7. It is neither trivial
nor a nontrivial order-two eta. No exceptional line has been rounded
away. This character is supplied, not forced by this kernel theorem.

Retain all source terms

  (24_g,1)+(1,24_b)+(10_g,5_b)+(bar10_g,bar5_b)
                          +(bar5_g,10_b)+(5_g,bar10_b),
  5_b=V2, 10_b=V1+V3, 24_b=V1+V2+V3+V4.

The resulting physical massless chiral roster is:

* Each SM component of10_g and bar10_g has multiplicity2 (j=2).
* Each component of5_g and bar5_g has multiplicity4 (j=1 plus j=3).
  The nonzero charges -2,3 and their negatives are all nonexceptional.
* In24_g the charge-zero su3+su2+u1 directions have multiplicity
  kappa=1+2 delta(eta). Its charge +/-5 mixed directions have none.
* The gauge-singlet24_b contributes 3+2+3+4=12 chiral singlets, since
  its j=1 line is L_0=O. The other singlet directions just mentioned
  inside24_g are retained separately, not discarded or counted twice.

The first two rows assemble, AS COUNTS, as

  2(10+bar10)+4(5+bar5),                                 (10)

branched under the actual SM group. This does not restore SU5 gauge
symmetry or assert equal wavefunctions, overlaps or Yukawas between
different charge components. The full chiral dimension is 92+12 kappa;
the vector dimension is12. In particular the three modes of V3 alone
are not three SM generations: the SAME5 sector also contains V1 and
the10 sector is V2. Selecting V3 and dropping its companions would
change the theory. The net complex charged spectrum is vector-like,
consistent with the prior same-domain index theorem.

This result holds across the complex-structure/shape choices of the
specified once-punctured elliptic carrier with these same bundle and
domain hypotheses. Counts do not fix its wavefunctions, interactions
or relative determinant values. Nonparallel backgrounds, neutral c/d
profiles, other carriers or end/source laws are not classified here.

## 5. The actual light beta coefficients and scale freedom

Use the SAME +1 chiral and -3 vector weights already derived from the
real action/ghost measure, with the source's SU5 hypercharge convention.
The complete charged roster (10) contributes equally to the normalized
three factors:

  2*(T10+Tbar10)+4*(T5+Tbar5)=2*3+4*1=10.

The kappa adjoints of the unbroken algebra contribute (0,2kappa,3kappa).
The12 additional singlets contribute zero; the vector part is (0,-6,-9).
Therefore

  (b1,b2,b3)_light=(10,4+2kappa,1+3kappa),
  (h21,h31)=(2kappa-6,3kappa-9).                         (11)

For the trivial extending spin line kappa=3, b=(10,10,10) and the two
weighted light counts vanish. The preceding relative determinant's
common internal-scale and matching-switch dependence consequently
cancels. For any of the three nontrivial extending spin lines kappa=1,
b=(10,6,4) and (h21,h31)=(-4,-6): that logarithmic scale dependence
must remain with the derived light running. The absolute coupling is
not made scale-free in either case.

Do NOT choose the trivial spin just to make a relative parameter
disappear. Spin selection is still an independent physical duty. The
two cases are the conditional programme output. Their beta coefficients
are those of this explicitly supersymmetric, vector-like model, not
the observed nonsupersymmetric SM or a fitted low-energy threshold.
Supersymmetry breaking and physical-scale identification would change
the light EFT and require their own same-action derivation.

## 6. Controls and precise mission accounting

At zero Wilson character all charges have L=O. The gauge kernel restores
su5; the full5/bar5 chiral multiplicity becomes6 (not4), the10 count
stays2, and the24_g count is kappa. The relative normalized gauge
coefficients cancel within each full SU5 representation, as required.
These jumps occur in the compact-core kernels while the essential gap
remains fixed, recovering the source's distinction between index and
individual kernel dimensions. No uniform heavy-only integral is inferred
through a light crossing.

All counts here are obtained by explicit extreme representatives PLUS
a bounded contraction of their complement, exact cusp endpoint bounds,
and elliptic-curve line dimensions. They are not a census of random
classes, a finite-grid null or an extrapolation from the asymptotic mass
histogram. The formulas are authored proofs awaiting independent review;
source custody and read scope are recorded. No science executable or
test was run and no old review/execution authorization is enlarged.

Before: the physical relative loop formula had an undetermined light
chiral count. After: that count is fixed in the specified parallel phase,
including spin/character exceptions and the actual light-running term.
This removes a separate spectrum choice inside this model. It does not
derive the parent, gauge embedding, carrier, spin or Wilson state from
the foundational principle, and adds no observed-parameter prediction.
Next are independent analytic review, the global relative spectral values
with these kernels removed consistently, and the physical end/state law
needed to go beyond this smooth zero-index benchmark. Three physical
chiral families, gravity and the full input-reduction mission remain
unachieved. No scoped model result is promoted to an architecture kill.
