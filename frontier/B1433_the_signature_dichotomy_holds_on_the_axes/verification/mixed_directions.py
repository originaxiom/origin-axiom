#!/usr/bin/env python3
"""B1433 -- C29's quantifier. The signature dichotomy was banked (B898) with the clause "zero generic-complex on C",
C the rank-4 torus spanned by the four charges x8, x14, x16, x22. B898's census classified the four AXES only.
This script computes, on main's own exact E6 frame (B854, executed read-only):
  * the ad-spectrum type of each axis (re-deriving B898),
  * of every pairwise sum and of two further mixed combinations,
  * and, for x8 + x14, the EXACT classification: characteristic polynomial over Q, factored, each factor's real roots
    counted by Sturm and its purely imaginary roots counted by Sturm on g where f(t) = g(t^2).
Outputs: ad_matrices.json (the four exact rational 78x78 matrices, so the lock need not rebuild the frame) and
mixed_directions.json.  Run from anywhere; ~5 minutes (the frame build dominates)."""
import io, contextlib, itertools, json, pathlib
import sympy as sp

OUT = pathlib.Path(__file__).resolve().parent
src = (OUT.parents[1] / "B854_centralizer_exact" / "e6_centralizer.py").read_text()
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(src, "b854", "exec"), globals())          # the frame's own globals (it rebinds HERE) stay its own
OUT = pathlib.Path(__file__).resolve().parent

AX = [8, 14, 16, 22]
M = {n: sp.Matrix(ADS[n]) for n in AX}
assert all((M[a] * M[b] - M[b] * M[a]).is_zero_matrix for a in AX for b in AX), "the four charges must commute"
json.dump({str(n): [[str(x) for x in row] for row in M[n].tolist()] for n in AX}, open(OUT / "ad_matrices.json", "w"))

t = sp.Symbol("t"); s = sp.Symbol("s")

def exact_type(A):
    """(zero, real, imaginary, generic_complex) of the eigenvalues of A, exactly, with the factor certificates."""
    cp = sp.Poly(A.charpoly(t).as_expr(), t)
    z = r = im = cx = 0; certs = []
    for f, m in sp.factor_list(cp.as_expr())[1]:
        p = sp.Poly(f, t); d = p.degree(); co = p.all_coeffs()
        if d == 1 and co[-1] == 0:
            z += m; certs.append(dict(factor="t", mult=int(m))); continue
        nreal = sp.polys.polytools.count_roots(p)
        nimag = 0
        if all(c == 0 for c in co[1::2]):                              # f(t) = g(t^2)
            g = sp.Poly(list(co[::2]), s)
            nimag = 2 * sp.polys.polytools.count_roots(g, None, 0) - (2 if g.eval(0) == 0 else 0)
        r += nreal * m; im += nimag * m; cx += (d - nreal - nimag) * m
        certs.append(dict(coeffs=[str(c) for c in co], degree=int(d), mult=int(m), real_roots=int(nreal), imaginary_roots=int(nimag)))
    assert z + r + im + cx == 78
    return dict(zero=int(z), real=int(r), imaginary=int(im), generic_complex=int(cx), factors=certs)

out = {"axes": {}, "mixed_exact": {}, "pairs_kernel": {}}
for n in AX:
    out["axes"][f"x{n}"] = {k: v for k, v in exact_type(M[n]).items() if k != "factors"}
    print(f"x{n}", out["axes"][f"x{n}"], flush=True)
combos = {f"x{a}+x{b}": M[a] + M[b] for a, b in itertools.combinations(AX, 2)}
combos["x8+2*x14"] = M[8] + 2 * M[14]
combos["2*x8+3*x14+5*x16+7*x22"] = 2 * M[8] + 3 * M[14] + 5 * M[16] + 7 * M[22]
for name, A in combos.items():
    out["mixed_exact"][name] = exact_type(A)
    print(name, {k: v for k, v in out["mixed_exact"][name].items() if k != "factors"}, flush=True)
json.dump(out, open(OUT / "mixed_directions.json", "w"), indent=1)
print("saved")
