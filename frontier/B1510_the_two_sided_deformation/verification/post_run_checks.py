"""B1510, post-run (computed after two_sided_run.txt; no sealed reading rests on these, and none is changed by them).

(a) The chiral index at the precision edge.  The sealed run read the chiral branch's index at N = 8 and at N = 10 from ONE jet solved to
    order 10.  At N = 10 the reading has a1 = b1 = 0 with r1 = q1 = 1, which no genuine module can have (r1 <= a1), and its deciding
    pivot sits at valuation 10 = N.  Hypothesis: the jet's last orders still carry free choices that later orders would fix, so the
    order-10 coefficients of the cohomology minors are not yet those of any continuation.  Check: solve the chiral branch to N = 12
    and read the index at N = 8, 10 and 12 from that one jet.
(b) Which free class moves the line's longitude at mu = -1.  On the free-end branch lam_l = 1 through order 10, while lam_m moves at
    order 2.  Check: at the chiral solver's step three (the order-2 choice), the coefficient of each basis class in the order-4 longitude
    condition, and the same for the meridian at order 2; and whether the longitude row is proportional to the odd-obstruction rows on
    the adjoint classes and the base (rank one), which would make the free-end choice kill both at once, and whether the twist breaks
    the proportionality (rank two).
(c) The free-end branch at mu = -1 continued to N = 14: does lam_l stay 1?
(d) Is the free-end branch's adjoint direction special?  The tangent of Ballas' q-family written in the adjoint classes; the 2 x 2
    minors [longitude; odd obstruction] x [class; base] per adjoint class; the free-end branch rerun with the adjoint classes
    reordered."""
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import two_sided as T  # noqa: E402
import deform_lib as DL  # noqa: E402


def chiral_edge(N=12):
    rows = []
    for p in T.PRIMES:
        for S in T.modp_setups(p):
            if S.mu_label != "-1":
                continue
            F = S.F
            basis, _ = T.h1_basis(S)
            sol = T.Solver(S, N, basis, chiral=True, use_det=True)
            res = sol.run()
            row = {"point": S.label, "exists_to_order": res["exists_to_order"], "stopped": res["stopped"]}
            if res["exists_to_order"] == N:
                ver = sol.verify()
                row["verify"] = {k: ver[k] for k in ("relator_identity_to_order_N", "det_one_to_order_N", "line_stays_(1,1)")}
                row["index"] = {}
                for n in (8, 10, 12):
                    ix = T.index_row(F, sol._fam(n), n)
                    row["index"][n] = {k: ix[k] for k in ("I", "a0", "b0", "a1", "b1", "t0", "s0", "r1", "q1", "prec_left")}
                    row["index"][n]["last_pivot_V"] = ix["pivots_V"][-1] if ix["pivots_V"] else None
            rows.append(row)
    return rows


def longitude_columns():
    """at the chiral step three: the order-4 longitude condition's and the order-2 meridian condition's coefficient per basis class"""
    rows = []
    for p in T.PRIMES:
        for S in T.modp_setups(p):
            if S.mu_label != "-1":
                continue
            F = S.F
            basis, _ = T.h1_basis(S)
            sol = T.Solver(S, 4, basis, chiral=True, use_det=True)
            sol.U[2], _ = sol.particular(2)
            kinds = sol.constraint_kinds(3)
            base = sol.constraints(3)
            saved = sol.U[2]
            col, raw = {}, {}
            for name, z in basis:
                sol.U[2] = T.add_cochains(F, saved, z)
                diff = [F.sub(x, y) for x, y in zip(sol.constraints(3), base)]
                sol.U[2] = saved
                col[name] = {k: F.show(d) for k, d in zip(kinds, diff) if k in ("lam_m", "lam_l_next", "det")}
                raw[name] = diff
            # the longitude row against each odd-obstruction row, on the adjoint classes and the base: rank of the 2 x 4 matrix
            adj = [n for n, _ in basis if n.startswith("adj")]
            il = kinds.index("lam_l_next")
            prop = {}
            for kind in ("A", "A*"):
                io = kinds.index(kind)
                M = [[raw[n][il] for n in adj] + [base[il]], [raw[n][io] for n in adj] + [base[io]]]
                prop[kind] = DL.rank(F, M)
            Mt = [[raw[n][il] for n in adj] + [raw["twist_T"][il]], [raw[n][kinds.index("A")] for n in adj] + [raw["twist_T"][kinds.index("A")]]]
            rows.append({"point": S.label, "base": {k: F.show(b) for k, b in zip(kinds, base) if k in ("lam_m", "lam_l_next", "det")},
                         "columns": col,
                         "rank_[longitude; odd obstruction]_on_adjoint_and_base": prop,
                         "rank_[longitude; A obstruction]_on_adjoint_and_twist": DL.rank(F, Mt)})
    return rows


