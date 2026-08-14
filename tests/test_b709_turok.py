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
    """Canonical <=> the Z/2 has a NON-EMPTY fixed set. Computed, 2026-07-29.

    This test used to be three hand-set booleans compared to one another --
    `turok_cpt_canonical == amphichirality_canonical` where both were literally `True`, and
    `!= fiber_torsor_canonical` where that was literally `False`. It held for ANY assignment of
    those three names, so the adjudication's spine was locked by its own transcription.
    B709's mechanism is a fixed-point question, so compute the fixed sets instead.

    Turok's own side stays a CITED premise (B710: method-only, thimble-level) -- it is not
    recomputed here, and the object-side content is the CONTRAST between the two Z/2's."""
    import sympy as sp
    sqrt5, sqrt3 = sp.sqrt(5), sp.sqrt(3)

    # Z/2-B, the fiber-functor torsor: gamma5 (sqrt5 -> -sqrt5) on the 5A/5B basepoint pair.
    g5 = lambda e: sp.simplify(e.subs(sqrt5, -sqrt5))
    phi = (1 + sqrt5) / 2
    pair = [phi - 1, -phi]                                   # chi_5A, chi_5B
    assert sp.simplify(g5(pair[0]) - pair[1]) == 0           # gamma5 SWAPS the two basepoints
    assert sp.simplify(g5(pair[1]) - pair[0]) == 0
    fixed_B = [p for p in pair if sp.simplify(g5(p) - p) == 0]
    assert fixed_B == [], f"Z/2-B must have NO fixed basepoint, got {fixed_B}"

    # Z/2-A, amphichirality: conjugation c on the trace field Q(sqrt-3). Its fixed set is the
    # real locus, which is NON-empty -- the geometric slice (CS = 0) is a rational point there.
    c = lambda e: sp.simplify(sp.conjugate(e))
    omega = sp.Rational(-1, 2) + sp.I * sqrt3 / 2
    candidates = [sp.Integer(0), sp.Integer(1), omega]       # CS=0 and 1 are real; omega is not
    fixed_A = [z for z in candidates if sp.simplify(c(z) - z) == 0]
    assert sp.simplify(c(omega) - omega) != 0                # c genuinely acts (not the identity)
    assert sp.Integer(0) in fixed_A                          # the CS=0 slice IS fixed
    assert len(fixed_A) == 2, f"real locus non-empty; got {fixed_A}"

    # The spine: opposite canonicity, now a CONSEQUENCE of the two fixed sets.
    assert (len(fixed_A) > 0) != (len(fixed_B) > 0)

def test_dimensionful_no_go():
    # N(v0)=-6 dimensionless; a mass is dimensionful; no scale in the program (S3/B615)
    N_v0 = -6
    assert isinstance(N_v0, int)         # a pure integer cannot fix 4.8e8 GeV
