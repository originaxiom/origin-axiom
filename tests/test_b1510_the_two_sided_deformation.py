"""B1510 lock -- THE TWO-SIDED DEFORMATION (2026-10-01).  The 16's and the 16*'s singlets c and c* switched on together on the audit
lane's harmonic vacuum A + 1 (A = mu rho_q, Ballas' projective holonomy of m004 with a central twist), sealed at 0cb24e2b before the
run.  Locked here:
- the seal's digest;
- the banked identity and the controls, live (B1509's 54 index rows through this arc's own F((eps)) index; GL(2) and GL(3) at simple
  roots);
- one sealed point of each kind and the exact order-two cross-check, live against the record;
- the decided items D1-D6 and the predictions P1-P5 read from the record;
- the post-run checks' record;
- the findings' load-bearing sentences.

The full sealed run and the post-run checks are marked slow."""
import hashlib
import importlib.util
import json
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1510_the_two_sided_deformation"
VER = ARC / "verification"
SEALED_SHA = "6010649413df2ade5d4fe0760b7dae29c8cdfa1a2ae12b0a2d714ee05d5786a3"


def _load(name):
    if str(VER) not in sys.path:
        sys.path.insert(0, str(VER))
    spec = importlib.util.spec_from_file_location(f"b1510_{name}", VER / f"{name}.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def _record(name):
    return json.loads((VER / f"{name}_run.txt").read_text(encoding="utf-8"))


def _norm(x):
    return json.loads(json.dumps(x, sort_keys=True, default=str))


def test_the_seal_is_unchanged():
    """PREREGISTRATION.md is byte-identical to the sealed text (SEAL_LEDGER), and carries the provenance markers"""
    assert hashlib.sha256((ARC / "PREREGISTRATION.md").read_bytes()).hexdigest() == SEALED_SHA
    txt = (ARC / "PREREGISTRATION.md").read_text(encoding="utf-8")
    assert "BANKED IDENTITY:" in txt and "PRIOR ART:" in txt


def test_the_banked_identity_and_the_controls_live():
    """C1-C3: B1509's I(W1), I(W2) (-1/+1 at mu = -1, 0/0 at +-i) and the split 0 at all 18 point-prime pairs; C0 the valuation
    rank; C5 the chiral solver returns the exact one-sided family; C4/C6 the GL(2) and GL(3) branches at simple roots count 0"""
    T = _load("two_sided")
    rows = T.control_one_sided()
    assert len(rows) == 54 and all(r["I"] == r["expected"] and r["exact_rep_to_order"] == 6 for r in rows)
    assert all(T.control_valuation_rank().values())
    c5 = T.control_chiral_one_sided()
    assert len(c5) == 6 and all(r["U_k_zero_for_k>=2"] and r["line_stays_(1,1)"] and r["I"] == -1 for r in c5)
    c4 = [r for r in T.control_gl2() if "skipped" not in r]
    assert len(c4) == 4 and all(r["absolute_exists_to_order"] == 8 and r["index_N8"]["I"] == 0 for r in c4)
    c6 = T.control_gl3()
    assert len(c6) == 6
    for r in c6:
        assert r["H1"]["h1_gl"] == 5 and r["rigidity"]["restriction_injective"] and r["rigidity"]["cusp_pair_regular"]
        assert r["absolute_exists_to_order"] == 8 and r["fixed_end_order2"]["o_rel_sl"] == 1 and r["index"][8]["I"] == 0


def test_one_sealed_point_of_each_kind_live():
    """the sealed instrument at (17 +- 12 sqrt2, -1) and (7 +- 4 sqrt3, i) mod 1009 reproduces the record entry exactly"""
    T = _load("two_sided")
    rec = _record("two_sided")["modp"]
    setups = T.modp_setups(1009)
    for i in (0, 2):
        assert _norm(T.sealed_point(setups[i])) == rec[i], setups[i].label


def test_the_exact_order_two_live():
    """over Q(sqrt2, sqrt3, i): the order-two obstruction vanishes at all six points; kappa_l = 0 exactly at mu = -1"""
    rows = _load("two_sided").sealed_exact_order2()
    assert _norm(rows) == _record("two_sided")["exact_order2"]
    assert all(r["order2_obstruction_zero"] for r in rows)
    assert [r["kappa_l_zero"] for r in rows] == [True, True, False, False, False, False]


def test_the_decided_items_in_the_record():
    """D1-D6 at all 18 point-prime pairs"""
    rec = _record("two_sided")
    assert rec["banked_identity_B1509_reproduced"] and rec["banked_identity_rows"] == 54
    pts = rec["modp"]
    assert len(pts) == 18
    for x in pts:
        p = int(x["point"].split(" mod ")[1].split(",")[0])
        assert x["H1"] == {"basis_spans_H1": True, "dim_B1": 23, "dim_Z1": 30, "h1_gl": 7, "h1_sl_adjoint": 3}
        assert x["rigidity"]["restriction_rank"] == 3 and x["rigidity"]["h0_T_gl_a"] == 4
        assert x["order2_obstruction_zero"] and x["absolute"]["log"][0]["coker_blocks"] == ["block"] * 3 + ["A", "A*"]
        assert x["kappa_l_zero"] == (x["mu"] == "-1")
        fe = x["fixed_end_order2"]
        assert fe["o_rel_sl"] == 1 and fe["line_at_longitude"] == x["kappa_l_hat"]
        assert (fe["line_at_longitude"] + fe["block_trace_at_longitude"]) % p == 0
        if x["mu"] != "-1":
            assert x["chiral"]["exists_to_order"] == 1
        for branch in ("absolute", "chiral"):
            for n, ix in x[branch].get("index", {}).items():
                assert ix["I"] == 0 and ix["a0"] == ix["b0"] == 0 and ix["r1"] == ix["q1"] == ix["t0"] == ix["s0"]
        if "index" in x["chiral"]:
            assert [x["chiral"]["index"]["8"][k] for k in ("a1", "b1", "r1", "q1")] == [1, 1, 1, 1]
            edge = x["chiral"]["index"]["10"]
            assert edge["a1"] == 0 and edge["r1"] == 1 and edge["prec_left"] == 1   # the edge artifact (FINDINGS section 4 (a))


def test_the_predictions_in_the_record():
    """P1-P4 YES at every pair they name; P5 NO: the instrument's free-end branch keeps lam_l = 1 at mu = -1"""
    pts = _record("two_sided")["modp"]
    for x in pts:
        a = x["absolute"]
        v = a["verify"]
        assert a["exists_to_order"] == 10 and v["relator_identity_to_order_N"] and v["det_one_to_order_N"] and v["parity_symmetric"]
        o3 = a["log"][1]
        assert o3["order"] == 3 and o3["rank_on_A_rows"] == 1 and o3["rank_on_A*_rows"] == 1 and o3["rank_of_linear_map"] == 2
        assert o3["base_A_nonzero"] == 1 and o3["base_A*_nonzero"] == 1 and o3["solvable"]
        for ix in a["index"].values():
            assert ix["a1"] == ix["b1"] == 0
        if x["mu"] == "-1":
            ch = x["chiral"]
            assert ch["exists_to_order"] == 10 and ch["verify"]["line_stays_(1,1)"] and ch["verify"]["relator_identity_to_order_N"]
            assert ch["log"][1]["rank_of_linear_map"] == 4
            assert set(v["lam_l_series"][1:]) == {"0"} or set(v["lam_l_series"][1:]) == {0}
            assert v["lam_m_series"][2] not in (0, "0")
        else:
            assert v["lam_l_series"][2] not in (0, "0")


def test_the_post_run_record():
    """(a) from an order-12 chiral jet the index is (1, 1, 1, 1) at N = 8 and 10 and the artifact moves to N = 12; (c) the free-end
    branch keeps lam_l = 1 to order 14 without the twist; (d) the q-tangent is the first adjoint class, and the free-end branch
    started from the third class moves lam_l at exactly order four"""
    rec = _record("post_run_checks")
    for x in rec["a_chiral_index_at_the_edge"]:
        assert x["exists_to_order"] == 12
        for n in ("8", "10"):
            assert [x["index"][n][k] for k in ("I", "a1", "b1", "r1", "q1")] == [0, 1, 1, 1, 1]
        assert x["index"]["12"]["a1"] == 0 and x["index"]["12"]["last_pivot_V"] == 12
    for x in rec["c_free_end_to_order_14"]:
        assert x["exists_to_order"] == 14 and set(x["lam_l_series"][1:]) == {0} and not x["twist_ever_chosen"]
    for x in rec["d_adjoint_direction"]:
        assert x["q_tangent_is_cocycle"]
        assert x["q_tangent_in_adjoint_basis"]["adj1"] != 0 and x["q_tangent_in_adjoint_basis"]["adj2"] == 0
        assert x["q_tangent_in_adjoint_basis"]["adj3"] == 0
        m = x["minor_with_base_per_class"]
        assert m["adj1"] == 0 and m["adj2"] == 0 and m["q_tangent"] == 0 and m["adj3"] != 0
        third = [r for r in x["free_end_reordered"] if r["adjoint_order"][0] == "adj3"][0]
        lam = third["lam_l_series"]
        assert lam[1:4] == [0, 0, 0] and lam[4] != 0
    for x in rec["b_longitude_columns_at_step_three"]:
        cols = x["columns"]
        assert all(cols[n]["lam_l_next"] == 0 for n in ("c", "c*", "centre"))
        assert cols["twist_T"]["lam_l_next"] != 0 and all(cols[f"adj{i}"]["lam_l_next"] != 0 for i in (1, 2, 3))


@pytest.mark.slow
def test_the_full_sealed_run_reproduces_the_record():
    """two_sided.sealed() equals the committed record (about 64 s)"""
    assert _norm(_load("two_sided").sealed()) == _record("two_sided")


@pytest.mark.slow
def test_the_controls_and_post_run_checks_reproduce():
    """the controls and the post-run checks reproduce their records (about 80 s)"""
    assert _norm(_load("two_sided").controls()) == _record("controls")
    assert _norm(_load("post_run_checks").main()) == _record("post_run_checks")


def test_findings_verdict_and_hygiene():
    """the verdict is PROVED, declares its law (corrected 2026-10-02), keeps 0 of 19; the findings carry the theorems, the
    table, the post-run checks and the disclosures; the owner's private term is absent"""
    v = json.loads((ARC / "arc_verdict.json").read_text(encoding="utf-8"))
    assert v["id"] == "B1510" and v["verdict"] == "PROVED" and v["creates_law"] is True and v["instrument"] is False
    cl = v["creates_law_corrected"]
    assert (cl["date"], cl["was"], cl["registry_row"]) == ("2026-10-02", False, "T-TWO-SIDED-ZERO")
    assert "0 of 19" in v["claim_one_line"] and "I-26 stays UNEARNED" in v["claim_one_line"]
    f = (ARC / "FINDINGS.md").read_text(encoding="utf-8")
    for needle in ("**Theorem A (the sl(4) obstructions vanish).**", "**Theorem C (the count is zero).**",
                   "**Proposition F (the fixed-end class).**", "| P5 | at μ = −1 the free-end branch's λ_ℓ − 1 has valuation exactly 4 | **NO**",
                   "| P3 | chiral branch at μ = −1 to order 10", "**A reading-rule slip.**", "post_run_checks_run.txt",
                   "6010649413df2ade5d4fe0760b7dae29c8cdfa1a2ae12b0a2d714ee05d5786a3", "F_S = λ Q₁Q̃₁", "I-26 stays UNEARNED",
                   "0 of 19"):
        assert needle in f, needle
    term = bytes([98, 114, 97, 118, 101]).decode()  # the owner's private term, kept out of the source text
    for path in (ARC / "FINDINGS.md", ARC / "PREREGISTRATION.md"):
        assert term not in path.read_text(encoding="utf-8").lower()
    assert term not in v["claim_one_line"].lower()
