"""B221 -- the golden chain's emergent SUSY: the EXACT anchor. Nothing to CLAIMS.md.

Load-bearing locks (all exact rational / exact symbolic):
  - c = 7/10 by three agreeing derivations (coset, Virasoro minimal, N=1 superconformal) -> the SUSY identity
  - the 6 tricritical-Ising primaries = {0,1/10,3/5,3/2,7/16,3/80} (incl. h=3/2 = the supercurrent)
  - the GKO coset (SU(2)_2 x SU(2)_1)/SU(2)_3 reproduces those weights mod 1 (golden SU(2)_3 -> TCI)
  - the golden quantum dimension d_1(SU(2)_3) = phi exactly
  - content(R^m L^m) = m (L39's period-controlling invariant IS the multiplicity)
"""
import os
import sys
from fractions import Fraction as Fr

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "frontier", "B221_golden_chain_susy"))
from coset_check import (  # noqa: E402
    c_su2, coset_central_charge, minimal_model_c, superconformal_c,
    kac_weights_m45, coset_weights_mod1, golden_quantum_dim_check, content, metallic_word,
)


def test_c_7_10_three_exact_derivations():
    # the SUSY identity: c=7/10 = coset = Virasoro minimal M(4,5) = N=1 superconformal (m=3)
    assert coset_central_charge() == Fr(7, 10)
    assert coset_central_charge() == c_su2(2) + c_su2(1) - c_su2(3)
    assert minimal_model_c(4) == Fr(7, 10)
    assert superconformal_c(3) == Fr(7, 10)
    assert coset_central_charge() == minimal_model_c(4) == superconformal_c(3)


def test_tricritical_ising_primaries():
    # the 6 primaries incl. h=3/2 (the supercurrent G, the SUSY generator)
    assert kac_weights_m45() == sorted([Fr(0), Fr(1, 10), Fr(3, 5), Fr(3, 2), Fr(7, 16), Fr(3, 80)])
    assert Fr(3, 2) in kac_weights_m45()


def test_coset_reproduces_weights_mod1():
    # GKO coset (SU(2)_2 x SU(2)_1)/SU(2)_3 -> the TCI weights mod 1 (SU(2)_3 = golden level)
    kac_mod1 = sorted(set(h % 1 for h in kac_weights_m45()))
    assert coset_weights_mod1() == kac_mod1


def test_golden_quantum_dimension_is_phi():
    ok, _ = golden_quantum_dim_check()
    assert ok  # d_1(SU(2)_3) = sin(3pi/5)/sin(pi/5) = (1+sqrt5)/2 = phi, exactly


def test_content_equals_multiplicity():
    # content(R^m L^m) = m for the metallic family (L39's invariant = the multiplicity)
    for m in range(1, 9):
        a, b, c, d = metallic_word(m)
        assert content(a, b, c, d) == m


if __name__ == "__main__":
    for name, fn in sorted(globals().items()):
        if name.startswith("test_"):
            fn(); print(f"{name}  PASS")
    print("ALL CHECKS PASS")
