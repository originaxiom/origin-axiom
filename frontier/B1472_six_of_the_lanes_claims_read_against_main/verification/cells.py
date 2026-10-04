#!/usr/bin/env python3
"""B1472 cells: (A) the Chern-Simons sign law under orientation reversal as SnapPy computes it, closed and
cusped samples; (B) L194 at 200 orientation double covers (xB020's slice; main's B1235 had 40); (C) the Bianchi covolumes
for B302's index (PSL vs PGL) by Humbert against Vol(4_1)/12 and /24."""
import json, sys, warnings, pathlib; warnings.filterwarnings("ignore")
import snappy
from mpmath import mp, mpf, zeta, pi, sqrt, nstr, nsum, inf
mp.dps = 30
HERE = pathlib.Path(__file__).resolve().parent
out = {}

# ---- (A) cs(-M) = -cs(M) in SnapPy's convention
def fold(x, mod):
    x = float(x) % mod
    return min(x, mod - x)
def closed_cs(M):
    """B1239's route: the kernel needs the cusped parent's value first, then the filling"""
    P = M.copy(); fill = [tuple(c["filling"]) for c in P.cusp_info()]
    P.dehn_fill([(0, 0)] * P.num_cusps()); P.chern_simons(); P.dehn_fill(fill)
    return float(P.chern_simons())
A = dict(closed=[], cusped=[], max_closed=0.0, max_cusped=0.0)
for M in list(snappy.OrientableClosedCensus[:150]):
    try:
        c = closed_cs(M); N = M.copy(); N.reverse_orientation(); cr = closed_cs(N)
    except Exception as e:
        A.setdefault("closed_errors", []).append((M.name(), repr(e)[:80])); continue
    d = fold(c + cr, 1.0); A["closed"].append((M.name(), float(c), float(cr), d)); A["max_closed"] = max(A["max_closed"], d)
for M in list(snappy.OrientableCuspedCensus[:150]):
    try:
        c = M.chern_simons(); N = M.copy(); N.reverse_orientation(); cr = N.chern_simons()
    except Exception as e:
        continue
    d = fold(c + cr, 0.5); A["cusped"].append((M.name(), float(c), float(cr), d)); A["max_cusped"] = max(A["max_cusped"], d)
A["n_closed"], A["n_cusped"] = len(A["closed"]), len(A["cusped"])
print("(A) cs(M) + cs(-M) folded: closed n=%d max %.2e (mod 1); cusped n=%d max %.2e (mod 1/2)" % (A["n_closed"], A["max_closed"], A["n_cusped"], A["max_cusped"]))
out["A_sign_law"] = {k: v for k, v in A.items() if k not in ("closed", "cusped")}
out["A_sign_law"]["sample_closed"] = A["closed"][:5]; out["A_sign_law"]["sample_cusped"] = A["cusped"][:5]

# ---- (B) L194: orientation double covers of non-orientable cusped census manifolds -- CS class
B = dict(zero=0, quarter=0, other=0, errors=0, rows=[])
count = 0
for N in snappy.NonorientableCuspedCensus:
    if count >= 200: break
    try:
        M = N.orientation_cover(); c = float(M.chern_simons()); count += 1
    except Exception as e:
        B["errors"] += 1; continue
    f0 = fold(c, 0.5); f4 = fold(c - 0.25, 0.5)
    cls = "zero" if f0 < 1e-9 else ("quarter" if f4 < 1e-9 else "other")
    B[cls] += 1; B["rows"].append((N.name(), M.num_cusps(), c, cls))
print("(B) L194 orientation double covers: tested %d -> zero %d quarter %d other %d errors %d" % (count, B["zero"], B["quarter"], B["other"], B["errors"]))
out["B_L194_200"] = {k: v for k, v in B.items() if k != "rows"}; out["B_L194_200"]["rows"] = B["rows"]

# ---- (C) Humbert: covol(PSL(2,O_d)) = |d_K|^{3/2} zeta_K(2) / (4 pi^2); K = Q(sqrt-3), d_K = -3, zeta_K = zeta * L(chi_-3)
L = (zeta(2, mpf(1) / 3) - zeta(2, mpf(2) / 3)) / 9          # L(chi_-3, 2) by Hurwitz zeta
zK = zeta(2) * L
vol_psl = mpf(3) ** mpf("1.5") * zK / (4 * pi ** 2)
vol_pgl = vol_psl / 2
v41 = mpf(str(snappy.Manifold("4_1").volume()))
C = dict(L_chi_minus3_2=nstr(L, 20), zeta_K_2=nstr(zK, 20), covol_PSL=nstr(vol_psl, 20), covol_PGL=nstr(vol_pgl, 20), vol_4_1=nstr(v41, 20),
         index_PSL=nstr(v41 / vol_psl, 15), index_PGL=nstr(v41 / vol_pgl, 15), gieseking_over_PGL=nstr(mpf(str(snappy.Manifold("m000").volume())) / vol_pgl, 15))
print("(C)", C)
out["C_bianchi_covolumes"] = C
json.dump(out, open(HERE / "b1472_cells.json", "w"), indent=1, default=str)
