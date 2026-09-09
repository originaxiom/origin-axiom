#!/usr/bin/env python3
"""B1324 PART D -- the four-record probe (DESIGN section 6): SL(4,Z) transvection closures to length 4; the minimal-trace mixed
hyperbolic closure; is its dilatation theta_4^4 for theta_4 the smallest quartic Pisot number (x^4 - x^3 - 1)?"""
import itertools, json, pathlib
import numpy as np, sympy as sp
HERE = pathlib.Path(__file__).resolve().parent

def transvections(n):
    T = {}
    for i in range(n):
        for j in range(n):
            if i != j:
                E = np.eye(n, dtype=np.int64); E[i, j] = 1; T[f"E{i+1}{j+1}"] = E
    return T

def run(n=4, maxlen=4):
    T = transvections(n); names = list(T); seen = {}; rows = []
    for L in range(1, maxlen + 1):
        for word in itertools.product(names, repeat=L):
            B = np.eye(n, dtype=np.int64)
            for w in word: B = B @ T[w]
            key = B.tobytes()
            if key in seen: continue
            seen[key] = word
            touched = set(int(c) for w in word for c in w[1:])
            ev = np.linalg.eigvals(B.astype(float)); mods = sorted(abs(ev))
            rows.append(dict(word=word, mixed=(touched == set(range(1, n + 1))), trace=int(np.trace(B)), hyperbolic=all(abs(m - 1) > 1e-9 for m in mods),
                             eig_moduli=[round(m, 6) for m in mods], detBI=int(round(np.linalg.det(B - np.eye(n)))), B=B.tolist()))
    mh = [r for r in rows if r["mixed"] and r["hyperbolic"]]
    tmin = min(r["trace"] for r in mh); minimal = [r for r in mh if r["trace"] == tmin]
    t, x = sp.symbols("t x")
    charpolys = sorted({str(sp.factor(sp.Matrix(r["B"]).charpoly(t).as_expr())) for r in minimal})
    theta4_min = x ** 4 - x ** 3 - 1; theta4 = max(abs(r) for r in np.roots([1, -1, 0, 0, -1]))
    mp_theta4_4 = sp.factor(sp.resultant(theta4_min, t - x ** 4, x))
    # the smallest Pisot number among quartics with small coefficients (control for the choice x^4 - x^3 - 1)
    best = None
    for c in itertools.product(range(-3, 4), repeat=4):
        if c[-1] == 0: continue
        roots = np.roots([1, *c]); big = [r for r in roots if abs(r.imag) < 1e-9 and r.real > 1]; small = [r for r in roots if abs(r) < 1 - 1e-9]
        if len(big) == 1 and len(small) == 3:
            p = sp.Poly([1, *c], x)
            if p.is_irreducible and (best is None or big[0].real < best[0]): best = (float(big[0].real), c)
    dil = max(minimal[0]["eig_moduli"])
    out = dict(records=n, distinct_products=len(rows), mixed_hyperbolic=len(mh), min_trace=tmin, n_minimal=len(minimal),
               minimal_examples=[(r["word"], r["eig_moduli"], r["detBI"]) for r in minimal[:6]], charpolys_of_minimal=charpolys,
               dilatation=dil, theta4=float(theta4), theta4_pow4=float(theta4 ** 4), minpoly_theta4_pow4=str(mp_theta4_4),
               smallest_quartic_pisot_small_coeffs=best,
               PASS=any(sp.expand(sp.sympify(cp) - mp_theta4_4) == 0 or sp.expand(sp.sympify(cp) + mp_theta4_4) == 0 for cp in charpolys))
    (HERE / "d_four_records.json").write_text(json.dumps(out, indent=1, default=str), encoding="utf-8")
    for k, v in out.items():
        if k != "minimal_examples": print(f"  {k}: {v}")
    print("  minimal examples:", out["minimal_examples"][:3])
    print("D FOUR RECORDS:", "PASS (dilatation = theta_4^4)" if out["PASS"] else "FAIL (the pattern was two instances)")

if __name__ == "__main__":
    run()
