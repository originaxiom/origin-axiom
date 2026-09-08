"""B1296 -- THE CHARGE-LOCUS PARITY LOCK: both halves reproduce by RUNNING and the banked numbers are pinned."""
import json, subprocess, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1296_the_charge_locus_parity_lock"
VER = ARC / "verification"


def _run(args, cwd):
    r = subprocess.run([sys.executable] + [str(a) for a in args], capture_output=True, text=True, cwd=str(cwd))
    assert r.returncode == 0, r.stdout[-2000:] + r.stderr[-2000:]
    return r.stdout


def test_T1_T2_T4_the_swap_theorem_and_the_level_curve_lemma_reproduce_by_RUNNING(tmp_path):
    # the script locates B1295's harmonic generator from its own path; outputs go to the scratch cwd
    out = _run([VER / "swap_and_level.py", tmp_path / "swap.json"], tmp_path)
    assert out.rstrip().endswith("SELFTEST: PASS"), out[-600:]
    assert "VERDICT: T1 SWAP holds" in out
    j = json.loads((tmp_path / "swap.json").read_text(encoding="utf-8"))
    assert j["n_half_modes"] == 538 and len(j["isometries"]) == 8
    assert j["equivariance_worst_rel_deviation"] < 1e-8                       # g(m z) = alpha(m) g(z) for all 8 isometries
    assert sorted(m["alpha"] for m in j["isometries"]) == [-1] * 4 + [1] * 4  # 4 swap, 4 preserve
    assert j["swap_on_grid"] is True                                          # sigma maps d+M onto d-M
    assert j["endpoint_max_abs_g"] < 1e-8 * j["gmax_on_sample"]               # arcs are level curves
    assert abs(j["endpoint_min_abs_omega_dx"] - 0.724301) < 1e-5              # ... but not zeros of the Higgs
    dx = sorted({round(e["omega_dx"], 6) for e in j["endpoints"] if abs(e["t"] - 0.7) < 1e-9})
    assert dx == [0.724301, 1.280438], dx                                     # two orbits, two values
    assert j["endpoint_stabiliser_sizes"] == {"2": 8}                         # no second stabiliser
    o = j["endpoint_orbits"]
    assert o["sizes"] == [4, 4] and o["arc_endpoints_same_orbit"] == [True, True] and o["two_arcs_same_orbit"] is False


