#!/usr/bin/env python3
"""The decisive script of this seat's P-589 (c) card in the queue's form (written 2026-11-28, as main's M88 asks: main's
code copied in; data-free, nothing compared with data). It runs for about half an hour, so the card declares it heavy.

    python3 relays/chat1_2026-11-28_p589c/card_p589c.py              # decisive: exit 0 when the claim holds
    python3 relays/chat1_2026-11-28_p589c/card_p589c.py --control    # the failing control: must exit 1

It imports, from this folder, the seat's two sealed scripts of 2026-11-25: p589c_exact_rows.py (e52f68352) and its
deciding post hoc check p589c_posthoc3.py (41e0fcbd2, written after the old referee read, so not blind), whose loaders
now import B1838's instrument and every file it loads from main at 88a1e9474, copied beside them by build_p589c.py
(verbatim but for the loaders; MANIFEST.md lists each replaced line). It runs both mains in turn and captures what they
print. It also reports, without deciding on it, whether each capture equals its sealed output byte for byte
(relays/chat1_2026-11-25_p589c/p589c_exact_rows_out.txt, SHA-256 3f42cff85160b580, and p589c_posthoc3_out.txt, SHA-256
3581f09ea8a456ad): floating-point noise in the last printed digit could differ on another machine, so the decisive
lines are the claim's tests and rounded values.

THE CLAIM, in those scripts' terms (each law-map row re-read at B1838's exact horoball norms, the small-cut norms from
B1667's column beside them):
  P0 B1838's instrument reproduces B1667's committed json at 0.25 + 3.0i within 1e-6;
  row 315 (B1701's degeneracy, P1): on the tied lines, max |m2/m3 - 1| stays below 1e-12 at both norms, and the
     small-exact difference below 1e-8;
  row 324 (B1729's negative, P3): the order-5 worst |R - 1| at the exact norms is below 1e-8, and the median log R2
     on the 3|N lines moves from 0.178 to 0.145, far from log 3;
  with the accessory parameter on its uniformising branch on Re tau = 0 (post hoc, not blind; B1667's track() returns
  a stuck c there without error): Q0 the stuck c reproduces the committed order-12 residue 8.814e-10; Q1 P1's 1.6i
  half holds; Q2 every exact order-12 lepton m1/m3 is at most 1e-12 on all 48 lines (B1712's zero holds), and every
  exact order-9 lepton m1/m3 is above 1e-12 on all 36 lines (B1711's lift);
  and the sealed run's own cells read "P0 holds, P1 holds, P2 FAILS, P3 holds", its P2 failing on the stuck c.

CONDITION, written before this script's first run: every test above passes, the verdict holds, and the script exits
0; and each capture equals its sealed output byte for byte here (reported, not decided). The control: the order-12
check run with the accessory parameter left stuck on purpose, as at_tau() returns it at 3.1i, over the 48 lines. The
largest exact lepton m1/m3 is then 8.8e-10, above 1e-12, the check fails, and the control exits 1, with no traceback.
Any other pattern is reported as found, and the card is not filed.

Eleven lines are marked "DECISIVE:".
"""
import contextlib
import io
import math
import pathlib
import re
import sys

import p589c_exact_rows as RW
import p589c_posthoc3 as PH

HERE = pathlib.Path(__file__).resolve().parent
OLD = HERE.parent / "chat1_2026-11-25_p589c"
FLOAT = r"([-+0-9.e]+)"


def run(main):
    argv = sys.argv
    sys.argv = ["x", "."]
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        main()
    sys.argv = argv
    return buf.getvalue()


def one(pattern, text):
    m = re.search(pattern, text, re.M)
    return m.groups() if m else None


def nums(s):
    return [float(x) for x in re.findall(r"[-+]?\d+\.\d+e[-+]\d+|[-+]?\d+\.\d+", s)]


