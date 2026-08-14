"""B766 audit locks -- cc3 scrutiny of the measurement torsor (compute-grade)."""
import sympy as sp

u, x, y = sp.symbols("u x y")
phi = (1 + sp.sqrt(5)) / 2
omega = sp.Rational(-1, 2) + sp.I * sp.sqrt(3) / 2

A = sp.Matrix([[1, 1], [0, 1]])
B_u = sp.Matrix([[1, 0], [-u, 1]])


def sym2(M):
    a, b, c, d = M[0,0], M[0,1], M[1,0], M[1,1]
    return sp.Matrix([
        [a**2,   2*a*b,     b**2],
        [a*c,    a*d+b*c,   b*d],
        [c**2,   2*c*d,     d**2]
    ])


def test_c_flips_T4_chirality():
    curve = y**2 - (x**2 - 1)*y + (x**2 - 1)
    sols = sp.solve(curve.subs(x, 2), y)
    sol_set = set(sp.nsimplify(s) for s in sols)
    conj_set = set(sp.nsimplify(sp.conjugate(s)) for s in sols)
    assert sol_set == conj_set
    assert all(sp.simplify(sp.conjugate(s) - s) != 0 for s in sols)


def test_theta_fixes_T4_via_trace_symmetry():
    assert sp.simplify((A * B_u).trace() - (B_u * A).trace()) == 0


def test_gamma3_equals_c_on_omega():
    c_omega = sp.conjugate(omega)
    g3_omega = sp.Rational(-1, 2) - sp.I * sp.sqrt(3) / 2
    assert sp.simplify(c_omega - g3_omega) == 0


def test_gamma3_flips_T4():
    sol_a = sp.Rational(3, 2) + sp.I * sp.sqrt(3) / 2
    sol_b = sp.Rational(3, 2) - sp.I * sp.sqrt(3) / 2
    assert sp.simplify(sp.conjugate(sol_a) - sol_b) == 0
    assert sp.simplify(sp.conjugate(sol_b) - sol_a) == 0


def test_c_flips_T6_chord_sign():
    chord = sp.diff(sp.expand((A * B_u).trace()**2 - 1), u).subs(u, omega)
    chord_im = sp.simplify(sp.im(chord))
    assert chord_im == sp.sqrt(3)
    assert sp.simplify(sp.im(sp.conjugate(chord)) + chord_im) == 0


def test_theta_flips_T6_at_sym2_matrix_level():
    AB = (A * B_u).subs(u, omega)
    BA = (B_u * A).subs(u, omega)
    S2_odd = sp.simplify(sym2(AB) - sym2(BA))
    assert any(S2_odd[i, j] != 0 for i in range(3) for j in range(3)), \
        "theta-odd sector of Sym^2 must be nontrivial"


def test_theta_flips_T6_sym2_derivatives_differ():
    S2_AB = sym2(A * B_u)
    S2_BA = sym2(B_u * A)
    diffs = []
    for i in range(3):
        for j in range(3):
            d = sp.simplify(
                sp.diff(S2_AB[i, j], u).subs(u, omega)
                - sp.diff(S2_BA[i, j], u).subs(u, omega))
            if d != 0:
                diffs.append((i, j, d))
    assert len(diffs) >= 1, "at least one Sym^2 entry derivative must differ under theta"


def test_gamma5_flips_T7_time_direction():
    assert sp.simplify((1 - phi)**2 - 1/phi**2) == 0


def test_c_fixes_T7_eigenvalues_real():
    M = sp.Matrix([[2, 1], [1, 1]])
    for ev in M.eigenvals():
        assert sp.simplify(sp.im(ev)) == 0


def test_theta_fixes_T7_reversed_eigenvalues():
    M_RL = sp.Matrix([[2, 1], [1, 1]])
    M_LR = sp.Matrix([[1, 1], [1, 2]])
    assert sorted(M_RL.eigenvals()) == sorted(M_LR.eigenvals())


def test_gamma5_swaps_A5_irreps():
    chi_5A = phi - 1
    chi_5B = -phi
    chi_5A_under_g5 = chi_5A.subs(sp.sqrt(5), -sp.sqrt(5))
    assert sp.simplify(chi_5A_under_g5 - chi_5B) == 0


