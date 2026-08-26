#!/usr/bin/env python3
"""CELL A3: THE MIRROR ON THE DEEPEST LAYER.

On the carrier Psi = C^2 (x) 27 (54-dim over the pair field Q(q)/(q^2-q+1),
slot (i,a) -> 27*i+a), the meridian A_Psi = kron(A2,A27) has N = A_Psi - I
with N^3 = 0 and (banked, memo depth_lock.py) rank N = 27, rank N^2 = 6,
so dim ker N = 27, dim ker N^2 = 48.  gr3 := Psi / ker N^2 is the 6-dim top
graded layer (one dim per J3 chain).  The beat operator BtP = kron(W2,U27)
acts semilinearly, beta(v) = BtP * gal(v), gal(x,y) = (x+y,-y) the field
involution swapping the two roots of q^2-q+1=0.

PREREGISTERED (two-outcome; every claim an assert):
  1. ker N^2 has an exact pair-field basis of dimension 48 (elimination on
     the 54x54 matrix N^2), and there exist 6 standard basis slots e_p
     whose N^2-images (columns of N^2) are linearly independent (rank 6);
     together with the 48 kernel vectors these 6 slots form a basis of Psi
     (54x54 basis-change matrix has rank 54).
  2. A_Psi induces the IDENTITY on gr3: for each of the 6 complement slots
     e_p, A_Psi(e_p) - e_p = N(e_p) lies in ker N^2 (mechanism: N^3=0 =>
     N^2(N v) = 0 for all v), so the gr3-coordinate part of A_Psi(e_p) in
     the adapted basis is exactly e_p itself: the induced 6x6 matrix is I.
  3. beta induces a semilinear 6x6 pair-field matrix B on gr3 (beta(e_p)
     reduced mod ker N^2 via exact solving in the adapted 54-basis), and
     B * gal(B) = I_6 (beta^2 = meridian = identity on gr3, so the induced
     beta is a semilinear involution).
  4. the semilinear fixed space {v in F^6 : B*gal(v) = v} is a Q-vector
     space (viewing F^6 = Q^12); its Q-dimension is computed exactly and
     reported (no dimension is preregistered in advance -- this is a
     genuine measurement).
  5. the 6 chain-top slots (a = p mod 27 for each complement index p) carry
     a family class from the banked charge q3[a] in {16-class q=1,
     10-class q=-2, singlet-class q=4}; PREREGISTERED 5 of the 6 fall in
     one class and 1 in another (the exact classes are reported, since
     which two classes appear is itself part of the measurement); and the
     induced B, reordered into the (5+1) split, is checked for exact
     block-mixing: either the off-diagonal 5x1 / 1x5 blocks vanish (split
     preserved) or they do not (split mixed) -- both are legitimate results.

If any assert fails, the failing branch is filed as the result: the
expected fact, what the machine returned, the mechanism, then corrected
and rerun. Structure only -- Gate 5 (no measured physical constants) is
untouched throughout.
"""
import os
from fractions import Fraction as F
from collections import Counter
SCR = os.path.dirname(os.path.abspath(__file__))
src = open(SCR + "/twisted_double.py").read()
exec(src[:src.index("# ---------------- stage 4")])

# ------------------------------------------------------------------
# carrier matrices (pair-field), exactly as in depth_lock.py
# ------------------------------------------------------------------
r0 = ROOTS[0]
E27 = rho27_Q(evec(r0))
hA = [F(0)] * DIM
for k in range(N):
    hA[k] = F(r0[k])
Hint = rho27_Q(hA)
wt = [int(Hint[a][a]) for a in range(27)]
assert dict(Counter(wt)) == {1: 6, 0: 15, -1: 6}

FZ, FO, FQ = ZERO, ONE, QQ          # field 0, 1, q  (from twisted_double)
E27p = toF(E27)
A27f = nilexp(E27p, ONE)            # A = exp(e) on the 27
U27f = nilexp(E27p, QQ)             # scaled by q : the beat's 27-part
A2f = [[FO, FO], [FZ, FO]]
W2f = [[FO, FQ], [FZ, FO]]

