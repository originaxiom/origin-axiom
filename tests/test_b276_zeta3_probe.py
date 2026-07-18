"""B276 locks -- the figure-eight's colored Jones degenerates at the trace-field roots zeta_3 (period 3) and
zeta_6 (period 6) into integer sequences in O_{Q(sqrt-3)}=Z[zeta_3], with the ramification (1-zeta_3)(1-zeta_3^2)=3
(the E6-end companion to B261's zeta_5/E8 result). A COHERENCE with the E6 selection (B266), not a settlement of
wall #2. FIREWALLED; nothing to CLAIMS.md."""
import importlib.util
import pathlib

import mpmath as mp
import pytest

_PATH = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B276_zeta3_arithmetic_probe" / "b276_zeta3_probe.py"
_spec = importlib.util.spec_from_file_location("b276", _PATH)
b276 = importlib.util.module_from_spec(_spec)
# E12 (module-level-dps sweep): b276_zeta3_probe sets mp.mp.dps=60 at module
# level, then internally imports B261's golden_root_aj which sets dps=50 — so
# the collection-time import used to leave 50 behind. Both modules compute
# their import-time values under a dps they set themselves; restore the entry
# dps afterwards so nothing leaks into later-collected modules.
_saved_dps = mp.mp.dps
_spec.loader.exec_module(b276)
mp.mp.dps = _saved_dps


@pytest.fixture(autouse=True)
def _dps_60():
    # E12 repair (the b204 pattern): the probe's entry points already self-guard
    # to 60 internally; pin the module's declared dps=60 per test as well so no
    # runtime path depends on the collection-time global.
    saved = mp.mp.dps
    mp.mp.dps = 60
    yield
    mp.mp.dps = saved


def test_verdict():
    assert b276.verdict()


def test_degeneration_in_ring_of_integers():
    assert b276.all_integral(3) and b276.detect_period(b276.jones_sequence(3)) == 3
    assert b276.all_integral(6) and b276.detect_period(b276.jones_sequence(6)) == 6
    # match the recorded sequences (first period)
    assert b276.jones_sequence(3)[:3] == b276.ZETA3["seq6"][:3]
    assert b276.jones_sequence(6)[:6] == b276.ZETA6["seq6"]


def test_ramification_of_3():
    assert b276.ramification_holds()          # (1-zeta_3)(1-zeta_3^2) = 3
    assert b276.RAMIFIED_PRIME == 3
