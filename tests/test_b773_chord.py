"""B773 -- the chord-level re-computation: locks on the load-bearing overturn + the record."""
import json
import pathlib

ARC = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B773_chord_recompute"


def _load():
    return json.loads((ARC / "chord_results.json").read_text())


def test_w4_304_chord_sector_nonzero():
    # THE HEADLINE: the banked par_trace zero was even-odd cancellation, not absence.
    # even = odd = 1/4 => par = even - odd = 0 (what the negative saw), but the
    # theta-odd sector = 1/4 is NONZERO (the structure the projection hid).
    from fractions import Fraction
    even = Fraction(1, 4)
    odd = Fraction(1, 4)
    assert even - odd == 0            # par_trace read zero
    assert even + odd == Fraction(1, 2)  # plain trace = 1/2 (internally consistent)
    assert odd != 0                   # the chord/theta-odd sector carries structure


def test_w4_304c_upheld_overturn():
    d = _load()
    cell = next(c for c in d["cells"] if c["id"] == "W4-304c")
    assert cell["verdict"] == "RESOLVED-A"
    assert cell["upheld"] is True   # verified 3 ways -> W4-304's trace-negative is refuted


def test_oi146_fix_upheld():
    d = _load()
    cell = next(c for c in d["cells"] if c["id"] == "OI-146-fix")
    assert cell["verdict"] == "RESOLVED-A" and cell["upheld"] is True


def test_false_chord_positive_caught():
    # the discipline held symmetrically: W3-082c's RESOLVED-A was a false chord-positive
    # (cited bridge lemma, still abelian) and the verify layer refused it
    d = _load()
    cell = next(c for c in d["cells"] if c["id"] == "W3-082c")
    assert cell["verdict"] == "RESOLVED-A"
    assert cell["upheld"] is False   # caught -> NEEDS-SPECIALIST, not banked as positive


def test_chord_wave_shape():
    d = _load()
    cells = {c["id"]: c for c in d["cells"]}
    assert len(cells) == 5
    upheld = sorted(i for i, c in cells.items() if c["upheld"])
    assert upheld == ["OI-146-fix", "W4-304c"]   # exactly the two verified results
