"""B1424 lock -- the outside referee's defects, verified and fixed.

(1) the census drift, recomputed on BOTH populations: steep on the full orientable cusped census,
    flat on the one-cusped census the paper's paragraph is about;
(2) the evidence file four locks read is tracked, and the gitignore negation that keeps it tracked is present
    -- this is the defect that made the shipped package unpassable on a clean checkout;
(3) the paper carries the corrected percentage and both triples.
"""
import json
import pathlib
import subprocess

ROOT = pathlib.Path(__file__).resolve().parents[1]
D = ROOT / "frontier" / "B1424_the_referees_defects" / "verification"


def _tracked(rel):
    r = subprocess.run(["git", "ls-files", "--error-unmatch", rel], cwd=ROOT,
                       capture_output=True, text=True)
    return r.returncode == 0


def test_the_census_evidence_four_locks_read_is_tracked():
    rel = "frontier/B1419_the_arithmetic_fillings_corrected/verification/arithmetic_census_closed.jsonl"
    assert (ROOT / rel).exists(), "the census evidence is missing"
    assert _tracked(rel), "untracked: the four B1419 locks cannot pass on a clean checkout"


def test_the_gitignore_negation_is_present():
    s = (ROOT / ".gitignore").read_text()
    assert "!frontier/B1419_the_arithmetic_fillings_corrected/verification/*.jsonl" in s


def test_the_drift_is_steep_on_the_full_census_and_flat_on_the_one_cusped():
    res = json.loads((D / "drift_population.json").read_text())
    full = {r["lo"]: r["rate"] for r in res["full orientable cusped"]}
    one = {r["lo"]: r["rate"] for r in res["one-cusped only"]}
    assert full[0] > 34 and full[80000] < 22               # the decline the paper had quoted
    assert full[0] - full[80000] > 12                       # steep
    assert one[0] > 32 and one[80000] > 30                  # and it is NOT there on one cusp
    assert abs(one[0] - one[80000]) < 3                     # flat to within a couple of points


def test_a_second_method_agrees():
    gap = json.loads((D / "drift_gap.json").read_text())
    one = {r["lo"]: r["rate"] for r in gap["one-cusped"]}
    full = {r["lo"]: r["rate"] for r in gap["full"]}
    assert abs(one[0] - 33.00) < 0.6 and abs(one[80000] - 31.38) < 0.6
    assert abs(full[80000] - 21.12) < 0.6


def test_the_paper_states_both_populations_and_the_corrected_percentage():
    t = (ROOT / "papers" / "P3_THE_PAPER" / "main.tex").read_text()
    assert "33.00\\% \\to 33.88\\% \\to 31.38\\%" in t
    assert "34.25\\% \\to 29.38\\% \\to 21.12\\%" in t
    assert "0.9\\%$, about fifty experimental" not in t     # the overstated miss is gone
    assert "$0.8\\%$, about fifty experimental" in t
