#!/usr/bin/env python3
"""B1352 stage C -- THE TANGENT SPACE OF THE FIXED-VECTOR LOCUS AT THE SUBREGULAR POINT, exactly.

At rho_0 the cusp holonomy (mu_0, lambda_0) fixes three vectors of the 27 (the weight-0 vectors of the blocks 13, 9, 5).  A
first-order deformation z in Z^1(M; e6) keeps a fixed vector continuing v0 iff there is dv with
        z(mu) v0 + (mu_0 - I) dv = 0     and     z(lambda) v0 + (lambda_0 - I) dv = 0
(the first-order fixed-vector equations).  Tested exactly over Q(omega) for each of the eight block classes (obstruction.py)
and each of the three fixed vectors: which directions of H^1(M; e6) are tangent to the fixed-vector locus.  Also the joint
question on the V10 plane (any combination of the two V10 classes)."""
from __future__ import annotations
import os, sys, time
import numpy as np
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'B1350_the_v10_direction', 'verification'))
import obstruction as O
E, S, Qw = O.E, O.S, O.Qw
from fractions import Fraction as F
t0 = time.time()
rho0 = O.rho0
n = 27
I27 = E.qw_eye(n)
mu0 = rho0.M[1]; lam0 = rho0.ev(S.LONG)
def qw_kernel(M):
    """exact kernel (list of column vectors) of a Qw matrix, by Gaussian elimination."""
    A = [[M[i, j] for j in range(M.shape[1])] for i in range(M.shape[0])]
    nr, nc = len(A), len(A[0]); piv = []; r = 0
    for c in range(nc):
        p = next((i for i in range(r, nr) if not A[i][c].is_zero()), None)
        if p is None: continue
        A[r], A[p] = A[p], A[r]; inv = A[r][c].inv(); A[r] = [x * inv for x in A[r]]
        for i in range(nr):
            if i != r and not A[i][c].is_zero():
                f = A[i][c]; A[i] = [x - f * y for x, y in zip(A[i], A[r])]
        piv.append(c); r += 1
    free = [c for c in range(nc) if c not in piv]
    out = []
    for fc in free:
        v = [E.ZERO] * nc; v[fc] = E.ONE
        for i, pc in enumerate(piv): v[pc] = -A[i][fc]
        out.append(v)
    return out
fixed = qw_kernel(np.vstack([mu0 - I27, lam0 - I27]))
print(f"=== rho_0: {len(fixed)} cusp-fixed vectors of the 27 (exact) ===")
def e6_in_27(Z):
    """the e6 element with Chevalley coordinates Z (78 Qw) as a 27x27 Qw matrix."""
    acc = E.qw_zeros(n)
    for k in range(78):
        if not Z[k].is_zero():
            Rk = E.REP[k]
            for i in range(n):
                for j in range(n):
                    if Rk[i, j] != 0:
                        acc[i, j] = acc[i, j] + Z[k] * Qw(F(Rk[i, j]))
    return acc
def cocycle_value(Za, Zb, word):
    """z(word) in e6 c gl(27), from the values on the generators, left convention: z(xy) = z(x) + Ad(rho(x)) z(y)."""
    za, zb = e6_in_27(Za), e6_in_27(Zb)
    acc = E.qw_zeros(n); cur = E.qw_eye(n)
    for L in word:
        if L > 0:
            zg = za if L == 1 else zb
            acc = acc + cur.dot(zg).dot(cur_inv(cur)); cur = cur.dot(rho0.M[L])
        else:
            cur = cur.dot(rho0.I[-L]); zg = za if L == -1 else zb
            acc = acc - cur.dot(zg).dot(cur_inv(cur))
    return acc
# Ad(g) z = g z g^-1 needs inverses of the partial products; keep them alongside
def cur_inv(cur):
    return CUR_INV[id(cur)]
def cocycle_value2(Za, Zb, word):
    za, zb = e6_in_27(Za), e6_in_27(Zb)
    acc = E.qw_zeros(n); cur = E.qw_eye(n); curi = E.qw_eye(n)
    for L in word:
        if L > 0:
            zg = za if L == 1 else zb
            acc = acc + cur.dot(zg).dot(curi); cur = cur.dot(rho0.M[L]); curi = rho0.I[L].dot(curi)
        else:
            cur = cur.dot(rho0.I[-L]); curi = rho0.M[-L].dot(curi); zg = za if L == -1 else zb
            acc = acc - cur.dot(zg).dot(curi)
    return acc
def consistent(A, b):
    """is A x = b solvable (exact)?"""
    return S.exact_rank_qw(np.hstack([A, b])) == S.exact_rank_qw(A)
labels = [f"V{w}" + ("#2" if i == 5 else "") for i, (w, _, _) in enumerate(O.COC)]
Aeq = np.vstack([mu0 - I27, lam0 - I27])          # 54 x 27, the unknown dv
res = {}
print("first-order fixed-vector condition z(mu) v0 + (mu0 - I) dv = 0, z(lambda) v0 + (lambda0 - I) dv = 0:")
for i, (w, Za, Zb) in enumerate(O.COC):
    zmu = cocycle_value2(Za, Zb, [1]); zlam = cocycle_value2(Za, Zb, S.LONG)
    row = []
    for k, v0 in enumerate(fixed):
        v0c = np.array([[x] for x in v0], dtype=object)
        b = -np.vstack([zmu.dot(v0c), zlam.dot(v0c)])
        row.append(consistent(Aeq, b))
    res[labels[i]] = row
    print(f"  {labels[i]:5s}: keeps fixed vector 0/1/2 to first order: {row}")
# the V10 plane: combinations c1 z1 + c2 z2 -- the condition is linear in z, so the set of tangent combinations is a subspace:
# both fail => a combination could still succeed only if the failures are proportional; test the augmented rank with both rhs
i1, i2 = 4, 5
z1 = (cocycle_value2(O.COC[i1][1], O.COC[i1][2], [1]), cocycle_value2(O.COC[i1][1], O.COC[i1][2], S.LONG))
z2 = (cocycle_value2(O.COC[i2][1], O.COC[i2][2], [1]), cocycle_value2(O.COC[i2][1], O.COC[i2][2], S.LONG))
for k, v0 in enumerate(fixed):
    v0c = np.array([[x] for x in v0], dtype=object)
    b1 = -np.vstack([z1[0].dot(v0c), z1[1].dot(v0c)]); b2 = -np.vstack([z2[0].dot(v0c), z2[1].dot(v0c)])
    rA = S.exact_rank_qw(Aeq); r12 = S.exact_rank_qw(np.hstack([Aeq, b1, b2]))
    # dimension of {(c1, c2): c1 b1 + c2 b2 in im(Aeq)} = 2 - (r12 - rA)
    print(f"  V10 plane, fixed vector {k}: dimension of the tangent combinations = {2 - (r12 - rA)}")
print(f"[{time.time() - t0:.0f} s]")
