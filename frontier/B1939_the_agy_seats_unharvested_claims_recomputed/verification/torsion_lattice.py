"""Run 4: the cap lattice. H_2(dP9) = I_{1,9}; F = 3H - sum E_i; Sigma = E_9; {F, Sigma}^perp = E8(-1)?
Plants: F'' = 3H - (E2+...+E9) and Sigma' = H must fail. (F' = 3H - (E1+..+E8) = F + E9 is NOT a valid plant: it lies
in span{F, E9} and has the same complement.)"""
from fractions import Fraction as Fr
from itertools import product as iprod
from sympy import Matrix

n = 10  # basis H, E1..E9


def dot(x, y):
    return x[0] * y[0] - sum(x[i] * y[i] for i in range(1, n))


def vec(a=0, **E):
    v = [0] * n
    v[0] = a
    for k, c in E.items():
        v[int(k[1:])] = c
    return v


def e(i):
    v = [0] * n
    v[i] = 1
    return v


H = e(0)
F = [3] + [-1] * 9
SIG = e(9)
Q = Matrix(n, n, lambda i, j: dot(e(i), e(j)))
print('I_{1,9}: det =', Q.det(), '; signature (pos, neg) =',
      (sum(1 for x in Q.eigenvals(multiple=True) if x > 0), sum(1 for x in Q.eigenvals(multiple=True) if x < 0)),
      '; odd (H.H = 1):', dot(H, H) % 2 == 1)
K = [-x for x in F]
print('F^2 =', dot(F, F), ' Sigma^2 =', dot(SIG, SIG), ' Sigma.F =', dot(SIG, F), ' K = -F, K^2 =', dot(K, K))
print('K characteristic (x^2 = x.K mod 2 on the basis):', all((dot(e(i), e(i)) - dot(e(i), K)) % 2 == 0 for i in range(n)))
chi = 2 + n   # b0 + b2 + b4, b1 = b3 = 0
sigma = 1 - 9
print('chi_top =', chi, ' sigma =', sigma, ' chi(O) = (K^2 + chi)/12 =', Fr(dot(K, K) + chi, 12),
      ' signature theorem (K^2 - 2 chi)/3 =', Fr(dot(K, K) - 2 * chi, 3))


def complement_report(Fv, Sv, label):
    span2 = Matrix([[dot(Fv, Fv), dot(Fv, Sv)], [dot(Sv, Fv), dot(Sv, Sv)]])
    roots = []
    odd_units = []
    # enumerate x = aH + sum c_i E_i with x^2 in {-1,-2}: sum c_i^2 = a^2 + {1,2}.
    # Bound |a| <= 4: for (F, E9), x.E9 = 0 gives c9 = 0 and x.F = 0 gives 3a = -sum_{i<=8} c_i, so
    # 9a^2 <= 8 (a^2 + 2) -> a^2 <= 16; for the plants the same argument gives |a| <= 2 (F'') and a = 0 (Sigma' = H).
    for a in range(-4, 5):
        budget = a * a + 2
        def rec2(i, partial, sq):
            if sq > budget:
                return
            if i == n:
                yield list(partial)
                return
            for c in range(-4, 5):
                if sq + c * c > budget:
                    continue
                partial.append(c)
                yield from rec2(i + 1, partial, sq + c * c)
                partial.pop()
        for x in rec2(1, [a], 0):
            q = dot(x, x)
            if q in (-1, -2) and dot(x, Fv) == 0 and dot(x, Sv) == 0:
                (roots if q == -2 else odd_units).append(tuple(x))
    print(f'[{label}] Gram of span{{F,Sigma}} = {span2.tolist()} (det {span2.det()}); '
          f'norm -2 vectors in complement: {len(roots)}; norm -1 vectors: {len(odd_units)} '
          f'-> {"EVEN" if not odd_units else "ODD"}')
    return roots, odd_units, span2.det()


