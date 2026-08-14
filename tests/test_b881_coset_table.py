"""Locks B881 -- the SM-graded coset commutation table."""
import json
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[1]
_D = _ROOT / "frontier" / "B881_coset_table"
RES = json.loads((_D / "results.json").read_text(encoding="utf-8"))
_F = " ".join((_D / "FINDINGS.md").read_text(encoding="utf-8").split()).lower().replace("*", "")


def test_the_gradings():
    assert RES["W_pieces"] == [1, 1, 1, 1, 2, 2, 3, 3, 3, 3, 6, 6]
    assert RES["K1_pieces"] == [1, 1, 3, 3, 6, 6, 6, 6, 14]


def test_the_3_grading_cell_complete():
    """42 = 2*(C(6,2)+6): every same-sign pair, all zero."""
    same = [z for z in RES["zero_cells"] if abs(z["z1_sum"]) > 1e-10]
    assert len(same) == 42
    assert RES["n_zero_cells"] == 50


def test_every_nonzero_cell_is_single_target():
    assert RES["n_nonzero_cells"] == 28
    assert all(len(t["targets"]) == 1 for t in RES["table"])


def test_the_gauge_covariance_diagonal():
    """six own-conjugate channels land in the unbroken 14."""
    to14 = [t for t in RES["table"] if t["targets"][0][0] == 14]
    assert len(to14) == 6
    assert sorted((t["a_dim"], t["b_dim"]) for t in to14) == \
        [(1, 1), (1, 1), (2, 2), (3, 3), (3, 3), (6, 6)]


def test_the_standing_rule_is_recorded():
    assert "must be oblique" in _F
    assert "earned three times" in _F
    assert "not the yukawa skeleton proper" in _F
