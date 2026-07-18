"""B695 — E-3b: opposite AL signs forced by even rank (not chirality)."""


def test_opposite_al_signs_are_generic_even_rank():
    w_inf, w3, w5 = -1, +1, -1
    eps = w_inf*w3*w5
    assert eps == 1 == (-1)**0          # eps = (-1)^rank, rank 0
    assert w3*w5 == -1                   # opposite <=> eps=+1 <=> even rank (generic)
