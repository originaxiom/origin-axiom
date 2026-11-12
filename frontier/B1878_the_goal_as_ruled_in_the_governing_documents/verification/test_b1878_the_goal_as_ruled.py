"""B1878 -- every amended passage keeps its original text beside a dated note; the goal is stated once; one file governs;
the two gates are in place with their controls.  The planted violations are in tests/test_arrival_phrases.py and
tests/test_attribution_history.py."""
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[3]


def _read(*parts):
    return ROOT.joinpath(*parts).read_text(encoding="utf-8")


def test_the_governing_document_keeps_the_old_sentences_and_states_the_goal_once():
    g = _read("GOVERNANCE.md")
    for original in ("The goal is **not** a theory of everything. The goal is a body of work an external expert",
                     "apart. Every other file in this repo is subordinate to the rules here.",
                     "structure is the object's, the values are the observer's.",
                     "value* (rather than the form a value would fill) has breached it."):
        assert original in g, original
    assert g.count("**The programme's only goal is a parameter-free theory of everything.**") == 1
    assert g.count("[Amended 2026-11-11") == 4 and "**Amended:** 2026-11-11" in g
    for kept in ("A goal says what is sought. It does not say what has been reached.", "no value derived, 0 of 19",
                 "This file is the one governing document.", "**`GENESIS.md` holds on the status of every item of the foundation.**",
                 "given the premises `GENESIS.md` lists", "is a record of the routes tested, not a limit on the goal",
                 "prose that says or implies that a value has been derived, before that"):
        assert kept in g, kept


def test_the_two_pages_under_it():
    c = _read("CLAIMS.md")
    assert "## Open — research targets (Phase B / `frontier/`). NOT partial results." in c
    assert "**Their status is unchanged: open, and none a partial result.**" in c and "`GOVERNANCE.md` is the one governing document." in c
    assert "| O4 | Matter / Standard Model content. |" in c
    t = _read("docs", "THE_CLAIM.md")
    assert "at most one dimensionless frame anchor** are LICENSED" in t                    # the original licence, kept
    assert "**The dimensionless frame anchor is a debt against the claim, to be removed. It is not a standing licence.**" in t
    assert "**The three theorems this section cites stand.**" in t


def test_no_amended_passage_states_arrival():
    """the ceiling: the amended pages pass the gate that reads for arrival, and each new note names the count"""
    import importlib.util
    spec = importlib.util.spec_from_file_location("gates_for_b1878", ROOT / "scripts" / "gates" / "gates.py")
    g = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(g)
    hits = g.arrival_hits()
    assert not [h for h in hits if h[0] in ("CLAIMS.md", "docs/THE_CLAIM.md", "README.md")]
    # CORRECTED 2026-11-12 (Review 79, from a reading on another family of model): the governing page is exempt from the gate, so it
    # is read here; and it was read for four substrings, which cover five of the gate's sixteen phrases.  Eleven were looked for by
    # nobody on this page.  All of the gate's phrases are looked for now, in the page's text with its line breaks joined.
    low = " ".join(_read("GOVERNANCE.md").lower().split())
    assert len(g.ARRIVAL_PHRASES) >= 16
    for phrase in tuple(g.ARRIVAL_PHRASES) + ("the standard model is derived", "is a theory of everything", "the values are derived", "all nineteen"):
        assert phrase not in low, phrase
    assert _read("GOVERNANCE.md").count("0 of 19") >= 2


def test_the_gates_and_the_findings():
    controls = json.loads(_read("tests", "GATE_CONTROLS.json"))
    assert controls["arrival-phrases"].startswith("tests/test_arrival_phrases.py::") and "attribution" in controls
    gates = _read("scripts", "gates", "gates.py")
    assert "def attribution_history_problems(" in gates and 'ATTRIBUTION_FROM = "da25c4f497adf5b137f95e5f5ee98d6513c159d9"' in gates
    assert '"toward the full SM",' not in gates
    pr = _read("docs", "PRACTICES.md")
    assert "`arrival-phrases`" in pr and "every commit message after `da25c4f49`" in pr
    f = _read("frontier", "B1878_the_goal_as_ruled_in_the_governing_documents", "FINDINGS.md")
    for s in ("The repo sweep:", "**The ceiling did not move.**", "**Which file governs was main's choice.**", "It is a\n  tripwire for the plain cases"):
        assert s in f, s


# ------------------------------------------------------------------------------------------------ added 2026-11-12 (Review 80)
# A session that built none of this planted against the lock: the dated note removed from the page passed, and the verdict
# file made unreadable passed.

def test_the_verdict_and_the_dated_notes_are_held():
    arc = pathlib.Path(__file__).resolve().parents[1]
    v = json.loads((arc / "arc_verdict.json").read_text(encoding="utf-8"))
    assert v["id"] == "B1878" and v["verdict"] == "PROVED"
    assert "[NOTE 2026-11-12 (Review 80" in v["claim_one_line"] and "replaced the same day by B1880, five of them" in v["claim_one_line"]
    f = (arc / "FINDINGS.md").read_text(encoding="utf-8")
    assert "> **NOTE 2026-11-12 (Review 79's second round" in f and "> **CORRECTED 2026-11-12 (Review 80" in f and "Five, not" in f
