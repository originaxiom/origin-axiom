# G1_TUBE -- raw data (no physics language). Prereg: seat-work/generation_leg/PREREG_G1.md.
Script: g1_tube.py. Full log: g1_run.log. Machine-readable: g1_results.json.

## Target reproduction (STOP gate) -- PASS

Three independent constructions of G(q)=sum q^{n^2}/(q;q)_n, H(q)=sum q^{n(n+1)}/(q;q)_n:
- Route A: RR sum formula (direct truncated series).
- Route B: RR Euler-product formula, G=1/[(q;q^5)(q^4;q^5)], H=1/[(q^2;q^5)(q^3;q^5)].
- Route C: theta/Jacobi-triple-product numerator N1=theta_num(1,.), N2=theta_num(3,.),
  G=N1/(q;q), H=N2/(q;q).

All three agree exactly, coefficient-by-coefficient, to 160 terms (required: >=120).
comp1_reduced = N1(q)*(q;q)^9 (comp1 = q^{2/5} * this): head
  [1, -9, 26, -4, -108, 120, 156, -144, -378, -39, 936, 140, -728, -729, ...]
comp2_reduced = N2(q)*(q;q)^9 (comp2 = q^{3/5} * this): head
  [1, -10, 36, -39, -79, 234, -108, -140, -9, -4, 676, -810, 351, 104, ...]
Spot-check against repo-banked frontier/B672_grading_hunt/cellG/cellG_output.txt (read-only,
not used to derive anything): banked ratio(n=1) for 2hat.comp1=-9, 2hat.comp2=-10; matches
exactly.
eta^{48/5}-bookkeeping gate: F1=N1*E1^(-3/5), F2=N2*E1^(-3/5) (fractional-power binomial
series, exact Fraction coefficients); F1*eta_reduced^{48/5} == comp1_reduced and
F2*eta_reduced^{48/5} == comp2_reduced, verified to 121 terms.

## Cyclotomic engine (Q(zeta_5), power basis {1,z,z^2,z^3})

All gates pass: z^5=1; SQRT5 = z-z^2-z^3+z^4 numerically = +sqrt(5) (not -sqrt(5));
phi^2=phi+1; psi*phi=-1 (psi=-1/phi). Q(zeta_5) is used (not just Q(sqrt5)) because the
T-matrix phases (5th roots of unity) are genuinely degree-4 over Q; Q(zeta_5)'s real
subfield is exactly Q(sqrt5).

## Weld operator W (B238's kappa=5 golden-block RL monodromy)