def free_end_longer(N=14):
    rows = []
    for p in T.PRIMES:
        for S in T.modp_setups(p):
            if S.mu_label != "-1":
                continue
            basis, _ = T.h1_basis(S)
            sol = T.Solver(S, N, basis, chiral=False, use_det=True)
            res = sol.run()
            row = {"point": S.label, "exists_to_order": res["exists_to_order"]}
            if res["exists_to_order"] == N:
                ver = sol.verify()
                row["lam_l_series"] = ver["lam_l_series"]
                row["lam_m_series"] = ver["lam_m_series"]
                row["relator_identity_to_order_N"] = ver["relator_identity_to_order_N"]
                row["twist_ever_chosen"] = any("twist_T" in e.get("free_choice", {}) for e in res["log"])
            rows.append(row)
    return rows


def q_tangent(S, p):
    """the tangent of Ballas' family at the point, as a block cocycle u(g) = (dA/dq)(g) A(g)^-1 (mod p)"""
    F = S.F
    qq, mu = S.q_modp, None
    F0 = T.IL.GF(p)
    inv2 = F0.inv(2)
    t = qq * inv2 % p
    # dm/dq and dn/dq of Ballas' matrices (t = q/2): m has t - 1, t, t + 1/2 in its last column; n has 2 + 1/t
    dm = [[0, 0, 0, inv2], [0, 0, 0, inv2], [0, 0, 0, inv2], [0, 0, 0, 0]]
    dn = [[0] * 4 for _ in range(4)]
    dn[1][0] = (-F0.inv(t * t % p) * inv2) % p
    A = S.A
    mus = A["m"][0][0] * F0.inv(1) % p            # A(m) = mu * m and m[0][0] = 1, so mu = A(m)[0][0]
    U = {}
    for g, d in (("m", dm), ("n", dn)):
        dA = [[mus * x % p for x in r] for r in d]
        u = DL.mmul(F, dA, DL.inverse(F, A[g]))
        M = DL.zeros(F, S.d, S.d)
        for i in range(S.a):
            for j in range(S.a):
                M[i][j] = u[i][j]
        U[g] = M
    return U


def adjoint_direction_diagnostics():
    """(d) is the free-end branch's adjoint direction special?  the q-tangent in the adjoint basis; the per-class minors
    M(adj_i) base_A - tau(adj_i) base_l at step three; the free-end branch with the adjoint classes reordered (lam_l to order 8)"""
    rows = []
    for p in T.PRIMES:
        for S in T.modp_setups(p):
            if S.mu_label != "-1":
                continue
            F, d = S.F, S.d
            basis, _ = T.h1_basis(S)
            adj = [(n, z) for n, z in basis if n.startswith("adj")]
            # the q-tangent: a cocycle?  its coordinates on the adjoint classes modulo B^1
            uq = q_tangent(S, p)
            J = T.fox_J(S)
            vq = T.vec_cochain(uq, d)
            is_cocycle = all(F.iszero(r[0]) for r in DL.mmul(F, J, [[x] for x in vq]))
            B = T.coboundaries(S)
            cols = [T.vec_cochain(z, d) for _, z in adj] + B
            coords = DL.solve(F, DL.mT(cols), vq)
            q_in_adj = None if coords is None else {n: F.show(c) for (n, _), c in zip(adj, coords[:len(adj)])}
            # minors at step three
            sol = T.Solver(S, 4, basis, chiral=True, use_det=True)
            sol.U[2], _ = sol.particular(2)
            kinds = sol.constraint_kinds(3)
            base = sol.constraints(3)
            saved = sol.U[2]
            il, ia = kinds.index("lam_l_next"), kinds.index("A")
            minors = {}
            for n, z in adj + [("q_tangent", uq)]:
                sol.U[2] = T.add_cochains(F, saved, z)
                diff = [F.sub(x, y) for x, y in zip(sol.constraints(3), base)]
                sol.U[2] = saved
                minors[n] = F.show(F.sub(F.mul(diff[il], base[ia]), F.mul(diff[ia], base[il])))
            # the free-end branch with the adjoint classes reordered
            reordered = []
            for order in ((1, 2, 0), (2, 0, 1)):
                b2 = [x for x in basis if not x[0].startswith("adj")] + [adj[i] for i in order]
                sol2 = T.Solver(S, 8, b2, chiral=False, use_det=True)
                res2 = sol2.run()
                ver2 = sol2.verify() if res2["exists_to_order"] == 8 else {}
                reordered.append({"adjoint_order": [adj[i][0] for i in order], "exists_to_order": res2["exists_to_order"],
                                  "lam_l_series": ver2.get("lam_l_series"), "lam_m_series": ver2.get("lam_m_series")})
            rows.append({"point": S.label, "q_tangent_is_cocycle": is_cocycle, "q_tangent_in_adjoint_basis": q_in_adj,
                         "minor_with_base_per_class": minors, "free_end_reordered": reordered})
    return rows


def main():
    return {"a_chiral_index_at_the_edge": chiral_edge(), "b_longitude_columns_at_step_three": longitude_columns(),
            "c_free_end_to_order_14": free_end_longer(),
            "d_adjoint_direction": adjoint_direction_diagnostics()}


if __name__ == "__main__":
    res = main()
    txt = json.dumps(res, indent=1, sort_keys=True, default=str)
    print(txt)
    if "--record" in sys.argv:
        (HERE / "post_run_checks_run.txt").write_text(txt + "\n", encoding="utf-8")
