"""B1341 - the atlas needs a word for 'is there an action?' and for 'does it feed back?'.

B1247 (on main) located the retrieval failure: the lexicon indexes the OBJECTS studied and had no
word for the QUESTION, so "do we have an arrow of time?" retrieved nothing while B497 sat banked
under twelve object-motifs. It added seven question-motifs -- arrow, monoid, measurement, closing,
naming, choice, coupling.

It did not add a word for ACTION or FEEDBACK, and that gap cost this session directly: "feedback"
returned 4 corpus hits in 1300+ arcs, "least action" returned zero arcs joined to the object, while
B6 (an Euler-Lagrange equation, OPEN since week one), B21 (the anti-Poisson half step) and B37 (the
feedback predicate) had all been banked for a year. Same mechanism, same fix.

The sharpest thing these lock: B1157 concluded "the object supplies NO parameter-free dynamical law"
and B6 holds a derived potential with an Euler-Lagrange equation. B1247's own text names that pair
as un-joined. They must now share a motif.
"""
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
DATA = ROOT / "scripts" / "atlas" / "atlas_data.json"


def _probes():
    return json.loads(DATA.read_text(encoding="utf-8"))["probes"]


def test_the_two_motifs_exist_and_are_populated():
    lex = json.loads(DATA.read_text(encoding="utf-8"))["lexicon"]
    for m in ("action", "feedback"):
        assert m in lex, f"the lexicon has no word for {m!r}"
    pr = _probes()
    for m, floor in (("action", 20), ("feedback", 5)):
        n = sum(1 for v in pr.values() if m in (v.get("motifs") or []))
        assert n >= floor, f"motif {m!r} matched only {n} probes -- the patterns are too narrow"


def test_the_arcs_this_session_needed_are_retrievable():
    """each was banked and unreachable by the question that wanted it."""
    pr = _probes()
    for arc, motif in (("B6", "action"),      # the Euler-Lagrange equation, OPEN since week one
                       ("B21", "action"),     # the anti-Poisson half step
                       ("B1157", "action"),   # the dynamics NEGATIVE
                       ("B1341", "action"),   # the theorem
                       ("B37", "feedback"),   # the feedback predicate, measured then fenced
                       ("B1341", "feedback")):
        assert arc in pr, f"{arc} is not in the atlas at all"
        assert motif in (pr[arc].get("motifs") or []), (
            f"{arc} is not retrievable under {motif!r} -- the question still has no word")


def test_the_pair_b1247_named_as_unjoined_now_shares_a_motif():
    """B1247: B1157 concluded 'no parameter-free dynamical law' while B6 held the very kinetic term
    it lists as missing. A seat asking 'is there an action?' must now get BOTH."""
    pr = _probes()
    a, b = set(pr["B1157"].get("motifs") or []), set(pr["B6"].get("motifs") or [])
    assert "action" in a & b, "the dynamics NEGATIVE and the field equation are still un-joined"


def test_the_markov_conflation_hazard_is_respected():
    """campaign row X31: 'the corpus is full of Markov TRIPLES, a different object'. The feedback
    motif may match the phrase 'markov blanket' but must not match bare 'markov'.

    The dumped lexicon drops `patterns`, so this reads the source of truth."""
    src = (ROOT / "scripts" / "atlas" / "atlas.py").read_text(encoding="utf-8")
    i = src.find('"feedback":')
    assert i > 0, "the feedback motif went missing from the lexicon source"
    block = src[i:src.find('"figure_eight":', i)]
    assert '"markov blanket"' in block, "the blanket phrase should be indexed"
    for bad in ('"markov"', "'markov'", '"markov ', "r\"markov\""):
        assert bad not in block.lower().replace("markov blanket", "blanket"), (
            f"a bare markov pattern ({bad}) would sweep in the Markov surface, an unrelated object")
