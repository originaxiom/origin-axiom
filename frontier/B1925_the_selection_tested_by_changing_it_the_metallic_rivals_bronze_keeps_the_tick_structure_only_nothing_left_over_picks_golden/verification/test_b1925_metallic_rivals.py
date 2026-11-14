"""The lock of B1925. Each test recomputes, with a planted case that must fail."""
import pathlib, sys
import numpy as np
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import metallic_rivals as MR            # noqa: E402
import selection_equivalence as SE      # noqa: E402


def parity_law(m, use_ground=False):
    J = MR.mat(m); G = J.dot(J); N = m * m + 4
    T = G if use_ground else J
    pts = MR.kernel_mod(G + np.eye(2, dtype=object), N); gen = MR.cyclic_generator(pts, N)
    if gen is None:
        return None
    ok = True
    for s in (1, -1):
        for n in range(6):
            for e in (0, 1):
                X = s * np.linalg.matrix_power(T, n).dot(np.linalg.matrix_power(MR.K, e)) if n else s * np.linalg.matrix_power(MR.K, e)
                sc = MR.scalar_on(X, gen, N, pts)
                swaps = sc is not None and sc % N not in (1, N - 1)
                ok &= (sc is not None) and (swaps == ((n + e) % 2 == 1))
    return ok


def test_odd_metallic_keep_the_tick_structure():
    for m in (1, 3, 5):
        assert parity_law(m) is True
        assert parity_law(m, use_ground=True) is False          # planted: the ground (det +1) in place of the tick


def test_even_metallic_have_no_line():
    for m in (2, 4):
        assert parity_law(m) is None


def test_torsion_orders():
    for m in range(1, 6):
        J = MR.mat(m); G = J.dot(J); I = np.eye(2, dtype=object)
        assert MR.smith_2x2(G - I) == [m, m] and MR.smith_2x2(J - I) == [1, m]
        assert MR.smith_2x2(G + I) != [m, m]                    # planted: the frustrated level is not the torsion


def test_se1_is_level_five():
    import itertools
    for a, b, c, d in itertools.product(range(-4, 5), repeat=4):
        if a * d - b * c != 1 or a + d < 3:
            continue
        tf = SE.smith(a - 1, b, c, d - 1) == (1, 1)
        lev = SE.smith_order(a + 1, b, c, d + 1)
        assert tf == (lev == 5) == (a + d == 3)
        assert SE.smith_order(-a - 1, -b, -c, -d - 1) == lev    # -A exchanges the two orders
    # planted: reading the level off A - I instead breaks the equivalence
    assert not all((SE.smith(a - 1, b, c, d - 1) == (1, 1)) == (SE.smith_order(a - 1, b, c, d - 1) == 5)
                   for a, b, c, d in [(2, 1, 1, 1), (3, 1, 2, 1)])


def test_snappy_names():
    try:
        import snappy
    except ImportError:
        return
    for word, name in (("b-+R", "m000"), ("b-+RRR", "m005"), ("b++LR", "m004"), ("b+-LR", "m003")):
        assert str(snappy.Manifold(word).identify()[0]).startswith(name)
