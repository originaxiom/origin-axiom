"""The aim may be stated and arrival may not (the owner's ruling R1, confirmed to main on 2026-11-10; carried out at B1878).

GOVERNANCE.md § 1 now says that the programme's only goal is a parameter-free theory of everything.  The framing lock's
ceiling did not move: no living page may say or imply that a value, or the Standard Model, has been derived.  The gate
`arrival-phrases` reads the living pages for a sentence of arrival, and these tests plant one."""
import importlib.util
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]


def _gates():
    spec = importlib.util.spec_from_file_location("gates_for_arrival_phrases", ROOT / "scripts" / "gates" / "gates.py")
    g = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(g)
    return g


def _page(tmp_path, text, name="README.md"):
    (tmp_path / "docs").mkdir(exist_ok=True)
    (tmp_path / name).write_text(text, encoding="utf-8")
    return tmp_path


def test_a_sentence_of_arrival_on_a_living_page_is_refused(tmp_path):
    """the advisor seat's own planted violation for its finding X1: add the sentence to the front page, and the gate fails"""
    g = _gates()
    front = (ROOT / "README.md").read_text(encoding="utf-8")
    root = _page(tmp_path, front + "\nWith this result the Standard Model is derived.\n")
    ok, why = g.gate_arrival_phrases(_root=root, _baseline=0)
    assert not ok and "README.md: the standard model is derived" in why, why
    for sentence in ("The object derives the Standard Model.", "All nineteen are derived.", "Our programme is a theory of everything.",
                     "The values are derived from the object alone."):
        ok, why = g.gate_arrival_phrases(_root=_page(tmp_path, sentence + "\n"), _baseline=0)
        assert not ok, sentence


def test_the_aim_a_denial_and_a_condition_pass(tmp_path):
    g = _gates()
    for sentence in ("The programme's only goal is a parameter-free theory of everything.",
                     "No value of the Standard Model is derived.",
                     "0 of 19: no value of the Standard Model is derived, and the paper says so.",
                     "It does not say that the Standard Model is derived.",
                     "Whether the Standard Model is derived from one object is the open question.",
                     "The goal is that the values are derived, with nothing fitted.",
                     "Nothing here says that this is a theory of everything."):
        assert g.arrival_hits(_page(tmp_path, sentence + "\n")) == [], sentence


def test_the_gate_is_green_on_this_repository_and_its_old_lines_are_frozen_by_key():
    """B1878 froze three old lines by COUNT; a count lets an old line be traded for a new sentence.  From B1880 each is frozen by
    a key of its page, its phrase and its sentence, and a sentence that is not one of the three fails."""
    g = _gates()
    ok, why = g.gate_arrival_phrases()
    assert ok and "3 old line(s) frozen by key" in why, why
    sents = g.arrival_sentences()
    assert sorted(k for k, *_ in sents) == sorted(g.ARRIVAL_FROZEN) and len(g.ARRIVAL_FROZEN) == g.ARRIVAL_BASELINE == 3
    assert sorted(rel for _, rel, _, _ in sents) == ["docs/CLOSURE_MASTERPLAN.md", "docs/THE_STATE_2026-09-06.md", "docs/WHAT_WOULD_COUNT.md"]
    assert g.arrival_hits() == []
    keep = g.ARRIVAL_FROZEN
    try:
        g.ARRIVAL_FROZEN = frozenset(sorted(keep)[1:])                              # one of the three no longer frozen: the gate fails
        ok, why = g.gate_arrival_phrases()
        assert not ok and "1 sentence(s) of arrival" in why, why
        g.ARRIVAL_FROZEN = keep | {"0" * 12}                                        # a key that matches nothing is reported
        ok, why = g.gate_arrival_phrases()
        assert ok and "1 frozen key(s) match nothing now" in why, why
    finally:
        g.ARRIVAL_FROZEN = keep


