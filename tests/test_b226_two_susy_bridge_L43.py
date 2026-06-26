"""B226 / L43 -- the two-SUSY bridge, resolved (literature-grounded). Nothing to CLAIMS.md.

Load-bearing locks (firewall-clean bookkeeping): the two sides' central charges, and that the resolution is
recorded with its references. (The physics reading is in speculations/S040; the literature verdict is cited,
not derived in-sandbox.)
"""
import os
import sys
from fractions import Fraction as Fr

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "frontier", "B226_two_susy_bridge_L43"))
from l43_grounding import c_su2_wzw, coset_c, VERDICT, REFERENCES, SIDE_A, SIDE_B  # noqa: E402


def test_side_a_central_charges():
    assert c_su2_wzw(3) == Fr(9, 5)        # SU(2)_3 WZW boundary CFT
    assert coset_c() == Fr(7, 10)          # golden-chain coset = tricritical Ising (N=1 SCFT)
    assert SIDE_A["c"] == Fr(7, 10)


def test_two_faces_separated_by_hyperbolicity():
    # the verdict: the two SUSYs are two faces, separated by the hyperbolic/non-hyperbolic divide
    assert "TWO FACES" in VERDICT
    assert "non-hyperbolic" in VERDICT.lower() and "hyperbolic" in VERDICT.lower()
    assert "SU(2)_3" in VERDICT                     # the shared ingredient
    assert "Seifert" in SIDE_A["3d-3d realization"]  # TCI from a non-hyperbolic Seifert space
    assert "SL(2,C)" in SIDE_B["CS"]                 # figure-eight = complex CS / 3d gravity


def test_references_present():
    refs = " ".join(REFERENCES)
    for arx in ["2405.16377", "2511.04524", "2512.23122"]:   # the Gang et al. minimal-model-from-Seifert papers
        assert arx in refs


if __name__ == "__main__":
    for name, fn in sorted(globals().items()):
        if name.startswith("test_"):
            fn(); print(f"{name}  PASS")
    print("ALL CHECKS PASS")
