"""B1046 — the arc graph does not carry what the bodies know.

Two defects, one shape, both mechanical:

(A) 42 arcs declare `supersedes`; 5 carry the back-link. A reader of `superseded_by` cannot tell a
    live arc from one its successor refuted -- and 12 superseded targets are cited on curated
    surfaces. B1037 caught B123 by READING A BODY; B1043 missed B564 because no body said so. The
    graph is what should have said so, and it is one-way.

(B) 35 FINDINGS carry a CORRECTION/REFUTED/WITHDRAWN banner BELOW their own headline; 31 have no
    docs/RETRACTIONS.md row, against that file's own same-PR rule. Worst case B408: opens "THE SEAM
    DOES NOT CONTRACT -- the one scale lever stands", verdict NEGATIVE, and kills itself 27 lines
    later. A SCALE-LEVER claim -- the most firewall-sensitive object in the programme.

The instrument is TRIAGED, NOT CAPPED (B821/B823) and the back-links are DELIBERATELY NOT WRITTEN.
"""
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts" / "checks"))
import supersession as sp          # noqa: E402  the gate's own module, not a reimplementation

R = {"checks": {}}


def chk(name, ok, **d):
    R["checks"][name] = {"pass": bool(ok), **d}
    return ok


def read(rel):
    return (ROOT / rel).read_text(encoding="utf-8")


# ------------------------------------------------- 1. the graph is one-way, and it is unchecked
arcs = sp._arcs()
says = [b for b, d in arcs.items() if sp._refs(d.get("supersedes"))]
back = [b for b, d in arcs.items() if sp._refs(d.get("superseded_by"))]
ow = sp.one_way_links()
chk("the_supersession_graph_is_one_way",
    len(says) > 40 and len(back) < 10 and len(ow) > 35,
    declaring_supersedes=len(says), carrying_back_link=len(back), broken=len(ow),
    note="the back-link is populated in %d of the %d cases it is owed" % (len(back), len(says)))
gates_src = read("scripts/gates/gates.py")
chk("and_NOTHING_read_superseded_by_before_this_arc",
    "superseded_by" not in gates_src.split("def gate_supersession")[0],
    note="verified against the gate file's own text ahead of this arc's addition; no check in "
         "scripts/checks/ referenced it either")
cited = [c for c in ow if "IS CITED" in c[2]]
chk("and_superseded_targets_are_LIVE_on_curated_surfaces",
    len(cited) >= 10, n=len(cited),
    arcs=sorted({c[1] for c in cited}, key=lambda z: int(z[1:])),
    note="including B123 -- the arc B1037 declined to restore BECAUSE B125 refutes it -- and "
         "B111, which B1037 dispositioned as SUBSUMED. A reader of the metadata cannot tell")

# ------------------------------------------------- 2. self-corrections, unregistered
sc = sp.unregistered_self_corrections()
chk("self_correcting_arcs_are_unregistered_in_RETRACTIONS",
    len(sc) > 25, unregistered=len(sc),
    rule="every future retraction adds its row in the PR that banks the correction",
    note="RETRACTIONS.md's own maintenance rule, quoted from its header")
b408 = read(list(ROOT.glob("frontier/B408_*/FINDINGS.md"))[0].relative_to(ROOT).as_posix())
head408 = b408.split("\n", 1)[0]
v408 = json.loads(list(ROOT.glob("frontier/B408_*/arc_verdict.json"))[0]
                  .read_text(encoding="utf-8"))
chk("B408_asserts_the_OPPOSITE_of_its_own_verdict_in_its_headline",
    "THE SEAM DOES NOT CONTRACT" in head408 and "scale lever stands" in head408
    and v408["verdict"] == "NEGATIVE"
    and "the seam CONTRACTS" in b408
    and "NO scale lever in any tested channel" in re.sub(r"\s+", " ", b408),   # wraps a line
    headline=head408[:90], verdict=v408["verdict"],
    note="a SCALE-LEVER claim, which WHAT_WOULD_COUNT grades Tier 2 on. The correction is 27 "
         "lines down; a body-reading pass meets the refuted headline first")
chk("and_B408_has_no_RETRACTIONS_row",
    not re.search(r"\bB408\b", read("docs/RETRACTIONS.md")),
    note="the arc_verdict is correctly NEGATIVE and docs/views/VERDICT_LEDGER carries that; the "
         "same-PR retraction rule was simply not applied")

# ------------------------------------------------- 3. the instrument, and what it refuses to do
chk("the_gate_is_wired_registered_and_fails_closed",
    '"supersession": gate_supersession' in gates_src
    and "FAIL-CLOSED" in gates_src.split("def gate_supersession")[1][:900]
    and "supersession" in read("docs/PRACTICES.md"))
chk("it_is_TRIAGED_not_capped__and_the_backlog_is_published",
    sp.sweep() == [] and len(sp.candidates()) > len(sp.load_bearing()),
    candidates=len(sp.candidates()), load_bearing=len(sp.load_bearing()),
    backlog=len(sp.candidates()) - len(sp.load_bearing()),
    note="triaging all 72 would mean writing 72 judgements without reading 72 bodies -- the "
         "claim-line sin this instrument exists to name. The backlog is stated, not hidden")
chk("the_back_links_are_DELIBERATELY_not_written",
    "DELIBERATELY NOT AUTOMATED" in read("scripts/checks/supersession.py")
    and all(not sp._refs(arcs[t].get("superseded_by"))
            for t in ("B141",) if t in arcs),
    note="`supersedes` conflates REPLACES with EXTENDS. B142 supersedes B141 and B1039 correctly "
         "restored BOTH -- an auto-filled back-link would have marked a live arc dead")

# ------------------------------------------------- 4. the instrument's first catch was its author
REG = read("docs/consolidation/SUPERSESSIONS.md")
mine = ("B141", "B154", "B157", "B164", "B95")
chk("its_FIRST_real_catch_was_this_refreshs_OWN_restorations",
    all(m in REG for m in mine)
    and "The instrument caught me" in REG,
    arcs=list(mine),
    note="B1039/B1040/B1044 cited five superseded arcs onto LAW_MAP. All five are genuinely "
         "EXTENDS -- which is exactly the outcome that vindicates not auto-writing back-links, "
         "since a mechanical rule would have marked all five dead, B141's live Item 1 with them")
chk("and_the_registry_disposes_BOTH_ways",
    "REPLACES" in REG and "EXTENDS" in REG and "SELF-LABELLED" in REG,
    note="B123/B111/B408/B702 REPLACE; B141/B154/B157/B164/B95/B13/B65/B162/B273/B496 EXTEND; "
         "B731/B437/B385/B812/B331/B558 are SELF-LABELLED and mislead nobody")

R["all_pass"] = all(v["pass"] for v in R["checks"].values())
if __name__ == "__main__":
    (pathlib.Path(__file__).parent / "results.json").write_text(
        json.dumps(R, indent=1, ensure_ascii=False, default=str))
    for k, v in R["checks"].items():
        print(("PASS " if v["pass"] else "FAIL ") + k)
    print("\nALL PASS:", R["all_pass"], " checks:", len(R["checks"]))
