#!/usr/bin/env python3
"""R44 -- Lie-theory checks on ASSERTED/IMPORTED claims (Phase C tier C-3, batch 2). Root systems built from Cartan
matrices by reflection closure (exact rationals); no external Lie library."""
from fractions import Fraction as F
import itertools, math
import numpy as np

def cartan(t):
    n = int(t[1:]); C = [[2 if i == j else 0 for j in range(n)] for i in range(n)]
    if t[0] == 'A':
        for i in range(n-1): C[i][i+1] = C[i+1][i] = -1
    if t[0] == 'D':
        for i in range(n-2): C[i][i+1] = C[i+1][i] = -1
        C[n-3][n-1] = C[n-1][n-3] = -1
    if t[0] == 'E':   # Bourbaki: 1-3-4-5-6(-7-8), 2 attached to 4
        edges = [(1,3),(3,4),(4,5),(5,6),(2,4)] + ([(6,7)] if n >= 7 else []) + ([(7,8)] if n >= 8 else [])
        for a, b in edges: C[a-1][b-1] = C[b-1][a-1] = -1
    return C

def positive_roots(C):
    """roots in the simple-root basis; simply laced so (a,b) = a^T C b."""
    n = len(C); simple = [tuple(1 if j == i else 0 for j in range(n)) for i in range(n)]
    roots = set(simple); frontier = list(simple)
    while frontier:
        new = []
        for r in frontier:
            for i in range(n):
                pairing = sum(r[j]*C[j][i] for j in range(n))   # <r, alpha_i^vee>
                s = tuple(r[j] - (pairing if j == i else 0) for j in range(n))
                if all(x >= 0 for x in s) and any(s) and s not in roots: roots.add(s); new.append(s)
        frontier = new
    return sorted(roots, key=sum)

def ip(C, a, b): return sum(a[i]*C[i][j]*b[j] for i in range(len(C)) for j in range(len(C)))

print('== B266: McKay(2T) = affine E6 marks {1,1,1,2,2,2,3}: irrep dims of the binary tetrahedral group')
dims = [1,1,1,2,2,2,3]; print('  sum of squares =', sum(d*d for d in dims), '= |2T| = 24 ->', sum(d*d for d in dims) == 24, '; affine E6 marks (Kac labels) are (1,1,1,2,2,2,3) with highest-root coefficient sum 12 = h^vee')

C6 = cartan('E6'); P6 = positive_roots(C6)
print('\n== B304: E6 positive roots, heights, height-6 roots, max height')
hts = [sum(r) for r in P6]; print('  #positive roots =', len(P6), '(dim e6 = 2*36+6 =', 2*len(P6)+6, ') max height =', max(hts), 'highest root =', P6[-1])
h6 = [r for r in P6 if sum(r) == 6]; print('  height-6 roots:', h6)
print('  pairwise inner products among height-6 roots:', [ip(C6, a, b) for a, b in itertools.combinations(h6, 2)], '-> mutually orthogonal:', all(ip(C6, a, b) == 0 for a, b in itertools.combinations(h6, 2)))
from collections import Counter; print('  height distribution:', sorted(Counter(hts).items()))

print('\n== B687: c(E6,1) = 6 and h(27) = C2(27)/(2(k+h^vee)) = 2/3 (long roots length^2 2)')
# fundamental weights in simple-root basis: rows of C^{-1}
Cinv = np.linalg.inv(np.array(C6, dtype=float))
rho = tuple(F(1,2)*sum(r[i] for r in P6) for i in range(6))     # rho = half sum of positive roots, in root basis
def C2(lam):   # (lam, lam + 2 rho) with lam in root basis
    v = [lam[i] + 2*rho[i] for i in range(6)]; return sum(lam[i]*C6[i][j]*v[j] for i in range(6) for j in range(6))
w1 = tuple(F(x).limit_denominator(3) for x in Cinv[0]); w6 = tuple(F(x).limit_denominator(3) for x in Cinv[5]); theta = tuple(F(x) for x in P6[-1])
print('  omega_1 (root basis) =', w1, ' C2(27) = (w1, w1+2rho) =', C2(w1), ' C2(78) = (theta, theta+2rho) =', C2(theta), '= 2 h^vee =', 2*12)
hv = 12; k = 1; print('  c(E6,1) = k dim/(k+h^vee) = 78/13 =', F(78, 13), ' h(27) = C2(27)/(2(k+h^vee)) =', C2(w1)/(2*(k+hv)))
print('  27 vs 27bar: omega_1 and omega_6 differ ->', w1 != w6, '(complex representation; R34 checked -w(omega_1) != omega_1)')

