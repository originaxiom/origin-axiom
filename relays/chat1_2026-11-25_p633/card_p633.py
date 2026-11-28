#!/usr/bin/env python3
"""The decisive script of this seat's refiled claim card for P-633 (written 2026-11-28 for the queue's form;
data-free).

    python3 relays/chat1_2026-11-25_p633/card_p633.py              # decisive: exit 0 when the claim holds
    python3 relays/chat1_2026-11-25_p633/card_p633.py --control    # the failing control: must exit 1

It imports p633_switch.py from this folder (the sealed script of the old card, SHA-256 f697477746682401, unchanged),
runs its main() as it stands, and reads what it prints.

THE CLAIM, in p633_switch.py's terms: Mayer's transfer operator (L_s f)(x) = sum over n >= 1 of (x + n)^(-2s)
f(1 / (x + n)) on [0, 1], discretised by collocation at 32 Chebyshev nodes with the tail n > 60 taken by Hurwitz zeta
values (mpmath at 60 digits); lambda_1(s) its spectral radius. Read as a weight exp(-(c / 6 pi) l) per closed thread
of geodesic length l, the sum over threads converges iff lambda_1(c / 6 pi) < 1, so the critical c is 6 pi s*, with
lambda_1(s*) = 1.
  M1 (control) at s = 1, lambda_1 = 1 to 1e-12, and lambda_2 is the Gauss-Kuzmin-Wirsing constant to 1e-10;
  M2 (control) d log lambda_1 / ds at s = 1 is -pi^2 / (6 log 2) to 1e-6;
  M3 lambda_1(s) - 1 changes sign once on s = 0.80, 0.85, ..., 1.20, at s* within 1e-10 of 1: so c* = 6 pi.
  What is not claimed here: the reading of P-633's c as such a weight, and the clock (under B1813's move clock the
  same s* gives 6 pi log 2); both are the card's hypotheses. The record's sweep is the card's, not this script's.

CONDITION, written before this script's first run (its expectation is the sealed output p633_switch_out.txt,
SHA-256 3b1f1ebc5630dee4):
  D1 M1 within its tolerances, lambda_2 = -0.30366300289873 to 14 digits;
  D2 M2 within its tolerance, the derivative -2.37313822083125;
  D3 M3: the signs of lambda_1(s) - 1 on the grid are +, +, +, +, +, -, -, -, - (the value at s = 1 is 5.12e-28 and
     positive), one sign change, s* within 1e-10 of 1, c* = 18.8495559215 to 10 decimals;
  D4 the verdict: M1 to M3 hold, so the script exits 0.
  The control: M3's check run on the operator with its weight made wrong on purpose, (x + n)^(-3s) in place of
  (x + n)^(-2s); its leading eigenvalue at s is lambda_1(3s/2) of the true one, which is below 1 at every s of the
  grid. No sign change, so M3 fails, and the control exits 1, with no traceback. Any other pattern is reported as
  found, and the card is not filed.

Six lines are marked "DECISIVE:".
"""
import contextlib
import io
import re
import sys

import mpmath as mp

import p633_switch as P

M1 = re.compile(r"^M1 s = 1: lambda_1 = (\S+) \(\|lambda_1 - 1\| = (\S+)\); lambda_2 = (\S+) \(\|lambda_2 - GKW\| = (\S+)\);")
M2 = re.compile(r"^M2 d log lambda_1 / ds at s = 1: (\S+); -pi\^2/\(6 log 2\) = (\S+); difference (\S+)$")
M3V = re.compile(r"^M3 lambda_1\(s\) - 1 on s = 0\.80, 0\.85, \.\.\., 1\.20: (.*)$")
M3S = re.compile(r"^M3 one sign change; s\* = (\S+) \(\|s\* - 1\| = (\S+)\); c\* = 6 pi s\* = (\S+)$")
SUMMARY = re.compile(r"^(M1 \w+, M2 \w+, M3 \w+)$")


def switch_check(values, star):
    """M3's check: one sign change on the grid, and s* within 1e-10 of 1"""
    changes = sum(1 for a, b in zip(values, values[1:]) if a * b < 0)
    return changes == 1 and star is not None and abs(star - 1) < 1e-10


def decisive():
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        P.main()
    lines = buf.getvalue().splitlines()
    got = [[m.groups() for m in map(p.match, lines) if m] for p in (M1, M2, M3V, M3S, SUMMARY)]
    if [len(g) for g in got] != [1, 1, 1, 1, 1]:
        print("p633_switch.py's output did not parse: %s" % [len(g) for g in got])
        return 2
    (l1, d1, l2, d2), (der, target, dd), (vals,), (star, ds, cstar), (summary,) = (g[0] for g in got)
    print("DECISIVE: M1 at s = 1: |lambda_1 - 1| < 1e-12: %s; lambda_2 = %s; |lambda_2 - GKW| < 1e-10: %s"
          % (float(d1) < 1e-12, l2[:16], float(d2) < 1e-10))
    print("DECISIVE: M2 d log lambda_1 / ds at s = 1 = %s; -pi^2/(6 log 2) = %s; within 1e-6: %s"
          % (der, target, float(dd) < 1e-6))
    v = [float(x) for x in vals.split(", ")]
    print("DECISIVE: M3 signs of lambda_1(s) - 1 on s = 0.80, 0.85, ..., 1.20: %s" % " ".join("+-"[x < 0] for x in v))
    ok = switch_check(v, float(mp.mpf(star))) and summary == "M1 holds, M2 holds, M3 holds"
    print("DECISIVE: M3 one sign change; |s* - 1| < 1e-10: %s" % (float(ds) < 1e-10))
    print("DECISIVE: c* = 6 pi s* = %.10f" % float(mp.mpf(cstar)))
    print("DECISIVE: verdict: %s (%s)" % ("the claim holds" if ok else "the claim FAILS", summary))
    return 0 if ok else 2


def control():
    """M3's check on the operator with its weight (x + n)^(-3s): its spectrum at s is the true one at 3s/2"""
    xs = P.nodes()
    w, Vinv = P.lagrange_tables(xs)
    grid = [mp.mpf("0.8") + mp.mpf("0.05") * k for k in range(9)]
    wrong = lambda s: P.spectrum(mp.mpf(3) / 2 * s, xs, w, Vinv)[0] - 1
    vals = [wrong(s) for s in grid]
    changes = [(grid[k], grid[k + 1]) for k in range(8) if vals[k] * vals[k + 1] < 0]
    star = mp.findroot(wrong, changes[0], solver="anderson", tol=mp.mpf(10) ** -40) if len(changes) == 1 else None
    ok = switch_check([float(x) for x in vals], None if star is None else float(star))
    changes = len(changes)
    print("control: the weight made (x + n)^(-3s) on purpose: lambda_1 - 1 on the grid %s; sign changes %d; M3's check: "
          "%s" % (", ".join(mp.nstr(x, 4) for x in vals), changes,
                  "holds (the control has FAILED to fail)" if ok else "fails, as it must"))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(control() if sys.argv[1:] == ["--control"] else decisive())
