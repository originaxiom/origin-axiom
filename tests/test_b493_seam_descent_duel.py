"""Locks for B493 (CL-1a duel: the seam sqrt(-15) vanishing vs CRT/Galois descent).

Two tiers, together < 60 s:
  (A) artifact locks on the committed run records (control / prediction / verify JSONs
      + FINDINGS.md documentation integrity, incl. the committed-before-compute order);
  (B) live recompute locks on the mandatory control and the key derivation identities,
      exact Q(zeta60) arithmetic via the banked engines: the flagship by two routes,
      the (1,2) descent chain (master identity vs the banked global C-table, the XY
      closed form, X0/Xbar/N1/QM/L5a/L5b, the classifier, the B459/P1 tier law), the
      (1,3) counterexample that makes L5b the named pair-specific residue, and a
      bright/dark pair of live classifications.
"""
import importlib.util
import json
import pathlib

from fractions import Fraction as Fr

_ROOT = pathlib.Path(__file__).resolve().parents[1]
_DIR = _ROOT / "frontier" / "B493_seam_descent_duel"

_spec = importlib.util.spec_from_file_location("b493_probe", _DIR / "probe.py")
P = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(P)

CONTROL = json.load(open(_DIR / "b493_control.json"))
PRED = json.load(open(_DIR / "b493_prediction_47.json"))
VERIFY = json.load(open(_DIR / "b493_verify_47.json"))
FINDINGS = (_DIR / "FINDINGS.md").read_text(encoding="utf-8")


# ---------------- tier A: the committed artifacts ----------------
def test_control_record():
    assert CONTROL["control_pass"] is True
    assert CONTROL["banked_pairs_all_ok"] is True
    assert all(CONTROL["banked_pairs_cell_exact"].values())
    assert CONTROL["brightdark_tally_banked12"] == "12/12"
    assert CONTROL["brightdark_tally_with_oos"] == "13/13"
    assert CONTROL["flagship_ok"] is True
    assert CONTROL["flagship_local_route"] == ["-1/48", "-1/80", "-1/48", "1/48"]
    assert CONTROL["universal_lemmas_clean"] is True
    assert CONTROL["p1_law_ok"] is True
    # L5b is the pair-specific residue: fails on exactly (1,3) and (2,4)
    l5b = CONTROL["L5b_by_pair"]
    assert l5b["1,3"] == 64 and l5b["2,4"] == 128
    assert all(v == 0 for k, v in l5b.items() if k not in ("1,3", "2,4"))
    assert CONTROL["lattice_only_by_pair"] == {k: (v == 0) for k, v in l5b.items()}
    assert CONTROL["node_absent_all_pairs"] is True
    # the gate scope facts: Eisenstein universal, chi5-gate (1,2)-specific
    assert CONTROL["gate3_local_clean_all_pairs"] is True
    assert CONTROL["gate15_L1_L2_clean_all_pairs"] is True
    l3 = CONTROL["gate15_L3_by_pair"]
    assert l3["1,2"] == 0 and l3["1,3"] == 6 and l3["1,4"] == 24 and l3["2,4"] == 14
    # the (1,2) master identity against the banked global C-table
    rep12 = CONTROL["descent_reports"]["1,2"]
    assert rep12["master_identity_mismatches"] == 0
    assert rep12["master_identity_checks"] == 960
    # B396's banked class-1 domain counts, reproduced from local data
    doms = {k: CONTROL["descent_reports"][k]["gate15_domain"]
            for k in ("1,2", "1,3", "1,4", "2,3", "2,4", "3,4")}
    assert doms == {"1,2": 142, "1,3": 63, "1,4": 212, "2,3": 39, "2,4": 142, "3,4": 63}


def test_prediction_and_verify_records():
    # the commitment order: prediction strictly before the global computation
    assert PRED["committed_utc"] < VERIFY["started_utc"]
    assert VERIFY["prediction_committed_utc"] == PRED["committed_utc"]
    # the prediction: DARK, full-table hash, tiers
    p = PRED["prediction"]
    assert p["s"]["bright"] is False and p["s"]["n_s_cells"] == 0
    assert p["s"]["sum_s_squared"] == "0"
    assert p["tier_counts"] == {"0001": 96, "0011": 24, "0111": 20, "1111": 100}
    assert p["node_absent"] is True and p["lattice_only"] is False
    assert len(p["channels"]) == 31
    # the outcome: HIT on every registered comparison
    assert VERIFY["all_match"] is True
    assert VERIFY["global_orders"] == [20, 12]
    assert VERIFY["G1_tensor_mismatches"] == 0
    assert VERIFY["global_table_sha256"] == p["table_sha256"]
    assert VERIFY["global_s"]["bright"] is False
    rep = VERIFY["descent_4_7_global"]
    assert rep["master_identity_mismatches"] == 0
    assert rep["xy_formula_mismatches"] == 0
    assert rep["classifier_mismatches"] == 0
    assert rep["L5b_matching_violations"] == 128
    assert rep["gate15_L2_violations"] == 0 and rep["gate15_L3_violations"] == 12


