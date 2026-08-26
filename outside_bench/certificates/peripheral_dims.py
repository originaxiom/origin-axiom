#!/usr/bin/env python3
"""CELL A4 CERTIFICATE: PERIPHERAL DIMENSIONS AND THE 12/15 COINCIDENCE TEST.

Carrier: rho_Psi = rho_2 (x) rho_27, rho_2 the SL2(Q(q)) holonomy on the
meridian a = [[1,1],[0,1]] (pair-field entries), rho_27 the exact e6-27 rep
of a (a single positive-root exponential A27 = exp(rho27(E_r0))) and of b
(the "Riley" B = [[1,0],[q,1]] image, B27 = exp(q.rho27(F_r0))), all on the
banked bridge root r0 = ROOTS[0].  The longitude is lambda = bABaaBAb.

PREREGISTERED (two-outcome; every claim an assert):
  FACT 1 (anchor, banked): dim ker(rho_Psi(a) - I) = 27.
  FACT 2 (measured): dim ker(rho_Psi(lambda) - I) >= 12 (the joint cusp-fixed
    space {mu, lambda both fix} is banked at exactly 12, memo 51 FACT 5).
    Extra (measured, not preregistered to a value): whether the longitude-
    alone fixed space equals the joint space (i.e. ker(lambda-I) subset
    ker(a-I)), checked by an exact rank-containment test.
  FACT 3 (two-outcome): is ker(rho_Psi(a)-I) invariant under rho_Psi(b)?
    Generic expectation: NOT invariant (a,b do not commute). Measured via
    dim( rho_Psi(b).ker(a-I) cap ker(a-I) ), exact, by the standard
    dim(U)+dim(V)-dim(U+V) formula on spanning sets over the pair field.
  FACT 4 (the coincidence test, two independently computed splits that must
    agree numerically):
    4a. the 27's own weight-parity split (Hint diagonal, wt in {-1,0,1}):
        12 odd-weight (wt=+-1) + 15 even-weight (wt=0) states.
    4b. the lock split of ker(rho_Psi(a)-I) under C_Psi = (-I_2)(x)C_27,
        C_27=(-1)^wt: computed as an exact restricted-nullspace dimension,
        expected (banked memo 50 numbers 24-12=12, 30-15=15) to come out
        12 locked + 15 unlocked, and assert 4a == 4b coordinatewise.
  FACT 4' (structural derivation, settles "coincidence or structure"):
    write N27 = A27 - I. A27 = exp(single root vector) so N27^2 = 0 is
    checked, not assumed. A general kernel vector of rho_Psi(a)-I decomposes
    (SL2 factor basis e1,e2, N2 = A2-I nilpotent order 1 rank 1) as
        v = e1 (x) x + e2 (x) y,   y in ker(N27),   N27 x = -y.
    Because N27^2=0, im(N27) subset ker(N27) automatically, so the map
    v -> y is a surjection ker(rho_Psi(a)-I) -> im(N27) with kernel
    e1 (x) ker(N27); this SHORT EXACT SEQUENCE gives
        dim ker(rho_Psi(a)-I) = dim ker(N27) + rank(N27) = 27
    by the rank-nullity theorem applied to N27 on the 27 itself -- so the
    "27" is STRUCTURAL (forced for ANY single-root-vector meridian, not
    special to r0). Checked: N27 is exactly block-diagonal across the
    weight-parity split (c27 commutes with A27); on the 15-dim even
    (wt=0) block N27 vanishes IDENTICALLY (checked), so the entire even
    block lifts freely as e1(x)(even block) -- this is why "15" reappears:
    it is FORCED (dim of a block N27 kills outright), not a coincidence.
    On the 12-dim odd (wt=+-1) block, N27|odd has rank = nullity = 6
    (checked; not forced by rank-nullity alone, which only gives
    rank+nullity=12 -- this specific 6/6 split IS a fact about r0, and it
    is what makes the locked count come out to 2*6=12, matching the odd
    block's own size 12). So: the "15" match is structural/tautological;
    the "12" match is a genuine (verified, non-tautological) coincidence
    of this root's nilpotent rank, reported exactly, not assumed.
    An explicit basis of ker(rho_Psi(a)-I) is built from this
    parametrization and checked (i) each vector solves (rho_Psi(a)-I)v=0
    exactly and (ii) the 27 vectors have full rank 27 (span the kernel).

If any assert fails, the failing branch is the result: file, pin, correct.
"""
import os
from collections import Counter
SCR = os.path.dirname(os.path.abspath(__file__))
src = open(SCR + "/twisted_double.py").read()
exec(src[: src.index("# ---------------- stage 4")])

