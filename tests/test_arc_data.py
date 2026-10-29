"""P-420 phase 0 -- scripts/checks/arc_data.py detects each defect class on a planted frontier, and nothing on a clean one."""
import importlib.util, json, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[1]
sp = importlib.util.spec_from_file_location("arc_data", ROOT / "scripts" / "checks" / "arc_data.py")
AD = importlib.util.module_from_spec(sp); sp.loader.exec_module(AD)


def _arc(root, folder, **v):
    d = root / "frontier" / folder; d.mkdir(parents=True, exist_ok=True)
    (d / "arc_verdict.json").write_text(json.dumps(v), encoding="utf-8")


def test_clean_frontier_has_no_defects(tmp_path):
    _arc(tmp_path, "B1_a", id="B1", depends_on=[], claim_one_line="x")
    _arc(tmp_path, "B2_b", id="B2", depends_on=["B1"], supersedes="B1", claim_one_line="y")
    (tmp_path / "frontier" / "B1_a" / "arc_verdict.json").write_text(json.dumps({"id": "B1", "superseded_by": "B2", "claim_one_line": "x"}), encoding="utf-8")
    out = AD.check(root=str(tmp_path))
    assert all(not out[k] for k in out if k[:2] in ("D1", "D2", "D3", "D4", "D5", "D6", "D7"))


def test_every_planted_defect_is_found(tmp_path):
    _arc(tmp_path, "B1_a", id="B1", depends_on=["B9", "B5", "B6", "K002", "sm:B1268"], claim_one_line="B2 retracts a clause of this")
    _arc(tmp_path, "B1_b", id="B1", depends_on=[])                       # D1
    _arc(tmp_path, "B2T_c", id="B2", depends_on=[], superseded_by="B3")    # D2; D6 (B3 does not name B2)
    _arc(tmp_path, "B3_d", id="B3", depends_on=[])
    (tmp_path / "frontier" / "B5_no_verdict").mkdir(parents=True)       # R4: a preregistration folder, not a defect
    (tmp_path / "frontier" / "B6_findings_only").mkdir(parents=True)    # D4: FINDINGS without a verdict
    (tmp_path / "frontier" / "B6_findings_only" / "FINDINGS.md").write_text("x", encoding="utf-8")
    out = AD.check(root=str(tmp_path))
    assert out["D1 one id, several verdict files"] == {"B1": ["B1_a", "B1_b"]}
    assert out["D2 folder number is not the verdict id"] == [["B2T_c", "B2"]]
    assert list(out["D3 dependency on a number with no folder"]) == ["B9"]
    assert list(out["D4 dependency on a folder with FINDINGS but no verdict file"]) == ["B6"]
    assert list(out["R4 dependency on a folder with neither verdict nor FINDINGS"]) == ["B5"]
    assert out["D5 dependency on a non-arc id"] == {"K002": ["B1"], "sm:B1268": ["B1"]}
    assert out["D6 one-sided supersession"] == ["B2 superseded_by B3; B3 does not name B2"]
    assert [r[:2] for r in out["D7 relation in prose only (candidates)"]] == [["B1", "B2"]]
