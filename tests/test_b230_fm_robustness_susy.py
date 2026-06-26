"""B230 -- golden's SUSY-uniqueness is robust to AFM/FM; the FM silver c-coincidence is NOT genuine SUSY.
Nothing to CLAIMS.md.

Load-bearing locks:
  - AFM golden = M(4,5) = TCI (c=7/10, genuinely super via the B228 coset coincidence).
  - FM silver = Z_6 parafermion, c=5/4 = c(SM(6)) -- a central-charge COINCIDENCE, NOT genuine SUSY
    (Z_6 parafermion coset SU(2)_6/U(1) != super coset (SU(2)_4 x SU(2)_2)/SU(2)_6).
  - so the only genuine N=1 super metallic chain (any coupling) is golden+AFM -- robust to AFM/FM.
"""
import os
import sys
from fractions import Fraction as Fr

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "frontier", "B230_fm_robustness_susy"))
from fm_robustness import (  # noqa: E402
    afm_c, fm_c, c_scft, super_c_set, parafermion_coset, super_coset,
)


def test_afm_golden_is_tci():
    assert afm_c(1) == Fr(7, 10)                    # golden+AFM = TCI (genuinely super, B228)


def test_fm_silver_is_central_charge_coincidence_not_susy():
    sc = super_c_set()
    assert fm_c(2) == Fr(5, 4) == c_scft(6)         # silver FM Z_6 has c = c(SM(6)) -- a coincidence
    assert parafermion_coset(6) != super_coset(6)   # but different cosets -> different CFTs -> not genuine SUSY


def test_no_other_fm_central_charge_coincidence_low_m():
    sc = super_c_set()
    # only m=2 has even a central-charge coincidence among low m; and it is not genuine SUSY anyway
    coincidences = [m for m in range(1, 30) if fm_c(m) in sc]
    assert coincidences == [2]


if __name__ == "__main__":
    for name, fn in sorted(globals().items()):
        if name.startswith("test_"):
            fn(); print(f"{name}  PASS")
    print("ALL CHECKS PASS")
