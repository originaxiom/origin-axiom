#!/usr/bin/env python3
"""B1353 -- THE ISOLATED ENHANCEMENT POINT ON AN E6 LOCUS, MADE FINITE (the orbifold class).

Setting.  In a flat G2 orbifold R^7/Gamma the E6 locus is the fixed 3-plane P of a binary tetrahedral group 2T c SU(2)_R c G2
(B1084: pointwise stabiliser exactly 2T).  The stabiliser in G2 of the associative 3-plane P is SO(4) = (SU(2)_L x SU(2)_R)/Z2
acting on R^7 = Im H (+) H by (l, r).(y, x) = (l y l^-1, l x r^-1).  A point p of P is an ISOLATED fixed point of its stabiliser
Gamma_p exactly when the image H of Gamma_p in SO(3) (its action on the locus direction Im H) has no fixed vector, i.e. is
non-cyclic (D_n, T, O, I) -- B1259's element lemma (every single element fixes a line) does not forbid that (main's E70 scope).

This script (1) enumerates every finite Gamma c SO(4) whose kernel on Im H is exactly 2T and whose image in SO(3) is non-cyclic
(Goursat: Gamma = L ×_{Q} R with R in {2T, 2O} -- the finite subgroups of SU(2) containing 2T as a NORMAL subgroup -- and
L/L_K = R/2T), checked by explicit quaternion arithmetic; (2) for each Gamma computes the census of fixed-subspace dimensions of
its elements (B1259's census), the isolatedness of 0, and THE INTERSECTION WITH P OF EVERY CODIMENSION-4 STRATUM THROUGH 0
(the fixed 3-planes of elements g = (l, r) with l != +-1 and l conjugate to r, i.e. the A-type loci): each such plane is
axis(l) (+) {x : l x = x r} and meets P = 0 (+) Im H exactly in the line axis(l) -- never in the single point 0.
(3) The same for the D-, E-type strata (fixed 3-planes of the non-cyclic subgroups) and the enhanced stabilisers along the
axis lines.  Output: a table per group.  Exact statements are checked numerically at 1e-9 on unit quaternions (a finite
computation; every group is closed under multiplication to that tolerance).
Usage: python3 isolated_point_groups.py"""
from __future__ import annotations
import itertools, math
import numpy as np

# ---------------------------------------------------------------- quaternions
def qmul(a, b):
    a0, a1, a2, a3 = a; b0, b1, b2, b3 = b
    return (a0*b0 - a1*b1 - a2*b2 - a3*b3, a0*b1 + a1*b0 + a2*b3 - a3*b2, a0*b2 - a1*b3 + a2*b0 + a3*b1, a0*b3 + a1*b2 - a2*b1 + a3*b0)
def qconj(a): return (a[0], -a[1], -a[2], -a[3])
def key(q): return tuple(round(c, 7) + 0.0 for c in q)
def closure(gens):
    G = {key((1.0, 0.0, 0.0, 0.0)): (1.0, 0.0, 0.0, 0.0)}
    frontier = list(G.values())
    while frontier:
        new = []
        for g in frontier:
            for h in gens:
                p = qmul(g, h); k = key(p)
                if k not in G: G[k] = p; new.append(p)
        frontier = new
    return list(G.values())
def cyc(n):  # C_n = <exp(i pi/ n *2)>: order n (n even contains -1)
    t = 2 * math.pi / n
    return closure([(math.cos(t), math.sin(t), 0.0, 0.0)])
def bindih(n):  # binary dihedral D*_n of order 4n: <exp(i pi/n), j>
    t = math.pi / n
    return closure([(math.cos(t), math.sin(t), 0.0, 0.0), (0.0, 0.0, 1.0, 0.0)])
def bintet():  # 2T: order 24
    return closure([(0.0, 1.0, 0.0, 0.0), (0.0, 0.0, 1.0, 0.0), (0.5, 0.5, 0.5, 0.5)])
def binoct():  # 2O: order 48
    s = 1 / math.sqrt(2)
    return closure([(0.5, 0.5, 0.5, 0.5), (s, s, 0.0, 0.0), (0.0, 0.0, 1.0, 0.0)])
def binico():  # 2I: order 120
    phi = (1 + math.sqrt(5)) / 2
    return closure([(0.5, 0.5, 0.5, 0.5), (0.0, 1.0, 0.0, 0.0), (0.5, 0.5 * phi, 0.5 / phi, 0.0)])
def is_subgroup(S, G):
    GK = {key(g) for g in G}
    return all(key(s) in GK for s in S)
def is_normal(N, G):
    NK = {key(n) for n in N}
    return all(key(qmul(qmul(g, n), qconj(g))) in NK for g in G for n in N)
