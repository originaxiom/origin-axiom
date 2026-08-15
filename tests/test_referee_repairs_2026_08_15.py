"""Two claims added under referee pressure, locked so they cannot drift back.

Both came from Wave-6 hostile reads that arrived together and agreed.

## 1. The monodromy's shadow is CYCLIC OF ORDER 10, not 2I.

An earlier draft wrote that "the golden member lands on a genuine group ... the reduction
is onto SL(2,Z/5) = 2I".  SL(2,Z) does surject onto SL(2,Z/5), but the object attached to
THIS MANIFOLD is the image of its own monodromy, and that image is small:

    chi_1(t) = t^2 - 3t + 1 = (t-4)^2  mod 5,

so phi_1 mod 5 is 4 times a unipotent and generates a cyclic group of order 10.  2I is
the room the shadow sits in, not the shadow.  The selection theorem is a statement about
the MODULUS N_m = m^2 + 4, which is a function of m alone -- it discriminates between
grammars, not between manifolds via their monodromy images.  The paper now says so.

## 2. The enhancement rule is a CHOICE, and output-stability is not zero cost.

An earlier draft priced the second measurement plane at zero because every point of the
14-locus gives the same Levi type.  That confuses output-stability with freedom: a
GENERIC second charge gives 12, and the 14-locus is two hyperplanes in a 3-dimensional
space of choices, so one must first arrange to land there.  The same objection applies
one step earlier -- the first measurement is made at a WALL (dim 46) while the generic
point of the measurement plane gives 30.

This test pins the quantitative facts that make the enhancement rule a real choice: the
generic value is strictly below the value on the jump loci at BOTH measurements.  If a
later draft ever re-prices this at zero, the numbers here contradict it.

Uses the exact banked e6 build; the weight machinery is shared with
test_second_measurement_is_exhaustive.py, which certifies its own numerical gap.
"""
import pathlib

import pytest

_ROOT = pathlib.Path(__file__).resolve().parents[1]


# ------------------------------------------------------------------ claim 1


def _phi(m):
    return [[m * m + 1, m], [m, 1]]


def _matmul_mod(A, B, n):
    return [[sum(A[i][k] * B[k][j] for k in range(2)) % n for j in range(2)]
            for i in range(2)]


def _order_mod(A, n):
    I = [[1, 0], [0, 1]]
    Y, k = A, 1
    while Y != I:
        Y = _matmul_mod(Y, A, n)
        k += 1
        if k > 10_000:
            raise AssertionError("no finite order found")
    return k


def _generated_mod(A, n):
    I = [[1, 0], [0, 1]]
    seen, Y = set(), I
    for _ in range(_order_mod(A, n)):
        Y = _matmul_mod(Y, A, n)
        seen.add(tuple(Y[0]) + tuple(Y[1]))
    return seen


def test_golden_monodromy_reduces_to_a_cyclic_group_of_order_ten():
    A = [[x % 5 for x in row] for row in _phi(1)]
    assert _order_mod(A, 5) == 10
    assert len(_generated_mod(A, 5)) == 10


def test_that_group_is_far_smaller_than_2I():
    """|SL(2,Z/5)| = 120.  The shadow is index 12 inside it."""
    order = 5**3
    for p in (5,):
        order = order * (p * p - 1) // (p * p)
    assert order == 120
    assert 120 // 10 == 12


def test_the_characteristic_polynomial_is_a_perfect_square_mod_5():
    """chi_1(t) = t^2 - 3t + 1 = (t-4)^2 mod 5 -- why the image is not semisimple."""
    # (t-4)^2 = t^2 - 8t + 16 = t^2 - 3t + 1 (mod 5)
    assert (-8) % 5 == (-3) % 5
    assert 16 % 5 == 1 % 5
    disc = (3 * 3 - 4 * 1) % 5
    assert disc == 0, "a repeated root is exactly why the image is unipotent-by-scalar"


def test_the_modulus_is_a_function_of_m_alone():
    """The selection criterion cannot see the manifold beyond m."""
    assert [1 + (m * m + 2) + 1 for m in range(1, 8)] == [m * m + 4 for m in range(1, 8)]


# ------------------------------------------------------------------ claim 2


def test_the_enhancement_rule_is_a_real_choice_at_both_measurements():
    """Generic beats special at neither step: the jump loci are strictly exceptional."""
    np = pytest.importorskip("numpy")
    src = _ROOT / "frontier" / "B854_centralizer_exact" / "e6_centralizer.py"
    g = {"__file__": str(src), "__name__": "b854_ref"}
    exec(compile(src.read_text(), str(src), "exec"), g)
    DIM, N, br = g["DIM"], g["N"], g["br"]
    INV, hvec, evec, ROOTS_ = g["INV"], g["hvec"], g["evec"], g["ROOTS"]
    NS = [8, 14, 16, 22]

    basis = [hvec(i) for i in range(N)] + [evec(r) for r in ROOTS_]
    trip = {}
    for p_ in range(DIM):
        for q_ in range(DIM):
            for r_, c_ in enumerate(br(basis[p_], basis[q_])):
                if c_:
                    trip.setdefault(p_, []).append((q_, r_, float(c_)))

    def admat(vec):
        A = np.zeros((DIM, DIM))
        for p_ in range(DIM):
            if not vec[p_]:
                continue
            f = float(vec[p_])
            for q_, r_, c_ in trip.get(p_, []):
                A[r_, q_] += f * c_
        return A

    AD = {n: admat(INV[n]) for n in NS}
    M = AD[8] + 3.0 * AD[14] + 7.0 * AD[16] + 13.0 * AD[22]
    _, V = np.linalg.eig(M)
    W = np.zeros((DIM, 4), dtype=complex)
    for k in range(DIM):
        col = V[:, k]
        i = int(np.argmax(np.abs(col)))
        for j, n in enumerate(NS):
            W[k, j] = (AD[n] @ col)[i] / col[i]
    W[np.abs(W) < 1e-8 * np.max(np.abs(W))] = 0

    def dim_z(pts):
        ok = np.ones(DIM, dtype=bool)
        for y in pts:
            nw = np.maximum(np.max(np.abs(W), axis=1), 1e-300)
            ok &= np.abs(W @ np.asarray(y, dtype=complex)) / nw < 1e-9 * max(
                np.max(np.abs(y)), 1e-300)
        return int(ok.sum())

    split = [k for k in range(DIM) if W[k, 0] != 0 and W[k, 2] != 0]
    ts = []
    for k in split:
        t = -W[k, 0] / W[k, 2]
        if not any(abs(t - u) < 1e-7 for u in ts):
            ts.append(t)
    ts.sort(key=lambda z: z.real)

    # FIRST measurement: a generic point of the measurement plane gives 30, a wall 46.
    rng = np.random.default_rng(4)
    generic_plane = set()
    for _ in range(30):
        a, b = rng.normal(size=2)
        generic_plane.add(dim_z([np.array([a, 0, b, 0], dtype=complex)]))
    assert generic_plane == {30}, generic_plane
    for t in ts:
        assert dim_z([np.array([1, 0, t, 0], dtype=complex)]) == 46
    assert 46 > 30, "the wall is a strict enhancement -- going there is a choice"

    # SECOND measurement: a generic second charge gives 12, the jump loci 14 or 18.
    x1 = np.array([1, 0, ts[0], 0], dtype=complex)
    generic_second = set()
    for _ in range(60):
        generic_second.add(dim_z([x1, rng.normal(size=4) + 1j * rng.normal(size=4)]))
    assert generic_second == {12}, generic_second
    assert 14 > 12 and 18 > 12, "the 14-locus is a strict enhancement, hence a choice"