LAM = 'bABaaBAb'

# ---- pair-field scalars, SL2 generators (Riley presentation)
Z = (F(0), F(0)); O = (F(1), F(0)); Qp = (F(0), F(1))
A2 = [[O, O], [Z, O]]
B2 = [[O, Z], [Qp, O]]
def m2(X, Y):
    return [[fadd(fmul(X[i][0], Y[0][j]), fmul(X[i][1], Y[1][j])) for j in range(2)] for i in range(2)]
def inv2x2(X):
    d = fsub(fmul(X[0][0], X[1][1]), fmul(X[0][1], X[1][0]))
    assert d == O
    return [[X[1][1], fneg(X[0][1])], [fneg(X[1][0]), X[0][0]]]
d2 = {'a': A2, 'A': inv2x2(A2), 'b': B2, 'B': inv2x2(B2)}
def word2(w):
    M = [[O, Z], [Z, O]]
    for ch in w:
        M = m2(M, d2[ch])
    return M
L2 = word2(LAM)

# ---- internal bridge on the 27, r0 = ROOTS[0] (banked bridge root)
r0 = ROOTS[0]
E27p = toF(rho27_Q(evec(r0)))
F27p = toF(rho27_Q([-x for x in evec(tuple(-t for t in r0))]))
A27 = nilexp(E27p, ONE); A27i = nilexp(E27p, fneg(ONE))
B27 = nilexp(F27p, QQ); B27i = nilexp(F27p, fneg(QQ))
d27 = {'a': A27, 'A': A27i, 'b': B27, 'B': B27i}
def mmF(X, Y):
    n = len(X)
    out = [[Z] * n for _ in range(n)]
    for i in range(n):
        Xi = X[i]
        for k in range(n):
            x = Xi[k]
            if x == Z:
                continue
            Yk = Y[k]; Oi = out[i]
            for j in range(n):
                if Yk[j] != Z:
                    Oi[j] = fadd(Oi[j], fmul(x, Yk[j]))
    return out
def meye(n):
    return [[O if i == j else Z for j in range(n)] for i in range(n)]
def word27(w):
    M = meye(27)
    for ch in w:
        M = mmF(M, d27[ch])
    return M
L27 = word27(LAM)

hA = [F(0)] * DIM
for k in range(N):
    hA[k] = F(r0[k])
Hint = rho27_Q(hA)
wt = [int(Hint[a][a]) for a in range(27)]
assert dict(Counter(wt)) == {1: 6, 0: 15, -1: 6}
c27 = [(1 if w % 2 == 0 else -1) for w in wt]

# ---- carrier
def kronF(X, Y):
    nx = len(X); ny = len(Y)
    out = [[Z] * (nx * ny) for _ in range(nx * ny)]
    for i in range(nx):
        for j in range(nx):
            if X[i][j] == Z:
                continue
            for a in range(ny):
                for b in range(ny):
                    if Y[a][b] == Z:
                        continue
                    out[i * ny + a][j * ny + b] = fmul(X[i][j], Y[a][b])
    return out
APsi = kronF(A2, A27)
BPsi = kronF(B2, B27)
LPsi = kronF(L2, L27)

# =========================== FACT 1 ===========================
NA = msub(APsi, eye(54))
d1 = nullity(NA)
print(f"FACT 1: dim ker(rho_Psi(a) - I) = {d1}  (preregistered anchor: 27)")
assert d1 == 27
kerA = nullspace(NA)
assert len(kerA) == 27
for v in kerA:
    assert all(x == Z for x in mvec(NA, v)), "kernel basis vector not exact"

# =========================== FACT 2 ===========================
NLam = msub(LPsi, eye(54))
d2 = nullity(NLam)
print(f"FACT 2: dim ker(rho_Psi(lambda) - I) = {d2}  (measured; expect >= 12)")
assert d2 >= 12
# containment test: is ker(lambda-I) subset ker(a-I)? (rank of stacked system
# unchanged when NA's rows are added on top of NLam's rows)
rkLam = rank(NLam)
rkBoth = rank(NLam + NA)
contained = (rkBoth == rkLam)
print(f"        ker(lambda-I) subset ker(a-I): {contained}  (rank {rkLam} -> {rkBoth})")
assert contained
print("        => the longitude-alone fixed space COINCIDES with the banked")
print("           joint (mu,lambda)-fixed space (both dimension", d2, ")")
assert d2 == 12

