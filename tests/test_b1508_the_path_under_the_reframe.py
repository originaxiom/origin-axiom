"""B1508 lock -- THE PATH UNDER THE REFRAME (2026-10-01).  The path note's blocks read for scope after the owner's correction
("they assume m004 is the only object"), and the record searched beyond m004 (the audit lane = codex's second lane, the xB seat, the
paper-review rounds, outside-bench).  Locked here: the recomputed items -- the audit lane's partial-filling witness and the filling
descent's abelian shadow, the witness's peripheral ranks against a control on m004's degree-5 covers, R69's level counts against
B1506's own record, the free dimensionless constant of the object's action -- and the findings' load-bearing sentences."""
import importlib.util
import json
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1508_the_path_under_the_reframe"
VER = ARC / "verification"


def _load(name):
    spec = importlib.util.spec_from_file_location(f"b1508_{name}", VER / f"{name}.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def test_the_partial_filling_witness_live():
    """the audit lane's witness: an irregular degree-5 cover of m004 with three cusps; cusp 0 filled along (2, 1) leaves two cusps,
    volume 7.706911803, CS 0.157590040879 (0.0924 from {0, 1/4} mod 1/2), symmetry group Z/2 + Z/2, not amphicheiral, H1 = Z^2"""
    pytest.importorskip("snappy")
    P = _load("partial_filling")
    w = P.witness()
    assert (w["cusps"], w["tets"], w["H1"], w["vol_ratio"]) == (3, 10, "Z + Z + Z", 5.0)
    assert w["m004_covers_isometric"] == [{"index": 2, "type": "irregular", "degree": 5}]
    assert w["filled_cusps"] == 2 and w["filled_solution"] == "all tetrahedra positively oriented"
    assert abs(w["filled_volume"] - 7.706911803) < 1e-8 and abs(w["filled_cs"] - 0.157590040879) < 1e-10
    assert abs(w["cs_distance_from_mirror_classes"] - 0.092409959) < 1e-8
    assert w["filled_symmetry_group"] == "Z/2 + Z/2" and w["filled_amphicheiral"] is False and w["filled_H1"] == "Z + Z"


def test_the_filling_descent_live():
    """R57's non-cover transport, abelian shadow: H1(M(s)) = H1(M)/<[s]> -- Z^3 -> Z^2, equal to SnapPy's H1 of the filling"""
    pytest.importorskip("snappy")
    d = _load("partial_filling").descent()
    assert d["H1_M"] == [0, 0, 0] and d["H1_M_mod_s"] == [0, 0] and d["snappy_H1_filled"] == "Z + Z" and d["agree"]


def test_the_peripheral_ranks_live():
    """B1369's free-cusp criterion: on m004's degree-5 covers only the three-cusped one (index 2) has free cusps (all three); the
    witness's unfilled cusps are free, the two left after filling are not (rank 2 = b1)"""
    pytest.importorskip("snappy")
    r = _load("partial_filling").ranks()
    ctrl = {c["index"]: (c["cusps"], c["b1"], c["ranks"]) for c in r["m004_degree5_covers"]}
    assert ctrl == {0: (1, 1, [1]), 1: (2, 2, [2, 2]), 2: (3, 3, [2, 2, 2]), 3: (2, 2, [2, 2])}
    assert r["unfilled"] == {"b1": 3, "ranks": [2, 2, 2], "free": [True, True, True]}
    assert r["filled"] == {"b1": 2, "ranks": [2, 2], "free": [False, False]}


def test_the_level_counts_against_r69():
    """R69's (-1,-1,-3,-1,-1,-3) is B1506's own post-run record in every sector (-gcd(n, 3)); pullbacks 3 -> 6 keep the index"""
    L = _load("level_counts").main()
    assert L["s961_generation_shaped"] == 48
    assert L["every_sector_equals_R69"] and L["equals_minus_gcd_n_3"] and len(L["ind_D0_counts_per_sector"]) == 6
    assert L["pullbacks_keep_index"] and L["pullback_3_to_6"]["candidates"] == 256


def test_the_free_constant():
    """sigma = l/4G is dimensionless in three dimensions ([G] = L^(d-2)); c = 6 sigma; one free dimensionless constant"""
    F = _load("free_constant").main()
    assert F["G_length_exponent_by_d"] == {3: 1, 4: 2, 5: 3, 11: 9}
    assert F["sigma_dimensionless"] and F["brown_henneaux_c_over_sigma"] == "6"
    assert F["free_dimensionless_constants_in_S_eq_minus_Vol_sigma"] == 1


def test_findings_verdict_and_hygiene():
    """the verdict is PROVED, creates no law, and names the reframe; the findings carry the scope table, the harvested results with
    their sources and the corrections; the records exist"""
    v = json.loads((ARC / "arc_verdict.json").read_text(encoding="utf-8"))
    assert v["id"] == "B1508" and v["verdict"] == "PROVED" and v["creates_law"] is False and v["instrument"] is False
    assert "reality uses more thsn that" in v["claim_one_line"] and "0 of 19" in v["claim_one_line"]
    f = (ARC / "FINDINGS.md").read_text(encoding="utf-8")
    for needle in ("## 1. The path note's blocks, read for scope", "ONE seat with TWO lanes", "exclusivity is unearned",
                   "AFFINE_BACKGROUND.md:8–13", "one singlet + one 16 + one 16*", "CURRENT_BALANCE.md", "CONE_MULTIPLET_PROOF.md:79–88",
                   "LEVEL_ACTION.md:50–53", "cube~3.24", "B1398's own scope sentence", "xB027", "REFEREE_REPORT_ROUND3",
                   "THE_SUPPLIED_LITERATURE.md:128", "computed without a seal", "The join is what is missing", "0 of 19"):
        assert needle in f, needle
    term = bytes([98, 114, 97, 118, 101]).decode()  # the owner's private term, kept out of the source text
    assert term not in f.lower() and term not in v["claim_one_line"].lower()
    for name in ("partial_filling", "level_counts", "free_constant"):
        assert (VER / f"{name}_run.txt").exists(), name
