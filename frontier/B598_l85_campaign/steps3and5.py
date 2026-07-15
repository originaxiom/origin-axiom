"""B598 readiness-chain steps 3 + 5 (see CAMPAIGN.md; registered designs in
the banked transcript).

STEP 3: the gauge-invariant boundary table — per block, the invariant form G
(acts^T G acts = G, unique up to scale), the peripheral-invariant vector w,
and the invariant ratio (I_mu : I_lambda) = (<xi(mu), w> : <xi(lambda), w>);
rank-6/6 nonvanishing re-derived.

STEP 5: the exact 27-27bar intertwiner J: rho(X)^T J + J rho(theta X) = 0 on
generators {e_pr, f_pr, v4} (theta = +-1 by block parity), weight-reduced;
gates: Schur-uniqueness, invertibility, group-level identity, and the
NO-untwisted-form check (the same solve without theta must give 0 only).
Plus the J-versions of the L1 contractions.

Run: OA_SLOW=1 python3 steps3and5.py (~20 min). Nothing to CLAIMS.md.
"""
import importlib.util
import os
import sys
from fractions import Fraction as Fr

HERE = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(HERE, '..', 'B575_bridge_obstruction',
                        'l51_obstruction.py')).read()
ns = {'__name__': 'l51mod'}
sys.argv = ['l51']
exec(compile(src, 'l51', 'exec'), ns)
K, K0, K1 = ns['K'], ns['K0'], ns['K1']
mmul, nullspace, rref = ns['mmul'], ns['nullspace'], ns['rref']
BLOCK_DATA, BLOCKS = ns['BLOCK_DATA'], ns['BLOCKS']
A27, B27 = ns['A27'], ns['B27']
e_pr, f_pr, h_pr = ns['e_pr'], ns['f_pr'], ns['h_pr']
REL = ns['REL']


def mat_vec(M, v):
    return [sum((M[i][j] * v[j] for j in range(len(v)) if not v[j].is_zero()), K0)
            for i in range(len(M))]


def fox_pair(acts, d):
    I = [[K1 if i == j else K0 for j in range(d)] for i in range(d)]
    Da = [[K0] * d for _ in range(d)]
    Db = [[K0] * d for _ in range(d)]
    P = I
    for ch in REL:
        if ch == 'a':
            for i in range(d):
                for j in range(d):
                    Da[i][j] = Da[i][j] + P[i][j]
        elif ch == 'A':
            PA = mmul(P, acts['A'])
            for i in range(d):
                for j in range(d):
                    Da[i][j] = Da[i][j] - PA[i][j]
        elif ch == 'b':
            for i in range(d):
                for j in range(d):
                    Db[i][j] = Db[i][j] + P[i][j]
        else:
            PB = mmul(P, acts['B'])
            for i in range(d):
                for j in range(d):
                    Db[i][j] = Db[i][j] - PB[i][j]
        P = mmul(P, acts[ch])
    return Da, Db


def rank(rows):
    if not rows:
        return 0
    _, piv = rref([list(r) for r in rows])
    return len(piv)


def cocycle_eval(acts, xa, xb, word):
    d = len(xa)
    val = [K0] * d
    P = [[K1 if i == j else K0 for j in range(d)] for i in range(d)]
    for ch in word:
        if ch == 'a':
            inc = xa
        elif ch == 'b':
            inc = xb
        elif ch == 'A':
            inc = [K0 - v for v in mat_vec(acts['A'], xa)]
        else:
            inc = [K0 - v for v in mat_vec(acts['B'], xb)]
        val = [val[i] + v for i, v in enumerate(mat_vec(P, inc))]
        P = mmul(P, acts[ch])
    return val


def fmt(x):
    if x.is_zero():
        return "0"
    if x.b == 0:
        return str(x.a)
    return f"({x.a}{'+' if x.b > 0 else ''}{x.b}w)"


LAM = "abABaaBAbA"
print("STEP 3 — the gauge-invariant boundary table:")
for mexp in sorted(BLOCK_DATA.keys()):
    D = BLOCK_DATA[mexp]
    d, acts = D['d'], D['acts']
    # the invariant form G: acts(g)^T G acts(g) = G for g in {a, b}: solve linearly
    # unknowns G[i][j]: equations sum_kl acts[g][k][i] G[k][l] acts[g][l][j] = G[i][j]
    rows = []
    for g in ('a', 'b'):
        Ag = acts[g]
        for i in range(d):
            for j in range(d):
                row = [K0] * (d * d)
                for k in range(d):
                    if Ag[k][i].is_zero():
                        continue
                    for l in range(d):
                        if not Ag[l][j].is_zero():
                            row[k * d + l] = row[k * d + l] + Ag[k][i] * Ag[l][j]
                row[i * d + j] = row[i * d + j] - K1
                rows.append(row)
    Gs = nullspace(rows)
    assert len(Gs) == 1, f"invariant form not unique at m={mexp}: {len(Gs)}"
    G = [[Gs[0][i * d + j] for j in range(d)] for i in range(d)]
    # w = the peripheral invariant of the meridian: ker(acts[a] - 1)
    Am1 = [[acts['a'][i][j] - (K1 if i == j else K0) for j in range(d)]
           for i in range(d)]
    ws = nullspace(Am1)
    assert len(ws) == 1, f"meridian invariant not a line at m={mexp}"
    w = ws[0]
    # the H1 representative (recomputed)
    Da, Db = fox_pair(acts, d)
    big = [[Da[i][j] for j in range(d)] + [Db[i][j] for j in range(d)]
           for i in range(d)]
    sols = nullspace(big)
    cobs = []
    for j in range(d):
        e = [K1 if i == j else K0 for i in range(d)]
        ca = [e[i] - v for i, v in enumerate(mat_vec(acts['a'], e))]
        cb = [e[i] - v for i, v in enumerate(mat_vec(acts['b'], e))]
        cobs.append(ca + cb)
    rc = rank(cobs)
    rep = next(s for s in sols if rank(cobs + [list(s)]) > rc)
    xa, xb = list(rep[:d]), list(rep[d:])
    xl = cocycle_eval(acts, xa, xb, LAM)
    pair = lambda u, v: sum((u[i] * sum((G[i][j] * v[j] for j in range(d)
                            if not v[j].is_zero()), K0) for i in range(d)), K0)
    # gauge-invariance gate: I_mu of a coboundary must vanish
    e0 = [K1 if i == 0 else K0 for i in range(d)]
    cob_mu = [e0[i] - v for i, v in enumerate(mat_vec(acts['a'], e0))]
    gate_gauge = pair(cob_mu, w).is_zero()
    I_mu = pair(xa, w)
    I_lam = pair(xl, w)
    nonvanishing = not (I_mu.is_zero() and I_lam.is_zero())
    ratio = "undefined" if I_mu.is_zero() else fmt(I_lam * I_mu.inv())
    assert gate_gauge and nonvanishing, f"step-3 gate failed at m={mexp}"   # D8
    rv = I_lam * I_mu.inv()
    assert rv.a == 0 and rv.b == -2, f"universal ratio broken at m={mexp}"  # -2w
    print(f"  m={mexp:2d}: gauge-gate {gate_gauge}; nonvanishing {nonvanishing}; "
          f"(I_mu : I_lam) ratio I_lam/I_mu = {ratio}")

