"""B1513 post-run checks (written and run after higgs_census_run.txt; not predictions, not sealed). Record: post_run_checks_run.txt.

The sealed run found Y_k = 0 exactly for every member of both populations (P4 NO). A zero needs a positive control, because the
wedge-form triple product had produced no non-zero value before. Lemma 6's identity gives one: for any lift a of c* and the own class
h with q(h) = lam_h c,
    Y(h, a, e f0) = Y_V(q h, pi a, e) = -lam_h <c u e u c*>,
so at B1510's +-i points (no Jordan block) it must equal -lam_h kappa_l_hat exactly, with B1509's cocycles.

(a) The positive control at all six of B1510's points (level one, exact over B1509's field):
    - Y(h, a, e f0; wedge form) = -lam_h kappa_l_hat for the own 5'_H class h and a lift a of c*;
    - the mu-type pairing <h u e u hbar> = lam_h kappa_l_hat, with hbar the own 5bar'_H (c*'s image) and the form s <eta, omega>.
    Both must vanish exactly at mu = -1 and be non-zero at +-i.
(b) The whole 10' sector, at both sealed populations: the symmetric form B(a, a') = Y(h, a, a') on H^1(W*) (both basis classes).
    It is zero iff the own 5'_H decouples from every 10' end condition, interior or not.
(c) The mu-type pairing <h u e u hbar> at both populations (Lemma 6's cross term: zero at Jordan points).
(d) The boundary class of the 10' sector's line component. For a lift a of c*, a restricted to the cusp is x_t (e_t f0) + x_l (e_l f0)
    modulo coboundaries (V*|_P is acyclic). By Stokes' theorem applied to the line component beta (d beta = <c, c*>), x_l is
    <c u e u c*>: kappa_l_hat at B1510's points, and 0 at Jordan points. That is why an interior 10' exists exactly at Jordan points.
    Checked at all six of B1510's points and at both populations. Also, at the +-i points: Y(h, a + alpha e f0, a + alpha e f0) is
    affine in alpha with slope -2 lam_h kappa (Lemma 6), so it vanishes on exactly one (non-interior) lift there, while at Jordan
    points it vanishes on every lift.
(e) The Higgs bulk is acyclic on every cyclic cover (a theorem from Part A's exact P_L). With w = q + 1/q and u = s + 1/s,
    s^-3 P_L(q, s) = f(u) - (w^2 - w), f(u) = u^3 - 12u^2 + 45u - 48. f is increasing on [-2, 2] (f' = 3(u - 3)(u - 5)) with f(2) = 2.
    For real q > 0, w^2 - w >= 2 with equality only at q = 1. So P_L(q, mu) != 0 for every |mu| = 1 unless q = mu = 1. And
    H^0(F; Lambda^2 rho_q) = 0 for every q > 0: the gcd of twelve 6 x 6 minors of the fibre coboundary matrix has no positive root.
    By Wang and Shapiro, H*(M_n; Lambda^2 rho_q) = 0 for every n and every q > 0, q != 1."""
import json
import sys
from pathlib import Path

import sympy as sp
from sympy.polys.matrices import DomainMatrix

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import controls as K  # noqa: E402
import higgs_census as HC  # noqa: E402
import higgs_lib as H  # noqa: E402

T = H.T


def coefficient_on(mod, coc, target):
    """lam with coc = lam * target + coboundary (exact), or None"""
    B = H.coboundary_matrix(mod)
    A = target.column().hstack(B)
    x = H.solve(A, coc.column())
    return None if x is None else x[0, 0].element


def form_pairing():
    """Lambda^2 W (x) C (x) Lambda^2 W* -> C:  (omega, s, eta) -> s <eta, omega> (dual wedge bases)"""
    def F(om, s1, eta):
        o, et = om.to_list(), eta.to_list()
        tot = o[0][0] - o[0][0]
        for i in range(len(o)):
            tot += et[i][0] * o[i][0]
        return tot * s1.to_list()[0][0]
    return F


