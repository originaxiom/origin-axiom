"""B1696 -- tau is the state's own cusp shape (P-244), sealed 1a3f6e2aa, NEGATIVE as sealed. Live: the comparison re-run from
the stored rows and the pinned data reproduces the three failures (best worst factor 3.56; 26.8% of random hierarchies fit
as well; chi2 317). Stored: tau = 2 sqrt3 i; the seal's hashes."""
import hashlib, importlib.util, io, contextlib, json, math, pathlib
A = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B1696_tau_is_the_cusp_shape"


def test_the_three_failures_live():
    spec = importlib.util.spec_from_file_location("b1696_compare", A / "verification" / "compare.py")
    m = importlib.util.module_from_spec(spec)
    with contextlib.redirect_stdout(io.StringIO()):
        spec.loader.exec_module(m)
    o = m.out
    assert not o["H1_within_factor_3"] and not o["H2_specific_p_below_0.01"] and not o["H3_chi2_below_16.75"]
    assert abs(o["best_by_worst_factor"]["worst_factor"] - 3.56) < 0.01 and abs(o["calibration"]["fraction_fit_as_well"] - 0.268) < 1e-9


def test_tau_and_the_seal():
    d = json.loads((A / "verification" / "the_cusp_tau.json").read_text(encoding="utf-8"))
    assert abs(d["tau"][1] - 2 * math.sqrt(3)) < 1e-12 and d["tau"][0] == 0.0 and len(d["rows"]) == 97
    for name in ("the_cusp_tau.py", "compare.py", "b1656_funcs.py"):
        h = hashlib.sha256((A / "verification" / name).read_bytes()).hexdigest()
        assert h in (A / "ARTIFACT_HASHES.txt").read_text(encoding="utf-8")
    assert hashlib.sha256((A / "PREREGISTRATION.md").read_bytes()).hexdigest().startswith("6481d943")
