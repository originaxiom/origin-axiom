"""B1944's lock: the three outputs are the sealed ones (their hashes, committed before reading), the governing outcome is
FAIL with no passing option, version 1 agrees, and the page's table is the outputs' figures."""
import json, hashlib, re, pathlib
HERE = pathlib.Path(__file__).resolve().parent
ROOT = next(q for q in HERE.parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
B40 = next((ROOT / "frontier").glob("B1940_*")) / "verification"; B32 = next((ROOT / "frontier").glob("B1932_*")) / "verification"


def test_the_outputs_are_the_sealed_ones_and_say_fail():
    for f, h in ((B40 / "big_run_output_v3.json", "0441eb5c"), (B40 / "big_run_windows_v3_output.json", "952f3fc4"), (B32 / "big_run_output.json", "667ff85f")):
        assert hashlib.sha256(f.read_bytes()).hexdigest().startswith(h), f
    v3 = json.loads((B40 / "big_run_output_v3.json").read_text()); v1 = json.loads((B32 / "big_run_output.json").read_text())
    assert v3["outcome_governing_seven"] == "FAIL" and v3["passing_options_none_preferred"] == [] and v1["outcome"] == "FAIL"
    f = (HERE.parent / "FINDINGS.md").read_text()
    for o, e in v3["options"].items():
        assert ("%.1f" % e["chi2_seven"]).replace("", "") in f.replace(" ", "").replace(",", "") or ("%.1f" % e["chi2_seven"]) in f.replace(" ", "").replace(" ", ""), o
    assert "**The governing outcome is FAIL.**" in f
