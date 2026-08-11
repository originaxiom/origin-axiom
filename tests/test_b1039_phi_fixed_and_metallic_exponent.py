"""B1039 locks — the φ-fixed and metallic-exponent clusters, re-verified before restoration.

These deliberately do NOT exec `verify.py` (its grid check shells out to B198's Newton reproducer
and takes minutes). They INDEPENDENTLY recompute the load-bearing identities — an independent
reimplementation is a stronger lock than a re-execution — and read the banked `results.json` for
the expensive ones. If any breaks, the two restored LAW_MAP rows are wrong and must move with it.
"""
import json
import pathlib

import sympy as sp
from sympy import I, Rational

_ROOT = pathlib.Path(__file__).resolve().parents[1]
_ARC = _ROOT / "frontier" / "B1039_phi_fixed_and_metallic_exponent"
_R = json.loads((_ARC / "results.json").read_text(encoding="utf-8"))

_x, _y = sp.symbols("x y")


def _sym(M, d):
    """Sym^d of a 2x2 matrix — through M^T, so it is a homomorphism and not its opposite."""
    basis = [_x**(d - i) * _y**i for i in range(d + 1)]
    nx = M[0, 0] * _x + M[1, 0] * _y
    ny = M[0, 1] * _x + M[1, 1] * _y
    cols = []
    for b in basis:
        p = sp.Poly(sp.expand(b.subs({_x: nx, _y: ny}, simultaneous=True)), _x, _y)
        cols.append([sp.expand(p.coeff_monomial(bb)) for bb in basis])
    return sp.Matrix(cols).T


def _alg_dim(gens, n):
    def rk(ms):
        return sp.Matrix([list(m) for m in ms]).rank()
    seen, front, cur = [sp.eye(n)], [sp.eye(n)], 1
    for _ in range(2 * n * n):
        new = []
        for m in front:
            for g in gens:
                p = sp.expand(m * g)
                if rk(seen + [p]) > cur:
                    seen, cur = seen + [p], rk(seen + [p])
                    new.append(p)
        if not new or cur >= n * n:
            break
        front = new
    return cur


def test_every_check_passes():
    failed = [k for k, c in _R["checks"].items() if not c["pass"]]
    assert failed == [], failed


def test_the_instrument_is_a_homomorphism_not_its_opposite():
    """Substituting coordinates directly makes Sym^d ANTI-multiplicative — B154's contravariance
    bug-class. The control is what catches it, so the control itself is locked."""
    p, q, r, s, u, v_, w, z = sp.symbols("p q r s u v w z")
    M = sp.Matrix([[p, q], [r, s]])
    N = sp.Matrix([[u, v_], [w, z]])
    for d in range(1, 4):
        assert sp.simplify(_sym(M * N, d) - _sym(M, d) * _sym(N, d)) == sp.zeros(d + 1)
        assert sp.simplify(sp.factor(_sym(M, d).det()) - M.det()**Rational(d * (d + 1), 2)) == 0


def test_the_bridge_equation_selects_the_unique_irreducible_phi_fixed_point():
    """(x,y,z) -> (z, x, xz-y) has exactly two fixed points; kappa = 2 marks the reducible one."""
    X, Y, Z = sp.symbols("X Y Z")
    sols = sp.solve([Z - X, X - Y, X * Z - Y - Z], [X, Y, Z], dict=True)
    kap = X**2 + Y**2 + Z**2 - X * Y * Z - 2
    got = {(int(s[X]), int(s[Y]), int(s[Z])): sp.simplify(kap.subs(s)) for s in sols}
    assert set(got) == {(0, 0, 0), (2, 2, 2)}
    assert got[(2, 2, 2)] == 2 and got[(0, 0, 0)] == -2


def test_the_phi_fixed_principal_point_is_Q8_and_its_tower_is_reducible():
    A = sp.Matrix([[I, 0], [0, -I]])
    B = sp.Matrix([[0, 1], [-1, 0]])
    assert (A.trace(), B.trace(), (A * B).trace()) == (0, 0, 0)
    assert sp.simplify(A * B + B * A) == sp.zeros(2)
    assert _alg_dim([_sym(A, 1), _sym(B, 1)], 2) == 4          # irreducible at n = 2
    for n in (3, 4, 5):                                        # and reducible above
        assert _alg_dim([_sym(A, n - 1), _sym(B, n - 1)], n) < n * n


def test_finite_image_does_NOT_imply_a_reducible_tower():
    """B141 Item 3's slogan, falsified: SL(2,3) is finite and its Sym^2 is IRREDUCIBLE. The real
    bound is the max irrep dimension (2 for Q8, 3 for SL(2,3)) — sharp at exactly n = 3."""
    A = sp.Matrix([[I, 0], [0, -I]])
    B = sp.Matrix([[0, 1], [-1, 0]])
    C = Rational(1, 2) * sp.Matrix([[-1 + I, -1 + I], [1 + I, -1 - I]])
    assert sp.simplify(C.det()) == 1
    assert _alg_dim([_sym(M, 2) for M in (A, B, C)], 3) == 9
    assert _R["checks"]["A8_CORRECTION_finite_image_does_NOT_imply_a_reducible_tower"]["order"] == 24


def test_the_klein4_lemma_holds_as_a_group_identity_not_one_example():
    """B142's own probe exhibited a single commuting pair; the universally quantified lemma is
    two involutions whose product is an involution commute."""
    from sympy.combinatorics.free_groups import free_group
    from sympy.combinatorics.fp_groups import FpGroup
    F, a, b = free_group("a b")
    K = FpGroup(F, [a**2, b**2, (a * b)**2])
    assert K.order() == 4
    assert K.reduce(a * b * a**-1 * b**-1) == F.identity


