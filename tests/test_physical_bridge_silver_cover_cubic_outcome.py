"""Post-result locks; freshly computed polynomials, never stored transcripts."""
import importlib.util
from functools import lru_cache
from pathlib import Path
import sympy as s

BASE = Path(__file__).resolve().parents[1]/'reports/physical_bridge_2026_09_05/silver_cover_cubic_2026_10_12'
z = s.symbols('z')


@lru_cache(None)
def both():
    out = []
    for name in ('probe', 'reference'):
        spec = importlib.util.spec_from_file_location('cover_cubic_outcome_'+name, BASE/(name+'.py'))
        mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
        out.append(mod.run())
    return out


def polynomial(text):
    return s.Poly(s.sympify(text, locals={'z': z}), z, extension=s.sqrt(2))


def test_actual_QdL_tensor_is_nonzero_not_just_algorithm_agreement():
    a, b = both()
    values = [polynomial(x) for x in a['channels']['QdL']['polynomials']]
    assert any(not x.is_zero for x in values)
    assert sum(not x.is_zero for x in values) == 4
    assert b['channels']['QdL']['zero_certified'] is False


def test_actual_eLL_and_udd_zero_with_nonzero_terms():
    a, b = both()
    for key in ('eLL', 'udd'):
        row = a['channels'][key]
        assert all(polynomial(x).is_zero for x in row['polynomials'])
        assert any(not polynomial(x).is_zero for x in row['first_terms'])
        assert any(not polynomial(x).is_zero for x in row['second_terms'])
        assert all(polynomial(x).as_expr() == polynomial(y).as_expr()
                   for x, y in zip(row['first_terms'], row['second_terms']))
        assert b['channels'][key]['zero_certified'] is True


def test_nonzero_tensor_keeps_actual_two_odd_vertex_not_three_even_copies():
    a, b = both()
    row = a['channels']['QdL']; parities = (0, 1, 1)
    indices = []
    for index, entry in enumerate(row['polynomials']):
        if not polynomial(entry).is_zero:
            ix = (index//9, (index % 9)//3, index % 3)
            assert sum(parities[j] for j in ix) == 2
            assert row['parity_forbidden'][index] is False
            indices.append(ix)
    assert len(indices) == 4
    assert b['checks']['two_odd_not_discarded']
