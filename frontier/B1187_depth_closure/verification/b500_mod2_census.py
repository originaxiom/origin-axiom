#!/usr/bin/env python3
"""B1187 / B500-wrap: the mod-2 etale-signature census.

The child x^4-x-1 (d_K=-283, odd) has 2 INERT (x^4+x+1 irreducible over GF(2)):
if the child field ever appears as an isolated fixed-point field of a word w with
2 not dividing the coordinate-order index, the fixed scheme of w mod 2 must carry
an ETALE closed point of residue degree 4 -- i.e. a Frobenius orbit of size 4 of
etale fixed points over GF(16).

The hunt's prereg confines the space to ALL-THREE-VERB words (F, M, D all present).
This census iterates every such word at each depth, enumerates its fixed points
over GF(16) (all 4096 points, vectorized), tests etaleness det(J_w - I) != 0, and
looks for size-4 Frobenius orbits. Verbs (trace coordinates, from B500 hunt.py):
    F(x,y,z) = (z, x, x*z - y)
    M(x,y,z) = (z, z, x*y*z - x^2 - y^2 + 2)
    D(x,y,z) = (x^2-2, y^2-2, x*y*z - x^2 - y^2 + 2)
Mod 2: -1 == 1, 2 == 0.

FENCE: absence of the signature at depth d excludes the child at depth d only up
to the index caveat (2 | [O_K : O_xi] could hide an inert 2 behind a non-maximal
coordinate order). Presence of the signature is NOT a hit -- only a non-exclusion.
"""
import json, sys, time
import numpy as np

# ---- GF(16) as polynomial basis over GF(2), g^4 = g + 1 (x^4+x+1 primitive) ----
Q = 16
EXP = np.zeros(2 * Q, dtype=np.int64)   # EXP[i] = g^i as int (bits = coeffs)
LOG = np.zeros(Q, dtype=np.int64)
v = 1
for i in range(Q - 1):
    EXP[i] = v
    LOG[v] = i
    v <<= 1
    if v & 16:
        v ^= 0b10011          # reduce by x^4 + x + 1
for i in range(Q - 1, 2 * Q):
    EXP[i] = EXP[i - (Q - 1)]

MUL = np.zeros((Q, Q), dtype=np.int64)
for a in range(1, Q):
    for b in range(1, Q):
        MUL[a, b] = EXP[LOG[a] + LOG[b]]

def gmul(a, b):
    return MUL[a, b]

def gadd(a, b):
    return a ^ b

# Frobenius x -> x^2 on GF(16)
FROB = np.array([gmul(a, a) for a in range(Q)], dtype=np.int64)

# ---- the verbs mod 2 on GF(16)^3, vectorized over point arrays ----
def F(x, y, z):
    return z, x, gadd(gmul(x, z), y)

def M(x, y, z):
    xyz = gmul(gmul(x, y), z)
    return z, z, gadd(gadd(xyz, gmul(x, x)), gmul(y, y))

def D(x, y, z):
    xyz = gmul(gmul(x, y), z)
    return gmul(x, x), gmul(y, y), gadd(gadd(xyz, gmul(x, x)), gmul(y, y))

VERBS = {"F": F, "M": M, "D": D}

# Jacobians mod 2 (entries as functions of the CURRENT point, before the step):
#  F: [[0,0,1],[1,0,0],[z,1,x]]           (chars: -1 == 1)
#  M: [[0,0,1],[0,0,1],[yz, xz, xy]]      (d/dx(xyz+x^2+y^2) = yz+2x == yz)
#  D: [[0,0,0],[0,0,0],[yz, xz, xy]]      (d/dx(x^2-2) = 2x == 0)
def JF(x, y, z, one, zero):
    return [[zero, zero, one], [one, zero, zero], [z, one, x]]

def JM(x, y, z, one, zero):
    yz, xz, xy = gmul(y, z), gmul(x, z), gmul(x, y)
    return [[zero, zero, one], [zero, zero, one], [yz, xz, xy]]

