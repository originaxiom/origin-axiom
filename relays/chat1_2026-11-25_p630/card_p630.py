#!/usr/bin/env python3
"""The decisive script of this seat's refiled claim card for P-630 (written 2026-11-28 for the queue's form;
data-free: B1788's exponents are the record's own tropical prediction, and nothing is compared with data).

    python3 relays/chat1_2026-11-25_p630/card_p630.py              # decisive: exit 0 when the claim holds
    python3 relays/chat1_2026-11-25_p630/card_p630.py --control    # the failing control: must exit 1

It imports, from this folder and unchanged, the two sealed scripts of the old card: p630_trace.py (part B, SHA-256
b2bd98cf28cc8fba, at e30d17fc9) and p630_control.py (part A, SHA-256 2a5841e1c035ddc9, at d4c206878). It runs their
main() as they stand and reads what they print. The post hoc recounts in this folder are not run and not claimed.

THE CLAIM, at V = 0 (the free chain's end of B181's critical surfaces), in p630_trace.py's terms:
  (1) for m = 1 to 8 the metallic trace map T_m preserves I, fixes (1, 1, 1), and its spectrum there in the
      substitution's units is y = 0, -2, +2 (C1);
  (2) the six-cycle's Jacobian keeps the eigenvalue 1 at every V tried, and its multiplier at V = 0 is phi^6 (C2);
  (3) with one unit for every line, B1788's positive exponents over B1785's 41 lines are not in the V = 0 spectrum of
      all metallic directions: they are not all odd multiples of one common divisor, for the m2/m3 set alone and with
      the m1/m3 set (C6, "across all lines together"); and no line's m2/m3 and m1/m3 set together lies in one
      direction's spectrum u {2, -2} (C5, "both": 0 of 41);
  (4) part A, the method's control on the golden chain: the deviation read-out gives the leading thermal dimension
      h = 1/10 within 0.01 (A1), and at the sizes run (N up to 30) not h = 3/5 within 0.03 (A2).
  What is not claimed: anything inside the surfaces (V > 0), where C7 says one V matches any one ratio; and the per-line
  counts of the old card, which come from its post hoc recount.

CONDITION, written before this script's first run (its expectation is the sealed outputs p630_trace_out.txt, SHA-256
43ee8e61a828a612, and p630_control_out.txt, SHA-256 096b9e3c384aa6e8):
  D1 C1 on all eight m, with y = +0.000000 -2.000000 +2.000000 as printed;
  D2 C2: the eigenvalue 1 True, mu(0) printed equal to phi^6, mu increasing on [0, 10] True; C4 True on 246 cases;
  D3 C5: m2/m3 5 of 41, both 0 of 41; C6: m2/m3 14 of 41, both 0 of 41, across all lines together m2/m3 False and
     both False;
  D4 part A: A1 h = 0.09993, holds; A2 h = 0.50860, fails;
  D5 the verdict: (1) to (4) hold, so the script exits 0.
  The control: the claim's verdict with B1788's exponents replaced on purpose by a set that lies in the spectrum
  (every exponent 1/2, as on the lines alpha = 0 and 1/2 for m2/m3), checked by p630_trace.py's own odd_multiples()
  and all_equal(). Then (3) fails, and the control exits 1, with no traceback. Any other pattern is reported as found,
  and the card is not filed.

Fifteen lines are marked "DECISIVE:".
"""
import contextlib
import io
import re
import sys
from fractions import Fraction as Fr

import p630_control as A
import p630_trace as T

C1 = re.compile(r"^C1 m=(\d+): invariant (\w+), fixes \(1,1,1\) (\w+), charpoly .*; y = (\S+) (\S+) (\S+)$")
C2 = re.compile(r"^C2 eigenvalue 1: (\w+); mu\(0\) = (\S+) \(phi\^6 = (\S+)\); mu increases on \[0, 10\]: (\w+);")
C4 = re.compile(r"^C4 tropical m2/m3 = closed form in all (\d+) cases: (\w+)$")
C5 = re.compile(r"^C5 lines where the positive exponents are all equal: m2/m3 (\d+) of 41, both (\d+) of 41;")
C6 = re.compile(r"^C6 lines where the positive exponents are odd multiples of their gcd: m2/m3 (\d+) of 41, both (\d+) of "
                r"41; fails on alpha = 2/5 and 1/10 \(m2/m3\): (\w+); across all lines together: m2/m3 (\w+), both (\w+)$")
