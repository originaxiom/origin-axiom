"""B1980's lock (part B's runs used a wrong end law and are kept as run; B1982 corrects them): part A reruns exactly (no interior fixed point, 48 act-fixed cusps equal to the 96 points); part B's
committed run holds no duality and the controls. Fails if a K passes, a control fails, or the cusp set moves."""
import pathlib, re, subprocess, sys
HERE = pathlib.Path(__file__).resolve().parent


def test_part_a_reruns():
    for name in ("act_level30", "cusps_are_the_points"):
        out = subprocess.run([sys.executable, "-B", str(HERE / (name + ".py"))], capture_output=True, text=True, timeout=300).stdout
        assert out == (HERE / (name + "_run.txt")).read_text()
    a = (HERE / "act_level30_run.txt").read_text()
    assert "SUMMARY A: no interior fixed point for k < 60: True; M fixes no cusp: True" in a and "cusps of X(30) (vectors of order 30 up to sign): 288" in a
    assert "SUMMARY: the cusps of X(30) fixed by a power of the act are exactly B1976's 96 points up to sign: True" in (HERE / "cusps_are_the_points_run.txt").read_text()


def test_part_b_no_duality():
    # Review 87: the S-move part of this run used the table outside its domain (withdrawn, B1982); held as run.
    t = (HERE / "duality_run.txt").read_text()
    assert "SUMMARY C0 passes: True; C1 passes: True" in t and "SUMMARY dualities passing (largest d < 1e-8 at both heights): []" in t
    big = [float(x) for x in re.findall(r"^K = \d+: .*largest d ([\d.e+-]+)", t, re.M)]
    assert len(big) == 20 and min(big) > 0.1, big
    w = (HERE / "s_wider_posthoc_run.txt").read_text()
    assert "control (same height 1.5, all 48 assignments): largest d 0.0e+00" in w
    ws = [float(x) for x in re.findall(r"^S move, .*largest d ([\d.e+-]+)", w, re.M)]
    assert len(ws) == 2 and min(ws) > 0.1, ws


def test_part_b_corrected_end():
    # Review 87 (2026-11-26): these asserts hold the record of runs made with a wrong end law (B1982 withdrew their S verdict);
    # they guard the runs' text as run, not a live claim about frame C, whose S-covariance B1982's own lock holds.
    t = (HERE / "duality_cov_run.txt").read_text()
    assert "SUMMARY K0 passes: True" in t and "SUMMARY S-cov (plain matching) passes: False" in t and "SUMMARY F-cov: K passing with the covariant end: []" in t
    s = [float(x) for x in re.findall(r"^S move, covariant end: .*largest d ([\d.e+-]+)", t, re.M)]
    assert len(s) == 3 and min(s) > 0.1, s
    w = (HERE / "s_wider_cov_run.txt").read_text()
    assert "all 48 assignments): largest d 0.0e+00" in w
    ws = [float(x) for x in re.findall(r"^S move, covariant end, wider matching: .*largest d ([\d.e+-]+)", w, re.M)]
    assert len(ws) == 3 and min(ws) > 0.1, ws