def kronF(X, Y):
    nx, ny = len(X), len(Y)
    out = [[FZ] * (nx * ny) for _ in range(nx * ny)]
    for i in range(nx):
        for j in range(nx):
            if X[i][j] == FZ:
                continue
            for a in range(ny):
                for b in range(ny):
                    if Y[a][b] == FZ:
                        continue
                    out[i * ny + a][j * ny + b] = fmul(X[i][j], Y[a][b])
    return out

def mmF(X, Y):
    n, m = len(X), len(Y[0])
    k_ = len(Y)
    out = [[FZ] * m for _ in range(n)]
    for i in range(n):
        for t in range(k_):
            x = X[i][t]
            if x == FZ:
                continue
            for j in range(m):
                if Y[t][j] != FZ:
                    out[i][j] = fadd(out[i][j], fmul(x, Y[t][j]))
    return out

def mvecF(M, v):
    n = len(M)
    return [sum_f(fmul(M[i][k], v[k]) for k in range(len(v))) for i in range(n)]

def sum_f(it):
    s = FZ
    for x in it:
        s = fadd(s, x)
    return s

def gal(x):
    return (x[0] + x[1], -x[1])

def galvec(v):
    return [gal(x) for x in v]

def galmat(M):
    return [[gal(x) for x in row] for row in M]

APsif = kronF(A2f, A27f)
BtP = kronF(W2f, U27f)
Ident54 = [[FO if i == j else FZ for j in range(54)] for i in range(54)]
Nf = [[fsub(APsif[i][j], Ident54[i][j]) for j in range(54)] for i in range(54)]
N2f = mmF(Nf, Nf)
N3f = mmF(N2f, Nf)
assert all(x == FZ for row in N3f for x in row), "N^3 must vanish exactly (banked, memo 49/depth_lock)"

# ------------------------------------------------------------------
# exact field row-reduction (Gaussian elimination over Q(q))
# ------------------------------------------------------------------
def frref(rows_in, ncols):
    A = [row[:] for row in rows_in]
    nrows = len(A)
    pivots = []
    r = 0
    for c in range(ncols):
        piv = None
        for i in range(r, nrows):
            if A[i][c] != FZ:
                piv = i
                break
        if piv is None:
            continue
        A[r], A[piv] = A[piv], A[r]
        inv = finv(A[r][c])
        A[r] = [fmul(inv, x) for x in A[r]]
        for i in range(nrows):
            if i != r and A[i][c] != FZ:
                fct = A[i][c]
                A[i] = [ fsub(A[i][j], fmul(fct, A[r][j])) for j in range(len(A[i])) ]
        pivots.append(c)
        r += 1
        if r == nrows:
            break
    return A, pivots, r

# (1) rank / pivots of N^2, and the kernel basis
R2, piv2, rank2 = frref(N2f, 54)
print(f"1a. rank_F(N^2) = {rank2}  (banked expectation: 6)")
assert rank2 == 6
kerdim = 54 - rank2
print(f"    dim ker N^2 = {kerdim}  (banked expectation: 48)")
assert kerdim == 48

# free (non-pivot) columns give the kernel basis of N^2 by back substitution
free_cols = [c for c in range(54) if c not in piv2]
assert len(free_cols) == 48
kerN2_basis = []
for fc in free_cols:
    v = [FZ] * 54
    v[fc] = FO
    for ridx, pc in enumerate(piv2):
        v[pc] = fneg(R2[ridx][fc])
    kerN2_basis.append(v)
# verify: N2f @ v == 0 for every kernel-basis vector (real, non-tautological check)
for v in kerN2_basis:
    assert all(x == FZ for x in mvecF(N2f, v))
print("1b. all 48 kernel-basis vectors verified: N^2 v = 0 exactly")

# the 6 pivot columns of N^2's own rref ARE the indices of 6 standard basis
# slots e_p whose N^2-images (columns of N^2) are linearly independent
pivots6 = piv2
assert len(pivots6) == 6
sub = [[N2f[i][p] for p in pivots6] for i in range(54)]
_, subpiv, subrank = frref(sub, 6)
print(f"1c. complement slots (standard-basis indices): {pivots6}")
print(f"    rank of their N^2-images: {subrank}  (must be 6)")
assert subrank == 6