AH = re.compile(r"^(A1|A2): h = (\S+) \(target (\S+), tolerance (\S+)\) -> (holds|FAILS);")


def run(main):
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        main()
    return buf.getvalue().splitlines()


def grab(pattern, lines):
    return [m.groups() for m in map(pattern.match, lines) if m]


def verdict(c1_all, c2_one, c2_phi6, c5_both, together_m2, together_both, a1, a2):
    """the claim's verdict: (1) to (4) above"""
    return c1_all and c2_one and c2_phi6 and c5_both == 0 and not together_m2 and not together_both and a1 and not a2


def decisive():
    tr, co = run(T.main), run(A.main)
    c1, c2, c4, c5, c6 = (grab(p, tr) for p in (C1, C2, C4, C5, C6))
    ah = grab(AH, co)
    if [len(x) for x in (c1, c2, c4, c5, c6, ah)] != [8, 1, 1, 1, 1, 2]:
        print("the sealed scripts' output did not parse: %s" % [len(x) for x in (c1, c2, c4, c5, c6, ah)])
        return 2
    c1_all = True
    for m, inv, fix, *ys in c1:
        y = [round(float(v)) for v in ys]
        ok = inv == "True" and fix == "True" and sorted(y) == [-2, 0, 2]
        c1_all &= ok
        print("DECISIVE: C1 m = %s: preserves I %s, fixes (1, 1, 1) %s, y = %d, %d, %d" % (m, inv, fix, *y))
    one, mu0, phi6, incr = c2[0]
    print("DECISIVE: C2 the six-cycle keeps the eigenvalue 1: %s; mu(0) = phi^6: %s; mu increases on [0, 10]: %s"
          % (one, mu0 == phi6, incr))
    print("DECISIVE: C4 B1788's tropical m2/m3 equals its closed form in all %s cases: %s" % c4[0])
    print("DECISIVE: C5 lines whose positive exponents lie in one direction's spectrum: m2/m3 %s of 41, with m1/m3 %s "
          "of 41" % c5[0])
    n2, nb, pair, tog2, togb = c6[0]
    print("DECISIVE: C6 lines whose positive exponents are odd multiples of their gcd: m2/m3 %s of 41, with m1/m3 %s of "
          "41; all 41 lines under one unit: m2/m3 %s, with m1/m3 %s" % (n2, nb, tog2, togb))
    for name, h, target, tol, res in ah:
        print("DECISIVE: part A %s: h = %.3f, target %s within %s: %s" % (name, float(h), target, tol, res))
    ok = verdict(c1_all, one == "True", mu0 == phi6, int(c5[0][1]), tog2 == "True", togb == "True",
                 ah[0][4] == "holds", ah[1][4] == "holds")
    print("DECISIVE: verdict: %s" % ("the claim holds" if ok else "the claim FAILS"))
    return 0 if ok else 2


def control():
    """the claim's verdict with B1788's exponents replaced by a set that lies in the spectrum, every exponent 1/2"""
    half = [Fr(1, 2)] * 6
    sets = {al: (list(half), list(half)) for al in T.ALPHAS}
    c5_both = sum(T.all_equal(e2 + e3) for e2, e3 in sets.values())
    pos2 = sorted({x for e2, _ in sets.values() for x in e2 if x > 0})
    pos = sorted({x for e2, e3 in sets.values() for x in e2 + e3 if x > 0})
    ok = verdict(True, True, True, c5_both, T.odd_multiples(pos2), T.odd_multiples(pos), True, False)
    print("control: every exponent 1/2 on purpose: C5 with m1/m3 %d of 41; all lines under one unit: m2/m3 %s, with "
          "m1/m3 %s; the claim's verdict: %s" % (c5_both, T.odd_multiples(pos2), T.odd_multiples(pos),
                                                 "holds (the control has FAILED to fail)" if ok else "fails, as it must"))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(control() if sys.argv[1:] == ["--control"] else decisive())
