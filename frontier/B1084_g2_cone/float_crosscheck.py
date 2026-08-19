#!/usr/bin/env python3
"""
INDEPENDENT SECOND implementation (numpy floating point, tol=1e-9) of the same
claim, using a deliberately different technique from exact_verify.py:
  - subspaces canonicalized via SVD -> orthogonal projection matrix (not RREF)
  - group closure keyed by rounded matrix entries (not exact Fractions)
This exists purely as a cross-check against a shared bug in the exact script.
Written from scratch; does not import cloud_handoff/certificates/g2cone.py or
g2strata.py, and does not import or reuse any code from exact_verify.py.
"""

import numpy as np
import itertools
import math
from collections import Counter

np.set_printoptions(suppress=True)

SQRT2 = math.sqrt(2)
TOL = 1e-9
ROUND = 7  # decimal places for hashing keys


def qmul(p, q):
    a1, b1, c1, d1 = p
    a2, b2, c2, d2 = q
    return np.array([
        a1 * a2 - b1 * b2 - c1 * c2 - d1 * d2,
        a1 * b2 + b1 * a2 + c1 * d2 - d1 * c2,
        a1 * c2 - b1 * d2 + c1 * a2 + d1 * b2,
        a1 * d2 + b1 * c2 - c1 * b2 + d1 * a2,
    ])


E4 = [np.array([1., 0, 0, 0]), np.array([0., 1, 0, 0]),
      np.array([0., 0, 1, 0]), np.array([0., 0, 0, 1])]


def left_mult_matrix(q):
    cols = [qmul(q, e) for e in E4]
    return np.array(cols).T


def right_mult_matrix(p):
    cols = [qmul(e, p) for e in E4]
    return np.array(cols).T


def block_diag(A, B):
    n = A.shape[0] + B.shape[0]
    M = np.zeros((n, n))
    M[:A.shape[0], :A.shape[0]] = A
    M[A.shape[0]:, A.shape[0]:] = B
    return M


def key(M, nd=ROUND):
    return tuple(np.round(M.flatten(), nd))


# ---- 2T ----
twoT = []
for idx in range(4):
    for s in (1, -1):
        v = np.zeros(4)
        v[idx] = s
        twoT.append(v)
for signs in itertools.product((1, -1), repeat=4):
    twoT.append(np.array(signs) * 0.5)
assert len(twoT) == 24
for q in twoT:
    assert abs(np.dot(q, q) - 1.0) < TOL

i_q = np.array([0., 1, 0, 0])
k_q = np.array([0., 0, 0, 1])
w_q = np.array([1 / SQRT2, 1 / SQRT2, 0., 0.])
assert abs(np.dot(w_q, w_q) - 1.0) < TOL

I3 = np.eye(3)
I4 = np.eye(4)
I7 = np.eye(7)
rot_axis1 = np.diag([1., -1., -1.])
rot_axis3 = np.diag([-1., -1., 1.])

R_i = right_mult_matrix(i_q)
R_k = right_mult_matrix(k_q)
L_w = left_mult_matrix(w_q)

g_tau = block_diag(rot_axis1, R_i)
g_sigma = block_diag(rot_axis3, L_w @ R_k)

twoT_matrices = [block_diag(I3, left_mult_matrix(q)) for q in twoT]
generators = twoT_matrices + [g_tau, g_sigma]

for M in generators:
    assert np.allclose(M.T @ M, I7, atol=TOL), "generator not orthogonal"
print("[float self-check] all generators orthogonal to 1e-9: OK")

# ---- closure ----
seen = {key(I7): I7}
frontier = [I7]
while frontier:
    nxt = []
    for M in frontier:
        for g in generators:
            P = M @ g
            k = key(P)
            if k not in seen:
                seen[k] = P
                nxt.append(P)
    frontier = nxt
    if len(seen) > 20000:
        break

group = list(seen.values())
print()
print(f"FLOAT ITEM 1: |Ghat| = {len(group)}   (claim: 96)")

twoT_keys = set(key(M) for M in twoT_matrices)
in_group = twoT_keys.issubset(seen.keys())
print(f"FLOAT ITEM 1: 2T-copy subset: {in_group}; |Ghat|/24 = {len(group)/24}")

