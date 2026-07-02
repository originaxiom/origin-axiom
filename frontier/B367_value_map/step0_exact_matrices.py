"""B367 (W2.3) step 0 -- the exact six-pair s-matrices at matched exponent labels.

Runs the checks pre-registered in PREREGISTRATION.md (committed before this file).

Construction (declared there): for each seed m the theta-lift Weil matrix at level 15,
    W_m = WR^m * D^m,   D = diag(zeta15^{j(j-1)/2}),   WR = F * D^{-1} * F^{-1}
(the B358 theta construction; conjugation by the raw DFT F[j,k] = zeta15^{jk} is
normalization-free). All arithmetic exact in Q(zeta60) (the B358 engine). For a pair
(m1, m2) the table
    C[j][l] = tr(Par * W_{m1}^j * W_{m2}^l),   tr(Par*A*B) = sum_{x,y} A[-x,y] B[y,x]
is DFT'd over powers into the eigenprojector pair-traces
    t(a,b) = (1/(o1*o2)) sum_{j,l} zeta_{o1}^{-ja} zeta_{o2}^{-lb} C[j][l]
           = tr(Par * P_a * Q_b),
Galois-averaged to H = Q(sqrt5, sqrt-3) and solved exactly in the basis
{1, sqrt5, sqrt-3, sqrt-15}. s(a,b) := the sqrt-15 coefficient. Labels are RAW
exponents (eigenvalue of P_a is zeta_{ord}^a). No PSLQ, no floats, no free parameters.

Cross-seat label dictionaries (recorded so the comparisons are auditable):
  - the addendum's (i,j) are INDICES into ascending exponent lists
    K1 = K4 = [0,1,4,5,6,9,11,14,15,16,19] (ord 20), K2 = [0,...,5,7,...,11] (ord 12),
    K3 = [0,1,2,4,5] (ord 6);
  - the briefing's 11x11 matrix uses raw exponent VALUES as row/col headers.
"""
import json
import os
import sys
from fractions import Fraction as Fr

HERE = os.path.dirname(os.path.abspath(__file__))
B358 = os.path.join(HERE, "..", "B358_seam_certification")
sys.path.insert(0, B358)
import cyclo_engine as E                     # noqa: E402
import seam_certification as SC              # noqa: E402

N = 15


