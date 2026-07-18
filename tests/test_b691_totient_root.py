"""B691 — the totient asymmetry: 3 prime-totient (minimal), 5 composite."""
import sympy as sp


def test_totient_asymmetry_root_of_b685():
    assert sp.totient(3) == 2 and sp.isprime(sp.totient(3))     # phi(3)=2 prime
    assert sp.totient(5) == 4 and not sp.isprime(sp.totient(5))  # phi(5)=4 composite
    t = sp.symbols("t")
    # being shape roots (zeta_3/zeta_6): z^2-z+1=0
    assert sp.discriminant(t**2 - t + 1, t) == -3
    # hearing Gaussian periods: golden-related t^2+t-1
    phi = (1 + sp.sqrt(5))/2
    assert sp.simplify((t**2 + t - 1).subs(t, phi - 1)) == 0