def test_the_advisor_seats_six_planted_sentences(tmp_path):
    """the seat's fourth re-audit (2026-11-11), its cases r1 to r6, planted by main on a small tree.  r2 passed the gate as first
    written because the excusing words were matched as pieces of words ('claim' holds 'aim'); r3 because a word of denial anywhere
    in the 64 characters before the phrase excused it; r5 and r6 because the papers and the folders below docs/ were not read.  r4
    is in other words and is not caught: the gate is a tripwire for the phrases it lists, and says so."""
    g = _gates()
    def planted(text, name="README.md"):
        root = tmp_path / ("t%d" % len(list(tmp_path.iterdir()))); f = root / name
        f.parent.mkdir(parents=True, exist_ok=True); f.write_text(text, encoding="utf-8")
        return g.gate_arrival_phrases(_root=root, _baseline=0)[0]
    assert not planted("The Standard Model is derived.\n")                                             # r1
    assert not planted("We claim that the Standard Model is derived.\n")                               # r2
    assert not planted("Nothing stands in the way now. The Standard Model is derived.\n")              # r3
    assert planted("All nineteen parameters now follow from the object with no free input.\n")         # r4: other words, NOT caught
    assert not planted("\\section{Result}\nThe Standard Model is derived.\n", "papers/P9/tex/sections/s09.tex")   # r5
    assert not planted("The Standard Model is derived.\n", "docs/progress/NOTE.md")                    # r6
    # the same defect in the other excusing words, and the excuses that must still hold
    assert not planted("A minor point: the Standard Model is derived.\n")                              # 'minor' holds 'nor'
    assert not planted("Nonetheless the Standard Model is derived.\n")                                 # 'nonetheless' holds 'none'
    assert not planted("We proclaim it. The Standard Model is derived!\n")
    assert not planted("- no value is fitted\n- the Standard Model is derived\n")                     # a denial in the bullet before
    assert not planted("| nothing is assumed | the Standard Model is derived |\n")                     # a denial in the cell before
    assert planted("We do not claim that the Standard Model is derived.\n")
    assert planted("The paper doesn't say that the Standard Model is derived.\n")
    assert planted("Our aim is a page on which the Standard Model is derived.\n")
    assert planted("It aims to show that the Standard Model is derived; it has not.\n")
    assert planted("an untracked note\n", "audit/draft/NOTE.md")                                       # outside the reach: not a page


def test_the_advisor_seats_own_sentences_for_its_mend_of_the_same_gate(tmp_path):
    """The advisor seat wrote its own mend of this gate the same morning (its patches_for_main/ @ 7726eeed) and tested it on
    these sentences.  Main's first mend refused one honest sentence of them ("We are seeking a frame in which ..."), and the
    seat's refused one that main's passed ("The paper doesn't say that ...").  The two are joined, and both lists hold."""
    g = _gates()
    def planted(text):
        root = tmp_path / ("s%d" % len(list(tmp_path.iterdir())))
        root.mkdir(); (root / "README.md").write_text(text + "\n", encoding="utf-8")
        return g.gate_arrival_phrases(_root=root, _baseline=0)[0]
    for sentence in ("We claim that the Standard Model is derived.", "A minor point: the Standard Model is derived.",
                     "The motif is plain: the values are derived.", "Nonetheless the Standard Model is derived.",
                     "Nevertheless, the values are derived.", "Now the Standard Model is derived.", "Notably, the values are derived."):
        assert not planted(sentence), sentence                                    # a word that only contains, or begins like, an excusing word
    for sentence in ("The programme aims to show that the Standard Model is derived.", "Among its goals: that the values are derived.",
                     "It wouldn't follow that the Standard Model is derived.", "We are seeking a frame in which the values are derived.",
                     "None of this says that the Standard Model is derived.", "We never say that the values are derived.",
                     "(Not yet: the Standard Model is derived only in the sense of its grammar.)",
                     "The paper doesn't say that the Standard Model is derived.", "It is aiming at a page where the values are derived."):
        assert planted(sentence), sentence                                        # an honest sentence of aim, denial or condition


def test_the_statement_of_aim_is_no_longer_banned_and_the_governing_page_says_why():
    g = _gates()
    assert "toward the full SM" not in g.BANNED and len(g.BANNED) == 8
    gov = (ROOT / "GOVERNANCE.md").read_text(encoding="utf-8")
    assert "The goal is **not** a theory of everything." in gov                  # the original sentence is kept
    assert "**The programme's only goal is a parameter-free theory of everything.**" in gov
    assert "A goal says what is sought. It does not say what has been reached." in gov
    assert "0 of 19" in gov


def test_the_gate_is_registered_with_a_control_and_a_practice():
    g = _gates()
    assert "arrival-phrases" in g.GATES
    controls = json.loads((ROOT / "tests" / "GATE_CONTROLS.json").read_text(encoding="utf-8"))
    assert controls["arrival-phrases"] == "tests/test_arrival_phrases.py::test_a_sentence_of_arrival_on_a_living_page_is_refused"
    assert "`arrival-phrases`" in (ROOT / "docs" / "PRACTICES.md").read_text(encoding="utf-8")
