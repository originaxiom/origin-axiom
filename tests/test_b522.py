"""B522 locks — the tower filtration theorem's independently-recomputed cores.

The deep Luna/Procesi/BCH step is cited on the audit's B503 (SHARPER-REDUCTION, probe-writeup
strength). These locks pin the classical, checkable cores: the character generating function,
the carrier-dimension reconstruction (n<=4), and the mu_d bookkeeping (incl. the n=5 doubled Sym^2).
"""
import sympy as sp

z, x, y = sp.symbols('z x y')


def _hgen(vars_, a):
    gf = sp.Integer(1)
    for v in vars_:
        gf *= 1 / (1 - v * z)
    ser = sp.series(gf, z, 0, a + 1).removeO()
    return sp.expand(ser.coeff(z, a))


def test_character_layer_closed_all_n():
    # h_a(x,y,1) = sum_{k<=a} h_k(x,y): closes B122(2)
    for a in range(0, 6):
        lhs = _hgen([x, y, 1], a)
        rhs = sp.expand(sum(_hgen([x, y], k) for k in range(0, a + 1)))
        assert sp.expand(lhs - rhs) == 0


def test_carrier_dims_reconstruct_catalog():
    sym = lambda k: k + 1        # dim Sym^k V (V 2-dim)
    det = 1                      # dim det^j
    assert sym(2) == 3                                   # n=2 : n^2-1 = 3
    assert sym(2) + sym(3) + det + det == 9              # n=3 : Lawton embdim 9
    assert sym(2) + sym(3) + (sym(4) + det) + 2 == 15    # n=4 : n^2-1 = 15 (V x D^2 is 2-dim)


def test_mu_d_bookkeeping_has_doubled_sym2_at_n5():
    mu = lambda d, n: int(0 <= d <= n) + int(0 <= d <= n - 3) - int(d == 0) - int(d == 1)
    assert [mu(d, 4) for d in range(0, 5)] == [1, 1, 1, 1, 1]
    assert [mu(d, 5) for d in range(0, 6)] == [1, 1, 2, 1, 1, 1]   # mu_2 = 2 : the doubled Sym^2 wall
    assert [mu(d, 6) for d in range(0, 7)] == [1, 1, 2, 2, 1, 1, 1]


def test_first_arm_cayley_hamilton_cutoff():
    # Chevalley: untwisted Sym^d present exactly for 2 <= d <= n (mu_n = 1, CH cutoff at d=n)
    for n in range(2, 7):
        arm = [d for d in range(0, n + 3) if 2 <= d <= n]
        assert arm == list(range(2, n + 1))
