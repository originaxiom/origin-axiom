"""B598 P3 — V1, THE MIRROR-SWAP KILL CELL (sealed prereg cell 1 of 3;
failure-enforcing on machinery gates; the VERDICT is printed, not asserted
— the outcome statement uses only the locked A/B/D table).

Per STEP8_P3_PREREG.md (sealed, sha256 96a2d494...): rerun the step-4b
bending responses with the twist conjugator MIRRORED — v_m -> mconj(v_m),
c = exp(t vbar_m) — at the two hearing blocks m in {4, 8}, J-paired, the
frozen 20-word list.

REQUIRED for existence (V1 PASS): the phase classes SWAP exactly —
  mirrored m=4: every nonzero t^2 response in Q^x (1-w), the mixed word
                a1b2A1B2 in Q^x (1+w);
  mirrored m=8: every nonzero t^2 response in Q^x (1+w), the mixed word
                in Q^x (1-w);
  the word-pattern (zero set) preserved. A zero column or a non-swapped
  phase FAILS V1 (outcome D).

Run: OA_SLOW=1 python3 p3_v1_mirror_swap.py   (~25 min)
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


# ---- J and v0, rebuilt (the banked weight-reduced recipe) -------------------
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
# the banked (unmirrored) zero set from step 4b:
ZEROSET = {"a1", "b1", "a2", "a1b1", "a2b1", "a1a2", "a1b1A1B1", "a1b1a1"}


def parse(word):
    return [word[i:i + 2] for i in range(0, len(word), 2)]


def phase_class(x):
    """Return '1+w', '1-w', 'zero', or 'other' for x in Q(sqrt-3)."""
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


verdict = True
for m, want, want_mixed in ((4, "1-w", "1+w"), (8, "1+w", "1-w")):
    v = mconj(BLOCKS[m][0])                     # THE MIRRORED DIRECTION
    v2h = mscale(half, mmul(v, v))
    c = (meye(27), v, v2h)
    ci = (meye(27), mscale(K(-1), v), v2h)
    Bbar = mconj(B27)
    Bbari = mconj(B27i)
    y = tmul(tmul(c, const(Bbar)), ci)
    Y = tmul(tmul(c, const(Bbari)), ci)
    LM = {'a1': const(A27), 'b1': const(B27), 'A1': const(A27i),
          'B1': const(B27i), 'a2': const(A27), 'b2': y,
          'A2': const(A27i), 'B2': Y}
    print(f"mirrored block m={m} (require class {want}, mixed {want_mixed}):",
          flush=True)
    ok = True
    for w in WORDS:
        M = (meye(27), ZERO, ZERO)
        for tok in parse(w):
            M = tmul(M, LM[tok])
        r2 = jpair(v0, matvec(M[2], v0))
        cls = phase_class(r2)
        expect = "zero" if w in ZEROSET else (want_mixed if w == MIXED
                                              else want)
        good = cls == expect
        ok &= good
        print(f"    {w:10s} {fmtk(r2):>40s}  class {cls:5s} "
              f"expect {expect:5s}  [{good}]", flush=True)
    print(f"  mirrored m={m}: swap verdict {ok}", flush=True)
    verdict &= ok

print(f"\nV1 VERDICT (the mirror-swap kill cell): "
      f"{'PASS — the phase classes swap' if verdict else 'FAIL'}", flush=True)
print("banked blind; V2 runs only after this output is committed.", flush=True)