# --- the flip vectors, DERIVED (2026-07-29 vacuity repair) --------------------------------
# These four vectors used to be hand-typed literals, and every lattice test below compared a
# literal to a literal: `assert (0, 0, 1) == (0, 0, 1)`, and a "match cc" test whose two sides
# were identical hardcoded dicts. They passed unconditionally -- the F2 rank, the T7 = T3
# identification and T6 = T4 (+) theta could not have failed however the involutions actually
# behaved, so the cross-seat check verified nothing but its own transcription. Each bit is now
# computed from the same objects the tests above exercise; FINDINGS marks all of them "derived".
def _flip_vectors():
    """Return {axis: (c_bit, theta_bit, gamma5_bit)}, every bit from an actual computation."""
    g5 = lambda e: e.subs(sp.sqrt(5), -sp.sqrt(5))       # the golden Galois, sqrt5 -> -sqrt5
    vecs = {}

    # T4 -- chirality: the Riley curve's two geometric roots at x = 2.
    roots = sp.solve((y**2 - (x**2 - 1)*y + (x**2 - 1)).subs(x, 2), y)
    c_T4 = int(sp.simplify(sp.conjugate(roots[0]) - roots[0]) != 0)   # conjugation moves it
    th_T4 = int(sp.simplify((A * B_u).trace() - (B_u * A).trace()) != 0)  # trace symmetry fixes
    g5_T4 = int(any(g5(r) != r for r in roots))          # roots lie in Q(sqrt-3): no sqrt5
    vecs["T4"] = (c_T4, th_T4, g5_T4)

    # T6 -- the chord: d/du[tr(AB)^2 - 1] at u = omega, whose value is purely imaginary sqrt3.
    chord = sp.diff(sp.expand((A * B_u).trace()**2 - 1), u).subs(u, omega)
    c_T6 = int(sp.simplify(sp.conjugate(chord) - chord) != 0)
    S2_odd = sp.simplify(sym2((A * B_u).subs(u, omega)) - sym2((B_u * A).subs(u, omega)))
    th_T6 = int(any(S2_odd[i, j] != 0 for i in range(3) for j in range(3)))
    g5_T6 = int(sp.simplify(g5(chord) - chord) != 0)
    vecs["T6"] = (c_T6, th_T6, g5_T6)

    # T7 -- time's direction: the eigenvalues phi^2, phi^-2 of RL.
    M_RL, M_LR = sp.Matrix([[2, 1], [1, 1]]), sp.Matrix([[1, 1], [1, 2]])
    evs = list(M_RL.eigenvals())
    c_T7 = int(any(sp.simplify(sp.im(e)) != 0 for e in evs))          # real => fixed
    th_T7 = int(sorted(M_RL.eigenvals()) != sorted(M_LR.eigenvals()))  # reversal fixes
    g5_T7 = int(any(sp.simplify(g5(e) - e) != 0 for e in evs))         # sqrt5 -> -sqrt5 inverts
    vecs["T7"] = (c_T7, th_T7, g5_T7)

    # T3 -- the basepoint bit: the A5 irreps 5A/5B, chi_5A = phi - 1, chi_5B = -phi.
    chi_5A, chi_5B = phi - 1, -phi
    c_T3 = int(sp.simplify(sp.im(chi_5A)) != 0)          # character is real => c fixes it
    th_T3 = int(sp.simplify(sp.conjugate(chi_5A) - chi_5A) != 0)   # contragredient = conj on chi
    g5_T3 = int(sp.simplify(g5(chi_5A) - chi_5B) == 0 and sp.simplify(chi_5A - chi_5B) != 0)
    vecs["T3"] = (c_T3, th_T3, g5_T3)
    return vecs


def test_flip_vectors_match_cc():
    """A REAL cross-seat check: cc's banked literals vs vectors derived here from scratch."""
    cc_vecs = {"T4": (1, 0, 0), "T6": (1, 1, 0), "T7": (0, 0, 1), "T3": (0, 0, 1)}
    assert _flip_vectors() == cc_vecs


def test_f2_rank_is_three():
    mat = [list(v) for v in _flip_vectors().values()]
    r = 0
    for col in range(3):
        piv = next((i for i in range(r, len(mat)) if mat[i][col] % 2), None)
        if piv is None:
            continue
        mat[r], mat[piv] = mat[piv], mat[r]
        for i in range(len(mat)):
            if i != r and mat[i][col] % 2:
                mat[i] = [(a + b) % 2 for a, b in zip(mat[i], mat[r])]
        r += 1
    assert r == 3, "rank 3 = B733's menu rank (saturated)"


def test_T7_equals_T3_same_flip_vector():
    v = _flip_vectors()
    assert v["T7"] == v["T3"]          # time's arrow and the basepoint are ONE choice
    assert v["T7"] == (0, 0, 1)        # and that choice is the gamma5 (golden) branch


def test_T6_is_T4_xor_theta():
    v = _flip_vectors()
    theta_vec = (0, 1, 0)
    assert tuple((a + b) % 2 for a, b in zip(v["T4"], theta_vec)) == v["T6"]


def test_T1_unmoved_by_involution_set():
    """T1 is the FINDINGS' honest residue -- 'reported, uncounted; a named door'.

    No computation in this arc moves it, so unlike the four above there is no bit to derive:
    this locks that T1 is absent from the derived set, NOT that a computation found it fixed.
    Stated as the arc states it, rather than dressed up as a verified zero."""
    assert "T1" not in _flip_vectors()


def test_riley_disc_minus_three():
    curve = y**2 - (x**2 - 1)*y + (x**2 - 1)
    disc = sp.discriminant(curve.subs(x, 2), y)
    assert disc == -3
