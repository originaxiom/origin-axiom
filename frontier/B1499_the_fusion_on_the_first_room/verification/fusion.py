#!/usr/bin/env python3
"""B1499 -- the non-split deformation on o10_150691 at nu = (i, 1, 1) (exponents (2, 0, 0) of zeta_8; B1497-B1498): B1486's fusion
of the two ORDERS -- the split S = V (+) 1 deformed along c (a class of V over the line, the generic member of B1498's pencil)
plus d (a class of the line over V, i.e. of H^1(V*)), the second-order obstruction, Gauss-Newton to an exact flat module, its
commutant (irreducible iff 1), and its count by B1492's stacked two-cusp index (I(X), I(Lambda^2 X)).  Writes fusion_o10_150691.json."""
import sys, json, pathlib, random
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[1] / "B1492_the_three_ended_companion_read" / "verification"))
sys.path.insert(0, str(HERE.parents[1] / "B1493_the_room_on_the_companions" / "verification"))
sys.path.insert(0, str(HERE.parents[1] / "B1486_the_two_orders_at_the_silver_members" / "verification"))
import multicusp as MC, room as RM, fused as F
from mpmath import mp, mpf, mpc, matrix, zeros, eye, inverse, norm, nstr
mp.dps = 40; random.seed(1499)
EPS = (mpf("0.1"), mpf("0.02"))        # 0.005 dropped after the sealed run: each seed takes ~35 minutes and the first two decide
S = RM.site("o10_150691"); gens, rels = S.gens, S.rels; n = 4
ks = [int(x) for x in (sys.argv[1] if len(sys.argv) > 1 else "2,0,0").split(",")]
nu = {g: RM.zeta(k) for g, k in zip(gens, ks)}; assert RM.is_character(S, nu)
V = S.four(nu); Vd = MC.dual(V)
int1, _ = S.classes(V); int2, _ = S.classes(Vd); print("interior classes of V, V*:", len(int1), len(int2), flush=True)
lam = mpc(random.uniform(-1, 1), random.uniform(-1, 1)); z1 = (int1[0][0] + lam * int1[1][0]) if len(int1) > 1 else int1[0][0]
z2 = int2[0][0] if len(int2) == 1 else int2[0][0] + mpc(random.uniform(-1, 1), random.uniform(-1, 1)) * int2[1][0]
S5, N1, N2 = {}, {}, {}
for k, g in enumerate(gens):
    M = zeros(5); A = V[g]
    for i in range(4):
        for j in range(4): M[i, j] = A[i, j]
    M[4, 4] = 1; S5[g] = M
    P = zeros(5); Q = zeros(5); d = (A.T * matrix([z2[k * n + i] for i in range(n)]))      # the row cocycle from the column cocycle of V*
    for i in range(4): P[i, 4] = z1[k * n + i]; Q[4, i] = -d[i]
    N1[g] = P; N2[g] = Q
out = dict(exponents=ks, lambda_pencil=nstr(lam, 6), classes=(len(int1), len(int2)))
def ext2(X): return {g: MC.ext2(X[g]) for g in gens}
def count(X):
    a = S.index(X); b = S.index(ext2(X)); return dict(I=a["I"], I_L2=b["I"], n=a["E"]["n"], n_dual=a["Edual"]["n"])
out["split S"] = count(S5); out["W1 (c alone)"] = count({g: S5[g] + N1[g] for g in gens}); out["W2 (d alone)"] = count({g: S5[g] + N2[g] for g in gens})
print("counts: split", out["split S"], "W1", out["W1 (c alone)"], "W2", out["W2 (d alone)"], flush=True)
for label, Nn in (("c alone", N1), ("d alone", N2), ("c + d", {g: N1[g] + N2[g] for g in gens})):
    u = {g: Nn[g] * inverse(S5[g]) for g in gens}; ob = F.obstruction(gens, rels, S5, u)
    out["obstruction " + label] = dict(first_order_residual=nstr(ob["first_order_residual"], 3), norm_Q=nstr(ob["norm_Q"], 6), rank_L=ob["rank_L"], residual=nstr(ob["residual"], 3), unobstructed=bool(ob["residual"] < mpf(10) ** -30 * max(1, ob["norm_Q"])))
    print(label, out["obstruction " + label], flush=True)
    if label == "c + d": ob_mixed, u_mixed = ob, u
out["fusions"] = []
if out["obstruction c + d"]["unobstructed"]:
    for eps in EPS:
        X = {g: (eye(5) + eps * u_mixed[g] + eps ** 2 * ob_mixed["w"][g]) * S5[g] for g in gens}
        X, hist = F.gauss_newton(gens, rels, X)
        # CORRECTED AFTER THE SEALED RUN (2026-10-07): at eps = 0.1 the iteration reached the arithmetic floor (residual ~1e-36 against
        # relator norms ~2e3, relative ~1e-39) and stayed there; the sealed threshold 1e-40 was tighter than 40-digit arithmetic allows
        # on these relators, so the count was skipped.  The module is read when the residual is below 1e-30 (relative 1e-33), and both
        # flags are recorded; the sealed output is kept in sealed_run/.
        rec = dict(eps=nstr(eps, 3), newton_residuals=[nstr(h, 3) for h in hist], converged=bool(hist[-1] < mpf(10) ** -40), at_floor=bool(hist[-1] < mpf(10) ** -30))
        if rec["at_floor"]:
            cd, gap = F.commutant_dim(gens, X); inv = F.invariants(gens, X)
            rec.update(distance_from_S=nstr(max(norm(X[g] - S5[g]) for g in gens), 6), commutant_dim=cd, invariant_line=inv[0], dual_invariant_line=inv[1], count=count(X),
                       relator_residual=nstr(max(norm(MC.word(r, X) - eye(5)) for r in rels), 3))
        out["fusions"].append(rec); print(json.dumps(rec), flush=True)
json.dump(out, open(HERE / f"fusion_o10_150691_{'_'.join(map(str, ks))}.json", "w"), indent=1, default=str)
print("FUSION", ks, [(r.get("commutant_dim"), r.get("count")) for r in out["fusions"]])
