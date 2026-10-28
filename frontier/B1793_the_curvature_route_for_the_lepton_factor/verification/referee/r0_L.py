import sys, importlib.util, pathlib, numpy as np
ROOT = next(q for q in __import__("pathlib").Path(__file__).resolve().parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
spec = importlib.util.spec_from_file_location("c26", ROOT / "frontier/B1726_the_two_ingredients_replicated/verification/census.py")
C = importlib.util.module_from_spec(spec); spec.loader.exec_module(C)
M = C._modules(); B, te, col = M["B"], M["te"], M["col"]
for im in (3.0, 6.0):
    L = float(np.interp(im, [q[0] for q in col], [q[1] for q in col])); print("Im tau", im, "L_max", L, "2 pi L", 2*np.pi*L)
print("col range", col[0][0], col[-1][0])
