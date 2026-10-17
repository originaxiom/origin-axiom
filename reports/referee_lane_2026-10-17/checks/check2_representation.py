"""Check 2: reconstruct rho = chi_eta^21 (x) rho_u in the theta basis (theta2^2, theta3^2, theta4^2)
and test the claims of Theorem 9, Remark 10, Theorem 27(1), Theorem 28(2).
Convention: f(g tau) = rho(g) (c tau + d)^k f(tau), s: tau -> -1/tau, t: tau -> tau+1."""
import numpy as np, itertools, cmath
from numpy.linalg import eigvals, eig, matrix_rank, norm

I3 = np.eye(3, dtype=complex)
P24 = np.array([[0,0,1],[0,1,0],[1,0,0]], dtype=complex)   # swaps theta2^2 <-> theta4^2
P34 = np.array([[1,0,0],[0,0,1],[0,1,0]], dtype=complex)   # swaps theta3^2 <-> theta4^2
rho_u_t = np.diag([1j, 1, 1]) @ P34        # theta2^2 -> i theta2^2, theta3^2 <-> theta4^2
rho_u_s = -1j * P24                        # theta_j^2(-1/tau) = (-i tau) * (swapped theta)^2
chi_t = cmath.exp(2j*np.pi/24)             # eta(tau+1) = e^{2 pi i/24} eta(tau)
chi_s = cmath.exp(-1j*np.pi/4)             # eta(-1/tau) = sqrt(-i tau) eta(tau) = e^{-i pi/4} sqrt(tau) eta
k = 21
rho_t = chi_t**k * rho_u_t
rho_s = chi_s**k * rho_u_s
print("rho(s) =\n", np.round(rho_s, 6)); print("rho(t) =\n", np.round(rho_t, 6))

def key(M): return tuple(np.round(M, 8).round(8).flatten().view(float))
def close(M, N): return norm(M - N) < 1e-9

def generate(gens):
    elems = {key(I3): I3}; frontier = [I3]
    while frontier:
        new = []
        for g in frontier:
            for h in gens:
                p = g @ h
                kk = key(p)
                if kk not in elems:
                    elems[kk] = p; new.append(p)
        frontier = new
    return list(elems.values())

G = generate([rho_s, rho_t])
Gu = generate([rho_u_s, rho_u_t])
print("\n|<rho(s),rho(t)>| =", len(G), "   |<rho_u(s),rho_u(t)>| =", len(Gu))

# Mp2(Z) relations
st = rho_s @ rho_t
print("s^2 = (st)^3 :", close(rho_s @ rho_s, st @ st @ st), "  s^8 = 1 :", close(np.linalg.matrix_power(rho_s, 8), I3),
      "  s^4 = -1 :", close(np.linalg.matrix_power(rho_s, 4), -I3), "  s^2 = i*1 :", close(rho_s @ rho_s, 1j*I3))
ev_t = eigvals(rho_t)
print("exponents of t (turns):", sorted(np.round((np.angle(ev_t)/(2*np.pi)) % 1, 6)))
# Delta = (st)^... braid group: sigma1 = t, sigma2 = ? ; the center of B3 is <Delta^2>, Delta^2 -> s^2 (since s = sigma1 sigma2 sigma1 maps to S).
# Here Delta^4 -> s^4: check it acts as -1 on T
print("Delta^4 -> s^4 acts as -1:", close(np.linalg.matrix_power(rho_s, 4), -I3))

# central element and allowed weights: rho(s^2) = i^{-2k} => -2k = 1 mod 4 => k = 3/2 mod 2
val = (rho_s @ rho_s)[0,0]
print("rho(s^2) scalar =", np.round(val, 6), " => allowed weights k with i^(-2k) =", np.round(val,6), ": k = 3/2 mod 2; dual rep would need k = 1/2 mod 2")

# irreducibility: commutant dimension
def commutant_dim(group):
    # solve X g = g X for all g; vectorize
    rows = []
    for g in group:
        rows.append(np.kron(I3, g) - np.kron(g.T, I3))
    Acm = np.vstack(rows)
    sv = np.linalg.svd(Acm, compute_uv=False)
    return int(np.sum(sv < 1e-8))
print("commutant dimension (1 = irreducible):", commutant_dim(G))
chars = np.array([np.trace(g) for g in G])
print("<chi,chi> =", np.round(np.mean(np.abs(chars)**2), 6), "  <chi,chibar> =", np.round(abs(np.mean(chars**2)), 6), " (0 = not self-conjugate)")

