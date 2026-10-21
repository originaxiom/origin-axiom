"""B1697 (the owner's scan for misses): the computations behind its verified items, mathematics only, no data.
(1) W68 G1 on main: in B1691's weight-7/2 family a = alpha E4 R + beta D2R, the unit at the cusp (the x^-1 terms, on v+ only)
    cancels at exactly one ratio, t = alpha/beta = -1/48; a0 = D2R - E4 R/48 is holomorphic at the cusp (no end data); at
    weights -1/2 and 3/2 every section carries the unit (R, DR).  So the Higgs without end data is unique, at weight 7/2.
(2) a0's mass ratios: no second-to-third hierarchy near the cusp (m2/m3 -> 1/2; B1646's real-direction control), m2 = 0 at
    omega (an isotropic eigenline, B1691's table for k = 7/2 mod 6).
(3) Both sections at the record's candidate taus (omega, i; B1483's spin-structure end curves at m004's cusp; W51's
    coupling-norm peaks; the cusp shape), by B1646's exact formulas (the large-L limit).
    python3 -B the_scan.py      # writes the_scan.json beside itself"""
import io, json, contextlib, importlib.util, pathlib, sys
import mpmath as mp
HERE = pathlib.Path(__file__).resolve().parent
ROOT = next(q for q in HERE.parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
P = ROOT / "frontier" / "B1691_the_exponents_at_the_two_fixed_points" / "verification"
sys.path.insert(0, str(P))
spec = importlib.util.spec_from_file_location("te", P / "the_exponents.py"); te = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()): spec.loader.exec_module(te)
S, F, B, e4 = te.S, te.F, te.B, te.e4
fr = lambda p: None if p is None else [str(p[0]), str(p[1])]
vp = lambda u: (u[1] + u[2] * S.c(0, 1)) * S.c(F(1, 2)); vm = lambda u: (u[1] - u[2] * S.c(0, 1)) * S.c(F(1, 2))
out = {}
E4R = [e4 * c for c in B[0]]
out["unit_coefficients_x^-1"] = {"E4 R on v+": fr(vp(E4R).d.get(-1)), "D2R on v+": fr(vp(B[2]).d.get(-1)),
                                  "E4 R on v-": fr(vm(E4R).d.get(-1)), "D2R on v-": fr(vm(B[2]).d.get(-1)),
                                  "E4 R on e_i": fr(E4R[0].d.get(-1)), "D2R on e_i": fr(B[2][0].d.get(-1))}
a0 = [c * S.c(F(-1, 48)) + d for c, d in zip(E4R, B[2])]
out["a0_orders_on_(e_i,e_j,e_k)"] = [c.ord() for c in a0]
out["a0_holomorphic_at_the_cusp"] = all(c.ord() >= 0 for c in a0)
out["R_orders"] = [c.ord() for c in B[0]]; out["DR_orders"] = [c.ord() for c in B[1]]
out["a0_cusp_exponents"] = te.cusp_exps(a0)
out["a0_m2/m3_along_i_y"] = {str(y): float(te.at(a0, mp.mpc(0, y))[0]) for y in (1.5, 2, 2.5, 3, 4)}
pts = {"omega": mp.mpc(-0.5, mp.sqrt(3) / 2), "i": mp.mpc(0, 1),
       "B1483: -1/2 + sqrt3 i": mp.mpc(-0.5, mp.sqrt(3)), "B1483: 4 sqrt3 i": mp.mpc(0, 4 * mp.sqrt(3)),
       "W51: 1.551 i": mp.mpc(0, 1.551), "W51: 1/2 + 2.224 i": mp.mpc(0.5, 2.224), "the cusp shape 2 sqrt3 i": mp.mpc(0, 2 * mp.sqrt(3))}
out["candidate_taus_m2/m3_large_L"] = {k: {"DR": float(te.at(B[1], t)[0]), "a0": float(te.at(a0, t)[0])} for k, t in pts.items()}

# (4) the order-5 lines fixed by the tick up to sign (B591, B489; the seat's row 1209): LR on H1 in the record's convention
import numpy as np
from fractions import Fraction as Fr
X_, Y_ = 1, 2
def _inv(w): return [-g for g in reversed(w)]
def _red(w):
    o = []
    for g in w:
        if o and o[-1] == -g: o.pop()
        else: o.append(g)
    return o
def _apply(a, w):
    o = []
    for g in w: o += a[g] if g > 0 else _inv(a[-g])
    return _red(o)
def _comp(a, b): return {X_: _apply(a, b[X_]), Y_: _apply(a, b[Y_])}
TAU = {"L": {X_: [X_], Y_: [Y_, X_]}, "R": {X_: [X_, Y_], Y_: [Y_]}}     # B1434's architecture_census.py
phi = _comp(_comp({X_: [X_], Y_: [Y_]}, TAU["L"]), TAU["R"])
ex = lambda w: [sum(1 if g == X_ else -1 if g == -X_ else 0 for g in w), sum(1 if g == Y_ else -1 if g == -Y_ else 0 for g in w)]
Mlr = np.array([[ex(phi[X_])[0], ex(phi[Y_])[0]], [ex(phi[X_])[1], ex(phi[Y_])[1]]])
out["LR_on_H1"] = Mlr.tolist()
out["det_LR_minus_I"] = int(round(np.linalg.det(Mlr - np.eye(2)))); out["det_LR_plus_I"] = int(round(np.linalg.det(Mlr + np.eye(2))))
out["lines_fixed_by_LR"] = [[i, j] for i in range(5) for j in range(5) if all(v % 5 == 0 for v in (Mlr - np.eye(2, dtype=int)) @ [i, j])]
out["order5_lines_fixed_up_to_sign"] = [[str(Fr(i, 5)), str(Fr(j, 5))] for i in range(5) for j in range(5)
                                        if (i, j) != (0, 0) and all(v % 5 == 0 for v in (Mlr + np.eye(2, dtype=int)) @ [i, j])]
# (5) the silver word state's cusp shape (B485): 2i (SnapPy's frame prints its reciprocal)
import snappy
out["cusp_shapes_snappy"] = {w: [complex(snappy.Manifold("b++" + w).cusp_info(0)["shape"]).real, complex(snappy.Manifold("b++" + w).cusp_info(0)["shape"]).imag] for w in ("LR", "LLRR")}

if __name__ == "__main__":
    json.dump(out, open(HERE / "the_scan.json", "w"), indent=1); print(json.dumps(out, indent=1)[:2500])
