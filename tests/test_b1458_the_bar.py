"""B1458 -- the bar adopted, and what the own-level law is not."""
import json, os, subprocess, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
A = os.path.join(ROOT, "frontier", "B1458_the_bar_adopted_and_the_own_level_law")


def test_the_strata_live():
    r = subprocess.run([sys.executable, os.path.join(A, "verification", "own_level_strata.py")], capture_output=True, text=True)
    assert r.returncode == 0 and "VERDICT own-level-strata: PASS" in r.stdout, r.stdout[-400:]
    d = json.load(open(os.path.join(A, "verification", "own_level_strata.json")))
    assert (d["manifolds"], d["firing_manifolds"], d["mixed_strata"]) == (536, 87, 22) and d["pairs_agree"]
    assert d["smallest_mixed"] == {"stratum": "((1, 12), '-')", "firing": "-LLRLR", "silent": "-LLLLLLLLR"}
    assert d["m369"]["G"] == d["o9_00001"]["G"] == "(1, 12)" and d["m369"]["backgrounds"] == 8 and d["o9_00001"]["backgrounds"] == 0


def test_the_bar_is_on_main_and_the_page_points_to_it():
    b = open(os.path.join(ROOT, "docs", "THE_BAR.md")).read()
    assert "Adopted on main 2026-10-03 (B1458)" in b and "UNJUDGED" in b and "p < 0.01" in b and "this seat's proposal" not in b
    g = open(os.path.join(ROOT, "GENESIS.md")).read()
    import re
    v = re.search(r"\*\*Version 1\.(\d+) ·", g); assert v and int(v.group(1)) >= 4   # at v1.4 or a later version that keeps the log line
    assert "- **v1.4 · 2026-10-03 · main B1458.**" in g and "`docs/THE_BAR.md` (**[v1.4]** on main from B1458)" in g
    assert "not yet on main" not in g.split("## 10.")[0].split("THE_BAR")[-1][:80]
    r = open(os.path.join(ROOT, "README.md")).read()
    assert "## The state of the programme (as of B1458, 2026-10-03)" in r and "## The state as it was written at B1134 (2026-08-22)" in r