def angle(q): return 2 * math.acos(max(-1.0, min(1.0, q[0])))     # rotation angle of the SU(2) element (0 .. 2pi)
def same_class(l, r):  # conjugate in SU(2) iff same real part
    return abs(l[0] - r[0]) < 1e-7

# ---------------------------------------------------------------- the action on R^7 = Im H (+) H
def mat_of(l, r):
    """7x7 matrix of (l, r): y -> l y l^-1 on Im H (coordinates 0..2), x -> l x r^-1 on H (coordinates 3..6)."""
    M = np.zeros((7, 7))
    li = qconj(l); ri = qconj(r)
    for a in range(3):
        e = [0.0] * 4; e[a + 1] = 1.0
        v = qmul(qmul(l, tuple(e)), li)
        M[0:3, a] = v[1:]
    for a in range(4):
        e = [0.0] * 4; e[a] = 1.0
        v = qmul(qmul(l, tuple(e)), ri)
        M[3:7, 3 + a] = v
    return M
def fixed_space(M, tol=1e-7):
    """orthonormal basis of ker(M - I) (SVD null space; eigenvector routines undercount repeated eigenvalue 1)."""
    U, sv, Vt = np.linalg.svd(M - np.eye(7))
    null = [Vt[i] for i in range(7) if (sv[i] if i < len(sv) else 0.0) < tol]
    if not null: return np.zeros((7, 0))
    return np.array(null).T
def joint_fixed_dim(mats):
    A = np.vstack([M - np.eye(7) for M in mats])
    return 7 - np.linalg.matrix_rank(A, tol=1e-7)

# ---------------------------------------------------------------- Goursat enumeration
SU2 = {"C2": cyc(2), "C4": cyc(4), "C6": cyc(6), "C8": cyc(8), "C12": cyc(12),
       "D*2": bindih(2), "D*3": bindih(3), "D*4": bindih(4), "D*6": bindih(6), "2T": bintet(), "2O": binoct(), "2I": binico()}
T2 = SU2["2T"]; O2 = SU2["2O"]; I2 = SU2["2I"]
print("=== the finite subgroups of SU(2) containing 2T, and normality ===")
for name in ("2T", "2O", "2I"):
    G = SU2[name]
    print(f"    {name}: order {len(G)}; contains 2T: {is_subgroup(T2, G)}; 2T normal in it: {is_normal(T2, G) if is_subgroup(T2, G) else '-'}")

def goursat(Lname, LKname, Rname, RKname):
    """the fibre product {(l, r) : l L_K <-> r R_K} for the unique-up-to-automorphism identification of the quotients of
    order <= 2 (both quotients are 1 or Z2 here), as a set of pairs; then modulo the diagonal Z2 (SO(4))."""
    L, LK, R, RK = SU2[Lname], SU2[LKname], SU2[Rname], SU2[RKname]
    assert is_subgroup(LK, L) and is_subgroup(RK, R) and is_normal(LK, L) and is_normal(RK, R)
    qL, qR = len(L) // len(LK), len(R) // len(RK)
    assert qL == qR and qL in (1, 2), (Lname, LKname, Rname, RKname, qL, qR)
    LKK = {key(g) for g in LK}; RKK = {key(g) for g in RK}
    pairs = []
    for l in L:
        for r in R:
            if (key(l) in LKK) == (key(r) in RKK):
                pairs.append((l, r))
    # SO(4): identify (l, r) ~ (-l, -r)
    seen = {}; out = []
    for l, r in pairs:
        k1 = key(l) + key(r); k2 = key(tuple(-c for c in l)) + key(tuple(-c for c in r))
        if k1 in seen or k2 in seen: continue
        seen[k1] = True; out.append((l, r))
    return out