# basis-change matrix: 48 kernel vectors + 6 complement e_p's -> must be a
# basis of all of Psi (rank 54)
basis_cols = kerN2_basis + [[FO if k == p else FZ for k in range(54)] for p in pivots6]
basis_rows = [[basis_cols[j][i] for j in range(54)] for i in range(54)]
_, bpiv, brank = frref(basis_rows, 54)
print(f"1d. rank of [ker N^2 basis | complement slots] = {brank}  (must be 54)")
assert brank == 54

# ------------------------------------------------------------------
# generic "solve in the adapted basis": express w as combo of the 54
# basis_cols; return the 6 coordinates on the complement part
# ------------------------------------------------------------------
def solve_complement_coords(w):
    # augmented system: basis_rows (54x54) | w  -> rref -> read off solution
    aug = [basis_rows[i] + [w[i]] for i in range(54)]
    Ra, pv, rk = frref(aug, 54)
    assert rk == 54 and pv == list(range(54))
    sol = [Ra[i][54] for i in range(54)]
    return sol[48:54]   # coordinates on the 6 complement basis vectors

# ------------------------------------------------------------------
# (2) induced action of A_Psi on gr3 = identity
# ------------------------------------------------------------------
B_A = [[FZ] * 6 for _ in range(6)]
for j, p in enumerate(pivots6):
    ep = [FO if k == p else FZ for k in range(54)]
    w = mvecF(APsif, ep)
    coords = solve_complement_coords(w)
    for k in range(6):
        B_A[k][j] = coords[k]
Ident6 = [[FO if i == j else FZ for j in range(6)] for i in range(6)]
print("2.  induced A_Psi on gr3 (6x6, adapted basis):")
for row in B_A:
    print("   ", row)
assert B_A == Ident6, "FACT 2 failed: A_Psi should induce the identity on gr3"
print("    matches I_6 exactly: A_Psi induces the identity on gr3, as N maps Psi into ker N^2 (N^3=0).")

# ------------------------------------------------------------------
# (3) induced semilinear beta on gr3
# ------------------------------------------------------------------
Bmat = [[FZ] * 6 for _ in range(6)]
for j, p in enumerate(pivots6):
    ep = [FO if k == p else FZ for k in range(54)]
    gep = galvec(ep)
    w = mvecF(BtP, gep)
    coords = solve_complement_coords(w)
    for k in range(6):
        Bmat[k][j] = coords[k]
print("3.  induced beta on gr3, matrix B (6x6 over Q(q), adapted basis):")
for row in Bmat:
    print("   ", row)

galB = galmat(Bmat)
BgalB = mmF(Bmat, galB)
print("    B * gal(B) =")
for row in BgalB:
    print("   ", row)
assert BgalB == Ident6, "FACT 3 failed: beta^2 should equal the meridian = identity on gr3"
print("    B * gal(B) = I_6 exactly: the induced beta is a semilinear involution on gr3.")

# ------------------------------------------------------------------
# (4) semilinear fixed space {v : B*gal(v) = v}, as a Q-vector space
# ------------------------------------------------------------------
# build the 12x12 rational matrix of the Q-linear map v(12 reals)->B*gal(v)-v
def field_to_pair(w6):
    out = []
    for x in w6:
        out.append(x[0]); out.append(x[1])
    return out

def pair_to_field(v12):
    return [(v12[2*k], v12[2*k+1]) for k in range(6)]

L = [[F(0)] * 12 for _ in range(12)]
for col in range(12):
    v12 = [F(0)] * 12
    v12[col] = F(1)
    v6 = pair_to_field(v12)
    gv6 = galvec(v6)
    Bg = mvecF(Bmat, gv6)
    diff = [ (Bg[k][0] - v6[k][0], Bg[k][1] - v6[k][1]) for k in range(6) ]
    d12 = field_to_pair(diff)
    for row in range(12):
        L[row][col] = d12[row]

