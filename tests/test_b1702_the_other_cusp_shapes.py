"""B1702 -- the other cusp shapes (P-249), sealed f51ab2718, NEGATIVE as sealed. Live: the comparison re-run from the
stored rows and the pinned data reproduces H1, H2, H3 failing and the up quarks' floor. Stored: the seal's hashes."""
import hashlib, importlib.util, io, contextlib, pathlib
A = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B1702_the_other_cusp_shapes"


def test_the_cells_live():
    spec = importlib.util.spec_from_file_location("b1702_compare", A / "verification" / "compare.py")
    m = importlib.util.module_from_spec(spec)
    with contextlib.redirect_stdout(io.StringIO()):
        spec.loader.exec_module(m)
    o = m.out
    assert not o["H1_within_factor_3"] and not o["H2_specific_p_below_0.01"] and not o["H3_chi2_below_16.75"]
    assert abs(o["best_by_worst_factor"]["worst_factor"] - 8.948) < 0.01 and o["rows"] == 6912
    assert o["smallest_model_ratio_over_all_rows"]["up m2/m3"] > 0.0134


def test_the_seal():
    for name in ("the_cusp_shapes.py", "compare.py", "b1656_funcs.py"):
        h = hashlib.sha256((A / "verification" / name).read_bytes()).hexdigest()
        assert h in (A / "ARTIFACT_HASHES.txt").read_text(encoding="utf-8")
    assert hashlib.sha256((A / "PREREGISTRATION.md").read_bytes()).hexdigest().startswith("8f26df36")
