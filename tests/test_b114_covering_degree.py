"""B114 -- locking test: the covering-degree-=-k mechanism for degree=rank's exponent is TESTED-NEGATIVE.
The full covering degree (meridian spectra, det=1, mod permutation -> same L=c*M^k) is ~k^{n-1}, not k; the
'=k' reading holds only at the single-eigenvalue level (B111). NO physics; P1-P16 untouched."""
import importlib.util
import pathlib

_ROOT = pathlib.Path(__file__).resolve().parents[1]
_spec = importlib.util.spec_from_file_location("b114", _ROOT / "frontier" / "B114_covering_degree" / "probe.py")
B = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(B)


def test_full_covering_degree_is_not_k():
    r = B.covering_degree_negative()
    assert r["covering_degree_equals_k"] is False        # not k on any of the four
    # the known full counts: SL3 W1 = 9 = 3^2; SL4 secondary = 27 = 3^3
    assert r["per_component"]["SL3_W1"]["full_covering_degree"] == 9
    assert r["per_component"]["SL4_secondary"]["full_covering_degree"] == 27
    for comp in r["per_component"].values():
        assert comp["equals_k"] is False
