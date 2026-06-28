"""B266 lock (R6 addendum) -- the E6/E8 ends are arithmetically asymmetric at the group level: pi_1(4_1) surjects
onto 2T=SL(2,F_3) (E6 leg, genuine) but NOT onto A_5 or 2I=SL(2,F_5) (E8 leg, field-level only). Verified by
GAP GQuotients (frontier/B266_arithmetic_selects_e6/verify_surjections.py); confirms Stuebner 2025. FIREWALLED."""
import importlib.util
import pathlib

_PATH = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B266_arithmetic_selects_e6" / "b266_surjection_verdict.py"
_spec = importlib.util.spec_from_file_location("b266sv", _PATH)
b266sv = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(b266sv)


def test_e6_leg_is_a_genuine_surjection():
    assert b266sv.SURJECTION_COUNTS["2T = SL(2,3)"] == 2     # load-bearing E6 leg


def test_e8_leg_has_no_4_1_surjection():
    assert b266sv.SURJECTION_COUNTS["A5 = PSL(2,5)"] == 0    # Stuebner 2025
    assert b266sv.SURJECTION_COUNTS["2I = SL(2,5)"] == 0     # => E8 end is field-level, not a 4_1 surjection
    assert b266sv.verdict()
