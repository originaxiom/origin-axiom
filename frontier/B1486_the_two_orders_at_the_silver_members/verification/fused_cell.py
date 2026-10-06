#!/usr/bin/env python3
"""B1486 -- THE TWO ORDERS AT THE SILVER MEMBERS: do they fuse, and what does the fusion count?

For each member nu of m135 and m136 (B1485's objects): S = V (+) 1 with V = nu (x) four; c1 the interior class of
H^1(V) (the order W1 = [[V, c1], [0, 1]]), c2 the interior class of H^1(V*) (the order W2 = [[1, 0], [c2^T, V]] -- the
dual order, read as the lower-left block).  The mixed first-order direction u = N1 + N2 is tested for its second-order
obstruction by expanding both relators to order eps^2; if unobstructed, Gauss-Newton from the second-order seed at a
finite eps to an exact flat module; then its commutant, its invariant line and hyperplane, its traces against S's, and
its class index (I(X), I(Lambda^2 X)) by the numerical twin of main's instrument.  Controlled first on B1466's counted
point of m004 (control_c3b.py, reproducing C3b).  Usage: fused_cell.py STATE  (writes fused_<name>.json)."""
import sys, os, json, pathlib, itertools
HERE = pathlib.Path(__file__).resolve().parent
ROOT = next((p for p in [HERE, *HERE.parents] if (p / "frontier" / "B1485_the_silver_members_by_a_second_route").is_dir()), pathlib.Path(os.environ.get("OA_ROOT", ".")))
sys.path.insert(0, str(HERE)); sys.path.insert(0, str(ROOT / "frontier" / "B1485_the_silver_members_by_a_second_route" / "verification"))
import second_route as SR, fused as F
import c2_reducible_index as CI
from mpmath import mp, mpf, mpc, matrix, eye, zeros, inverse, nstr, norm
mp.dps = 50; F.mp.mp.dps = 50
EPS = (mpf("0.1"), mpf("0.02"), mpf("0.005"))     # 0.005 added after the sealed run: at eps = 0.1 the seed on m136 did not converge in 40 steps


def cxmat(P): return matrix([[SR.cx(x) for x in r] for r in P])
def cxvec(v): return [SR.cx(x) for x in v]


def ext2_num(M):
    n = M.rows; pairs = list(itertools.combinations(range(n), 2)); E = matrix(len(pairs), len(pairs))
    for a, (i, j) in enumerate(pairs):
        for b, (k, l) in enumerate(pairs): E[a, b] = M[i, k] * M[j, l] - M[i, l] * M[j, k]
    return E