roots, odd, d2 = complement_report(F, SIG, 'F, E9')
# the stated basis (indices are my reading; the relay masks them): alpha_i = E_i - E_{i+1} (i=1..7), alpha_8 = H-E1-E2-E3
alphas = [vec(0, **{f'E{i}': 1, f'E{i+1}': -1}) for i in range(1, 8)] + [vec(1, E1=-1, E2=-1, E3=-1)]
print('alphas in complement:', all(dot(a, F) == 0 and dot(a, SIG) == 0 for a in alphas))
G = Matrix(8, 8, lambda i, j: -dot(alphas[i], alphas[j]))
print('-Gram(alphas) det =', G.det(), '; positive definite:', all(x > 0 for x in G.eigenvals(multiple=True)),
      '; diagonal all 2:', all(G[i, i] == 2 for i in range(8)))
edges = [(i, j) for i in range(8) for j in range(i + 1, 8) if G[i, j] != 0]
deg = [sum(1 for ed in edges if i in ed) for i in range(8)]
print('Dynkin edges:', len(edges), 'entries:', sorted(set(G[i, j] for i, j in edges)), 'degrees:', deg)
# arm lengths from the trivalent node
tri = [i for i in range(8) if deg[i] == 3]
arms = []
if len(tri) == 1:
    adj = {i: [j for ed in edges for j in ed if i in ed and j != i] for i in range(8)}
    for start in adj[tri[0]]:
        L, prev, cur = 1, tri[0], start
        while True:
            nxt = [x for x in adj[cur] if x != prev]
            if not nxt:
                break
            prev, cur = cur, nxt[0]
            L += 1
        arms.append(L)
print('trivalent nodes:', tri, ' arm lengths:', sorted(arms), ' (E8 = tree with arms 1,2,4)')
# the alphas span the whole complement: complement is unimodular (span{F,E9} unimodular), alphas have det 1
print('index of span(alphas) in the complement = sqrt(det/|det complement|) = 1 since det(-Gram) = 1 and the '
      'complement of a unimodular sublattice of a unimodular lattice is unimodular')
E8_ok = (len(roots) == 240 and not odd and G.det() == 1 and sorted(arms) == [1, 2, 4] and len(edges) == 7)
print('E8(-1) complement:', E8_ok)

print('\n--- plants')
F2 = [3, 0] + [-1] * 8   # 3H - (E2+...+E9)
r2, o2, d22 = complement_report(F2, SIG, "PLANT F''=3H-(E2..E9)")
P6a = (len(r2) == 240 and not o2)
print("PLANT P6a caught (complement not E8(-1)):", not P6a)
r3, o3, d33 = complement_report(F, H, "PLANT Sigma'=H")
print("PLANT P6b caught (span not unimodular, det", d33, "; complement roots", len(r3), "):", not (abs(d33) == 1 and len(r3) == 240))
F1 = [3] + [-1] * 8 + [0]   # 3H - (E1..E8) = F + E9: an INVALID plant (same span)
r1_, o1_, d11 = complement_report(F1, SIG, "INVALID PLANT F'=3H-(E1..E8)=F+E9")
print("invalid plant F' gives the same complement (cannot fail):", len(r1_) == 240 and not o1_)

print('\n--- arithmetic')
print('12/2 =', Fr(12, 2), '; N(N+1)/2 for N=1..4:', [N * (N + 1) // 2 for N in range(1, 5)])
# minimisation as the relay states it: five integers, sum 0, |h_1| = N, k = (1/2) sum h^2
for N in range(1, 5):
    best = min(sum(h * h for h in (N,) + rest) for rest in iprod(range(-6, 7), repeat=4) if N + sum(rest) == 0)
    print(f'  N={N}: min sum h^2 = {best}, k_min = {Fr(best, 2)}')
print("pairs (x,y) in F_5^2 with x*y = 0 mod 5:", sum(1 for x in range(5) for y in range(5) if (x * y) % 5 == 0))
# spectral curve under MY reading (digits masked): n = 5 sheets, C in |5 Sigma + 6 F|
nS, mF = 5, 6
C = [nS * SIG[i] + mF * F[i] for i in range(n)]
C2, CK = dot(C, C), dot(C, K)
g = 1 + Fr(C2 + CK, 2)
R = (2 * g - 2) - nS * (-2)
print(f'reading C in |5 Sigma + 6 F|: C^2 = {C2}, C.K = {CK}, g = {g}, Riemann-Hurwitz R = {R}, C.Sigma = {dot(C, SIG)}')
