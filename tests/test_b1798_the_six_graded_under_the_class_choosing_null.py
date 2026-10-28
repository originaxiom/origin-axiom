"""B1798 -- the six graded under the class-choosing null (R71-1).  The committed runs: the class-choosing null's counts and
r for B1753 and B1749; main's checks; the referee's c-choosing null, every variant above THE_BAR; the census extension's
stored hashes."""
import hashlib, gzip, pathlib, re
ROOT = pathlib.Path(__file__).resolve().parents[1]
V = ROOT / "frontier" / "B1798_the_six_graded_under_the_class_choosing_null" / "verification"


def test_the_class_choosing_null():
    a = (V / "analysis_b1753_all.txt").read_text(encoding="utf-8")
    assert "10000000 targets" in a and "hits   2058  frac 2.0580e-04  r97.5 2.1489e-04" in a
    b = (V / "analysis_b1749.txt").read_text(encoding="utf-8")
    assert "hits   2749  frac 2.7490e-04  r97.5 2.8537e-04" in b


def test_mains_checks():
    m = (V / "main" / "main_check_run.txt").read_text(encoding="utf-8")
    assert "max |stored - recomputed| = 0.000e+00" in m and "direct hits 10, KD hits 10" in m
    t = (V / "main" / "tail_check_run.txt").read_text(encoding="utf-8")
    assert "max |stored - recomputed| = 0.000e+00" in t


def test_the_c_choosing_null_fails_the_bar():
    for f in ("cnull_b1753_gjset.txt", "cnull_b1753_set.txt", "cnull_b1753_bounded.txt", "cnull_b1749_gjset.txt", "cnull_b1749_set.txt", "cnull_b1749_bounded.txt"):
        t = (V / "referee" / f).read_text(encoding="utf-8")
        line = [l for l in t.splitlines() if l.startswith("c-choosing")][0]
        mr = float(re.search(r"m\*r\(41\) ([0-9.]+)", line).group(1))
        assert mr > 0.01, (f, mr)


def test_the_extension_hashes():
    raw = dict(l.split()[::-1] for l in (V / "b1753_all266" / "RAW_SHA256.txt").read_text(encoding="utf-8").splitlines())
    for name in ("census_ext.jsonl", "census_ext_tail.jsonl"):
        h = hashlib.sha256(gzip.open(V / "b1753_all266" / (name + ".gz")).read()).hexdigest()
        assert h == raw["b1753_all266/" + name]
