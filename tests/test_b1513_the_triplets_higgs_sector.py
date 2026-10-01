"""B1513 lock -- THE TRIPLET'S HIGGS SECTOR (2026-10-01). Main's B1443 question asked of B1511's projective triplet and of B1509's
join in the harmonic frame; sealed at 5e995321 before any Lambda^2 cohomology at q != 1 and any coupling was computed; NEGATIVE.
Locked here:
- the seal's digest and markers;
- the controls' record (K1-K10, 87 checks), the sealed run's record (Parts 0, A-E) and the post-run record (a)-(e);
- live:
  - the relative triple product's chains on level 3;
  - B1510's banked kappa_l_hat at (7 - 4 sqrt 3, i) through the triple product;
  - B1509's join: one own 5'_H, the coupling zero, and the positive control at a +-i point non-zero and equal to -lam_h kappa;
  - one triplet member's coupling zero;
- the Higgs-bulk theorem's reduction identity, from the recorded P_L;
- the kill-graph entry, the verdict, the findings' load-bearing sentences, and hygiene.
The fibre polynomial's recomputation and the controls' rerun are marked slow. The sealed census (36 s) is not rerun by the lock."""
import hashlib
import importlib.util
import json
import sys
from pathlib import Path

import pytest
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1513_the_triplets_higgs_sector"
VER = ARC / "verification"
SEALED_SHA = "6f3ff4803a777a524997215101706e7f87344627824570e3f798d16d76bc1065"


def _load(name):
    if str(VER) not in sys.path:
        sys.path.insert(0, str(VER))
    spec = importlib.util.spec_from_file_location(name, VER / f"{name}.py")
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


def _record(name):
    return json.loads((VER / f"{name}_run.txt").read_text(encoding="utf-8"))


def _bools(d):
    if isinstance(d, dict):
        return [b for v in d.values() for b in _bools(v)]
    if isinstance(d, list):
        return [b for v in d for b in _bools(v)]
    return [d] if isinstance(d, bool) else []


def test_the_seal_is_unchanged():
    """PREREGISTRATION.md is byte-identical to the sealed text (SEAL_LEDGER) and carries the provenance markers"""
    assert hashlib.sha256((ARC / "PREREGISTRATION.md").read_bytes()).hexdigest() == SEALED_SHA
    txt = (ARC / "PREREGISTRATION.md").read_text(encoding="utf-8")
    assert "BANKED IDENTITY:" in txt and "PRIOR ART:" in txt
    assert SEALED_SHA in (ROOT / "docs" / "SEAL_LEDGER.md").read_text(encoding="utf-8")


def test_the_controls_record():
    """K1-K10 as recorded before the seal: every check holds"""
    c = _record("controls")
    b = _bools(c)
    assert len(b) == 87 and all(b)
    assert c["K3"]["h1(G_1; Lambda^2 rho_1)"] == c["K3"]["h1(G_3; Lambda^2 rho_1)"] == c["K3"]["h1(RS_3; Lambda^2 rho_1)"] == 2
    assert c["K4-K6"]["K4 global sign"] == 1
    assert [r["Y(c, e, c*)"] for r in c["K4-K6"]["K4"]][2] == "1024 + 1024*sqrt(3) - 4096*sqrt(3)*I"
    assert c["K1"]["levels"]["level_3"]["cells_in_C"] == 87
    assert all(r == {"h1(V)": 1, "h1(V*)": 1, "W (a0,a1,t0,r1)": [0, 1, 1, 1], "W* (b0,b1,s0,q1)": [1, 2, 1, 1], "I(W)": -1}
               for r in c["K2"]["B1511 banked triplet rows on G_3 (exact)"].values())


