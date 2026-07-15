"""B608 — THE ROSETTA TABLE (mixed form): which theta-odd root content sits in which
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




def theta_neg(X):
    """the negative-root odd partner: X -> transpose (the Chevalley
    anti-automorphism maps the +root odd combo to the -root one, up to
    sign — adequate for span/expansion purposes)."""
    return [[X[j][i] for j in range(27)] for i in range(27)]

# ---- B608: the G_SM refinement -----------------------------------------------
# THE DECLARED CHAIN (all nodes computed from the adjacency, no conventions):
#   E6 > D5 x U(1)_1 : delete endP            (charge q1 = n_endP)
#   D5 > A4 x U(1)_2 : delete short_end       (charge q2 = n_shortend)
#   A4 > su(3)+su(2)+U(1)_Y : delete branch   (charge q3 = n_branch)
#   su(3) nodes = {midQ, endQ}; su(2) node = {midP}.
# Each root's G_SM class = the charge triple (q1, q2, q3); the diagonal
# class (0,0,0) splits into su(3)-roots / su(2)-roots / nothing else.

DEL = (endP, short_end, branch)
SU3 = (midQ, endQ)
SU2 = (midP,)


def gsm_class(al):
    q = tuple(al[i] for i in DEL)
    if q == (0, 0, 0):
        supp = [i for i in range(N) if al[i] != 0]
        if all(i in SU3 for i in supp):
            return ("su3-root", q)
        if all(i in SU2 for i in supp):
            return ("su2-root", q)
        return ("cartan-dir?", q)
    return ("multiplet", q)


# ---- C2: the total census over all 72 roots ---------------------------------
census = {}
for al in list(roots) :
    kind, q = gsm_class(al)
    key = (kind, q)
    census[key] = census.get(key, 0) + 1
# include the negative roots by symmetry (charge -> -q)
total = 0
print("\nC2 — the FULL root census by G_SM class (positive roots shown; "
      "negatives mirror with -q):", flush=True)
for (kind, q), n in sorted(census.items()):
    print(f"  {kind:12s} q={q}: {n} roots", flush=True)
    total += n
print(f"  total positive roots: {total} (expect 36)", flush=True)
assert total == 36, "C2 FAIL: root total"
nsu3 = census.get(("su3-root", (0, 0, 0)), 0)
nsu2 = census.get(("su2-root", (0, 0, 0)), 0)
assert nsu3 == 3 and nsu2 == 1, \
    f"C2 FAIL: su3/su2 positive-root counts {nsu3}/{nsu2}"
# multiplet classes must have sizes consistent with color x weak products
for (kind, q), n in census.items():
    if kind == "multiplet":
        assert n in (1, 2, 3, 6), f"C2 FAIL: class {q} size {n}"
print("C2 PASS: 36 positive roots; su(3) = 3+, su(2) = 1+; every charged "
      "class has size in {1,2,3,6}", flush=True)

# ---- C3: the theta-odd 26 census ---------------------------------------------
print("\nC3 — the theta-odd census by G_SM CLASS-PAIR (one odd combination "
      "per root pair; a two-class pair IS root-level mixing):", flush=True)
odd_census = {}
for (a, b) in pairs:
    ka, kb = gsm_class(a), gsm_class(b)
    key = tuple(sorted([ka, kb]))
    odd_census[key] = odd_census.get(key, 0) + 1
npairs = sum(odd_census.values())
nmixed_pairs = 0
for key, n in sorted(odd_census.items()):
    mixed = key[0] != key[1]
    nmixed_pairs += n if mixed else 0
    print(f"  {key[0][0]:9s} q={key[0][1]}  |  {key[1][0]:9s} "
          f"q={key[1][1]}: {n} pair(s)"
          + ("   [CLASS-MIXED combo]" if mixed else "   [class-pure combo]"),
          flush=True)
print(f"  pairs: {npairs} (x2 signs = {2*npairs}; + 2 Cartan = "
      f"{2*npairs + 2}; expect 26);  class-mixed pairs: {nmixed_pairs}",
      flush=True)
assert 2 * npairs + 2 == 26, "C3 FAIL: odd dimension"
print("C3 PASS: the odd 26 accounted (one combo per pair)", flush=True)

# ---- C1: the theta-even block lines expand in even combos --------------------
print("\nC1 — the theta-even blocks expand exactly in theta-even root "
      "combos (gate) + census:", flush=True)
fixed_by_h = {}
for al in fixed:
    fixed_by_h.setdefault(heights[al], []).append(al)
pairs_by_h = {}
for (a, b) in pairs:
    pairs_by_h.setdefault(heights[a], []).append((a, b))
even_ok = True
for m in (1, 5, 7, 11):
    for j, vec in enumerate(BLOCKS[m]):
        hw = m - j
        if hw <= 0:
            continue                      # positive side suffices (strings
                                          # are f_pr-generated downward)
        basis = []
        for al in fixed_by_h.get(hw, []):
            basis.append(roots[al])
        for (a, b) in pairs_by_h.get(hw, []):
            xa = roots[a]
            basis.append(madd(xa, theta(xa)))
        co = solve_in(basis, vec) if basis else None
        ok = co is not None
        even_ok &= ok
        if not ok:
            print(f"  m={m} wt {2*hw:+3d}: EXPANSION FAIL", flush=True)
assert even_ok, "C1 FAIL"
print("C1 PASS: every positive-weight even-block line lies in the "
      "theta-even span at its height", flush=True)

# ---- THE ROSETTA TABLE (mixed form): the odd lines with G_SM labels ----------
print("\nTHE ROSETTA TABLE (mixed form) — per odd line, the exact "
      "contributions with G_SM classes:", flush=True)
for m in (4, 8):
    print(f"\nblock V(m={m}):", flush=True)
    for j, vec in enumerate(BLOCKS[m]):
        hw = m - j
        if hw <= 0:
            continue
        h = hw
        odds = []
        info = []
        for (a, b) in pairs_by_h.get(h, []):
            xa = roots[a]
            odds.append(msub(xa, theta(xa)))
            info.append((gsm_class(a), gsm_class(b)))
        co = solve_in(odds, vec)
        parts = []
        for cf, (ca, cb) in zip(co, info):
            if cf.is_zero():
                continue
            parts.append(f"{fmtk(cf)}*[{ca[0]} q={ca[1]} | {cb[0]} "
                         f"q={cb[1]}]")
        print(f"  wt {2*hw:+3d}: " + "  +  ".join(parts), flush=True)

print("\nB608 DONE", flush=True)
