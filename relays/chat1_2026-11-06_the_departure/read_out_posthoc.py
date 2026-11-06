"""The web seat, 2026-11-06: POST HOC to read_out_check.py (PREREGISTRATION_READ_OUT.md), written after reading its
outputs (a34f5cdd1). Data-free; no coupling, no ratio of the six, no theta-bar, no held-out quantity.

  (a) P2 found one class of symmetric points on the golden loop, not two: the check builds only mirrors (det -1, the
      palindromic P J0). Here every direction-reversing element g (g W g^-1 = +-W^-1) of either determinant is
      enumerated from the exact solution space of the linear condition, with its two free entries bounded by 300,
      for W = LR and for L^n R (LR)^k (n = 5, 6; k = 0, 1, 2); fixed points on the axis, classes modulo the minimal
      translation, and the determinant of each class.
  (b) P8 found the n = 6 height tied between tetrahedra 2, 3, 4: the run's shapes for b++ L^n R (LR)^12 (n = 5, 6),
      their highest Z/3-orbit members, and whether neighbouring shapes differ by an integer translation.

    python3 read_out_posthoc.py
"""
import math
import warnings
from fractions import Fraction as Fr

import mpmath as mp

warnings.filterwarnings("ignore", message="Plink failed to import tkinter")
import snappy  # noqa: E402

from read_out_check import (mat, det, inv, mul, peq, axis, length, half_root, mirror_point, to_F, nullspace, z3,
                            I2)

mp.mp.dps = 60
BOUND = 300


def solve_reversing(W):
    """all integer g with g W = eps W^-1 g (eps = +-1), det g = +-1, the two free entries in [-BOUND, BOUND]"""
    Wi = inv(W)
    out = []
    for eps in (1, -1):
        rows = []
        # (g W - eps Wi g)_{ab} = sum_c g_ac W_cb - eps sum_c Wi_ac g_cb ; unknowns (p, q, r, s) = g00, g01, g10, g11
        for a in range(2):
            for b in range(2):
                row = [0, 0, 0, 0]
                for c in range(2):
                    row[2 * a + c] += W[c][b]
                    row[2 * c + b] -= eps * Wi[a][c]
                rows.append(row)
        basis = nullspace(rows)
        if not basis:            # g W g^-1 = -W^-1 would need tr W = 0
            continue
        assert len(basis) == 2, (W, eps, basis)
        free = [next(i for i in range(4) if v[i] != 0 and all(u[i] == 0 for u in basis if u is not v)) for v in basis]
        v1, v2 = basis
        d1, d2 = v1[free[0]], v2[free[1]]
        for x in range(-BOUND, BOUND + 1):
            for y in range(-BOUND, BOUND + 1):
                num = [x * v1[i] * d2 + y * v2[i] * d1 for i in range(4)]   # g = x/d1 v1 + y/d2 v2, g[free] = (x, y)
                if any(e % (d1 * d2) for e in num):
                    continue
                g = [e // (d1 * d2) for e in num]
                G = ((g[0], g[1]), (g[2], g[3]))
                if det(G) in (1, -1):
                    assert peq(mul(mul(G, W), inv(G)), Wi)
                    out.append(G)
    return out


def fixed_on_axis(G, c0, rho):
    p, q, r, s = G[0][0], G[0][1], G[1][0], G[1][1]
    assert p + s == 0, G
    if det(G) == -1:
        return mirror_point(G, c0, rho)
    z = mp.mpc(p, 1) / r if r > 0 else mp.mpc(-p, 1) / (-r)          # the elliptic point of a half-turn
    assert abs(abs(z - c0) - rho) < mp.mpf(10) ** -40, "half-turn centre off the axis"
    return z


def census(word):
    W = mat(word)
    c0, rho = axis(W)
    ell = length(W)
    kind, _ = half_root(W)
    ellmin = ell / 2 if kind else ell
    classes = []
    for G in solve_reversing(W):
        z = fixed_on_axis(G, c0, rho)
        s = mp.asinh((z.real - c0) / z.imag)
        r = s - ellmin * mp.floor(s / ellmin)
        for cl in classes:
            dd = abs(r - cl[0])
            if min(dd, ellmin - dd) < mp.mpf(10) ** -30:
                cl[1].add(det(G))
                cl[2] += 1
                break
        else:
            classes.append([r, {det(G)}, 1, z])
    print("   %-14s minimal translation %s; %d classes:" % (word if len(word) < 15 else word[:12] + "...",
                                                            mp.nstr(ellmin, 10), len(classes)))
    for r, dets, cnt, z in sorted(classes, key=lambda c: c[0]):
        zf = to_F(z)
        print("      at %s: determinants %s, %d elements found, reduced |Re| %s, Im %s" % (
            mp.nstr(r, 12), sorted(dets), cnt, mp.nstr(abs(zf.real), 10), mp.nstr(zf.imag, 12)))


def part_b():
    for n in (5, 6):
        word = "L" * n + "R" + "LR" * 12
        M = snappy.ManifoldHP("b++" + word)
        sh = [mp.mpc(mp.mpf(str(z.real())), mp.mpf(str(z.imag()))) for z in M.tetrahedra_shapes("rect")]
        print("   n = %d, k = 12, the run's tetrahedra 0..%d and the next two:" % (n, n))
        tops = []
        for i in range(n + 3):
            zm = max(z3(sh[i]), key=lambda u: u.imag)
            tops.append(zm)
            print("      %2d: shape %s, highest orbit member %s, height (reduced Im) %s" % (
                i, mp.nstr(sh[i], 10), mp.nstr(zm, 12), mp.nstr(to_F(sh[i]).imag, 12)))
        for i in range(n + 2):
            best = min(((abs(u - v - mp.nint((u - v).real)), mp.nint((u - v).real))
                        for u in z3(sh[i + 1]) for v in z3(sh[i])), key=lambda t: t[0])
            print("      %2d -> %2d: nearest integer translation between the orbits %s, residual %s" % (
                i, i + 1, int(best[1]), mp.nstr(best[0], 3)))


if __name__ == "__main__":
    print("POST HOC to read_out_check (the web seat, 2026-11-06; written after reading its outputs)")
    print("(a) every direction-reversing element of either determinant (free entries bounded by %d)" % BOUND)
    for word in ["LR"] + ["L" * n + "R" + "LR" * k for n in (5, 6) for k in (0, 1, 2)]:
        census(word)
    print("    S = [[0, -1], [1, 0]] and LR: S LR S^-1 = (LR)^-1: %s; i on LR's axis: %s" % (
        peq(mul(mul(((0, -1), (1, 0)), mat("LR")), ((0, 1), (-1, 0))), inv(mat("LR"))),
        abs(abs(mp.mpc(0, 1) - axis(mat("LR"))[0]) - axis(mat("LR"))[1]) < mp.mpf(10) ** -50))
    print("(b) the run's shapes")
    part_b()
    print("read_out_posthoc exit 0")
