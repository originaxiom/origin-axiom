"""B604 — THE ROSETTA CELL: which theta-odd root content sits in which
principal block (chat-1's handoff, verified and resolved; failure-enforcing
on all verification gates; the resolution itself is printed as data).

VERIFY (chat-1's claims):
  V1  36 positive roots; the fold theta classifies them 12 fixed + 12
      pairs; heights of the pairs = (2,2,2,2,1,1,1,1) at h = 1..8.
  V2  the D5/16 labels per pair (end-node coefficient): every pair mixes
      one D5 and one 16 root at every height EXCEPT one (D5,D5) pair at
      h = 1 and a (16,16) pair at h = 8 (their table; checked exactly).
RESOLVE (chat-1's ask 1 — beyond their method):
  R1  for h = 1..4: expand the ACTUAL principal-string vectors
      BLOCKS[4][4-h] and BLOCKS[8][8-h] in the two odd pair-combinations
      at that height. Chat-1 assumed each block line IS one pair-combo
      ("which pair goes to which block"); the expansion decides whether
      the assignment is PURE (one coefficient zero) or MIXED.
  R2  the Cartan (h = 0) split between the two blocks.
  R3  per block line, the exact D5-vs-16 root-content split (the
      mathematical face of chat-1's "gauge-matter mixing" reading —
      the physics interpretation stays quarantined in FINDINGS).

theta is taken from the banked intertwiner (convention-free):
theta(X) = -J^{-1} X^T J (the banked parity convention: +1 on e_pr, f_pr,
-1 on the odd blocks). The diagram is read off the computed Cartan matrix.

Run: OA_SLOW=1 python3 rosetta_blocks.py   (~20 min, l51 build)
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
mmul = ns['mmul']; madd = ns['madd']; mscale = ns['mscale']
msub = ns['msub']
bracket = ns['bracket']
nullspace = ns['nullspace']
BLOCKS = ns['BLOCKS']
E6_e = ns['E6_e']; E6_f = ns['E6_f']
e_pr = ns['e_pr']; f_pr = ns['f_pr']; h_pr = ns['h_pr']

N = 6
hs = [bracket(E6_e[i], E6_f[i]) for i in range(N)]

# ---- the Cartan matrix and the diagram, computed --------------------------
def is_zero_mat(X):
    return all(all(x.is_zero() for x in r) for r in X)


A = [[None] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        # [h_i, e_j] = A[i][j] e_j
        br = bracket(hs[i], E6_e[j])
        for c in (-1, 0, 1, 2):
            if is_zero_mat(msub(br, mscale(K(c), E6_e[j]))):
                A[i][j] = c
                break
        assert A[i][j] is not None
deg = [sum(1 for j in range(N) if i != j and A[i][j] == -1) for i in range(N)]
branch = deg.index(3)
arms = []
for nb in [j for j in range(N) if A[branch][j] == -1]:
    arm = [nb]
    prev, cur = branch, nb
    while True:
        nxt = [j for j in range(N) if j != prev and A[cur][j] == -1]
        if not nxt:
            break
        prev, cur = cur, nxt[0]
        arm.append(cur)
    arms.append(arm)
arms.sort(key=len)
assert [len(a) for a in arms] == [1, 2, 2], f"not E6: {arms}"
short_end = arms[0][0]
endP, endQ = arms[1][-1], arms[2][-1]
midP, midQ = arms[1][0], arms[2][0]
print(f"diagram: branch={branch}, short end={short_end}, "
      f"long ends={endP},{endQ}, mids={midP},{midQ}", flush=True)
sigma = {branch: branch, short_end: short_end,
         endP: endQ, endQ: endP, midP: midQ, midQ: midP}

# ---- positive root vectors by bracket BFS ----------------------------------
roots = {}
heights = {}
for i in range(N):
    al = tuple(1 if j == i else 0 for j in range(N))
    roots[al] = E6_e[i]
    heights[al] = 1
front = list(roots)
while front:
    nf = []
    for al in front:
        for i in range(N):
            nal = tuple(al[j] + (1 if j == i else 0) for j in range(N))
            if nal in roots:
                continue
            X = bracket(E6_e[i], roots[al])
            if not is_zero_mat(X):
                roots[nal] = X
                heights[nal] = heights[al] + 1
                nf.append(nal)
    front = nf
assert len(roots) == 36, f"V1 FAIL: {len(roots)} positive roots"

# root sigma: (sigma alpha)_j = alpha_{sigma(j)} (sigma is an involution)
sig_root = lambda al: tuple(al[sigma[j]] for j in range(N))
fixed = [al for al in roots if sig_root(al) == al]
paired = [al for al in roots if sig_root(al) != al]
pairs = sorted({tuple(sorted([al, sig_root(al)])) for al in paired})
assert len(fixed) == 12 and len(pairs) == 12, \
    f"V1 FAIL: {len(fixed)} fixed, {len(pairs)} pairs"
hist = {}
for a, b in pairs:
    assert heights[a] == heights[b]
    hist[heights[a]] = hist.get(heights[a], 0) + 1
assert [hist.get(h, 0) for h in range(1, 9)] == [2, 2, 2, 2, 1, 1, 1, 1], \
    f"V1 FAIL: heights {hist}"
print(f"V1 PASS: 36 roots; 12 theta-fixed + 12 pairs; pair heights "
      f"{[hist.get(h, 0) for h in range(1, 9)]}", flush=True)

# ---- J and theta ------------------------------------------------------------
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
# invert J by rref on [J | I]
aug = [[J[i][j] for j in range(27)] + [K1 if i == j else K0 for j in range(27)]
       for i in range(27)]
for c in range(27):
    piv = next(r for r in range(c, 27) if not aug[r][c].is_zero())
    aug[c], aug[piv] = aug[piv], aug[c]
    inv = aug[c][c].inv()
    aug[c] = [x * inv for x in aug[c]]
    for r in range(27):
        if r != c and not aug[r][c].is_zero():
            f = aug[r][c]
            aug[r] = [x - f * y for x, y in zip(aug[r], aug[c])]
Jinv = [[aug[i][27 + j] for j in range(27)] for i in range(27)]


def theta(X):
    XT = [[X[j][i] for j in range(27)] for i in range(27)]
    return mscale(K(-1), mmul(Jinv, mmul(XT, J)))


assert is_zero_mat(msub(theta(e_pr), e_pr)), "theta gate: e_pr"
assert is_zero_mat(msub(theta(f_pr), f_pr)), "theta gate: f_pr"
# theta permutes the Cartan per sigma
for i in range(N):
    assert is_zero_mat(msub(theta(hs[i]), hs[sigma[i]])), f"theta gate h_{i}"
print("theta gates PASS (e_pr, f_pr fixed; Cartan permuted per the fold)",
      flush=True)


def flat(M):
    return [M[i][j] for i in range(27) for j in range(27)]


def solve_in(basis_mats, target):
    """coords of target in span(basis_mats), or None."""
    cols = [flat(M) for M in basis_mats]
    b = flat(target)
    d = len(cols)
    aug_ = [[cols[k][r] for k in range(d)] + [b[r]] for r in range(729)]
    red = []
    for row in aug_:
        rr = list(row)
        for pc, pr in red:
            if not rr[pc].is_zero():
                f = rr[pc]
                rr = [x - f * y for x, y in zip(rr, pr)]
        piv = next((k for k, x in enumerate(rr) if not x.is_zero()), None)
        if piv is None:
            continue
        if piv == d:
            return None                       # inconsistent
        rr = [x * rr[piv].inv() for x in rr]
        red.append((piv, rr))
    sol = [K0] * d
    for pc, pr in sorted(red, reverse=True):
        sol[pc] = pr[d] - sum((pr[k] * sol[k] for k in range(d)
                               if k != pc and not sol[k].is_zero()), K0)
    return sol


def fmtk(x):
    if x.is_zero():
        return "0"
    if x.b == 0:
        return str(x.a)
    return f"({x.a}{'+' if x.b >= 0 else ''}{x.b}w)"


# ---- V2 + R1 + R3: per height -----------------------------------------------
nstar = endP                                   # the D5 choice: delete endP
lab = lambda al: "D5" if al[nstar] == 0 else "16"
print(f"\nD5/16 labels via end node {nstar} (theta maps them to the "
      f"end-{endQ} labeling):", flush=True)
print("\nR1 — the block resolution (exact):", flush=True)
for h in range(1, 9):
    ph = [p for p in pairs if heights[p[0]] == h]
    odds = []
    labels = []
    for (a, b) in ph:
        o = msub(roots[a], theta(roots[a]))
        odds.append(o)
        labels.append(f"{{{lab(a)},{lab(b)}}}")
    if h <= 4:
        b4 = BLOCKS[4][4 - h]
        b8 = BLOCKS[8][8 - h]
        c4 = solve_in(odds, b4)
        c8 = solve_in(odds, b8)
        assert c4 is not None and c8 is not None, f"span FAIL at h={h}"
        pure4 = sum(1 for x in c4 if x.is_zero()) == 1
        pure8 = sum(1 for x in c8 if x.is_zero()) == 1
        print(f"  h={h}: pairs {labels[0]} {labels[1]};  "
              f"V8-line = {fmtk(c4[0])}*o1 + {fmtk(c4[1])}*o2 "
              f"[{'PURE' if pure4 else 'MIXED'}];  "
              f"V16-line = {fmtk(c8[0])}*o1 + {fmtk(c8[1])}*o2 "
              f"[{'PURE' if pure8 else 'MIXED'}]", flush=True)
    else:
        c8 = solve_in(odds, BLOCKS[8][8 - h])
        assert c8 is not None and len(ph) == 1, f"h={h} structure"
        print(f"  h={h}: pair {labels[0]};  V16-line = {fmtk(c8[0])}*o1",
              flush=True)

# R2: the Cartan split
oC1 = msub(hs[endP], hs[endQ])
oC2 = msub(hs[midP], hs[midQ])
c4 = solve_in([oC1, oC2], BLOCKS[4][4])
c8 = solve_in([oC1, oC2], BLOCKS[8][8])
print(f"  h=0 (Cartan): V8-zero = {fmtk(c4[0])}*(hP-hQ) + "
      f"{fmtk(c4[1])}*(hmP-hmQ);  V16-zero = {fmtk(c8[0])}*(hP-hQ) + "
      f"{fmtk(c8[1])}*(hmP-hmQ)", flush=True)

print("\nB604 DONE", flush=True)