def JD(x, y, z, one, zero):
    yz, xz, xy = gmul(y, z), gmul(x, z), gmul(x, y)
    return [[zero, zero, zero], [zero, zero, zero], [yz, xz, xy]]

JACS = {"F": JF, "M": JM, "D": JD}

def matmul3(A, B):
    return [[gadd(gadd(gmul(A[i][0], B[0][j]), gmul(A[i][1], B[1][j])),
                  gmul(A[i][2], B[2][j])) for j in range(3)] for i in range(3)]

def det3(A):
    t1 = gmul(A[0][0], gadd(gmul(A[1][1], A[2][2]), gmul(A[1][2], A[2][1])))
    t2 = gmul(A[0][1], gadd(gmul(A[1][0], A[2][2]), gmul(A[1][2], A[2][0])))
    t3 = gmul(A[0][2], gadd(gmul(A[1][0], A[2][1]), gmul(A[1][1], A[2][0])))
    return gadd(gadd(t1, t2), t3)

def all_words(depth):
    """All-three-verb words of the given depth."""
    from itertools import product
    for w in product("FMD", repeat=depth):
        if "F" in w and "M" in w and "D" in w:
            yield "".join(w)

def census_depth(depth):
    pts = np.arange(Q, dtype=np.int64)
    X0, Y0, Z0 = np.meshgrid(pts, pts, pts, indexing="ij")
    X0, Y0, Z0 = X0.ravel(), Y0.ravel(), Z0.ravel()
    one = np.ones_like(X0)
    zero = np.zeros_like(X0)
    n_words = 0
    sig_words = []          # words with an etale degree-4 closed point
    orbit_hist = {1: 0, 2: 0, 4: 0}
    t0 = time.time()
    for w in all_words(depth):
        n_words += 1
        x, y, z = X0, Y0, Z0
        J = [[one, zero, zero], [zero, one, zero], [zero, zero, one]]
        for ch in w:
            Jstep = JACS[ch](x, y, z, one, zero)
            J = matmul3(Jstep, J)
            x, y, z = VERBS[ch](x, y, z)
        fixed = (x == X0) & (y == Y0) & (z == Z0)
        JmI = [[gadd(J[i][j], one if i == j else zero) for j in range(3)] for i in range(3)]
        etale = fixed & (det3(JmI) != 0)
        idx = np.nonzero(etale)[0]
        if len(idx) == 0:
            continue
        # Frobenius orbits among etale fixed points
        pts_set = {(int(X0[i]), int(Y0[i]), int(Z0[i])) for i in idx}
        seen = set()
        found4 = False
        for p in pts_set:
            if p in seen:
                continue
            orb = []
            q = p
            while q not in orb:
                orb.append(q)
                q = (int(FROB[q[0]]), int(FROB[q[1]]), int(FROB[q[2]]))
                if q not in pts_set:
                    orb = None
                    break
            if orb is None:
                seen.add(p)
                continue
            seen.update(orb)
            L = len(orb)
            if L in orbit_hist:
                orbit_hist[L] += 1
            if L == 4:
                found4 = True
        if found4:
            sig_words.append(w)
    return {"depth": depth, "words": n_words, "signature_words": sig_words,
            "etale_orbit_histogram": orbit_hist, "seconds": round(time.time() - t0, 1)}

def main():
    out = {"target": "x^4-x-1, d_K=-283, 2 INERT (x^4+x+1 irred/GF(2)) => needs an "
                     "etale degree-4 closed point mod 2 (up to the index caveat)",
           "depths": []}
    for depth in range(4, 11):
        r = census_depth(depth)
        print(f"depth {r['depth']}: {r['words']} all-three-verb words; "
              f"etale orbit histogram {r['etale_orbit_histogram']}; "
              f"degree-4-signature words: {len(r['signature_words'])}  ({r['seconds']}s)",
              flush=True)
        out["depths"].append(r)
    with open(sys.argv[1] if len(sys.argv) > 1 else "b500_mod2_census.json", "w") as f:
        json.dump(out, f, indent=1)
    print("DONE", flush=True)

if __name__ == "__main__":
    main()
