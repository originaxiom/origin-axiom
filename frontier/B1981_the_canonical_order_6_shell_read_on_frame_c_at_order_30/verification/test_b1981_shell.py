"""B1981's lock: the committed runs hold the page's outcomes. Fails if a block's rates fall on one of the 12 classes, if
the linear reading becomes aligned at every block, or if the post hoc Gramian rates move off m2/m3 0 and m1/m3 1."""
import pathlib, re
HERE = pathlib.Path(__file__).resolve().parent


def test_sealed_outcomes():
    t = (HERE / "shell_run.txt").read_text()
    assert "SUMMARY H3 L: each block's rates equal one of B1979's 12 classes: False (class per block [None, None, None, None])" in t
    assert "SUMMARY H3 G: each block's rates equal one of B1979's 12 classes: False (class per block [None, None, None, None])" in t
    assert "SUMMARY H5 L: every block aligned at 50 and hierarchical in both quark sectors: False" in t
    assert "SUMMARY H2 L: full rank (every mass rate finite and below 3) in every block: True" in t
    d = [float(x) for x in re.findall(r"^L p5=\S+\s+40-50: .*\| diag50 ([\d.]+)", t, re.M)]
    assert len(d) == 4 and max(d) < 0.9, d
    v23 = [float(x) for x in re.findall(r"^L p5=\S+\s+40-50: .* V23=(-?[\d.]+)", t, re.M)]
    assert len(v23) == 4 and all(abs(x) < 1e-3 for x in v23), v23


def test_posthoc_gramian():
    t = (HERE / "g_precision_posthoc_run.txt").read_text()
    pairs = re.findall(r"m2/m3 (-?[\d.]+) (-?[\d.]+) m1/m3 (-?[\d.]+) (-?[\d.]+)", t)
    assert len(pairs) == 15
    assert all(abs(float(a)) < 1e-3 and abs(float(b)) < 1e-3 and abs(float(c) - 1) < 1e-3 and abs(float(d) - 1) < 1e-3 for a, b, c, d in pairs)
