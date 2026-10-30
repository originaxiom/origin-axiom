"""B1820 -- the census's curvature along Re tau and its refinement list: the committed aggregates are consistent and came
from the committed tool, which reuses B1819's check against the manifest on record."""
import json, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[1]
V = ROOT / "frontier" / "B1820_the_rigid_censuss_curvature_along_re_tau" / "verification"


def test_the_aggregates_are_consistent():
    d = json.loads((V / "refinement_list.json").read_text(encoding="utf-8"))
    assert d["aggregates_and_indices_only"] is True and "256 files match the recorded manifest" in d["input"]
    a = d["second_difference_log10_along_re_per_mean_step"]; qs = [a["q50"], a["q90"], a["q99"], a["q99.9"], a["max"]]
    assert qs == sorted(qs) and 0.05 < d["fraction_re_above_threshold"] < 0.10
    assert len(d["refinement_list"]) == 256 and sum(d["per_line_interval_counts"].values()) == d["totals"]["im_intervals"] + d["totals"]["re_intervals"]
    assert "exit 0" in (V / "refinement_list_run.txt").read_text(encoding="utf-8")


def test_the_tool_reuses_the_recorded_manifest_check():
    src = (ROOT / "scripts" / "census" / "rigid_census_refinement_list.py").read_text(encoding="utf-8")
    assert "from rigid_census_smoothness_map import manifest_ok" in src and "REFUSED" in src
