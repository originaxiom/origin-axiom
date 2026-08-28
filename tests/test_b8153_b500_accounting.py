"""Lock: B500's depth-5 partition, and that the obstruction method was proved vacuous."""
import json, pathlib, re, itertools
ROOT = pathlib.Path(__file__).resolve().parents[1]
R = json.loads((ROOT / "frontier/B8153_b500_accounting/results.json").read_text())
LOG = ROOT / "frontier/B500_child_hunt/hunt_results_d5.txt"

def test_the_partition_sums_to_150():
    a = R["the_accounting"]
    assert a["completed_with_a_verdict"] + a["timed_out"] + a["never_reached"] == 150

def test_the_nine_never_reached_are_really_absent_from_the_log():
    seen = set(re.findall(r"^([FMD]{5}):", LOG.read_text(), re.M))
    words = [''.join(w) for w in itertools.product('FMD', repeat=5) if set(w) == set('FMD')]
    assert sorted(set(words) - seen) == sorted(R["the_accounting"]["never_reached_words"])

def test_no_airlock_in_the_banked_log():
    assert "AIRLOCK" not in LOG.read_text()

def test_the_obstruction_method_is_recorded_as_vacuous():
    m = R["my_failed_method"]
    assert m["verdict"].startswith("VACUOUS")
    assert "x^29-x-1" in m["the_bite_control"]

def test_my_process_error_is_recorded():
    assert "PRESENTED INCONCLUSIVE RESULTS before" in R["my_failed_method"]["my_process_error"]

def test_nothing_is_claimed_for_the_unfinished_run():
    assert any("the run is still going" in x for x in R["not_claimed"])
