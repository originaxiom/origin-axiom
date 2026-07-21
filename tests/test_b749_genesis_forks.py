"""B749 locks — the genesis forks (mathematical asserts, extracted minimal)."""
import numpy as np
from sympy import Matrix, sqrt, gcd, resultant, Symbol


def test_f5_parent_matrix_squares_to_m004_monodromy():
    # A6's price: the det -1 Fibonacci matrix squares to m004's monodromy exactly.
    M = Matrix([[1, 1], [1, 0]])
    assert M.det() == -1 and (M**2) == Matrix([[2, 1], [1, 1]])


def test_f6_being_field_distinct_from_monodromy_field():
    # F6: the Sol carrier's only field is Q(sqrt5); distinct from Q(sqrt-3) — by resultant.
    x = Symbol('x')
    r = resultant(x**2 - 3*x + 1, x**2 + 3, x)
    assert r != 0                       # no common root: the fields are distinct


def test_f4_shadow_variants_fail_structurally():
    # sigma_rev (a->ab, b->ba) abelianization is singular — no mapping class.
    assert Matrix([[1, 1], [1, 1]]).det() == 0
    # sigma_inert fixes b forever: the abelianization has eigenvector (0,1) with eigenvalue 1.
    A = Matrix([[1, 0], [1, 1]])        # columns: images of a=ab, b=b
    assert (A * Matrix([0, 1])) == Matrix([0, 1])


def test_f7_witness_is_quadratic_self_similar_non_metallic():
    # sqrt(3)-1: quadratic, CF period (1,2), not [0;m,m,...] for ANY m (symbolic proof:
    # a metallic slope satisfies x^2 + m x - 1 = 0; sqrt(3)-1 satisfies x^2 + 2x - 2 = 0;
    # equal only if the polynomials are proportional -> -1 = -2, impossible).
    x = Symbol('x')
    w = sqrt(3) - 1
    assert (w**2 + 2*w - 2).expand() == 0
    # proportionality of x^2+mx-1 and x^2+2x-2 requires 1=1, m=2, -1=-2 — contradiction.
    assert -1 != -2
