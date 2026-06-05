"""B70 (Path D, V55) -- the symbolic-m pinv-limit construction reproduces the SL(3) tower.

The full n=3 gate (m=1..7 + interpolation) is ~8 min; here we check a single m (m=2) reproduces the
SL(3) tower at m=2 -- a fast validation that the from-first-principles symbolic-m construction is
correct (the e_2 closure is automatic via the n x n matrix arithmetic)."""
import importlib.util
import pathlib

import sympy as sp

_ROOT = pathlib.Path(__file__).resolve().parents[1]
_spec = importlib.util.spec_from_file_location(
    "b70_smp", _ROOT / "frontier" / "B70_trace_ring" / "symbolic_m_pinv.py")
smp = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(smp)


def test_tower_reference():
    """char(M^-1)=t^2+mt-1, char(M^2)=t^2-(m^2+2)t+1, char(M^3)=t^2-(m^3+3m)t-1."""
    m, t = sp.symbols("m t")
    assert sp.expand(smp.char_factor(-1) - (t**2 + m * t - 1)) == 0
    assert sp.expand(smp.char_factor(2) - (t**2 - (m**2 + 2) * t + 1)) == 0
    assert sp.expand(smp.char_factor(3) - (t**2 - (m**3 + 3 * m) * t - 1)) == 0


def test_sl3_jacobian_reproduces_tower_at_m2():
    """The symbolic-m construction at m=2 reproduces the SL(3) tower at m=2 (single-m fast check)."""
    t = sp.symbols("t")
    Jm, DT0_at = smp.fixed_line_jacobian(3, smp.SL3_WORDS, L=8, mvals=(2,))
    cp = sp.factor(DT0_at[2].charpoly(t).as_expr())
    tower2 = sp.factor(smp.sl3_tower().subs(sp.symbols("m"), 2))
    assert sp.expand(cp - tower2) == 0