# residual symmetries at i (stabilizer <s>) and omega (stabilizer <st>)
def ordr(M):
    P = I3.copy()
    for n in range(1, 200):
        P = P @ M
        if close(P, I3): return n
    return None
print("\norder of rho(s) =", ordr(rho_s), " order of rho(st) =", ordr(st))
w, V = eig(rho_s)
print("rho(s) eigenvalues (turns):", np.round((np.angle(w)/(2*np.pi)) % 1, 4))
for j in range(3): print("   eigvec", np.round(V[:, j], 3))
w, V = eig(st)
print("rho(st) eigenvalues (turns):", np.round((np.angle(w)/(2*np.pi)) % 1, 4))
for j in range(3): print("   eigvec |components|^2 =", np.round(np.abs(V[:, j])**2, 4))

# the tick LR: rho(R) = rho(s) rho(t)^-1 rho(s)^-1  (R = S0 L^-1 S0^-1), rho(L) = rho(t)
rho_L = rho_t; rho_R = rho_s @ np.linalg.inv(rho_t) @ np.linalg.inv(rho_s)
rho_LR = rho_L @ rho_R
w = eigvals(rho_LR)
print("\nrho(LR) eigenvalues (turns):", np.round((np.angle(w)/(2*np.pi)) % 1, 4), " det =", np.round(np.linalg.det(rho_LR), 6))
mean = (I3 + rho_LR + rho_LR @ rho_LR)/3
print("operator mean of LR: rank", matrix_rank(mean, tol=1e-9), "; |entries| =", np.round(np.abs(mean), 4).tolist())
print("rho(LR) is monomial with a 3-cycle:", np.round(np.abs(rho_LR), 3).tolist())

# also check the generic stabilizer: the centre of the image
Z = [g for g in G if all(close(g @ h, h @ g) for h in G)]
print("centre of the image has order", len(Z), " scalars:", [np.round(g[0,0], 4) for g in Z if close(g, g[0,0]*I3)])

# ---------------- subgroup lattice ----------------
idx = {key(g): i for i, g in enumerate(G)}
n = len(G)
mult = np.zeros((n, n), dtype=int)
for i, g in enumerate(G):
    for j, h in enumerate(G):
        mult[i, j] = idx[key(g @ h)]
e = idx[key(I3)]
inv = [int(np.where(mult[i] == e)[0][0]) for i in range(n)]

def closure(S):
    S = set(S) | {e}
    frontier = list(S)
    while frontier:
        new = []
        for a in frontier:
            for b in list(S):
                for c in (mult[a, b], mult[b, a]):
                    if c not in S:
                        S.add(c); new.append(c)
        frontier = new
    return frozenset(S)

cyc = {closure([i]) for i in range(n)}
subs = set(cyc)
frontier = set(cyc)
while frontier:
    new = set()
    for H in frontier:
        for C in cyc:
            if not C <= H:
                J = closure(H | C)
                if J not in subs:
                    new.add(J)
    subs |= new
    frontier = new
subs = list(subs)
print("\nnumber of subgroups:", len(subs))
def conj(H, g): return frozenset(mult[mult[g, h], inv[g]] for h in H)
classes = []
seen = set()
for H in subs:
    if H in seen: continue
    cls = {conj(H, g) for g in range(n)}
    seen |= cls; classes.append(cls)
print("conjugacy classes of subgroups:", len(classes))
def is_abelian(H): return all(mult[a, b] == mult[b, a] for a in H for b in H)
ab = [H for H in subs if is_abelian(H)]
print("abelian subgroups:", len(ab))
# T|H sum of three characters <=> commuting matrices simultaneously diagonalisable: check via commutant/characters
def n_irreps_dim1(H):
    chars = np.array([np.trace(G[h]) for h in H])
    # number of 1-dim constituents = sum over 1-dim chars... simpler: T|H is sum of three characters iff the matrices commute pairwise
    return is_abelian(H)
print("subgroups with T|H a sum of three characters (= abelian):", sum(1 for H in subs if n_irreps_dim1(H)))
orders = sorted(len(H) for H in subs)
from collections import Counter
print("subgroup orders:", dict(sorted(Counter(orders).items())))
print("class representatives (order, abelian):", sorted((len(next(iter(c))), is_abelian(next(iter(c)))) for c in classes))
# identify the structure: exponent, derived subgroup, etc.
def derived(H):
    return closure([mult[mult[a, b], mult[inv[a], inv[b]]] for a in H for b in H])
Gfull = frozenset(range(n))
D = derived(Gfull)
print("derived subgroup order:", len(D), " abelianisation order:", n // len(D), " G/[G,G] cyclic?", any(len(closure([x]) | D) == n for x in range(n)))
