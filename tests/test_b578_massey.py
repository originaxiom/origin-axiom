"""B578 D1-massey -- the THIRD-ORDER (Massey) obstruction, EXACT over Q(sqrt(-3)).

Locks the reconciliation of B370 (dps-100, conditional) on the independent B575
gl(27) build.  Re-runs the full exact e6 build (l51_obstruction.py, the B575 lock)
then computes the order-3 obstruction by direct truncated-jet arithmetic and asserts:

  * all six third-order classes <z1,z1,z1> vanish EXACTLY (incl. theta-odd u4,u8);
  * the order-2 obstruction Q2 == 1/2 * B575.cup_on_relator (convention gate);
  * two extractions (P1=P2=0 shortcut vs full truncated log) agree exactly;
  * the Massey INDETERMINACY is exactly zero (u4,u8 vs all six shift cocycles)
    -- correcting B370's dps-100 nonzero "ranks".

Runtime ~11 min exact (the B575 build ~6 min + the jets).  House pattern: gated
behind OA_SLOW=1 (reviews run slow-tier on).  Place in tests/ (imports l51 via
../frontier/B575_bridge_obstruction/l51_obstruction.py).  See B578 FINDINGS.
"""
import importlib.util, os, sys
from fractions import Fraction as Fr
import pytest


@pytest.mark.skipif(os.environ.get('OA_SLOW') != '1',
                    reason='full exact e6 build ~11 min; run with OA_SLOW=1 (B352/B575 house pattern)')
