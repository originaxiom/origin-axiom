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


def test_the_gate_is_green_on_this_repository_and_its_baseline_can_only_shrink():
    g = _gates()
    ok, why = g.gate_arrival_phrases()
    assert ok, why
    hits = g.arrival_hits()
    assert sum(c for _, _, c in hits) == g.ARRIVAL_BASELINE == 3 and sorted(h[0] for h in hits) == [
        "docs/CLOSURE_MASTERPLAN.md", "docs/THE_STATE_2026-09-06.md", "docs/WHAT_WOULD_COUNT.md"]
    ok, why = g.gate_arrival_phrases(_baseline=g.ARRIVAL_BASELINE - 1)          # one more than the frozen three would fail
    assert not ok and "baseline 2" in why


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
