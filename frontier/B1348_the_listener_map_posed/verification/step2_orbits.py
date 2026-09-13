"""B1348 step 2 -- the odd plane, its group, and the candidate directions.

THE EXISTENCE QUESTION (spec 1.2): is there a rule in DOMAIN DATA ALONE that excludes at least one
candidate unit direction in CP^1_odd? Two admissible outcomes: a POSITIVE CONSTRUCTION (u fixed, up
to phase, by a NAMED stabilizer), or a STRUCTURAL NO (the candidate symmetry group acts with NO
field-fixed point -- B1040's "Galois simply-transitive" shape).
"""
import numpy as np, itertools
np.set_printoptions(precision=6, suppress=True)
S = np.load("/tmp/b1348_S.npy"); T = np.load("/tmp/b1348_T.npy")
n = 6
W = [(0,0),(0,1),(0,2),(1,0),(1,1),(2,0)]
C = S @ S
R = T; L = np.linalg.inv(S) @ np.linalg.inv(T) @ S

# ---- the theta-grading: C is central, so its eigenspaces are G-invariant -----------------
print("C central in <R,L>?  [C,R]=0:", np.allclose(C@R - R@C, 0, atol=1e-9),
      "  [C,L]=0:", np.allclose(C@L - L@C, 0, atol=1e-9))
ev, V = np.linalg.eig(C)
odd = V[:, np.abs(ev + 1) < 1e-8]; even = V[:, np.abs(ev - 1) < 1e-8]
print(f"C eigenvalues: {sorted(np.round(ev.real,6))}  ->  dim odd = {odd.shape[1]}, dim even = {even.shape[1]}")
# orthonormalise the odd plane
Q, _ = np.linalg.qr(odd)
def restrict(M): return Q.conj().T @ M @ Q
Ro, Lo = restrict(R), restrict(L)
print("  restriction is well defined (odd is invariant):",
      np.allclose(Q @ (Q.conj().T @ R @ Q) - R @ Q, 0, atol=1e-8),
      np.allclose(Q @ (Q.conj().T @ L @ Q) - L @ Q, 0, atol=1e-8))

# ---- the group on the odd plane, modulo scalars (we care about CP^1) --------------------
def pkey(M, q=7):
    M = M / np.exp(1j*np.angle(M[np.unravel_index(np.argmax(np.abs(M)), M.shape)]))
    return tuple(np.round(M.flatten(), q).tolist())
seen, frontier = {pkey(np.eye(2))}, [np.eye(2, dtype=complex)]
mats = [np.eye(2, dtype=complex)]
gens = [Ro, Lo, np.linalg.inv(Ro), np.linalg.inv(Lo)]
while frontier and len(seen) < 5000:
    nxt = []
    for M in frontier:
        for g in gens:
            P = M @ g; k = pkey(P)
            if k not in seen:
                seen.add(k); nxt.append(P); mats.append(P)
    frontier = nxt
print(f"\n  image of <R,L> in PGL(2) on the odd plane: {len(seen)} elements")
print(f"  |A_5| = 60, |2I| = 120 -> the PROJECTIVE icosahedral group is A_5 = 60: {len(seen)==60}")

# ---- irreducibility: is any line invariant under the whole group? -----------------------
inv_lines = 0
for M in mats[:1]: pass
# a common eigenvector of all generators would be a G-invariant line
evR, VR = np.linalg.eig(Ro)
common = []
for i in range(2):
    v = VR[:, i]
    if np.allclose(np.abs(np.vdot(v, Lo @ v)) , np.linalg.norm(Lo @ v), atol=1e-7):
        common.append(v)
print(f"  common eigenvectors of R and L on the odd plane: {len(common)}")
print(f"  => C^2_odd irreducible under <R,L>: {len(common)==0}")

# ---- the exceptional orbits: points of CP^1 with non-trivial stabiliser -----------------
def fixed_points(M):
    ev, V = np.linalg.eig(M)
    if abs(ev[0]-ev[1]) < 1e-9: return []           # scalar: fixes everything
    return [V[:, 0], V[:, 1]]
pts = []
for M in mats:
    if np.allclose(M - np.trace(M)/2*np.eye(2), 0, atol=1e-8): continue
    pts.extend(fixed_points(M))
def cpkey(v, q=6):
    v = v / v[np.argmax(np.abs(v))]
    return tuple(np.round(v, q).tolist())
uniq = {}
for v in pts: uniq.setdefault(cpkey(v), v)
print(f"\n  distinct fixed points on CP^1_odd: {len(uniq)}")
# orbit decomposition under the projective group
verts = list(uniq.values())
orbits = []
used = set()
for v in verts:
    if cpkey(v) in used: continue
    orb = set()
    for M in mats:
        w = M @ v; orb.add(cpkey(w))
    orbits.append(orb); used |= orb
sizes = sorted(len(o) for o in orbits)
print(f"  orbit sizes: {sizes}")
print(f"  the icosahedral exceptional orbits are 12 (vertices), 20 (faces), 30 (edges): {sizes==[12,20,30]}")
