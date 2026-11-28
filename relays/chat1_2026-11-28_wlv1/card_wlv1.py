#!/usr/bin/env python3
"""The decisive script of this seat's W-LV1 card in the queue's form (written 2026-11-28, as main's M88 asks: main's
code copied in; data-free, nothing compared with data).

    python3 relays/chat1_2026-11-28_wlv1/card_wlv1.py              # decisive: exit 0 when the claim holds
    python3 relays/chat1_2026-11-28_wlv1/card_wlv1.py --control    # the failing control: must exit 1

It imports w_lv1_level.py from this folder: the seat's sealed script of 2026-11-25 (3b44d1337), whose load() now does
only the plain import of determinant_law, with main's frame at be8c83d4f copied beside it by build_wlv1.py (every
file verbatim but its loaders; MANIFEST.md lists each replaced line). It runs that script's main() and captures what
it prints. The copy's test is that the capture equals the sealed output relays/chat1_2026-11-25_level/
w_lv1_level_out.txt (SHA-256 f5639dec60f37e4b), byte for byte.

THE CLAIM, in w_lv1_level.py's terms (B1976's unit rule: sectors s and t tie at level N when a unit k of Z/N carries
s's charge pair to t's, k p = q mod N, directly or swapped; a self pair counts only swapped; the charge pairs are
frame C's 6Y charges, up (1, -4), down (1, 2), lep (-3, 6)):
  T2 for N = 2 to 420, the levels with a whole-level tie are exactly 2, 3, 4, 5, 6, 7, 9 and 15, and with a pointwise
     tie (k = 1 or -1) exactly 2 to 7 and 9; the primes with a tie at some power are 2, 3, 5 and 7; the multiplets'
     charge differences are 1, 4, 5, 6, 9, 10, with primes 2, 3 and 5;
  T3 the three principles fixed before the old run give P1 = 210, P2 = 30, P3 = 10;
  C1 on frame C's coupling (column 0.13, height 6, reading S), each of the four ties the rule finds (N = 5, 6, 7, 15)
     holds pointwise to 1e-12 at two points, and the negative control at order 30 tells (down, lep) apart (> 1e-3);
  so the reading is R2: the tie arithmetic does not single out level 30.

CONDITION, written before this script's first run:
  D1 the capture equals the sealed output byte for byte;
  D2 the decisive lines restate T2, T3, C1 and the reading as above; the verdict holds, and the script exits 0.
  The control: T2's check, the whole-level tie levels for N = 2 to 420 being exactly the claim's eight, run on purpose
  with the lepton pair's charge made (-3, 5) in place of (-3, 6), through the copy's own table(). The tie levels then
  differ, the check fails, and the control exits 1, with no traceback. Any other pattern is reported as found, and the
  card is not filed.

Thirteen lines are marked "DECISIVE:".
"""
import contextlib
import io
import pathlib
import re
import sys

import w_lv1_level as W

HERE = pathlib.Path(__file__).resolve().parent
SEALED = HERE.parent / "chat1_2026-11-25_level" / "w_lv1_level_out.txt"
CLAIM_TIES = [2, 3, 4, 5, 6, 7, 9, 15]


def tie_levels(charges):
    T = W.table(charges)
    return [N for N, row in T.items() if any(v["whole"] for v in row.values())]


def decisive():
    argv = sys.argv
    sys.argv = ["w_lv1_level.py", "."]           # its main() reads its argument only to pass it to load()
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        W.main()
    sys.argv = argv
    text = buf.getvalue()
    same = text.encode("utf-8") == SEALED.read_bytes()
    print("DECISIVE: the copy reproduces the sealed output of 2026-11-25 byte for byte: %s" % same)
    lines = text.splitlines()
    pick = lambda prefix: [l.strip() for l in lines if l.strip().startswith(prefix)]
    for l in pick("T2 ") + pick("T3 "):
        print("DECISIVE: %s" % l)
    for l in pick("N = ") [-4:]:
        m = re.match(r"N = +(\d+): (Y_\w+\(w\) against Y_\w+\(\d+ w\)): the rule finds (.*); differences .* -> (\S+)$", l)
        print("DECISIVE: C1 N = %s: %s, the rule finds %s -> %s" % m.groups() if m else "DECISIVE: C1 unparsed")
    neg = pick("negative control")
    print("DECISIVE: C1 the negative control at order 30: %s" % (neg[0].rsplit("-> ", 1)[-1] if neg else "absent"))
    reading = pick("READING:")
    print("DECISIVE: %s" % (reading[0] if reading else "READING: absent"))
    ties = [int(x) for x in re.findall(r"\d+", (pick("T2 levels with a whole-level tie:") or [""])[0])]
    ok = (same and ties == CLAIM_TIES and reading == ["READING: R2 (P1 = 210, P2 = 30, P3 = 10)"]
          and all(l.endswith("-> holds") for l in pick("N = ")[-4:]) and bool(neg) and neg[0].endswith("-> passes"))
    print("DECISIVE: verdict: %s" % ("the claim holds" if ok else "the claim FAILS"))
    return 0 if ok else 2


def control():
    charges = {s: (W_B.SIXY[W_B.SECTORS[s][0]], W_B.SIXY[W_B.SECTORS[s][1]]) for s in W.SECS}
    charges["lep"] = (charges["lep"][0], 5)       # made wrong on purpose: 6 in the frame
    got = tie_levels(charges)
    ok = got == CLAIM_TIES
    print("control: the lepton pair made %s on purpose: whole-level ties at %s; T2's check: %s"
          % (charges["lep"], got, "holds (the control has FAILED to fail)" if ok else "fails, as it must"))
    return 0 if ok else 1


if __name__ == "__main__":
    if sys.argv[1:] == ["--control"]:
        W_B = W.load(".").B
        sys.exit(control())
    sys.exit(decisive())
