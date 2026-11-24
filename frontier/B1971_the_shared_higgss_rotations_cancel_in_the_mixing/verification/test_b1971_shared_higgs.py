"""B1971's lock: the exact identities (rerun), and the committed runs read for the numbers the page states.
Each check can fail: a changed sign in I3, a rate off its stated rational by more than 5e-3, an aligned point on the line
a = 1/2, or a census count that moves."""
import pathlib, re, subprocess, sys, json
HERE = pathlib.Path(__file__).resolve().parent


def test_identities_rerun_and_hold():
    out = subprocess.run([sys.executable, "-B", str(HERE / "identities.py")], capture_output=True, text=True, timeout=300).stdout
    assert out.count("True") == 7 and "False" not in out, out
    assert out == (HERE / "identities_run.txt").read_text()


def _rates():
    t = (HERE / "rates_run.txt").read_text()
    blocks = dict(re.findall(r"== (\w+) .*?\n(.*?)(?=\n== |\Z)", t, re.S))
    res = {}
    for name, body in blocks.items():
        rows = [list(map(float, re.findall(r"-?\d+\.\d+", l.split("|V| at")[0].split("rates:")[1]))) for l in body.splitlines() if l.strip().startswith("|V| row")]
        J = float(re.search(r"\|J\| rate:\s+(-?\d+\.\d+)", body).group(1))
        res[name] = (rows, J)
    return res


def test_wd2_table_reproduced():
    R = _rates()
    want = {"mark": (0.6, 0.3, 1.1, 2.0), "twin": (0.9, 0.1, 1.0, 2.2)}
    for name, (v12, v23, v13, J) in want.items():
        rows, j = R[name]
        assert abs(rows[0][1] - v12) < 5e-3 and abs(rows[1][2] - v23) < 5e-3 and abs(rows[0][2] - v13) < 5e-3 and abs(j - J) < 5e-3, (name, rows, j)


def test_cancelled_entries_fall_faster_than_naive():
    R = _rates()
    rows_m, _ = R["mark"]; rows_t, _ = R["twin"]
    assert rows_m[0][2] > 1.0 and rows_m[2][0] > 0.85          # naive 0.5 at the mark
    assert rows_t[0][1] > 0.85 and rows_t[0][2] > 0.95 and rows_t[2][0] > 1.15   # naive 0.5 to 0.6 at the twin


def test_higgs_nullity_is_b1739s():
    t = (HERE / "invariants_run.txt").read_text()
    vals = [complex(v.replace(" ", "")) for v in re.findall(r"h\.h / \(eta\^6/4\) = \(?([^)\n]+)\)?", t)]
    assert len(vals) == 8 and all(abs(v - 1) < 1e-30 for v in vals), vals


def test_census():
    s5 = (HERE / "bits_run_30_5.txt").read_text(); s810 = (HERE / "bits_run_30_8_10.txt").read_text()
    assert "SUMMARY: 24 points (0 errors); assignments agree at 24; of those aligned (diag >= 0.9): 24; of the others aligned: 0" in s5
    assert "SUMMARY: 112 points (0 errors); assignments agree at 110; of those aligned (diag >= 0.9): 104; of the others aligned: 0" in s810
    assert "the points not aligned all have a = 1/2: True; the points with a = 1/2: 8" in s810
    rows = json.loads((HERE / "bits_run_30_8_10.json").read_text())
    assert not [r for r in rows if r["a"] == "1/2" and r["diag"] >= 0.9]
