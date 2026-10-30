# Referee check: on the zero line, which of the eight readings (and c = 3, applied as B1726's compare.py does:
# c multiplies m_mu/m_tau and divides m_e/m_tau) separate down from leptons, and which split all three sectors.
import sys, itertools, importlib.util, pathlib
from fractions import Fraction as Fr
ROOT = pathlib.Path(sys.argv[1])
spec = importlib.util.spec_from_file_location("census", ROOT / "frontier/B1726_the_two_ingredients_replicated/verification/census.py")
c = importlib.util.module_from_spec(spec); spec.loader.exec_module(c)
r = c.compute(0.35, 2.75, Fr(0), Fr(0))
sp = {rn: tuple(r["up|L_max|%s" % rn]) for rn in ("S", "St")}
for s in ("up", "down", "lep"):
    for rn in ("S", "St"):
        assert max(abs(a - b) for a, b in zip(r["%s|L_max|%s" % (s, rn)], sp[rn])) < 1e-12
print("zero line, 0.35+2.75i, L_max: S", sp["S"], " St", sp["St"])
def same(a, b): return max(abs(x - y) / max(abs(x), abs(y)) for x, y in zip(a, b)) < 1e-9
for cfac in (1, 3):
    for rd in itertools.product(("S", "St"), repeat=3):
        u, d, l = sp[rd[0]], sp[rd[1]], sp[rd[2]]
        l = (l[0] * cfac, l[1] / cfac)
        tag = []
        if not same(u, d): tag.append("u!=d")
        if not same(d, l): tag.append("d!=e")
        if not same(u, l): tag.append("u!=e")
        allthree = len(tag) == 3
        print("c=%d reading(u,d,l)=%-14s %-18s %s" % (cfac, ",".join(rd), " ".join(tag) or "all equal", "ALL THREE SPLIT" if allthree else ""))
