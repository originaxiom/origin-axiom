#!/usr/bin/env python3
"""Main's ask of 2026-10-24 (its handoff CC_TO_SM_2026-10-24_B1753_AND_THE_LITERATURE.md, section 4): does any
forced 45, or an E-series branching piece, land W154's t = B/|A| in the band window [3.205, 4.624]?  Post hoc and
data-free: exact arithmetic on W154's closed form, with W154's units and rows (W154_RULE.md).  Not a test.

  A = w0 - (15/16) wp - (31/1024) wrho,  B = (31/1024) wrho,  V = -(A E(tau, 3) + B E(tau, 2)).
  The band holds tau exactly when A < 0 < B and t = B/|A| lies in W154's C2 window; equivalently wrho > 0 and
  r = wrho / (w0 - (15/16) wp) lies in [42.15, 48.01].

    python3 -B docs/dossiers/the_weave_2026-10-07/the_w154_45_check.py
"""
import json
import math
from fractions import Fraction as Fr
from pathlib import Path

HERE = Path(__file__).resolve().parent
W154 = json.loads((HERE / "the_content_census.json").read_text(encoding="utf-8"))["C2"]
T1, T2 = W154["t1"], W154["t2"]
K31 = Fr(31, 1024)
Z6, Z4 = math.pi ** 6 / 945, math.pi ** 4 / 90
CC3 = 2 * math.sqrt(math.pi) * math.gamma(2.5) * 1.0369277551433699 / math.gamma(3)     # zeta(5)
CC2 = 2 * math.sqrt(math.pi) * math.gamma(1.5) * 1.2020569031595942 / math.gamma(2)     # zeta(3)


def t_formula(y):
    """W154's asymptotic t(y) (W154_RULE.md, C1), as the_content_census.py writes it"""
    return (6 * Z6 * y ** 2 - 2 * CC3 / y ** 3) / (4 * Z4 * y - CC2 / y ** 2)


def y_formula(t):
    lo, hi = 1.5, 40.0
    for _ in range(200):
        mid = (lo + hi) / 2
        lo, hi = (mid, hi) if t_formula(mid) < t else (lo, mid)
    return (lo + hi) / 2


def regime(w0, wp, wr):
    """W154's C1 regimes, from the signs of A and B and the value of t"""
    a, b = Fr(w0) - Fr(15, 16) * Fr(wp) - K31 * Fr(wr), K31 * Fr(wr)
    out = {"A": float(a), "B": float(b)}
    if a > 0:
        out["regime"] = "runs to the cusp"
    elif a == 0:
        out["regime"] = "runs to the cusp" if b > 0 else ("V = 0" if b == 0 else "omega")
    elif b <= 0:
        out["regime"] = "omega"
    else:
        t = float(b / -a)
        out["t"] = t
        out["regime"] = "on the axis" if t > 2.2 else "omega or i (t below the axis range, W154's R)"
        if t > 2.2:
            out["y*"] = y_formula(t)
    out["lands in the band"] = bool(a < 0 < b and T1 <= float(b / -a) <= T2)
    return out


# W154's rows (W154_RULE.md): weights (w0, wp, wrho) in B1686's and B1704's units
ROWS = {"the matter": (0, 0, -90), "+ the Higgs's copies": (0, 2, -90), "+ the gauge fields": (48, 2, -90),
        "+ the graviton": (57, 2, -90)}
# a 45-dimensional multiplet, in each place the frame has for it (a complex scalar 2, a Weyl fermion -2, a real
# six-dimensional vector 4; a complex scalar in rho_Q 2)
PIECES = {
    "45 complex scalars in rho_Q (the matter's representation)": (0, 0, 90),
    "45 complex scalars on each parity characteristic (where the Higgs's copies sit; a Georgi-Jarlskog 45 there)":
        (0, 90, 0),
    "45 complex scalars on the trivial characteristic": (90, 0, 0),
    "45 real vectors on the trivial characteristic (SO(10)'s adjoint commuting with the fibre)": (180, 0, 0),
    "45 Weyl fermions in rho_Q (a second copy of the matter's count)": (0, 0, -90),
}


def main():
    out = {"window t": [T1, T2], "window r = wrho / (w0 - 15/16 wp)": W154["dominance"]}
    # the ratio 45 as a point of the window
    u = float(1 / (K31 * 45))
    t45 = 1 / (1 - u)
    out["r = 45"] = {"u": u, "t": t45, "y*": y_formula(t45), "in the window": T1 <= t45 <= T2}
    table = {}
    for rn, (w0, wp, wr) in ROWS.items():
        table[rn] = {"row alone": regime(w0, wp, wr)}
        for pn, (d0, dp, dr) in PIECES.items():
            table[rn][pn] = regime(w0 + d0, wp + dp, wr + dr)
    out["rows plus one 45"] = table
    out["any row plus one 45 lands"] = any(v["lands in the band"] for r in table.values() for v in r.values())
    # what a 45 would have to do: the rho_Q net bosons the full row needs at r = 45
    x = Fr(57) - Fr(15, 16) * 2
    need = 45 * x
    out["the full row at r = 45"] = {"w0 - 15/16 wp": float(x), "net wrho needed": float(need),
                                     "complex scalars in rho_Q to add": float((need + 90) / 2)}
    # E8's 248 under the fibre's SU(2) (W81): 55.1 + 52.2 + 27.3 + 2.4 as six-dimensional vectors.  Every
    # sub-multiset (k0, k1, kh, kq) of it, with W154's units: w0 = 4 k0, wp = 4 k1, wrho = 2 (2 kh + 4 kq)
    land, total, land45, total45, smallest = 0, 0, 0, 0, None
    for k0 in range(56):
        for k1 in range(28):
            for kh in range(53):
                for kq in range(3):
                    total += 1
                    dim = k0 + 3 * k1 + 2 * kh + 4 * kq
                    r = regime(4 * k0, 4 * k1, 2 * (2 * kh + 4 * kq))
                    if dim == 45:
                        total45 += 1
                    if r["lands in the band"]:
                        land += 1
                        if dim == 45:
                            land45 += 1
                        if smallest is None or dim < smallest[0]:
                            smallest = (dim, (k0, k1, kh, kq))
    out["E8's 248 under the fibre"] = regime(220, 108, 224)
    out["sub-multisets of the fibre's decomposition"] = {
        "total": total, "landing": land, "fraction landing": land / total,
        "of dimension 45": total45, "of dimension 45 landing": land45,
        "smallest landing dimension and (k0, k1, k_half, k_three_halves)": smallest}
    (HERE / "the_w154_45_check_run.txt").write_text(json.dumps(out, indent=1) + "\n", encoding="utf-8")
    print(json.dumps(out, indent=1))


if __name__ == "__main__":
    main()
