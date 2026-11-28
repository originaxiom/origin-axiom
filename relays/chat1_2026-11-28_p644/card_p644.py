#!/usr/bin/env python3
"""The decisive script of this seat's P-644 card in the queue's form (written 2026-11-28, as main's M88 asks: main's
frame copied in; data-free, nothing compared with data: the read-outs' values are compared only with each other, in
units of their sampling error). It runs for about an hour, so the card declares it heavy.

    python3 relays/chat1_2026-11-28_p644/card_p644.py              # decisive: exit 0 when the claim holds
    python3 relays/chat1_2026-11-28_p644/card_p644.py --control    # the failing control: must exit 1

It imports, from this folder, the seat's two sealed scripts of 2026-11-25: p644_rival.py (348e7874f) and its post hoc
follow-up p644_rival_posthoc.py (5b3ca3e7b, written after the first run's X3 failed its expectation), whose loaders
now import B1924's thread_average, fast_norm and B1724's covariance from main at 88a1e9474, copied beside them by
build_p644.py (verbatim but for the loaders; MANIFEST.md lists each replaced line). It runs both mains in turn and
captures what they print. It reports, without deciding on it, whether each capture equals its sealed output byte for
byte (relays/chat1_2026-11-25_p644/p644_rival_out.txt, SHA-256 eb77e9501d8d2f28, and p644_rival_posthoc_out.txt,
SHA-256 2ab2c6c9d8db65bb); the decisive lines are the claim's tests, with fractions to 3 decimals.

THE CLAIM, in p644_rival.py's terms (FL-04's object-against-rival null on frame C, in the log-ratio variant of B1924's
instrument; R_n the length-weighted average over 20 allowed words of n moves, n = 12 and 16 pooled, of each word's
thread average of the log ratios, at the line the object's mark gives; a component "differs" when the two read-outs
differ by more than 3 jackknife sampling errors):
  X1 the object enters only through its level and mark: LR (m004) has the single eigenline (1, 2) mod 5, -LR (m003)
     the same, and m003's read-out equals m004's exactly, word by word;
  X2 m004's read-out with a second seed differs from the first on fewer than 10 % of the compared components;
  X3 at p = 3 the rival +-LLLR differs from m004 on more than half of the compared components; at p = 7, at 40 words,
     on fewer than half (X3's expectation of more than half at both failed);
  F (post hoc) at p = 7 with 120 words, +-LLLR differs from m004 on a larger share than m004's second 120 words differ
     from its first, which differ on none: a real difference at level 7, smaller than at level 3.

CONDITION, written before this script's first run: each test above passes, the sealed run's cells read "X1 holds, X2
holds, X3 FAILS", the post hoc reading reads "the p = 7 difference is real", the verdict holds, and the script exits
0; each capture equals its sealed output byte for byte here (reported, not decided). The control: X1's check, an exact
equality of two read-outs, run on purpose on m004's read-out against m004's own read-out with a second seed (X2's).
They are not equal, the check fails, and the control exits 1, with no traceback. Any other pattern is reported as
found, and the card is not filed.

Ten lines are marked "DECISIVE:".
"""
import ast
import contextlib
import io
import pathlib
import re
import sys

import p644_rival as RV
import p644_rival_posthoc as PH

HERE = pathlib.Path(__file__).resolve().parent
OLD = HERE.parent / "chat1_2026-11-25_p644"


def run(main):
    argv = sys.argv
    sys.argv = ["x", "."]
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        main()
    sys.argv = argv
    return buf.getvalue()


def table(pattern, text):
    m = re.search(pattern + r": (\{.*\})$", text, re.M)
    return ast.literal_eval(m.group(1)) if m else None


def short(d):
    return "compared %d, dropped %d, differing %.3f" % (d["compared"], d["dropped"], d["frac_above_3"]) if d else "absent"


