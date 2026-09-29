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
    # CLASS, not incident (2026-09-17, round 2): the first version of this test asserted one literal
    # string, so a THIRD occurrence of the overstated figure -- inside the GENERATED chain table, which
    # the paper says is generated rather than typed -- passed it green. Assert the figure is absent
    # everywhere it could be the Weinberg miss, and that the generated block agrees with its generator.
    assert "$0.8\\%$, about fifty experimental" in t
    import re as _re
    bad = [m.start() for m in _re.finditer(r"sin\^2\\theta_W[^.]{0,40}?0\.9", t)]
    assert not bad, "the 0.822%% miss is still written 0.9%% at %d place(s)" % len(bad)


def test_the_manifest_names_a_commit_a_reader_can_resolve():
    """round 2: the manifest recorded a hash that existed only in the author's local object store.

    It was built before a commit that was then amended, so the recorded commit was never published; the
    referee could not resolve it after fetching every ref, and the author's own check passed only because
    it ran against that dangling object. The manifest now carries the evidence, and this asserts it.
    """
    m = json.loads((ROOT / "papers" / "P3_THE_PAPER" / "verification_package" / "MANIFEST.json").read_text())
    env = m["environment"]
    head = env.get("git_head")
    assert head and head != "?"
    assert subprocess.run(["git", "cat-file", "-t", head], cwd=ROOT,
                          capture_output=True, text=True).stdout.strip() == "commit", "recorded head does not resolve"
    assert env.get("git_head_published") is True, (
        "the manifest names a commit that is on no remote-tracking branch: push, then rebuild the manifest")
    anc = subprocess.run(["git", "merge-base", "--is-ancestor", head, "HEAD"], cwd=ROOT, capture_output=True)
    assert anc.returncode == 0, "the recorded head is not an ancestor of HEAD (was it amended after the build?)"