W_FIB (Fibonacci/unitary convention: d=phi, h_tau=2/5, theta_tau=e^{4pi i/5} matching the
prereg's T0 statement exactly):
  trace(W_FIB) = psi = -1/phi, EXACT (not approximate) -- matches B238's banked headline
  number Z(figure-eight; SU(2)_3)=Z(figure-eight; SU(3)_2)=-1/phi.
  det(W_FIB) = 1, EXACT.
W_YL (Yang-Lee/sigma_3-Galois-conjugate convention: d=psi=-1/phi, h_tau=-1/5):
  trace(W_YL) = +phi, EXACT. det(W_YL)=1.
  FINDING: this does NOT match B238's -1/phi -- the Yang-Lee point is a formal Galois
  conjugate of the abstract fusion data, not a literal sub-block of the unitary SU(2)_3/
  SU(3)_2 modular data.
Modular-relation gates (mirroring B238's own modular_gate): M^2=(1+phi^2)*I exact (<=>S^2=I
once normalized); (M T)^3 is a scalar matrix (propto M^2) exact.

FINDING (anomaly, banked): naive row/column extraction of indices {spin0,spin1} from the
ACTUAL SU(2)_3 4x4 (S,T) matrices (freshly built via Kac-Peterson, sympy, 40-digit numeric
exactness) does NOT reproduce W_FIB or its trace. The full 4x4 RL-monodromy trace matches
-1/phi exactly (confirms B238); the naive {0,2}-submatrix's trace is
-0.309016994375 - 0.309016994375*I (complex, not -1/phi) -- because S does not act
block-diagonally on the {spin0,spin1} subspace (S mixes all 4 spins). The standalone
Fibonacci category's own (S,T) (W_FIB, as used throughout this repo: B135/B220/B484/B218)
is the correct "golden block" object, matching the ambient trace via an independent
mechanism, not via literal restriction.

## T2 -- weld-weighted chiral character sum: KILL

Two classical (2,5)-model character normalizations tested, both stated explicitly:
  YL:  c=-22/5, h_1=0, h_tau=-1/5 (c_eff=c-24*h_min=2/5)  => chi_1=q^(11/60)*G(q), chi_tau=q^(-1/60)*H(q)
  FIB: c=+14/5, h_1=0, h_tau=+2/5                          => chi_1=q^(-7/60)*G(q), chi_tau=q^(17/60)*H(q)

Reading (A), full CFT prefactor retained: fractional-support-class check (exact Fraction
arithmetic). Neither chi_1's nor chi_tau's class mod 1 equals comp1's class (2/5) or comp2's
class (3/5), for EITHER convention:
  YL:  chi_1 class=11/60, chi_tau class=59/60 (mutual gap=1/5, non-integer)
  FIB: chi_1 class=53/60, chi_tau class=17/60 (mutual gap=3/5, non-integer)
=> structural KILL, independent of W's numeric value: every candidate's support lies
entirely outside comp1's/comp2's actual exponents; first mismatch is n=0 (expected 1, got 0
identically, for any weld weighting).

Reading (B), prefactor-stripped (chi_1->G(q), chi_tau->H(q)), numeric test, weld in
{W_FIB, W_YL}, variant in {diag(sum_a W_aa chi_a), row1(W_a1 chi_1+W_a2 chi_2 vs F1),
row2 vs F2} -- 6 sub-candidates total. Leading coefficient (n=0, using G(0)=H(0)=1) computed
exactly for each:
  W_FIB.diag = W11+W22 = 1+z^2+z^3            (numeric -0.618034+0.000000i)  NOT rational
  W_FIB.row1 = W11+W12                         (numeric  0.500000-0.162460i)  NOT rational
  W_FIB.row2 = W21+W22                         (numeric -1.118034+0.688191i) NOT rational
  W_YL.diag  = W11+W22 = -1-z^2-z^3            (numeric  1.618034-0.000000i)  NOT rational
  W_YL.row1  = W11+W12                         (numeric  0.500000+0.688191i)  NOT rational
  W_YL.row2  = W21+W22                         (numeric  1.118034+0.162460i)  NOT rational
None of the 6 leading coefficients is rational (all have nonzero z/z^2/z^3 components in
the Q(zeta_5) power basis). Target's leading coefficient is 1 (rational) in every case
(F1[0]=F2[0]=1). Since the prereg's sole allowed freedom is ONE overall RATIONAL constant,
no rescaling can turn an irrational cyclotomic number into 1 -- first mismatch banked at
n=0 for all 6 sub-candidates, exact witness values as above.

VERDICT T2: KILL. Both readings, both conventions, both welds, all variants (diag + 2 rows) = 8 tests total, all fail at term 0.

## T1 -- double Z(Fib)=Fib(x)Fib-bar character sum: KILL

Fib modularity gate: det(unnormalized S-matrix M) = -2+z^2+z^3 != 0 (nonzero, exact) =>
Fib is modular => Z(Fib)=Fib(x)Fib-bar (4 simples), standard theorem.
Full weld W' = T^{-1} S T S built (swap of W_FIB=T S T^{-1} S); cross-check
weld_general(phi,+2,-2)==W_FIB exactly (gate PASS). W' trace = 1+z^2+z^3 = -1/phi (same
value as W_FIB's trace, det(W')=1).
4x4 double weld W4[(i,j),(k,l)] = W_FIB[i,k]*W'[j,l] built explicitly (Kronecker structure).
TRACE-BLINDNESS DATUM: the fully-diagonal-summed candidate T1.diag equals
tr(W_FIB)*tr(W') = 2+z^2+z^3 (numeric 0.381966) -- a SINGLE SCALAR, not a q-series at all
(the Kronecker-diagonal sum factors exactly into the product of the two component traces).
This mirrors B674's independent finding (tr(A1*|H^1(Gamma(5),Sym^m))=0 identically for all
m -- a pure-trace object with zero per-degree information).
5 candidates tested (diag + 4 rows, prefactor-stripped reading matching T2 reading B).
Leading coefficients (n=0), all NOT rational:
  T1.diag   = 2+z^2+z^3     (numeric  0.381966+0.000000i)
  T1.row_11 = 3/5+z^2/5+z^3/5 (numeric  0.276393+0.000000i)
  T1.row_12                  (numeric -0.670820-0.162460i)
  T1.row_21                  (numeric -0.670820+0.162460i)
  T1.row_22                  (numeric  1.723607-0.000000i)
Target leading coefficient (F1[0]=F2[0]=1, rational) unreachable by rational rescaling in
every case -- first mismatch banked at n=0 for all 5.

VERDICT T1: KILL. Same n=0 irrationality obstruction as T2.

## T0 -- weld-twisted Hochschild graded trace on Tube(Fib): KILL

(i) Tube(Fib) dimension, computed from Fibonacci's own fusion ring N (N_111=1, N_1tt=N_t1t=1,
N_ttt=1(c=1)+1(c=tau), all else 0), via dim Hom(x(x)a,b(x)x)=sum_c N_xa^c N_bx^c, summed over
all (x,a,b) in {1,tau}^3:
  x=1,a=1,b=1: 1 | x=1,a=tau,b=tau: 1 | x=tau,a=1,b=1: 1 | x=tau,a=1,b=tau: 1 |
  x=tau,a=tau,b=1: 1 | x=tau,a=tau,b=tau: 2
  TOTAL = 7 (matches 1+1+1+2^2=7, the dimension count implied by Z(Fib)'s 4 simples having
  module dimensions {1,1,1,2}).

