"""B144 -- chirality of cusp-glued interactions. GL(2,Z) structural core unconditional; SnapPy/Regina gated."""
import pytest

from frontier.B144_interaction_chirality.probe import (
    chiral_composites_exist,
    mirror_closure_identity,
    pieces_are_amphichiral,
    regina_build_attempt,
)


def test_mirror_closure_identity():
    """The structural core: the mirror of a phi-gluing is the (h2 phi h1^-1)-gluing, still in GL(2,Z) (mirror-closed)."""
    mc = mirror_closure_identity()
    assert mc["all_mirror_gluings_in_GL2Z"] is True


def test_chiral_composites_are_generic():
    """Notion-(i) chirality (M not ~+ M-bar) is generic among gluings -- chiral JSJ composites exist (cf B128)."""
    ce = chiral_composites_exist()
    assert ce["sampled"] > 0
    assert ce["most_are_chiral"] is True


def test_pieces_amphichiral_premise():
    """The structural result's premise: each metallic piece is amphichiral (so an orientation-reversing h_i exists)."""
    pa = pieces_are_amphichiral()
    # works with or without SnapPy (records B128 values if absent)
    vals = pa.get("amphichiral", pa.get("recorded"))
    assert all(v is True for v in vals.values())


def test_regina_build_gate_reported():
    """Chat-2's one-instance gate: the build attempt reports a verdict (constructible pieces; closed-glue obstruction)."""
    rb = regina_build_attempt()
    if "skipped" in rb:
        pytest.skip(rb["skipped"])
    assert "build_verdict" in rb
    assert rb["b++RL"]["boundary_tori"] == 1 and rb["b++RRLL"]["boundary_tori"] == 1
