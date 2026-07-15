"""B598 P3 — V1', THE COPY-EXCHANGE MIRROR (amended kill cell; see
STEP8_P3_PREREG_AMENDMENT1.md, sha256 ec08f67f..., sealed before this run).

The mirrored CONFIGURATION: the twist moves to copy 1 —
  b1 -> c B27 c^{-1} (twisted plain b), b2 -> mconj(B27) (untwisted
  mirror letter), a1 = a2 = A27. Words mapped by the copy-swap sigma
  (1 <-> 2). PREDICTION (mirror-equivariance): r^{V1'}(sigma(w)) lies in
  the gamma-conjugate phase class of the banked r^{4b}(w); zero set
  mapped by sigma. Any violation FAILS (outcome D, V1 row).

Run: OA_SLOW=1 python3 p3_v1prime_copy_exchange.py   (~25 min)
"""
import os
import sys
from fractions import Fraction as Fr

HERE = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(HERE, '..', 'B575_bridge_obstruction',
                        'l51_obstruction.py')).read()
ns = {'__name__': 'l51mod'}
sys.argv = ['l51']
exec(compile(src, 'l51', 'exec'), ns)
K = ns['K']; K0 = ns['K0']; K1 = ns['K1']
mmul = ns['mmul']; madd = ns['madd']; mscale = ns['mscale']; meye = ns['meye']
nullspace = ns['nullspace']
A27 = ns['A27']; B27 = ns['B27']; A27i = ns['A27i']; B27i = ns['B27i']
BLOCKS = ns['BLOCKS']

kc = lambda x: K(x.a, -x.b)


def mconj(M):
    return [[kc(x) for x in r] for r in M]


def matvec(M, v):
    return [sum((M[i][j] * v[j] for j in range(27) if not v[j].is_zero()), K0)
            for i in range(27)]


e_pr = ns['e_pr']; f_pr = ns['f_pr']; h_pr = ns['h_pr']
half = K(Fr(1, 2))
Om = madd(madd(mmul(e_pr, f_pr), mmul(f_pr, e_pr)),
          mscale(half, mmul(h_pr, h_pr)))
v0 = nullspace(Om)[0]
V4 = BLOCKS[4][0]
wts = [h_pr[i][i] for i in range(27)]
pairs_idx = [(i, j) for i in range(27) for j in range(27)
             if (wts[i] + wts[j]).is_zero()]
idx_of = {p: k for k, p in enumerate(pairs_idx)}
nunk = len(pairs_idx)


def add_equations(X, sign, rows_):
    for i in range(27):
        for j in range(27):
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
                rows_.append(row)


rows = []
add_equations(e_pr, 1, rows)
add_equations(f_pr, 1, rows)
add_equations(V4, -1, rows)
Js = nullspace(rows)
assert len(Js) == 1
J = [[K0] * 27 for _ in range(27)]
for k, (i, j) in enumerate(pairs_idx):
    J[i][j] = Js[0][k]
print("J rebuilt (Schur-unique)", flush=True)


def jpair(u, w):
    Ju = matvec(J, w)
    return sum((u[i] * Ju[i] for i in range(27) if not u[i].is_zero()), K0)


def tmul(X, Y):
    return (mmul(X[0], Y[0]),
            madd(mmul(X[0], Y[1]), mmul(X[1], Y[0])),
            madd(madd(mmul(X[0], Y[2]), mmul(X[1], Y[1])), mmul(X[2], Y[0])))


ZERO = [[K0] * 27 for _ in range(27)]


def const(M):
    return (M, ZERO, ZERO)


WORDS = ["a1", "b1", "a2", "b2", "a1b1", "a2b2", "a1b2", "a2b1", "a1a2",
         "b1b2", "a1b1a2b2", "a2b2a1b1", "a1b2a2b1", "a1b1A1B1", "a1b2A1B2",
         "a1a2b1b2", "b1a2b2a1", "a1b1a1", "a1b1b2", "a2b1b2"]
MIXED = "a1b2A1B2"
ZEROSET = {"a1", "b1", "a2", "a1b1", "a2b1", "a1a2", "a1b1A1B1", "a1b1a1"}


def parse(word):
    return [word[i:i + 2] for i in range(0, len(word), 2)]


def sigma(word):
    out = []
    for tok in parse(word):
        out.append(tok[0] + ('2' if tok[1] == '1' else '1'))
    return "".join(out)


def phase_class(x):
    if x.is_zero():
        return "zero"
    if x.a != 0 and x.a == x.b:
        return "1+w"
    if x.a != 0 and x.a == -x.b:
        return "1-w"
    return "other"


def fmtk(x):
    if x.is_zero():
        return "0"
    return f"({x.a}{'+' if x.b >= 0 else ''}{x.b}w)"


# the banked 4b classes per original word (loud words) per block
CLASS_4B = {4: "1+w", 8: "1-w"}
CONJ = {"1+w": "1-w", "1-w": "1+w"}

verdict = True
for m in (4, 8):
    v = BLOCKS[m][0]
    v2h = mscale(half, mmul(v, v))
    c = (meye(27), v, v2h)
    ci = (meye(27), mscale(K(-1), v), v2h)
    y1 = tmul(tmul(c, const(B27)), ci)          # copy-1 b, TWISTED
    Y1 = tmul(tmul(c, const(B27i)), ci)
    LM = {'a1': const(A27), 'b1': y1, 'A1': const(A27i), 'B1': Y1,
          'a2': const(A27), 'b2': const(mconj(B27)),
          'A2': const(A27i), 'B2': const(mconj(B27i))}
    print(f"V1' mirrored configuration, block m={m}:", flush=True)
    ok = True
    for w in WORDS:
        sw = sigma(w)
        M = (meye(27), ZERO, ZERO)
        for tok in parse(sw):
            M = tmul(M, LM[tok])
        r2 = jpair(v0, matvec(M[2], v0))
        cls = phase_class(r2)
        if w in ZEROSET:
            expect = "zero"
        elif w == MIXED:
            expect = CLASS_4B[m]                # conj of the 4b mixed class
        else:
            expect = CONJ[CLASS_4B[m]]          # conj of the 4b loud class
        good = cls == expect
        ok &= good
        print(f"    sigma({w:10s}) = {sw:10s} {fmtk(r2):>40s}  class "
              f"{cls:5s} expect {expect:5s}  [{good}]", flush=True)
    print(f"  m={m}: V1' verdict {ok}", flush=True)
    verdict &= ok

print(f"\nV1' VERDICT (the copy-exchange mirror kill cell): "
      f"{'PASS — mirror-equivariant' if verdict else 'FAIL'}", flush=True)
print("banked blind; V2 runs only after this output is committed.", flush=True)
