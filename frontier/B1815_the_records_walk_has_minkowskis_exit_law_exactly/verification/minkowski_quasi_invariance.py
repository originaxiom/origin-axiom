"""T2(a) (data-free; audit room): is Minkowski's measure d? quasi-invariant under SL(2,Z), and not under a translation
outside it?  ? is computed exactly on the Stern-Brocot tree (? sends each mediant to the dyadic midpoint), with
?(x + 1) = ?(x) + 1 on the line.  d? is quasi-invariant under a map g iff h = ? o g o ?^-1 is absolutely continuous with a
positive derivative; for g in PSL(2,Z) h should be piecewise linear with power-of-2 slopes (the Thompson-group picture).
Test: on the dyadic grid of depth d inside [1/64, 63/64], the slopes of h between consecutive grid points."""
from fractions import Fraction as F
import math, json, pathlib
def q_unit(x):                                   # ? on [0, 1], x rational
    if x == 0: return F(0)
    if x == 1: return F(1)
    lo, hi, ylo, yhi = (0, 1), (1, 1), F(0), F(1)
    while True:
        m = F(lo[0] + hi[0], lo[1] + hi[1]); ym = (ylo + yhi) / 2
        if x == m: return ym
        if x < m: hi, yhi = (m.numerator, m.denominator), ym
        else: lo, ylo = (m.numerator, m.denominator), ym
def q(x):
    x = F(x); n = math.floor(x); return n + q_unit(x - n)
def q_inv_unit(y):                               # ?^-1 on dyadic y in [0, 1]
    if y == 0: return F(0)
    if y == 1: return F(1)
    lo, hi, ylo, yhi = (0, 1), (1, 1), F(0), F(1)
    while True:
        m = F(lo[0] + hi[0], lo[1] + hi[1]); ym = (ylo + yhi) / 2
        if y == ym: return m
        if y < ym: hi, yhi = (m.numerator, m.denominator), ym
        else: lo, ylo = (m.numerator, m.denominator), ym
def q_inv(y):
    y = F(y); n = math.floor(y); return n + q_inv_unit(y - n)
def slopes(g, depth):
    N = 2 ** depth; pts = [F(i, N) for i in range(N // 64, 63 * N // 64 + 1)]
    hv = [q(g(q_inv(y))) for y in pts]
    return [(hv[i + 1] - hv[i]) * N for i in range(len(pts) - 1)]
maps = {"T: x -> x + 1": lambda x: x + 1, "S: x -> -1/x": lambda x: -1 / x, "R: x -> x/(x+1)": lambda x: x / (x + 1),
        "translation by 1/3 (not in SL(2,Z))": lambda x: x + F(1, 3)}
check = max(abs(q(q_inv(F(k, 256))) - F(k, 256)) for k in range(1, 256))
out = {"roundtrip ?(?^-1(y)) - y over k/256": float(check)}
for name, g in maps.items():
    row = {}
    for depth in (6, 8, 10):
        sl = slopes(g, depth); pos = [s for s in sl if s > 0]
        p2 = sum(1 for s in sl if s > 0 and s.numerator & (s.numerator - 1) == 0 and s.denominator & (s.denominator - 1) == 0)
        row[str(depth)] = {"intervals": len(sl), "share with a power-of-2 slope": round(p2 / len(sl), 3),
                           "distinct slopes": len(set(sl)), "min slope": float(min(sl)), "max slope": float(max(sl))}
    out[name] = row
print(json.dumps(out, indent=1))
pathlib.Path(__file__).with_suffix(".json").write_text(json.dumps(out, indent=1))
