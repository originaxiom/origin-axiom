#!/usr/bin/env python3
"""Independent zero-shared-code verification and exact SOS positivity extension of Q0034 (P-635 / FL-08)."""
import itertools
import sys
import sympy as sp


def build_q8_adjoint():
    one = sp.eye(2)
    qi = sp.Matrix([[sp.I, 0], [0, -sp.I]])
    qj = sp.Matrix([[0, 1], [-1, 0]])
    qk = qi * qj
    basis = (qi, qj, qk)

    def ad_mat(g):
        gi = g.inv()
        return sp.Matrix(
            3,
            3,
            lambda r, c: sp.simplify(sp.re(sp.expand((g * basis[c] * gi * basis[r].H).trace() / 2))),
        )

    return one, qi, qj, qk, basis, {"a": ad_mat(qi), "b": ad_mat(qj)}


def word_rep(word, rep):
    dim = rep["a"].shape[0]
    out = sp.eye(dim)
    for gen, exp in word:
        out = out * (rep[gen] if exp == 1 else rep[gen].inv())
    return out


def fox_deriv(word, target_gen, rep):
    dim = rep[target_gen].shape[0]
    acc = sp.zeros(dim, dim)
    prefix = sp.eye(dim)
    for gen, exp in word:
        if gen == target_gen:
            acc = acc + (prefix if exp == 1 else -prefix * rep[gen].inv())
        prefix = prefix * (rep[gen] if exp == 1 else rep[gen].inv())
    return acc


def group_cohomology(rels, rep, bdy_word=None):
    dim = rep["a"].shape[0]
    d0 = sp.Matrix.vstack(rep["a"] - sp.eye(dim), rep["b"] - sp.eye(dim))
    h0 = dim - d0.rank()
    b1 = d0.rank()
    if rels:
        jac = sp.Matrix.vstack(*[sp.Matrix.hstack(fox_deriv(w, "a", rep), fox_deriv(w, "b", rep)) for w in rels])
        z_basis = jac.nullspace()
    else:
        z_basis = [sp.eye(2 * dim)[:, k] for k in range(2 * dim)]
    z1 = len(z_basis)
    res = {"H0": h0, "H1": z1 - b1}
    if bdy_word is not None:
        ad_c = word_rep(bdy_word, rep)
        fox_c = sp.Matrix.hstack(fox_deriv(bdy_word, "a", rep), fox_deriv(bdy_word, "b", rep))
        z_mat = sp.Matrix.hstack(*z_basis) if z_basis else sp.zeros(2 * dim, 0)
        bdy_cob = ad_c - sp.eye(dim)
        restr_rank = sp.Matrix.hstack(fox_c * z_mat, bdy_cob).rank() - bdy_cob.rank()
        res["restr_rank"] = restr_rank
        res["H1_par"] = (z1 - restr_rank) - b1
    return res