(ii) Generating F/R data axiom gates (sympy):
  F=[[1/phi, 1/sqrt(phi)],[1/sqrt(phi), -1/phi]]: F^2=I exact; F symmetric exact;
  phi^2-phi-1=0 exact.
  FINDING (honest, precise): F's off-diagonal entries need sqrt(phi), a genuine DEGREE-4
  algebraic number (phi is not a square in Q(sqrt5): the equation (a+b*sqrt5)^2=phi has no
  rational solution a,b, by direct elimination -- 80b^4-8b^2+1=0 has negative discriminant).
  So Tube(Fib)'s generating data lives in Q(sqrt(phi),sqrt5), not literally "Q(sqrt5)" as
  the prereg's phrasing suggested.
  B484 reproduction: tr(figure-eight 3-anyon braid) = -3/phi, matched to 60-digit numeric
  precision (symbolic sympy.simplify stalls on the (-1)^{fractional} branch representations
  here; 60-digit numeric agreement, far beyond float-rounding concerns, is the exactness
  gate used, matching the style of B238's own modular_gate()).
  W's modular-relation gates (PART 3, reused): S^2=I (via M^2=(1+phi^2)I), (ST)^3 propto S^2,
  det(W)=1 -- all exact.

(iii) The decisive argument: Tube(Fib) is finite-dimensional (dim=7, computed above); since
Fib is a fusion category, its Drinfeld center Z(Fib) is again a fusion category (standard
theorem: semisimple, finitely many simples), so Tube(Fib) (module category = Z(Fib)) is a
finite-dimensional SEMISIMPLE algebra. Semisimple algebras have HH^n(A,M)=0 for all n>=1 and
ANY bimodule M (separability => homological dimension 0) -- holding identically for the
W-twisted bimodule A_W. Therefore:
  HH^1(A,A_W) = HH^2(A,A_W) = 0 IDENTICALLY (the zero series).
  HH^0(A,A_W) has dimension <= dim(Tube(Fib)) = 7 (in fact <= 4 = #simples of Z(Fib)).
Grading by the theta eigenvalues theta_1=1, theta_tau=e^{4pi i/5} (a fixed finite set of at
most 5 distinct values, per the prereg's own T0 statement) produces at best a finite/
eventually-periodic object in the grading variable.
Explicit witness: comp1_reduced[40]=3402, comp2_reduced[40]=7290. Any object built from
<=7 dimensions of unit-modulus (5th-root-of-unity) phases has |value| <= 7 at every grading
slot; both witness values exceed 7 by a factor of >480. Bankable exact mismatch at n=40 (and
at every sufficiently large n thereafter, since target coefficients grow without bound while
the candidate is bounded).

VERDICT T0: KILL. HH^{1,2}=0 exactly (proved, not observed); HH^0 bounded/periodic vs
unbounded/aperiodic target, explicit witness at n=40.

## Trace-blindness pattern (cross-cell corroboration)

Mid-run intel from frontier/B674_generation_leg (read-only, banked): Eichler-Shimura route 1
found tr(A1*|H^1(Gamma(5),Sym^m)) = 0 identically for all m -- a pure trace functor cannot
generate the streams. This cell's independent findings converge on the same pattern:
- T1's fully-traced/diagonal-summed candidate (T1.diag) collapses to a SINGLE SCALAR
  (tr(W_FIB)*tr(W')), zero per-degree information -- structurally identical failure mode to
  B674's trace tower.
- T0's defining operation (a graded Hochschild TRACE) is bounded/periodic by construction
  (semisimplicity forces HH^{>=1}=0; the remaining HH^0 piece is graded by a 5-element root-
  of-unity set) -- also structurally trace-blind.
- T2/T1's non-diagonal ROW candidates (character-level, not fully traced) have the CORRECT
  unbounded/aperiodic q-series SHAPE (inherited directly from G(q),H(q), which do have the
  right growth), but fail on a DIFFERENT axis: the weld's exact algebraic VALUE at each
  entry is irrational (in Q(zeta_5)\Q), so no rational rescaling can match the target's
  rational coefficients. This is a VALUE-level obstruction, distinct in kind from T0's
  SHAPE-level (bounded/periodic) obstruction -- both are exact, both are bankable, and the
  distinction itself is a bankable datum: trace-reduction kills SHAPE; the weld's algebraic
  field kills VALUE.

## Overall

target_reproduction: PASS (160 terms, 3 independent routes)
T2: KILL (first mismatch n=0, all 8 sub-tests)
T1: KILL (first mismatch n=0, all 5 sub-tests)
T0: KILL (HH^{1,2}=0 identically; HH^0 bounded/periodic; witness n=40)
runtime: 1.3s
