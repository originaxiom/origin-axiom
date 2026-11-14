"""The lock of B1926: recomputes the odd-level zero and the twisted classes at a small prime, with planted cases."""
import pathlib, sys
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import odd_ticks_no_modules as O     # noqa: E402

P = 661                              # 1 mod 220 = lcm of the torsion exponents at levels 3 to 6


def test_tick_inverts_the_scar():
    for n in range(1, 7):
        g, e = O.find_g(n)
        assert e == (-1) ** n
    # planted: a conjugator of the wrong sign is refused
    g, e = O.find_g(3)
    assert O.red(g + O.LAM + O.inv(g)) != O.sigma_n(O.LAM, 3)


def test_odd_levels_have_no_class_on_the_scar():
    for n in (3, 5):
        r = O.run(n, P)
        assert r["characters"] > 0 and r["with_c_lambda_nonzero"] == 0


def test_twisted_characters_free_the_scar():
    for n in (3, 5):
        r = O.run(n, P, keep_mu=False)
        assert r["characters"] > 0 and r["with_c_lambda_nonzero"] == r["characters"]


def test_even_levels_carry_classes():
    for n in (4, 6):
        r = O.run(n, P)
        assert r["characters"] > 0 and r["with_c_lambda_nonzero"] == r["characters"]


def test_twisted_classes_lift_to_the_double_cover():
    import twisted_descends as TD
    tw, ok, mu1, cls = TD.check(3, P)
    assert tw > 0 and tw == ok == mu1 == cls

