"""Locks for Cell 1C finite defect kinematics."""

import json
from pathlib import Path

SUB = {"a": "abAAB", "b": "aAB", "A": "abAB", "B": "aA"}
Q = {"a": 1, "b": 3, "A": 6, "B": 7}
ROOT = Path(__file__).resolve().parent


def grow(depth):
    word = "a"
    for _ in range(depth):
        word = "".join(SUB[c] for c in word)
    return word


def total_delta(background, configuration):
    return sum(
        Q[new] - Q[old]
        for old, new in zip(background, configuration)
    ) % 11


def load_certificate():
    return json.loads(
        (ROOT / "CELL1C_DEFECT_KINEMATICS_CERTIFICATE.json")
        .read_text(encoding="utf-8")
    )


def test_finite_census_summary():
    result = load_certificate()
    census = result["finite_census"]
    assert census["maximum_factor_length"] == 500
    assert census["depth_9_to_10_stable_length_count"] == 494
    assert census["motion_witness_count"] == 0
    assert census["factor_count_at_length_500"] == 1699


def test_annihilation_witnesses_are_legal_and_neutral():
    result = load_certificate()
    word = grow(10)
    assert sorted(
        record["charge"]
        for record in result["annihilation_witnesses"]
    ) == [1, 2, 3, 4, 7, 8, 9, 10]

    for record in result["annihilation_witnesses"]:
        assert record["background"] in word
        assert record["pair_configuration"] in word
        assert total_delta(
            record["background"],
            record["pair_configuration"],
        ) == 0
        assert (
            record["first_component"]["charge"]
            + record["second_component"]["charge"]
        ) % 11 == 0


def test_fusion_witnesses_are_legal_and_conserve_charge():
    result = load_certificate()
    word = grow(10)
    channels = set()

    for record in result["fusion_witnesses"]:
        channels.add((
            record["first_charge"],
            record["second_charge"],
            record["total_charge"],
        ))
        assert record["background"] in word
        assert record["split_configuration"] in word
        assert record["fused_configuration"] in word

        split_delta = total_delta(
            record["background"],
            record["split_configuration"],
        )
        fused_delta = total_delta(
            record["background"],
            record["fused_configuration"],
        )
        assert split_delta == fused_delta == record["total_charge"]

    assert channels == {(3, 9, 1), (10, 3, 2)}


def test_missing_channels_are_scoped_as_finite_range():
    result = load_certificate()
    classification = result["classification"]
    assert classification[
        "strict_translation_channel_through_length_500"
    ].startswith("NOT_OBSERVED")
    assert classification["missing_inverse_pair"].startswith("5_PLUS_6")
