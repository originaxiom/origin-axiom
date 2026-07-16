# P1+P2 — BANKED: THE GENERIC-RUNG LAW CERTIFIED EXACTLY (cc2, 2026-07-16)

P1 CERTIFICATION (p1_certificates.json; zero floats): each of the 25 Weyl classes'
generic Gauss sums computed as exact integer cyclotomic vectors at r = 13
((13|5) = -1) and r = 29 ((29|5) = +1) and identified EXACTLY as sqrt|A_w| * zeta_8^j
(Milgram shape): every gamma_w in {+1, -1} (exponents 0/4 only — all signatures
trivial or 4 mod 8). The three identities hold as EXACT Q(zeta_8) arithmetic:
  total(13) = 1;  total(29) = 0;  trivial sector = 1/2;  chi5 sector = 1/2;
  twist gamma(29)/gamma(13) = -1 on all ten chi5 classes, +1 on all fifteen others.
=> **Z_generic(kappa) = (1 - (kappa|5))/2 is now certified at both symbol values as
an exact algebraic identity**; the extension to all generic kappa rests only on the
cited multiplier-twist lemma (Milgram/Wall — known; lit-gated in Q3) plus the banked
mod-8 invariance datum (the 13/17/23 equality: 5, 1, 7 mod 8 all agree).

THE JEWEL (new, exact, from the certificate table): det(w) = (-1)^{v5(det B_w)} —
the Weyl SIGN character coincides with the 5-parity of the class's fixed-point
count, on all 25 classes. This is WHY the sectors each weigh exactly 1/2 (the chi5
sector IS the odd Weyl classes) and why every class contributes +size/|W| at
(kappa|5) = -1. The sign-equals-golden-parity identity is E6+A1-specific structure
tying the Weyl group's parity to disc(A1) = 5; proposed as a NOTICED row with its
own one-line exact check (the table).

P2 ASSEMBLY (the jump law's proof shape, riding the same local machinery): on each
local factor Z/p^a with multiplier p^v u, the reduced form's radical has index
p^{a - min(v,a)}, giving local magnitude p^{(a + min(v,a))/2} vs generic p^{a/2} —
the ratio p^{min(v,a)/2} per elementary divisor, which is L3's uniform law verified
300/300 (Q3) and now 6/6 more at the D2 congruent pairs. Status: proof-by-local-
computation with every instance exact-verified; the remaining write-up is the
2-adic case's bookkeeping (standard but fiddly) — one focused session, priced.

P3 (P3_NOTE.md): the PSL-factoring statement assembled — one proven instance
(k=2, Q2), two consistent banked instances (k=6 kernel, k=7 vacuity), the stage
invariance reading, and the one priced step to theorem (decompose the k=6 odd
block under SL(2,4) x SL(2,27); exact matrices already banked).
Artifacts: p1_milgram.py, p1_certificates.json, p1_run.log. Repo untouched.
