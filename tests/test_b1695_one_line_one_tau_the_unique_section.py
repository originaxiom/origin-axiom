"""B1695 -- one line, one tau, the unique section (P-243), sealed fc3bf0684. Live: the comparison re-run from the stored grid
and the pinned data reproduces G1 (fails) and G2 (passes, best worst-factor 1.788); the calibration after the seal
reproduces its two numbers (a wrong sector order fits better; 6.25% of random targets fit as well); the bite: with a
tolerance of 1.5 instead of 3, G2 fails. Stored: the seal's hashes."""
import hashlib, importlib.util, io, contextlib, json, pathlib
A = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B1695_one_line_one_tau_the_unique_section"


def _load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(spec)
    with contextlib.redirect_stdout(io.StringIO()):
        spec.loader.exec_module(m)
    return m


def test_the_comparison_live_with_the_bite():
    m = _load(A / "verification" / "compare.py", "b1695_compare"); out = m.out
    assert out["G1_pass"] is False and out["G2_pass"] is True and out["G2_points_within_factor_3"] == 29
    best = out["overall_min_chi2"]
    assert abs(best["worst_factor"] - 1.788) < 1e-3 and best["alpha_96ths"] == 37 and abs(best["Im_tau"] - 3.15) < 1e-9
    assert not any(h["worst_factor"] <= 1.5 for h in out["G2_examples"])              # the bite: a tolerance of 1.5 fails


def test_the_calibration_after_the_seal():
    c = json.loads((A / "verification" / "after_the_seal" / "calibration.json").read_text(encoding="utf-8"))
    assert c["true_order_best_worst_factor"] > min(v for k, v in c["sector_permutations_best_worst_factor"].items() if k != "udl")
    assert abs(c["random_targets"]["fraction_fit_as_well"] - 0.0625) < 1e-9


def test_the_seal():
    for name in ("the_grid.py", "compare.py", "b1656_funcs.py"):
        h = hashlib.sha256((A / "verification" / name).read_bytes()).hexdigest()
        assert h in (A / "ARTIFACT_HASHES.txt").read_text(encoding="utf-8")
    assert hashlib.sha256((A / "PREREGISTRATION.md").read_bytes()).hexdigest().startswith("aced715b")
