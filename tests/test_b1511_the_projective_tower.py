"""B1511 lock -- THE PROJECTIVE TOWER (2026-10-01).  B1509's rank-five extension on the audit lane's harmonic family, carried to m004's
cyclic covers M1-M6 and twisted by their fibre torsion; sealed at 49baea7d before any twisted polynomial of a non-trivial character was
computed.  Locked here:
- the seal's digest and markers;
- the controls' record (C1-C10) and the banked identity, live;
- the projective triplet live: the order-2 orbit's polynomial is Q(q^3, s), its Jordan block at q^6 - 34 q^3 + 1, and one member's
  count over GF(p);
- case (b) on M4 live: one 3-torsion member's count +1 over GF(p) at q^2 - 7 q + 1;
- Part C2 on M2 and M4, live against the record;
- the decided items D1-D7 and the predictions P1-P8 from the record, and the post-run checks' record;
- the findings' load-bearing sentences.
The controls' full rerun is marked slow (about five minutes); the sealed census itself (21 minutes) is not rerun by the lock."""
import hashlib
import importlib.util
import json
import sys
from pathlib import Path

import pytest
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1511_the_projective_tower"
VER = ARC / "verification"
SEALED_SHA = "b5fbd35930882eacb5e1ba8d01203c2520dce8da1de81cd04142eeb1d575e8d7"


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


def _norm(x):
    return json.loads(json.dumps(x, sort_keys=True, default=str))


def test_the_seal_is_unchanged():
    """PREREGISTRATION.md is byte-identical to the sealed text (SEAL_LEDGER) and carries the provenance markers"""
    assert hashlib.sha256((ARC / "PREREGISTRATION.md").read_bytes()).hexdigest() == SEALED_SHA
    txt = (ARC / "PREREGISTRATION.md").read_text(encoding="utf-8")
    assert "BANKED IDENTITY:" in txt and "PRIOR ART:" in txt


def test_the_controls_record():
    """C1-C10 as recorded before the seal"""
    c = _record("controls")
    assert all(v for k, v in c["C1_C2"].items() if k != "C2_level3_charpoly")
    assert c["C3"]["orders_match_B1506"]
    assert c["C3"]["level_6"]["invariant_factors"] == [8, 40] and c["C3"]["level_3"]["invariant_factors"] == [4, 4]
    assert all(v in (True, None) for row in c["C4"].values() for v in row.values())
    assert all(r["exact_equals_B1509_at_both_roots"] and all(m["agrees_with_exact"] for m in r["mod_p"]) for r in c["C5"])
    assert all(r["as_expected"] for r in c["C6"])
    assert all(v for k, v in c["C7_C8"].items() if k != "C7_laurent_ranges_of_the_blocks")
    d = c["C9_dry_run"]
    assert d["A_theorem_D_reproduced"] and d["B_shapiro_holds"] and d["case_b_counter_on_M1"]["ok"]
    assert d["identically_exceptional_handler_on_the_trivial_orbit_ok"]
    assert d["gcd_common_factor_found"]["deg_rest"] == 2 and d["gcd_coprime_pair"]["deg_rest"] == 0
    cl = c["C10_case_b_classification"]
    assert cl["4"]["exact_pairs"] == [[[0, 5], "1"], [[0, 5], "-1"], [[5, 5], "1"], [[5, 5], "-1"]]
    assert [cl[n]["pairs_by_kind"].get("gcd") for n in ("2", "4", "5", "6")] == [8, 44, 96, 208]


def test_the_banked_identity_live():
    """B1509's Q at level one and its first index row, inside the census code"""
    TC = _load("tower_census")
    b = TC.banked_identity(lambda m: None)
    assert b["passed"] and b["B1509_row_q^2-34q+1_mu=-1"] == {"h1": 1, "I(W1)": -1, "I(W2)": 1, "I(L2 W1)": 0}