# =========================== FACT 3 ===========================
BkerA = [mvec(BPsi, v) for v in kerA]
dimU = len(kerA)
dimV = rank(BkerA)
assert dimV == dimU, "rho_Psi(b) is invertible, must preserve dimension of the image"
dimSum = rank(kerA + BkerA)
dimInt = dimU + dimV - dimSum
invariant = (dimInt == dimU)
print(f"FACT 3: dim( rho_Psi(b).ker(a-I) cap ker(a-I) ) = {dimInt}  (of {dimU})")
print(f"        ker(rho_Psi(a)-I) invariant under rho_Psi(b): {invariant}")
assert not invariant, "generic expectation was NOT invariant"
assert 0 < dimInt < dimU

# =========================== FACT 4a: internal 27 parity split =====
odd_idx = [a for a in range(27) if c27[a] == -1]
even_idx = [a for a in range(27) if c27[a] == 1]
assert len(odd_idx) == 12 and len(even_idx) == 15
print(f"FACT 4a: internal 27 weight-parity split: odd(wt=+-1)={len(odd_idx)}, even(wt=0)={len(even_idx)}")

# =========================== FACT 4b: lock split of ker(a-I) =======
cP = [-c27[a] for i in range(2) for a in range(27)]   # C_Psi = (-I_2)(x)C_27
assert sum(1 for x in cP if x == 1) == 24
locked_coords = [i for i in range(54) if cP[i] == 1]
unlocked_coords = [i for i in range(54) if cP[i] == -1]
assert len(locked_coords) == 24 and len(unlocked_coords) == 30

def restricted_nullity(M, zero_coords):
    rows = [row[:] for row in M]
    for i in zero_coords:
        r = [Z] * len(M[0]); r[i] = O
        rows.append(r)
    return nullity(rows)

lock_dim = restricted_nullity(NA, unlocked_coords)   # solutions vanishing on unlocked => living in locked
unlock_dim = restricted_nullity(NA, locked_coords)   # solutions vanishing on locked => living in unlocked
print(f"FACT 4b: lock split of ker(rho_Psi(a)-I): locked={lock_dim}, unlocked={unlock_dim}")
assert lock_dim == 12 and unlock_dim == 15
assert lock_dim + unlock_dim == d1
assert lock_dim == len(odd_idx) and unlock_dim == len(even_idx)
print("        => FACT 4a and FACT 4b agree numerically: 12=12, 15=15")

# =========================== FACT 4': structural derivation ========
N27 = msub(A27, eye(27))
N27sq = mmul(N27, N27)
n27sq_zero = all(x == Z for row in N27sq for x in row)
print(f"FACT 4'.1: N27^2 = 0 (single-root exponential is order-2 nilpotent): {n27sq_zero}")
assert n27sq_zero

cross = any(N27[i][j] != Z for i in range(27) for j in range(27) if c27[i] != c27[j])
print(f"FACT 4'.2: N27 has nonzero entries across the odd/even parity blocks: {cross}")
assert not cross
print("           (forced: c27 commutes with A27, cf. memo 51 FACT 1)")

# even block: N27 must vanish identically there
even_block_zero = all(N27[i][j] == Z for i in even_idx for j in range(27))
print(f"FACT 4'.3: N27 vanishes identically on the 15-dim even (wt=0) block: {even_block_zero}")
assert even_block_zero
print("           => the WHOLE even block lifts freely (e1 (x) even-block) into")
print("              ker(rho_Psi(a)-I): the '15' match is STRUCTURAL/forced.")

# odd block: rank/nullity split
N27_odd = [[N27[i][j] for j in odd_idx] for i in odd_idx]
rank_odd = rank(N27_odd)
null_odd = nullity(N27_odd)
print(f"FACT 4'.4: on the 12-dim odd block, rank(N27|odd)={rank_odd}, nullity(N27|odd)={null_odd}")
# (rank + nullity = 12 is the rank-nullity theorem, stated not asserted)
assert rank_odd == null_odd == 6
print("           (rank=nullity=6 is NOT forced by rank-nullity alone -- it is a")
print("            genuine fact about r0, verified here, not assumed)")

