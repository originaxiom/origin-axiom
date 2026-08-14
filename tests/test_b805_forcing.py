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
    # B805 banked with MOST arcs on no face, because attachment had only ever been done for the
    # NEGATIVES (the faces come from kill_graph). Its message read: "if this ever drops below half,
    # the positives have been attached -- update the arc." B842 attached them, so it dropped
    # (383+ -> 134 of 766). This is that update: the lock now guards the ATTACHED state, and the
    # residue is the arcs the panel judged to sit on NO face plus those with nothing to read.
    n_off = len(gp["arcs_on_no_face"])
    assert n_off < len(G["arcs"]) // 2, f"{n_off} arcs on no face -- attachment has regressed"
    assert n_off > 20, ("every arc is on a face -- suspicious: the panel judged ~15% to sit on "
                        "NO face, and forcing an attachment is the over-prediction that sank the "
                        "keyword classifier (B806)")