def test_third_order_massey_vanishes_exactly():
    path = os.path.join(os.path.dirname(__file__), "..", "frontier",
                        "B575_bridge_obstruction", "l51_obstruction.py")
    spec = importlib.util.spec_from_file_location("l51mod_b578", path)
    M = importlib.util.module_from_spec(spec)
    argv = sys.argv; sys.argv = [path]
    try:
        spec.loader.exec_module(M)          # G1-G5 module-level asserts (the B575 build)
    finally:
        sys.argv = argv

    K = M.K
    mmul, madd, mscale, meye, mzero = M.mmul, M.madd, M.mscale, M.meye, M.mzero
    bracket, flat, mzero_p, msub = M.bracket, M.flat, M.mzero_p, M.msub
    rref = M.rref
    block_to_mat, cup_on_relator, obstruction = M.block_to_mat, M.cup_on_relator, M.obstruction
    GLOBAL_SOLVER, SLICES, ORDER = M.GLOBAL_SOLVER, M.SLICES, M.ORDER
    BLOCK_DATA, BLOCKS = M.BLOCK_DATA, M.BLOCKS
    A27, B27, A27i, B27i, REL = M.A27, M.B27, M.A27i, M.B27i, M.REL

    ZERO, IMAT = mzero(27, 27), meye(27)
    HALF, SIXTH, THIRD, NEG = K(Fr(1, 2)), K(Fr(1, 6)), K(Fr(1, 3)), K(-1)

    def pm_mul(P, Q):
        R = [None] * 4
        for i in range(4):
            if P[i] is None: continue
            for j in range(4 - i):
                if Q[j] is None: continue
                pr = mmul(P[i], Q[j]); R[i + j] = pr if R[i + j] is None else madd(R[i + j], pr)
        return R
    def pm_add(P, Q):
        return [Q[k] if P[k] is None else (P[k] if Q[k] is None else madd(P[k], Q[k])) for k in range(4)]
    def pm_scale(c, P):
        return [None if P[k] is None else mscale(c, P[k]) for k in range(4)]
    def exp_series(Z1, Z2, Z3):
        S = [None, Z1, Z2, Z3]; S2 = pm_mul(S, S); S3 = pm_mul(S2, S)
        E = pm_add([IMAT, None, None, None], S)
        E = pm_add(E, pm_scale(HALF, S2)); return pm_add(E, pm_scale(SIXTH, S3))
    def jets(Z1a, Z2a, Z1b, Z2b):
        Ea, Eb = exp_series(Z1a, Z2a, ZERO), exp_series(Z1b, Z2b, ZERO)
        ja, jb = pm_mul(Ea, [A27, None, None, None]), pm_mul(Eb, [B27, None, None, None])
        Eai = exp_series(mscale(NEG, Z1a), mscale(NEG, Z2a), ZERO)
        Ebi = exp_series(mscale(NEG, Z1b), mscale(NEG, Z2b), ZERO)
        jA, jB = pm_mul([A27i, None, None, None], Eai), pm_mul([B27i, None, None, None], Ebi)
        return {'a': ja, 'b': jb, 'A': jA, 'B': jB}
    def rel_series(J):
        P = [IMAT, None, None, None]
        for ch in REL: P = pm_mul(P, J[ch])
        return P
    def solve_particular(L, rhs):
        d, w = len(L), len(L[0])
        Rr, piv = rref([L[i][:] + [rhs[i]] for i in range(d)])
        for pc in piv:
            assert pc != w, "inconsistent -> second-order obstruction nonzero!"
        v = [K(0)] * w
        for r_i, pc in enumerate(piv): v[pc] = Rr[r_i][w]
        return v
    def solve_z2(Q2):
        co = GLOBAL_SOLVER.coords(flat(Q2)); Za = ZERO; Zb = ZERO; touched = []
        for m in ORDER:
            s, e = SLICES[m]; comp = co[s:e]
            if all(x.is_zero() for x in comp): continue
            touched.append(m); d = BLOCK_DATA[m]['d']
            v = solve_particular(BLOCK_DATA[m]['L'], [K(0) - comp[i] for i in range(d)])
            Za = madd(Za, block_to_mat(m, v[:d])); Zb = madd(Zb, block_to_mat(m, v[d:]))
        return Za, Zb, touched
    def log3(P):
        N = [None, P[1], P[2], P[3]]; N2 = pm_mul(N, N); N3 = pm_mul(N2, N); out = None
        for term, c in ((N, K(1)), (N2, NEG * HALF), (N3, THIRD)):
            if term[3] is not None:
                a = mscale(c, term[3]); out = a if out is None else madd(out, a)
        return out if out is not None else ZERO

    EXPECT = {1: [1], 4: [1, 5, 7], 5: [1, 5, 7], 7: [1, 5, 7, 11],
              8: [1, 5, 7, 11], 11: [1, 5, 7, 11]}
    z2store = {}
    for m in ORDER:
        d = BLOCK_DATA[m]['d']; u = BLOCK_DATA[m]['u']
        Z1a, Z1b = block_to_mat(m, u[:d]), block_to_mat(m, u[d:])
        P = rel_series(jets(Z1a, ZERO, Z1b, ZERO))
        assert P[1] is None or mzero_p(P[1]), f"m={m}: P1 (cocycle gate) != 0"
        Q2 = P[2] if P[2] is not None else ZERO
        assert mzero_p(msub(Q2, mscale(HALF, cup_on_relator(m, u, m, u)))), f"m={m}: Q2 != 1/2 cup"
        Z2a, Z2b, touched = solve_z2(Q2)
        assert touched == EXPECT[m], f"m={m}: z2 channels {touched} != {EXPECT[m]}"
        P = rel_series(jets(Z1a, Z2a, Z1b, Z2b))
        assert P[1] is None or mzero_p(P[1])
        assert P[2] is None or mzero_p(P[2]), f"m={m}: P2 pass2 != 0 (z2 solve failed)"
        C3 = P[3] if P[3] is not None else ZERO
        assert mzero_p(msub(C3, log3(P))), f"m={m}: two extractions disagree"
        ob = obstruction(C3)
        assert all(v.is_zero() for v in ob.values()), f"m={m}: THIRD-ORDER OBSTRUCTED {ob}"
        z2store[m] = (Z1a, Z1b, Z2a, Z2b)

    # indeterminacy exactly zero (theta-odd u4,u8 vs all six shift cocycles)
    for m in (4, 8):
        Z1a, Z1b, Z2a, Z2b = z2store[m]
        base = obstruction(rel_series(jets(Z1a, Z2a, Z1b, Z2b))[3] or ZERO)
        for mp in ORDER:
            dp, up = BLOCK_DATA[mp]['d'], BLOCK_DATA[mp]['u']
            Za = madd(Z2a, block_to_mat(mp, up[:dp])); Zb = madd(Z2b, block_to_mat(mp, up[dp:]))
            sh = obstruction(rel_series(jets(Z1a, Za, Z1b, Zb))[3] or ZERO)
            assert all((sh[c] - base[c]).is_zero() for c in ORDER), \
                f"m={m}: indeterminacy nonzero under shift zeta_{mp}"

    # positive control: obstruction() is non-vacuous
    for m in ORDER:
        phi = BLOCK_DATA[m]['phi']
        j = next(k for k in range(BLOCK_DATA[m]['d']) if not phi[k].is_zero())
        assert obstruction(BLOCKS[m][j])[m] == phi[j] and not phi[j].is_zero()