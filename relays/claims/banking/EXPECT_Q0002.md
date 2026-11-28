# EXPECT_Q0002 — sm2 (fam1-v1-unset-05), committed before any run

Card: Q0002, `relays/claims/CLAIM_2026-11-27_B2012_main_trial.md` on main at 0fd0a70f43722056a17992667016a31b34cfb1d3.
Written from the card and its queue record alone, before reading or running the card's script and before running any code
for this card. Not read: the peer's note, the other banking seat's branch, B2012's files.

## By hand, before any run (so that the cited theorem is derived, not cited: K4)
- Push-forwards compose: P(g h) = P(g) P(h). With L = sigma C^2 and R = sigma C as maps, and sigma an involution,
  L^-1 = C sigma and R^-1 = C^2 sigma, so T4 = S C^2 + S C + C S + C^2 S = S(C + C^2) + (C + C^2) S, and C + C^2 = 3P - 1,
  so T4 = 3(SP + PS) - 2S. This needs C and sigma to map the orbit to itself; I will check that on every orbit.
- With Q = (1 + S)/2, T4 = 6(QP + PQ) - 6P - 4Q + 2. On a two-dimensional block of the two projections, with P = diag(1, 0)
  and Q of angle c = cos^2 (0 < c < 1), T4 = [[8c - 4, 2s], [2s, 4c - 2]] with s^2 = c(1 - c): trace 12c - 6, determinant
  36c^2 - 36c + 8, eigenvalues 6c - 2 and 6c - 4. A = 3P(1 + S)P = 6PQP has the eigenvalue 6c there. So each root mu of R
  gives T4 the roots mu - 2 and mu - 4: the factor R(x + 2) R(x + 4). The one-dimensional pieces give 4 on P and Q
  (A = 6, d1), -4 on P not Q (A = 0, d2), -2 on Q not P (d3) and 2 on neither (d4), with rank Q = (n + f_S)/2: the
  card's d3 and d4.
- So the law should hold on every orbit on which C and sigma act, which is what I expect to find.

## What I will compute, my own code
On every orbit of every leaf mod 7, 11 and 13 (the card does not say which leaf; all of them covers its six orbits and
more), and on the orbit of (3,3,3) mod 27, 81 and 135: that C and sigma preserve the orbit; that T4 = 3(SP + PS) - 2S as
matrices, exactly; A, d1, d2, R, f_S, d3, d4; and the characteristic polynomial of T4 against
R(x+4) R(x+2) (x-4)^d1 (x+4)^d2 (x+2)^d3 (x-2)^d4, exactly where the size allows and modulo primes at 135.
Control (K8): the same comparison with a wrong pairing (R(x+4) R(x+1)) or with sigma replaced by X must fail.

## Expectation
ACCEPT, with the effect read as a law of the moves' algebra (it holds wherever L = sigma C^2, R = sigma C act on an orbit
closed under C and sigma), which the card calls a law of the modular group. REFUSE if the characteristic polynomial differs
on any orbit, or if C or sigma does not preserve one of the card's orbits (the law would then not apply there as stated).
