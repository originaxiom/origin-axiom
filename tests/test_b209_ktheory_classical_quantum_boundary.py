"""B209 -- Lambda*(R^6) under A5 = 5 bosonic irreps each mult 4 (total 64); the 4 spinorial 2I irreps
{2,2',4',6} (completing affine E8) are ABSENT. The classical/quantum boundary. Nothing to CLAIMS.md."""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "frontier", "B209_ktheory_classical_quantum_boundary"))
from lambda_decomposition import decompose, A5_IRREPS, SPINORIAL_2I_DIMS  # noqa: E402


def test_lambda_star_decomposition_all_mult_4():
    chiLS, mults = decompose()
    assert chiLS == [64, 0, 4, 4, 4]
    assert all(v == 4 for v in mults.values())                 # every A5 irrep mult 4
    assert sum(mults[n] * A5_IRREPS[n][0] for n in mults) == 64  # = 2^6


def test_spinorial_irreps_are_the_e8_completion():
    # the 4 spinorial 2I irreps {2,2,4,6} = 2I minus A5; sum of dims^2 = 60 (= |2I|-|A5| order halves)
    assert SPINORIAL_2I_DIMS == [2, 2, 4, 6]
    assert sum(d * d for d in SPINORIAL_2I_DIMS) == 60          # the spin-only half of 2I (|2I|=120)
    # A5 irrep dims (the bosonic half): sum of squares 60
    assert sum(A5_IRREPS[n][0] ** 2 for n in A5_IRREPS) == 60


if __name__ == "__main__":
    test_lambda_star_decomposition_all_mult_4()
    test_spinorial_irreps_are_the_e8_completion()
    print("ALL CHECKS PASS")
