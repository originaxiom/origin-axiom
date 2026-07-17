# CELL G — L100 CERTIFIED: THE RESONANT-PHASE LAW — THE MELODY'S EXACT MINIMAL PERIOD

**VERDICT: CERTIFIED (sealed outcome 1). The E6 Z-ladder's exact minimal
period is**

    P = 175560 = 2^3 * 3 * 5 * 7 * 11 * 19          (N0 / P = 13,167,000)

**with the closed form: P = the exponent of the total discriminant group —
the lcm of ALL Smith elementary divisors of the 25 Weyl classes' B_w =
3I − w − w⁻¹ (per-prime caps 2:3, 3:1, 5:1, 7:1, 11:1, 19:1).** The melody
theorem's period N0 = 2⁶·3³·5⁴·7²·11²·19² compresses by a factor of
13,167,000; the ladder's complete information content is 175,560 rungs.

## The certificate structure (subsumes the gamma identification at resonant rungs)

Every class term is a finite character sum with EXACT rational frequencies:
G_w(r) = Σ_q n^w_q·e^{−iπrq}, where the multiset {q(μ) mod 2} (μ over the
banked HNF box, q = μᵀC6B_w⁻¹μ) is computed as exact Fractions with integer
counts — this is the complete phase data of every jumped term at every
resonant rung across all unit classes at once. Aggregated over the 25
classes, Z(r) = Σ_q N_q·e^{−iπrq} with N_q = A_q + B_q√5, A_q, B_q ∈ Q
exact (only squarefree classes s = 1, 5 occur; √5-independence over Q
decides N_q = 0 exactly). There are **130 supported q and ZERO aggregate
cancellations** (lcm of per-class periods = aggregate period — the
resonant-phase law needs no cross-class conspiracy). By linear independence
of distinct characters (Artin), d is a period of Z iff d·q ∈ 2Z for every
supported q; the periods form P·Z with P = lcm ord(q) = 175560. Exact
arithmetic in every decisive step; numerics only at gate evaluation
(house pattern: dps 50, quantize 1e-30).

## Gates — 12/12 PASS (cellG_output.txt)

- **A0** class table == banked jeffrey_terms.json (25 classes; size/sign/det exact).
- **B** 2-representative EXACT q-multiset equality per class (exact class function).
- **A1** verbatim banked gauss_sum vs multiset evaluation: max dev 1.3e-13 (r = 13, 19).
- **P1** G(13), G(29) = ζ₈^j·√|det| against cc2's banked p1_certificates.json:
  max dev 2.2e-48 at dps 50 (50/50 exact-quantized).
- **F1** the uniform jump law |G(r)|² = Π p^(a+min(v_p(r),a)) over SNF divisors:
  150/150 integer-quantized at 1e-30 (r ∈ {13,16,19,20,45,57}).
- **A2** totals: Z(13)=1, Z(16)=0, Z(19)=2, and the generic law at 17, 23, 29
  (devs ≤ 5e-51 at dps 50).
- **C** P | N0 (melody theorem) and 5 | P (B656/G2 generic-5): both exact.
- **D** Z(κ) = Z(κ+P) on the D2 sealed rung set {13,29,16,25,19,45}: dev exactly 0
  (per-class route, dps 30).
- **E** minimality witnesses — every maximal proper divisor P/p FAILS on the
  physical ladder (κ ≥ 13), certified at dps 50, plus an algebraic q* each:

  | p | d = P/p | κ | Z(κ) | Z(κ+d) | q* (ord) |
  |---|---------|---|------|--------|----------|
  | 2 | 87780 | 20 | 1 | 2−√5 | 11/20 (40) |
  | 3 | 58520 | 13 | 1 | 0 | 7/12 (24) |
  | 5 | 35112 | 13 | 1 | 0 | 22/35 (35) |
  | 7 | 25080 | 14 | 1 | 0 | 22/35 (35) |
  | 11 | 15960 | 22 | 2 | 0 | 6/11 (11) |
  | 19 | 9240 | 13 | 1 | 3 | 14/19 (19) |

- **closed form** P == lcm of all elementary divisors (exact).
- **value ring** 22/22 showcase rungs quantize in Z[√5] at 1e-30 (dps 50).

Since periods form a group, refuting each P/p refutes every proper divisor;
witnesses at κ ≥ 13 make minimality hold on the physical ladder domain, not
just the abstract Z-extension.

## Structure read off the certificate (new facts)

- **The dyadic economy:** the naive phase bound would allow a 2⁴ component
  (ord 2b at odd numerator); the deepest dyadic q (denominator 8-part) all
  carry EVEN numerators, so the dyadic cap is exactly the elementary-divisor
  cap 2³ — F1's even-type 2-adic mechanism, now visible in the phase data.
- **Resonant values live in Z[√5]:** −√5 at κ = 35, 70; 2−√5 at 30, 40;
  1−√5 at 55, 60; Z = 2 at every multiple of 19 (19, 38, 57, 76, 95);
  Z(48) = Z(72) = 3; Z(36) = −2, Z(63) = −1. Generic rungs stay at
  (1−(κ|5))/2 ∈ {0, 1}.
- **P = 5 · 35112:** the generic-5 (= disc(A1), the B204 cross-stage
  coincidence) times the resonant enrichment 2³·3·7·11·19.
- **Correction note for G2's parenthetical:** B656/G2 quoted jump caps
  "(2:3, 3:2, 5:3, 7:1, 11:1, 19:1)". The SNF elementary-divisor caps are
  (2:3, 3:1, 5:1, 7:1, 11:1, 19:1) — the 3:2/5:3 figures match det-valuation
  shorthand, not elementary divisors (e.g. det 125 = 5³ has divisors
  [5,5,5]; det 81 = 3⁴ has [3,3,3,3]). N0's 3³·5⁴ shape was safe overkill;
  the melody needs 3¹·5¹ only. G2's hedge ("p^(cap+1)-ish") is resolved here.

## Run notes

Run 1 (cellG_output_run1.txt): phases 0–5, verdict CERTIFIED, 10/10 gates.
Run 2 (cellG_output.txt): identical code path + addendum phase 5b (closed
form + value-ring quantization), verdict unchanged, 12/12 gates. Both
outputs preserved byte-faithfully. Repo untouched; no tracked file modified.

Machinery provenance: weyl_group/C6 verbatim from
frontier/B600_level_ladder/packet/scripts/engine.py; bucket construction and
gauss_sum verbatim from frontier/B646_wave2_integration/cc2_packets/
next_queue/next_queue/n1_counting/n1_jeffrey_terms.py (P_WORD = 3); banked
cross-gate inputs: jeffrey_terms.json (B646) and p1_certificates.json (B651).

## Files

- frontier/B662_successor_campaign/cellG/l100_period.py — the certifier.
- frontier/B662_successor_campaign/cellG/l100_results.json — machine-readable
  certificate: the 130-line support table (q, ord, exact Q-coefficients of 1
  and √5), per-class exact multisets, SNF divisors, witnesses, gates.
- frontier/B662_successor_campaign/cellG/cellG_output.txt (+ _run1.txt) — full
  run output.
