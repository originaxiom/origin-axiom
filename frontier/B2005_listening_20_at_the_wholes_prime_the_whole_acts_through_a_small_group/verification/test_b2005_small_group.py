"""B2005's lock: the fast levels of the group run rerun exactly; the committed runs hold the page's table."""
import pathlib, re, subprocess, sys
HERE = pathlib.Path(__file__).resolve().parent


def test_fast_levels_rerun():
    code = (HERE / "small_group.py").read_text().replace("for k in (2, 3, 4, 5):", "for k in (2, 3, 4):").replace("HERE = pathlib.Path(__file__).resolve().parent", "HERE = pathlib.Path(%r)" % str(HERE))
    out = subprocess.run([sys.executable, "-B", "-c", code], capture_output=True, text=True, timeout=900).stdout
    strip = lambda s: [l.split("  [")[0] for l in s.splitlines()]
    want = strip((HERE / "small_group_run.txt").read_text())[:7]
    assert strip(out) == want


def test_tables():
    t = (HERE / "small_group_run.txt").read_text()
    assert "|G_k| = 216" in t and "|G_k| = 1944" in t and "|G_k| = 52488" in t and "stabiliser of (3,3,3) has order 9" in t
    assert t.count("rho factors through G_k (labels consistent): True") == 3 and t.count("rho factors through G_k (labels consistent): False") == 1
    assert "{1: 1, 2: 9, 3: 8, 4: 6}: True" in t
    a = (HERE / "abelian_posthoc_run.txt").read_text()
    assert a.count("abelianisation order 2; 6 divides it: False") == 6
