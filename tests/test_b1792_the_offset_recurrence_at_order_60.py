"""B1792 -- the offset recurrence at order 60.  The committed comparison (38c4a3bd6, read once): R_a fails (six of the eight
predicted lines carry; the pair 1/60-7/12 does not), R_b holds (no other line carries), the controls hold; the instruments are
the sealed ones, compare.py with its one recorded fix."""
import hashlib, json, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[1]
A = ROOT / "frontier" / "B1792_the_offset_recurrence_at_order_60"
V = A / "verification"


def test_the_cells_as_committed():
    d = json.loads((V / "comparison.json").read_text(encoding="utf-8"))
    c = d["cells"]
    assert c["R_a_DECISIVE_every_predicted_line_carries"] is False and c["R_b_DECISIVE_no_other_line_carries"] is True
    assert c["C1_control"] is True and c["C2_control_chi2_reproduces_B1735"] is True
    assert sorted(d["predicted_carrying"]) == sorted(["11/12", "29/60", "41/60", "47/60", "49/60", "7/60"]) and d["other_carrying"] == []
    pl = {v["b"]: v["chi2_six_seat"] for v in d["readout_per_line"].values()}
    assert pl["1/60"] > 30 and pl["7/12"] > 30 and min(v for b, v in pl.items() if b not in d["predicted"]) > 16.75


def test_the_instruments():
    lines = [l.split() for l in (A / "ARTIFACT_HASHES.txt").read_text(encoding="utf-8").splitlines() if l and not l.startswith("#")]
    pins = {}
    for h, p in lines: pins.setdefault(p, []).append(h)
    assert hashlib.sha256((V / "census.py").read_bytes()).hexdigest() == pins["verification/census.py"][0]
    assert hashlib.sha256((V / "compare.py").read_bytes()).hexdigest() == pins["verification/compare.py"][-1]   # the recorded fix
