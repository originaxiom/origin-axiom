"""diagnose third opinion (2a): the same 30 random rows (rng 41003); per row and quantity, the sealed vs independent log
ratio, with the ratio's size, so a discrepancy at machine-noise ratios is told apart from a real one."""
import sys, math, json, pathlib, importlib.util, random
import numpy as np
ROOT = next(q for q in pathlib.Path(__file__).resolve().parents if (q / "GENESIS.md").is_file()); H41 = ROOT / "frontier/B1841_the_principled_ends_card/verification"
sp = importlib.util.spec_from_file_location("b1841_look", H41 / "look.py"); L41 = importlib.util.module_from_spec(sp); sys.modules["b1841_look"] = L41; sp.loader.exec_module(L41)
sys.path.insert(0, str(ROOT / "frontier/B1842_the_closure_instruments/verification")); import exact_card_instrument as X
c41 = L41.C41(); M = c41.C39().mods(); acc = c41.C39().load_acc(); nl = len(M["LINES"]); na = len(M["AP"]); ne = 4
rng = random.Random(41003); ENDS = lambda r: [r["L_2"], math.log(2), r["L_max"], r["L_2"] - math.pi / 2]
cache = {}; rows = []
for _ in range(30):
    i = rng.randrange(na); k = rng.randrange(nl); j = rng.randrange(ne); rows.append((i, k, j))
big = 0; worst_sig = 0.0
for (i, k, j) in rows:
    if i not in cache: cache[i] = L41.apex_features(i)
    _, U, D, E = cache[i]; r = acc[i]; a, b = M["LINES"][k]
    Y, _ = X.yukawas_exact(r["tau0"][0], r["tau0"][1], a, b, ENDS(r)[j] - r["L_max"], ("up", "down", "lep"))
    for sec, A in (("up", U), ("down", D), ("lep", E)):
        for rn_i, rn in enumerate(("S", "St")):
            ind = np.log(np.maximum(X.ratios_of(Y[sec][rn]), 1e-300)); sea = A[k, j, rn_i]
            for q in range(2):
                dlt = abs(ind[q] - sea[q]); size = math.exp(min(ind[q], sea[q]))
                if dlt > 1e-8:
                    big += 1
                    print("row (apex %d, line %d %s, end %d) %s %s ratio#%d: sealed ln %.3f indep ln %.3f  |d| %.2e  ratio size %.1e" % (i, k, (str(a), str(b)), j, sec, rn, q, sea[q], ind[q], dlt, size))
                    if size > 1e-10: worst_sig = max(worst_sig, dlt)
print("discrepancies > 1e-8: %d of %d values; worst among ratios > 1e-10: %.2e" % (big, 30 * 12, worst_sig))
