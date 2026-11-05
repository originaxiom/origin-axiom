"""Data-free: at B1841's sealed features, are the lepton sector's two ln ratios equal to the down sector's on order-5 lines
(the order dictionary's SU(5) relation Y_e ∝ Y_d^T), at apex 162 (the best row's) and 5 more apexes? No target is read."""
import sys, pathlib, importlib.util, math
from fractions import Fraction as F
import numpy as np
ROOT = next(q for q in pathlib.Path(__file__).resolve().parents if (q / "GENESIS.md").is_file()); H41 = ROOT / "frontier/B1841_the_principled_ends_card/verification"
sp = importlib.util.spec_from_file_location("b1841_look", H41 / "look.py"); L41 = importlib.util.module_from_spec(sp); sys.modules["b1841_look"] = L41; sp.loader.exec_module(L41)
M = L41.C41().C39().mods(); LINES = M["LINES"]
def order(ln):
    a, b = F(str(ln[0])), F(str(ln[1])); return math.lcm(a.denominator, b.denominator)
for ap in (162, 0, 41, 100, 150, 222):
    _, U, D, E = L41.apex_features(ap)
    for o in (5, 10, 3, 4):
        ks = [k for k, ln in enumerate(LINES) if order(ln) == o]
        # lep reading S vs down reading S and its transpose-equivalent (singular values are transpose-invariant)
        big = lambda X: X > math.log(1e-10)
        dev = []
        for k in ks:
            for j in range(4):
                for r in (0, 1):
                    for rr in (0, 1):
                        m = big(E[k, j, r]) & big(D[k, j, rr])
                        if m.all(): dev.append((abs(E[k, j, r] - D[k, j, rr]).max(), r, rr))
        best = {}
        for d, r, rr in dev:
            best[(r, rr)] = max(best.get((r, rr), 0.0), d)
        print("apex %3d order %2d (%2d lines): max |ln lep - ln down| per (lep reading, down reading) %s" % (
            ap, o, len(ks), {("S" if a == 0 else "St") + "/" + ("S" if b == 0 else "St"): "%.2e" % v for (a, b), v in sorted(best.items())}), flush=True)
k = [k for k, ln in enumerate(LINES) if str(ln[0]) == "2/5" and str(ln[1]) == "4/5"][0]
_, U, D, E = L41.apex_features(162)
print("best row (apex 162, line (2/5, 4/5), E4): ln lep S", E[k, 3, 0], "St", E[k, 3, 1], "| ln down S", D[k, 3, 0], "St", D[k, 3, 1])
