"""B1811 -- the symmetry-selection values against the six (sealed; NEGATIVE as sealed): the committed comparison's cells."""
import json, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[1]
V = ROOT / "frontier" / "B1811_the_symmetry_selection_values_against_the_six" / "verification"


def test_the_sealed_cells():
    c = json.loads((V / "comparison.json").read_text(encoding="utf-8"))
    assert c["cells"]["DECISIVE_P1_and_P2_seat_0.1pc"] is False and c["cells"]["P1_chi2_six_below_16.75_seat"] is False
    assert c["cells"]["C1_control"] is True and c["cells"]["C2_control_chi2_reproduces_B1735"] is True
    assert c["chi2"]["six|seat"]["min"] > 1000


def test_the_decode_p517():
    """P-517 (2026-11-19): decode.py run live equals its committed output; it reads no measured value; the numbers FINDINGS
    states are the run's."""
    import subprocess, sys
    src = (V / "decode.py").read_text(encoding="utf-8")
    code = src.split('"""', 2)[2]
    assert "HZ2021" not in code and "B1637" not in code and "B1612" not in code and "compare" not in code
    out = subprocess.run([sys.executable, "-B", str(V / "decode.py")], capture_output=True, text=True, check=True).stdout
    assert out == (V / "decode_run.txt").read_text(encoding="utf-8")
    assert "D1 cells: 208; massless: 164; non-degenerate: 44" in out
    for cf, z, n in (("(i, 0)", 12, 40), ("(omega, 0)", 52, 0), ("(i, (1/2, 1/2))", 48, 4), ("(omega, (1/3, 2/3))", 52, 0)):
        assert "D1 split %s: massless %d, non-degenerate %d" % (cf, z, n) in out
    assert "(configuration, direction, reading) 22;" in out
    assert "c = 3: D = 9.000000000000; V_ud = 1.000000000000000" in out
    assert "D3 (i, 0) a_0 vs F_6: largest relative difference 2.352" in out
    small = float(out.split("D3 (i, (1/2, 1/2)) a_0 vs F_6: largest relative difference ")[1].split()[0]); assert small < 1e-12
    assert "D4 stored chi2_six minimum (seat): 4521.518" in out
    f = (V.parent / "FINDINGS.md").read_text(encoding="utf-8")
    assert "164 of the 208" in f and "(relative 2.35)" in f and "D = 9.0 (= c²)" in f and "the non-degenerate cells are 44" in f
