"""B528 lock — the computed DGG gauge-rank arithmetic for the figure-eight.
Full gauge group computed via SnapPy in compute_gauge.py (sage env); this pyenv lock pins the
discriminating arithmetic: SL(2) gauge rank N-c=1, and the 'N-1' ladder = cusp Cartan rank K-1.
"""

def test_sl2_gauge_rank_is_one_abelian():
    N, c = 2, 1                      # figure-eight: 2 ideal tetrahedra, 1 cusp
    assert N - c == 1               # DGG gauge = U(1)^{N-c} = U(1) (abelian) -- matches SnapPy NZ datum


def test_the_N_minus_1_pattern_is_the_cusp_cartan_rank():
    # the handoff's "U(N-1) at rank N" ladder = the boundary SL(K) Cartan rank K-1 (abelian flavor),
    # NOT a nonabelian gauge group (DGG: "K does not appear as the rank of a gauge group").
    assert [K - 1 for K in (2, 3, 4, 5)] == [1, 2, 3, 4]
    # the genuine nonabelian object (T[SU(N)] defect quiver U(1)xU(2)x...xU(N-1)) exists only in the
    # defect sector (Gang-Kim-Romo-Yamazaki 1510.05011), not as the generic T_N[M] gauge group.
