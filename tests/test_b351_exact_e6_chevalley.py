"""B351 lock -- the exact Chevalley e6 (part 1 of the {4,8}-integrability program).

Frenkel-Kac cocycle structure constants with the FULL Jacobi identity verified exactly
over the integers (76,076 triples, 0 violations); the principal sl2 with exact relations;
the exponent decomposition e6 = (+) Sym^{2m}, m in {1,4,5,7,8,11}; the diagram involution
theta as a verified automorphism with the f4 (+) 26 split; and theta's signs on the six
exponent lines = (-1)^{m+1} -- settling B347's flagged sign-pattern question at the
algebra level. Pure ints/Fractions; no numerics. Nothing to CLAIMS.md."""
import importlib.util
import pathlib

_PATH = (pathlib.Path(__file__).resolve().parents[1] / "frontier"
         / "B351_exact_e6_chevalley" / "exact_e6.py")
_spec = importlib.util.spec_from_file_location("b351", _PATH)
b351 = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(b351)


def test_root_system():
    assert len(b351.POS) == 36
    assert len(b351.ROOTS) == 72


def test_bracket_antisymmetry():
    assert b351.antisymmetry_holds()


def test_jacobi_exact_zero_violations():
    # the load-bearing check: every one of the 76,076 basis triples, exact integers
    assert b351.jacobi_residual_count() == 0


def test_principal_sl2_exact():
    assert [int(x) for x in b351.PRINCIPAL_C] == [16, 22, 30, 42, 30, 16]
    assert b351.principal_relations_hold()


def test_exponent_decomposition():
    assert b351.exponent_weights() == [2 * m for m in b351.EXPONENTS]
    assert b351.EXPONENTS == [1, 4, 5, 7, 8, 11]


def test_theta_is_an_involutive_automorphism_with_f4_split():
    auto, invol, fixed, minus = b351.theta_checks()
    assert auto and invol
    assert fixed == 52          # f4
    assert minus == 26          # the e6/f4 coset


def test_theta_signs_on_exponent_lines_are_minus_one_to_m_plus_one():
    assert b351.theta_commutes_with_principal_sl2()
    signs = b351.theta_signs_on_exponent_lines()
    assert signs == {m: (-1) ** (m + 1) for m in b351.EXPONENTS}
    assert [m for m, s in signs.items() if s == -1] == [4, 8]   # the 26 / escape sector
