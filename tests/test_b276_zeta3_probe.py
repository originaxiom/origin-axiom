"""B276 locks -- the figure-eight's colored Jones degenerates at the trace-field roots zeta_3 (period 3) and
zeta_6 (period 6) into integer sequences in O_{Q(sqrt-3)}=Z[zeta_3], with the ramification (1-zeta_3)(1-zeta_3^2)=3
(the E6-end companion to B261's zeta_5/E8 result). A COHERENCE with the E6 selection (B266), not a settlement of
wall #2. FIREWALLED; nothing to CLAIMS.md."""
import importlib.util
import pathlib

_PATH = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B276_zeta3_arithmetic_probe" / "b276_zeta3_probe.py"
_spec = importlib.util.spec_from_file_location("b276", _PATH)
b276 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(b276)


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