def decisive():
    rows = run(RW.main)
    post = run(PH.main)
    for name, text, sealed in (("p589c_exact_rows", rows, "p589c_exact_rows_out.txt"),
                               ("p589c_posthoc3", post, "p589c_posthoc3_out.txt")):
        print("(not decisive) %s's capture equals its sealed output byte for byte: %s"
              % (name, text.encode("utf-8") == (OLD / sealed).read_bytes()))
    t = {}
    p0 = one(r"^P0 at .*: max relative deviation from B1667's json " + FLOAT + "$", rows)
    t["P0"] = bool(p0) and float(p0[0]) < 1e-6
    print("DECISIVE: P0 the instrument reproduces B1667's json at 0.25 + 3.0i within 1e-6: %s" % t["P0"])
    p1 = one(r"^P1 row 315: max \|m2/m3 - 1\|, max m1/m3: small \[(.*?)\], exact \[(.*?)\]; worst difference " + FLOAT + "$",
             rows)
    t["315"] = bool(p1) and nums(p1[0])[0] < 1e-12 and nums(p1[1])[0] < 1e-12 and float(p1[2]) < 1e-8
    print("DECISIVE: row 315: max |m2/m3 - 1| below 1e-12 at both norms and the small-exact difference below 1e-8: %s"
          % t["315"])
    p3 = one(r"^P3 row 324: order-5 worst \|R - 1\| \(exact\) " + FLOAT + r"; median log R2 small \{'3\|N': " + FLOAT +
             r", 'other': [^}]*\}, exact \{'3\|N': " + FLOAT + r", 'other': [^}]*\}; shift of the 3\|N difference " + FLOAT,
             rows)
    t["324"] = bool(p3) and float(p3[0]) < 1e-8 and abs(float(p3[2]) - math.log(3)) > 0.5
    print("DECISIVE: row 324: order-5 worst |R - 1| below 1e-8: %s; median log R2 on the 3|N lines, small %.3f, exact "
          "%.3f, log 3 = %.3f" % (bool(p3) and float(p3[0]) < 1e-8, float(p3[1]) if p3 else -1, float(p3[2]) if p3 else -1,
                                  math.log(3)))
    cells = one(r"^(P0 \w+, P1 \w+, P2 \w+, P3 \w+)$", rows)
    print("DECISIVE: the sealed run's cells: %s" % (cells[0] if cells else "absent"))
    for y in ("1.6", "3.1", "3.5"):
        c = one(r"^tau = " + re.escape(y) + r"i: c\* = " + FLOAT + " ", post)
        print("DECISIVE: the uniformising accessory parameter at %si: c* = %.4f" % (y, float(c[0]) if c else -1))
    q0 = one(r"^Q0: with the stuck c, the largest exact order-12 lepton m1/m3 is (\S+) \(committed: (\S+)\)$", post)
    t["Q0"] = bool(q0) and q0[0] == q0[1]
    print("DECISIVE: Q0 the stuck c reproduces the committed order-12 residue %s: %s" % (q0[1] if q0 else "?", t["Q0"]))
    q1 = one(r"^Q1 \(P1 at 1\.6i\): .*; worst difference " + FLOAT + ";", post)
    t["Q1"] = bool(q1) and float(q1[0]) < 1e-8
    q12 = one(r"^Q2 order 12 at 3\.1i: 48 lines; lepton m1/m3 small \[.*?\], exact \[(.*?)\];", post)
    t["12"] = bool(q12) and nums(q12[0])[1] <= 1e-12
    q9 = one(r"^Q2 order 9 at 3\.5i: 36 lines; lepton m1/m3 small \[.*?\], exact \[(.*?)\];", post)
    t["9"] = bool(q9) and nums(q9[0])[0] > 1e-12
    print("DECISIVE: Q1 P1's 1.6i half at c*: the small-exact difference below 1e-8: %s" % t["Q1"])
    print("DECISIVE: Q2 at c*: every exact order-12 lepton m1/m3 at most 1e-12 on the 48 lines: %s; every exact order-9 "
          "lepton m1/m3 above 1e-12 on the 36 lines: %s" % (t["12"], t["9"]))
    ok = all(t.values()) and bool(cells) and cells[0] == "P0 holds, P1 holds, P2 FAILS, P3 holds"
    print("DECISIVE: verdict: %s" % ("the claim holds" if ok else "the claim FAILS"))
    return 0 if ok else 2


def control():
    """the order-12 check with the accessory parameter left stuck on purpose, at 3.1i (posthoc3's Q0 computation)"""
    argv = sys.argv
    sys.argv = ["x", "."]
    with contextlib.redirect_stdout(io.StringIO()):
        EE, root = RW.load(".")
        tau = complex(0, 3.1)
        Gs, Lcol, _ = RW.at_tau(EE, tau)
        rd = EE.higgs(tau)
        worst = 0.0
        for (a, b) in RW.lines_of_order(12):
            sp = RW.sector_spectra(EE, tau, Gs, Lcol, float(a) * tau + float(b), "lep", rd)
            worst = max(worst, max(v[1] for k, v in sp.items() if k[1] == "exact"))
    sys.argv = argv
    ok = worst <= 1e-12
    print("control: the accessory parameter left stuck on purpose at 3.1i: the largest exact order-12 lepton m1/m3 is "
          "%.3e; the order-12 check: %s" % (worst, "holds (the control has FAILED to fail)" if ok else "fails, as it must"))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(control() if sys.argv[1:] == ["--control"] else decisive())