def _dmat(power):
    """D^power = diag(zeta15^{power * j(j-1)/2}) as an exact matrix."""
    M = [[E.ZERO for _ in range(N)] for _ in range(N)]
    for j in range(N):
        M[j][j] = E.e15((power * (j * (j - 1) // 2)) % 15)
    return M


def _fmat(sign):
    """Raw DFT F[j,k] = zeta15^{sign*jk} (sign=-1 gives F^{-1} up to 1/15)."""
    return [[E.e15((sign * j * k) % 15) for k in range(N)] for j in range(N)]


def build_theta_W(m):
    """W_m = WR^m * D^m with WR = F * D^{-1} * F^{-1} (exact; 1/15 applied once)."""
    F = _fmat(+1)
    Fi = _fmat(-1)
    WR = E.mmul(E.mmul(F, _dmat(-1)), Fi)
    WR = [[E.scal(Fr(1, 15), WR[i][j]) for j in range(N)] for i in range(N)]
    P = WR
    for _ in range(m - 1):
        P = E.mmul(P, WR)
    return E.mmul(P, _dmat(m))


def matrix_order(W, cap=64):
    """Multiplicative order of W (exact); also returns the power cache W^0..W^{ord-1}."""
    ident = [[E.ONE if i == j else E.ZERO for j in range(N)] for i in range(N)]
    powers = [ident]
    P = W
    for k in range(1, cap + 1):
        if P == ident:
            return k, powers
        powers.append(P)
        P = E.mmul(P, W)
    raise RuntimeError("order cap exceeded")


def par_trace(A, B):
    """tr(Par * A * B) exactly."""
    t = E.ZERO
    for x in range(N):
        Arow = A[(-x) % N]
        for y in range(N):
            if Arow[y] != E.ZERO and B[y][x] != E.ZERO:
                t = E.add(t, E.mul(Arow[y], B[y][x]))
    return t


def pair_smatrix(pow1, pow2):
    """All exact H-vectors t(a,b); returns dict {(a,b): (p,q,r,s)} over nonzero t."""
    o1, o2 = len(pow1), len(pow2)
    C = [[par_trace(pow1[j], pow2[l]) for l in range(o2)] for j in range(o1)]
    z1, z2 = 60 // o1, 60 // o2
    out = {}
    for a in range(o1):
        for b in range(o2):
            t = E.ZERO
            for j in range(o1):
                zja = E.zeta((-z1 * j * a) % 60)
                for l in range(o2):
                    t = E.add(t, E.mul(E.mul(zja, E.zeta((-z2 * l * b) % 60)), C[j][l]))
            t = E.scal(Fr(1, o1 * o2), t)
            if t == E.ZERO:
                continue
            sol = SC.solve_H(SC.H_avg(t))
            assert sol is not None, ("outside H", a, b)
            out[(a, b)] = sol
    return out


def single_controls(powers):
    """Single-seed control: every tr(Par*P_a) has zero sqrt-3 and sqrt-15 parts."""
    o = len(powers)
    z = 60 // o
    for a in range(o):
        t = E.ZERO
        for j in range(o):
            tr = E.ZERO
            for x in range(N):
                tr = E.add(tr, powers[j][(-x) % N][x])
            t = E.add(t, E.mul(E.zeta((-z * j * a) % 60), tr))
        t = E.scal(Fr(1, o), t)
        if t == E.ZERO:
            continue
        sol = SC.solve_H(SC.H_avg(t))
        if sol is None or sol[2] != 0 or sol[3] != 0:
            return False
    return True


def projector_gates(powers):
    """Sum over a of P_a = I, and one idempotence check (a=0), exactly."""
    o = len(powers)
    z = 60 // o
    ident = [[E.ONE if i == j else E.ZERO for j in range(N)] for i in range(N)]

    def proj(a):
        M = [[E.ZERO] * N for _ in range(N)]
        for j in range(o):
            c = E.scal(Fr(1, o), E.zeta((-z * j * a) % 60))
            for i in range(N):
                for k in range(N):
                    if powers[j][i][k] != E.ZERO:
                        M[i][k] = E.add(M[i][k], E.mul(c, powers[j][i][k]))
        return M

    tot = [[E.ZERO] * N for _ in range(N)]
    for a in range(o):
        P = proj(a)
        for i in range(N):
            for k in range(N):
                tot[i][k] = E.add(tot[i][k], P[i][k])
    if tot != ident:
        return False
    P0 = proj(0)
    return E.mmul(P0, P0) == P0


# ---- the cross-seat reference data (transcribed; provenance in FINDINGS) ----

# addendum pair (1,2): 8 entries, INDEX labels -> raw exponents via K1/K2
K1 = [0, 1, 4, 5, 6, 9, 11, 14, 15, 16, 19]
K2 = [0, 1, 2, 3, 4, 5, 7, 8, 9, 10, 11]
K3 = [0, 1, 2, 4, 5]
ADDENDUM_12 = {  # index labels: s value
    (0, 4): Fr(1, 48), (0, 7): Fr(-1, 48), (3, 1): Fr(1, 120), (3, 5): Fr(-1, 480),
    (3, 8): Fr(-1, 160), (8, 3): Fr(-1, 160), (8, 6): Fr(1, 120), (8, 10): Fr(-1, 480),
}
ADDENDUM_23 = {  # index labels into K2 x K3: sign * 1/144
    (0, 2): Fr(1, 144), (0, 3): Fr(-1, 144), (4, 0): Fr(1, 144),
    (4, 2): Fr(-1, 144), (7, 0): Fr(-1, 144), (7, 3): Fr(1, 144),
}

# briefing 11x11 (pair (1,2)) -- raw exponent VALUE labels, entries are s*480
BRIEFING_ROWS = [0, 1, 4, 5, 6, 9, 11, 14, 15, 19]
BRIEFING_COLS = [1, 2, 3, 4, 5, 7, 8, 9, 10, 11]
BRIEFING_S480 = [
    [0, 0, 0, 10, 0, 0, -10, 0, 0, 0],
    [3, 0, 1, 0, -2, 2, 0, -1, 0, -3],
    [0, 0, 0, -10, 0, 0, 10, 0, 0, 0],
    [4, 0, 3, 0, -1, 1, 0, -3, 0, -4],
    [0, -10, 0, 0, 0, 0, 0, 0, 10, 0],
    [-2, 0, 6, 0, 8, -8, 0, -6, 0, 2],
    [2, 0, -1, 0, -3, 3, 0, 1, 0, -2],
    [0, 10, 0, 0, 0, 0, 0, 0, -10, 0],
    [1, 0, -3, 0, -4, 4, 0, 3, 0, -1],
    [-8, 0, -6, 0, 2, -2, 0, 6, 0, 8],
]


def smat_only(table):
    return {k: v[3] for k, v in table.items() if v[3] != 0}


def rank_over_Q(rows_idx, cols_idx, table):
    """Exact rank of the s-matrix on the given exponent grid."""
    M = [[table.get((a, b), (0, 0, 0, Fr(0)))[3] for b in cols_idx] for a in rows_idx]
    M = [row[:] for row in M]
    r = 0
    for c in range(len(cols_idx)):
        piv = next((i for i in range(r, len(M)) if M[i][c] != 0), None)
        if piv is None:
            continue
        M[r], M[piv] = M[piv], M[r]
        pv = M[r][c]
        M[r] = [v / pv for v in M[r]]
        for i in range(len(M)):
            if i != r and M[i][c] != 0:
                f = M[i][c]
                M[i] = [M[i][j] - f * M[r][j] for j in range(len(cols_idx))]
        r += 1
    return r


def run():
    report = {}
    seeds = {}
    for m in (1, 2, 3, 4, 7):
        W = build_theta_W(m)
        o, powers = matrix_order(W)
        exps = None  # filled from the pair tables' support
        seeds[m] = dict(order=o, powers=powers)
    report["orders"] = {m: seeds[m]["order"] for m in seeds}

    # gates
    report["projector_gates"] = {m: projector_gates(seeds[m]["powers"]) for m in (1, 2, 3, 4, 7)}
    report["single_controls"] = {m: single_controls(seeds[m]["powers"]) for m in (1, 2, 3, 4, 7)}

    pairs = [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]
    tables = {}
    for (m1, m2) in pairs:
        tables[(m1, m2)] = pair_smatrix(seeds[m1]["powers"], seeds[m2]["powers"])

    # S0.1 row/col sums of s over the full exponent grid = 0
    def sums_zero(tab, o1, o2):
        for a in range(o1):
            if sum((tab.get((a, b), (0, 0, 0, Fr(0)))[3] for b in range(o2)), Fr(0)) != 0:
                return False
        for b in range(o2):
            if sum((tab.get((a, b), (0, 0, 0, Fr(0)))[3] for a in range(o1)), Fr(0)) != 0:
                return False
        return True
    report["S0_1_sum_rules"] = all(
        sums_zero(tables[(m1, m2)], seeds[m1]["order"], seeds[m2]["order"])
        for (m1, m2) in pairs)

    # S0.2 the addendum's 8 identified (1,2) entries (index -> raw exponent labels)
    t12s = smat_only(tables[(1, 2)])
    s02 = all(t12s.get((K1[i], K2[j])) == v for (i, j), v in ADDENDUM_12.items())
    report["S0_2_addendum_12"] = s02

    # S0.6 the briefing's full 11x11 (1,2) matrix + structure claims
    brief_ok = True
    for ri, a in enumerate(BRIEFING_ROWS):
        for ci, b in enumerate(BRIEFING_COLS):
            mine = tables[(1, 2)].get((a, b), (0, 0, 0, Fr(0)))[3]
            if mine != Fr(BRIEFING_S480[ri][ci], 480):
                brief_ok = False
    # inactive row 16 / col 0 must be all-zero in s
    brief_ok &= all(tables[(1, 2)].get((16, b), (0, 0, 0, Fr(0)))[3] == 0 for b in range(12))
    brief_ok &= all(tables[(1, 2)].get((a, 0), (0, 0, 0, Fr(0)))[3] == 0 for a in range(20))
    report["S0_6_briefing_table"] = brief_ok
    report["S0_6_rank"] = rank_over_Q(K1, K2, tables[(1, 2)])
    report["S0_6_coxeter_odd"] = all(
        tables[(1, 2)].get((a, (12 - b) % 12), (0, 0, 0, Fr(0)))[3]
        == -tables[(1, 2)].get((a, b), (0, 0, 0, Fr(0)))[3]
        for a in K1 for b in K2)
    supp = {}
    for (a, b), s in t12s.items():
        supp.setdefault(a, set()).add(b)
    sectorB = {a for a in supp if supp[a] == {4, 8}}
    report["S0_6_sectorB_rows"] = sorted(sectorB)
    report["S0_6_sector_disjoint"] = all(
        supp[a] == {4, 8} or not (supp[a] & {4, 8}) for a in supp)

    # S0.3 the addendum's (2,3) entries + the +-1/288 prediction resolution
    t23s = smat_only(tables[(2, 3)])
    s03 = all(t23s.get((K2[i], K3[j])) == v for (i, j), v in ADDENDUM_23.items())
    report["S0_3_addendum_23"] = s03
    report["S0_3_value_set_23"] = sorted({str(v) for v in t23s.values()})

    # S0.4 zeros at full identification
    report["S0_4_13_zero"] = not smat_only(tables[(1, 3)])
    report["S0_4_14_zero"] = not smat_only(tables[(1, 4)])

    # S0.5 full (2,4), (3,4) tables
    report["S0_5_value_set_24"] = sorted({str(v) for v in smat_only(tables[(2, 4)]).values()})
    report["S0_5_value_set_34"] = sorted({str(v) for v in smat_only(tables[(3, 4)]).values()})

    # S0.7 exact aggregates
    aggs = {}
    for (m1, m2) in pairs:
        aggs[f"{m1},{m2}"] = str(sum((v * v for v in smat_only(tables[(m1, m2)]).values()), Fr(0)))
    report["S0_7_sum_s_squared"] = aggs

    # persist the six tables (exact strings)
    dump = {}
    for (m1, m2) in pairs:
        dump[f"{m1},{m2}"] = {f"{a},{b}": [str(x) for x in v]
                              for (a, b), v in tables[(m1, m2)].items()}
    with open(os.path.join(HERE, "step0_tables.json"), "w") as fh:
        json.dump(dump, fh)
    with open(os.path.join(HERE, "step0_report.json"), "w") as fh:
        json.dump({k: v for k, v in report.items()}, fh, indent=1, default=str)
    return report


if __name__ == "__main__":
    rep = run()
    for k, v in rep.items():
        print(f"  {k}: {v}")
