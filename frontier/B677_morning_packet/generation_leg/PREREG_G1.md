# PREREG — THE GENERATION LEG, cc2 route: THE TUBE-ALGEBRA / CHARACTER
# CANDIDATES (sealed before compute, 2026-07-18; plan 353ca003)

TARGETS (fixed, banked, READ from repo frontier/B672_grading_hunt/ cellB +
cellG + FINDINGS.md — read-only): the exact weight-5 doublet streams
  comp1 = q^{2/5} * N1(q) * (q;q)^9,   comp2 = q^{3/5} * N2(q) * (q;q)^9
with N1 = (q;q)G(q), N2 = (q;q)H(q) the Rogers-Ramanujan numerators.
Comparison = exact integer coefficients, >= 100 terms, term-by-term.

THREE CANDIDATE GENERATORS (each defined BEFORE compute; each MATCH /
STRUCTURED-NEAR-MISS (exact mismatch banked) / KILL is bankable):
- T2 (cheapest, run FIRST): the weld-weighted CHIRAL character sum.
  The Fibonacci/Lee-Yang chiral characters chi_1, chi_tau (the (2,5)-model
  characters, c = -22/5 resp. effective c = 2/5 normalization -- STATE the
  normalization used and why, from the classical formulas; both
  q-expansions computed exactly from the RR product/sum forms). Candidate:
  Z_W(q) = sum_a (W)_{a a} chi_a(q) and the off-diagonal variants
  (W)_{a b} chi_b for the 2x2 weld W = B238's operator restricted to the
  golden block (kappa = 5). Does any weld-matrix-weighted combination
  reproduce comp1/comp2 (up to the sealed eta-power bookkeeping
  eta^{48/5}, stated explicitly)?
- T1: the DOUBLE's character sum: the 4 simples of Z(Fib) = Fib (x)
  Fib-bar with characters chi_(a,b) = chi_a(q) chi_b(q-bar) restricted to
  the diagonal q-grading; weld-weighted via B238's full modular action.
- T0 (the structural candidate): the weld-twisted Hochschild graded trace
  on Tube(Fib): build Tube(Fib) explicitly from the Fibonacci F/R symbols
  (phi-entries, exact in Q(sqrt5)); W induces the mapping-class
  automorphism; compute HH^n(A, A_W) for n = 0,1,2 exactly and the trace
  of the induced action, graded by the twist (theta) eigenvalues
  theta_1 = 1, theta_tau = e^{4 pi i/5} (the 2/5 weight — NOTE, stated as
  consistency only: the targets' leading powers 2/5 and 3/5 are the
  (2,5)-model weights).
FALSIFIERS: any candidate whose FIRST 10 coefficients mismatch is killed
at the first exact mismatch (banked like B672's four kills); no
normalization freedom beyond what each candidate's definition names IN
ADVANCE (eta powers, overall rational constant, q-shift by the stated
weights — NOTHING ELSE; no post-hoc rescaling).
K020: silver control runs ONLY on a MATCH (silver category per B649's
Q(sqrt2) hearing conjecture — scoped separately if reached).
DISCIPLINE: repo read-only; work in seat-work/generation_leg/g1_tube/;
exact arithmetic (Q(sqrt5)/cyclotomic exact or integer q-series) in all
verdict paths; subagent compute, main-seat verify; bank only finished runs.
