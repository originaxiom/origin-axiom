"""B239 locks -- the reconciled unimodular trace-field law (referee-proof). Pure arithmetic, pyenv.
Firewall: rep-theory/arithmetic; nothing to CLAIMS.md."""
import importlib.util
import pathlib

_PATH = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B239_reconciled_trace_field_law" / "reconciled_law.py"
_spec = importlib.util.spec_from_file_location("b239_law", _PATH)
b239 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(b239)


def test_sqrt5_robust_across_representatives():
    """RL (trace 3, det +1) and M_1 (trace 1, det -1) both give Q(sqrt5) -- 'trace 1' was a representative."""
    assert b239.sqfree(b239.disc(3, 1)) == 5
    assert b239.sqfree(b239.disc(1, -1)) == 5


def test_only_two_imaginary_trace_fields():
    """the ONLY imaginary quadratic trace fields of a unimodular element are Q(i) and Q(sqrt-3) (disc -4 floor)."""
    assert set(b239.imaginary_trace_fields()) == {-1, -3}


def test_E7_needs_even_trace_and_sqrtm7_below_floor():
    """Q(sqrt2) (E7) only at even trace; odd trace => disc=1 mod4; Q(sqrt-7) unreachable (below the -4 floor)."""
    assert b239.trace_of_field(2) and all(t % 2 == 0 for t, _ in b239.trace_of_field(2))
    assert all(b239.disc(t, det) % 4 == 1 for det in (1, -1) for t in (-3, -1, 1, 3))
    assert b239.trace_of_field(-7) == []