def test_spectrum_alone_does_not_give_an_involution():
    """The unstated hypothesis: A must be SEMISIMPLE."""
    J = sp.Matrix([[1, 0, 0], [0, -1, 1], [0, 0, -1]])
    assert J.eigenvals() == {sp.Integer(1): 1, sp.Integer(-1): 2} and J.det() == 1
    assert sp.simplify(J * J - sp.eye(3)) != sp.zeros(3)
    assert sp.simplify(sp.diag(1, -1, -1)**2 - sp.eye(3)) == sp.zeros(3)


def _red(w):
    out = []
    for g in w:
        if out and out[-1][0] == g[0] and out[-1][1] == -g[1]:
            out.pop()
        else:
            out.append(g)
    return tuple(out)


def _inv(w):
    return _red(tuple((s, -e) for s, e in reversed(w)))


def _mul(*ws):
    o = ()
    for w in ws:
        o = _red(o + w)
    return o


def test_the_monodromy_conjugates_the_longitude_by_A_to_the_m():
    """phi_m([A,B]) = A^m [A,B] A^-m, exactly in the free group — the identity that DERIVES the
    cusp meridian mu = A^-m t. B154 verified m = 1, 2."""
    WA, WB = (("A", 1),), (("B", 1),)

    def sub(w, ia, ib):
        o = ()
        for s, e in w:
            im = ia if s == "A" else ib
            o = _red(o + (im if e == 1 else _inv(im)))
        return o

    def phi(w, m):
        for _ in range(m):
            w = sub(w, _mul(WA, WB), WB)
        for _ in range(m):
            w = sub(w, WA, _mul(WA, WB))
        return w

    def pw(w, k):
        if k == 0:
            return ()
        return _mul(*([w] * k)) if k > 0 else _inv(_mul(*([w] * (-k))))

    comm = _mul(WA, WB, _inv(WA), _inv(WB))
    assert phi(WA, 1) == _mul(WA, WA, WB) and phi(WB, 1) == _mul(WA, WB)
    assert phi(WA, 2) == _mul(pw(WA, 3), WB, pw(WA, 2), WB)
    for m in range(1, 9):
        assert phi(comm, m) == _mul(pw(WA, m), comm, pw(WA, -m)), m
        # and the meridian exponent is FORCED: A^-k t is peripheral only at k = m.
        # The k-sweep must cover m, or the check is vacuous rather than passing.
        ks = [k for k in range(m + 4) if _mul(pw(WA, m - k), comm, pw(WA, k - m)) == comm]
        assert ks == [m], (m, ks)


def test_the_banked_SL5_certificate_still_certifies_k_equals_2():
    import mpmath as mp
    mp.mp.dps = 40
    D = json.loads((_ROOT / "frontier" / "B198_metallic_exponent_CAS" / "cert_sl5o5_rep.json")
                   .read_text(encoding="utf-8"))
    o, n, exps = D["o"], D["n"], D["exps"]
    t = mp.matrix([[mp.mpc(mp.mpf(D["t"][i][j][0]), mp.mpf(D["t"][i][j][1]))
                    for j in range(n)] for i in range(n)])
    z = mp.exp(2j * mp.pi / o)
    A = mp.diag([z**k for k in exps])
    Ai = mp.diag([1 / (z**k) for k in exps])
    B = Ai * Ai * t * A * (t**-1)
    mu = Ai * t
    L = A * B * (A**-1) * (B**-1)

    def nm(M):
        return float(max(abs(M[i, j]) for i in range(n) for j in range(n)))

    assert nm(L - mu**2) < 1e-15
    assert min(nm(L - mu**k) for k in (0, 1, 3, 4)) > 1.0        # neighbours excluded
    ev = [complex(e) for e in mp.eig(mu, left=False, right=False)]
    assert max(abs(abs(e) - 1) for e in ev) > 0.1                # loxodromic
    assert not any(max(abs(e**d - 1) for e in ev) < 1e-6 for d in range(1, 121))  # infinite order


def test_no_closed_form_k_of_o_and_m_survives():
    """o=4 and o=8 both give k=3 on the mu-infinite stratum, so k = 7-o (which predicts 3 and -1)
    and k = 4-m(o-3) are both refuted. Measured by verify.py re-running B198's own reproducer."""
    c = _R["checks"]["B7_no_closed_form_k(o,m)_survives_o=4_and_o=8_BOTH_give_k=3"]
    assert c["pass"]
    assert set(c["grid"]) == {"o=4,m=1", "o=8,m=1"}
    for cell in c["grid"].values():
        assert list(cell) == ["3"] and cell["3"] >= 8


def test_the_two_restorations_landed_with_their_scope():
    lawmap = (_ROOT / "docs" / "LAW_MAP.md").read_text(encoding="utf-8")
    assert "FINITENESS VERSUS DENSITY SPLITS THE TOWER" in lawmap
    assert "ORDER-DETERMINED, NOT RANK-DETERMINED" in lawmap
    # the corrections that make each restoration honest rather than a re-assertion
    assert "SL(2,3)" in lawmap and "max irrep dim" in lawmap and "semisimple" in lawmap
    assert "sublocus" in lawmap and "complete cusped rep" in lawmap and "REFUTED" in lawmap
    for b in ("B141", "B142", "B154", "B198"):
        assert b in lawmap, b


def test_what_is_carried_by_citation_is_named_not_implied():
    cb = _R["carried_by_citation"]
    assert any("SnapPy" in v for v in cb.values())          # B142's s776 cartography
    assert any("primary" in v for v in cb.values())         # B154's component count
    assert any("CONJECTURE" in v for v in cb.values())      # B141 Item 4
