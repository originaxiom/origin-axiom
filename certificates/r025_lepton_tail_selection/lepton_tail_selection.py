#!/usr/bin/env python3
"""Correct the R024 quark/lepton tail-selection scope.

The primary BCDD excerpt fixes the Wilson charges and the physical A-sector
multiplicities.  The committed height-308 artifacts fix the raw/physical
shifts and the five one-dimensional Serre-tail characters.  This certificate
keeps those two layers distinct and derives the selection equation for an
arbitrary raw A-character before specializing to Q and e^c.

It proves no connecting or mixed Yukawa entry.  Its only vanishing statement
is the alternating square of a single one-dimensional tail direction.
"""

from __future__ import annotations

import re
from pathlib import Path


MODULUS = 12
HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]


def parse_primary_excerpt(text: str) -> tuple[dict[str, int], tuple[int, ...]]:
    field_match = re.search(
        r"Field\s*& \$u\^c\$\s*& \$Q\$\s*& \$e\^c\$\s*& \$d\^c\$\s*& \$L, H_d\$",
        text,
    )
    assert field_match, "primary field row not found"

    charge_match = re.search(
        r"\\IZ_\{12\}\$ charge\s*& \$(8k)\$\s*& \$(k)\$\s*& \$(6k)\$\s*& \$(2k)\$\s*& \$(9k)\$",
        text,
    )
    assert charge_match, "primary Wilson-charge row not found"
    coefficients = tuple(1 if term == "k" else int(term[:-1]) for term in charge_match.groups())
    charges = dict(zip(("u^c", "Q", "e^c", "d^c", "L/Hd"), coefficients))

    decomposition_match = re.search(
        r"H\^1\([^\n]+?\) \\sim 3\*\\Reg_\{\\IZ_\{12\}\}\\oplus\s*(.+?)\.",
        text,
        re.DOTALL,
    )
    assert decomposition_match, "primary H1(V) decomposition not found"
    extra_labels = tuple(int(label) for label in re.findall(r"\\rep\{(\d+)\}", decomposition_match.group(1)))
    assert extra_labels == (1, 3, 7, 9, 10, 11)
    assert re.search(r"\(n_1,n_2\)=\(3,4\).*?k=4,8", text, re.DOTALL)
    return charges, extra_labels


def multiplicities(extra_labels: tuple[int, ...]) -> tuple[int, ...]:
    result = [3] * MODULUS
    for label in extra_labels:
        result[label] += 1
    return tuple(result)


def physical_character(charge_coefficient: int, k: int) -> int:
    """Cohomology must carry the character conjugate to the Wilson charge."""

    return -(charge_coefficient * k) % MODULUS


def required_b_sum(raw_a: int) -> int:
    """Solve (a+1)+(rho-2)+(sigma-2)=0 modulo twelve."""

    return (3 - raw_a) % MODULUS


def unordered_pairs(labels: tuple[int, ...], target: int) -> tuple[tuple[int, int], ...]:
    return tuple(
        (left, right)
        for index, left in enumerate(labels)
        for right in labels[index:]
        if (left + right) % MODULUS == target
    )


def wedge_one_direction(left: tuple[int, ...], right: tuple[int, ...]) -> dict[tuple[int, int], int]:
    """Exterior square in a fixed basis; used only for the skew-zero control."""

    answer: dict[tuple[int, int], int] = {}
    for i, x in enumerate(left):
        for j, y in enumerate(right):
            if i == j:
                continue
            pair = (i, j) if i < j else (j, i)
            sign = 1 if i < j else -1
            answer[pair] = answer.get(pair, 0) + sign * x * y
    return {pair: value for pair, value in answer.items() if value}