def test_the_sealed_record():
    """Parts 0 and A-E: the banked identity, P_L and its loci, the exact Higgs sector, the zero couplings, GF(p), the forms"""
    r = _record("higgs_census")
    assert r["0_banked_identity"]["passed"]
    A = r["A"]
    assert A["P_L(q, 0)"] == "1" and A["B^1 part"] == "(s - 1)**6" and A["degree in s"] == 6
    assert A["D7a: P_L(1/q, s) = P_L(q, s)"] and A["D7b: s^6 P_L(q, 1/s) = P_L(q, 0) P_L(q, s)"]
    for k in ("P1: generic h1 = 0 at every root of unity of order <= 6", "P2: triplet (orders 1, 3) on no locus",
              "P2': triplet on M_6 (orders 1, 2, 3, 6) on no locus", "P2: join (order 1) on no locus"):
        assert A[k] is True, k
    assert all(not row["identically zero"] and all(not f["positive_roots_not_1"] for f in row["factors"])
               for row in A["loci"].values())
    for pop, row in r["B_C_exact"].items():
        assert row[f"h1(G_{3 if 'triplet' in pop else 1}; L2 rho_q)"] == 0
        assert row["fibre: rank of the coboundary matrix (6 = no H^0(F))"] == 6
        for m in row["members"].values():
            assert m["h1(V), h1(V*)"] == [1, 1] and m["h1(L2 W)"] == 1 and m["h1(L2 W*)"] == 1
            assert m["L2 W (a0,a1,t0,t1,r1)"] == [0, 1, 0, 0, 0] and m["L2 W* (a0,a1,t0,t1,r1)"] == [0, 1, 0, 0, 0]
            assert m["rank of H1(L2 W) -> H1(V)"] == 1 and m["c* nonzero in H1(L2 W*)"] and m["interior classes of H1(W*)"] == 1
            assert m["couplings"] == [{"class": 0, "maps onto c": True, "Y": "0", "Y nonzero": False}]
            assert all(v is True for k, v in m["checks"].items() if k != "cross term <c u e u c*>")
            assert m["checks"]["cross term <c u e u c*>"] == "0"
    assert len(r["B_C_exact"]["I (the triplet, s961)"]["members"]) == 3
    D = r["D_modp"]
    assert len(D["I (the triplet, s961)"]) == 10 and len(D["II (B1509's join, m004)"]) == 6
    for rows in D.values():
        for x in rows:
            for m in x["members"].values():
                assert (m["h1(L2 W)"], m["h1(L2 W*)"], m["rank of H1(L2 W) -> H1(V)"]) == (1, 1, 1)
                assert [c["Y"] for c in m["couplings"]] == [0]
    E = r["E_invariant_forms"]
    assert E["P5: one form iff i = j = k"] is True
    assert sum(v for k, v in E.items() if k.startswith("(k=")) == 3


def test_the_post_run_record():
    """(a) the positive control; (b) the whole 10' sector zero; (c) the mu pairing zero; (d) x_l = kappa; (e) the theorem"""
    p = _record("post_run_checks")
    a = p["a_positive_control_at_B1510_points"]
    assert a["all agree"] and a["non-zero exactly at +-i"] and len(a["rows"]) == 6
    for pop in p["b_c_the_whole_10prime_sector_and_the_mu_pairing"].values():
        for m in pop.values():
            assert m["B identically zero"] and m["<h u e u hbar>"] == "0"
    d = p["d_the_boundary_class_and_the_lift_dependence"]
    assert d["x_l = kappa_l_hat at all six points"] and d["affine in the lift at all six points"]
    assert d["Y zero on every lift exactly at mu = -1"]
    assert all(v["x_l zero"] and v["interior classes"] == 1 for v in d["populations"].values())
    e = p["e_the_higgs_bulk_on_every_cyclic_cover"]
    assert e["theorem: H*(M_n; L2 rho_q) = 0 for all n, all q > 0, q != 1"]
    assert e["gcd of 6x6 minors of the fibre coboundary (times its denominator)"] == "1024*q**3*(q + 1)**4"


def test_the_chains_and_the_banked_identity_live():
    """dC = z on level 3; B1510's exact kappa_l_hat at (7 - 4 sqrt 3, i) through the triple product"""
    H = _load("higgs_lib")
    C, z, ok = H.FibredGroup(3).fundamental()
    assert all(ok.values()) and len(C) == 87
    K = _load("controls")
    label, qq, mu, ml, kap = K.banked_kappas()[2]
    G, V, Vd, c, cs, e = K.b1510_setup(qq, mu)
    C1, z1, _ = G.fundamental()
    assert H.triple(G, C1, z1, c, e, cs, H.form_line_pairing()) == kap
    assert K.EI.K.to_sympy(kap) == sp.sympify("1024 + 1024*sqrt(3) - 4096*sqrt(3)*I")


def test_the_join_and_the_positive_control_live():
    """B1509's join: one own 5'_H and Y = 0 exactly; at (7 - 4 sqrt 3, i): Y(h, a, e f0) = -lam_h kappa != 0"""
    H = _load("higgs_lib")
    T = H.T
    PR = _load("post_run_checks")
    q = H.q
    field = T.Field("ext", g=q ** 2 - 34 * q + 1, gaussian=False)
    G = H.FibredGroup(1)
    C, z, _ = G.fundamental()
    V = H.Module(G, H.member_mats(G, field, (0, 0), -1))
    Vd = V.dual()
    c, cs = H.h1_basis(V)[0][0], H.h1_basis(Vd)[0][0]
    d = PR.own_data(G, V, Vd, c, cs, field.dom)
    assert d["info"]["h1(L2 W)"] == 1
    a, ea = H.interior_classes(d["Wd"])[0]
    assert H.triple(G, C, z, d["h"], a, a, H.form_wedge(5)) == field.dom.zero
    K = _load("controls")
    label, qq, mu, ml, kap = K.banked_kappas()[2]
    G2, V2, Vd2, c2, cs2, e2 = K.b1510_setup(qq, mu)
    C2, z2, _ = G2.fundamental()
    d2 = PR.own_data(G2, V2, Vd2, c2, cs2, K.EI.K)
    Y = H.triple(G2, C2, z2, d2["h"], d2["a"], d2["ef0"], H.form_wedge(5))
    assert Y == -d2["lam_h"] * kap and Y != K.EI.K.zero


