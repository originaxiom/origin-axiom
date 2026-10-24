"""B1747 -- the reading test verified on main (P-360), PROVED as a verification on a sample.  Stored: main's forty rows
(none below 100; the seat's lowest reproduced).  Live: the Standard Model's reading's chi2_nine at the seat's best row's
optimum region is far above the bar for a planted direction set (the record's forms), and the instrument's reading flips
the up sector (the control: reading S everywhere gives a different value)."""
import importlib.util, json, pathlib
from fractions import Fraction as Fr
import numpy as np
A = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B1747_the_reading_test_verified_on_main"


def test_stored():
    d = json.loads((A / "verification" / "sm_reading_check.json").read_text(encoding="utf-8"))
    assert len(d) == 40 and min(o["main"] for o in d) > 100 and abs(min(o["main"] for o in d) - 1045.407) < 0.01
    assert np.median([o["main"] / o["seat"] for o in d]) > 0.99


def test_reading_is_the_standard_models_live():
    spec = importlib.util.spec_from_file_location("b1747_s", A / "verification" / "sm_reading_check.py"); m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m); P = m.P; B = P.R.CEN._modules()["B"]
    M = P.SC.channels(0.6354, 3.3521, Fr(2, 5), Fr(7, 10)); F = P.forms(complex(0.6354, 3.3521))
    for k in ("DR", "F6", "F22"):
        h = F[k]; r_sm, _ = m.nine_sm(h, M, "L_2", B); r_s = P.res9(h, M, "L_2", B)
        assert float((r_sm ** 2).sum()) > 100 and abs(float((r_sm ** 2).sum()) - float((r_s ** 2).sum())) > 1.0
