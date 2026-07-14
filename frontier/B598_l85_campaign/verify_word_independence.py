"""Verification (seat 4's step 3 + the erratum's claim): at ALL SIX blocks,
the cocycle evaluated on the canonical longitude word bABaaBAb equals its
evaluation on the group-equal word abABaaBAbA (word-independence of cocycle
values), and Gate A holds with the canonical word too.
Run: OA_SLOW=1 python3 verify_word_independence.py (~12 min)."""
import importlib.util
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(HERE, '..', 'B575_bridge_obstruction',
                        'l51_obstruction.py')).read()
ns = {'__name__': 'l51mod'}
sys.argv = ['l51']
exec(compile(src, 'l51', 'exec'), ns)
K0, K1 = ns['K0'], ns['K1']
REL = ns['REL']
rref, nullspace = ns['rref'], ns['nullspace']
BLOCK_DATA = ns['BLOCK_DATA']


def mat_vec(M, v):
    return [sum((M[i][j] * v[j] for j in range(len(v)) if not v[j].is_zero()), K0)
            for i in range(len(M))]


def mat_mul(X, Y):
    n, m, p = len(X), len(Y), len(Y[0])
    out = [[K0] * p for _ in range(n)]
    for i in range(n):
        for k in range(m):
            x = X[i][k]
            if x.is_zero():
                continue
            for j in range(p):
                y = Y[k][j]
                if not y.is_zero():
                    out[i][j] = out[i][j] + x * y
    return out


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
            PA = mat_mul(P, acts['A'])
            for i in range(d):
                for j in range(d):
                    Da[i][j] = Da[i][j] - PA[i][j]
        elif ch == 'b':
            for i in range(d):
                for j in range(d):
                    Db[i][j] = Db[i][j] + P[i][j]
        else:
            PB = mat_mul(P, acts['B'])
            for i in range(d):
                for j in range(d):
                    Db[i][j] = Db[i][j] - PB[i][j]
        P = mat_mul(P, acts[ch])
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
        P = mat_mul(P, acts[ch])
    return val


def word_action(acts, word):
    d = len(acts['a'])
    W = [[K1 if i == j else K0 for j in range(d)] for i in range(d)]
    for ch in word:
        W = mat_mul(W, acts[ch])
    return W


ALL_OK = True
for mexp in sorted(BLOCK_DATA.keys()):
    D = BLOCK_DATA[mexp]
    d, acts = D['d'], D['acts']
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
    v_canon = cocycle_eval(acts, xa, xb, "bABaaBAb")
    v_used = cocycle_eval(acts, xa, xb, "abABaaBAbA")
    eq = all((u - v).is_zero() for u, v in zip(v_canon, v_used))
    # Gate A with the canonical word
    Wmu = acts['a']
    Wlam = word_action(acts, "bABaaBAb")
    lhs = [x - y for x, y in zip(mat_vec(Wmu, v_canon), v_canon)]
    rhs = [x - y for x, y in zip(mat_vec(Wlam, xa), xa)]
    gA = all((l - r).is_zero() for l, r in zip(lhs, rhs))
    ALL_OK &= eq and gA
    print(f"block m={mexp:2d}: xi(canonical) == xi(used word): {eq};  Gate A (canonical): {gA}")
print("ALL SIX BLOCKS:", "PASS" if ALL_OK else "FAIL")
