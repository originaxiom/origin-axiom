"""The web seat's third check for its relations note (data-free; no measured value is read): the half-period
coincidences (B1742 section 3 and their kin), the frame's exact zeros, and the branches on which the ten collapse to one
function.

The note's read-only referee found that B1742's mechanism is not confined to (2/5, odd/10), and that the note's list of
explicit relations left out the frame's exact zeros. This script checks both on the seat's own code before the note
states them. No inter-sector value is printed: a coincidence is printed as a count of lines, and its departure off the
condition only by decade bin.

For every census line (orders 1-12 up to w -> -w: 266 lines), at tau = 0.13 + 2.2i and 0.27 + 2.6i, the three sectors'
residues and channel norms are computed once (FR-FIB as B1821's module builds it; c not applied, H = I, h0 = 0), and
then for each direction, radius rule and reading:

(1) The half-period classes. On a line of even order N the half-period (N/2)w has class ((N/2)p1, (N/2)p2) mod 1, one
    of (0, 1/2), (1/2, 0), (1/2, 1/2). Printed: the lines per (order, class), and the classes of three named lines.
(2) Coincidences by direction. Seven synthetic Higgs directions -- generic; with no QI, no QJ or no QK component; along
    QI, QJ or QK only -- read S in all three sectors, radius L_2. For each sector pair: "full" when all three singular
    values agree to 1e-8 relative to the larger largest one; "ratios" when only the two mass ratios agree (to 1e-8, or
    both below 1e-12). A pair counts when it holds at both tau. Printed per (order, class, direction): the counts of
    lines with each pair full, and with each pair equal in its ratios only. Then whether the table read S~ in all three
    sectors is the same cell by cell.
(3) The menu on the class lines. For each of B1810's thirteen directions and each class of orders 4, 8 and 10, read S
    and S~ alike, radius L_2: the largest relative departure, over the class's lines and both tau, of the pair the
    class's half-period relates (up-down on order 4, down-lepton on orders 8 and 10), all three singular values, by
    decade bin: "<1e-8", "<1e-5", "<1e-2", ">=1e-2". Then each direction's smallest |component|/|S| over both tau.
(4) The exact zeros. Over all 266 lines, both tau, the thirteen directions, both radii and both readings per sector: the
    rows with m1/m3 below 1e-12, by order and sector, separately for the null directions (R, t = -5/288) and the eleven
    others.
(5) The order-4 mixing. On the six order-4 lines, for every (direction, radius, up reading, down reading) whose up and
    down spectra are non-degenerate (gaps above 1e-8 of the largest): the largest |V_us|, |V_ub| and |J| and the
    smallest |V_cb|; and the number of such rows with the mixing undefined.
(6) The collapsed branches. On the four lines of orders 1 and 2, the two null directions read alike in all three sectors
    (S S S or S~ S~ S~), both radii: on how many of the 32 branches, at both tau, the three sectors share their spectrum,
    m1/m3 < 1e-12 and the off-diagonal |V| lie below 1e-8.

Usage: python3 halfperiod_check.py <main checkout>   (main at 354a4ea4d)
"""
import contextlib
import io
import math
import os
import pathlib
import sys
from collections import defaultdict
from fractions import Fraction as Fr
from multiprocessing import Pool

import numpy as np

sys.dont_write_bytecode = True
ROOT = pathlib.Path(sys.argv[1]).resolve()
sys.path.insert(0, str(ROOT / "frontier" / "B1821_the_frames_mirror_symmetry_in_re_tau" / "verification"))
os.chdir(ROOT)
with contextlib.redirect_stdout(io.StringIO()):
    import cm_zero_line as Z
    B = Z.mods()["B"]

TAUS = (complex(0.13, 2.2), complex(0.27, 2.6))
SECT = [(sn, ql, qr) for sn, ql, qr in Z.SECTORS]
SYN = {"generic": (1.0, 0.7 + 0.2j, -0.4 + 0.9j), "no QI": (0.0, 0.7 + 0.2j, -0.4 + 0.9j),
       "no QJ": (1.0, 0.0, -0.4 + 0.9j), "no QK": (1.0, 0.7 + 0.2j, 0.0),
       "QI only": (1.0, 0.0, 0.0), "QJ only": (0.0, 1.0, 0.0), "QK only": (0.0, 0.0, 1.0)}
MENU = Z.DIRS
NULL = ("R", "t=-5/288")
PAIRS = (("up", "down"), ("down", "lepton"), ("up", "lepton"))
TAG = {("up", "down"): "u=d", ("down", "lepton"): "d=e", ("up", "lepton"): "u=e"}


def census():
    lines = {}
    for N in range(1, 13):
        for a in range(N):
            for b in range(N):
                p = (Fr(a, N), Fr(b, N))
                lines[min(p, ((-p[0]) % 1, (-p[1]) % 1))] = True
    return sorted(lines)


def order(l):
    return int(np.lcm(l[0].denominator, l[1].denominator))


def hclass(l):
    N = order(l)
    if N % 2:
        return None
    k = N // 2
    return ((k * l[0]) % 1, (k * l[1]) % 1)


