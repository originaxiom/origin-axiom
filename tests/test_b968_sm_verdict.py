"""B968 locks — the crystallised SM verdict."""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from _prose import contains  # noqa: E402

ROOT = pathlib.Path(__file__).resolve().parents[1]
DOC = ROOT / "docs" / "THE_SM_VERDICT.md"


def test_the_one_sentence_is_present_and_scoped():
    assert contains(DOC, "adjoint half", "not the 27 half",
                    "an input in every theory anyone has")


def test_reproduced_is_distinguished_from_predicted():
    assert contains(DOC, "reproduced, not predicted", "16")


def test_the_rank_theorem_carries_its_scope_and_its_citation():
    assert contains(DOC, "proved for the simply connected form",
                    "cited, not re-derived", "steinberg")


def test_the_crossings_are_not_retrofitted():
    """They failed on values, not rank -- the verdict must say so."""
    assert contains(DOC, "failed on values, not on rank",
                    "retrofit explanation")


def test_the_live_opening_and_its_caveats():
    assert contains(DOC, "cubic étale algebras", "l138",
                    "never touched a vev", "a direction, not the values")


def test_what_the_verdict_is_not():
    assert contains(DOC, "the object fails", "unreachable from here",
                    "gate 5 is untouched")


def test_the_remaining_surface_is_enumerated():
    t = DOC.read_text(encoding="utf-8")
    for lead in ("L138", "L134", "L132", "L135", "L137"):
        assert lead in t
