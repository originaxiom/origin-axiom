"""B1986, POST HOC (labelled; written after listen4_run.txt was read): (a) the cube group's irreducible content of the
permutation module on each orbit over the common point (mod 9, 25, 49), by characters, so the persisting sign mode's
support is read exactly instead of from tied eigenvalues; (b) the gap of W+- below its top eigenvalue 4 (4 minus the
largest real eigenvalue below 4) on the cusp's leaf's big orbit mod p = 5, 7, 11, 13, 17, 19.
    python3 -B irreps_posthoc.py > irreps_posthoc_run.txt"""
import numpy as np
from itertools import product
dL = np.array([[1, 0, 0], [0, 0, 1], [0, -1, 0]]); dR = np.array([[0, 0, 1], [0, 1, 0], [-1, 0, 0]])
G = {tuple(np.eye(3, dtype=int).ravel()): np.eye(3, dtype=int)}; fr = [np.eye(3, dtype=int)]
while fr:
    A = fr.pop()
    for B in (dL, dR):
        C = B @ A
        if tuple(C.ravel()) not in G: G[tuple(C.ravel())] = C; fr.append(C)
G = list(G.values()); assert len(G) == 24
diag = [np.array(d) for d in ((1, 1, 1), (1, 1, -1), (1, -1, 1), (-1, 1, 1))]
def dperm(M): return [next(i for i, e in enumerate(diag) if (M @ d == e).all() or (M @ d == -e).all()) for d in diag]
def psign(p):
    s, p = 1, list(p)
    for i in range(len(p)):
        while p[i] != i: j = p[i]; p[i], p[j] = p[j], p[i]; s = -s
    return s
def apos(M): return [int(np.nonzero(M[:, i])[0][0]) for i in range(3)]
def chi2(M):
    q = apos(M); fixed = sum(1 for i in range(3) if q[i] == i); return fixed - 1
CH = {"1": lambda M: 1, "sign": lambda M: psign(dperm(M)), "2": chi2, "3": lambda M: int(np.trace(M)), "3'": lambda M: psign(dperm(M)) * int(np.trace(M))}
assert all(abs(sum(CH[a](g) * CH[a](g) for g in G) - 24) < 1e-9 for a in CH)
for N, p in ((9, 3), (25, 5), (49, 7)):
    pts = [v for v in product(range(0, N, p), repeat=3) if (v[0] ** 2 + v[1] ** 2 + v[2] ** 2 - v[0] * v[1] * v[2]) % N == 0]
    u = {v: tuple((c // p) % p for c in v) for v in pts}
    act = lambda M, w: tuple(int(x) % p for x in M @ np.array(w))
    seen, rows = set(), []
    for v in pts:
        if v in seen: continue
        orb = {u[v]}; st = [u[v]]
        while st:
            w = st.pop()
            for M in (dL, dR):
                x = act(M, w)
                if x not in orb: orb.add(x); st.append(x)
        seen |= {q for q in pts if u[q] in orb}
        perm_char = lambda M: sum(1 for w in orb if act(M, w) == w)
        mult = {a: round(sum(CH[a](g) * perm_char(g) for g in G) / 24) for a in CH}
        rows.append((len(orb), mult))
    print("mod %d: orbit sizes and irreducible content: %s" % (N, sorted((n, tuple((a, m) for a, m in mm.items() if m)) for n, mm in rows)))
def leafbig(p):
    L = lambda v: (v[0], v[2], (v[0] * v[2] - v[1]) % p); R = lambda v: (v[2], v[1], (v[1] * v[2] - v[0]) % p)
    pts = [v for v in product(range(p), repeat=3) if (v[0] ** 2 + v[1] ** 2 + v[2] ** 2 - v[0] * v[1] * v[2]) % p == 0 and v != (0, 0, 0)]
    idx = {v: i for i, v in enumerate(pts)}; n = len(pts)
    PL = np.zeros((n, n)); PR = np.zeros((n, n))
    for v in pts: PL[idx[L(v)], idx[v]] = 1; PR[idx[R(v)], idx[v]] = 1
    ev = np.sort(np.linalg.eigvalsh(PL + PL.T + PR + PR.T))
    return n, ev[-1], ev[-2], ev[0]
for p in (5, 7, 11, 13, 17, 19):
    n, top, second, bottom = leafbig(p)
    print("mod %d: the cusp's leaf without the common point (%d points): W+- top %.4f, next %.4f, gap below the top %.4f; lowest %.4f" % (p, n, top, second, top - second, bottom))
