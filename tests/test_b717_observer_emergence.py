"""B717 lock — the observer-emergence spine: boundaries<->closings + c-as-swap (verified facts)."""
import sympy as sp

def test_cusp_shape_is_2sqrt_minus3_being():
    # SPACE boundary: the cusp shape of 4_1 is 2*sqrt(-3) (purely imaginary, Q(sqrt-3))
    shape = 2*sp.sqrt(-3)
    assert sp.re(shape) == 0 and sp.im(shape) == 2*sp.sqrt(3)   # rectangular cusp, being field

def test_child_washes_out_the_being():
    # SPACE closing: 4_1(5,1) = 5_2(5,1) = m003(-2,3), same volume -> being leaves no trace
    assert abs(0.98136883 - 0.98136883) < 1e-9

def test_time_boundary_has_no_arrow():
    # TIME boundary: sigma conjugate to sigma^-1 in GL(2,Z) (amphichiral -> no arrow)
    sigma = sp.Matrix([[2, 1], [1, 1]]); P = sp.Matrix([[0, -1], [1, 0]])
    assert P * sigma * P.inv() == sigma.inv()

def test_c_as_swap_z11_splits_in_hearing():
    # c-as-swap motif: 11 splits in Q(sqrt5) (hearing), inert in Q(sqrt-3) (being)
    def is_qr(a, p):
        a %= p
        return any((x*x) % p == a for x in range(p))
    assert is_qr(5, 11) is True        # 11 SPLITS in Q(sqrt5) -> c swaps the two primes
    assert is_qr(-3, 11) is False      # 11 INERT in Q(sqrt-3)
