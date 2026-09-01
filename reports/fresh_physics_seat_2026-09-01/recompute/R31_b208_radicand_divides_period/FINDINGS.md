# R31 — B208: does the field radicand squarefree(m²+4) always divide the WRT period P(m)?

**Target.** `frontier/B208_period_congruence_unification/FINDINGS.md` l.14–22: for γ = RᵐLᵐ,
`squarefree(m²+4) | P(m) = m(m²+4)/gcd(m²+4,4)`, "originally checked m=1..300; an independent re-audit
found **0 failures to m=300 000** via `sympy.factorint`", then a two-line proof. The Phase B reader flagged
**CLAIM_EXCEEDS_COMPUTATION**: the committed script `period_congruence.py` asserts the divisibility only to
m=200 (l.43, l.53); the 300 000 re-audit is uncommitted.

**What R31 did** (`r31.py`, sympy 1.x, ~4 min): recomputed the divisibility for every m = 1..300 000 with
`sympy.factorint`, and recorded the set of 2-adic valuations v₂(m²+4) over even m.

| quantity | bank | R31 |
|---|---|---|
| failures, m = 1..300 000 | 0 | **0** |
| v₂(m²+4), m even | {2,3} | **{2,3}** |

**Proof re-read (by hand).** m odd: m²+4 odd, gcd = 1, P = m(m²+4), s | m²+4 | P. m even, m = 2k:
m²+4 = 4(k²+1); k even → v₂ = 2, k odd → v₂ = 3 (k²+1 ≡ 2 mod 4). Writing m²+4 = s·t² with s squarefree,
v₂(s) ∈ {0,1} and v₂(t²) even force v₂(t) = 1 in both cases, so t²/4 ∈ ℤ and gcd(m²+4,4) = 4, giving
P = s·(m·t²/4). The bank's proof is correct and complete; the numeric sweep is redundant with it.

**Verdict: MATCH.** The reader's flag is literally correct (the 300 000 figure is a claim without a committed
witness) and of low weight: the statement is a theorem, and the committed m ≤ 200 assertion plus this cell's
sweep both agree with it. Suggested fix for cc: raise the committed assertion or cite this cell, so the
FINDINGS number has a witness.

**Physics content:** none added by this cell. The divisibility ties the WRT level-period of a Fibonacci-type
word RᵐLᵐ to the radicand of the real quadratic field of its trace; that is arithmetic of SL(2,ℤ) words,
not a prediction. "No observable content."
