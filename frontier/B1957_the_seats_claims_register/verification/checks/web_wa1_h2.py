"""B1957: the web seat's W-A1, line 155 (H2): how far the two Higgs readings differ away from tau = i, in the two measures
the seat's review separates (its post hoc script's definition, read as text): the largest relative deviation of the
ratios, |S~/S - 1|, and the largest absolute deviation of |V| over the four reading pairs.  On main's frame code, at the
seat's four control points.  Data-free."""
import math, pathlib, sys
import numpy as np
HERE = pathlib.Path(__file__).resolve().parent
ROOT = next(q for q in HERE.parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
sys.path.insert(0, str(HERE)); import web_wa1_part3 as P
s0 = math.atanh(-1 / math.sqrt(5)); ax = lambda s: (repr(0.5 + (math.sqrt(5) / 2) * math.tanh(s)), (math.sqrt(5) / 2) / math.cosh(s))
if __name__ == "__main__":
    for lab, (tx, ty), seat in (("1.3i", ("0", 1.3), (0.701, 0.724)), ("0.05 + 0.9i", ("0.05", 0.9), (0.676, 0.655)), ("the act's axis at s0 - 0.05", ax(s0 - 0.05), (0.165, 0.415)), ("the act's axis at s0 + 0.05", ax(s0 + 0.05), (0.280, 0.560))):
        r, V = P.out(tx, ty, P.MARK)
        rel = max(abs(r[(sec, "St")][i] / r[(sec, "S")][i] - 1) for sec in ("up", "down") for i in (0, 1)); rec = max(abs(r[(sec, "S")][i] / r[(sec, "St")][i] - 1) for sec in ("up", "down") for i in (0, 1))
        v = max(float(np.abs(V[k] - V[("S", "S")]).max()) for k in V)
        print("%-28s S~ against S: ratios %.3f (the seat: %.3f); the same with the two exchanged %.3f; |V| over the four pairs %.3f (the seat: %.3f)" % (lab, rel, seat[0], rec, v, seat[1]), flush=True)