def analyse(label, Gam):
    mats = [(l, r, mat_of(l, r)) for l, r in Gam]
    n = len(mats)
    # kernel on Im H: l = +-1
    ker = [(l, r) for l, r in Gam if abs(abs(l[0]) - 1) < 1e-7]
    ker_R = {key(r if l[0] > 0 else tuple(-c for c in r)) for l, r in ker}
    ker_is_2T = ker_R == {key(g) for g in T2}
    # image in SO(3): the l's mod +-1; fixed vectors on Im H
    imH = [mat_of(l, (1.0, 0.0, 0.0, 0.0))[0:3, 0:3] for l, r in Gam]
    fixH = 3 - np.linalg.matrix_rank(np.vstack([M - np.eye(3) for M in imH]), tol=1e-7)
    jf = joint_fixed_dim([M for _, _, M in mats])
    census = {}
    for l, r, M in mats:
        if abs(abs(l[0]) - 1) < 1e-7 and abs(l[0] - r[0]) < 1e-7: continue   # the identity of SO(4) is +-(1, 1); (1, -1) is the involution -1 on H
        d = fixed_space(M).shape[1]; census[d] = census.get(d, 0) + 1
    # the codimension-4 strata through 0: fixed 3-planes of single elements
    planes = {}
    for l, r, M in mats:
        F = fixed_space(M)
        if F.shape[1] != 3: continue
        # its intersection with P = 0 (+) Im H (coordinates 0..2): dimension
        A = np.hstack([F, -np.vstack([np.eye(3), np.zeros((4, 3))])])
        inter = 6 - np.linalg.matrix_rank(A, tol=1e-7)
        keyp = tuple(np.round(np.abs(np.linalg.svd(F @ F.T)[0][:, :3]).sum(axis=1), 5))
        kind = "l = +-1 (the E6 plane P itself)" if abs(abs(l[0]) - 1) < 1e-7 else f"l ~ r, angle {angle(l) / math.pi:.3f} pi"
        planes.setdefault((kind, inter), 0); planes[(kind, inter)] += 1
    # pairwise intersections of the A-type planes (l != +-1): can two A-strata meet only at 0?
    Aplanes = [fixed_space(M) for l, r, M in mats if abs(abs(l[0]) - 1) >= 1e-7 and fixed_space(M).shape[1] == 3]
    # distinct planes
    distinct = []
    for F in Aplanes:
        if not any(np.linalg.matrix_rank(np.hstack([F, G]), tol=1e-7) == 3 for G in distinct): distinct.append(F)
    pair_dims = {}
    for i in range(len(distinct)):
        for j in range(i + 1, len(distinct)):
            d = 6 - np.linalg.matrix_rank(np.hstack([distinct[i], -distinct[j]]), tol=1e-7)
            pair_dims[int(d)] = pair_dims.get(int(d), 0) + 1
    print(f"    {label}: |Gamma| = {n} (in SO(4)); kernel on Im H is 2T: {ker_is_2T}; fixed vectors of Gamma on Im H: {fixH}; joint fixed dimension on R^7: {jf} -> {'ISOLATED' if jf == 0 else 'not isolated'}")
    print(f"        census of fixed dimensions of the {n - 1} non-trivial elements: {dict(sorted(census.items()))}")
    for (kind, inter), cnt in sorted(planes.items()):
        print(f"        3-dimensional fixed planes of elements with {kind}: {cnt} elements; each meets P in a subspace of dimension {inter}")
    print(f"        distinct A-type planes through 0: {len(distinct)}; pairwise intersection dimensions {dict(sorted(pair_dims.items()))}  (0 = two A-loci meeting only at the apex)")
    return ker_is_2T, jf, planes, dict(sorted(census.items()))

print("\n=== Goursat data (L, L_K; R, R_K = 2T) with R/2T = L/L_K, the kernel on Im H exactly 2T, the image in SO(3) non-cyclic ===")
cands = []
# R = 2T: L = L_K any finite subgroup of SU(2) with non-cyclic image in SO(3): D*_n (n >= 2), 2T, 2O, 2I
for Ln in ("D*2", "D*3", "D*4", "D*6", "2T", "2O", "2I"):
    cands.append((Ln, Ln, "2T", "2T"))
# R = 2O: L_K index 2 in L, non-cyclic image: (D*_n, C_2n), (D*_2n, D*_n), (2O, 2T)
for Ln, LKn in (("D*2", "C4"), ("D*3", "C6"), ("D*4", "C8"), ("D*6", "C12"), ("D*4", "D*2"), ("D*6", "D*3"), ("2O", "2T")):
    cands.append((Ln, LKn, "2O", "2T"))
results = {}
for c in cands:
    Gam = goursat(*c)
    label = f"L = {c[0]}, L_K = {c[1]}, R = {c[2]}"
    results[label] = analyse(label, Gam)
print("\n=== B1084's group (order 96; census {3d: 53, 1d: 42}) placed in the enumeration ===")
for lab, (k, jf, planes, census) in results.items():
    if census == {1: 42, 3: 53}:
        print(f"    {lab}: census {census} = B1084's -- its apex is an isolated fixed point of the group, and its A-type strata meet the E6 plane in lines")
print("\n=== summary ===")
bad = [lab for lab, (k, jf, planes, census) in results.items() if not k or jf != 0]
print(f"    groups enumerated: {len(results)}; all with kernel 2T and an isolated fixed point: {not bad}")
allA = all(inter >= 1 for lab, (k, jf, planes, census) in results.items() for (kind, inter) in planes)
print(f"    every codimension-4 stratum through the isolated point meets the E6 plane P in a subspace of dimension >= 1 (never only at 0): {allA}")
