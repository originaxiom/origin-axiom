"""B242 locks -- the three-SU(3) trichotomy: level-rank SU(2)_3<->SU(3)_2 = complex conjugation at the golden
root, EXACT coincidence iff amphicheiral. Firewall-clean; nothing to CLAIMS.md."""
import importlib.util
import pathlib

_PATH = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B242_three_su3_trichotomy" / "trichotomy.py"
_spec = importlib.util.spec_from_file_location("b242", _PATH)
b242 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(b242)


def test_figure_eight_levelrank_coincidence_is_golden():
    s2, s3 = b242.levelrank_pair(b242.HOMFLY["4_1 (amph)"])
    assert abs(s2 - (-2 / b242.PHI)) < 1e-9            # SU(2)_3 fundamental = -2/phi (= B240 J_2)
    assert abs(s3 - (-2 / b242.PHI)) < 1e-9            # SU(3)_2 fundamental = -2/phi (exact coincidence)


def test_exact_coincidence_iff_amphicheiral():
    for nm, P in b242.HOMFLY.items():
        s2, s3 = b242.levelrank_pair(P)
        exact = abs(s2 - s3) < 1e-9
        assert exact == b242.is_amphicheiral(P)        # level-rank coincidence <=> amphicheiral


def test_chiral_knots_are_complex_conjugate_pairs():
    for nm in ("3_1 (chiral)", "5_2 (chiral)"):
        s2, s3 = b242.levelrank_pair(b242.HOMFLY[nm])
        assert abs(s2 - s3) > 1e-6                      # differ
        assert abs(s2 - s3.conjugate()) < 1e-9         # but are exact complex conjugates (level-rank = conj)
