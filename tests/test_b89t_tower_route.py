"""B89-T (Task T) -- locking tests: the cohomological route to the metallic tower is closed
(char(M)^(n^2-1) != tower), and the explicit two-sequence Sym-power product equals the proved
(n<=4) / structural (n=5) tower SYMBOLICALLY in m, with the n=6 discriminator a_3 = 2."""
import importlib.util
import pathlib
import sys

import sympy as sp

_ROOT = pathlib.Path(__file__).resolve().parents[1]
_spec = importlib.util.spec_from_file_location(
    "b89t", _ROOT / "frontier" / "B89T_tower_route" / "probe.py")
B = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(B)


def test_sym_product_matches_B80_actual_Jm_n4():
    """Cross-check (CC-web audit): the two-sequence Sym product equals B80's ACTUAL symbolic J(m) char
    poly at n=4 -- not just a hardcoded target string. Rules out a coincidence with a wrong target."""
    spec = importlib.util.spec_from_file_location(
        "b65", _ROOT / "frontier" / "B65_sl4_symbolic_jacobian" / "probe.py")
    b65 = importlib.util.module_from_spec(spec)
    sys.modules["b65"] = b65                      # required: b65 uses @dataclass
    spec.loader.exec_module(b65)
    t = sp.symbols("t")
    charJ = sp.expand(b65.symbolic_jacobian().charpoly(t).as_expr())   # the real 15x15 J(m) (B80/B65)
    sym = sp.expand(B.sym_tower(4).subs({B.t: t}))
    assert sp.expand(charJ - sym) == 0


def test_cohomological_route_fails():
    """The H^1(F_2; ad rho) action at the (trivial-rep) fixed line is char(M)^(n^2-1) -- NOT the
    tower -- for n=3,4,5. The cohomological route does not carry the tower (C1 fails)."""
    for n in (3, 4, 5):
        coh = B.cohomological_at_trivial(n)
        assert sp.expand(coh - B.char_Mk(1) ** (n * n - 1)) == 0
        assert sp.expand(coh - B.proved_tower(n)) != 0


def test_sym_tower_equals_proved_tower_symbolic_m():
    """The explicit two-sequence Sym product equals the proved (n<=4) / structural (n=5) tower,
    SYMBOLICALLY in m (strengthening B58's m=1-only check); degree n^2-1."""
    for n in (3, 4, 5):
        assert sp.expand(B.sym_tower(n) - B.proved_tower(n)) == 0
        assert sp.degree(B.sym_tower(n), B.t) == n * n - 1


def test_n6_discriminator_a3_is_2():
    """The Sym tower predicts a_3(n=6) = 2 (char(M^3) multiplicity), matching the theta-split (B62)
    and overruling B66's gauge-corrupted pinv a_3 = 1."""
    assert B.char_M3_multiplicity(6) == 2


def test_sym_power_factorization_both_parities():
    """Sanity anchor: each Sym^d(M) factors over the Dickson catalog in BOTH parities -- so the odd
    powers char(M^-1), char(M), char(M^3) DO arise (Sym^3 = char(M^-1) char(M^3))."""
    # Sym^3(M) = char(M^-1) * char(M^3)
    lhs = sp.expand(B.sym_charpoly(3))
    rhs = sp.expand(B.char_Mk(-1) * B.char_Mk(3))
    assert sp.expand(lhs - rhs) == 0
    # Sym^4(M) = (t-1) * char(-M^2) * char(M^4)
    lhs4 = sp.expand(B.sym_charpoly(4))
    rhs4 = sp.expand((B.t - 1) * B.char_Mk(2, -1) * B.char_Mk(4))
    assert sp.expand(lhs4 - rhs4) == 0
