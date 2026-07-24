# B776 PREREGISTRATION — THE B685 HOMEWORK (chat-1's proposal, verified & adopted)

*Sealed before compute. The last provisional wall: B685's terminal no-go is CONDITIONAL
on Φ(h)Φ(−h) being 3-integral at ALL orders (B772/B774 flagged this as the one open
premise; census label SEARCH-BOUNDED(depth 100)). This resolves it as far as in-sandbox
computation allows, so any question to the GSWZ authors is precise and computation-backed.
Chat-1's data verified exact against OI-055 (r-stream, denominators, v5=0,0,1,1,1,2,
h-failure 2²·3⁵, the 3¹⁴⁶ anchor). The GSWZ SEND is a HARD-STOP for owner approval —
NOT part of this arc.*

## Computation 1 — PUSH r₇
Identify r₇ exactly. The v5 pattern is 0,0,1,1,1,2 (r₁–r₆); r₇ decides whether v5 keeps
growing. Method: high-precision colored Jones J_N(e^{2πi/N}) over large N, Richardson/
Euler–Maclaurin extraction of the asymptotic r-stream, PSLQ at ≥100 digits. OI-055 used
dps=520 (r₇ trusted only ~33 digits — below threshold); push to dps=1000–1500 to clear
it. Reproduce on ≥2 independent ladders. Outcome: r₇ EXACT (den factored, v5(r₇) stated)
=> RESOLVED-A / still below threshold at dps=2000 (bank the precision limit) => RESOLVED-B.

## Computation 2 — SYMMETRISED PRODUCT to order ~200
Compute Φ(h)Φ(−h) in u=q−1 to order u²⁰⁰ (or as high as feasible), tracking the
denominator prime-factorization at each order. **THE GUARD (binding): FIRST reproduce
B685's known anchor — denominator 3¹⁴⁶ at (q−1)¹⁰⁰. Do NOT proceed past order 100 until
that is reproduced.** If the GSWZ Section-4.5 normalisation cannot be reproduced
in-sandbox (the paper may be unreadable / the normalisation subtle), BANK THAT as the
honest boundary (RESOLVED-B, the normalisation gap named) rather than guessing.
**E15 GUARD: track prime FACTORIZATION — 3⁵ (a power of 3) is NOT "5 appears"; only a
literal 5^k, 7^k, … with k≥1 in the denominator counts.** Outcome: 5 (or any prime ≠3)
appears at order N (101≤N≤200) => **RESOLVED-A: B685 REVERSED at depth N — the terminal
no-go falls, the generation leg reopens** (independently reproduced before believed) /
3-only through the reached order => RESOLVED-B (pattern holds to depth D, still unproved;
the precise GSWZ question is now well-posed) / the normalisation gap => RESOLVED-B(boundary).

## What this arc does NOT do
It does NOT send anything to the GSWZ authors (external act, owner-gated). It does NOT
make any physics claim. It is pure number theory about one element of the Habiro ring of
ℚ(√−3). A RESOLVED-A (5 appears) is extraordinary — it reverses the program's most
load-bearing negative — so it gets the escalated bar: independent in-cell reproduction +
a skeptic check + cc hand-verification + surfaced to the owner before banking.

## Method: the binding B771/B775 block; discriminating fact in-cell; no forced result
(a false "5 appears" is as bad as a false "3-only"); Gate 5/5-Q (no physics, no CLAIMS,
the one-number pin untouched); adversarial verify. Env pyenv python3.
