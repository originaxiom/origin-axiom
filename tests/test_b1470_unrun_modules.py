"""B1470 -- the unrun modules run on main: no three on t12835."""
import json, os, subprocess, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
V = os.path.join(ROOT, "frontier", "B1470_the_unrun_modules_run_on_main", "verification")


def test_compare_live_on_the_stored_results():
    r = subprocess.run([sys.executable, os.path.join(V, "compare.py")], capture_output=True, text=True)
    assert r.returncode == 0 and "VERDICT t12835-complete: PASS" in r.stdout, r.stdout[-400:] + r.stderr[-300:]
    d = json.load(open(os.path.join(V, "compare.json")))
    assert d["modules"] == 6435 and d["not_run"] == 0 and d["agree_with_b1418_on_run"] == 3110 and d["agree_with_xB031"] == 6435
    assert d["I_values"] == {"0": 6003, "-1": 252, "1": 156, "-2": 24} and not d["any_three"] and d["max_abs_I"] == 2
