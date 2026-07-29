"""B805 — locks the forcing graph's structure and its honesty constraint."""
import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def _m():
    spec = importlib.util.spec_from_file_location("b805", ROOT / "scripts" / "forcing" / "build.py")
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def test_the_saturated_menu_is_exactly_three_bits():
    """B733 bounded it; B766 proved it RANK-SATURATED. Not a sample -- the whole closing set."""
    m = _m()
    assert len(m.BITS) == 3
    names = {n for _, n in m.BITS}
    assert names == {"conjugation", "reversal", "the golden branch"}


def test_graph_builds_and_separates_authored_edges_from_attachment():
    """The honesty constraint: a citation is not a forcing, and the graph must keep them apart."""
    G = _m().build()
    assert G["faces"] and G["facets"] and G["arcs"]
    # authored edges are arc->arc pairs and are the ONLY forcing-grade ones
    assert isinstance(G["authored"], list)
    assert all(isinstance(e, tuple) and len(e) == 2 for e in G["authored"])
    # attachment edges vastly outnumber authored ones -- if that ever inverts silently,
    # someone has started calling citations forcings
    attachment = sum(len(v) for v in G["faces"].values()) + sum(len(v) for v in G["facets"].values())
    assert attachment > len(G["authored"])


def test_gaps_are_reported_not_hidden():
    """The property the whole instrument exists for: a missing branch shows as a hole."""
    m = _m()
    G = m.build()
    gp = m.gaps(G)
    for k in ("faces_with_no_proved_arc", "arcs_on_no_face", "arcs_with_no_verdict"):
        assert k in gp
    # the measured state at banking: most arcs are on no face, because face-attachment was
    # only ever done for the NEGATIVES (the faces come from kill_graph)
    assert len(gp["arcs_on_no_face"]) > len(G["arcs"]) // 2, \
        "if this ever drops below half, the positives have been attached -- update the arc"