def test_the_projective_triplet_live():
    """the order-2 orbit of T3 on s961: P = Q(q^3, s) for every member; at q^6 - 34 q^3 + 1 the kernel dimensions of (S + 1)^j on H^1
    are 1, 2, 2, 2; one member counts -1 (W1) and +1 (W2) over GF(1033)"""
    T = _load("tower_lib")
    TC = _load("tower_census")
    q, s = T.Q, T.S_
    F = T.Field("sym")
    blocks = [F.mat(A) for A in T.block_mats()]
    target = T.Q_MONIC.subs(q, q ** 3)
    for ab in ((0, 2), (2, 2), (2, 0)):
        P = sp.expand(T.charpoly_on_H1(TC.fibre_P(F, blocks, ab, 4, 3)))
        assert sp.simplify(P - target) == 0, ab
    g0 = q ** 6 - 34 * q ** 3 + 1
    K = T.Field("ext", g=g0)
    S = TC.fibre_P(K, [K.mat(A) for A in T.block_mats()], (0, 2), 4, 3)
    B = T.FibreMonodromy(K).coboundary((0, 2), 4)
    assert T.kernel_dims_on_H1(S, B, K.unit(2, 4)) == [1, 2, 2, 2]
    cov = T.rs_cover(3)
    p = 1033
    roots, ok = TC.gf_roots_poly(g0, p)
    assert ok and roots
    Fp = T.Field("gf", p=p, r=roots[0], iota=T.gf_root_of_unity(p, 4))
    rep = T.DMRep(cov["gens"], T.twisted_rep(cov, Fp, (0, 2), 4, 2, 4))
    c = TC.counts_case_a(rep, cov["rels"], cov["mu"], cov["lam"], "gf", p)
    assert c["h1"] == 1 and c["W1"]["c1"]["I"] == -1 and c["W2"]["c1"]["I"] == 1 and c["W1"]["c1"]["I_L2"] == 0


def test_case_b_on_M4_live():
    """a 3-torsion character of M4 at q^2 - 7 q + 1, lam = 1: I(W1) = +1, I(W2) = -1 over GF(p) (case (b), x u c != 0)"""
    T = _load("tower_lib")
    TC = _load("tower_census")
    q = T.Q
    g0 = q ** 2 - 7 * q + 1
    cov = T.rs_cover(4)
    p = TC.primes_for(12, 1, accept=lambda p: TC.gf_roots_poly(g0, p)[1] and TC.gf_roots_poly(g0, p)[0])[0]
    roots, _ = TC.gf_roots_poly(g0, p)
    Fp = T.Field("gf", p=p, r=roots[0], iota=T.gf_root_of_unity(p, 4))
    c = TC.counts_case_b(cov, Fp, T.rs_rho(cov, Fp), (0, 1), 3, 0, 4, "gf", p)
    assert c["h1(L)"] == 1 and c["h1(V_nu)"] == 1 and c["h1(V_eta)"] == 1
    assert c["W1"]["c1"]["I"] == 1 and c["W1"]["c1"]["data(a0,a1,t0,r1)"][3] == 0 and c["W2"]["c1"]["I"] == -1


def test_part_c2_on_M2_and_M4_live():
    """the GF(p) gcd test reproduces the record on levels 2 and 4"""
    TC = _load("tower_census")
    rec = _record("tower_census")["C2"]
    for n in (2, 4):
        assert _norm(TC.part_c2(n, lambda m: None)) == rec[str(n)]


def test_the_record():
    """D1-D7 and P1-P8 as read in FINDINGS sections 3-4"""
    r = _record("tower_census")
    assert r["banked_identity"]["passed"] and r["C1_expected_only_level4_3torsion"]
    A = r["A"]
    assert all(o["deck_invariant"] and o["H0(F)_generic_rank_B"] == 4 for o in A["orbits"])
    O2 = [o for o in A["orbits"] if o["orders"] == [2]][0]
    assert O2["symmetries"]["palindromic"] and O2["lams"]["-1"]["real_locus"] == "q**6 - 34*q**3 + 1"
    assert all(not L.get("identically_exceptional") for o in A["orbits"] for L in o["lams"].values())
    firing = []
    for pt in A["points"]:
        kd = pt["fibre"]["ker_dims_(S-lam)^j_on_H1"]
        rows = [c for x in pt["mod_p"] for c in x["counts"].values()] + list(pt["exact_counts"].values())
        w1 = {v["I"] for c in rows for v in c["W1"].values()}
        w2 = {v["I"] for c in rows for v in c["W2"].values()}
        assert pt["fibre"]["rank_B"] == 4 and all(c["h1"] == kd[0] for c in rows)
        assert all(v.get("I_L2", 0) == 0 for c in rows for v in list(c["W1"].values()) + list(c["W2"].values()))
        if kd[1] > kd[0]:
            firing.append((pt["orbit"], pt["lam"]))
            assert w1 == {-1} and w2 == {1}
        else:
            assert w1 == {0} and w2 == {0}
    assert firing == [[[[0, 2], [2, 2], [2, 0]], "-1"]] or firing == [([[0, 2], [2, 2], [2, 0]], "-1")]
    for row in r["B"]:
        assert all(x["h1_M6"] == row["shapiro_h1_M6 = h1(lam3) + h1(-lam3)"] for x in row["rows"])
    c1 = [fac["point"] for rows in r["C1"].values() for row in rows for fac in row.get("factors", []) if fac.get("point")]
    assert len(c1) == 2
    for pt in c1:
        for x in pt["mod_p"]:
            for c in x["counts"].values():
                assert c["W1"]["c1"]["I"] == 1 and c["W2"]["c1"]["I"] == -1
        assert all(c["W1"]["c1"]["I"] == 1 for c in pt["exact_counts"].values())
    assert {n: len(v) for n, v in r["D"]["C2_unresolved"].items()} == {"4": 8, "5": 36, "6": 58}


