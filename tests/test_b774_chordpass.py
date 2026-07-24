"""B774 -- the chord-pass campaign: locks on the negatives-base audit result."""
import json
import pathlib

ARC = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B774_chord_pass"


def test_stageA_structural_immune_majority():
    # 174 negatives scanned; the immune fraction is the framing result
    d = json.loads((ARC / "stageA_scan.json").read_text())
    assert d["total_scanned"] == 174
    assert d["candidates"] == 45                      # flagged chord-blind
    non_candidates = d["total_scanned"] - d["candidates"]
    assert non_candidates == 129                      # B766-immune (74%), never at projection risk
    explicit_structural = sum(1 for n in d["all"] if n["projection"] == "CHORD-OR-STRUCTURAL")
    assert explicit_structural == 95                  # explicitly structural projection


def test_stageB_all_harden_zero_overturns():
    # the decisive result: every load-bearing chord-blind wall hardens at theta-odd level
    d = json.loads((ARC / "stageB_results.json").read_text())
    cells = d["cells"]
    assert len(cells) == 12
    assert all(c["verdict"] == "HARDENS" for c in cells)
    assert all(c["upheld"] for c in cells)
    assert not any(c["verdict"] == "OVERTURNED" for c in cells)


def test_stageB_trap_detector_worked():
    # the W3-082c lesson: 11/12 "chord analogs" were not genuine chord objects
    # (abelian/character relabel or identical zero) -- only CP-W2 was genuine, and it confirms
    d = json.loads((ARC / "stageB_results.json").read_text())
    cells = {c["id"]: c for c in d["cells"]}
    genuine = [i for i, c in cells.items() if c.get("verify_genuine")]
    assert genuine == ["CP-W2-yukawa"]  # the one genuine theta-odd object -- and it HARDENS


def test_symmetric_alternating_contraction_is_type_zero():
    # CP-W2's core: symmetric cubic (x) alternating cup = 0 by graded-commutativity (a TYPE fact)
    import itertools
    import sympy as sp
    # totally symmetric S and totally antisymmetric A on 3 indices over a 3-dim space
    x = sp.symbols("x0:3")
    S = {p: sp.prod([x[i] for i in p]) for p in itertools.product(range(3), repeat=3)}  # symmetric
    # antisymmetric tensor via Levi-Civita
    eps = sp.LeviCivita
    total = sum(S[(i, j, k)] * eps(i, j, k) for i, j, k in itertools.product(range(3), repeat=3))
    assert sp.simplify(total) == 0  # symmetric contracted with alternating = 0 identically
