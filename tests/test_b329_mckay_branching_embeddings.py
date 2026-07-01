"""B329 -- 27|_2T for both natural embeddings (Chat-1 handoff follow-on). sympy-only."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..',
                                'frontier', 'B329_mckay_branching_embeddings'))
import sympy as sp
from mckay_embeddings import (character_table, branch_principal, branch_trinification,
                              su3_three_is_complex, n1_n2)


def test_character_table_valid():
    reps, sizes, irreps = character_table()
    assert sum(int(irreps[k](reps[0]))**2 for k in irreps) == 24        # sum dim^2
    for a in irreps:
        for b in irreps:
            val = sp.simplify(sum(sizes[i] * irreps[a](reps[i]) * sp.conjugate(irreps[b](reps[i]))
                                  for i in range(7)) / 24)
            assert val == (1 if a == b else 0)


def test_principal_embedding_n1_equals_n2():
    dec_nonzero, dec = branch_principal()
    assert dec_nonzero == {'1': 3, "1'": 3, "1''": 3, '3': 6}           # factors through A4
    assert dec['2'] == 0 and dec["2'"] == 0 and dec["2''"] == 0          # no spinors
    n1, n2 = n1_n2(dec)
    assert sp.simplify(n1 - n2) == 0


def test_trinification_embedding_n1_equals_n2():
    dec_nonzero, dec = branch_trinification()
    assert dec_nonzero == {'1': 9, "1'": 3, "1''": 3, "2'": 3, "2''": 3}
    n1, n2 = n1_n2(dec)
    assert sp.simplify(n1 - n2) == 0                                     # both 0 -> Level 4


def test_nonvacuity_su3_three_is_complex():
    # the SU(3) 3|_2T = 1'+2' is genuinely non-self-conjugate (complex character);
    # it is the E6 27's balanced 3/3bar pairing that restores reality.
    vals, is_complex = su3_three_is_complex()
    assert is_complex
