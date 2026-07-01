"""B334 -- the seam's Hilbert class field = the two-ended compositum (Chat handoff). sympy-only."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'frontier', 'B334_seam_hilbert_class_field'))
from seam_hcf import splitting_law, form_cross_check, null_137, prime_class


def test_hilbert_class_field_is_compositum():
    # principal <=> splits completely in Q(sqrt5,sqrt-3); the splitting law + form cross-check confirm HCF.
    prin, nonp = splitting_law()
    assert prin == [1, 4] and nonp == [2, 8]
    assert form_cross_check() == 0                 # 0 mismatches vs the principal form x^2+xy+4y^2


def test_137_is_dead_as_prediction():
    cls137, frac = null_137()
    assert cls137 == "non-principal"
    assert 0.4 < frac < 0.65                        # ~1/2 -> coin flip -> no SM content