def decisive():
    rows = run(RV.main)
    post = run(PH.main)
    for name, text, sealed in (("p644_rival", rows, "p644_rival_out.txt"),
                               ("p644_rival_posthoc", post, "p644_rival_posthoc_out.txt")):
        print("(not decisive) %s's capture equals its sealed output byte for byte: %s"
              % (name, text.encode("utf-8") == (OLD / sealed).read_bytes()))
    lr = re.search(r"^X1 m004 \(LR\): .*mod 5 its eigenlines (\[.*?\]) \(of -w: (\[.*?\])\)$", rows, re.M)
    m3 = re.search(r"^X1 m003 \(-LR\): .*mod 5 its eigenlines (\[.*?\]) \(of -w: (\[.*?\])\)$", rows, re.M)
    marks_ok = bool(lr and m3) and lr.group(1) == m3.group(1) == "[(1, 2)]"
    print("DECISIVE: X1 the single eigenline mod 5 of LR and of -LR is (1, 2): %s" % marks_ok)
    x1 = table(r"^X1 m003 against m004", rows)
    x2 = table(r"^X2 m004, second seed against the first", rows)
    x37 = table(r"^X3 \+-LLLR at p = 7 against m004", rows)
    x33 = table(r"^X3 \+-LLLR at p = 3 against m004", rows)
    print("DECISIVE: X1 m003 against m004: %s; exactly equal: %s" % (short(x1), bool(x1) and x1["exact_equal"]))
    print("DECISIVE: X2 m004, second seed against the first: %s" % short(x2))
    print("DECISIVE: X3 +-LLLR at p = 3 against m004: %s" % short(x33))
    print("DECISIVE: X3 +-LLLR at p = 7 against m004: %s" % short(x37))
    cells = re.search(r"^(X1 \w+, X2 \w+, X3 \w+)$", rows, re.M)
    print("DECISIVE: the sealed run's cells: %s" % (cells.group(1) if cells else "absent"))
    f2 = table(r"^F2 LLLR at p = 7 against m004 at the mark, 120 words", post)
    f3 = table(r"^F3 m004 at the mark, a second 120 words against the first", post)
    print("DECISIVE: F (post hoc) +-LLLR at p = 7 against m004, 120 words: %s" % short(f2))
    print("DECISIVE: F (post hoc) m004, a second 120 words against the first: %s" % short(f3))
    reading = re.search(r"^reading: (.*)$", post, re.M)
    print("DECISIVE: F (post hoc) reading: %s" % (reading.group(1) if reading else "absent"))
    ok = (marks_ok and bool(x1) and x1["exact_equal"] and bool(x2) and x2["frac_above_3"] < 0.10
          and bool(x33) and x33["frac_above_3"] > 0.5 and bool(x37) and x37["frac_above_3"] <= 0.5
          and bool(cells) and cells.group(1) == "X1 holds, X2 holds, X3 FAILS"
          and bool(f2 and f3) and f2["frac_above_3"] > f3["frac_above_3"] and f3["frac_above_3"] == 0.0
          and bool(reading) and reading.group(1) == "the p = 7 difference is real")
    print("DECISIVE: verdict: %s" % ("the claim holds" if ok else "the claim FAILS"))
    return 0 if ok else 2


def control():
    """X1's exact-equality check, on purpose on m004 against its own read-out with X2's second seed"""
    argv = sys.argv
    sys.argv = ["x", "."]
    with contextlib.redirect_stdout(io.StringIO()):
        T, C = RV.load(".")
        a = RV.readout(T, C, (1, 2), 5, 20261125 + 5)
        b = RV.readout(T, C, (1, 2), 5, 777)
        c = RV.compare(b, a)
    sys.argv = argv
    ok = c["exact_equal"]
    print("control: m004 against its own read-out with a second seed, on purpose: %s; exactly equal: %s; X1's check: %s"
          % (short(c), c["exact_equal"], "holds (the control has FAILED to fail)" if ok else "fails, as it must"))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(control() if sys.argv[1:] == ["--control"] else decisive())
