"""B1481 -- the hand is a phase: the stored run re-read state by state against the four sealed predictions (three hold,
one fails and must stay failed), with the reading function shown able to fail, and the two controls live."""
import json, os, sys, math
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
V = os.path.join(ROOT, "frontier", "B1481_the_hand_is_a_phase", "verification")
sys.path.insert(0, V)


def test_the_four_predictions_on_the_stored_run():
    import hand_phase as H
    d = json.load(open(os.path.join(V, "hand_phase.json"))); st = d["states"]; s = d["summary"]
    assert s["states"] == 68 and s["errors"] == {}
    minus = [r for n, r in st.items() if n.startswith("b+-")]; plus = [r for n, r in st.items() if n.startswith("b++")]
    assert len(minus) == len(plus) == 34 and sum(len(r["rows"]) for r in minus) == 152
    for t in ("2", "3", "0.6", "1"):
        for r in minus:
            n, special, paired = H.read(r, t); assert special == 0 and paired is True, (r["name"], t)
    for r in plus:
        n, special, paired = H.read(r, "2"); assert special >= 2 and paired is False, r["name"]
    # P4 fails and stays failed: only m003's two phases are on the pi/24 lattice
    on = [(r["name"], row["theta"]["1"]) for r in minus for row in r["rows"] if abs(row["theta"]["1"] * 24 / math.pi - round(row["theta"]["1"] * 24 / math.pi)) < 1e-7]
    assert sorted(n for n, _ in on) == ["b+-LR", "b+-LR"] and sorted(round(x * 3 / math.pi) for _, x in on) == [1, 2]
    # the reading can fail: a state with a planted real phase is neither special-free nor paired
    fake = dict(rows=[dict(theta={"2": 0.0}), dict(theta={"2": 1.0})]); assert H.read(fake, "2")[1] == 1 and H.read(fake, "2")[2] is False


def test_the_two_controls_live():
    """run in a fresh interpreter: B1476's census_swap replaces realness.setup at import, so inside a shared test process
    the order of earlier imports decides which setup B1477's module captured (found by S63's first suite)"""
    import subprocess
    code = ("import sys, json; sys.path.insert(0, %r); import hand_phase as H; "
            "print(json.dumps([H.one('b++LR'), H.one('b+-LR')]))" % V)
    out = subprocess.run([sys.executable, "-c", code], capture_output=True, text=True, timeout=600)
    a, b = json.loads([l for l in out.stdout.splitlines() if l.startswith("[")][-1])
    import hand_phase as H
    assert all(H.special(row["theta"]["2"]) for row in a["rows"])
    th = sorted(row["theta"]["1"] for row in b["rows"]); assert abs(th[0] - math.pi / 3) < 1e-7 and abs(th[1] - 2 * math.pi / 3) < 1e-7
    assert H.read(b, "2") == (2, 0, True)