def test_a_triplet_member_live():
    """the triplet member (0, 2) on s961 over Q[q]/(q^6 - 34 q^3 + 1): h1(L2 W) = 1, the own class, Y = 0 exactly"""
    H = _load("higgs_lib")
    T = H.T
    field = T.Field("ext", g=H.G0, gaussian=False)
    G = H.FibredGroup(3)
    C, z, _ = G.fundamental()
    V = H.Module(G, H.member_mats(G, field, (0, 2), -1))
    c = H.h1_basis(V)[0][0]
    W = V.extension(c.column())
    hb, h1 = H.h1_basis(W.wedge2())
    assert h1 == 1
    assert H.rank_mod_coboundaries(V, [H.Cocycle(V, H.quotient_to_V(W.wedge2(), hb[0], 5))]) == 1
    a, _ = H.interior_classes(W.dual())[0]
    assert H.triple(G, C, z, hb[0], a, a, H.form_wedge(5)) == field.dom.zero


def test_the_higgs_bulk_reduction():
    """s^-3 P_L(q, s) = f(s + 1/s) - (w^2 - w) with f(u) = u^3 - 12u^2 + 45u - 48 increasing on [-2, 2] and f(2) = 2"""
    q, s, u = sp.symbols("q s u")
    P = sp.expand(sp.sympify(_record("higgs_census")["A"]["P_L(q,s) factored"], locals={"q": q, "s": s}))
    f = u ** 3 - 12 * u ** 2 + 45 * u - 48
    w = q + 1 / q
    assert sp.simplify(sp.expand(P / s ** 3) - sp.expand((f - (w ** 2 - w)).subs(u, s + 1 / s))) == 0
    assert sp.expand(sp.diff(f, u) - 3 * (u - 5) * (u - 3)) == 0 and f.subs(u, 2) == 2
    assert sp.factor(P.subs(q, 1)) == (s - 1) ** 2 * (s ** 2 - 5 * s + 1) ** 2


@pytest.mark.slow
def test_the_fibre_polynomial_reproduces():
    """P_L(q, s) recomputed from scratch equals the record"""
    H = _load("higgs_lib")
    q, s = H.q, H.s
    m, n = H.T.ballas(q)
    res = H.fibre_polynomial({"m": H.wedge2_sym(m).applyfunc(sp.cancel), "n": H.wedge2_sym(n).applyfunc(sp.cancel)})
    P = sp.expand(sp.sympify(_record("higgs_census")["A"]["P_L(q,s) factored"], locals={"q": q, "s": s}))
    assert sp.simplify(res["P"] - P) == 0


def test_the_kill_graph_entry():
    """the NEGATIVE is routed with content (B1207's A3)"""
    kg = json.loads((ROOT / "frontier" / "B738_pathfinder_compiler" / "kill_graph.json").read_text(encoding="utf-8"))
    rec = [r for r in kg if r.get("id") == "B1513"]
    assert len(rec) == 1
    r = rec[0]
    assert r["fact_computed"] is True and r["routed_from"] == "sm-branch-2026-10-01-banking"
    assert r["kill_form"].startswith("jordan-decoupling") and len(r["hatch"]) > 80
    assert "tests/test_b1513_the_triplets_higgs_sector.py" in r["note"]


def test_findings_verdict_and_hygiene():
    """the verdict is NEGATIVE, creates no law, keeps 0 of 19; the findings carry the answer, the predictions, the control, the
    theorem and the leads; the owner's private term is absent"""
    v = json.loads((ARC / "arc_verdict.json").read_text(encoding="utf-8"))
    assert v["id"] == "B1513" and v["verdict"] == "NEGATIVE" and v["creates_law"] is False
    assert "0 of 19" in v["claim_one_line"] and "I-26 stays UNEARNED" in v["claim_one_line"]
    f = (ARC / "FINDINGS.md").read_text(encoding="utf-8")
    for needle in ("**The answer (the sealed run).**", "**The coupling is zero.**",
                   "| P4 | each member couples to its own Higgs class: Y_k ≠ 0 for every member (~50% each) | **NO**",
                   "**T-HIGGS-BULK-ACYCLIC", "**x_ℓ = κ̂_ℓ exactly**", "**The zero is real, not an instrument artefact.**",
                   "post_run_checks_run.txt", SEALED_SHA, "I-26 stays UNEARNED", "0 of 19"):
        assert needle in f, needle
    term = bytes([98, 114, 97, 118, 101]).decode()  # the owner's private term, kept out of the source text
    for path in list(ARC.glob("*.md")) + list(VER.glob("*.py")):
        assert term not in path.read_text(encoding="utf-8").lower(), path
    assert term not in v["claim_one_line"].lower()
