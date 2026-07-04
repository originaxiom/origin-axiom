"""B410 2b-i -- does sigma_cl act at window level? exhaustive affine ι search."""
import json, os, sys
from fractions import Fraction as Fr
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "B367_value_map"))
T = json.load(open(os.path.join(HERE, "..", "B367_value_map", "step0_tables.json")))["1,2"]
o1, o2 = 20, 12
def cell(a, b):
    r = T.get(f"{a%o1},{b%o2}")
    return tuple(Fr(x) for x in r) if r else (Fr(0),)*4
def scl(t): return (t[0], -t[1], -t[2], t[3])
support = [tuple(map(int, k.split(","))) for k in T]

from math import gcd
hits = []
for a1 in range(o1):
    if gcd(a1, o1) != 1: continue
    for a0 in range(o1):
        for b1 in range(o2):
            if gcd(b1, o2) != 1: continue
            for b0 in range(o2):
                ok = True
                for (a, b) in support:
                    if cell((a1*a+a0) % o1, (b1*b+b0) % o2) != scl(cell(a, b)):
                        ok = False; break
                if ok: hits.append((a1, a0, b1, b0))
print("affine window involutions ι with t(ι)=σ_cl·t:", hits if hits else "NONE")
# also test the mirror-composed and known symmetries as controls
res = dict(window_class_action=hits, exists=bool(hits))
json.dump(res, open(os.path.join(HERE, "b2i_window.json"), "w"), indent=1)
print("DONE")
