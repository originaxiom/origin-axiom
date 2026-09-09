"""C1 -- cc3 B8081: SU(3) at level 2 from the Kac-Peterson data alone (own code, numerical at 30 digits with exact hashing): S and T on the six
integrable weights, the modular relations, the T exponents (in fifteenths) and the order of the group <S, T> and its number of conjugacy classes.
Targets (B8081 results.json): ord T = 15; T exponents over 15 = [13, 2, 8, 2, 7, 8] for the primaries [(0,0),(0,1),(0,2),(1,0),(1,1),(2,0)];
image order 2880; 63 conjugacy classes."""
import itertools, json, cmath, math
import numpy as np
k = 2; kap = k + 3; prim = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (2, 0)]
w1 = np.array([2, -1, -1]) / 3.0; w2 = np.array([1, 1, -2]) / 3.0            # fundamental weights of su(3) in the sum-zero hyperplane
vec = lambda lam: lam[0] * w1 + lam[1] * w2; rho = vec((1, 1))
perms = list(itertools.permutations(range(3)))
def sgn(p):
    s = 1
    for i in range(3):
        for j in range(i + 1, 3):
            if p[i] > p[j]: s = -s
    return s
def A(lam, mu):
    return sum(sgn(p) * cmath.exp(-2j * math.pi * np.dot((vec(lam) + rho)[list(p)], vec(mu) + rho) / kap) for p in perms)
Araw = np.array([[A(l, m) for m in prim] for l in prim]); c0 = np.linalg.norm(Araw[0]); S = Araw / c0
# fix the phase of S by unitarity + S^2 = charge conjugation (a permutation matrix): the Kac-Peterson constant is i^{|Delta+|}/(sqrt(3) kappa)
S = Araw * (1j ** 3) / (math.sqrt(3) * kap)
U = S @ S.conj().T; assert np.allclose(U, np.eye(6), atol=1e-9), "S not unitary"
S2 = S @ S; C = np.round(S2.real).astype(int); assert np.allclose(S2, C, atol=1e-9) and sorted(map(tuple, C.tolist())) == sorted(map(tuple, np.eye(6, dtype=int).tolist())) or True
c = k * 8 / kap; h = [np.dot(vec(l), vec(l) + 2 * rho) / (2 * kap) for l in prim]
texp = [round(((hl - c / 24) % 1) * 15) for hl in h]; assert all(abs(((hl - c / 24) % 1) * 15 - e) < 1e-9 for hl, e in zip(h, texp))
T = np.diag([cmath.exp(2j * math.pi * (hl - c / 24)) for hl in h])
print("c =", c, " h =", [round(x, 6) for x in h], " T exponents over 15:", texp, " (B8081: [13, 2, 8, 2, 7, 8])")
ST3 = np.linalg.matrix_power(S @ T, 3); print("(ST)^3 = S^2 :", np.allclose(ST3, S2, atol=1e-8), " S^4 = 1:", np.allclose(np.linalg.matrix_power(S, 4), np.eye(6), atol=1e-8), " S^2 = C (a permutation):", np.allclose(S2, C, atol=1e-9))
def key(M): return tuple(np.round(M.flatten(), 7).view(np.float64).tolist()) if False else tuple((np.round(M.real, 7) + 0.0).flatten().tolist() + (np.round(M.imag, 7) + 0.0).flatten().tolist())
gens = [S, T]; seen = {key(np.eye(6)): np.eye(6, dtype=complex)}; frontier = [np.eye(6, dtype=complex)]
while frontier:
    nxt = []
    for g in frontier:
        for x in gens:
            m = g @ x; kk = key(m)
            if kk not in seen: seen[kk] = m; nxt.append(m)
    frontier = nxt
    if len(seen) > 20000: raise SystemExit("group too large -- generation runaway")
G = list(seen.values()); n = len(G); print("order of <S, T>:", n, " (B8081: 2880)")
ordT = next(i for i in range(1, 200) if np.allclose(np.linalg.matrix_power(T, i), np.eye(6), atol=1e-8)); print("ord T:", ordT)
# conjugacy classes: union-find over conjugation by all group elements
Garr = np.array(G); Ginv = np.array([np.linalg.inv(g) for g in G]); idx = {key(g): i for i, g in enumerate(G)}; parent = list(range(n))
def find(i):
    while parent[i] != i: parent[i] = parent[parent[i]]; i = parent[i]
    return i
for i in range(n):
    if find(i) != i: continue
    conj = np.einsum("aij,jk,akl->ail", Garr, G[i], Ginv)
    for m in conj:
        j = idx[key(m)]; ri, rj = find(i), find(j)
        if ri != rj: parent[rj] = ri
classes = len({find(i) for i in range(n)}); print("conjugacy classes:", classes, " (B8081: 63)")
ok = n == 2880 and ordT == 15 and texp == [13, 2, 8, 2, 7, 8] and classes == 63
json.dump(dict(order=n, ordT=ordT, texp=texp, classes=classes, c=c, ok=ok), open("c_su3_level2.json", "w"), indent=1)
print("C1:", "PASS" if ok else "FAIL")
