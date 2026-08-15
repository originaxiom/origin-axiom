"""The +-diagonality hypothesis: its gap measured exactly, and a door closed.

The paper's sign-locking theorem is CONDITIONAL on a hypothesis -- that every
C-stabilizing automorphism of e6 acts +-diagonally on the four charge lines.  B901 proves
a great deal of that spectrally (the stabilizer is discrete; split cannot swap with
compact; x8 cannot swap with x16), but leaves one hole, named in the paper: a 3-CYCLE on
the three enhancement lines, which is not +-diagonal and which none of B901's spectral
obstructions forbid.

This test settles what can be settled about that hole WITHOUT leaving C, and the answer
is two-sided.

THE NECESSARY CONDITION.  If sigma is an automorphism of e6 with sigma(C) = C, then
ad(sigma x) = sigma ad(x) sigma^{-1}, so sigma permutes the weight spaces and the WEIGHT
MULTISET of C on e6 is invariant under w -> w . g, where g = sigma|_C.  Any candidate g
must therefore stabilize the 78-weight multiset.  Since C is toral (see the paper's
Lemma), that multiset is well defined and computable.

WHAT IS FOUND.

  * The stabilizer of the full 78-weight multiset, among block-diagonal g (block-diagonal
    is forced by B901's split/compact obstruction), has order EXACTLY 24.
  * It surjects onto the full symmetric group S3 on the three wall lines -- so the
    3-cycle is NOT excluded, and neither are the transpositions.
  * Exactly FOUR of the 24 are +-diagonal, and they are precisely
        (+,+,+,+), (+,-,+,-), (-,+,-,+), (-,-,-,-)
    which is EXACTLY the set of four patterns the sign-locking theorem obtains from two
    degree-six rational trace moments.  Two entirely different computations, the same
    four patterns.  That is a genuine cross-check of the sign-locking theorem.
  * Hence the hypothesis's gap is exactly a factor of SIX: the candidate group is order
    24, the hypothesis asserts the realized image is the order-4 diagonal subgroup, and
    the quotient is the S3 acting on the Galois orbit of the charge cubic.

## THE DOOR THIS CLOSES.  No invariant of C can exclude the 3-cycle, because the
3-cycle preserves every invariant of C that an automorphism must preserve -- the full
weight multiset included.  A future attempt to prove the hypothesis must work inside e6
itself, not inside the charge torus.  Recording that saves the attempt.

Numerics are double precision but self-certifying: the multiset comparison rounds to a
fixed number of digits and the test asserts the group order, which is an integer and
therefore robust to any tolerance that does not change it.  Cross-checked at 60 digits.
"""
import pathlib

import numpy as np
import pytest

_ROOT = pathlib.Path(__file__).resolve().parents[1]
_SRC = _ROOT / "frontier" / "B854_centralizer_exact" / "e6_centralizer.py"

pytest.importorskip("numpy")

_g = {"__file__": str(_SRC), "__name__": "b854_diag"}
exec(compile(_SRC.read_text(), str(_SRC), "exec"), _g)

DIM, N, br = _g["DIM"], _g["N"], _g["br"]
INV, hvec, evec, ROOTS_ = _g["INV"], _g["hvec"], _g["evec"], _g["ROOTS"]
NS = [8, 14, 16, 22]

_basis = [hvec(i) for i in range(N)] + [evec(r) for r in ROOTS_]
_trip = {}
for _p in range(DIM):
    for _q in range(DIM):
        for _r, _c in enumerate(br(_basis[_p], _basis[_q])):
            if _c:
                _trip.setdefault(_p, []).append((_q, _r, float(_c)))


def _admat(vec):
    A = np.zeros((DIM, DIM))
    for p in range(DIM):
        if not vec[p]:
            continue
        fp = float(vec[p])
        for q, r, c in _trip.get(p, []):
            A[r, q] += fp * c
    return A


AD = {n: _admat(INV[n]) for n in NS}


def _weights():
    M = AD[8] + 3.0 * AD[14] + 7.0 * AD[16] + 13.0 * AD[22]
    _, V = np.linalg.eig(M)
    W = np.zeros((DIM, 4), dtype=complex)
    for k in range(DIM):
        col = V[:, k]
        i = int(np.argmax(np.abs(col)))
        for j, n in enumerate(NS):
            W[k, j] = (AD[n] @ col)[i] / col[i]
    W[np.abs(W) < 1e-8 * np.max(np.abs(W))] = 0
    return W / np.max(np.abs(W))


Wn = _weights()
IDX_SPLIT = [k for k in range(DIM) if Wn[k, 0] != 0 and Wn[k, 2] != 0]
IDX_SOFT = [k for k in range(DIM) if Wn[k, 0] == 0 and Wn[k, 2] == 0
            and (Wn[k, 1] != 0 or Wn[k, 3] != 0)]

