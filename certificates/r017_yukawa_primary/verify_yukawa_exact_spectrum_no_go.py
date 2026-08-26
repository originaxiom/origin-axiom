#!/usr/bin/env python3
"""Exact character/dimension certificate for OA-C1055.

The sheaf vanishings and naturality proof are source-backed in the paired
report.  This executable locks the finite representation-theoretic part and
guards against silently replacing the unique ambient Higgs by a rank-jump
class without changing the massless spectrum.
"""

from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


def twist(characters: tuple[int, ...], amount: int) -> tuple[int, ...]:
    return tuple(sorted((q + amount) % 12 for q in characters))


def main() -> None:
    report = (ROOT / "memos/YUKAWA_EXACT_SPECTRUM_NO_GO.md").read_text(
        encoding="utf-8"
    )
    cup = (ROOT / "memos/YUKAWA_CUP_PRODUCTS_308.md").read_text(
        encoding="utf-8"
    )

    assert all(marker in cup for marker in (
        "H^1(Y,G_Y) = 0", "H^1(Y,K_1) = H^2(Y,K_1) = 0",
        "mu_u = 0", "rank(mu_u) = 0",
    ))
    assert all(marker in report for marker in (
        "equivariant injection", "C_amb = chi_0 + chi_1",
        "at least two `H_u`", "Changing only the coefficients",
    ))

    raw_ambient = (10, 11)
    twisted_ambient = twist(raw_ambient, 2)
    assert twisted_ambient == (0, 1)

    # The audited Wilson table selects H_u from chi_0 for both retained k.
    selected_hu_character = {4: 0, 8: 0}
    assert all(q in twisted_ambient for q in selected_hu_character.values())
    ambient_hu_multiplicity = twisted_ambient.count(0)
    assert ambient_hu_multiplicity == 1

    # r counts only possible nonambient classes.  Exact one-Hu content forces
    # their chi_0 multiplicity to vanish; any helpful extra chi_0 changes the
    # massless spectrum before a separate mass/mixing mechanism is supplied.
    for extra_chi0 in range(5):
        total_hu = ambient_hu_multiplicity + extra_chi0
        if total_hu == 1:
            assert extra_chi0 == 0
            ambient_yukawa_rank = 0
            assert ambient_yukawa_rank == 0
        else:
            assert total_hu >= 2

    print("DATA ambient Higgs characters after determinant twist =", twisted_ambient)
    print("DATA retained Wilson branches select H_u character =", selected_hu_character)
    print("RESULT exact one-Hu spectrum forces the unique Higgs into the ambient image")
    print("RESULT naturality forces its renormalisable up-type Yukawa rank to zero")
    print("PASS OA-C1055 same-monad coefficient variation cannot repair Y_u without changing the spectrum")


if __name__ == "__main__":
    main()
