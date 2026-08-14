"""B901 (N5): which symmetries stabilize the measurement torus C?

(a) the continuous normalizer n(C) = {x in e6 : [x, C] subset span(C)},
    exact nullspace over Q -- compared with the centralizer z(C);
(b) the spectral obstructions: exact factor multisets of ad(x8) vs ad(x16)
    (from B898), evenness (sign-flip allowance), and the split/compact
    invariance (B898 types are Aut(R)-invariants).
Writes normalizer.json + spectral_obstructions.json.
"""
import io, contextlib, json, os
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(open(os.path.join(HERE, "..", "B854_centralizer_exact",
                                   "e6_centralizer.py")).read(),
                 "b854", "exec"), globals())

ADSm = {n: sp.Matrix(ADS[n]) for n in ns}
Cvecs = [sp.Matrix([sp.Rational(c) for c in INV[n]]) for n in ns]
Cspan = sp.Matrix.hstack(*Cvecs)
P = sp.Matrix.vstack(*[v.T for v in Cspan.T.nullspace()])
big = sp.Matrix.vstack(*[P * ADSm[n] for n in ns])
dim_n = len(big.nullspace())
dim_z = len(sp.Matrix.vstack(*[ADSm[n] for n in ns]).nullspace())
print("dim n(C) =", dim_n, " dim z(C) =", dim_z)
json.dump({"dim_normalizer": dim_n, "dim_centralizer": dim_z},
          open(os.path.join(HERE, "normalizer.json"), "w"), indent=1)

r = json.load(open(os.path.join(HERE, "..", "B898_exact_census/results.json")))
t = sp.Symbol("t")
obs = {}
f8 = sorted(str(f[0]) for f in r["8"]["factors"] if f[0] != "t")
f16 = sorted(str(f[0]) for f in r["16"]["factors"] if f[0] != "t")
obs["x8_x16_same_spectrum"] = (f8 == f16)
def all_even(fl):
    out = True
    for fs in fl:
        p = sp.Poly(sp.sympify(fs), t)
        out = out and all(c == 0 for c in p.all_coeffs()[1::2])
    return out
obs["x8_factors_even"] = all_even(f8)
obs["x16_factors_even"] = all_even(f16)
print("same spectrum:", obs["x8_x16_same_spectrum"],
      "| even (sign-flip allowed):", obs["x8_factors_even"], obs["x16_factors_even"])
json.dump(obs, open(os.path.join(HERE, "spectral_obstructions.json"), "w"),
          indent=1)
print("saved")
