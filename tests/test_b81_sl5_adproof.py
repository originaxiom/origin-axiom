"""B81 (follow-on, V63) -- locking test: the CRT/F_p route is seed-canonical at SL(4) (B80 valid) but
gauge-corrupt at SL(5) (route blocked). Uses the exact F_p engine; a few calls (~40s)."""
import importlib.util
import pathlib

_ROOT = pathlib.Path(__file__).resolve().parents[1]
_spec = importlib.util.spec_from_file_location(
    "b81_sl5", _ROOT / "frontier" / "B81_sl5_adproof" / "probe.py")
B81 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(B81)


def test_sl4_charpoly_seed_canonical():
    """SL(4): char(DT_0) is seed-invariant -- the reason B80's CRT route is valid at rank 4."""
    ok, _ = B81.is_seed_canonical(4, seeds=(20, 99))
    assert ok, "SL(4) char(DT_0) must be gauge-invariant (B80 relies on this)"


def test_sl5_charpoly_scatters_route_blocked():
    """SL(5): char(DT_0) SCATTERS across seeds -> gauge-corrupt -> CRT route blocked."""
    ok, cps = B81.is_seed_canonical(5, seeds=(20, 99))
    assert not ok, "SL(5) char(DT_0) must scatter across seeds (the gauge-corruption)"
    nd = sum(1 for i in range(len(cps[20])) if cps[20][i] != cps[99][i])
    assert nd >= 5, ("many char-poly coeffs must differ", nd)


def test_sl5_tagging_shows_degree3_gap():
    """The corruption is the doubly-degenerate even-k sector: char(M^2) mult 1 (not 2), (t+1) mult 1."""
    tower, remok = B81.sl5_tag()
    assert not remok, "SL(5) must have an untagged remainder (the degree-3 gap)"
    assert tower.get("char(M^2)") == 1, ("char(M^2) resolves at multiplicity 1, not 2", tower)