def CLS(c):
    return {None: "-", (Fr(0), Fr(1, 2)): "(0,1/2)", (Fr(1, 2), Fr(0)): "(1/2,0)", (Fr(1, 2), Fr(1, 2)): "(1/2,1/2)"}[c]


def work(task):
    line, dirs = task
    out = []
    for ti, tau in enumerate(TAUS):
        Ls = Z.radii(tau)
        Mw = {}
        for sn, ql, qr in SECT:
            w = B.line_w(float(line[0]), float(line[1]), tau); x, y = B.sector_twists(w, tau, ql, qr)
            with contextlib.redirect_stdout(io.StringIO()):
                R = B.residues(x, y, tau); c = B.cA(x, y, tau, R)
            for ri, L in enumerate(Ls):
                u = {k: (math.sqrt(2 * math.pi * L + c[k]) * R[k] if c[k] is not None and 2 * math.pi * L + c[k] > 0 else 0)
                     for k in B.UNITS}
                Mw[(sn, ri)] = B.weighted_M(u)
        res = {}
        alld = dict(SYN); alld.update(dirs[ti])
        for dn, a in alld.items():
            S0 = a[0] * B.QI + a[1] * B.QJ + a[2] * B.QK
            for rd in (0, 1):
                Sm = B.EPS @ S0.conj() @ B.EPS.T if rd else S0
                for ri in (0, 1):
                    if dn in SYN and ri == 0:
                        continue
                    for sn, _, _ in SECT:
                        u_, s, _ = np.linalg.svd(B.coupling(Sm, Mw[(sn, ri)])); o = np.argsort(s)
                        res[(dn, ri, rd, sn)] = (s[o], u_[:, o])
        out.append(res)
    return line, out


def full_eq(sa, sb):
    return np.max(np.abs(sa - sb)) <= 1e-8 * max(sa[2], sb[2])


def ratio_eq(sa, sb):
    ra, rb = sa[:2] / sa[2], sb[:2] / sb[2]
    return all((max(x, y) < 1e-12) or abs(x - y) <= 1e-8 * max(x, y) for x, y in zip(ra, rb))


def dep(sa, sb):
    return float(np.max(np.abs(sa - sb)) / max(sa[2], sb[2]))


def binof(v):
    return "<1e-8" if v < 1e-8 else "<1e-5" if v < 1e-5 else "<1e-2" if v < 1e-2 else ">=1e-2"


