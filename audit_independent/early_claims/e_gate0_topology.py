"""(e) Gate 0 clauses 1, 2, 4: independent checks of the arithmetic and of 'unique connected 3-fold cover'."""
import numpy as np, itertools, json
import snappy
out = {}
LR = np.array([[2, 1], [1, 1]]); I = np.eye(2, dtype=int)
out["det(LR-I)"] = int(round(np.linalg.det(LR - I)))
LR3 = np.linalg.matrix_power(LR, 3); out["det(LR^3-I)"] = int(round(np.linalg.det(LR3 - I)))
# fixed torsion points of (LR)^3 on (Z/N)^2 for small N
for N in (2, 3, 4, 5, 8):
    fx = [(x, y) for x in range(N) for y in range(N) if (x, y) != (0, 0) and all(((LR3 @ np.array([x, y]))[i] - [x, y][i]) % N == 0 for i in range(2))]
    out[f"nonzero LR^3-fixed points mod {N}"] = len(fx)
M = snappy.Manifold("m004")
out["H1(m004)"] = str(M.homology())
covs = M.covers(3); out["n_connected_3fold_covers(all)"] = len(covs)
out["3fold cover types"] = [c.cover_info().get("type") for c in covs]
out["3fold cover homology"] = [str(c.homology()) for c in covs]
out["n_cyclic_3fold"] = len(M.covers(3, cover_type="cyclic"))
# commutants (symmetric real 3x3 H with g^T H g = H)
def comm_dim(gens):
    basis = []
    for i in range(3):
        for j in range(i, 3):
            m = np.zeros((3, 3)); m[i, j] = m[j, i] = 1; basis.append(m)
    A = np.column_stack([np.concatenate([(g.T @ b @ g - b).ravel() for g in gens]) for b in basis])
    return int(np.sum(np.linalg.svd(A)[1] < 1e-12))
C3 = np.array([[0, 1, 0], [0, 0, 1], [1, 0, 0]], float)
Pp = np.array([[1, 0, 0], [0, 0, 1], [0, 1, 0]], float)
Pr = np.array([[1, 0, 0], [0, 0, -1], [0, -1, 0]], float)
out["commutant dim <C3>"] = comm_dim([C3]); out["commutant dim <C3,P_perm>"] = comm_dim([C3, Pp]); out["commutant dim <C3,P_refl=diag(1,-1,-1)P_perm>"] = comm_dim([C3, Pr])
out["commutant dim <C3, diag(1,-1,-1)>"] = comm_dim([C3, np.diag([1., -1, -1])])
w = np.exp(2j*np.pi/3); out["|Delta(omega)|"] = abs(w - 3 + 1/w); out["|Delta(omega)|/|1-omega|"] = abs(w - 3 + 1/w)/abs(1 - w)
print(json.dumps(out, indent=1, default=str)); json.dump(out, open("e_gate0_topology.json", "w"), indent=1, default=str)
