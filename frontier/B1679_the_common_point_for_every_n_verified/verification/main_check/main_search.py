"""Main's independent check of W109 (i): numerically search SL(2,C)^n for characters fixed by every move R_ij
(a_i -> a_i a_j), by minimising the move-defect of the trace coordinates over many random starts. W109 predicts:
at n = 3 every zero of the defect has all traces 2 (trivial); at n = 2 under R_12 and L_21 the zeros are the trivial
character and the quaternion point (traces 0)."""
import numpy as np
from scipy.optimize import least_squares
rng = np.random.default_rng(109)

def mat(v):                                     # SL(2,C) from 3 complex parameters (a, b, c), d = (1 + b c)/a
    a, b, c = v[0] + 1j * v[1], v[2] + 1j * v[3], v[4] + 1j * v[5]
    return np.array([[a, b], [c, (1 + b * c) / a]])

def coords(g):                                  # traces of words of length <= 3 in distinct generators (both orders)
    n = len(g); out = [np.trace(x) for x in g]
    out += [np.trace(g[i] @ g[j]) for i in range(n) for j in range(i + 1, n)]
    out += [np.trace(g[i] @ g[j] @ g[k]) for i in range(n) for j in range(n) for k in range(n) if len({i, j, k}) == 3]
    return np.array(out)

def moved(g, i, j, side):
    h = list(g); h[i] = g[i] @ g[j] if side == "R" else g[j] @ g[i]; return h

def residual(v, n, moves):
    g = [mat(v[6 * k:6 * k + 6]) for k in range(n)]
    c = coords(g); r = []
    for (i, j, s) in moves: r.append(coords(moved(g, i, j, s)) - c)
    r = np.concatenate(r); return np.concatenate([r.real, r.imag])

def search(n, moves, starts):
    hits = []
    for _ in range(starts):
        v0 = rng.normal(size=6 * n); v0[0::6] += 1.5
        sol = least_squares(residual, v0, args=(n, moves), xtol=1e-14, ftol=1e-14, gtol=1e-14, max_nfev=4000)
        if np.linalg.norm(sol.fun) < 1e-9:
            g = [mat(sol.x[6 * k:6 * k + 6]) for k in range(n)]
            hits.append(np.round(coords(g)[: n + n * (n - 1) // 2].real, 6))
    return hits

n3 = search(3, [(i, j, "R") for i in range(3) for j in range(3) if i != j], 200)
kinds3 = {tuple(h) for h in n3}
print(f"n = 3, the six R_ij: {len(n3)} zeros of the defect from 200 starts; distinct trace vectors: {sorted(kinds3)}")
n2 = search(2, [(0, 1, "R"), (1, 0, "L")], 200)
kinds2 = {tuple(h) for h in n2}
print(f"n = 2, the record's R and L: {len(n2)} zeros from 200 starts; distinct (x, y, z): {sorted(kinds2)}")
