"""B1718 -- the running allowance (P-265). Stored: the factors and the 1e8 coverage; live: the one-loop run re-done at
1e16 GeV from the pinned masses reproduces the stored factors."""
import importlib.util, io, contextlib, json, math, pathlib
A = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B1718_the_running_allowance" / "verification"


def test_stored():
    d = json.loads((A / "the_running_allowance.json").read_text(encoding="utf-8"))
    f = d["scales"]["1e+16"]["factors"]
    assert abs(f["c/t"] - 0.884) < 0.002 and abs(f["s/b"] - 1.131) < 0.002 and abs(f["mu/tau"] - 1) < 1e-3
    assert 0.12 < d["largest_abs_log_to_1e16"] < 0.13 and 4e10 < d["allowance_0.10_covers_up_to_GeV"] < 7e10


def test_live():
    spec = importlib.util.spec_from_file_location("b1718", A / "the_running_allowance.py")
    m = importlib.util.module_from_spec(spec)
    with contextlib.redirect_stdout(io.StringIO()):
        spec.loader.exec_module(m)
    f, yt = m.factors(1e16, m.G0)
    stored = json.loads((A / "the_running_allowance.json").read_text(encoding="utf-8"))["scales"]["1e+16"]["factors"]
    assert all(abs(f[k] - stored[k]) < 1e-9 for k in f) and 0.43 < yt < 0.46
