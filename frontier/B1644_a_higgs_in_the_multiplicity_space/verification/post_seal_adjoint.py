#!/usr/bin/env python3
"""B1644, post-seal (labelled): why the smallest mass is zero. Symbolic det Y(a) for Y(a) = a_i Y(i) + a_j Y(j) + a_k Y(k)
with the hand table (S1 held exactly); its null vector; complex directions; and the range of the middle ratio m."""
import json, pathlib
import sympy as sp
import numpy as np
HERE = pathlib.Path(__file__).resolve().parent
ai, aj, ak, Ri, Rj, Rk = sp.symbols("a_i a_j a_k R_i R_j R_k")
Yi = sp.Matrix([[-Ri, Rj, 0], [Rj, Ri, Rk], [0, Rk, -Ri]])
Yj = sp.Matrix([[Rj, Ri, Rk], [Ri, -Rj, 0], [Rk, 0, -Rj]])
Yk = sp.Matrix([[-Rk, 0, Rj], [0, -Rk, Ri], [Rj, Ri, Rk]])
Y = ai * Yi + aj * Yj + ak * Yk
det = sp.factor(sp.expand(Y.det()))
ns = Y.nullspace()
out = {"det_Y(a)": str(det), "det_is_identically_zero": bool(sp.simplify(det) == 0),
       "null_vector": [str(sp.simplify(x)) for x in ns[0]] if ns else None}
# the middle ratio over random real and complex directions and the R's at sample tau (closed forms from the run's S1)
d = json.load(open(HERE / "adjoint_higgs.json"))
rng = np.random.default_rng(16440)
mids = {"real": [], "complex": []}
for _ in range(2000):
    R = rng.normal(size=3) + 1j * rng.normal(size=3)
    f = sp.lambdify((ai, aj, ak, Ri, Rj, Rk), Y, "numpy")
    for kind in ("real", "complex"):
        a = rng.normal(size=3) + (1j * rng.normal(size=3) if kind == "complex" else 0)
        s = np.linalg.svd(np.array(f(*a, *R), dtype=complex), compute_uv=False); s = s / s[0]
        mids[kind].append((float(s[1]), float(s[2])))
out["random_R_and_a"] = {k: {"middle_range": [min(m for m, _ in v), max(m for m, _ in v)], "smallest_max": max(z for _, z in v)} for k, v in mids.items()}
json.dump(out, open(HERE / "post_seal_adjoint.json", "w"), indent=1)
print(json.dumps(out, indent=1))
