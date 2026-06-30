"""B312 lock -- Face IV <-> SM-content (the last in-sandbox frontier). The object's TQFT quantization (Face IV, SU(2)_k
WRT) houses the SAME E6 the content carries -- as the CIZ exceptional modular invariant of SU(2)_10 (Coxeter 12,
exponents {1,4,5,7,8,11}, the Lie-group E6 of the cascade B305, the McKay 2T atom B266 as the classical limit). Face IV
houses BOTH ends (E6@10 Eisenstein, E8@28 golden -- two of the three CIZ exceptionals); the fig-8 trace field Q(sqrt-3)
is compatible via the triality (Q(sqrt-3) in Q(zeta_12), 3|12=h(E6)). BUT the level k=10 is generic to SU(2)_10, so even
Face IV gives the structural theorem -- the quantization houses the FORM, not the SM values. Nothing to CLAIMS.md."""
import importlib.util
import pathlib

_PATH = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B312_face_iv_houses_the_form" / "face_iv_houses_the_form.py"
_spec = importlib.util.spec_from_file_location("b312", _PATH)
b312 = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(b312)


def test_one_e6_three_ade_hats():
    assert b312.e6_exponents_consistent()                         # sum=36 positive roots, symmetric about h/2
    assert b312.ciz_e6_level() == 10                              # CIZ E6 modular invariant at k = h-2 = 10
    assert b312.ciz_e6_diagonal_is_exponents()                    # diagonal labels+1 == E6 exponents (same E6)
    assert b312.ONE_E6_THREE_ADE_HATS


def test_face_iv_houses_both_ends():
    assert b312.two_ends_are_ciz_exceptionals()                   # E6@10 (Eisenstein) + E8@28 (golden)
    assert b312.ciz_exceptional_levels() == {"E6": 10, "E7": 16, "E8": 28}
    assert b312.FACE_IV_HOUSES_BOTH_ENDS


def test_arithmetic_compatible_via_triality():
    assert b312.trace_field_in_cyclotomic()                       # Q(sqrt-3) in Q(zeta_12), 3|12=h(E6)
    assert b312.ARITHMETIC_COMPATIBLE_VIA_TRIALITY


def test_structural_theorem_at_the_quantum_level():
    assert b312.LEVEL_IS_GENERIC_NOT_SELECTED                     # k=10 a feature of SU(2)_10, not object-specific
    assert b312.FACE_IV_HOUSES_THE_FORM_NOT_THE_VALUES
    assert b312.DERIVES_SM_VALUES is False
    assert b312.verdict()
