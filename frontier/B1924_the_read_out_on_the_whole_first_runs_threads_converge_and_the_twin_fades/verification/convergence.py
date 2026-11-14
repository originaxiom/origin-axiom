"""Why the golden thread's average still moves with the window: the range of the frame's log ratios along one period
(a near-zero singular value gives an integrable log singularity), and the bounded alternative, the average of the
ratios themselves, at 32 and 64 trapezoid nodes and two windows. Structure only is printed; values go to the json."""
import json, math, pathlib
import numpy as np
import thread_average as T
HERE = pathlib.Path(__file__).resolve().parent


def samples(w, start, nodes):
    beta, betap, ell, g = T.geodesic(w)
    zt = lambda s: complex((beta * 1j * math.exp(s) + betap) / (1j * math.exp(s) + 1))
    s0 = start * ell - ell / 2
    return [T.outputs(zt(s0 + ell * j / nodes)) for j in range(nodes)]


def averages(S):
    keys = S[0].keys()
    lin = {k: np.mean([np.array(o[k]) for o in S], 0) for k in keys}
    lg = {k: np.mean([np.log(np.maximum(np.array(o[k]), 1e-300)) for o in S], 0) for k in keys}
    return lin, lg


def spread(A, B):
    return max(float(np.max(np.abs(A[k] - B[k]))) for k in A)


if __name__ == "__main__":
    out = {}
    S64a = samples("LR", 0.0, 64)
    S32a = S64a[::2]
    S64b = samples("LR", 0.37, 64)
    lr = [float(np.log(max(min(o[k]), 1e-300))) for o in S64a for k in o]
    print("golden thread: the smallest log ratio along the period %.1f, the largest %.1f (a deep minimum means a near-zero singular value)" % (min(lr), max(lr)), flush=True)
    l64a, g64a = averages(S64a); l32a, g32a = averages(S32a); l64b, g64b = averages(S64b)
    print("ratios averaged:     32 vs 64 nodes %.1e; window spread at 64 %.1e" % (spread(l32a, l64a), spread(l64a, l64b)), flush=True)
    print("log ratios averaged: 32 vs 64 nodes %.1e; window spread at 64 %.1e" % (spread(g32a, g64a), spread(g64a, g64b)), flush=True)
    out = {"lin64a": {k: v.tolist() for k, v in l64a.items()}, "lin64b": {k: v.tolist() for k, v in l64b.items()},
           "log64a": {k: v.tolist() for k, v in g64a.items()}, "log64b": {k: v.tolist() for k, v in g64b.items()}}
    (HERE / "convergence.json").write_text(json.dumps(out, indent=1))
