"""B1092 lock: the purity selector's numbers (compact re-run of the stabilizer dims)."""
import itertools
from sympy import Rational, Matrix, zeros, eye
import pytest

N = 5
MODES = list(range(1, N + 1))
half = Rational(1, 2)

@pytest.fixture(scope="module")
def machinery():
    subs = [frozenset(c) for k in range(N + 1) for c in itertools.combinations(MODES, k)]
    idx = {s: i for i, s in enumerate(subs)}
    def op(j, dag):
        M = zeros(32, 32)
        for S in subs:
            if dag and j not in S:
                p = sum(1 for m in S if m < j); M[idx[frozenset(S | {j})], idx[S]] = (-1) ** p
            if not dag and j in S:
                p = sum(1 for m in S if m < j); M[idx[frozenset(S - {j})], idx[S]] = (-1) ** p
        return M
    AD = {j: op(j, True) for j in MODES}
    A = {j: op(j, False) for j in MODES}
    ev = sorted([s for s in subs if len(s) % 2 == 0], key=lambda s: (len(s), sorted(s)))
    ei = {s: i for i, s in enumerate(ev)}
    def restrict(M):
        R = zeros(16, 16)
        for S1 in ev:
            for S2 in ev:
                R[ei[S1], ei[S2]] = M[idx[S1], idx[S2]]
        return R
    gens = []
    for i in MODES:
        for j in MODES:
            M = AD[i] * A[j]
            if i == j: M = M - half * eye(32)
            gens.append(restrict(M))
    for i, j in itertools.combinations(MODES, 2): gens.append(restrict(AD[i] * AD[j]))
    for i, j in itertools.combinations(MODES, 2): gens.append(restrict(A[i] * A[j]))
    return gens, ev, ei

def _stab(gens, v):
    M = zeros(16, 45)
    for a in range(45):
        col = gens[a] * v
        for r in range(16): M[r, a] = col[r]
    return 45 - M.rank()

def test_pure_34_generic_29_orbit_11(machinery):
    gens, ev, ei = machinery
    v0 = zeros(16, 1); v0[ei[frozenset()]] = 1
    d0 = _stab(gens, v0)
    assert d0 == 34
    assert 45 - d0 == 11                    # the cone: 10 + 1
    coeffs = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9, 3]
    vg = Matrix([Rational(c) for c in coeffs])
    assert _stab(gens, vg) == 29
