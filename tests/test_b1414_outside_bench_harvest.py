"""B1414 locks: (1) E81 -- the uncanonized isometry list undercounts on t10829 and the canonical one exhibits the |det(A-I)| = 3 rotation
on all nine members of the three-line class to nine tetrahedra; (2) memo 233 v2 re-derived exactly: H_1(Y_3) = Z/4 + Z/4 and the deck
3-cycles the three order-2 characters; 2T/Q_8 = Z/3 acts on {i, j, k} as a 3-cycle."""
import itertools
import pytest

NINE = ["m202", "s959", "v3461", "v3551", "o9_40999", "o9_43931", "t10829", "t12582", "o9_42897"]


def _det2(m):
    return m[0][0] * m[1][1] - m[0][1] * m[1][0]


def _rows(M, canonical):
    isos = M.is_isometric_to(M, return_isometries=True) if canonical else M.isomorphisms_to(M)
    out = []
    for iso in isos:
        for c, (img, A) in enumerate(zip(iso.cusp_images(), iso.cusp_maps())):
            if img != c:
                continue
            a, b, cc, d = int(A[0, 0]), int(A[0, 1]), int(A[1, 0]), int(A[1, 1])
            out.append((c, a * d - b * cc, abs((a - 1) * (d - 1) - b * cc)))
    return len(isos), out


def test_e81_nine_members_and_the_undercount():
    snappy = pytest.importorskip("snappy")
    for name in NINE:
        M = snappy.Manifold(name)
        n, rows = _rows(M, canonical=True)
        assert n == M.symmetry_group().order(), name
        cusps_with_3 = {c for c, det, v in rows if det == 1 and v == 3}
        assert cusps_with_3 == {0, 1}, (name, rows)
    # the witness of the defect: the census triangulation of t10829 shows 2 of its 12 isometries and no rotation of det 3
    M = snappy.Manifold("t10829")
    n_raw, rows_raw = _rows(M, canonical=False)
    assert n_raw == 2 and not any(det == 1 and v == 3 for _, det, v in rows_raw)


def test_memo233_v2_alexander_module_and_deck():
    import sympy as sp
    from sympy.matrices.normalforms import smith_normal_form
    R = sp.Matrix([[1, 1, -3], [-3, 1, 1], [1, -3, 1]])   # multiplication by t^2 - 3t + 1 on Z[t]/(t^3 - 1)
    d = sorted(abs(int(smith_normal_form(R, domain=sp.ZZ)[i, i])) for i in range(3))
    assert d == [1, 4, 4]
    cols = [tuple(int(R[i, j]) % 2 for i in range(3)) for j in range(3)]
    span = {(0, 0, 0)}
    for c in cols:
        span |= {tuple((a + b) % 2 for a, b in zip(s, c)) for s in span}
    assert len(span) == 2                       # H_1/2H_1 = (Z/2)^2
    canon = lambda v: min(tuple((a + b) % 2 for a, b in zip(v, s)) for s in span)
    classes = sorted({canon(v) for v in itertools.product((0, 1), repeat=3)} - {canon((0, 0, 0))})
    shift = lambda v: (v[2], v[0], v[1])       # multiplication by t
    perm = {c: canon(shift(c)) for c in classes}
    assert len(classes) == 3 and all(perm[c] != c for c in classes) and set(perm.values()) == set(classes)


def test_2T_mod_Q8_is_a_3_cycle_on_ijk():
    def qmul(p, q):
        a1, b1, c1, d1 = p; a2, b2, c2, d2 = q
        w = a1*a2 - b1*b2 - c1*c2 - d1*d2; x = a1*b2 + b1*a2 + c1*d2 - d1*c2
        y = a1*c2 - b1*d2 + c1*a2 + d1*b2; z = a1*d2 + b1*c2 - c1*b2 + d1*a2
        assert all(v % 2 == 0 for v in (w, x, y, z)); return (w // 2, x // 2, y // 2, z // 2)
    inv = lambda p: (p[0], -p[1], -p[2], -p[3])
    W = (1, 1, 1, 1); I, J, K = (0, 2, 0, 0), (0, 0, 2, 0), (0, 0, 0, 2)
    conj = {n: qmul(qmul(W, n), inv(W)) for n in (I, J, K)}
    assert conj[I] == J and conj[J] == K and conj[K] == I
    Q8 = {(2, 0, 0, 0), (-2, 0, 0, 0), I, (0, -2, 0, 0), J, (0, 0, -2, 0), K, (0, 0, 0, -2)}
    assert W not in Q8 and qmul(W, W) not in Q8 and qmul(qmul(W, W), W) == (-2, 0, 0, 0)
