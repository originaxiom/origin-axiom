"""B1392 lock -- THE ENDS CARRY THE CHIRALITY (PROVED; the cusp algebra exact).

In the cusp (x, y, h), g = (dx^2 + dy^2 + dh^2)/h^2: the flat form a dx + b dy is harmonic with norm h sqrt(a^2 + b^2) and
|nabla omega| / |omega|^2 = sqrt2 / (h |alpha|) -> 0, so a Higgs class that does not vanish on a cusp seals it (the Witten potential
grows like h^2); the harmonic functions of h are h^0, h^2 and only h^0 is L^2 (the canonical representative); the undeformed 1-form
sector has Delta_H(h^s dx) = -s^2 h^s dx, so an unsealed cusp keeps the continuum [0, oo) (B1388's premise, derived).  On the 99
arithmetic census members and cube~3.24 every peripheral rank is >= 1 (a generic class seals every cusp); free cusps 86 on 35."""
import importlib.util
import warnings
from pathlib import Path

import sympy as sp

warnings.filterwarnings("ignore")
ROOT = Path(__file__).resolve().parents[1]
VER = ROOT / "frontier" / "B1392_the_ends_carry_the_chirality" / "verification"


def _load():
    spec = importlib.util.spec_from_file_location("b1392_ends", VER / "ends.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def test_the_cusp_algebra():
    E = _load()
    S = E.cusp_symbolics()
    h = sp.Symbol("h", positive=True)
    a, b, s = sp.Symbol("a", real=True), sp.Symbol("b", real=True), sp.Symbol("s", real=True)
    assert S["closed"] and S["coclosed"]
    assert sp.simplify(S["norm^2"] - h ** 2 * (a ** 2 + b ** 2)) == 0                   # a sealed cusp: |omega| = h |alpha|
    assert sp.simplify(S["|nabla omega|^2"] - 2 * h ** 2 * (a ** 2 + b ** 2)) == 0     # the Hessian term is O(1/h) of the potential
    assert sorted(S["harmonic exponents"]) == [0, 2] and S["L2 exponents"] == [0]       # the canonical (bounded-primitive) choice
    assert sp.simplify(S["Delta_H(h^s dx) / (h^s dx)"] + s ** 2) == 0                   # the unsealed continuum starts at 0


def test_the_members_peripheral_ranks():
    import snappy
    E = _load()
    for name, expect in (("m004", (1, [1])), ("m202", (2, [2, 2])), ("L6a4", (3, [1, 1, 1]))):
        assert E.peripheral_ranks(snappy.Manifold(name)) == expect
    M = snappy.Manifold("o10_150725").covers(3)[4].covers(3)[24]
    assert E.peripheral_ranks(M) == (5, [2, 1, 1, 2])                                     # cube~3.24: every cusp free