def own_data(G, V, Vd, c, cs, dom):
    W = V.extension(c.column())
    Wd, L2W = W.dual(), W.wedge2()
    L2Wd = Wd.wedge2()
    hb, h1 = H.h1_basis(L2W)
    out = {"h1(L2 W)": h1}
    lams = [coefficient_on(V, H.Cocycle(V, H.quotient_to_V(L2W, h, 5)), c) for h in hb]
    own = [(h, l) for h, l in zip(hb, lams) if l is not None and l != dom.zero]
    h, lam_h = own[0]
    zb, h1d = H.h1_basis(Wd)
    out["h1(W*)"] = h1d
    zero4 = DomainMatrix.zeros((4, 1), dom)
    pis = []
    for z in zb:
        piz = H.Cocycle(Vd, {g: z.v[g][0:4, :] for g in G.gens})
        assert piz.is_cocycle()
        pis.append(coefficient_on(Vd, piz, cs))
    k = next(i for i, l in enumerate(pis) if l is not None and l != dom.zero)
    a = zb[k].scaled(dom.one / pis[k])                     # a lift of c* (pi a = c* mod coboundaries)
    f0 = DomainMatrix([[dom.zero]] * 4 + [[dom.one]], (5, 1), dom)
    zero5 = DomainMatrix.zeros((5, 1), dom)
    ef0 = H.Cocycle(Wd, {"x": zero5, "y": zero5, "t": f0})
    hbar = H.include_Vstar(L2Wd, cs, 5)
    del zero4
    return {"W": W, "Wd": Wd, "L2W": L2W, "L2Wd": L2Wd, "h": h, "lam_h": lam_h, "a": a, "ef0": ef0, "hbar": hbar, "basis_Wd": zb,
            "info": out}


def check_a():
    rows = []
    for label, qq, mu, ml, kap in K.banked_kappas():
        G, V, Vd, c, cs, e = K.b1510_setup(qq, mu)
        C, z, _ = G.fundamental()
        dom = K.EI.K
        d = own_data(G, V, Vd, c, cs, dom)
        Ywe = H.triple(G, C, z, d["h"], d["a"], d["ef0"], H.form_wedge(5))
        Ymu = H.triple(G, C, z, d["h"], e, d["hbar"], form_pairing())
        lam = d["lam_h"]
        rows.append({"point": f"{label}, mu = {ml}", **d["info"], "lam_h": str(dom.to_sympy(lam)),
                     "Y(h, a, e f0)": str(dom.to_sympy(Ywe)), "-lam_h kappa": str(dom.to_sympy(-lam * kap)),
                     "Y(h, a, e f0) = -lam_h kappa": Ywe == -lam * kap,
                     "<h u e u hbar>": str(dom.to_sympy(Ymu)), "<h u e u hbar> = lam_h kappa": Ymu == lam * kap,
                     "nonzero": Ywe != dom.zero})
    return {"rows": rows, "all agree": all(r["Y(h, a, e f0) = -lam_h kappa"] and r["<h u e u hbar> = lam_h kappa"] for r in rows),
            "non-zero exactly at +-i": all(r["nonzero"] == (not r["point"].endswith("-1")) for r in rows)}


def check_b_c():
    out = {}
    for name, pop in HC.POPULATIONS.items():
        field = T.Field("ext", g=pop["g"], gaussian=False)
        dom = field.dom
        G = H.FibredGroup(pop["level"])
        C, z, _ = G.fundamental()
        rho = H.rho_mats(G, field)
        rows = {}
        for ab, lam in pop["members"]:
            V = H.Module(G, H.member_mats(G, field, ab, lam, rho))
            Vd = V.dual()
            c, cs = H.h1_basis(V)[0][0], H.h1_basis(Vd)[0][0]
            d = own_data(G, V, Vd, c, cs, dom)
            zb = d["basis_Wd"]
            Bm = [[str(dom.to_sympy(H.triple(G, C, z, d["h"], zi, zj, H.form_wedge(5)))) for zj in zb] for zi in zb]
            e = H.fibration_class(G, dom)
            mu_term = H.triple(G, C, z, d["h"], e, d["hbar"], form_pairing())
            rows[str(ab)] = {"B(a, a') on the basis of H^1(W*)": Bm, "B identically zero": all(x == "0" for r in Bm for x in r),
                             "<h u e u hbar>": str(dom.to_sympy(mu_term))}
        out[name] = rows
    return out


def boundary_class(Wd, a, dom):
    I5 = DomainMatrix.eye(5, dom)
    f0 = DomainMatrix([[dom.zero]] * 4 + [[dom.one]], (5, 1), dom)
    z5 = DomainMatrix.zeros((5, 1), dom)
    A = f0.vstack(z5).hstack(z5.vstack(f0), (Wd.rho("t") - I5).vstack(Wd.rho(H.ELL) - I5))
    sol = H.solve(A, a("t").vstack(a(H.ELL)))
    return sol[0, 0].element, sol[1, 0].element


