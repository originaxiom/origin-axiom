"""B1704 -- what holds tau (P-251). Stored: the holding contents' minima (i and near omega for trivial fermions; the band
only for 89-95, 595-672, 689-780 scalars in the matter's representation; axis minima genuine). Live: the cusp algebra's
threshold and the record's positive totals; content (a) + 90 such scalars has an axis minimum near Im tau = 2.85."""
import importlib.util, io, contextlib, json, pathlib
import numpy as np
A = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B1704_what_holds_tau" / "verification"


def test_stored():
    h = json.loads((A / "hold.json").read_text(encoding="utf-8"))
    for r in h["rows"]:
        if r["extra"] == "trivial Weyl fermions":
            assert r["minima_y_Re0.0"] == [1.0] and all(0.9 <= y <= 1.06 for y in r["minima_y_Re0.5"])
    rho = json.loads((A / "hold_rho.json").read_text(encoding="utf-8"))
    assert [(rho[k]["band_rows"][0]["n"], rho[k]["band_rows"][-1]["n"]) for k in ("(a)", "(b)", "(c)")] == [(89, 95), (595, 672), (689, 780)]
    for k in ("(a)", "(b)", "(c)"):
        assert all(x["minimum"] for x in rho[k]["kinds"] if x["Re"] == 0.0)


def test_live():
    spec = importlib.util.spec_from_file_location("b1704_hold", A / "hold.py")
    H = importlib.util.module_from_spec(spec)
    with contextlib.redirect_stdout(io.StringIO()):
        spec.loader.exec_module(H)
    assert abs((31 / 512) / 2 - 31 / 1024) < 1e-15
    assert all(H.cusp(c) > 0 for c in H.CONT.values())
    c = dict(H.CONT["(a)"]); c[("m",)] -= 2 * 90
    v = -H.F(c, 0.0); d = np.diff(v)
    mins = [float(H.ys[i + 1]) for i in range(len(d) - 1) if d[i] < 0 <= d[i + 1]]
    assert len(mins) == 1 and abs(mins[0] - 2.85) < 0.02


def test_the_correction_stored():
    d = json.loads((A / "correction" / "mirror_check.json").read_text(encoding="utf-8"))
    assert d["mirror_pairs"]["0.0"] < 1e-10 and d["mirror_pairs"]["1.0"] < 1e-6 and d["mirror_pairs"]["0.5"] > 0.1
    assert min(abs(v) for v in d["dVdx_at_B1704_Re_half"].values()) > 1.0
    assert all(v["on_the_unit_arc"] for v in d["grid_minima"].values())
