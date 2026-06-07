"""B116 -- locking test: the theta-split (B112) and the Sym two-sequence (B103) reconciliation.
The Sym two-sequence = the actual tower (matches the resolved SL(5)); the theta-split = the tower only n<=5
(differs by a single degree=rank promotion) and DIVERGES from Sym at n=6 (V26/V27). This CORRECTS B112's
'sign half for all n' to 'sign half n<=5; all-n OPEN'. NO physics; P1-P16 untouched."""
import importlib.util
import pathlib

_ROOT = pathlib.Path(__file__).resolve().parents[1]
_spec = importlib.util.spec_from_file_location(
    "b116", _ROOT / "frontier" / "B116_reconcile_theta_sym" / "probe.py")
B = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(B)


def test_sym_two_sequence_equals_sl5_tower():
    s = B.sym_equals_sl5_tower()
    assert s["matches"] is True                     # Sym = the resolved SL(5) tower (B61+B62)
    assert s["has_top_char_M5"] is True             # incl. char(M^5), the degree=rank top power


def test_single_promotion_through_n5_diverge_at_n6():
    # n<=5: Sym = theta-split + one degree=rank promotion; n>=6: NOT a single promotion (diverge)
    assert B.differ_by_single_promotion(3) and B.differ_by_single_promotion(4) and B.differ_by_single_promotion(5)
    assert not B.differ_by_single_promotion(6)
    assert not B.differ_by_single_promotion(7)


def test_divergence_at_n6_matches_v26_v27():
    d = B.divergence_at_n6()
    assert d["diverge"] is True
    assert d["a1_sym_vs_theta"] == (2, 3)           # a_1: Sym 2 vs theta 3
    assert d["a2_sym_vs_theta"] == (3, 2)           # a_2: Sym 3 vs theta 2
    assert d["b2_sym_vs_theta"] == (1, 2)           # b_2: Sym 1 vs theta 2
    assert d["a3_both"] == (2, 2)                    # both agree a_3(n=6)=2


def test_b112_correction_recorded():
    c = B.b112_correction()
    assert "n<=5" in c["corrected_claim"] and "OPEN" in c["corrected_claim"]
