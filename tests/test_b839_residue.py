"""B839 — locks the artifact result and, critically, that the criterion CAN fail."""
import importlib.util
from math import factorial
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
_SPEC = importlib.util.spec_from_file_location(
    "b839", ROOT / "frontier" / "B839_b685_residue" / "normalisation.py")
b = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(b)


def test_2n_factorial_clears_every_non3_denominator():
    C = b.coefficients()
    for n, c in C.items():
        d = b.non3_denominator(c)
        if d == 1:
            continue
        assert factorial(2 * n) % d == 0, f"(2n)! fails to absorb the non-3 denominator at n={n}"


def test_the_criterion_can_FAIL_and_most_of_the_family_does():
    """Eight of nine sealed family members fail -- so the winner is not fitted to the data."""
    C = b.coefficients()
    losers = []
    for name, f in b.FAMILY.items():
        for n, c in C.items():
            d = b.non3_denominator(c)
            if d != 1 and f(n) % d != 0:
                losers.append(name)
                break
    assert len(losers) == len(b.FAMILY) - 1, f"expected exactly one winner; losers={losers}"
    assert "(2n)!" not in losers


def test_the_double_factorial_alone_is_insufficient():
    """The recorded mechanism error: (2n)! = 2^n * n! * (2n-1)!!, and the 2-part dominates."""
    for n in range(1, 8):
        assert factorial(2 * n) == 2 ** n * factorial(n) * b.dfact(2 * n - 1)
    C = b.coefficients()
    d2 = b.non3_denominator(C[2])
    assert b.dfact(2 * 2 - 1) % d2 != 0, "(2n-1)!! must fail at n=2, as recorded"


def test_the_convention_is_still_labelled_CITED():
    f = " ".join((ROOT / "frontier" / "B839_b685_residue" / "FINDINGS.md").read_text(
        encoding="utf-8").split())
    assert "NOT discharged — the CONVENTION" in f
    assert "stays FALSE" in f
