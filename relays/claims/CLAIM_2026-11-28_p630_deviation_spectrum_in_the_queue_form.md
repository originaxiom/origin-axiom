# CLAIM CARD — P-630 at V = 0: every metallic trace map T_m (m = 1 to 8) has the spectrum y = 0, −2, +2 at its cone point, and with one unit for every line B1788's exponents over B1785's 41 lines do not lie in the cone points' spectrum; the golden chain's control recovers h = 1/10 by the deviation read-out and, up to N = 30, not h = 3/5 (the seat's card of 2026-11-25 in the queue's form)

- card id: new
- seat code: fam1-v1-unset-03
- seat, branch, commit: fam1-v1-unset-03, chat1/web-seat, 0a89dddd2fa84dda59eb6c77ebd3b114f78050db
- kind: negative
- touches: P-630, P-629
- effect: conditions — P-630's lead (Q1): at the free chain's end of B181's critical surfaces, with one unit for every
  line, B1788's exponent set is not in the cone points' spectrum of T_1 to T_8; the six-cycle and other orbits are not
  tested, and inside the surfaces (V > 0) the comparison is not posed
- scope: frame: B471's metallic trace maps T_1 to T_8 on B181's critical surfaces I = V, at V = 0; object: the
  linearised spectrum at the cone point (1, 1, 1), against B1788's exponent set on B1785's 41 slopes (the six-cycle's
  eigenvalue 1 and multiplier are checked, not compared); reach: class; hypotheses: one unit u > 0 for every line,
  converting Im τ to the substitution's units; the m2/m3 set alone and with the m1/m3 set; for part A, the golden
  chain's rings of N = 12 to 30 sites. The verdict's criteria were chosen after the sealed output, whose own cells
  missed their expectations: C5 5 of 41 against at most 3, C6 14 of 41 against fewer than 10, and part A's A2 0.509
  against 3/5, so that the sealed control printed "the control passes: False"
- identifications: none
- definitions: T_m(x, y, z) = (y, U_{m−1}(y) z − U_{m−2}(y) x, U_m(y) z − U_{m−1}(y) x), with U_n the Chebyshev
  polynomials of the second kind, preserves I = x² + y² + z² − 2xyz − 1; y = ln|μ| / ln λ_m per step for an
  eigenvalue μ of its Jacobian at a periodic point, λ_m = (m + √(m² + 4))/2. B1788's exponents are the leading
  exponents of m2/m3 and m1/m3 in the up, down and lepton sectors and both readings, by its tropical prediction,
  copied verbatim into p630_trace.py. A line's set lies in one direction's spectrum if every positive exponent is u·y
  for one u and y in {2, −2}, so if they are all equal; in the cone-point spectrum of T_1 to T_8 together only if each
  is an odd multiple of their greatest common divisor (ln λ_m / ln λ_n is rational only within one quadratic field,
  where it is a ratio of odd integers). The decisive script reads each y rounded to an integer from the sealed print.
  Part A: on a ring of N Fibonacci anyons (the golden chain, B220), V_μ = Σᵢ (1 − lᵢ), the number of identity
  labels; h = (1 − s)/2 from the fit ln|⟨φ|V_μ|0⟩| = b + s ln N + c/N + d/N² over N = 12, 14, ..., 30, with φ the
  first excited k = 0 level for A1 (ε, h = 1/10) and the second for A2 (ε′, h = 3/5).
- imports: that ln λ_m / ln λ_n, for the metallic means λ_m, is rational only when λ_m and λ_n lie in one quadratic
  field, and is then a ratio of odd integers (the metallic means are odd powers of the field's unit of norm −1);
  standard number theory, stated in p630_trace.py's C6 and not re-derived
- premises on main: B181 (permanent criticality), B160 (κ = 2 + λ², so I = λ²/4), B471 (the metallic family), B107
  (the single scale), B1788 (the closed form), B1785 (the 41 line slopes), B220 and B222 (the golden chain's c and
  content)
- decisive script: relays/chat1_2026-11-25_p630/card_p630.py, SHA-256 6adb64d4a619a0dc, depends on the standard library,
  numpy, scipy and sympy, run as python3 relays/chat1_2026-11-25_p630/card_p630.py, output SHA-256 b1be3b6d5162e177
- decisive lines: 15 lines marked "DECISIVE:", SHA-256 ae82cde688ec2a31
- failing control: python3 relays/chat1_2026-11-25_p630/card_p630.py --control
- second computation: none that shares no code. Within the sealed p630_trace.py, the six-cycle's multiplier is
  computed exactly from the Jacobian and, independently, from band widths of direct transfer-matrix products (C3,
  agreeing to about 1e-10); the cone point's spectrum is exact symbolic algebra. The decisive script runs the sealed
  p630_trace.py (SHA-256 b2bd98cf28cc8fba) and p630_control.py (SHA-256 2a5841e1c035ddc9) unchanged.
- already on main?: topic_sweep.py "deviation spectrum|deviation direction" at 68b04c69d: no arc, and P-630's own
  row; "metallic trace map": no arc, one register row. No arc compares a trace map's spectrum with B1788's exponents
- what would make it fail: a cone-point spectrum other than y = 0, 2, −2 for some m of 1 to 8; a unit under which
  every line's positive exponents are odd multiples of one divisor; a line whose m2/m3 and m1/m3 exponents are all
  equal; or, for part A, h away from 1/10. The control replaces B1788's exponents on purpose by 1/2 on every line,
  a set that lies in the cone points' spectrum; p630_trace.py's own odd_multiples() and all_equal() then say so, and
  the claim's verdict fails. It is an easy control, but it runs the sealed checks.
