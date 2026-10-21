"""B1694 -- the parameter-free curve (P-242), sealed 90edb73e3. Live: the comparison re-run from the stored curves and the
pinned data reproduces the grades; the bite: with a tolerance of 50 instead of 3 every sector passes every curve, so the
outcome rests on the stated tolerance. Stored: the curves' monotonicity and range; the seal's hashes."""
import hashlib, importlib.util, io, contextlib, json, pathlib
A = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B1694_the_parameter_free_curve"


def _cmp(tol=None):
    spec = importlib.util.spec_from_file_location("b1694_compare", A / "verification" / "compare.py")
    m = importlib.util.module_from_spec(spec)
    with contextlib.redirect_stdout(io.StringIO()):
        spec.loader.exec_module(m)
    return m


def test_the_grades_live_and_the_bite():
    m = _cmp(); out = m.out
    stored = json.loads((A / "verification" / "comparison.json").read_text(encoding="utf-8"))
    for c in out["by_curve"]:
        for s in ("up", "down", "lepton"):
            assert out["by_curve"][c][s]["grade"] == stored["by_curve"][c][s]["grade"]
    assert out["some_curve_passes_all_three"] is False
    assert all(out["by_curve"][c]["up"]["grade"] == "PASS" for c in out["by_curve"])
    lo = min(out["by_curve"][c]["down"]["rho_3sigma"][0] for c in out["by_curve"])
    assert lo < 50                                                          # the bite: a tolerance of 50 would pass the down quarks


def test_the_curves_and_the_seal():
    d = json.loads((A / "verification" / "the_curve.json").read_text(encoding="utf-8"))
    for pts in d["curves"].values():
        r2 = [p["m2/m3"] for p in pts]; r1 = [p["m1/m3"] for p in pts]
        assert all(r2[i] > r2[i + 1] for i in range(len(r2) - 1)) and 0.4 < r2[0] < 0.7 and r2[-1] < 1e-3
        assert all(r1[i] > r1[i + 1] for i in range(1, len(r1) - 1)) and r1[1] / r1[0] < 1.02    # a flat start on the L_2 curves
    for name in ("the_curve.py", "compare.py", "b1656_funcs.py"):
        h = hashlib.sha256((A / "verification" / name).read_bytes()).hexdigest()
        assert h in (A / "ARTIFACT_HASHES.txt").read_text(encoding="utf-8")
    assert hashlib.sha256((A / "PREREGISTRATION.md").read_bytes()).hexdigest().startswith("a6d90f7e")