# ---- item 2 ----
census = {}
type_counts = {}
idk = key(I7)
for M in group:
    if key(M) == idk:
        continue
    d3 = 3 - np.linalg.matrix_rank(M[:3, :3] - I3, tol=TOL)
    d4 = 4 - np.linalg.matrix_rank(M[3:, 3:] - I4, tol=TOL)
    dtot = 7 - np.linalg.matrix_rank(M - I7, tol=TOL)
    census[dtot] = census.get(dtot, 0) + 1
    type_counts[(d3, d4)] = type_counts.get((d3, d4), 0) + 1

print(f"FLOAT ITEM 2: census = {census}   (claim: {{3:53,1:42}})")
print(f"FLOAT ITEM 2: type breakdown = {type_counts}")

# ---- item 3 ----
S3 = [M for M in group if np.allclose(M[:3, :3], I3, atol=TOL)]
S3keys = set(key(M) for M in S3)
print(f"FLOAT ITEM 3: |stab(R^3 pointwise)| = {len(S3)}  equals 2T-copy: {S3keys == twoT_keys}")

# ---- item 5 ----
axis_stab = []
for idx in range(3):
    v = np.zeros(7)
    v[idx] = 1
    cnt = sum(1 for M in group if np.allclose(M @ v, v, atol=TOL))
    axis_stab.append(cnt)
print(f"FLOAT ITEM 5: axis stabilizer orders = {axis_stab}   (claim: [48,48,48])")

# ---- item 4 (independent method: SVD nullspace -> projection-matrix key) ----
special = []
for M in group:
    if key(M) == idk:
        continue
    d3 = 3 - np.linalg.matrix_rank(M[:3, :3] - I3, tol=TOL)
    d4 = 4 - np.linalg.matrix_rank(M[3:, 3:] - I4, tol=TOL)
    if (d3, d4) == (1, 2):
        A = M - I7
        u, s, vh = np.linalg.svd(A)
        rk = int(np.sum(s > TOL * max(1, s[0] if len(s) else 1)))
        null_basis = vh[rk:]   # rows spanning the nullspace (dim should be 3)
        assert null_basis.shape[0] == 3
        special.append((M, null_basis))

print(f"\nFLOAT ITEM 4: count with (dim_fix_R3,dim_fix_H)=(1,2): {len(special)}")


def subspace_proj_key(basis, nd=6):
    # orthonormalize via QR, then form the (basis-independent) orthogonal projector
    Q, _ = np.linalg.qr(basis.T)   # columns of Q: orthonormal basis of the subspace
    P = Q @ Q.T
    return tuple(np.round(P.flatten(), nd)), P


plane_map = {}
plane_P = {}
for M, basis in special:
    k, P = subspace_proj_key(basis)
    plane_map.setdefault(k, []).append(M)
    plane_P.setdefault(k, P)

print(f"FLOAT ITEM 4: distinct planes = {len(plane_map)}")
print(f"FLOAT ITEM 4: multiplicities = {dict(Counter(len(v) for v in plane_map.values()))}")

pw_orders = []
for k, P in plane_P.items():
    # M fixes the subspace range(P) pointwise  <=>  M @ P == P  (see derivation in report)
    cnt = sum(1 for M in group if np.allclose(M @ P, P, atol=1e-6))
    pw_orders.append(cnt)
print(f"FLOAT ITEM 4: pointwise-stab-order distribution = {dict(Counter(pw_orders))}   (claim: all 2)")

visited = set()
orbits = []
plane_keys = list(plane_P.keys())
for k in plane_keys:
    if k in visited:
        continue
    P = plane_P[k]
    orbit_keys = set()
    for M in group:
        newP = M @ P @ M.T  # M orthogonal => M^{-1} = M^T; conjugated projector
        nk = tuple(np.round(newP.flatten(), 6))
        orbit_keys.add(nk)
    visited |= orbit_keys
    orbits.append(len(orbit_keys))

print(f"FLOAT ITEM 4: orbit sizes = {sorted(orbits)}   (claim: [6,12,12])")

print()
print("FLOAT CROSSCHECK DONE")
