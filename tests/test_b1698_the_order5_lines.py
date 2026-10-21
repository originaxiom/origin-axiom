"""B1698 -- the order-5 lines (P-248), sealed 9c2a50039, NEGATIVE as sealed. Live: the comparison re-run from the stored
rows and the pinned data reproduces H1 (holds, 2.33), H2 (fails, 1.675% against 1%) and H3 (fails); the down quarks and the
leptons coincide at the best point; after the seal, one order-5 line makes them coincide and one order-8 line splits
them. Stored: the line sets; the seal's hashes; the criterion (coincide exactly when the order divides 4 or 5)."""
import hashlib, importlib.util, io, contextlib, json, math, pathlib
A = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B1698_the_order5_lines"


def test_the_cells_live():
    spec = importlib.util.spec_from_file_location("b1698_compare", A / "verification" / "compare.py")
    m = importlib.util.module_from_spec(spec)
    with contextlib.redirect_stdout(io.StringIO()):
        spec.loader.exec_module(m)
    o = m.out
    assert o["H1_within_factor_3"] and not o["H2_specific_p_below_0.01"] and not o["H3_chi2_below_16.75"]
    assert abs(o["best_by_worst_factor"]["worst_factor"] - 2.33) < 0.01 and abs(o["calibration"]["fraction_fit_as_well"] - 0.01675) < 1e-9
    ml = o["best_by_worst_factor"]["model_log"]
    assert abs(ml[2] - ml[4]) < 1e-9 and abs(ml[3] - ml[5]) < 1e-9                    # down and leptons coincide


def test_the_lines_and_the_seal():
    d = json.loads((A / "verification" / "the_order5_lines.json").read_text(encoding="utf-8"))
    assert d["S1"] == [["1/5", "2/5"], ["2/5", "4/5"], ["3/5", "1/5"], ["4/5", "3/5"]]
    assert d["S2"] == [["1/5", "3/5"], ["2/5", "1/5"], ["3/5", "4/5"], ["4/5", "2/5"]]
    for name in ("the_order5_lines.py", "compare.py", "b1656_funcs.py"):
        h = hashlib.sha256((A / "verification" / name).read_bytes()).hexdigest()
        assert h in (A / "ARTIFACT_HASHES.txt").read_text(encoding="utf-8")
    assert hashlib.sha256((A / "PREREGISTRATION.md").read_bytes()).hexdigest().startswith("6cb3ac13")


def test_after_the_seal_the_d_e_criterion():
    d = json.loads((A / "verification" / "after_the_seal" / "the_d_e_criterion.json").read_text(encoding="utf-8"))
    assert d["criterion_holds"] and len(d["rows"]) == 66
    for r in d["rows"]:
        assert r["coincide"] == (4 % r["order"] == 0 or 5 % r["order"] == 0)
    six_y = {"Q": 1, "u": -4, "d": 2, "L": -3, "e": 6, "H": 3}
    assert {k: v % 5 for k, v in six_y.items()} == {"Q": 1, "u": 1, "e": 1, "d": 2, "L": 2, "H": 3}     # SU(5)'s 10, 5bar, 5
    assert six_y["Q"] % 4 == six_y["L"] % 4 and six_y["d"] % 4 == six_y["e"] % 4                     # Pati-Salam's SU(4)
    spec = importlib.util.spec_from_file_location("b1698_de", A / "verification" / "after_the_seal" / "the_d_e_criterion.py")
    m = importlib.util.module_from_spec(spec)
    with contextlib.redirect_stdout(io.StringIO()):
        spec.loader.exec_module(m)
    from fractions import Fraction as Fr
    assert m.point((Fr(2, 5), Fr(4, 5), 0.5, 3.1))["coincide"]
    assert not m.point((Fr(1, 8), Fr(0), 0.5, 2.5))["coincide"]
