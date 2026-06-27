"""B241 locks -- the Gang-Yonekura twist-knot SU(3) (flavor, universal) is NOT our level-rank SU(3)_2 (gauge,
golden). The golden structure is figure-eight-specific WITHIN the twist-knot family. Firewall-clean; nothing to
CLAIMS.md."""
import importlib.util
import pathlib

_PATH = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B241_twistknot_su3_vs_levelrank" / "twist_su3.py"
_spec = importlib.util.spec_from_file_location("b241", _PATH)
b241 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(b241)


def test_golden_structure_is_figure_eight_specific_within_twist_family():
    # 4_1 (amphicheiral) -> real & pure integer; 5_2, 6_1 (chiral) -> not real
    real41, pure41 = b241.golden_profile(*b241.TWIST["4_1"])
    assert real41 and pure41
    for nm in ("5_2", "6_1"):
        real, _ = b241.golden_profile(*b241.TWIST[nm])
        assert not real                                  # chiral -> complex (not in Q(sqrt5))


def test_only_figure_eight_is_real_in_twist_family():
    real_ones = [nm for nm, (bw, s) in b241.TWIST.items() if b241.golden_profile(bw, s)[0]]
    assert real_ones == ["4_1"]                          # the golden/level-rank structure is 4_1-specific
