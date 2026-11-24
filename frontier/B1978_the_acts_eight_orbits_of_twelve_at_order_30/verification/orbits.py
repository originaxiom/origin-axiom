"""B1978 (main, 2026-11-24; data-free): the act's monodromy M = [[2,1],[1,1]] on B1976's 96 order-30 points, read against
B1977's committed rates (no new frame computation): its orbits, and alignment, hierarchy and the slow 2-3 mixing on each.
    python3 -B orbits.py > orbits_run.txt"""
import json, pathlib
from fractions import Fraction as Fr
ROOT = next((q for q in [*pathlib.Path(__file__).resolve().parents, pathlib.Path.cwd()] if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file()))
R = json.loads((next((ROOT / "frontier").glob("B1977_*")) / "verification" / "rates30_run.json").read_text())
K = ("up_m2m3", "up_m1m3", "down_m2m3", "down_m1m3", "lep_m2m3", "lep_m1m3", "V12", "V23", "V13")
row = {(Fr(r["a"]), Fr(r["b"])): r for r in R}
def act(w): return ((2 * w[0] + w[1]) % 1, (w[0] + w[1]) % 1)
cls = {w: tuple(round(r[k], 2) for k in K) for w, r in row.items()}
print("M maps the 96 points into themselves: %s; it keeps the rate class at %d of 96" % (all(act(w) in row for w in row), sum(cls[act(w)] == cls[w] for w in row)))
seen, orbits = set(), []
for w in sorted(row):
    if w in seen: continue
    o = [w]; x = act(w)
    while x != w: o.append(x); x = act(x)
    seen |= set(o); orbits.append(o)
print("orbits: %d, sizes %s" % (len(orbits), sorted(len(o) for o in orbits)))
hier = lambda v: v["up_m2m3"] >= 0.1 and v["down_m2m3"] >= 0.1 and v["up_m1m3"] >= 0.2 and v["down_m1m3"] >= 0.2
for o in orbits:
    vs = [row[w] for w in o]
    print("orbit from (%s, %s): aligned %d of 12, hierarchical in both quark sectors %d of 12, slow 2-3 (rate within 3e-3 of 1/30) %d; least mixing rates %s" % (
        o[0][0], o[0][1], sum(v["diag"] >= 0.9 for v in vs), sum(hier(v) for v in vs), sum(abs(v["V23"] - 1 / 30) < 3e-3 for v in vs),
        sorted({round(min(v["V12"], v["V23"], v["V13"]), 3) for v in vs})))
print("SUMMARY: aligned at %d of 96, hierarchical at %d of 96; orbits carrying the slow 2-3 mixing: %d of %d" % (
    sum(v["diag"] >= 0.9 for v in R), sum(hier(v) for v in R), sum(any(abs(row[w]["V23"] - 1 / 30) < 3e-3 for w in o) for o in orbits), len(orbits)))
