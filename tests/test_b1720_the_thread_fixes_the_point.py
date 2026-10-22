"""B1720 -- the thread fixes the point (P-284), sealed a93ff339a, NEGATIVE as sealed. Live: the comparison re-run from
the stored rows and the pinned data reproduces T1 and K1 holding, T2, T3, K2-K4 failing and the control holding; the best
row's geometry re-derived from thread_geometry. Stored: the seal's hashes."""
import hashlib, importlib.util, io, contextlib, json, pathlib, sys
A = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B1720_the_thread_fixes_the_point"


def test_the_cells_live():
    spec = importlib.util.spec_from_file_location("b1720_compare", A / "verification" / "compare.py")
    m = importlib.util.module_from_spec(spec)
    with contextlib.redirect_stdout(io.StringIO()):
        spec.loader.exec_module(m)
    o = m.out
    assert o["T1_six_within_factor_3"] and not o["T2_specific_p_below_0.01"] and not o["T3_chi2_below_16.75"]
    assert o["K1_three_within_factor_3"] and not o["K2_specific_p_below_0.01"] and not o["K3_nine_within_factor_3"] and not o["K4_specific_p_below_0.01"]
    assert o["C1_holds"]
    assert abs(o["masses"]["worst_factor"] - 1.8037) < 0.001 and abs(o["calibration_masses"]["fraction_fit_as_well"] - 0.0165) < 1e-9
    assert o["masses"]["word"] in ("LLLLLRLRR", "LLRLRRRRR", "LLLLLRRLR", "LLRRRRRLR")


def test_the_best_geometry_live():
    sys.path.insert(0, str(A / "verification"))
    import thread_geometry as TG
    import math
    from fractions import Fraction as Fr
    M = TG.mat("LLLLLRLRR"); t = int(M[0, 0] + M[1, 1])
    assert t == 30 and abs(TG.lagrange("LLLLLRLRR") / 2 - math.sqrt(896) / 10) < 1e-9          # height = sqrt(disc)/(2 min|c|), min|c| = 5
    assert math.lcm(Fr(11, 28).denominator, Fr(2, 7).denominator) == 28 == abs(2 - t)


def test_the_seal():
    for name in ("the_thread_census.py", "compare.py", "b1656_funcs.py", "thread_geometry.py"):
        h = hashlib.sha256((A / "verification" / name).read_bytes()).hexdigest()
        assert h in (A / "ARTIFACT_HASHES.txt").read_text(encoding="utf-8")
    assert hashlib.sha256((A / "PREREGISTRATION.md").read_bytes()).hexdigest().startswith("a0d2a726")
