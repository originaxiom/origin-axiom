"""B275 locks -- an explicit E6-irreducible flat connection on the figure-eight was constructed (high-precision
Newton from the exp-4 cocycle): relator residual ~7.9e-8 with a nonzero {4,8} component, off rho_prin and
E6-dense by B265. An explicit NUMERICAL witness illustrating B274's rigorous existence. FIREWALLED; nothing to
CLAIMS.md. (Heavy computation reproduced by sage-python b275_witness.py.)"""
import importlib.util
import pathlib

_PATH = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B275_explicit_witness" / "b275_verdict.py"
_spec = importlib.util.spec_from_file_location("b275", _PATH)
b275 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(b275)


def test_witness_found():
    assert b275.witness_found()


def test_witness_is_off_rho_prin_and_dense():
    assert b275.WITNESS["exp4_nonzero"]               # nonzero {4,8} => not rho_prin / not principal SL(2)
    assert b275.WITNESS["e6_dense_by"] == "B265"      # density inherited from B265
    assert b275.WITNESS["rigorous_existence_by"] == "B274"   # honest: B274 is the proof, this illustrates
    assert b275.RELATOR_RESIDUAL < 1e-6
