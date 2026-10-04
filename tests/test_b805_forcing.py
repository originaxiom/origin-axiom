"""B805 — locks the forcing graph's structure and its honesty constraint."""
import importlib.util
import json
import os
import re
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
    # B805 banked with 19 authored edges against 583 attachment edges (330 arc->face, 253 facet->arc),
    # and this lock asserted that attachment still outnumbers authored. That is a live count of records
    # every later arc adds to, and it inverted at e41609cf (2026-10-04: 2,007 attachment, 2,023 authored)
    # because depends_on became a routine verdict field (the SM seat's arcs declare 7-10 each), with no
    # citation relabelled. A lock never asserts a live count of a record others add to (ERROR_LEDGER,
    # sm:B1531's bank slip), so the separation itself is checked: the authored edges are exactly the
    # verdicts' declared depends_on, and no attachment node is an arc.
    m = _m()
    declared = []
    for d in sorted(os.listdir(os.path.join(ROOT, "frontier"))):
        a = re.match(r"(B\d+)[a-zA-Z]?_", d)
        vp = os.path.join(ROOT, "frontier", d, "arc_verdict.json")
        if a and m._findings_doc(os.path.join(ROOT, "frontier", d)) and os.path.isfile(vp):
            declared += [(a.group(1), dep) for dep in (json.load(open(vp, encoding="utf-8")).get("depends_on") or [])]
    assert sorted(G["authored"]) == sorted(declared)
    assert not (set(G["faces"]) | set(G["facets"])) & set(G["arcs"])
    f = (ROOT / "frontier" / "B805_forcing_graph" / "FINDINGS.md").read_text(encoding="utf-8")
    assert "330 arc→face, 253 facet→arc" in f and "**19 arc→arc authored**" in f


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
