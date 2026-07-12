"""Locks for B553 — Seat-1 session-3 verified items."""


def test_metallic_torsion_m_squared():
    for m in range(1, 8):
        tr = m*m + 2                     # metallic monodromy trace
        det_AmI = 1 - tr + 1             # det(A-I) = det - tr + 1, det=1
        assert abs(det_AmI) == m*m


def test_odd_fibonacci_markoff_cluster():
    fib = [0, 1]
    while len(fib) < 25:
        fib.append(fib[-1] + fib[-2])
    odd = [fib[2*n-1] for n in range(1, 12)]
    assert odd == [1, 2, 5, 13, 34, 89, 233, 610, 1597, 4181, 10946]


def test_sl5_dimension_is_n2_minus_1_not_rank():
    n = 5
    assert n*n - 1 == 24           # program's banked trace-coordinate count (B66)
    assert n - 1 == 4              # the rank — what Seat-1's "correction" gave
    assert (n*n - 1) != (n - 1)    # they are different quantities
