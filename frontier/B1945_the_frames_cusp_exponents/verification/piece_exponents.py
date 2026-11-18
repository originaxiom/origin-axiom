"""B1945, section 2: the exponents of the coupling's pieces, measured (added at Review 84, 2026-11-18: a reader found
that the page stated these four closed forms as measured while no script of the arc computed them).  Data-free.
For X ~ |q|^e with |q| = exp(-2 pi y): e = -d ln|X| / d(2 pi y), between two heights of one column, at the three kinds
of point (a = 0, +-1/5, +-2/5), both sectors, both readings.  Against, with D = ||2 q_L a||/2 and E' = ||2 q_R a||/2:
  the largest entry of Y:   D^2 + E'^2 - 1/4
  the adjugate of Y:        2 D^2 + 2 E'^2 - D - E'
  the matter's determinant: [(1/2 - 2D)^2 + (1/2 - 2E')^2]/2
  the Higgs's determinant:  1/4"""
import sys, pathlib, math, functools
from fractions import Fraction as Fr
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import determinant_law as DL
mp = DL.mp; B = DL.B; print = functools.partial(print, flush=True)
nd = lambda x: abs(x - round(x))
def adj_max(Y):
    n = Y.rows; best = mp.mpf(0)
    for i in range(n):
        for j in range(n):
            rows = [r for r in range(n) if r != i]; cols = [c for c in range(n) if c != j]
            best = max(best, abs(Y[rows[0], cols[0]] * Y[rows[1], cols[1]] - Y[rows[0], cols[1]] * Y[rows[1], cols[0]]))
    return best
def measures(tx, ty, a, b, sec):
    RD, Mw, Ys, u, cs, ds = DL.parts(tx, ty, a, b, sec)
    return {"Y|S": max(abs(v) for v in Ys["S"]), "Y|St": max(abs(v) for v in Ys["St"]), "adj|S": adj_max(Ys["S"]), "adj|St": adj_max(Ys["St"]), "detM": abs(mp.det(Mw)), "detS": abs(mp.det(RD["S"])), "detSt": abs(mp.det(RD["St"]))}
if __name__ == "__main__":
    Y0, Y1 = 30, 38; worst = {}
    for (a, b) in ((Fr(0), Fr(3, 5)), (Fr(1, 5), Fr(2, 5)), (Fr(2, 5), Fr(1, 5))):
        for sec in ("up", "down"):
            ql, qr = B.SIXY[B.SECTORS[sec][0]], B.SIXY[B.SECTORS[sec][1]]; D = Fr(nd(2 * ql * a)).limit_denominator(100) / 2; E = Fr(nd(2 * qr * a)).limit_denominator(100) / 2
            want = {"Y": D * D + E * E - Fr(1, 4), "adj": 2 * D * D + 2 * E * E - D - E, "detM": ((Fr(1, 2) - 2 * D) ** 2 + (Fr(1, 2) - 2 * E) ** 2) / 2, "detS": Fr(1, 4)}
            m0, m1 = measures("0.13", Y0, a, b, sec), measures("0.13", Y1, a, b, sec)
            got = {k: (float(-(mp.log(m1[k]) - mp.log(m0[k])) / (2 * mp.pi * (Y1 - Y0))) if m0[k] > 0 and m1[k] > 0 else None) for k in m0}
            row = []
            for k, g in got.items():
                w = want[k.split("|")[0].replace("detSt", "detS")]; row.append("%s %s (closed form %s)" % (k, "zero" if g is None else "%.4f" % g, w))
                if g is not None: worst[k.split("|")[0].replace("detSt", "detS")] = max(worst.get(k.split("|")[0].replace("detSt", "detS"), 0), abs(g - float(w)))
            print("a = %s, %s (q_L, q_R = %s, %s; D = %s, E' = %s): %s" % (a, sec, ql, qr, D, E, "; ".join(row)))
    print("largest distance from the closed forms: %s" % {k: round(v, 4) for k, v in worst.items()})