def test_the_post_run_record():
    """(a) P_O2 = Q(q^3, s); (b) the 70 non-self-coincident unresolved pairs share only q^2 + q + 1; (c) P_nu = P_nu^-1 at levels
    2-6; (d) the triplet's members agree exactly and at every prime-root pair, and Shapiro holds"""
    r = _record("post_run_checks")
    assert r["a_O2_is_Q_at_q_cubed"]["P_O2(q,s) = Q_monic(q^3, s)"]
    b = r["b_C2_lam1_common_factor"]
    assert [b[n]["pairs"] for n in ("4", "5", "6")] == [8, 20, 42]
    assert all(b[n]["every_rest_is_q^2+q+1_at_every_prime"] for n in ("4", "5", "6"))
    c = r["c_P_nu_equals_P_nu_inverse"]
    assert all(v["P_nu = P_nu^-1 identically over GF(p)"] and v["pairs_differing"] == 0 for v in c.values())
    assert [c[n]["pairs_nu_nu^-1"] for n in ("2", "3", "4", "5", "6")] == [2, 6, 22, 60, 158]
    d = r["d_triplet_and_shapiro"]
    assert d["D6_all_agree"] and d["mod_p_rows"] == 10
    assert all(v[:3] == [-1, 1, 0] and v[3] == [0, 1, 1, 1] for v in d["exact"].values())


@pytest.mark.slow
def test_the_controls_reproduce():
    """controls.main() equals the committed record (about five minutes)"""
    rec = _record("controls")
    out = _norm(_load("controls").main())
    out.pop("seconds"), rec.pop("seconds")
    assert out == rec


def test_findings_verdict_and_hygiene():
    """the verdict is PROVED, declares its law (corrected 2026-10-02), keeps 0 of 19; the findings carry the triplet, case (b),
    the correction and the leads; the owner's private term is absent"""
    v = json.loads((ARC / "arc_verdict.json").read_text(encoding="utf-8"))
    assert v["id"] == "B1511" and v["verdict"] == "PROVED" and v["creates_law"] is True and v["instrument"] is False
    cl = v["creates_law_corrected"]
    assert (cl["date"], cl["was"], cl["registry_row"]) == ("2026-10-02", False, "T-PROJECTIVE-TOWER")
    assert "0 of 19" in v["claim_one_line"] and "I-26 stays UNEARNED" in v["claim_one_line"]
    f = (ARC / "FINDINGS.md").read_text(encoding="utf-8")
    for needle in ("**The mechanism is exact:**", "P_{O₂}(q, s) = Q(q³, s)", "| P2 | O₂ fires: a projective triplet on s961 (~40%) | **YES**",
                   "| P7 | Part C2 finds no coincidence (~85%) | **NO**", "**Theorem F's last sentence is withdrawn",
                   "**No level carries a 5̄′**", "post_run_checks_run.txt", SEALED_SHA, "I-26 stays UNEARNED", "0 of 19"):
        assert needle in f, needle
    term = bytes([98, 114, 97, 118, 101]).decode()  # the owner's private term, kept out of the source text
    for path in (ARC / "FINDINGS.md", ARC / "PREREGISTRATION.md"):
        assert term not in path.read_text(encoding="utf-8").lower()
    assert term not in v["claim_one_line"].lower()
