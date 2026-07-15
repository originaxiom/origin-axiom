"""B598-P2 — the quantization arrow: gates + the first-order boundary table.

RETROSPECTIVELY REGISTERED (D3: source+output+verdict shipped together in #945;
not a pre-result timestamp — the odd-trace prediction is recorded as a FAILED
exploratory prediction, permanently):
  GATE A (compatibility): P1's table restricts a knot-group cocycle, so per
    block the Z^2-cocycle condition (W_mu - 1) xi(lambda) = (W_lambda - 1) xi(mu)
    must hold exactly in coordinates.
  GATE B (embedding consistency): coordinates -> gl(27) via the BLOCKS basis
    intertwines the letter actions with Ad of the 27-model holonomy.
  PREDICTION (the selection rule's boundary face): the first-order character
    shifts delta tr_27(g) = tr(Xi(g) rho_27(g)) VANISH for the theta-odd
    blocks m in {4, 8} (one odd insertion, Theta-invariant contraction) and
    are generically NONZERO for the even blocks {1, 5, 7, 11}. Consequence
    (the P2 verdict if confirmed): the quantization arrow is QUADRATIC — its
    content is the eps^2 object; the classical side of P3's matching is the
    banked B599-ALG t^2 family.

Run: OA_SLOW=1 python3 p2_quantization_arrow.py (~12 min). Nothing to CLAIMS.md.
"""
import importlib.util
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(HERE, '..', 'B575_bridge_obstruction',
                        'l51_obstruction.py')).read()
ns = {'__name__': 'l51mod'}
sys.argv = ['l51']
exec(compile(src, 'l51', 'exec'), ns)
K = ns['K']; K0 = ns['K0']; K1 = ns['K1']
mmul = ns['mmul']; madd = ns['madd']; mscale = ns['mscale']; meye = ns['meye']
nullspace = ns['nullspace']; rref = ns['rref']
A27 = ns['A27']; B27 = ns['B27']; A27i = ns['A27i']; B27i = ns['B27i']
BLOCKS = ns['BLOCKS']; BLOCK_DATA = ns['BLOCK_DATA']
REL = ns['REL']
L27 = {'a': A27, 'b': B27, 'A': A27i, 'B': B27i}


def mat_vec(M, v):
    return [sum((M[i][j] * v[j] for j in range(len(v)) if not v[j].is_zero()), K0)
            for i in range(len(M))]


def mat_mul(X, Y):
    return mmul(X, Y)


def word_action(acts, word):
    d = len(acts['a'])
    W = [[K1 if i == j else K0 for j in range(d)] for i in range(d)]
    for ch in word:
        W = mat_mul(W, acts[ch])
    return W


def word27(word):
    W = meye(27)
    for ch in word:
        W = mmul(W, L27[ch])
    return W


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


def rank(rows):
    if not rows:
        return 0
    _, piv = rref([list(r) for r in rows])
    return len(piv)


def embed(mexp, coords):
    d = len(coords)
    M = [[K0] * 27 for _ in range(27)]
    for i, c in enumerate(coords):
        if c.is_zero():
            continue
        Bi = BLOCKS[mexp][i]
        for r in range(27):
            for s in range(27):
                if not Bi[r][s].is_zero():
                    M[r][s] = M[r][s] + c * Bi[r][s]
    return M


def tr27(M):
    return sum((M[i][i] for i in range(27) if not M[i][i].is_zero()), K0)


def fmt(x):
    if x.is_zero():
        return "0"
    if x.b == 0:
        return str(x.a)
    return f"({x.a}{'+' if x.b > 0 else ''}{x.b}w)"


print("P2 — gates + the first-order boundary character table")
LAM = "abABaaBAbA"   # the TRUE longitude (found by direct search;
# image -[[1, 2*sqrt(3)i],[0,1]] = the banked cusp shape; "baBA" was the fiber-frame
# commutator misapplied -- caught by Gate A, corrected 2026-07-15)
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
    piv = next(i for i, v in enumerate(xa) if not v.is_zero())
    sc = xa[piv].inv()
    xa = [sc * v for v in xa]
    xb = [sc * v for v in xb]
    xi_mu = xa
    xi_lam = cocycle_eval(acts, xa, xb, LAM)
    # GATE A: (W_mu - 1) xi(lam) = (W_lam - 1) xi(mu)
    Wmu = acts['a']
    Wlam = word_action(acts, LAM)
    lhs = [x - y for x, y in zip(mat_vec(Wmu, xi_lam), xi_lam)]
    rhs = [x - y for x, y in zip(mat_vec(Wlam, xi_mu), xi_mu)]
    gateA = all((l - r).is_zero() for l, r in zip(lhs, rhs))
    # GATE B: embedding intertwines: embed(acts['a'] c) = A27 embed(c) A27^{-1}
    c_test = xi_mu
    left = embed(mexp, mat_vec(acts['a'], c_test))
    right = mmul(mmul(A27, embed(mexp, c_test)), A27i)
    gateB = all((left[i][j] - right[i][j]).is_zero()
                for i in range(27) for j in range(27))
    # the first-order character shifts
    Ximu = embed(mexp, xi_mu)
    Xilam = embed(mexp, xi_lam)
    d_mu = tr27(mmul(Ximu, A27))
    d_lam = tr27(mmul(Xilam, word27(LAM)))
    xi_mulam = cocycle_eval(acts, xa, xb, "a" + LAM)
    d_mulam = tr27(mmul(embed(mexp, xi_mulam), word27("a" + LAM)))
    parity = "ODD " if mexp in (4, 8) else "even"
    assert gateA, f"GATE A FAILED at m={mexp}"           # failure-enforcing (D8)
    assert gateB, f"GATE B FAILED at m={mexp}"
    print(f"\n  block m={mexp:2d} ({parity}): gate A (Z^2-compat): {gateA};  "
          f"gate B (embedding): {gateB}")
    print(f"    delta tr27(mu)      = {fmt(d_mu)}")
    print(f"    delta tr27(lambda)  = {fmt(d_lam)}")
    print(f"    delta tr27(mu.lam)  = {fmt(d_mulam)}")

print("\n(prediction registered in the docstring: ODD rows all-zero, even rows generic)")
print("DONE")
