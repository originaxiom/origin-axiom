"""B1945: B1788's tropical rule (tropical.predict, derived in B1656's frame from B1659's law) against every cell of frame C's
pointwise cusp exponents, both generations (main, 2026-11-15; data-free)."""
import sys, json, math, pathlib
from fractions import Fraction as Fr
HERE = pathlib.Path(__file__).resolve().parent
ROOT = next(q for q in HERE.parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
sys.path.insert(0, str(next((ROOT / "frontier").glob("B1788_*")) / "verification")); import tropical as T
P = {rd: T.polys(rd) for rd in ("S", "St")}
D = json.loads((HERE / "pointwise_exponents.json").read_text()); A0 = json.loads((HERE / "pointwise_exponents_a0.json").read_text())
SIXY = {"Q": 1, "u": -4, "d": 2}; SEC = {"up": ("Q", "u"), "down": ("Q", "d")}


def fit(p, k, j):
    """the rate k of C y^s |q|^k from the two slopes between three equally spaced heights"""
    (s1, s2), ys = (A0[p][k][j], (40, 60, 80)) if p in A0 else (D[p][k][j], (24, 32, 40))
    L1, L2 = math.log(ys[1] / ys[0]), math.log(ys[2] / ys[1]); h = 2 * math.pi * (ys[1] - ys[0])
    pw = (s1 - s2) * h / (L2 - L1)
    return s1 + pw * L1 / h


def cells(charges=SIXY):
    out = []
    for p in D:
        a = Fr(p.split(",")[0])
        for sec, (l, r) in SEC.items():
            mu = T.E(charges[l] * a, charges[r] * a)
            for rd in ("S", "St"):
                e2, e3 = T.predict(P[rd], mu)
                for j, pe in ((0, e2), (1, e3)):
                    out.append((p, sec, rd, j, fit(p, "%s|L_2|%s" % (sec, rd), j), pe))
    return out


if __name__ == "__main__":
    c = cells(); w = max(abs(g - float(pe)) for *_, g, pe in c)
    print("B1788's tropical rule against frame C: %d cells, worst |difference| %.1e" % (len(c), w))
    bad = sum(abs(g - float(pe)) > 2e-3 for *_, g, pe in cells(dict(SIXY, u=-3)))
    print("planted: the up quark's charge -3 for -4 in the rule: %d cells break" % bad)
