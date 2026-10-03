"""B1465 -- the mirror-broken states at their complete points: no count for any character, the meridian twist included."""
import json, os, subprocess, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
A = os.path.join(ROOT, "frontier", "B1465_the_mirror_broken_states_at_their_complete_points"); V = os.path.join(A, "verification")


def test_the_record_of_the_four_states():
    tot = 0
    for s, N, pts in (("pLLRLRR", 13, 12), ("mLLRLRR", 17, 12), ("pLLLRLRR", 18, 14), ("mLLLRLRR", 22, 20)):
        d = json.load(open(os.path.join(V, "points_%s.json" % s)))
        rows = [r for p in d["points"] for r in p["rows"]]
        assert d["N"] == N and len(d["points"]) == pts and d["nonzero"] == [] and not any("error" in r for r in rows)
        assert len({r["lam"] for r in rows}) == 7 and all(r["I"] == 0 for r in rows)
        assert all(float(r["gap"][0]) > 1e-5 and float(r["gap"][1]) < 1e-40 for r in rows)
        tot += len(rows)
    assert tot == 7364


def test_quick_live_on_one_curve():
    r = subprocess.run([sys.executable, os.path.join(V, "mirror_broken_complete_points.py"), "+LLRLRR", "--quick"], capture_output=True, text=True, cwd=V)
    assert r.returncode == 0 and "rows 26 nonzero 0" in r.stdout, r.stdout[-300:] + r.stderr[-300:]
    q = json.load(open(os.path.join(V, "points_pLLRLRR_quick.json"))); assert q["rows"] == 26 and q["nonzero"] == []
