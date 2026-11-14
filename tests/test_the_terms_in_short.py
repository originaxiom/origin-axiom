"""2026-11-13 (main's M29, TERMINOLOGY as the builder proposed): the public face's glossary, docs/THE_TERMS_IN_SHORT.md.

Every entry names its source; every section it names is a section of the full account and every page it names exists;
it uses no inner word of the working record; each statement of mathematics in it stands in its source in the same
words; and TERMINOLOGY.md, the working record's glossary, is no longer read as the public face. A draft for one cold
reading before the README points to it."""
import importlib.util, pathlib, sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
TERMS = ROOT / "docs" / "THE_TERMS_IN_SHORT.md"
FULL = ROOT / "docs" / "THE_PROGRAMME_SO_FAR.md"


def _load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(spec); sys.dont_write_bytecode = True; spec.loader.exec_module(m)
    return m


SHORT = _load("the_short_pages_lock", ROOT / "tests" / "test_the_programme_so_far.py")
GATES = _load("gates_for_the_terms", ROOT / "scripts" / "gates" / "gates.py")

# (the words on the glossary, the same words in the full account): each statement of mathematics, as its source has it
SAID = (
    ("L = [[1,1],[0,1]] and R = [[1,0],[1,1]]", "L = [[1,1],[0,1]], R = [[1,0],[1,1]]"),
    ("LR = [[2,1],[1,1]], which has trace 3", "LR = [[2,1],[1,1]] has trace 3"),
    ("LP = [[1,1],[1,0]], where P = [[0,1],[1,0]] swaps the two counts; its square is LR",
     "the golden matrix LP = [[1,1],[1,0]] satisfies (LP)² = LR"),
    ("Cohn matrix of the golden ratio", "LR is the Cohn matrix of the golden ratio"),
    ("a → ab, b → a as the Fibonacci substitution", "the rule a → ab, b → a is the Fibonacci substitution"),
    ("758 states at word lengths 2 to 12, giving 536 distinct manifolds", "758 states at word lengths 2 to 12, realising 536 distinct manifolds"),
    ("whose monodromy is the n-th power of the state's", "the n-fold cyclic cover of a state has monodromy (εw)ⁿ"),
    ("hyperbolic three-dimensional manifold with one cusp", "a hyperbolic 3-manifold with one\ncusp"),
    ("it holds exactly for the class of LR (m004) and the class of LP (the Gieseking manifold, m000)",
     "H₁ is torsion-free exactly for the class of LR (trace 3: m004) and the class of LP (det −1: the Gieseking manifold m000)"),
    ("A frame is\n  a hypothesis, and none is derived from the principle", "A frame is"),
    ("Neutrino masses and mixing are outside the nineteen", "Neutrino masses and mixing are outside the nineteen"),
)


def _problems(text):
    bad = SHORT._short_problems(text, FULL.read_text(encoding="utf-8"))
    bad = [b for b in bad if b != "the goal's count is not stated as the goal states it"]      # a glossary states no count
    if dict(GATES.public_face_words(text)):
        bad.append("inner words: %s" % dict(GATES.public_face_words(text)))
    return bad


def test_every_entry_has_a_source_and_no_inner_word():
    assert _problems(TERMS.read_text(encoding="utf-8")) == []


def test_each_statement_of_mathematics_stands_in_its_source():
    text, full = TERMS.read_text(encoding="utf-8"), FULL.read_text(encoding="utf-8")
    genesis = (ROOT / "GENESIS.md").read_text(encoding="utf-8")
    for ours, theirs in SAID:
        assert ours in text, ours
        assert theirs in full or theirs in genesis, theirs


def test_the_working_glossary_is_not_the_public_face_and_is_kept():
    assert "TERMINOLOGY.md" not in GATES.PUBLIC_FACE and "TERMINOLOGY.md" not in GATES.PUBLIC_FACE_HELD
    assert (ROOT / "TERMINOLOGY.md").is_file() and "`TERMINOLOGY.md`" in TERMS.read_text(encoding="utf-8")


def test_the_lock_can_fail():
    text = TERMS.read_text(encoding="utf-8")
    assert len(_problems(text.replace(" (§ 3.1).", ".", 1))) == 1                 # an entry with its source taken out
    assert len(_problems(text.replace("(§ 0.3)", "(§ 13)", 1))) == 1              # a section the full account lacks
    assert len(_problems(text.replace("`docs/THE_WEAVE.md`", "`docs/THE_WEAVES.md`", 1))) == 1
    assert len(_problems(text + "\n- **A seat.** One session (§ 3).\n")) == 1     # an inner word
