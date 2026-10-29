"""Check 7: where the draft's float axis sampler (z = m + r(tanh s + i sech s), s up to ell) loses precision, against
the run-segment sampler (all quantities O(1)).  Uniform random words of length n; P(Im > 2) per word, both samplers."""
import math, random, sys, os
import numpy as np
sys.path.insert(0, os.path.dirname(__file__))
from refcore import mat, runs, reduce_vec, segments_from_runs, axis_samples
rng = random.Random(7)
for n in (14, 30, 40, 50, 70):
    worst = 0.0; ells = []
    for _ in range(40):
        w = "".join(rng.choice("LR") for _ in range(n))
        if "L" not in w or "R" not in w: continue
        M = mat(w); z, wt, ell = axis_samples(M); h1 = reduce_vec(z).imag
        z2, wt2, _ = segments_from_runs(runs(w)); h2 = reduce_vec(z2).imag
        p1 = wt[h1 > 2].sum() / wt.sum(); p2 = wt2[h2 > 2].sum() / wt2.sum(); worst = max(worst, abs(p1 - p2)); ells.append(ell)
    print("n=%d  median ell=%.1f  max |P_axis - P_runs| (Y=2) = %.4f" % (n, np.median(ells), worst))
