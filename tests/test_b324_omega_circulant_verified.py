"""B324 lock -- Chat-1's omega-circulant generation matrix VERIFIED EXACTLY in Z[omega]. The order-3 commensurator
element g (g^3=I) conjugates the figure-eight Riley rep into three 'generations'; the cross-conjugate trace matrix
M[i,j]=tr(a_i b_j^-1) is EXACTLY a Z/3-circulant alpha*J + omega*P with beta-alpha = omega, eigenvalues (7-sqrt3 i, 1,
omega^2). But it is STRUCTURE, not values: the two subdominant eigenvalues are magnitude-DEGENERATE (|1|=|omega^2|=1) ->
no hierarchy (needs the CRUX); the omega is the ubiquitous Eisenstein cube root (B305/B309); the circulant is
tautological (g-conjugation, B323); and the three 'generations' are g-conjugates with the SAME character (B307-walled).
Exact structural fact; not a value crossing. Firewalled; nothing to CLAIMS.md."""
import importlib.util
import pathlib

_PATH = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B324_omega_circulant_verified" / "omega_circulant_verified.py"
_spec = importlib.util.spec_from_file_location("b324", _PATH)
b324 = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(b324)


def test_exact_circulant_with_omega():
    assert b324.g_cubed_is_identity()                              # g^3 = I
    assert b324.is_alpha_J_omega_P()                              # M = alpha*J + omega*P, beta-alpha = omega
    assert b324.EXACT_STRUCTURAL_FACT_VERIFIED


def test_eigenvalues_degenerate_no_hierarchy():
    assert b324.eigenvalue_magnitudes_squared() == [1, 1, 52]     # two magnitude-1 -> degenerate
    assert b324.MAGNITUDES_DEGENERATE_NO_HIERARCHY


def test_structure_not_values():
    assert b324.IS_STRUCTURE_NOT_VALUES
    assert b324.OMEGA_IS_THE_UBIQUITOUS_EISENSTEIN                # B305/B309, not a new value
    assert b324.CIRCULANT_IS_TAUTOLOGICAL                        # g-conjugation (B323)
    assert b324.GENERATIONS_ARE_CONJUGATES_SAME_CHARACTER        # B307-walled multiplicity
    assert b324.DERIVES_SM_VALUES is False
    assert b324.verdict()
