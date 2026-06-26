"""B224 -- golden is the unique metallic mean whose anyon chain is supersymmetric. Nothing to CLAIMS.md.

Load-bearing locks (exact rational):
  - su(2)_3 chain -> M(4,5) c=7/10 (the golden chain CFT); the su(2)_k chain -> M(k+1,k+2).
  - among ALL unitary minimal models M(q,q+1), ONLY M(4,5) is N=1 superconformal (unique).
  - in the metallic family (k_m=m^2+2), ONLY m=1 (golden) has a superconformal chain.
"""
import os
import sys
from fractions import Fraction as Fr

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "frontier", "B224_golden_unique_susy_metallic"))
from coset_susy_uniqueness import (  # noqa: E402
    c_su2k_chain, c_minimal, c_scft, superconformal_minimal_models,
    metallic_level, metallic_chain_c, metallic_chain_is_susy,
)


def test_golden_chain_is_tricritical_ising():
    assert c_su2k_chain(3) == Fr(7, 10)            # su(2)_3 -> M(4,5)
    assert c_su2k_chain(3) == c_scft(3)            # = the first N=1 superconformal model


def test_unique_superconformal_minimal_model():
    scms = superconformal_minimal_models()
    assert scms == [(4, Fr(7, 10), 3)]             # ONLY M(4,5) is superconformal


def test_golden_is_the_unique_susy_metallic_chain():
    assert metallic_level(1) == 3                   # n=5=m^2+4 -> k=3 (golden/Fibonacci level)
    assert metallic_chain_c(1) == Fr(7, 10)
    assert metallic_chain_is_susy(1) is True
    assert all(metallic_chain_is_susy(m) is False for m in range(2, 12))
    assert [m for m in range(1, 30) if metallic_chain_is_susy(m)] == [1]


def test_silver_bronze_central_charges():
    assert metallic_chain_c(2) == Fr(25, 28)       # silver M(7,8)
    assert metallic_chain_c(3) == Fr(25, 26)       # bronze M(12,13)
    # c_m increases toward 1 (less special) for larger m; golden is the lowest
    assert metallic_chain_c(1) < metallic_chain_c(2) < metallic_chain_c(3) < 1


if __name__ == "__main__":
    for name, fn in sorted(globals().items()):
        if name.startswith("test_"):
            fn(); print(f"{name}  PASS")
    print("ALL CHECKS PASS")