print("\nSTEP 5 — the exact 27-27bar intertwiner J:")
# theta on e6: +1 on blocks {1,5,7,11}, -1 on {4,8}; generators e_pr, f_pr (even), v4 (odd)
v4 = BLOCKS[4][0]
# weight reduction: h_pr is diagonal in this model?
hdiag = all(h_pr[i][j].is_zero() for i in range(27) for j in range(27) if i != j)
print(f"  h_pr diagonal in the model: {hdiag}")
wts = [h_pr[i][i] for i in range(27)]
pairs_idx = [(i, j) for i in range(27) for j in range(27)
             if (wts[i] + wts[j]).is_zero()]
print(f"  weight-opposite support size: {len(pairs_idx)} (of 729)")
idx_of = {p: k for k, p in enumerate(pairs_idx)}
nunk = len(pairs_idx)

def add_equations(X, sign, rows):
    # X^T J + sign * J X = 0 restricted to the support
    # (X^T J)[i][j] = sum_k X[k][i] J[k][j];  (J X)[i][j] = sum_k J[i][k] X[k][j]
    for i in range(27):
        for j in range(27):
            if not (wts[i] + wts[j]).is_zero() and sign != 0:
                pass
            row = [K0] * nunk
            any_nz = False
            for k in range(27):
                if not X[k][i].is_zero() and (k, j) in idx_of:
                    row[idx_of[(k, j)]] = row[idx_of[(k, j)]] + X[k][i]
                    any_nz = True
                if not X[k][j].is_zero() and (i, k) in idx_of:
                    row[idx_of[(i, k)]] = row[idx_of[(i, k)]] + (K(sign) * X[k][j])
                    any_nz = True
            if any_nz:
                rows.append(row)

rows = []
add_equations(e_pr, 1, rows)      # even: X^T J + J X = 0
add_equations(f_pr, 1, rows)
add_equations(v4, -1, rows)       # odd:  X^T J - J X = 0
Js = nullspace(rows)
print(f"  solution space dim (Schur gate, expect 1): {len(Js)}")
assert len(Js) == 1
J = [[K0] * 27 for _ in range(27)]
for k, (i, j) in enumerate(pairs_idx):
    J[i][j] = Js[0][k]
# invertibility: rank 27
rkJ = rank(J)
print(f"  rank(J) = {rkJ} (invertible: {rkJ == 27})")
# group-level identity: A27^T J A27 = J (theta A27 = A27, even)
JA = mmul([[A27[k][i] for k in range(27)] for i in range(27)], mmul(J, A27))
gA = all((JA[i][j] - J[i][j]).is_zero() for i in range(27) for j in range(27))
assert gA, "group gate failed"                                # D8
print(f"  group gate: A27^T J A27 = J: {gA}")
# the NO-untwisted-form check: same solve with theta = +1 on v4 too
rows0 = []
add_equations(e_pr, 1, rows0)
add_equations(f_pr, 1, rows0)
add_equations(v4, 1, rows0)
G0 = nullspace(rows0)
assert len(G0) == 0, "an untwisted invariant form exists?!"    # D8
print(f"  untwisted-form solution dim (seat 4's claim, expect 0): {len(G0)}")
# the J-version of the L1 contractions
Om = ns['madd'](ns['madd'](mmul(e_pr, f_pr), mmul(f_pr, e_pr)),
                ns['mscale'](K(Fr(1, 2)), mmul(h_pr, h_pr)))
v0 = nullspace(Om)[0]
for m in (4, 8):
    vm = BLOCKS[m][0]
    w1 = mat_vec(vm, v0)
    Jv0 = mat_vec(J, v0)
    c = sum((w1[i] * Jv0[i] for i in range(27)), K0)
    assert c.is_zero(), f"J-L1 nonzero at m={m}"                              # D8
    print(f"  J-L1 m={m}: (v_m v0)^T J v0 = {fmt(c)}")
print("DONE")
