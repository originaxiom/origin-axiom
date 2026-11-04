"""agy:B1764's apex in MAIN's B1720 convention (thread_geometry.py: L = [[1,1],[0,1]], R = [[1,0],[1,1]]; height = Lagrange(w)/2):
is (1 + i sqrt 84)/3 the B1720 apex of LLLLLRRLRLLR, and is B1764's A = [[115,-32],[18,-5]] conjugate in SL(2,Z) to the word's matrix?"""
import sys, math, pathlib, importlib.util, json
import numpy as np
ROOT = next(p for p in pathlib.Path(__file__).resolve().parents if (p / "frontier").is_dir() and (p / "GENESIS.md").is_file())
sp_ = importlib.util.spec_from_file_location("tg", ROOT / "frontier/B1720_the_thread_fixes_the_point/verification/thread_geometry.py"); tg = importlib.util.module_from_spec(sp_); sp_.loader.exec_module(tg)
w = "LLLLLRRLRLLR"; M = tg.mat(w); h = tg.lagrange(w) / 2
A = np.array([[115, -32], [18, -5]])
# conjugacy: search X in SL(2,Z) with small entries such that X M X^-1 = A (or A^-1-free: same trace class)
found = []
rng = range(-12, 13)
for a in rng:
    for b in rng:
        for c in rng:
            for d in rng:
                if a * d - b * c != 1: continue
                X = np.array([[a, b], [c, d]]); Xi = np.array([[d, -b], [-c, a]])
                if np.array_equal(X @ M @ Xi, A): found.append([[a, b], [c, d]])
apexA = ((A[0, 0] - A[1, 1]) / (2 * A[1, 0]), math.sqrt(np.trace(A) ** 2 - 4) / (2 * abs(A[1, 0])))
out = {"word_matrix": M.tolist(), "trace": int(np.trace(M)), "B1720_height": h, "sqrt84/3": math.sqrt(84) / 3, "A_apex": apexA, "conjugators": found[:4], "n_conjugators_found": len(found)}
print("B1720 convention: mat(%s) = %s, trace %d; height Lagrange/2 = %.10f ; sqrt(84)/3 = %.10f" % (w, M.tolist(), np.trace(M), h, math.sqrt(84) / 3))
print("A's axis apex: center %.6f (= 1/3 mod 1), height %.10f; X M X^-1 = A for X in SL(2,Z) (entries <= 12): %d found, e.g. %s" % (apexA[0], apexA[1], len(found), found[:2]))
json.dump(out, open(pathlib.Path(__file__).with_suffix(".json"), "w"), indent=1); print("exit 0")