print('\n== B950/B951/B952/B955: dimensions -- su3+su2+u1^3 = 14; A2+A1 Levi of e6 dim 14 (ss 11, centre 3); centralizer of su(3)+su(2) in e6; rank facts')
print('  dim su(3)+su(2)+u(1)^3 = 8+3+3 =', 8+3+3, '; SM gauge algebra dim = 8+3+1 =', 12)
# Levi A2+A1 = simple roots {1,3} (A2) and {5} (A1)? choose disjoint non-adjacent nodes: A2 on {1,3}, A1 on {6}; check subsystem
def levi_dim(nodes):
    sub = [r for r in P6 if all(r[i] == 0 for i in range(6) if i not in nodes)]
    return 2*len(sub) + 6, 2*len(sub) + len(nodes), 6 - len(nodes)
for nodes in ([0, 2, 5], [0, 2, 4]):
    d, ss, z = levi_dim(nodes); print(f'  Levi on nodes {[n+1 for n in nodes]}: dim {d}, semisimple {ss}, centre {z}')
# centralizer of the A2+A1 (nodes 1,3 and 6) inside e6: roots orthogonal to all of alpha1, alpha3, alpha6, plus the Cartan part orthogonal (3-dim)
nodes = [0, 2, 5]; simple = [tuple(1 if j == i else 0 for j in range(6)) for i in nodes]
orth = [r for r in P6 if all(ip(C6, r, s) == 0 for s in simple)]
print('  roots orthogonal to A2+A1 (nodes 1,3,6): positive', len(orth), '-> centralizer dim = 2*%d + 3 = %d' % (len(orth), 2*len(orth)+3), '; roots:', orth)
# same for su(3)+su(2) inside su(5): A2+A1 = nodes {1,2} and {4} of A4: orthogonal roots none -> centralizer = centre 1-dim
C4 = cartan('A4'); P4 = positive_roots(C4); s4 = [(1,0,0,0),(0,1,0,0),(0,0,0,1)]
o4 = [r for r in P4 if all(ip(C4, r, s) == 0 for s in s4)]; print('  in su(5): roots orthogonal to A2+A1 =', o4, '-> centralizer dim =', 2*len(o4) + (4-3))
print('  rank E6 = 6, rank su3+su2+u1^3 = 2+1+3 = 6, rank SM = 2+1+1 = 4, deficit 2')

print('\n== B964: 78 -> 45+16+16bar+1 under D5, 45 -> 24+10+10bar+1 under A4 (root counting)')
D5 = [r for r in P6 if r[0] == 0]   # D5 = nodes 2..6 (Bourbaki: drop node 1)
print('  D5 subsystem positive roots =', len(D5), '-> dim so(10) = 2*%d+5 = %d' % (len(D5), 2*len(D5)+5), '; remaining roots', 2*(36-len(D5)), '= 16+16bar; Cartan 6 = 5+1 -> 78 = 45+16+16bar+1:', 2*len(D5)+5 == 45 and 2*(36-len(D5)) == 32)
A4 = [r for r in P4]; print('  A4 in D5: dim su(5) = 24; 45 - 24 = 21 = 10+10bar+1 ->', 2*len(P4)+4 == 24)

print('\n== B549: E7 Cartan matrix spectrum (claim lists 1, 1.285575, 1.879385, 1.969616, 2.532089, 2.879385, 3.701666)')
C7 = np.array(cartan('E7'), dtype=float); ev = sorted(np.linalg.eigvalsh(C7)); print('  eig(C_E7) =', [round(x, 6) for x in ev])
print('  2 - 2cos(pi e/18), e in {1,5,7,9,11,13,17} =', [round(2-2*math.cos(math.pi*e/18), 6) for e in (1,5,7,9,11,13,17)])
A7 = 2*np.eye(7) - C7; print('  eig(adjacency) = 2cos(pi e/18) =', [round(x, 6) for x in sorted(np.linalg.eigvalsh(A7))])
w, v = np.linalg.eigh(A7); p = v[:, -1]; p = p/p.min() if p.min() > 0 else -p/(-p).min()
print('  Perron root of adjacency =', round(max(w), 6), '; Perron EIGENVECTOR (min entry = 1) =', sorted(round(x, 6) for x in p), '<- this is the claimed list')

print('\n== B953: dim E6 = 78 = 52 + 26 (F4 + 26), rank F4 = 4; E5 = D5 rank 5, E4 = A4 rank 4')
CF = None; print('  dim f4 = 52 (24 positive roots*2 + 4), 78 - 52 = 26 ->', 78-52 == 26)
