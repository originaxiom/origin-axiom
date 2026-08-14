"""Locks the Fleiss' kappa instrument BEFORE it is allowed to gate wave 2.

An agreement statistic that has never been checked against a known answer is not evidence.
These locks cover the reference case, the two extremes, and -- most importantly -- the
degenerate inputs where a naive implementation happily returns a plausible-looking number.
"""
import importlib.util
import math
from pathlib import Path

import pytest

_SPEC = importlib.util.spec_from_file_location(
    "fleiss_kappa", Path(__file__).resolve().parents[1] / "scripts" / "checks" / "fleiss_kappa.py")
fk = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(fk)


def test_reproduces_the_published_worked_example():
    """The instrument is checked against an answer it did not compute."""
    k, _, _, _, _ = fk.fleiss_kappa(fk.REFERENCE_TABLE)
    assert abs(k - fk.REFERENCE_KAPPA) < 0.001, f"got {k}, published {fk.REFERENCE_KAPPA}"


def test_perfect_agreement_is_one():
    # 4 items, 12 raters, 2 categories, used evenly across items so P_e stays off 1.
    table = [[12, 0], [12, 0], [0, 12], [0, 12]]
    k, P_bar, P_e, _, _ = fk.fleiss_kappa(table)
    assert P_bar == pytest.approx(1.0)
    assert k == pytest.approx(1.0)


def test_agreement_at_chance_is_about_zero():
    """Every item split evenly: raters agree exactly as often as the margins predict."""
    table = [[6, 6]] * 8
    k, _, _, _, _ = fk.fleiss_kappa(table)
    assert abs(k) < 0.12, f"even splits should sit near chance, got {k}"


def test_systematic_disagreement_is_negative():
    table = [[6, 6], [6, 6], [6, 6], [6, 6]]
    k, _, _, _, _ = fk.fleiss_kappa(table)
    assert k <= 0.0


def test_ragged_table_is_REJECTED_not_averaged():
    """Unequal ratings per item violate a hypothesis of the statistic.

    The failure mode this forbids: a reader silently skips an arc, the row is short, and the
    instrument returns a number that is not Fleiss' kappa but is reported as one.
    """
    with pytest.raises(ValueError, match="ragged"):
        fk.fleiss_kappa([[12, 0], [11, 0], [0, 12]])


def test_single_category_margin_is_REJECTED_not_reported_as_one():
    """If every rating lands in one category, chance agreement is total and kappa is 0/0.

    A naive implementation returns 0/0 -> nan, or worse, is guarded to return 1.0 -- which would
    read as 'the panel agrees perfectly' when in fact the panel never discriminated anything.
    """
    with pytest.raises(ValueError, match="P_e = 1"):
        fk.fleiss_kappa([[12], [12], [12]])


def test_unknown_label_is_REJECTED():
    """A reader using a value outside the sealed vocabulary must stop the gate, not be binned."""
    ratings = {"B1": {"r1": "PROVED", "r2": "OPEN"},
               "B2": {"r1": "PROVED", "r2": "MAYBE-ISH"}}
    with pytest.raises(ValueError, match="outside the declared vocabulary"):
        fk.table_from_ratings(ratings, ["PROVED", "OPEN"])


def test_one_rater_is_REJECTED():
    with pytest.raises(ValueError, match="fewer than 2"):
        fk.fleiss_kappa([[1, 0], [0, 1]])


def test_table_from_ratings_round_trips():
    ratings = {"B1": {"r1": "PROVED", "r2": "PROVED", "r3": "OPEN"},
               "B2": {"r1": "OPEN", "r2": "OPEN", "r3": "OPEN"}}
    table, cats, items = fk.table_from_ratings(ratings)
    assert items == ["B1", "B2"]
    assert cats == ["OPEN", "PROVED"]
    assert table == [[1, 2], [3, 0]]


def test_per_rater_distribution_exposes_the_offset():
    """The whole point of the shared block: one rater's mix vs another's on IDENTICAL items."""
    ratings = {f"B{i}": {"strict": "OPEN", "loose": "PROVED"} for i in range(10)}
    per = fk.per_rater_distribution(ratings)
    assert per["strict"]["OPEN"] == 10 and per["strict"]["PROVED"] == 0
    assert per["loose"]["PROVED"] == 10 and per["loose"]["OPEN"] == 0


def test_bootstrap_is_deterministic_under_its_seed():
    a = fk.bootstrap_ci(fk.REFERENCE_TABLE, reps=300)
    b = fk.bootstrap_ci(fk.REFERENCE_TABLE, reps=300)
    assert a == b, "a seeded CI must be reproducible or the gate is not auditable"


def test_bootstrap_interval_brackets_the_point_estimate():
    k, _, _, _, _ = fk.fleiss_kappa(fk.REFERENCE_TABLE)
    lo, hi, used = fk.bootstrap_ci(fk.REFERENCE_TABLE, reps=800)
    assert used > 400
    assert lo <= k <= hi, f"CI [{lo}, {hi}] must contain the point estimate {k}"
