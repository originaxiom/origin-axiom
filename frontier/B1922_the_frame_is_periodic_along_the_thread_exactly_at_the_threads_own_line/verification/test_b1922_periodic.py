"""B1922's lock: the kept deviations say what the page says, and the symmetric window recomputed for the own line and
the other line. It writes nothing (only deviations are formed)."""
import sys, json, math, pathlib, warnings
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
warnings.simplefilter("ignore")
import periodic as P


def test_the_kept_run():
    d = json.loads((HERE / "periodic.json").read_text())
    own = [v for k, v in d.items() if "own line" in k]; other = [v for k, v in d.items() if "not fixed" in k]
    assert len(own) == 3 and len(other) == 3
    assert sorted(v["S, St"] for v in own)[1] < 1e-8 and min(v["S, St"] for v in other) > 1.0
    assert all(v["S*"] > 1.0 for v in own)


def test_the_symmetric_window_recomputed():
    r = P.deviations(-P.ell / 2, (0.4, 0.8)); q = P.deviations(-P.ell / 2, (0.2, 0.6))
    assert r["S, St"] < 1e-8 and q["S, St"] > 1.0                # planted alongside: a line the thread does not fix