# rank-nullity on N27 itself gives the structural 27
d_kerN27 = nullity(N27)
r_N27 = rank(N27)
print(f"FACT 4'.5: dim ker(N27) = {d_kerN27}, rank(N27) = {r_N27}, sum = {d_kerN27 + r_N27} (= dim of the 27)")
# (d_kerN27 + r_N27 = 27 is the rank-nullity theorem, stated not asserted;
# the substantive identity is that it equals the CARRIER kernel dimension d1)
assert d_kerN27 + r_N27 == d1
print("           => dim ker(rho_Psi(a)-I) = dim ker(N27) + rank(N27) = 27 is the")
print("              rank-nullity theorem for N27 acting on the 27 ITSELF: this holds")
print("              for ANY single-root-vector meridian, not just r0 -- STRUCTURAL.")

# ---- explicit parametrized basis of ker(rho_Psi(a)-I), checked directly
def solve_particular(M, rhs):
    """particular solution of M x = rhs (M square, consistent) with free vars = 0."""
    n = len(M)
    aug = [M[i][:] + [rhs[i]] for i in range(n)]
    R, piv = rref(aug)
    x = [Z] * n
    for i, c in enumerate(piv):
        x[c] = R[i][n]
    # verify consistency: rows past the pivots must have zero RHS
    for i in range(len(piv), n):
        assert R[i][n] == Z, "inconsistent system: rhs not in image"
    return x

ker_N27_odd = nullspace(N27_odd)   # basis, length 12 vectors (odd-block coords), dim 6
assert len(ker_N27_odd) == 6

basis = []
# (i) e1 (x) x, x in ker(N27) restricted to even coords (free, 15-dim)
for j in even_idx:
    x = [Z] * 27; x[j] = O
    v = [Z] * 54
    for a in range(27):
        v[0 * 27 + a] = x[a]   # e1 component
    basis.append(v)
# (ii) e1 (x) x, x in ker(N27|odd) embedded (homogeneous part, 6-dim)
for kv in ker_N27_odd:
    x = [Z] * 27
    for idx_pos, a in enumerate(odd_idx):
        x[a] = kv[idx_pos]
    v = [Z] * 54
    for a in range(27):
        v[0 * 27 + a] = x[a]
    basis.append(v)
# (iii) e1 (x) x_particular + e2 (x) y, y ranging over ker(N27|odd)=im(N27|odd) (6-dim)
odd_block_matrix = N27_odd
for kv in ker_N27_odd:
    rhs = [fneg(t) for t in kv]
    x_odd = solve_particular(odd_block_matrix, rhs)
    x = [Z] * 27
    for idx_pos, a in enumerate(odd_idx):
        x[a] = x_odd[idx_pos]
    y = [Z] * 27
    for idx_pos, a in enumerate(odd_idx):
        y[a] = kv[idx_pos]
    v = [Z] * 54
    for a in range(27):
        v[0 * 27 + a] = x[a]
        v[1 * 27 + a] = y[a]
    basis.append(v)

print(f"FACT 4'.6: explicit parametrized basis built: {len(basis)} vectors "
      f"(15 free-even + 6 odd-homogeneous + 6 odd-lifted)")
assert len(basis) == 27
for v in basis:
    img = mvec(NA, v)
    assert all(x == Z for x in img), "explicit basis vector does not solve (rho_Psi(a)-I)v=0"
rk_explicit = rank(basis)
print(f"           rank of the explicit basis: {rk_explicit}")
assert rk_explicit == 27
rk_combined = rank(basis + kerA)
print(f"           rank(explicit basis + computed nullspace) = {rk_combined} (same span)")
assert rk_combined == 27
print("           => every element of ker(rho_Psi(a)-I) IS of the derived shape")
print("              v = e1(x)x + e2(x)y,  y in ker(N27),  N27 x = -y.")

print(f"""
CONCLUSION: dim ker(rho_Psi(a)-I) = 27 (anchor, structural via rank-nullity of the
internal nilpotent N27 = A27-I on the 27 itself: ANY single-root-vector meridian
forces this, for any e6-27 bridge root). dim ker(rho_Psi(lambda)-I) = {d2}, and it
COINCIDES with (not just contains) the banked joint cusp-fixed space. ker(a-I) is
NOT rho_Psi(b)-invariant (intersection dimension {dimInt} of {dimU}). The 12/15
coincidence between the internal 27's weight-parity split and the lock split of
ker(a-I) is REAL (both computed independently, agree exactly) but has TWO
different causes: the 15 is forced (N27 kills the whole even/wt=0 block outright,
so it always contributes its full dimension), while the 12 is a genuine
(verified) numeric fact that rank(N27|odd) = nullity(N27|odd) = 6 for this
particular root r0 -- not a general theorem. The kernel's exact parametrized
shape is derived and checked directly above. Gate 5 untouched: no measured
physical constants entered any computation.""")
