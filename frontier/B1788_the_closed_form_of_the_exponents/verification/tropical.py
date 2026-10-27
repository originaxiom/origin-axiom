"""Closed-form check, layer D (data-free): the tropical (min-plus) prediction of the singular-value exponents of
Y_ab = sum_mn (C_a^T eps S C_b)_mn M_mn from the exponents of S's entries (exact, line-free: s00 = -s11 at 1/8, s01 at -1/8,
s10 at 3/8; S~ swaps s01 and s10) and of M's entries (mu_ij, by default the closed form E_ij = ||ax + i/2||^2 + ||ay + j/2||^2
- 1/8).  sigma1 ~ max entry, sigma1 sigma2 ~ max 2x2 minor, sigma1 sigma2 sigma3 = |det Y|; each polynomial's exponent is
the min over its monomials (generic coefficients; ties assumed not to cancel).  Compares with B1785's exponents.json."""
import sys, json, math, pathlib, itertools
from fractions import Fraction as Fr
import sympy as sp
ROOT = next(q for q in pathlib.Path(__file__).resolve().parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
HERE = pathlib.Path(__file__).resolve().parent
SIXY = {"Q": 1, "u": -4, "d": 2, "L": -3, "e": 6, "H": 3}
SECTORS = {"up": ("Q", "u"), "down": ("Q", "d"), "lep": ("L", "e")}
I = sp.I
QI = sp.Matrix([[I, 0], [0, -I]]); QJ = sp.Matrix([[0, 1], [-1, 0]]); QK = QI * QJ; EPS = QJ
BL = [QJ, QI, QK]
s, p, r = sp.symbols("s p r")                 # S = [[s, p], [r, -s]]
m00, m01, m10, m11 = sp.symbols("m00 m01 m10 m11")
SVARS = (s, p, r); MVARS = (m00, m01, m10, m11)


def polys(reading):
    S = sp.Matrix([[s, p], [r, -s]]) if reading == "S" else sp.Matrix([[s, r], [p, -s]])   # S~: the big entry moves to (1, 0)
    M = sp.Matrix([[m00, m01], [m10, m11]])
    Y = sp.Matrix(3, 3, lambda a, b: sp.expand(sum((BL[a].T * EPS * S * BL[b]).multiply_elementwise(M))))
    ents = [Y[a, b] for a in range(3) for b in range(3)]
    mins = [sp.expand(Y.extract(list(R_), list(C_)).det()) for R_ in itertools.combinations(range(3), 2) for C_ in itertools.combinations(range(3), 2)]
    det = sp.expand(Y.det())
    def monos(P):
        P = sp.Poly(P, *SVARS, *MVARS); return [m for m, c in P.terms() if c != 0]
    return [monos(e) for e in ents if e != 0], [monos(m) for m in mins if m != 0], monos(det)


SEXP = {"s": Fr(1, 8), "p": Fr(-1, 8), "r": Fr(3, 8)}


def trop(monolist, mu):
    ex = [SEXP["s"], SEXP["p"], SEXP["r"], mu[0], mu[1], mu[2], mu[3]]
    return min(sum(k * e for k, e in zip(m, ex)) for m in monolist)


def nd(x): x = x % 1; return min(x, 1 - x)


def E(ax, ay):
    return [nd(ax) ** 2 + nd(ay) ** 2 - Fr(1, 8), nd(ax) ** 2 + nd(ay + Fr(1, 2)) ** 2 - Fr(1, 8),
            nd(ax + Fr(1, 2)) ** 2 + nd(ay) ** 2 - Fr(1, 8), nd(ax + Fr(1, 2)) ** 2 + nd(ay + Fr(1, 2)) ** 2 - Fr(1, 8)]


def predict(P, mu):
    ents, mins, det = P
    e1 = min(trop(m, mu) for m in ents); e12 = min(trop(m, mu) for m in mins); e123 = trop(det, mu)
    return e12 - 2 * e1, (e123 - e12) - e1


if __name__ == "__main__":
    P = {rd: polys(rd) for rd in ("S", "St")}
    d = json.load(open(ROOT / "frontier/B1785_the_slope_sets_the_exponents/verification/exponents.json"))
    stats = {}; fails = []
    for row in d:
        a = Fr(row["alpha"])
        for sec, (lf, rf) in SECTORS.items():
            mu = E(SIXY[lf] * a, SIXY[rf] * a)
            for rd in ("S", "St"):
                e2, e3 = predict(P[rd], mu)
                for nm, pe in (("m2/m3", e2), ("m1/m3", e3)):
                    k = "%s|L_max|%s|%s" % (sec, rd, nm); obs = row[k]["exponent"]; dv = obs - float(pe)
                    st = stats.setdefault((sec, rd, nm), [0, 0]); st[1] += 1
                    if abs(dv) <= 0.05: st[0] += 1
                    else: fails.append((sec, rd, nm, row["alpha"], row["b"], round(obs, 3), str(pe)))
    for k, v in sorted(stats.items()): print(k, "%d/%d within 0.05" % tuple(v))
    json.dump(fails, open(HERE / "tropical_fails.json", "w"), indent=0)
    print("fails", len(fails))
