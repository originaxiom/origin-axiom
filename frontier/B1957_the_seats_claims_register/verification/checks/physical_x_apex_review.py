"""B1957: the physical lane's package 'X-APEX review' (2026-11-17), fifteen findings XA-01 to XA-15 on another seat's
sources: custody of its quotations, and the mathematics inside four of the findings, on main.  The other seat's scripts
are read as text; nothing is run.  Needs the seats' branches fetched.
 X0  all 36 excerpts of the package's QUOTATIONS.json are at the commit, path and line it names.
 X1  XA-07: the permutation [4, 3, 5, 0, 1, 2, 6, 7] is (0 4 1 3)(2 5), of order 4, not an involution.
 X2  XA-03: for q = f0 + f1 exp(i y), the cubic |q|^2 q has Fourier modes -1 and 2 with coefficients f0^2 f1 and
     f0 f1^2, beside modes 0 and 1.
 X3  XA-04: a Rayleigh-Ritz value on a subspace is an upper bound for the least eigenvalue, never a lower one (a
     random symmetric matrix and a random subspace).
 X4  XA-12: a determinant can be non-zero at a finite height while its leading coefficient cancels (the matrix
     [[1, 1], [1, 1 + x]] in a small parameter x: leading minors cancel, the determinant is x).
 (XA-08's central scalar, S^2 = gamma^-2 C, is in physical_all_seats_findings.py, A2.)"""
import functools, json, subprocess
import numpy as np
import sympy as sp
print = functools.partial(print, flush=True)
LANE = "8d5c91032"; DIR = "reports/physical_bridge_2026_09_05/x_apex_review_2026_11_17/"

if __name__ == "__main__":
    raw = subprocess.run(["git", "show", "%s:%sQUOTATIONS.json" % (LANE, DIR)], capture_output=True).stdout
    if raw:
        d = json.loads(raw); ok = 0; per = {}
        for it in d["checks"]:
            b = subprocess.run(["git", "show", "%s:%s" % (d["source_commit"], it["path"])], capture_output=True).stdout.decode("utf-8", "replace").split("\n")
            hit = 1 <= it["line"] <= len(b) and it["exact_excerpt"].strip() in b[it["line"] - 1]; ok += hit; per.setdefault(it["finding"], [0, 0]); per[it["finding"]][0] += hit; per[it["finding"]][1] += 1
        print("X0: excerpts at their lines: %d of %d; by finding: %s" % (ok, len(d["checks"]), {k: "%d/%d" % tuple(v) for k, v in sorted(per.items())}))
    else: print("X0: the lane's branch is not fetched here; custody not checked")
    p = [4, 3, 5, 0, 1, 2, 6, 7]; q = list(range(8)); order = 0
    while True:
        q = [p[i] for i in q]; order += 1
        if q == list(range(8)): break
    cyc = []; seen = set()
    for i in range(8):
        if i in seen or p[i] == i: continue
        c = [i]; seen.add(i); j = p[i]
        while j != i: c.append(j); seen.add(j); j = p[j]
        cyc.append(tuple(c))
    print("X1: the permutation has cycles %s and order %d" % (cyc, order))
    f0, f1, y = sp.symbols("f0 f1 y", real=True); qq = f0 + f1 * sp.exp(sp.I * y); cub = sp.expand(qq * sp.conjugate(qq) * qq); modes = {k: sp.simplify(sp.integrate(sp.expand(cub * sp.exp(-sp.I * k * y)), (y, 0, 2 * sp.pi)) / (2 * sp.pi)) for k in (-1, 0, 1, 2)}
    print("X2: the Fourier coefficients of |q|^2 q at modes -1, 0, 1, 2: %s" % {k: str(v) for k, v in modes.items()})
    rng = np.random.default_rng(50); M = rng.normal(size=(12, 12)); M = M + M.T; lo = np.linalg.eigvalsh(M)[0]; worst = min(np.linalg.eigvalsh((lambda Qb: Qb.T @ M @ Qb)(np.linalg.qr(rng.normal(size=(12, 4)))[0]))[0] - lo for _ in range(200))
    print("X3: over 200 random four-dimensional subspaces the least Ritz value exceeds the least eigenvalue by at least %.3f (never below it)" % worst)
    x = sp.symbols("x"); Mx = sp.Matrix([[1, 1], [1, 1 + x]]); print("X4: det [[1, 1], [1, 1 + x]] = %s: non-zero at any x != 0, while the order-zero terms of its two products cancel" % Mx.det())
