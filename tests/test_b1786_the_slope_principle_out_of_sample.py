"""B1786 -- the slope principle out of sample.  The committed comparison (c31c4d0e1, read once): the decisive cell D holds
(the 30 slope-2/5 lines at 8 of 160 000 random hierarchies, no other slope below 16.75), P1 and both controls hold; the
census is committed gzipped with the raw file's sha256; the sealed instruments match ARTIFACT_HASHES."""
import gzip, hashlib, json, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[1]
A = ROOT / "frontier" / "B1786_the_slope_principle_out_of_sample"
V = A / "verification"


def test_the_cells_as_committed():
    d = json.loads((V / "comparison.json").read_text(encoding="utf-8"))
    c = d["cells"]
    assert c["D_DECISIVE_slope_two_fifths_specific_at_0.1pc_and_no_other_slope_below_16.75"] is True
    assert c["P1_chi2_six_below_16.75_on_slope_two_fifths"] is True
    assert c["C1_control"] is True and c["C2_control_chi2_reproduces_B1735"] is True
    assert c["readout_slope_one_tenth_below_16.75"] is False and c["readout_nine_below_21.67_on_slope_two_fifths"] is False
    assert d["counts"] == {"a2/5": 30, "a1/10": 20, "rest": 538, "all": 588} and d["other_slopes_below_16.75"] == []
    pl = d["readout_per_line"].values()
    assert sum(1 for r in pl if r["alpha"] == "2/5" and r["chi2_six_seat"] < 16.75) == 12
    assert min(r["chi2_six_seat"] for r in pl if r["alpha"] != "2/5") > 100
    run = (V / "compare_run.txt").read_text(encoding="utf-8")
    assert "a2/5   chi2 six|seat   min 3.00, random as low 0.00005 (worst seed 0.00025, hits 8)" in run


def test_the_instruments_and_the_census_are_the_sealed_ones():
    pins = {}
    for line in (A / "ARTIFACT_HASHES.txt").read_text(encoding="utf-8").splitlines():
        parts = line.split()
        if len(parts) == 2 and len(parts[0]) == 64: pins[parts[1]] = parts[0]
    for rel in ("verification/census.py", "verification/compare.py"):
        assert hashlib.sha256((A / rel).read_bytes()).hexdigest() == pins[rel]
    want = (V / "census.jsonl.sha256").read_text(encoding="utf-8").split()[0]
    h = hashlib.sha256()
    with gzip.open(V / "census.jsonl.gz", "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""): h.update(chunk)
    assert h.hexdigest() == want


def test_the_class_choosing_null_decides_the_grade():
    """main's referee (verification/referee/kd_analysis.txt, prior_conditional.txt): on 10 million fresh targets the
    class-choosing form of D gives m*r 0.0112 at m = 41 and 0.0199 at 73; the prior-chosen class, conditional, 0.0099 and
    0.0177 -- on the gate at 41, failing at 73: not PASSED."""
    kd = (V / "referee" / "kd_analysis.txt").read_text(encoding="utf-8").split("== fresh10M")[1]
    line = next(l for l in kd.splitlines() if l.startswith("CLASS-CHOOSING"))
    assert "hits  2618" in line and "m*r(41) 0.0112" in line and "m*r(73) 0.0199" in line
    pc = (V / "referee" / "prior_conditional.txt").read_text(encoding="utf-8")
    assert "m*r(41) 0.0099  m*r(73) 0.0177" in pc


def test_the_grade_setting_readouts_have_a_committed_producer():
    """the web seat's checking pass: analyse_kd.py (committed) reproduces the class-choosing and prior-chosen rows exactly"""
    run = (V / "referee" / "analyse_kd_run.txt").read_text(encoding="utf-8").split("== fresh10M")[1]
    assert "hits  2618" in run and "m*r(41) 0.0112" in run
    assert "PRIOR-CHOSEN, unconditional" in run and "hits  1127" in run and "m*r(41) 0.0099" in run
    assert "targets      827  25/30 event follows   107" in run
