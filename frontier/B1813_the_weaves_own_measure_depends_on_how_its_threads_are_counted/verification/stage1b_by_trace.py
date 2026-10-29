"""Stage 1b (data-free): the same geodesic height measure, but over the complete set of primitive positive classes with
trace <= T (ordering by geometric length, Bowen-Margulis' regime), T = 12, 18, 24, 30; found by depth-first search with
trace pruning (a positive word's trace never falls as letters are appended), reduced to necklaces (primitive, both letters).
    python3 stage1b_by_trace.py      # writes stage1b_by_trace.json beside itself"""
import importlib.util, json, math, pathlib
import numpy as np
HERE = pathlib.Path(__file__).resolve().parent
sp = importlib.util.spec_from_file_location("s1", HERE / "stage1_threads_measure.py")
src = (HERE / "stage1_threads_measure.py").read_text().split("words = sorted(")[0]
ns = {"__file__": str(HERE / "stage1_threads_measure.py"), "__name__": "s1"}; exec(compile(src, "s1", "exec"), ns)
geodesic_heights, hyp_cdf_above = ns["geodesic_heights"], ns["hyp_cdf_above"]
L = np.array([[1, 1], [0, 1]], dtype=object); R = np.array([[1, 0], [1, 1]], dtype=object)
def canon(w): return min(w[i:] + w[:i] for i in range(len(w)))
def primitive(w):
    n = len(w); return all(w != w[k:] + w[:k] for k in range(1, n) if n % k == 0)
out = {}
for T in (12, 18, 24, 30):
    classes = set(); stack = [("", np.eye(2, dtype=object))]
    while stack:
        w, M = stack.pop()
        for ch, X in (("L", L), ("R", R)):
            w2, M2 = w + ch, M.dot(X)
            if M2[0, 0] + M2[1, 1] > T or len(w2) > T - 1: continue      # L^k keeps trace 2: cap the length (L^k R has trace k + 2)
            if "L" in w2 and "R" in w2 and primitive(w2): classes.add(canon(w2))
            stack.append((w2, M2))
    H, Wt = [], []
    for w in classes:
        A = np.eye(2, dtype=object)
        for ch in w: A = A.dot(L if ch == "L" else R)
        hs, ell = geodesic_heights([[int(A[0, 0]), int(A[0, 1])], [int(A[1, 0]), int(A[1, 1])]])
        H.extend(hs); Wt.extend([ell / len(hs)] * len(hs))
    H, Wt = np.array(H), np.array(Wt)
    out[T] = {"classes": len(classes), "P(Im tau > Y)": {str(Y): round(float(Wt[H > Y].sum() / Wt.sum()), 4) for Y in (1.0, 1.5, 2.0, 3.0, 4.0, 6.0)}}
    print(T, out[T], flush=True)
out["hyperbolic area"] = {str(Y): round(hyp_cdf_above(Y), 4) for Y in (1.0, 1.5, 2.0, 3.0, 4.0, 6.0)}
(HERE / "stage1b_by_trace.json").write_text(json.dumps(out, indent=1), encoding="utf-8"); print(out["hyperbolic area"])