def main() -> None:
    primary = (HERE / "Three_gen_models_primary_excerpt.tex").read_text(encoding="utf-8")
    cup = (ROOT / "memos" / "YUKAWA_CUP_PRODUCTS_308.md").read_text(encoding="utf-8")
    spec = (
        ROOT
        / "documents"
        / "program-question-map"
        / "evidence"
        / "YUKAWA_DOWN_RESIDUE_SPEC_308.md"
    ).read_text(encoding="utf-8")

    charges, extra_labels = parse_primary_excerpt(primary)
    assert charges == {"u^c": 8, "Q": 1, "e^c": 6, "d^c": 2, "L/Hd": 9}
    physical_a_dimensions = multiplicities(extra_labels)
    assert physical_a_dimensions == (3, 4, 3, 4, 3, 3, 3, 4, 3, 4, 4, 4)

    # Parse-lock the committed chain convention rather than silently treating
    # its A7-specific equation as universal.
    for marker in (
        "raw spaces are `A7`, `B6`, `B2`",
        "physical `(Q8,dc4,Hd0)`",
        "raw-character 3 and 7 quotients",
    ):
        assert marker in cup, marker
    for marker in (
        "raw characters sum to",
        "physical shifts `(+1,-2,-2)`",
        "For general raw characters with `A_7`",
        "labels `(0,2,4,6,8)`",
    ):
        assert marker in spec, marker

    retained_rows = []
    for k in (4, 8):
        ec_physical = physical_character(charges["e^c"], k)
        lepton_physical = physical_character(charges["L/Hd"], k)
        assert (ec_physical, lepton_physical) == (0, 0)
        assert physical_a_dimensions[ec_physical] == 3
        retained_rows.append((k, ec_physical, lepton_physical))

    # A physical A-character is raw+1; a physical B-character is raw-2.
    q_raw = (physical_character(charges["Q"], 4) - 1) % MODULUS
    ec_raw = (physical_character(charges["e^c"], 4) - 1) % MODULUS
    l_raw = (physical_character(charges["L/Hd"], 4) + 2) % MODULUS
    assert (q_raw, ec_raw, l_raw) == (7, 11, 2)

    assert required_b_sum(q_raw) == 8
    assert required_b_sum(ec_raw) == 4

    tail_labels = (0, 2, 4, 6, 8)
    q_tail_pairs = unordered_pairs(tail_labels, required_b_sum(q_raw))
    ec_tail_pairs = unordered_pairs(tail_labels, required_b_sum(ec_raw))
    assert q_tail_pairs == ((0, 8), (2, 6), (4, 4))
    assert ec_tail_pairs == ((0, 4), (2, 2), (8, 8))

    # The physical lepton/Hd block is raw B2 on both B legs.  Its unique tail
    # direction therefore appears twice.  The alternating B x B cup square is
    # zero before any determinant or residue normalization is chosen.
    basis_tail_2 = (1,)
    assert wedge_one_direction(basis_tail_2, basis_tail_2) == {}
    physical_pure_tail_pair = (l_raw, l_raw)
    assert physical_pure_tail_pair == (2, 2)
    assert sum(physical_pure_tail_pair) % MODULUS == required_b_sum(ec_raw)

    # Non-vacuity: two independent directions need not have zero exterior
    # product, so this control cannot be promoted to the mixed/connecting map.
    assert wedge_one_direction((1, 0), (0, 1)) == {(0, 1): 1}

    print(f"primary_charge_coefficients={charges}")
    print(f"retained_physical_rows={retained_rows}")
    print("raw_sector_down=A7xB6xB2; required_B_sum=8")
    print("raw_sector_lepton=A11xB2xB2; required_B_sum=4")
    print(f"quark_A7_unordered_tail_pairs={q_tail_pairs}")
    print(f"lepton_A11_unordered_tail_pairs={ec_tail_pairs}")
    print("physical_lepton_pure_tail_pair=(2, 2); alternating_square=ZERO")
    print("mixed_and_connecting_lepton_entries=UNEVALUATED")
    print("b1208_three_way_fork=UNRESOLVED")
    print("R025 LEPTON TAIL-SELECTION CORRECTION: PASS")


if __name__ == "__main__":
    main()
