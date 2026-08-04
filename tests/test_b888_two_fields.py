"""Locks B888 -- three cubics, one resolvent."""
import json
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[1]
_D = _ROOT / "frontier" / "B888_two_fields"
RES = json.loads((_D / "results.json").read_text(encoding="utf-8"))
_F = " ".join((_D / "FINDINGS.md").read_text(encoding="utf-8").split()).lower().replace("*", "")


def test_all_three_irreducible_positive():
    for k in ("vacuum_cubic", "generic_cubic", "mu"):
        assert RES[k]["irreducible"] is True
        assert RES[k]["disc_sign"] == 1


def test_one_resolvent_77():
    assert RES["shared_resolvent"] is True
    for k in ("vacuum_cubic", "generic_cubic", "mu"):
        assert RES[k]["squarefree_part"] == 77


def test_disc_factorizations():
    assert RES["mu"]["disc_factorization"] == {"2": 32, "3": 10, "5": 2,
                                               "7": 3, "11": 1, "13": 12}
    assert RES["vacuum_cubic"]["disc_factorization"]["2"] == 70
    assert RES["generic_cubic"]["disc_factorization"]["2"] == 64


def test_the_echo_is_fenced():
    assert "observation, unweighted" in _F
    assert "no mechanism claimed" in _F
