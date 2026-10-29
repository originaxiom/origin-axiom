"""B1813 -- the weave's own measure depends on how its threads are counted: the committed tables."""
import json, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[1]
V = ROOT / "frontier" / "B1813_the_weaves_own_measure_depends_on_how_its_threads_are_counted" / "verification"


def test_the_two_counts_and_the_family():
    a = json.loads((V / "stage1_threads_measure.json").read_text(encoding="utf-8"))
    assert a["classes"] == 2536 and abs(a["P(Im tau > Y)"]["3.0"]["geodesics (arclength)"] - 0.0346) < 0.001
    b = json.loads((V / "stage1b_by_trace.json").read_text(encoding="utf-8"))
    assert b["30"]["classes"] == 151 and b["30"]["P(Im tau > Y)"]["3.0"] > 0.25
    c = json.loads((V / "stage1c_two_clocks.json").read_text(encoding="utf-8"))
    row = c["n = 14 (threads of exactly that length: 1161)"]
    vals = [row[s]["3.0"] for s in ("0.0", "0.25", "0.5", "0.75", "1.0")]
    assert vals == sorted(vals) and vals[0] < 0.04 < 0.2 < vals[-1]
