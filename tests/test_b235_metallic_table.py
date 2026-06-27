"""B235 locks -- the metallic family table (L49), the trace-1 ladder closure (L47, algebraic part), and the
F4 retraction (H24). The SnapPy half of L47 lives in l47_snappy_probe.py (sage env), documented in FINDINGS;
here we lock the pyenv-computable facts. Firewall: nothing to CLAIMS.md."""
import importlib.util
import pathlib
from fractions import Fraction as Fr

_PATH = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B235_metallic_table" / "metallic_table.py"
_spec = importlib.util.spec_from_file_location("b235_table", _PATH)
b235 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(b235)


def test_metallic_table_headline_cells():
    rows = {b235.metallic_row(m)["m"]: b235.metallic_row(m) for m in range(1, 7)}
    assert rows[1]["c"] == Fr(7, 10) and rows[1]["susy"] and rows[1]["mckay"].startswith("2I=E8 (GROUP")
    assert rows[2]["c"] == Fr(25, 28) and not rows[2]["susy"] and "2O=E7" in rows[2]["mckay"]
    assert rows[3]["trace_field"] == "Q(sqrt13)"
    assert rows[4]["trace_field"] == "Q(sqrt5)" and "field only" in rows[4]["mckay"]   # E8 field, no group
    assert rows[6]["trace_field"] == "Q(sqrt10)"


def test_susy_only_golden_and_H1():
    rows = [b235.metallic_row(m) for m in range(1, 13)]
    assert [r["m"] for r in rows if r["susy"]] == [1]
    assert b235.metallic_row(1)["H1"] == 83          # cross-checks B227/B229
    assert b235.metallic_row(1)["seifert_dual"] == "S^2(5,4,3)"


def test_trace1_ladder_closes():
    """L47: disc=1-4det at unit dets {+1,-1} -> {-3,5}; det=2 -> -7 (the unreachable, non-unimodular rung)."""
    lad = b235.trace1_ladder_closure()
    assert lad[-1] == 5 and lad[1] == -3 and lad[2] == -7


def test_no_su3_conformal_embedding_in_F4():
    """H24: no integer k has c(SU(3)_k)==c((F4)_1)=26/5 -> SU(3)->F4 route void -> footprint 3/5."""
    c_F4, sols = b235.f4_no_conformal_embedding()
    assert c_F4 == Fr(26, 5) and sols == []