if __name__ == "__main__":
    lines = census()
    with contextlib.redirect_stdout(io.StringIO()):
        dirs = [{d: tuple(complex(v) for v in Z.direction(d, tau)) for d in MENU} for tau in TAUS]
    with Pool(2) as pool:
        data = dict(pool.map(work, [(l, dirs) for l in lines], chunksize=4))

    print("(1) the half-period classes: %d census lines" % len(lines))
    byoc = defaultdict(list)
    for l in lines:
        byoc[(order(l), hclass(l))].append(l)
    for N in range(1, 13):
        cells = ["%s: %d" % (CLS(c), len(v)) for (n, c), v in sorted(byoc.items(), key=lambda kv: CLS(kv[0][1])) if n == N]
        print("    order %2d: %s" % (N, ", ".join(cells)))
    for nm, l in (("check (1)'s (1/4, 1/8)", (Fr(1, 4), Fr(1, 8))), ("check (1)'s (2/5, 1/10)", (Fr(2, 5), Fr(1, 10))),
                  ("B1825's address (3/8, 3/8)", (Fr(3, 8), Fr(3, 8)))):
        print("    %s: order %d, class %s" % (nm, order(l), CLS(hclass(l))))

    print("(2) coincidences by direction (radius L_2; a pair counts when it holds at both tau)")
    tables = {}
    for rd in (0, 1):
        tab = {}
        for (N, c), ls in byoc.items():
            for dn in SYN:
                cnt = []
                for p in PAIRS:
                    f = r = 0
                    for l in ls:
                        F_ = all(full_eq(data[l][ti][(dn, 1, rd, p[0])][0], data[l][ti][(dn, 1, rd, p[1])][0]) for ti in (0, 1))
                        R_ = all(ratio_eq(data[l][ti][(dn, 1, rd, p[0])][0], data[l][ti][(dn, 1, rd, p[1])][0]) for ti in (0, 1))
                        f += F_; r += (R_ and not F_)
                    cnt.append((f, r))
                tab[(N, c, dn)] = cnt
        tables[rd] = tab
    for N in range(1, 13):
        for (n, c) in sorted((k for k in byoc if k[0] == N), key=lambda k: CLS(k[1])):
            print("    order %2d, class %s (%d lines)  [pair: full + ratios only]" % (N, CLS(c), len(byoc[(n, c)])))
            for dn in SYN:
                cnt = tables[0][(N, c, dn)]
                print("        %-8s %s" % (dn, ", ".join("%s %d + %d" % (TAG[p], f, r) for p, (f, r) in zip(PAIRS, cnt))))
    same = all(tables[0][k] == tables[1][k] for k in tables[0])
    print("    read S~ in all three sectors, the table is the same in every cell: %s" % ("yes" if same else "no"))
    if not same:
        for k in sorted(tables[0], key=str):
            if tables[0][k] != tables[1][k]:
                print("        differs: order %d class %s %s: S %s, S~ %s" % (k[0], CLS(k[1]), k[2], tables[0][k], tables[1][k]))

    print("(3) the menu on the class lines of orders 4, 8 and 10 (radius L_2; the largest departure over the class's lines "
          "and both tau, by decade bin)")
    for N, p in ((4, ("up", "down")), (8, ("down", "lepton")), (10, ("down", "lepton"))):
        for (n, c) in sorted((k for k in byoc if k[0] == N), key=lambda k: CLS(k[1])):
            for rd in (0, 1):
                cells = []
                for dn in MENU:
                    v = max(dep(data[l][ti][(dn, 1, rd, p[0])][0], data[l][ti][(dn, 1, rd, p[1])][0])
                            for l in byoc[(n, c)] for ti in (0, 1))
                    cells.append("%s %s" % (dn, binof(v)))
                print("    order %2d class %-9s (%2d lines) %s, read %s: %s" % (N, CLS(c), len(byoc[(n, c)]), TAG[p],
                                                                             "S~" if rd else "S ", "; ".join(cells)))
    print("    each direction's smallest |component|/|S| over both tau (QI, QJ, QK):")
    for dn in MENU:
        fr = [min(abs(dirs[ti][dn][k]) / math.sqrt(sum(abs(v) ** 2 for v in dirs[ti][dn])) for ti in (0, 1)) for k in range(3)]
        print("        %-9s %.1e, %.1e, %.1e" % (dn, *fr))

    print("(4) the exact zeros: rows with m1/m3 < 1e-12 (thirteen directions, both radii, both readings per sector, both tau)")
    for N in range(1, 13):
        ls = [l for l in lines if order(l) == N]
        cells = []
        for grp, ds in (("null", NULL), ("other", [d for d in MENU if d not in NULL])):
            for sn, _, _ in SECT:
                z = tot = 0
                for l in ls:
                    for ti in (0, 1):
                        for dn in ds:
                            for ri in (0, 1):
                                for rd in (0, 1):
                                    s = data[l][ti][(dn, ri, rd, sn)][0]; tot += 1; z += (s[0] / s[2] < 1e-12)
                cells.append("%s %s %d/%d" % (grp, sn, z, tot))
        print("    order %2d (%2d lines): %s" % (N, len(ls), "; ".join(cells)))

    print("(5) the order-4 mixing (six lines, thirteen directions, both radii, four (up, down) readings, both tau)")
    mx = {"us": 0.0, "ub": 0.0, "J": 0.0}; mn_cb = np.inf; nd = und = 0
    for l in [l for l in lines if order(l) == 4]:
        for ti in (0, 1):
            for dn in MENU:
                for ri in (0, 1):
                    for ru in (0, 1):
                        for rdd in (0, 1):
                            su, Uu = data[l][ti][(dn, ri, ru, "up")]; sd, Ud = data[l][ti][(dn, ri, rdd, "down")]
                            gap = lambda s: min(s[1] - s[0], s[2] - s[1]) / s[2]
                            if gap(su) < 1e-8 or gap(sd) < 1e-8:
                                und += 1; continue
                            V = Uu.conj().T @ Ud; nd += 1
                            mx["us"] = max(mx["us"], abs(V[0, 1])); mx["ub"] = max(mx["ub"], abs(V[0, 2]))
                            mx["J"] = max(mx["J"], abs(np.imag(V[0, 1] * V[1, 2] * np.conj(V[0, 2]) * np.conj(V[1, 1]))))
                            mn_cb = min(mn_cb, abs(V[1, 2]))
    print("    rows with the mixing defined: %d; largest |V_us| %.1e, |V_ub| %.1e, |J| %.1e; smallest |V_cb| %.1e; rows with "
          "the mixing undefined: %d" % (nd, mx["us"], mx["ub"], mx["J"], mn_cb, und))

    print("(6) the collapsed branches (orders 1 and 2; null directions read alike in all three sectors; both radii)")
    ok = tot = 0
    for l in [l for l in lines if order(l) <= 2]:
        for dn in NULL:
            for ri in (0, 1):
                for rd in (0, 1):
                    tot += 1; good = True
                    for ti in (0, 1):
                        sp = {sn: data[l][ti][(dn, ri, rd, sn)] for sn, _, _ in SECT}
                        good &= full_eq(sp["up"][0], sp["down"][0]) and full_eq(sp["down"][0], sp["lepton"][0])
                        good &= all(sp[sn][0][0] / sp[sn][0][2] < 1e-12 for sn in sp)
                        V = np.abs(sp["up"][1].conj().T @ sp["down"][1])
                        good &= max(V[0, 1], V[1, 2], V[0, 2]) < 1e-8
                    ok += good
    print("    branches: %d; with the three sectors sharing their spectrum, m1/m3 < 1e-12 and V = 1 at both tau: %d" % (tot, ok))
