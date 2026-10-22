"""B1711 -- W59's order-9 lines at the band tau (P-256), sealed 6fee45181, NEGATIVE as sealed. Live: the comparison re-run
from the stored rows and the pinned data reproduces H1, H2, H3 failing. Stored: the seal's hashes."""
import hashlib, importlib.util, io, contextlib, pathlib
A = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B1711_the_order9_lines"


def test_the_cells_live():
    spec = importlib.util.spec_from_file_location("b1711_compare", A / "verification" / "compare.py")
    m = importlib.util.module_from_spec(spec)
    with contextlib.redirect_stdout(io.StringIO()):
        spec.loader.exec_module(m)
    o = m.out
    assert not o["H1_within_factor_3"] and not o["H2_specific_p_below_0.01"] and not o["H3_chi2_below_16.75"]
    assert abs(o["best_by_worst_factor"]["worst_factor"] - 4.169) < 0.01 and abs(o["calibration"]["fraction_fit_as_well"] - 0.098) < 1e-9


def test_the_seal():
    for name in ("the_order9_lines.py", "compare.py", "b1656_funcs.py"):
        h = hashlib.sha256((A / "verification" / name).read_bytes()).hexdigest()
        assert h in (A / "ARTIFACT_HASHES.txt").read_text(encoding="utf-8")
    assert hashlib.sha256((A / "PREREGISTRATION.md").read_bytes()).hexdigest().startswith("8b1c45f4")
