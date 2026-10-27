"""Attack 4b: is there ANY line w' (B1713's 266 lines of order 1-12, up to sign) at the same tau whose spectrum under the flipped
assignment (S, S~, S~) equals the source's spectrum under (S~, S, S) in all three sectors?  Positive control: the same search for
the unflipped assignment must find the source line itself (and its mirror partner) at ~0."""
import sys; sys.path.insert(0, str(__import__("pathlib").Path(__file__).resolve().parent))
import os, json, math
from fractions import Fraction as Fr
from multiprocessing import Pool
import importlib.util
spec = importlib.util.spec_from_file_location("cen", str(next(q for q in __import__("pathlib").Path(__file__).resolve().parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file()) / "frontier/B1726_the_two_ingredients_replicated/verification/census.py"))
cen = importlib.util.module_from_spec(spec); spec.loader.exec_module(cen)
LINES = cen.lines()
TAUS = [complex(0.35, 2.9), complex(0.5, 2.9)]
SOURCES = [(Fr(2, 5), Fr(3, 10)), (Fr(2, 5), Fr(1, 10))]
A = {"up": "St", "down": "S", "lep": "S"}; AF = {"up": "S", "down": "St", "lep": "St"}
def job(task):
    import common as C
    ti, k = task; t = TAUS[ti]; a, b = LINES[k]
    sp = C.spectra(t, a, b, "L_max")
    return ti, k, {"%s|%s" % key: v.tolist() for key, v in sp.items()}
if __name__ == "__main__":
    import common as C
    src = {}
    for ti, t in enumerate(TAUS):
        for (a, b) in SOURCES:
            src[(ti, a, b)] = {"%s|%s" % key: v for key, v in C.spectra(t, a, b, "L_max").items()}
    tasks = [(ti, k) for ti in range(len(TAUS)) for k in range(len(LINES))]
    with Pool(4) as P:
        res = P.map(job, tasks, chunksize=4)
    import numpy as np
    out = {}
    for (ti, a, b), s in src.items():
        best_flip, best_ctrl = [], []
        for tj, k, sp in res:
            if tj != ti: continue
            sp = {kk: np.array(v) for kk, v in sp.items()}
            df = max(C.dln(s["%s|%s" % (sec, A[sec])], sp["%s|%s" % (sec, AF[sec])]) for sec in A)
            dc = max(C.dln(s["%s|%s" % (sec, A[sec])], sp["%s|%s" % (sec, A[sec])]) for sec in A)
            # per-sector flip partner (any sector alone)
            best_flip.append((df, k)); best_ctrl.append((dc, k))
        best_flip.sort(); best_ctrl.sort()
        key = "tau=%s src=(%s,%s)" % (TAUS[ti], a, b)
        out[key] = {"flip: 3 best (max-sector ln dev, line)": [(round(d, 4), str(LINES[k])) for d, k in best_flip[:3]],
                    "control unflipped: 3 best": [(float("%.2e" % d), str(LINES[k])) for d, k in best_ctrl[:3]]}
        print(key, json.dumps(out[key]))
    json.dump(out, open(__import__("pathlib").Path(__file__).resolve().parent / "flip_search.json", "w"), indent=1)
