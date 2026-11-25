"""B1979, second reading (data-free): the converged classes (heights 40-50, snapped to the grid of 1/60, from heights_run.json)
read on B1978's orbits of the act's monodromy M = [[2,1],[1,1]] at a fixed tau (B1978's dated caveat applies), and on the
CRT parts of the point. No frame computation.
    python3 -B orbits_classes.py > orbits_classes_run.txt"""
import json, pathlib
from fractions import Fraction as Fr
R = json.loads(pathlib.Path(__file__).with_name("heights_run.json").read_text())
K = ("up_m2m3", "up_m1m3", "down_m2m3", "down_m1m3", "lep_m2m3", "lep_m1m3", "V12", "V23", "V13")
cls = {(Fr(r["a"]), Fr(r["b"])): tuple(Fr(round(r["r4050"][k] * 60), 60) for k in K) for r in R}
names = {c: i for i, c in enumerate(sorted(set(cls.values()), key=lambda c: (-sum(v == c for v in cls.values()), c)))}
def act(w): return ((2 * w[0] + w[1]) % 1, (w[0] + w[1]) % 1)
print("the act keeps the converged class at %d of 96" % sum(cls[act(w)] == cls[w] for w in cls))
seen, orbits = set(), []
for w in sorted(cls):
    if w in seen: continue
    o = [w]; x = act(w)
    while x != w: o.append(x); x = act(x)
    seen |= set(o); orbits.append(o)
for o in orbits:
    print("orbit from (%s, %s): classes along it %s" % (o[0][0], o[0][1], [names[cls[w]] for w in o]))
def parts(w):
    a, b = w
    return ((6 * a) % 1, (6 * b) % 1), ((15 * a) % 1, (15 * b) % 1), ((10 * a) % 1, (10 * b) % 1)
for i, nm in ((0, "5-part"), (1, "2-part"), (2, "3-part")):
    G = {}
    for w, c in cls.items(): G.setdefault(parts(w)[i], set()).add(names[c])
    print("%s: %d values; classes per value %s" % (nm, len(G), sorted(len(v) for v in G.values())))
G = {}
for w, c in cls.items(): G.setdefault((parts(w)[1], parts(w)[2]), set()).add(names[c])
print("6-part: %d values; classes per value %s" % (len(G), sorted(len(v) for v in G.values())))
print("lepton m2/m3 rate over the 96 points: %s" % sorted({c[4] for c in cls.values()}))
print("V13 = V12 + V23 in %d of %d classes" % (sum(c[8] == c[6] + c[7] for c in names), len(names)))