def run_member(Sd, nu):
    gens, rels, cusp = Sd["gens"], Sd["rels"], tuple(Sd["cusp"]); n = 4
    V = SR.frame(Sd, nu); Vd = CI.dual(SR.K, V)
    int1, _ = SR.classes(Sd, V); int2, _ = SR.classes(Sd, Vd)
    assert len(int1) == 1 and len(int2) == 1, (len(int1), len(int2))
    z1, z2 = cxvec(int1[0]), cxvec(int2[0])
    S = {}; N1 = {}; N2 = {}
    for k, g in enumerate(gens):
        M = zeros(5, 5); A = cxmat(V[g])
        for i in range(4):
            for j in range(4): M[i, j] = A[i, j]
        M[4, 4] = 1; S[g] = M
        P = zeros(5, 5); Q = zeros(5, 5)
        # the lower-left block is a ROW cocycle d with d(gh) = d(g) V(h) + d(h); from the column cocycle z2 of V* it is
        # d = -(V^T z2)^T  (W2 = [[V, 0], [d, 1]] is the dual of [[V*, z2], [0, 1]]).  CORRECTED AFTER THE SEALED RUN: the sealed
        # code used d = z2^T, which is not a cocycle; the first-order residual check in `obstruction` caught it (140, not 0).
        d = (A.T * matrix(z2[k * n:(k + 1) * n]))
        for i in range(4): P[i, 4] = z1[k * n + i]; Q[4, i] = -d[i]
        N1[g] = P; N2[g] = Q
    # the Lorentz form J carries c1 to a multiple of c2 (V = V* through J): a check on the two interior classes
    J = matrix([[0, mpf(1) / 2, 0, 0], [mpf(1) / 2, 0, 0, 0], [0, 0, -1, 0], [0, 0, 0, -1]])
    Jz1 = [];
    for k in range(len(gens)): Jz1 += list(J * matrix(z1[k * n:(k + 1) * n]))
    ratio = [Jz1[i] / z2[i] for i in range(len(z2)) if abs(z2[i]) > mpf(10) ** -20]
    out = dict(nu=nu, J_c1_vs_c2_proportional=nstr(max(abs(r - ratio[0]) for r in ratio), 3) if ratio else None,
               cusp_words_commute=nstr(norm(F.word(cusp[0], S) * F.word(cusp[1], S) - F.word(cusp[1], S) * F.word(cusp[0], S)), 3))
    # obstructions: each order alone, then the mixed direction
    for label, Nn in (("c1 alone", {g: N1[g] for g in gens}), ("c2 alone", {g: N2[g] for g in gens}), ("c1 + c2", {g: N1[g] + N2[g] for g in gens})):
        u = {g: Nn[g] * inverse(S[g]) for g in gens}; ob = F.obstruction(gens, rels, S, u)
        out["obstruction " + label] = dict(first_order_residual=nstr(ob["first_order_residual"], 3), norm_Q=nstr(ob["norm_Q"], 6), rank_L=ob["rank_L"],
                                           residual=nstr(ob["residual"], 3), unobstructed=bool(ob["residual"] < mpf(10) ** -30 * max(1, ob["norm_Q"])))
        if label == "c1 + c2": ob_mixed, u_mixed = ob, u
    print(json.dumps({k: v for k, v in out.items() if k.startswith("obstruction")}), flush=True)
    out["fusions"] = []
    if out["obstruction c1 + c2"]["unobstructed"]:
        for eps in EPS:
            X = {g: (eye(5) + eps * u_mixed[g] + eps ** 2 * ob_mixed["w"][g]) * S[g] for g in gens}
            X, hist = F.gauss_newton(gens, rels, X)
            if not hist[-1] < mpf(10) ** -40:        # a recorded outcome, not an abort (after the sealed run the guard in F.index aborted here)
                rec = dict(eps=nstr(eps, 3), newton_residuals=[nstr(h, 3) for h in hist], converged=False)
                out["fusions"].append(rec); print(json.dumps(dict(nu=nu, **rec)), flush=True); continue
            cd, gap = F.commutant_dim(gens, X); inv = F.invariants(gens, X)
            idx = F.index(gens, rels, cusp, X); L2 = {g: ext2_num(X[g]) for g in gens}; idx2 = F.index(gens, rels, cusp, L2)
            rec = dict(eps=nstr(eps, 3), newton_residuals=[nstr(h, 3) for h in hist], converged=True,
                       distance_from_S=nstr(max(norm(X[g] - S[g]) for g in gens), 6), commutant_dim=cd, commutant_gap=nstr(gap, 4) if gap else None,
                       invariant_line=inv[0], dual_invariant_line=inv[1],
                       traces=dict((w, nstr(sum(F.word(w, X)[i, i] for i in range(5)), 12)) for w in ("a", "b", "t", "ab", "abt")),
                       traces_S=dict((w, nstr(sum(F.word(w, S)[i, i] for i in range(5)), 12)) for w in ("a", "b", "t", "ab", "abt")),
                       I_X=idx["I"], X=idx["E"], Xdual=idx["Edual"], I_L2X=idx2["I"], L2X=idx2["E"], L2Xdual=idx2["Edual"])
            out["fusions"].append(rec); print(json.dumps(dict(nu=nu, **{k: v for k, v in rec.items() if k not in ("traces", "traces_S")})), flush=True)
    # the split module and the two orders, for reference in the same code path
    for label, M in (("split", S), ("W1", {g: S[g] + N1[g] for g in gens}), ("W2", {g: S[g] + N2[g] for g in gens})):
        idx = F.index(gens, rels, cusp, M); idx2 = F.index(gens, rels, cusp, {g: ext2_num(M[g]) for g in gens})
        out["reference " + label] = dict(I=idx["I"], I_L2=idx2["I"], commutant_dim=F.commutant_dim(gens, M)[0], invariants=list(F.invariants(gens, M)))
    print(json.dumps({k: v for k, v in out.items() if k.startswith("reference")}), flush=True)
    return out


if __name__ == "__main__":
    state = sys.argv[1]; Sd = SR.load(ROOT / "frontier" / "B1485_the_silver_members_by_a_second_route" / "verification" / "members_for_main.json", state)
    res = [run_member(Sd, nu) for nu in Sd["members"]]
    json.dump(res, open(HERE / f"fused_{Sd['name']}.json", "w"), indent=1, default=str)
