#!/usr/bin/env python3
"""Narrow exact audit of B1208's height-308 lepton-character question.

The certificate re-derives only what the committed R017 character ledger and
the down-residue specification determine.  It deliberately does not promote a
coarse Wilson sector to a generation-level Cech representative or Yukawa map.
"""

from __future__ import annotations

from pathlib import Path


N = 12
ROOT = Path(__file__).resolve().parents[1]


def add(*vectors: list[int]) -> list[int]:
    return [sum(vector[q] for vector in vectors) for q in range(N)]


def characters(*labels: int) -> list[int]:
    result = [0] * N
    for label in labels:
        result[label % N] += 1
    return result


def selected_character(k: int, field: str) -> int:
    wilson_charge = {
        "e^c": 6 * k,
        "L/Hd": 9 * k,
    }[field]
    return (-wilson_charge) % N


def main() -> None:
    cup_path = ROOT / "memos" / "YUKAWA_CUP_PRODUCTS_308.md"
    spec_path = (
        ROOT
        / "documents"
        / "program-question-map"
        / "evidence"
        / "YUKAWA_DOWN_RESIDUE_SPEC_308.md"
    )
    cup = cup_path.read_text(encoding="utf-8")
    spec = spec_path.read_text(encoding="utf-8")

    # Lock the primary committed statements this audit is re-deriving.
    for marker in (
        "e^c: A_0 (dim 3)",
        "L/H_d: B_0 (dim 4)",
        "down/lepton:   C^3 tensor C^3,     dimension 9",
        "No Higgs line is selected",
    ):
        assert marker in cup, marker
    for marker in (
        "selection requires `rho+sigma=8 mod 12`",
        "pure-tail",
        "`(0,8)`, `(2,6)`, and `(4,4)`",
        "Not proved: any nonzero down-Yukawa entry",
    ):
        assert marker in spec, marker

    regular = [1] * N
    A = add([3 * multiplicity for multiplicity in regular], characters(1, 3, 7, 9, 10, 11))
    B = add([3 * multiplicity for multiplicity in regular], characters(0, 11))
    assert A == [3, 4, 3, 4, 3, 3, 3, 4, 3, 4, 4, 4]
    assert B == [4, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4]

    rows: list[tuple[int, int, int, int, int]] = []
    for k in (4, 8):
        ec = selected_character(k, "e^c")
        lepton_doublet = selected_character(k, "L/Hd")
        assert (ec, lepton_doublet) == (0, 0)
        assert A[ec] == 3
        assert B[lepton_doublet] == 4
        rows.append((k, ec, A[ec], lepton_doublet, B[lepton_doublet]))

    # Non-vacuity control: the formula is not identically zero for arbitrary k.
    assert (selected_character(1, "e^c"), selected_character(1, "L/Hd")) == (6, 3)

    tail_labels = (0, 2, 4, 6, 8)
    admissible_unordered = tuple(
        (rho, sigma)
        for i, rho in enumerate(tail_labels)
        for sigma in tail_labels[i:]
        if (rho + sigma) % N == 8
    )
    assert admissible_unordered == ((0, 8), (2, 6), (4, 4))

    print(f"retained_branch_rows={rows}")
    print("coarse_character_ec=0")
    print("coarse_character_l=0")
    print(f"abstract_admissible_tail_pairs={list(admissible_unordered)}")
    print("frame_level_lepton_pair=UNDETERMINED")
    print("b1208_three_way_fork=UNRESOLVED")
    print("scope=no Cech representative, cyclic/Serre map, nonzero entry, determinant, or physical Yukawa")
    print("R024 LEPTON CHARACTER DATUM: PASS")


if __name__ == "__main__":
    main()