def verify_family_and_sos(one, qi, qj, qk, basis, ad_q8):
    s1, s2, s3 = sp.symbols("s1 s2 s3", real=True)
    vars_s = (s1, s2, s3)
    at0 = {s1: 0, s2: 0, s3: 0}
    a_s = qi * (sp.cos(s1) * one + sp.sin(s1) * qi) * (sp.cos(s3) * one + sp.sin(s3) * qk)
    b_s = qj * (sp.cos(s2) * one + sp.sin(s2) * qj)
    x_s = sp.trigsimp(sp.expand(a_s.trace()))
    y_s = sp.trigsimp(sp.expand(b_s.trace()))
    z_s = sp.trigsimp(sp.expand((a_s * b_s).trace()))
    comm_s = a_s * b_s * a_s.adjugate() * b_s.adjugate()
    kap_s = sp.expand(comm_s.trace())
    fricke_exact_diff = sp.trigsimp(sp.expand(kap_s - (x_s**2 + y_s**2 + z_s**2 - x_s * y_s * z_s - 2)))
    sos_expr = 4 * sp.sin(s2) ** 2 + 4 * sp.cos(s2) ** 2 * (
        sp.sin(s1) ** 2 * sp.cos(s3) ** 2 + sp.cos(s1) ** 2 * sp.sin(s3) ** 2
    )
    sos_exact_diff = sp.trigsimp(sp.expand((kap_s + 2) - sos_expr))
    jac0 = sp.Matrix([[sp.diff(f, v).subs(at0) for v in vars_s] for f in (x_s, y_s, z_s)])
    grad0 = [sp.simplify(sp.diff(kap_s, v).subs(at0)) for v in vars_s]
    hess0 = sp.Matrix(3, 3, lambda i, j: sp.simplify(sp.diff(kap_s, vars_s[i], vars_s[j]).subs(at0)))

    def su2_coords(mat):
        return sp.Matrix([sp.simplify(sp.re(sp.expand((mat * b_el.H).trace() / 2))) for b_el in basis])

    tang_cols = []
    for v in vars_s:
        ua = su2_coords(sp.diff(a_s, v).subs(at0) * qi.inv())
        ub = su2_coords(sp.diff(b_s, v).subs(at0) * qj.inv())
        tang_cols.append(sp.Matrix.vstack(ua, ub))
    d0 = sp.Matrix.vstack(ad_q8["a"] - sp.eye(3), ad_q8["b"] - sp.eye(3))
    tang_rank = sp.Matrix.hstack(*tang_cols, d0).rank() - d0.rank()

    new_traces = (
        sp.expand((a_s * b_s).trace()),
        sp.expand((b_s * a_s * b_s).trace()),
        sp.expand((a_s * b_s * b_s * a_s * b_s).trace()),
    )
    jac1 = sp.Matrix([[sp.diff(f, v).subs(at0) for v in vars_s] for f in new_traces])
    dphi = sp.simplify(jac1 * jac0.inv())
    lam = sp.Symbol("lam")
    trace_cp = sp.factor(dphi.charpoly(lam).as_expr())
    trace_ker = 3 - (dphi - sp.eye(3)).rank()

    phi_map = {"a": [("a", 1), ("b", 1)], "b": [("b", 1), ("a", 1), ("b", 1)]}
    imgs = {g: word_rep(phi_map[g], ad_q8) for g in ("a", "b")}
    fox_kers = []
    for perm in itertools.permutations(range(3)):
        for signs in itertools.product((1, -1), repeat=3):
            p_mat = sp.zeros(3, 3)
            for r_idx, c_idx in enumerate(perm):
                p_mat[r_idx, c_idx] = signs[r_idx]
            if p_mat.det() == 1 and all(p_mat * imgs[g] * p_mat.inv() == ad_q8[g] for g in ("a", "b")):
                phi_z1 = sp.Matrix.vstack(
                    p_mat * sp.Matrix.hstack(fox_deriv(phi_map["a"], "a", ad_q8), fox_deriv(phi_map["a"], "b", ad_q8)),
                    p_mat * sp.Matrix.hstack(fox_deriv(phi_map["b"], "a", ad_q8), fox_deriv(phi_map["b"], "b", ad_q8)),
                )
                ns = sp.Matrix.hstack(phi_z1 - sp.eye(6), d0).nullspace()
                u_cols = sp.Matrix.hstack(*[vec[:6, :] for vec in ns]) if ns else sp.zeros(6, 0)
                fox_kers.append(sp.Matrix.hstack(u_cols, d0).rank() - d0.rank())

    return {
        "fricke_zero": fricke_exact_diff == 0,
        "sos_zero": sos_exact_diff == 0,
        "jac_rank": int(jac0.rank()),
        "tang_rank": int(tang_rank),
        "grad_zero": grad0 == [0, 0, 0],
        "hess_diag8": hess0 == 8 * sp.eye(3),
        "fox_kers": fox_kers,
        "trace_ker": int(trace_ker),
        "trace_cp": str(trace_cp),
    }


def main():
    one, qi, qj, qk, basis, ad_q8 = build_q8_adjoint()
    bdy = [("a", 1), ("b", 1), ("a", -1), ("b", -1)]
    closed_q8 = group_cohomology([bdy], ad_q8)
    punc_q8 = group_cohomology([], ad_q8, bdy_word=bdy)
    triv_rep = {"a": sp.eye(1), "b": sp.eye(1)}
    closed_u1 = group_cohomology([bdy], triv_rep)
    punc_u1 = group_cohomology([], triv_rep, bdy_word=bdy)
    fam = verify_family_and_sos(one, qi, qj, qk, basis, ad_q8)

    holds = (
        closed_q8["H1"] == 0
        and punc_q8["H1"] == 3
        and punc_q8["restr_rank"] == 3
        and punc_q8["H1_par"] == 0
        and closed_u1["H1"] == 2
        and punc_u1["H1"] == 2
        and punc_u1["restr_rank"] == 0
        and fam["fricke_zero"]
        and fam["sos_zero"]
        and fam["jac_rank"] == 3
        and fam["tang_rank"] == 3
        and fam["grad_zero"]
        and fam["hess_diag8"]
        and fam["fox_kers"] == [1, 1, 1, 1]
        and fam["trace_ker"] == 1
    )
    print("DECISIVE: q8_cohomology_closed_free_par_restr = [%d, %d, %d, %d]"
          % (closed_q8["H1"], punc_q8["H1"], punc_q8["H1_par"], punc_q8["restr_rank"]))
    print("DECISIVE: centre_lines_closed_free_restr = [%d, %d, %d]"
          % (closed_u1["H1"], punc_u1["H1"], punc_u1["restr_rank"]))
    print("DECISIVE: exact_symbolic_fricke_and_sos_identities = %s"
          % (fam["fricke_zero"] and fam["sos_zero"]))
    print("DECISIVE: m004_wang_kernel_fox_and_trace = [%s, %d]" % (fam["fox_kers"], fam["trace_ker"]))
    print("DECISIVE: q0034_all_claims_and_sos_extension_hold = %s" % holds)
    return 0 if holds else 1


if __name__ == "__main__":
    sys.exit(main())
