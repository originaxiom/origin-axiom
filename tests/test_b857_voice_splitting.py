"""Locks B857 -- the being voice cannot say 5, by splitting type.

These lock an EXACT arithmetic fact replacing a grep, and -- more importantly -- lock the SCOPE
correction: the phenomenon is a splitting type, not a property of voices, because the silver's
voice says 5 perfectly.
"""
import importlib.util
import json
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[1]
_D = _ROOT / "frontier" / "B857_voice_splitting"
_S = importlib.util.spec_from_file_location("b857", _D / "voice_splitting.py")
b7 = importlib.util.module_from_spec(_S)
_S.loader.exec_module(b7)
RES = json.loads((_D / "results.json").read_text(encoding="utf-8"))
_F = " ".join((_D / "FINDINGS.md").read_text(encoding="utf-8").split())


def test_the_being_voice_has_no_coefficient_at_5():
    assert b7.splitting(-3, 5) == "inert"
    assert b7.a_K(-3, 5) == 0
    assert RES["being_cannot_say_5"] is True


def test_the_being_prime_3_is_ramified_and_spoken():
    assert b7.splitting(-3, 3) == "ram"
    assert b7.a_K(-3, 3) == 1


def test_the_blindness_is_mutual():
    """3 is inert in Q(sqrt5): the hearing field cannot say the being prime either."""
    assert b7.splitting(5, 3) == "inert"
    assert RES["mutual_blindness"] is True


def test_THE_SCOPE_CORRECTION_the_silver_CAN_say_5():
    """The whole point: it is a splitting type, not a property of voices."""
    assert b7.splitting(-4, 5) == "split"
    assert b7.a_K(-4, 5) == 2
    assert RES["silver_can_say_5"] is True
    assert RES["is_a_property_of_voices"] is False


def test_inert_primes_always_give_zero_and_split_give_two():
    """The mechanism, not just the instance."""
    for d in (-3, -4, 5):
        for p in (2, 3, 5, 7, 11, 13, 17, 19, 23):
            t, a = b7.splitting(d, p), b7.a_K(d, p)
            assert a == {"inert": 0, "ram": 1, "split": 2}[t], (d, p, t, a)


def test_the_arc_states_the_discrete_channel_is_still_untested():
    """The real blind spot is the Hecke side, and the arc must not claim to have closed it."""
    assert "remains uncomputed" in _F
    assert "Hecke" in _F


def test_the_arc_records_that_it_replaces_a_grep():
    assert "grep" in _F.lower()
    assert "B746" in _F and "H-EAR" in _F
