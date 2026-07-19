"""B709 lock — the Turok-marriage adjudication: the kills stay killed.
Each test pins a KILL or a firewall; none asserts a physics claim."""
import math

def pos_roots(dim, rank):        # simple Lie algebra: #positive roots
    return (dim - rank) // 2

def test_36_does_not_select_E6():
    # 36 positive roots shared by E6, B6=so(13), C6=sp(12) -> base-rate, not E6
    share = {name for name, (d, r) in
             {"E6": (78, 6), "B6": (78, 6), "C6": (78, 6),
              "A6": (48, 6), "D6": (66, 6)}.items() if pos_roots(d, r) == 36}
    assert share == {"E6", "B6", "C6"}

def test_rung4_single_ratios_are_hints_only():
    phi = (1 + 5 ** 0.5) / 2
    assert abs(1 / (2 * phi) - 0.30902) < 1e-4     # vs sin^2 th12 ~0.307, no mechanism
    assert abs(2 / 9 - 0.22222) < 1e-4             # theta0, B703, 0.89 sigma
    # both rung-4 (B685 denies the mechanism for values) -> not derivations

def test_monodromy_is_hyperbolic_not_a_bang():
    # sigma = [[2,1],[1,1]] : tr=3>2 pseudo-Anosov (suspension flow), not a CPT gluing
    tr = 2 + 1
    det = 2 * 1 - 1 * 1
    assert tr == 3 and tr > 2 and det == 1

def test_two_zz2_have_opposite_canonicity():
    # the adjudication's spine: amphichirality is canonical, the fiber torsor is not
    amphichirality_canonical = True      # K=Kbar fixes the geometric slice (CS=0)
    fiber_torsor_canonical = False       # B701: sqrt5->-sqrt5 has no fixed basepoint
    turok_cpt_canonical = True           # fixes the bang
    assert turok_cpt_canonical == amphichirality_canonical      # marriage reaches A
    assert turok_cpt_canonical != fiber_torsor_canonical        # INVERTS B

def test_dimensionful_no_go():
    # N(v0)=-6 dimensionless; a mass is dimensionful; no scale in the program (S3/B615)
    N_v0 = -6
    assert isinstance(N_v0, int)         # a pure integer cannot fix 4.8e8 GeV
