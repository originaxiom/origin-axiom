"""B1675 -- no thread keeps a record, verified on main (the SM seat's W34). Live: the blocks' dimensions from Q8's
characters (m_0 = the multiplicity of the trivial character in Sym^{2k} rho_Q; dim H^1 = dim V + m_0, rank = dim V - m_0,
private = 2 m_0), with a bite (the binary octahedral group would give a different table); and a hyperbolic matrix tensored
with a finite-order map has no fixed vector. Stored: main's independent census (no thread keeps a private class on 758
states; L and R keep one, P two at rank three)."""
import cmath, pathlib
import numpy as np
A = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B1675_no_thread_keeps_a_record_verified"


def sym_char(theta, k):                      # character of Sym^{2k} of SU(2) at eigenvalues e^{+-i theta}
    return sum(cmath.exp(1j * (2 * k - 2 * j) * theta) for j in range(2 * k + 1)).real


def m0(angles_with_counts, k):
    order = sum(c for _, c in angles_with_counts)
    return round(sum(c * sym_char(t, k) for t, c in angles_with_counts) / order)


Q8 = [(0.0, 1), (cmath.pi, 1), (cmath.pi / 2, 6)]                          # +1, -1, and the six of order 4


def test_the_blocks_at_the_common_point():
    table = []
    for k in (1, 2, 3):
        d, m = 2 * k + 1, m0(Q8, k)
        table.append((d, d + m, d - m, 2 * m))
    assert table == [(3, 3, 3, 0), (5, 7, 3, 4), (7, 8, 6, 2)]
    # bite: the binary octahedral group 2O (order 48) has fewer invariants, so a different table
    O2 = [(0.0, 1), (cmath.pi, 1), (cmath.pi / 2, 6 + 12), (cmath.pi / 3, 8), (2 * cmath.pi / 3, 8), (cmath.pi / 4, 6), (3 * cmath.pi / 4, 6)]
    assert [m0(O2, k) for k in (1, 2, 3)] != [m0(Q8, k) for k in (1, 2, 3)]


def test_hyperbolic_times_finite_order_fixes_nothing():
    rng = np.random.default_rng(1675)
    H = np.array([[2.0, 1.0], [1.0, 1.0]])                                   # LR, eigenvalues phi^{+-2}
    for _ in range(20):
        th = rng.uniform(0, 2 * np.pi); Ufin = np.array([[np.cos(th), -np.sin(th)], [np.sin(th), np.cos(th)]])
        M = np.kron(H, Ufin)
        assert min(abs(np.linalg.eigvals(M) - 1)) > 0.5                       # no eigenvalue 1: no fixed vector


def test_stored_census():
    run = (A / "verification" / "main_check" / "v2_w34_independent_run.txt").read_text()
    assert "threads keeping a private class (any block): 0" in run
    assert "rank 3 (k=1,2) private kept by L 1" in run and "rank 3 (k=1,2) private kept by P 2 | rank 4 (k=1,2,3): 3" in run
    assert "number of cyclic states 379 x2 = 758" in run
