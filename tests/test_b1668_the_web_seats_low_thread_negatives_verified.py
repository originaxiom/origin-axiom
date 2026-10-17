"""B1668 -- the web seat's low-thread negatives, verified on main. The verification's stored logs: the seeded sample of six
configurations re-executes bit-identically; main's own scorers find no S-mass pass in either result, with the headline
numbers; the verdict is NEGATIVE and routed into the kill graph. The bite: a log that reported a difference, or a pass,
would fail these asserts."""
import json, pathlib, re
ROOT = pathlib.Path(__file__).resolve().parents[1]
A = ROOT / "frontier" / "B1668_the_web_seats_low_thread_negatives_verified"
V = A / "verification"


def test_reexecution_bit_identical():
    txt = (V / "repro_run_35.txt").read_text() + (V / "repro_run_23.txt").read_text()
    idx = sorted(int(m) for m in re.findall(r"^idx (\d+)", txt, re.M))
    assert idx == sorted([35, 3, 56, 23, 84, 15])
    assert txt.count("differing 0 max rel diff (any) 0.0") == 6 and "differing 1" not in txt


def test_rescore_no_pass_and_headlines():
    a = (V / "score_mine_tu_run.txt").read_text()
    b = (V / "score2_mine_run.txt").read_text()
    assert a.count("total mass passes (any assignment) 0") == 2            # per-field and minimal
    assert "claim mass per-field all (0," in a and "claim mass minimal all (0," in a
    nums = lambda pat, t: [float(x) for x in re.findall(pat, t)]
    sm = nums(r"SM best chi2 \(([0-9.]+)", a); nl = nums(r"best null ([0-9.]+)", a)
    assert [round(x, 2) for x in sm] == [983.26, 601.77] and [round(x, 2) for x in nl] == [267.32, 471.29]
    assert b.count("passes SM 0 nulls total 0") == 2                       # the mid-height scan and the replication
    smb = nums(r"SM best \(([0-9.]+)", b); nlb = nums(r"best null \(([0-9.]+)", b)
    assert [round(x, 1) for x in smb] == [28281.0, 578.2] and [round(x, 1) for x in nlb] == [14482.6, 262.9]


def test_verdict_and_routing():
    v = json.load(open(A / "arc_verdict.json"))
    assert v["verdict"] == "NEGATIVE" and v["id"] == "B1668"
    k = json.load(open(ROOT / "frontier" / "B738_pathfinder_compiler" / "kill_graph.json"))
    assert any(e.get("id") == "B1668" for e in k)
