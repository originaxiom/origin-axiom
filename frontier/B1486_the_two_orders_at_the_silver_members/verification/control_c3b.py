#!/usr/bin/env python3
"""B1486 CONTROL (before the seal): fused.py on B1466's counted point of m004's Ballas family (q0 = 17 + 12 sqrt2,
mu = -1), where the banked C3b result is: the mixed direction c1 + c2 is unobstructed (residual ~3e-57, rank d1 = 20,
dim H2 = 5), Gauss-Newton at eps = 0.1 reaches an exact flat module at distance ~0.13 from S, irreducible (commutant 1;
no invariant line, no invariant hyperplane), traces tr(m) ~ -2.9972, and its class index is 0 with h0 = h1 = 0 both sides.
The same numbers are to come out of the general code here (two generators, one relator) before it is pointed at
m135 (three generators, two relators)."""
import sys, json, pathlib, glob
HERE = pathlib.Path(__file__).resolve().parent
ROOT = next(p for p in HERE.parents if (p / "frontier").is_dir())
sys.path.insert(0, str(HERE))
V = ROOT / "frontier/B1466_the_two_orders_and_the_register_bit/verification"
sys.path.insert(0, str(V))
for d in ("B1453_*", "B1444_*", "B1445_*", "B1446_*"): sys.path.insert(0, glob.glob(str(ROOT / "frontier" / d / "verification"))[0])
sys.argv = [sys.argv[0]]
import two_orders as TO, join_own as jo
import fused as F
from mpmath import mp, mpf, mpc, matrix, eye, zeros, inverse, sqrt, nstr, norm
mp.dps = 60; F.mp.mp.dps = 60
gens = ["m", "n"]; rels = [jo.REL]
U0, U1 = "nM", "mnMM"; LAM = U0 + U1 + "mN" + "mmNM"; T = U0 + "mmNM" + "m"       # fibre boundary [u0, u1] and the meridian t = u0 u1^-1 m
cusp = (T, LAM)
q0 = 17 + 12 * sqrt(2); g = jo.ballas(q0, mpc(-1)); S = TO.blockS(g)
reps_up, _, _ = jo.cocycles(g); reps_dn, _, _ = TO.cocycles_down(g)
c1 = {"m": [reps_up[0][i] for i in range(4)], "n": [reps_up[0][4 + i] for i in range(4)]}
c2 = {"m": [reps_dn[0][i] for i in range(4)], "n": [reps_dn[0][4 + i] for i in range(4)]}
N = {}
for k in gens:
    M = zeros(5, 5)
    for i in range(4): M[i, 4] = c1[k][i]; M[4, i] = c2[k][i]
    N[k] = M
u = {k: N[k] * inverse(S[k]) for k in gens}            # rho_eps(g) = (1 + eps u_g + ...) S_g  with  u_g S_g = N_g = S_g phi_g
out = {}
# the cusp words commute on S (a check of the words)
cm = F.word(T, S) * F.word(LAM, S) - F.word(LAM, S) * F.word(T, S); out["cusp words commute on S"] = nstr(norm(cm), 3)
ob = F.obstruction(gens, rels, S, u)
out["obstruction"] = dict(first_order_residual=nstr(ob["first_order_residual"], 3), norm_Q=nstr(ob["norm_Q"], 6), rank_L=ob["rank_L"], residual=nstr(ob["residual"], 3))
print("obstruction:", out["obstruction"], flush=True)
eps = mpf("0.1")
X = {k: (eye(5) + eps * u[k] + eps ** 2 * ob["w"][k]) * S[k] for k in gens}
X, hist = F.gauss_newton(gens, rels, X)
out["newton_residuals"] = [nstr(h, 3) for h in hist]
out["distance_from_S"] = nstr(max(norm(X[k] - S[k]) for k in gens), 6)
cd, gap = F.commutant_dim(gens, X); out["commutant_dim"] = cd; out["commutant_gap"] = nstr(gap, 4) if gap else None
out["invariant_line, dual_invariant_line"] = list(F.invariants(gens, X))
out["traces"] = {w: nstr(F.word(w, X)[0, 0] + sum(F.word(w, X)[i, i] for i in range(1, 5)), 12) for w in ("m", "n", "mn", "mN")}
idx = F.index(gens, rels, cusp, X); out["I_mixed"] = idx
idxS = F.index(gens, rels, cusp, S); out["I_split"] = idxS
print(json.dumps(out, indent=1, default=str))
ok = (float(ob["residual"]) < 1e-40 and ob["rank_L"] == 20 and cd == 1 and out["invariant_line, dual_invariant_line"] == [0, 0]
      and idx["I"] == 0 and idx["E"]["a0"] == idx["E"]["a1"] == 0 and idx["Edual"]["a0"] == idx["Edual"]["a1"] == 0 and float(hist[-1]) < 1e-45)
print("CONTROL C3b REPRODUCED:", ok)
json.dump(dict(out, control_pass=ok), open(HERE / "control_c3b.json", "w"), indent=1, default=str)
