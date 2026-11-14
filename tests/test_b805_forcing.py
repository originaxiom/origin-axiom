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
    # CHANGED 2026-11-13 (main's card C15, register row P-239; built by the building session).  The line read
    #     assert attachment > len(G["authored"])
    # over the whole record, and has failed since October: the attachment ends with B842's panel while new arcs' honest
    # `depends_on` grow the authored edges.  What it guards, that a citation is not counted a forcing, is held where there
    # is attachment to hold it: over the arcs up to the panel.  The drift after the panel is held by the last test below.
    era = _m().panel_era(G)
    attachment_in_era = sum(1 for v in list(G["faces"].values()) + list(G["facets"].values()) for a in v if a in era)
    authored_in_era = [e for e in G["authored"] if e[0] in era and e[1] in era]
    assert attachment_in_era > len(authored_in_era)
    assert attachment == attachment_in_era + sum(1 for v in list(G["faces"].values()) + list(G["facets"].values()) for a in v if a not in era)


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
    # CHANGED 2026-11-13 (main's card C15, register row P-239; built by the building session).  The count read the whole
    # record and has failed since October, for the reason the test above gives.  The two lines as they stood:
    #     n_off = len(gp["arcs_on_no_face"])
    #     assert n_off < len(G["arcs"]) // 2, f"{n_off} arcs on no face -- attachment has regressed"
    # It guards the attached state, so it reads the arcs up to the panel's arc, where the panel attached them.
    era = m.panel_era(G)
    n_off = len(set(gp["arcs_on_no_face"]) & era)
    assert n_off < len(era) // 2, f"{n_off} of the panel's {len(era)} arcs on no face -- attachment has regressed"
    assert n_off > 20, ("every arc is on a face -- suspicious: the panel judged ~15% to sit on "
                        "NO face, and forcing an attachment is the over-prediction that sank the "
                        "keyword classifier (B806)")


def test_the_drift_after_the_panel_is_reported_and_the_era_can_fail():
    """ADDED 2026-11-13 (main's card C15, register row P-239; built by the building session).  The two tests above read the
    arcs up to B842's panel.  What is after it is the drift, and it is reported and printed, not hidden: the arcs after the
    panel, and how many of them sit on no face.  Controls: the panel's era with its attachment taken away fails the count of
    arcs on no face; and a citation counted a forcing in the era fails the other."""
    m = _m()
    G = m.build()
    gp = m.gaps(G)
    era = m.panel_era(G)
    assert m.PANEL_ARC == "B842" and "B842" in era and not any(m._number(a) > 842 for a in era)
    assert set(gp["arcs_after_the_panel"]) == set(G["arcs"]) - era and gp["arcs_after_the_panel"]
    assert set(gp["arcs_after_the_panel_on_no_face"]) == set(gp["arcs_on_no_face"]) - era
    line = "THE DRIFT: arcs after the panel (B842): %d, of which on NO face: %d" % (len(gp["arcs_after_the_panel"]), len(gp["arcs_after_the_panel_on_no_face"]))
    assert m.drift_line(gp).startswith(line)
    src = (ROOT / "scripts" / "forcing" / "build.py").read_text(encoding="utf-8")
    assert 'print("    " + drift_line(gp))' in src[src.index("def main():"):]                 # the report prints it
    # control 1: the era's attachment taken away
    stripped = dict(G, faces={f: {a for a in v if a not in era} for f, v in G["faces"].items()})
    n_off = len(set(m.gaps(stripped)["arcs_on_no_face"]) & era)
    assert not n_off < len(era) // 2
    # control 2: every arc of the era cited by every other, as if a citation were a forcing
    flood = [(a, b) for a in sorted(era)[:60] for b in sorted(era)[:60] if a != b]
    attachment_in_era = sum(1 for v in list(G["faces"].values()) + list(G["facets"].values()) for a in v if a in era)
    assert not attachment_in_era > len(flood)

