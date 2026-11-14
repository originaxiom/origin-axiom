"""B1941's lock: the kept run shows the log-determinant positive (W- preferred) at every sampled point under every declared
change but the functional, and the one-loop trace negative at every point; the page states the same counts."""
import re, pathlib
HERE = pathlib.Path(__file__).resolve().parent


def test_the_kept_run_and_the_page_agree():
    t = (HERE / "s4_pointwise_run.txt").read_text()
    rows = {m.group(1).strip(): (int(m.group(2)), int(m.group(3))) for m in re.finditer(r"^(.+?)\s+positive at\s+(\d+) of (\d+) points", t, re.M)}
    assert len(rows) == 8
    for k, (p, n) in rows.items():
        assert n == 28
        assert p == (28 if k.startswith("ln det") else 0), k
    f = (HERE.parent / "FINDINGS.md").read_text()
    assert "**28 of 28**" in f and "**0 of 28**" in f
