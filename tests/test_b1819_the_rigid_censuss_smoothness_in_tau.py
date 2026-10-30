"""B1819 -- the rigid census's smoothness in tau: the committed aggregates are consistent, they came from the committed
tool, and the tool refuses a census that is not the one on record. A planted control shows the refusal can fail closed."""
import hashlib, json, pathlib, re, sys
ROOT = pathlib.Path(__file__).resolve().parents[1]
V = ROOT / "frontier" / "B1819_the_rigid_censuss_smoothness_in_tau" / "verification"
TOOL = ROOT / "scripts" / "census" / "rigid_census_smoothness_map.py"


def test_the_aggregates_are_consistent():
    d = json.loads((V / "smoothness_map.json").read_text(encoding="utf-8"))
    assert d["aggregates_only"] is True and "256 files match the recorded manifest" in d["input"]
    for key in ("first_difference_log10_along_im_step_0.1", "first_difference_log10_along_re", "second_difference_log10_along_im"):
        a = d[key]["all"]; qs = [a["q50"], a["q90"], a["q99"], a["q99.9"], a["max"]]
        assert qs == sorted(qs), key
    assert 0 <= d["second_difference_log10_along_im"]["fraction_above_0.08"] < 0.01
    assert "exit 0" in (V / "smoothness_map_run.txt").read_text(encoding="utf-8")


def test_the_tool_pins_the_recorded_manifest():
    src = TOOL.read_text(encoding="utf-8")
    h = re.search(r'RECORDED_MANIFEST_SHA256 = "([0-9a-f]{64})"', src).group(1)
    reg = (ROOT / "docs" / "POINT_REGISTER.md").read_text(encoding="utf-8")
    assert h in reg, "the tool's manifest hash is not the one on record (P-495)"
    assert "if h != RECORDED_MANIFEST_SHA256:" in src


def test_the_tool_refuses_a_census_that_is_not_on_record(tmp_path):
    sys.path.insert(0, str(TOOL.parent)); import rigid_census_smoothness_map as T
    (tmp_path / "full_menu").mkdir(); (tmp_path / "full_menu" / "x.jsonl.gz").write_bytes(b"planted")
    per = {"x.jsonl.gz": hashlib.sha256(b"planted").hexdigest()}
    allh = hashlib.sha256(("%s  %s\n" % (per["x.jsonl.gz"], "x.jsonl.gz")).encode()).hexdigest()
    (tmp_path / "full_menu_MANIFEST.json").write_text(json.dumps({"per_file": per, "sha256_of_the_manifest": allh}), encoding="utf-8")
    ok, why = T.manifest_ok(tmp_path)
    assert not ok and "not the one on record" in why
