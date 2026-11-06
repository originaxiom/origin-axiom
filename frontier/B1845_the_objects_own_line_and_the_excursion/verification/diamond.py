"""Data-free: is the diamond operator <2> ((1/5, 2/5) <-> (2/5, 4/5), RL's two fixed order-5 lines) a symmetry of the frame?
Compare the sealed features (ln ratios per sector and reading) at the two lines, at 8 apexes and all four ends; also the
<2>-pair (1/5, 3/5) <-> (2/5, 1/5) (LR's). Any sector permutation allowed. No target is read."""
import sys, math, pathlib, importlib.util, itertools
import numpy as np
ROOT = next(q for q in pathlib.Path(__file__).resolve().parents if (q / "GENESIS.md").is_file()); H41 = ROOT / "frontier/B1841_the_principled_ends_card/verification"
sp = importlib.util.spec_from_file_location("b1841_look", H41 / "look.py"); L41 = importlib.util.module_from_spec(sp); sys.modules["b1841_look"] = L41; sp.loader.exec_module(L41)
LINES = [(str(a), str(b)) for a, b in L41.C41().C39().mods()["LINES"]]
pairs = [(("1/5", "2/5"), ("2/5", "4/5")), (("1/5", "3/5"), ("2/5", "1/5"))]
idx = {p: LINES.index(p) for pr in pairs for p in pr}
worst = {pr: [] for pr in pairs}
for ap in (0, 30, 60, 90, 120, 162, 190, 222):
    _, U, D, E = L41.apex_features(ap); S = {"up": U, "down": D, "lep": E}
    for pr in pairs:
        k1, k2 = idx[pr[0]], idx[pr[1]]
        for j in range(4):
            best = 1e9
            for perm in itertools.permutations(("up", "down", "lep")):
                for rflip in (False, True):
                    d = 0.0
                    for s1, s2 in zip(("up", "down", "lep"), perm):
                        x = S[s1][k1, j]; y = S[s2][k2, j][::-1] if rflip else S[s2][k2, j]
                        m = (x > math.log(1e-10)) & (y > math.log(1e-10))
                        if m.any(): d = max(d, float(np.max(np.abs((x - y)[m]))))
                    best = min(best, d)
            worst[pr].append(best)
for pr, v in worst.items():
    print("%s <-> %s: best-matching (any sector permutation, reading swap) max |d ln ratio| over 8 apexes x 4 ends: min %.3e, median %.3e, max %.3e" % (pr[0], pr[1], min(v), float(np.median(v)), max(v)))
