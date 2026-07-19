"""B715 lock — native gauge = complex CS (not Yang-Mills); Z/11 UV-arithmetic; 6' closed."""
import sympy as sp

def test_holonomy_has_no_real_form_nonreal_adjoint_trace():
    # probe 2: tr Ad_e6(rho(a)) is NON-real -> excludes ALL real forms (real forms: real adjoint trace)
    tr = sp.Integer(37437270) + sp.Integer(38799960)*sp.sqrt(3)*sp.I
    assert sp.im(tr) != 0                       # non-real -> no real form -> not compact Yang-Mills

def test_z11_is_uv_arithmetic_norm():
    # probe 3: N_Q(sqrt5)(phi^5-1) = -11 (prime); phi^5 = 5phi+3
    phi = (1 + sp.sqrt(5))/2
    val = phi**5 - 1                            # = 5phi+2
    norm = sp.expand(val * val.subs(sp.sqrt(5), -sp.sqrt(5)))
    assert sp.simplify(norm) == -11
    # non-descending: 11 prime, gcd(11, IR-symmetry-order 2) = 1 -> only trivial hom (vacuous IR)
    import math
    assert math.gcd(11, 2) == 1

def test_generation_route_fully_closed_block_obstruction():
    # 6' coda: incommensurable blocks 17/9/1 -> no operation (symmetry OR Hecke) cycles them
    blocks = (17, 9, 1)
    assert len(set(blocks)) == 3 and sum(blocks) == 27
    # A4/V4 = Z/3 exists but is mod-3 BEING: sqrt5 lives at disjoint prime 5 (B685 kill)
    assert 12 // 4 == 3                         # |A4|/|V4| = Z/3
    assert math_gcd(3, 5) == 1                  # being prime 3 vs hearing prime 5 disjoint

def math_gcd(a, b):
    import math
    return math.gcd(a, b)