def test_findings_documentation_integrity():
    assert "PARTIAL" in FINDINGS.splitlines()[0]
    assert "Nothing to CLAIMS.md; firewall untouched" in FINDINGS
    assert PRED["prediction"]["table_sha256"] in FINDINGS
    assert "BEFORE" in FINDINGS and "OUTCOME: HIT, cell-exact" in FINDINGS
    assert PRED["committed_utc"] in FINDINGS


# ---------------- tier B: live recomputes (exact) ----------------
def test_flagship_two_routes_live():
    flag_banked = P.SC.double_one("C_theta.json", 0, 4)
    assert tuple(flag_banked) == P.SC.FLAGSHIP == (Fr(-1, 48), Fr(-1, 80), Fr(-1, 48), Fr(1, 48))
    loc3, loc5 = P.build_locals(1, 2)
    T, o1, o2 = P.closed_form_ttable(loc3, loc5)
    ch = P.channel_tables(T, o1, o2)
    assert ch[(0, 4)] == P.SC.FLAGSHIP
    assert (o1, o2) == (20, 12)


def test_descent_chain_on_1_2_live():
    data = json.load(open(_ROOT / "frontier" / "B358_seam_certification" / "C_theta.json"))
    Cglob = {(j, l): [Fr(s) for s in data["C"][j][l]] for j in range(20) for l in range(12)}
    rep, ch_local, _ = P.descent_analysis(1, 2, check_master_against=Cglob)
    # the master identity and the XY closed form, every dual point, every channel
    assert rep["master_identity_mismatches"] == 0 and rep["master_identity_checks"] == 960
    assert rep["xy_formula_mismatches"] == 0 and rep["xy_formula_checks"] == 960
    # the derived lemmas + censuses
    for key in P.UNIVERSAL_KEYS:
        assert rep[key] == 0, key
    assert rep["C3_cells_mu6_or_zero"] is True
    assert rep["d_divides_4"] is True
    assert rep["L5b_matching_violations"] == 0
    assert rep["window_census"] == {"even,even": 32, "even,zero": 40,
                                    "gen,gen": 128, "zero,zero": 40}
    # the B459/P1 law, bit for bit
    assert rep["tier_counts"] == {"0000": 120, "0011": 20, "0101": 20, "0111": 10, "1111": 70}
    assert rep["lattice_only"] is True and rep["node_Q_sqrt_minus15_absent"] is True
    # bright, 44 s-cells (P67)
    s = P.s_summary(ch_local)
    assert s["bright"] is True and s["n_s_cells"] == 44


def test_l5b_counterexample_on_1_3_live():
    rep, ch_local, _ = P.descent_analysis(1, 3)
    for key in P.UNIVERSAL_KEYS:
        assert rep[key] == 0, key
    # L5b fails -- the residue is genuinely pair-specific -- and the classifier still
    # predicts the observed non-lattice tier pointwise
    assert rep["L5b_matching_violations"] == 64
    assert rep["window_census"]["gen,even"] == 64
    assert rep["tier_counts"] == {"0001": 48, "0011": 12, "0111": 15, "1111": 45}
    assert rep["lattice_only"] is False and rep["node_Q_sqrt_minus15_absent"] is True
    assert P.s_summary(ch_local)["bright"] is False   # (1,3) dark, from local data


def test_brightdark_live_pair():
    loc3, loc5 = P.build_locals(2, 3)
    T, o1, o2 = P.closed_form_ttable(loc3, loc5)
    assert P.s_summary(P.channel_tables(T, o1, o2))["n_s_cells"] == 18   # bright (banked)
    loc3, loc5 = P.build_locals(1, 5)
    T, o1, o2 = P.closed_form_ttable(loc3, loc5)
    assert P.s_summary(P.channel_tables(T, o1, o2))["n_s_cells"] == 0    # dark (banked)


def test_classifier_case_table():
    # the stage-2 theorem's case table, spot-locked
    assert P.classify_point("0", "gen", "gen") == (1, 1, 1, 1)
    assert P.classify_point("real", "zero", "zero") == (1, 1, 1, 1)
    assert P.classify_point("real", "even", "even") == (0, 0, 1, 1)   # value in Q(sqrt5)
    assert P.classify_point("gen", "even", "zero") == (0, 1, 0, 1)    # value in Q(sqrt-3)
    assert P.classify_point("real", "even", "zero") == (0, 1, 1, 1)   # value in Q
    assert P.classify_point("gen", "gen", "gen") == (0, 0, 0, 0)      # generic
    assert P.classify_point("real", "gen", "even") == (0, 0, 0, 1)    # the L5b-failure tier
    assert P.classify_point("imag", "gen", "gen") is None             # N1 premise
    assert P.classify_point("real", "odd", "gen") is None             # L5a premise
    # q dead forces s dead in every branch: the universal Q(sqrt-15)-node absence
    for xcls in ("real", "gen"):
        for t1 in ("zero", "even", "gen"):
            for tl in ("zero", "even", "gen"):
                pat = P.classify_point(xcls, t1, tl)
                assert not (pat[1] == 1 and pat[3] == 0)