def test_the_F4_chamber_and_the_toggle_reproduce_by_RUNNING(tmp_path):
    out = _run([VER / "e6_theta_spectra.py", tmp_path / "e6.json"], tmp_path)
    assert out.rstrip().endswith("SELFTEST: PASS"), out[-600:]
    j = json.loads((tmp_path / "e6.json").read_text(encoding="utf-8"))
    assert j["fixed_roots"] == 24 and j["even_cartan_dim"] == 4 and j["odd_cartan_dim"] == 2
    # the pre-registration's two wrong expectations, as the computation has them
    pl = j["parity_lock_spectral"]
    assert pl["even_symmetric"] == "44/44" and pl["odd_symmetric"] == "24/168" and pl["mixed_symmetric"] == "0/4"
    chiral = {"w4", "w3+w5", "w2+w4", "w1+w6+w3+w5"}
    assert set(pl["F4_chamber_summary"]["chiral"]) == chiral == set(pl["F4_chamber_summary"]["cubic_anomalous"])
    assert pl["F4_chamber_summary"]["faces"] == 15
    F = j["F4_chamber"]
    assert {k: v["chiral_dim_78"] for k, v in F.items() if k in chiral} == {"w4": 54, "w3+w5": 54, "w2+w4": 18, "w1+w6+w3+w5": 6}
    for k, v in F.items():
        if k in chiral or k.startswith("omega_1") or k.startswith("w1-w6"):
            continue
        assert v["vectorlike_78"] and v["chiral_dim_78"] == 0 and v["cubic_anomaly_free"], k   # the other 11 faces
        assert all(w == 0 for w in v["witten_mod2"]), k
    assert F["omega_1^vee (mixed)"]["C_ss"] == ["D5"] and F["omega_1^vee (mixed)"]["chiral_dim_78"] == 32 and F["omega_1^vee (mixed)"]["cubic_anomaly_free"]
    assert F["w1-w6 (odd wall)"]["C_ss"] == ["D5"] and F["w1-w6 (odd wall)"]["chiral_dim_78"] == 32 and F["w1-w6 (odd wall)"]["cubic_anomaly_free"]
    # the four fundamental coweights, both sectors
    V = j["vectorlike_test"]
    assert V["omega_2^vee (EVEN)"]["78"]["vectorlike"] and V["omega_1^vee + omega_6^vee (EVEN)"]["27"]["vectorlike"]
    assert V["omega_4^vee (EVEN)"]["78"]["chiral_dim"] == 54 and V["omega_4^vee (EVEN)"]["27"]["chiral_dim"] == 36
    assert V["omega_3^vee + omega_5^vee (EVEN)"]["78"]["chiral_dim"] == 54 and V["omega_3^vee + omega_5^vee (EVEN)"]["27"]["chiral_dim"] == 36
    for k in ("odd root line (1,1)", "odd root line (2,-1)", "odd generic (7,3)"):
        assert V[k]["78"]["vectorlike"] and V[k]["27"]["vectorlike"], k
    # the sector table: 1:3 on the swapped-pair faces, uncancellable on the fixed-A2 faces, E7/E8 parents do not cancel
    S = j["sector_anomalies"]
    assert S["w4"]["cancelling_multiplicities_primitive"] == [[1, 3]] == S["w2+w4"]["cancelling_multiplicities_primitive"]
    assert S["w3+w5"]["cancelling_multiplicities_primitive"] == [] == S["w1+w6+w3+w5"]["cancelling_multiplicities_primitive"]
    a2 = [(f["A3_78"], f["A3_27"]) for f in S["w4"]["factors"] if f["type"] == "A2"]
    assert a2 == [("-3", "1"), ("3", "-1")], a2
    assert [(f["A3_78"], f["A3_27"]) for f in S["w3+w5"]["factors"] if f["type"] == "A2"] == [("-1", "-2")]
    for k in ("w2", "w1+w6", "w2+w1+w6", "interior (all 4)", "omega_1^vee (mixed)", "w1-w6 (odd wall)", "odd generic (7,3)"):
        assert S[k]["cancelling_multiplicities_primitive"] == "unconstrained", k
    assert sorted(S["parent_frames_on_w4_first_A2"].values()) == ["-1", "3"]
    # the theta-odd plane is the restricted A2 of (E6, F4), multiplicity 8, and the odd wall is a Weyl conjugate of omega_1^vee
    R = j["restricted_A2"]
    assert R["weyl_conjugacy"]["omega_3^vee - omega_5^vee in W.omega_1"] is True
    assert R["weyl_conjugacy"]["omega_1^vee - omega_6^vee in W.omega_6"] is True
    assert R["weyl_conjugacy"]["omega_1^vee - omega_6^vee in W.omega_1"] is False
    assert sorted(R["classes"]) == ["ROOT-LINE|cent30|symTrue", "WALL|cent46|symFalse", "generic|cent30|symFalse"]
    assert "restricted roots on the odd plane: 6 distinct, multiplicities [8]" in out, out[-1500:]
    assert j["odd_quadratic_hessian_ranks"] == [2]
    # T3 the toggle: count 2 on the theta-odd direction with equal signs, 0 with opposite signs
    pp = {(r["source"], r["charge"]): r["net_chirality"] for r in j["toggled_omega1_signs_pp"]}
    assert pp == {("27", "-2/3"): 2, ("27", "1/3"): -2, ("27", "4/3"): -2, ("78", "-1"): 2, ("78", "1"): -2}, pp
    assert all(r["net_chirality"] == 0 for r in j["toggled_omega1_signs_pm"])
    assert {r["net_chirality"] for r in j["toggled_omega_3^vee_signs_pp"]} == {2, -2}


def test_the_arc_is_registered_as_a_law_with_the_identification_row():
    v = json.loads((ARC / "arc_verdict.json").read_text(encoding="utf-8"))
    assert v["verdict"] == "PROVED" and v["creates_law"] and v["law_id"] == "T-CHARGE-LOCUS-PARITY-LOCK"
    assert [d["row"] for d in v["identifications"]] == ["I-27"] and v["identifications"][0]["status"] == "UNEARNED"   # schema: a list of {row, status, note}
    assert "B1295" in v["depends_on"]
    reg = (ROOT / "docs" / "THEOREM_REGISTRY.md").read_text(encoding="utf-8")
    assert "| T-CHARGE-LOCUS-PARITY-LOCK |" in reg and "B1296" in reg
    led = (ROOT / "docs" / "IDENTIFICATION_LEDGER.md").read_text(encoding="utf-8")
    assert "| I-27 |" in led and "B1296" in led
