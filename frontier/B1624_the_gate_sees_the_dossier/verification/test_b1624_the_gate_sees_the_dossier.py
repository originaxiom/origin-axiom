"""B1624 -- the gate sees dossier items: B1606 declares sm:W19-W22 and the gate passes only because each row is VERIFIED;
W19's facts computed exactly."""
import json, pathlib, sys
ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "scripts" / "gates"))


def test_b1606_declares_its_dossier_dependencies_and_the_gate_checks_them():
    import gates
    v = json.loads(ROOT.joinpath("frontier", "B1606_three_on_the_weave_graded", "arc_verdict.json").read_text(encoding="utf-8"))
    assert v["rests_on_seat"] == ["sm:W19", "sm:W20", "sm:W21", "sm:W22"]
    rests = [r for r in gates.seat_positive_rests() if r[0] == "B1606"]
    assert len(rests) == 4 and all(r[2] for r in rests)
    assert gates._SEAT_ID_RE.match("sm:W19") and not gates._SEAT_ID_RE.match("sm:Wx")


def test_w19_facts():
    d = json.loads(ROOT.joinpath("frontier", "B1624_the_gate_sees_the_dossier", "verification", "w19_check.json").read_text())
    assert d["F1_dim_C_M12"] == 2 and d["F2_chi_SL2Z"] == "-1/12" and d["F3_chi_AutPlus_F2"] == "1/12" == d["F4_chi_M12_harer_zagier"]
    assert d["F5_agree_and_nonzero"] is True
