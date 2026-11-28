#!/usr/bin/env python3
"""The decisive script of this seat's B1977 card in the queue's form (written 2026-11-28, as main's M88 asks: main's
frame copied in; data-free, nothing compared with data).

    python3 relays/chat1_2026-11-28_b1977/card_b1977.py              # decisive: exit 0 when the claim holds
    python3 relays/chat1_2026-11-28_b1977/card_b1977.py --control    # the failing control: must exit 1

It imports chk1b_independent.py from this folder: the seat's sealed second computation of 2026-11-24 (f77dae59f),
with W-D2's referee's frame code (chk1_ref_frame.py) and CHK-1's points (chk1_run.py, 7dc9cdf67) beside it, and main's
B1940 frame_mp at 88a1e9474 with every file it loads, copied by build_b1977.py (verbatim but for the loaders;
MANIFEST.md lists each replaced line). It runs that script's main() and captures what it prints. The copy's test is
that the capture equals the sealed output relays/chat1_2026-11-24_chk1/chk1b_out.txt (SHA-256 785d259ba76449fb),
byte for byte.

THE CLAIM. At 16 of B1977's 96 points of order 30 (its five slow points and every eighth), at column 0.13 and heights
20 and 30, reading S in every sector: the nine rates (the six within-sector ratios' and the three moduli |V12|,
|V23|, |V13|'s log-slopes between the two heights, over 10 pi) and the least diagonal modulus at height 30, computed
by W-D2's referee's assembly (its own theta sums, eta by product, coupling, and singular values from the Hermitian
eigenproblem of Y Y^H at 40 + 4 Im tau digits; it shares with main's frame only F_u, the canonical end's table, the
triplet's q-series and the charges), equal B1977's committed table rates30_run.json exactly in double precision:
the largest difference of a rate is 0, and of the least diagonal 0.

CONDITION, written before this script's first run:
  D1 the capture equals the sealed output byte for byte;
  D2 its 16 point lines and its summary line are the decisive lines, the summary reading 16 points, largest rate
     difference 0.00e+00 and largest diagonal difference 0.00e+00; the verdict holds, and the script exits 0.
  The control: the same comparison at the first point, (1/30, 1/15), against B1977's row for another point on
  purpose, (4/15, 1/30). The rates then differ, the check fails, and the control exits 1, with no traceback. Any
  other pattern is reported as found, and the card is not filed.

Nineteen lines are marked "DECISIVE:".
"""
import contextlib
import io
import json
import os
import pathlib
import re
import sys

import chk1b_independent as K

HERE = pathlib.Path(__file__).resolve().parent
SEALED = HERE.parent / "chat1_2026-11-24_chk1" / "chk1b_out.txt"
TABLE = os.path.join(K.R.MAIN, "frontier", "B1977_order_30_rates_masses_and_mixing_on_one_grid", "verification",
                     "rates30_run.json")
SUMMARY = re.compile(r"^ADDENDUM: (\d+) points; largest rate difference (\S+); largest diagonal difference (\S+)$")


def decisive():
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        K.main()
    text = buf.getvalue()
    same = text.encode("utf-8") == SEALED.read_bytes()
    print("DECISIVE: the copy reproduces the sealed output of 2026-11-24 byte for byte: %s" % same)
    lines = text.splitlines()
    for l in lines:
        print("DECISIVE: %s" % l)
    m = [SUMMARY.match(l) for l in lines if SUMMARY.match(l)]
    ok = (same and len(m) == 1 and m[0].group(1) == "16" and float(m[0].group(2)) == 0.0
          and float(m[0].group(3)) == 0.0)
    print("DECISIVE: verdict: %s" % ("the claim holds" if ok else "the claim FAILS"))
    return 0 if ok else 2


def rates_at(a, b):
    A, B = K.snap(a, b, 20), K.snap(a, b, 30)
    mp = K.mp
    r = {}
    for s in ("up", "down", "lep"):
        r[s + "_m2m3"] = float(-(mp.log(B["r"][s][0]) - mp.log(A["r"][s][0])) / (mp.pi * 10))
        r[s + "_m1m3"] = float(-(mp.log(B["r"][s][1]) - mp.log(A["r"][s][1])) / (mp.pi * 10))
    for (i, j, n) in ((0, 1, "V12"), (1, 2, "V23"), (0, 2, "V13")):
        r[n] = float(-(mp.log(B["A"][i][j]) - mp.log(A["A"][i][j])) / (mp.pi * 10))
    return r


def control():
    from fractions import Fraction as Fr
    M = {(row["a"], row["b"]): row for row in json.load(open(TABLE))}
    r = rates_at(Fr(1, 30), Fr(1, 15))
    wrong = M[("4/15", "1/30")]                     # another point's row, on purpose
    d = max(abs(r[k] - wrong[k]) for k in K.KEYS if wrong[k] is not None)
    ok = d == 0.0
    print("control: the point (1/30, 1/15) against the row of (4/15, 1/30) on purpose: largest rate difference %.2e; "
          "the check: %s" % (d, "holds (the control has FAILED to fail)" if ok else "fails, as it must"))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(control() if sys.argv[1:] == ["--control"] else decisive())