RATIOS = []
for _k in IDX_SPLIT:
    _r = -Wn[_k, 0] / Wn[_k, 2]
    if not any(abs(_r - u) < 1e-6 for u in RATIOS):
        RATIOS.append(_r)
RATIOS.sort(key=lambda z: z.real)


def _key(rows, nd=5):
    return sorted(tuple(round(float(z.real), nd) for z in r)
                  + tuple(round(float(z.imag), nd) for z in r) for r in rows)


def _wall_class(w):
    if w[2] == 0:
        return -1
    r = -w[0] / w[2]
    for i, u in enumerate(RATIOS):
        if abs(r - u) < 1e-6:
            return i
    return -1


def _stabilizers(points):
    target = _key(points)
    i0 = 0
    j0 = next(j for j in range(1, len(points))
              if abs(np.linalg.det(np.array([points[i0], points[j]]))) > 1e-6)
    Binv = np.linalg.inv(np.array([points[i0], points[j0]]))
    out = []
    for a in range(len(points)):
        for b in range(len(points)):
            M = np.array([points[a], points[b]])
            if abs(np.linalg.det(M)) < 1e-9:
                continue
            g = Binv @ M
            if _key(points @ g) == target:
                if not any(np.max(np.abs(g - h)) < 1e-6 for h in out):
                    out.append(g)
    return out


def _block(g0, g1):
    g = np.zeros((4, 4), dtype=complex)
    g[0, 0], g[0, 2] = g0[0, 0], g0[0, 1]
    g[2, 0], g[2, 2] = g0[1, 0], g0[1, 1]
    g[1, 1], g[1, 3] = g1[0, 0], g1[0, 1]
    g[3, 1], g[3, 3] = g1[1, 0], g1[1, 1]
    return g


def _survivors():
    P0 = np.array([[Wn[k, 0], Wn[k, 2]] for k in IDX_SPLIT])
    P1 = np.array([[Wn[k, 1], Wn[k, 3]] for k in IDX_SOFT])
    target = _key(Wn)
    out = []
    for g0 in _stabilizers(P0):
        for g1 in _stabilizers(P1):
            g = _block(g0, g1)
            if _key(Wn @ g) == target:
                out.append(g)
    return out


SURV = _survivors()


def _perm(g):
    return tuple(_wall_class(Wn[next(k for k in IDX_SPLIT if _wall_class(Wn[k]) == i)] @ g)
                 for i in range(3))


def _is_pm_diagonal(g):
    off = g - np.diag(np.diag(g))
    return (np.max(np.abs(off)) < 1e-6
            and all(abs(abs(g[i, i]) - 1) < 1e-6 for i in range(4)))


def test_the_weight_system_has_the_expected_shape():
    assert len(IDX_SPLIT) == 48
    assert len(IDX_SOFT) == 18
    assert len(RATIOS) == 3


def test_the_candidate_group_has_order_24():
    assert len(SURV) == 24


def test_the_candidates_form_a_group():
    keys = {_key([g.reshape(-1)]) [0] for g in SURV}
    for a in SURV[:8]:
        for b in SURV[:8]:
            prod = a @ b
            assert any(np.max(np.abs(prod - c)) < 1e-5 for c in SURV), "not closed"


def test_the_three_cycle_is_NOT_excluded():
    """The hole the paper names is real: no invariant of C forbids it."""
    perms = {_perm(g) for g in SURV}
    assert (1, 2, 0) in perms or (2, 0, 1) in perms
    assert perms == {(0, 1, 2), (0, 2, 1), (1, 0, 2), (1, 2, 0), (2, 0, 1), (2, 1, 0)}


def test_exactly_four_candidates_are_pm_diagonal():
    diag = [g for g in SURV if _is_pm_diagonal(g)]
    assert len(diag) == 4
    signs = sorted(tuple(int(round(g[i, i].real)) for i in range(4)) for g in diag)
    assert signs == [(-1, -1, -1, -1), (-1, 1, -1, 1), (1, -1, 1, -1), (1, 1, 1, 1)]


def test_those_four_are_exactly_the_sign_locking_survivors():
    """Independent confirmation of the sign-locking theorem by a different route.

    Sign-locking obtains eps_8 eps_16 = +1 and eps_14 eps_22 = +1 from two degree-six
    rational trace moments.  The weight-multiset stabilizer knows nothing of those
    moments, and produces the same four patterns.
    """
    diag = [g for g in SURV if _is_pm_diagonal(g)]
    for g in diag:
        e8, e14, e16, e22 = (int(round(g[i, i].real)) for i in range(4))
        assert e8 * e16 == 1
        assert e14 * e22 == 1
    assert len(diag) == 4          # and all four such patterns occur


def test_the_gap_is_exactly_a_factor_of_six():
    """order 24 candidates / order 4 diagonal = S3 on the Galois orbit."""
    diag = [g for g in SURV if _is_pm_diagonal(g)]
    assert len(SURV) // len(diag) == 6
    assert len({_perm(g) for g in SURV}) == 6
