"""Check 1: the move-count table at n = 10, 12 (and 14), by two independent samplers; the partition identity
sum of run-segments = 2 arccosh(t/2); c > 0 for every positive word with both letters."""
import math, sys, json
import numpy as np
sys.path.insert(0, __import__("os").path.dirname(__file__))
from refcore import lyndon, mat, runs, reduce_vec, segments_from_runs, axis_samples

GRID = [1.0, 1.5, 2.0, 3.0, 4.0, 6.0]
out = {}
for n in (10, 12, 14):
    ws = lyndon(n)
    H1, W1, H2, W2 = [], [], [], []
    worst_len = 0.0; cmin = 10 ** 9; cnt_cneg = 0
    for w in ws:
        M = mat(w); t = M[0][0] + M[1][1]; cmin = min(cmin, M[1][0]); cnt_cneg += M[1][0] <= 0
        z, wt, ell = axis_samples(M); H1.append(reduce_vec(z).imag); W1.append(wt)
        z2, wt2, tot = segments_from_runs(runs(w)); H2.append(reduce_vec(z2).imag); W2.append(wt2)
        worst_len = max(worst_len, abs(tot - 2 * math.acosh(t / 2)))
    H1, W1, H2, W2 = map(np.concatenate, (H1, W1, H2, W2))
    row = {"threads": len(ws), "min c": cmin, "c<=0 count": cnt_cneg, "max |sum segments - ell|": worst_len,
           "axis": {str(Y): round(float(W1[H1 > Y].sum() / W1.sum()), 5) for Y in GRID},
           "runs": {str(Y): round(float(W2[H2 > Y].sum() / W2.sum()), 5) for Y in GRID}}
    # unweighted-by-length variant (each thread mass 1) for the runs sampler
    out[n] = row; print(n, json.dumps(row), flush=True)
json.dump(out, open(__file__.replace(".py", ".json"), "w"), indent=1)
