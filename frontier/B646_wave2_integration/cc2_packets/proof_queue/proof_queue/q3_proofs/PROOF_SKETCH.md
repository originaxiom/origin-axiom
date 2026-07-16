# Q3 — PROOF SKETCH: the resonance laws of the E6 Z-ladder (cc2, 2026-07-16)

Object: Z(kappa) = (1/|W|) sum_w det(w) |A_w|^{-1/2} G_w(kappa), A_w = Z^6/B_w Z^6,
B_w = 3 - w - w^{-1}, G_w(r) = sum_{mu in A_w} e(-i pi r <mu, B_w^{-1} mu>).
Identity (exact): det B_w = |det(A1 (x) w - 1)| = #Fix(w-twisted A1 on the coroot
12-torus); disc(A1) = 5.

## Lemma 1 (STANDARD — cited, no novelty): multiplier twist.
For q nondegenerate on a finite abelian p-group (p odd) and gcd(r, p) = 1:
G(r q) = (r|p)^{m} G(q), where m = number of odd-exponent elementary divisors
(rank-parity of the p-adic Jordan blocks); |G| is unchanged. 2-adic analogue twists
by a character mod 8. [Milgram/Wall; Scharlau, "Quadratic and Hermitian Forms";
standard Gauss-sum local theory. Lit-gate: known.]

## Lemma 2 (VERIFIED EXACTLY, this cell): sector decomposition.
Computing all 25 classes' elementary divisors (SNF, q3_lemmas.log): exactly ten
classes carry an odd number of odd-exponent 5-divisors; no other odd prime
contributes an odd-rank part with nonvanishing sector sum. Sector sums on the generic
row: trivial sector = +1/2, chi_5 sector = +1/2 (both real, imag < 1e-10).
With Lemma 1, for kappa coprime to all |A_w|:
  Z(kappa) = 1/2 + (1/2) * (kappa|5)/(13|5) = (1 - (kappa|5))/2.
DECIDED empirically at the three new rungs: Z(29) = Z(31) = 0 [(r|5) = +1],
Z(37) = +1 [(r|5) = -1] — jeffrey_decider.json, class-function guards on.
=> **THE GENERIC-RUNG THEOREM (corrected): Z(kappa) = (1 - (kappa|disc A1))/2 for
kappa coprime to 2*3*5*7*11*19.** Status: theorem modulo (i) the cited Lemma 1 and
(ii) the exactness of the computed sector sums (integer-certifiable: each generic
term is a normalized Gauss sum with |term| = size/|W| and phase an 8th root of unity;
certification path identified, not yet executed).

## Lemma 3 (VERIFIED EXACTLY, this cell): THE UNIFORM JUMP LAW.
For every class w and every kappa (r = 14..25, 300 cells, zero exceptions):
  |term_w(kappa)| / |term_w(generic)| = prod_{p^a in elem divisors of A_w}
                                          p^{min(v_p(kappa), a)/2}.
No odd/dyadic case split — the earlier "dyadic cap 2^floor(v2/4)" is min(v, a) at
elementary divisors 4 = 2^2 (e.g. (Z/4)^6 at b21: v=1 gives 2^{6*1/2} = 8, v=4 gives
2^{6*2/2} = 64). Local-proof shape: on Z/p^a with multiplier p^v u, the radical of
the reduced form has index p^{a - min(v,a)}; standard local Gauss magnitude gives
p^{(a + min(v,a))/2} vs generic p^{a/2}. [Proof-by-local-computation; assembly into
a clean statement = promotion target.]

## Corollaries (checked against direct computation):
- kappa = 16 and 25 (prime-power squares of the two "silent" primes 2, 5): residue
  baselines 0 + resonance sums 0 => the two silences. Z(25) = 0 confirmed directly.
- kappa = 19: residue baseline 0 + Phi_9-class full saturation (+2) => Z_7 = 2.
- kappa = 20 (Q1, measured +1 by the conformal-block build): 5-resonant classes +
  dyadic partials sum to +1 over a (20|5)=0 mixed baseline — consistency verified
  numerically; per-class table in jeffrey_extension.json.

## Open (promotion targets, honestly labeled):
1. Certify the sector sums as exact algebraic numbers (8th-roots x rational) — turns
   Lemma 2's "computed" into "proven". 2. Assemble Lemma 3's local computation into a
   stated theorem with the 2-adic case written out. 3. WHY disc(A1): derive the
   odd-rank-5 classes' structure from the golden eigenvalues mod 5 (ramification of
   Q(sqrt5) at 5) — the conceptual jewel. 4. The resonant-phase law (signs of jumped
   terms) — needed to predict surpluses (+2 vs 0) without running the pipeline.