def qrref(rows_in, ncols):
    A = [row[:] for row in rows_in]
    nrows = len(A)
    pivots = []
    r = 0
    for c in range(ncols):
        piv = None
        for i in range(r, nrows):
            if A[i][c] != 0:
                piv = i
                break
        if piv is None:
            continue
        A[r], A[piv] = A[piv], A[r]
        pv = A[r][c]
        A[r] = [x / pv for x in A[r]]
        for i in range(nrows):
            if i != r and A[i][c] != 0:
                fct = A[i][c]
                A[i] = [x - fct * y for x, y in zip(A[i], A[r])]
        pivots.append(c)
        r += 1
        if r == nrows:
            break
    return A, pivots, r

_, Lpiv, Lrank = qrref(L, 12)
fixdim = 12 - Lrank
print(f"4.  rank_Q(B*gal(.) - I as a 12x12 real map) = {Lrank}")
print(f"    Q-dimension of the semilinear fixed space {{v : B*gal(v)=v}} = {fixdim}")
assert 0 <= fixdim <= 12

# ------------------------------------------------------------------
# (5) family classes of the 6 chain tops, and the mixing block
# ------------------------------------------------------------------
q3 = {a: 3 * ipr(weights[a], omega1) for a in range(27)}
assert all(q3[a] == int(q3[a]) for a in q3)
q3 = {a: int(q3[a]) for a in q3}
cnt = Counter(q3.values())
assert sorted(cnt.values()) == [1, 10, 16]
c16 = next(v for v, m in cnt.items() if m == 16)
c10 = next(v for v, m in cnt.items() if m == 10)
c1 = next(v for v, m in cnt.items() if m == 1)
def classof(a):
    if q3[a] == c16: return '16'
    if q3[a] == c10: return '10'
    if q3[a] == c1: return '1'
    raise AssertionError

tops_a = [p % 27 for p in pivots6]
tops_i = [p // 27 for p in pivots6]
tops_cls = [classof(a) for a in tops_a]
print(f"5a. chain-top slots (i,a): {list(zip(tops_i, tops_a))}")
print(f"    chain-top wt values: {[wt[a] for a in tops_a]}")
print(f"    chain-top family classes (q3-derived): {tops_cls}")
cls_count = Counter(tops_cls)
print(f"    class multiset: {dict(cls_count)}")
assert sorted(cls_count.values()) == [1, 5], (
    f"FACT 5 pre-registration failed: expected a 5+1 split of the 6 chain tops, got {dict(cls_count)}"
)
majority_cls = cls_count.most_common(1)[0][0]
minority_cls = next(c for c in cls_count if c != majority_cls)
print(f"    => 5 chain tops are '{majority_cls}'-class, 1 chain top is '{minority_cls}'-class")

order = [j for j, c in enumerate(tops_cls) if c == majority_cls] + \
        [j for j, c in enumerate(tops_cls) if c == minority_cls]
Badapt = [[Bmat[order[i]][order[j]] for j in range(6)] for i in range(6)]
print("5b. B reordered into the (5 majority + 1 minority) adapted basis:")
for row in Badapt:
    print("   ", row)
off_5x1 = [Badapt[i][5] for i in range(5)]
off_1x5 = [Badapt[5][j] for j in range(5)]
mixed = any(x != FZ for x in off_5x1) or any(x != FZ for x in off_1x5)
print(f"    off-diagonal 5x1 block (col 5, rows 0-4): {off_5x1}")
print(f"    off-diagonal 1x5 block (row 5, cols 0-4): {off_1x5}")
print(f"    the induced beta {'MIXES' if mixed else 'PRESERVES'} the {len(off_5x1)}+1 split on gr3")

print(f"""
SUMMARY (Cell A3 - mirror on the deepest layer):
  ker N^2 dim = 48, complement dim = 6 (exact pair-field elimination).
  A_Psi induces the identity on gr3 (verified as an explicit 6x6 = I_6).
  The beat beta induces a semilinear involution B on gr3: B*gal(B) = I_6.
  Semilinear fixed space of beta on gr3 has Q-dimension {fixdim}.
  The 6 chain tops split 5 ('{majority_cls}') + 1 ('{minority_cls}') by family
  charge q3, and the induced beta {'mixes' if mixed else 'preserves'} that split.
Structure only; Gate 5 (no measured physical constants) untouched.""")