def check_d():
    rows = []
    for label, qq, mu, ml, kap in K.banked_kappas():
        G, V, Vd, c, cs, e = K.b1510_setup(qq, mu)
        C, z, _ = G.fundamental()
        dom = K.EI.K
        d = own_data(G, V, Vd, c, cs, dom)
        xt, xl = boundary_class(d["Wd"], d["a"], dom)
        ys = []
        for alpha in (0, 1, 2):
            aa = H.Cocycle(d["Wd"], {g: d["a"].v[g] + d["ef0"].v[g] * dom.convert(alpha) for g in G.gens})
            ys.append(H.triple(G, C, z, d["h"], aa, aa, H.form_wedge(5)))
        rows.append({"point": f"{label}, mu = {ml}", "x_t": str(dom.to_sympy(xt)), "x_l": str(dom.to_sympy(xl)),
                     "x_l = kappa_l_hat": xl == kap,
                     "Y at alpha = 0, 1, 2": [str(dom.to_sympy(y)) for y in ys],
                     "affine with slope -2 lam_h kappa": ys[1] - ys[0] == -2 * d["lam_h"] * kap and ys[2] - ys[1] == ys[1] - ys[0],
                     "Y zero for every lift": all(y == dom.zero for y in ys)})
    pops = {}
    for name, pop in HC.POPULATIONS.items():
        field = T.Field("ext", g=pop["g"], gaussian=False)
        dom = field.dom
        G = H.FibredGroup(pop["level"])
        rho = H.rho_mats(G, field)
        for ab, lam in pop["members"]:
            V = H.Module(G, H.member_mats(G, field, ab, lam, rho))
            Vd = V.dual()
            c, cs = H.h1_basis(V)[0][0], H.h1_basis(Vd)[0][0]
            d = own_data(G, V, Vd, c, cs, dom)
            xt, xl = boundary_class(d["Wd"], d["a"], dom)
            ints = H.interior_classes(d["Wd"])
            pops[f"{name} {ab}"] = {"x_l of a lift of c*": str(dom.to_sympy(xl)), "x_l zero": xl == dom.zero,
                                    "interior classes": len(ints)}
    return {"B1510 points": rows, "populations": pops,
            "x_l = kappa_l_hat at all six points": all(r["x_l = kappa_l_hat"] for r in rows),
            "affine in the lift at all six points": all(r["affine with slope -2 lam_h kappa"] for r in rows),
            "Y zero on every lift exactly at mu = -1": all(r["Y zero for every lift"] == r["point"].endswith("-1") for r in rows)}


def check_e():
    import itertools
    q, s, u = H.q, H.s, sp.Symbol("u")
    rec = json.loads((HERE / "higgs_census_run.txt").read_text(encoding="utf-8"))
    P = sp.expand(sp.sympify(rec["A"]["P_L(q,s) factored"], locals={"q": q, "s": s}))
    f = u ** 3 - 12 * u ** 2 + 45 * u - 48
    w = q + 1 / q
    reduction = sp.simplify(sp.expand(P / s ** 3) - sp.expand((f - (w ** 2 - w)).subs(u, s + 1 / s))) == 0
    m, n = T.ballas(q)
    E = {"m": H.wedge2_sym(m).applyfunc(sp.cancel), "n": H.wedge2_sym(n).applyfunc(sp.cancel)}
    _, B = H.fibre_monodromy(E)
    den = sp.lcm([sp.fraction(sp.together(x))[1] for x in B])
    Bp = (B * den).applyfunc(sp.expand)
    g, used = None, 0
    for comb in itertools.combinations(range(12), 6):
        d = sp.factor(Bp.extract(list(comb), list(range(6))).det())
        if d != 0:
            g = d if g is None else sp.gcd(g, d)
            used += 1
            if used >= 12:
                break
    pos_roots = [r for r in sp.real_roots(sp.Poly(g, q)) if r > 0]
    return {"reduction s^-3 P_L = f(u) - (w^2 - w)": reduction, "f'(u)": str(sp.factor(sp.diff(f, u))), "f(2)": int(f.subs(u, 2)),
            "f increasing on [-2, 2]": all(sp.diff(f, u).subs(u, x) > 0 for x in (-2, -1, 0, 1, 2)) and
            sp.solve(sp.diff(f, u), u) == [3, 5],
            "gcd of 6x6 minors of the fibre coboundary (times its denominator)": str(sp.factor(g)), "minors used": used,
            "denominator": str(sp.factor(den)), "positive roots of the gcd": [str(r) for r in pos_roots],
            "H^0(F) = 0 for every q > 0": not pos_roots,
            "theorem: H*(M_n; L2 rho_q) = 0 for all n, all q > 0, q != 1": reduction and not pos_roots}


def main():
    return {"a_positive_control_at_B1510_points": check_a(), "b_c_the_whole_10prime_sector_and_the_mu_pairing": check_b_c(),
            "d_the_boundary_class_and_the_lift_dependence": check_d(), "e_the_higgs_bulk_on_every_cyclic_cover": check_e()}


if __name__ == "__main__":
    res = main()
    txt = json.dumps(res, indent=1, sort_keys=True, default=str)
    print(txt[:7000])
    if "--record" in sys.argv:
        (HERE / "post_run_checks_run.txt").write_text(txt + "\n", encoding="utf-8")
