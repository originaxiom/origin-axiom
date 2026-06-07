"""B115 -- locking test: higher-rank/higher-genus generality of degree=rank (exploratory scoping).
The known SL(4) Dehn-filling reps are on the forced locus (tr A = tr A^-1), like SL(3) -- so off-locus SL(4)
content is in uncomputed components; genus-2 degree=rank needs machinery not in the repo. Both scoped OPEN with
the specific obstruction. NO physics; P1-P16 untouched."""
import importlib.util
import pathlib

_ROOT = pathlib.Path(__file__).resolve().parents[1]
_spec = importlib.util.spec_from_file_location(
    "b115", _ROOT / "frontier" / "B115_higher_generality" / "probe.py")
B = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(B)


def test_sl4_dehn_filling_reps_on_forced_locus():
    r = B.sl4_dehn_filling_on_forced_locus()
    assert r["all_on_forced_locus"] is True            # like SL(3): the known SL(4) reps are forced-locus
    assert "uncomputed" in r["obstruction"]            # off-locus SL(4) is open (no SL(4) HMP classification)


def test_genus2_scoped_open():
    g = B.genus2_scope()
    assert "OPEN" in g["genus2_status"]
    assert "obstruction" in g
