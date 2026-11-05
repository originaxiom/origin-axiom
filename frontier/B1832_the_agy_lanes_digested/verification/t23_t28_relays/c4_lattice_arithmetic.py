"""c4: exact arithmetic behind the agy lane's lattice / monodromy / character claims (first principles; no lane code).

Claims checked (agy/audit-2026-11-02 @ 18c607040):
  T23 step 1 / Phase 1: N = 5 the unique N in 2..12 (gcd(N,6)=1) with (1,2) == (6,-3) mod N
  T23 step 3 / T28 cc1: tau -> tau+1 permutes the five order-10 lines (2/5, (2j+1)/10) as j -> j-2 (mod 5)
  FOUR_STEPS 1.1: U = ((LR)^3 - I)/4, det -1, tr 4; 'U^2 == I mod 5'; '(2/5,0) in the (+2) eigenspace of U mod 5'
  SEVEN_PILLARS P2: spin cosets of the 64 8-torsion points; NS coset -> '2 Gamma(2)-orbits of size 8';
                    '(2/5,3/5) a Golden eigen-line of LR mod 5'; 'the 4 nontrivial 5-torsion points split into two eigen-lines'
  HOSTILE 7.3 / ELEVATION s6: Fix((LR)^3) = (Z/4)^2, '5 nonzero <T,-I>-orbits + 1 projective order-5 eigen-orbit';
                    which census lines lie in Fix((LR)^3)
  SEVEN_PILLARS P6: (LR)^3 apex (1 + i sqrt5)/2; 'W = L^5 R^2 L R = [[18,13],[5,4]], tr 22, apex 2/5 + i 4 sqrt14/5'
  FOUR_STEPS 1.2 / Thm 7: |det S_s| = |1 + c_s^2| |h.h| for the characters c_u, c_d, c_e
  SEVEN_PILLARS Thm 6: |1 + c^2| = 1 for c in {+-w, +-w^2}
  T25: Q2 = qL^2 + qR^2 = (17, 5, 45), sqrt(45/5) = 3
  ELEVATION s6: menu 266*13*8*2*9 and its bits
  HOSTILE 6.1: |det(LR - w I)| (the referee's intermediate '|3 - 3w|')
  HOSTILE 6.x / P-564: symmetric real commutant of <C3, p_refl> (lane's p_refl) vs <C3, pure transposition>
"""
import cmath
import itertools
import math
from fractions import Fraction as F

import numpy as np

out = []
def say(*a):
    s = " ".join(str(x) for x in a); print(s); out.append(s)

def mat(a): return np.array(a, dtype=object)
def mmul(A, B): return np.array([[sum(A[i][k] * B[k][j] for k in range(2)) for j in range(2)] for i in range(2)], dtype=object)

# ---------------------------------------------------------------- N = 5 uniqueness
hits = [N for N in range(2, 13) if math.gcd(N, 6) == 1 and (1 - 6) % N == 0 and (2 - (-3)) % N == 0]
say("[T23.1] N in 2..12, gcd(N,6)=1, (1,2)==(6,-3) mod N:", hits, "(the condition is N | 5: 1-6 = -5, 2+3 = 5)")

# ---------------------------------------------------------------- T-action on order-10 lines
def tshift(j):  # w = (2/5)(tau+1) - (2j+1)/10 = (2/5)tau - ((2j+1)/10 - 2/5)
    b = (F(2 * j + 1, 10) - F(2, 5)) % 1
    return [k for k in range(5) if F(2 * k + 1, 10) == b][0]
perm = [tshift(j) for j in range(5)]
orb, x = [], 0
for _ in range(5): orb.append(x); x = tshift(x)
say("[T23.3] tau->tau+1 maps line j to", perm, "; orbit of 0:", orb, "; fixed points:", sum(perm[j] == j for j in range(5)))

# ---------------------------------------------------------------- LR, U and mod-5 structure
for name, L, R in (("L=[[1,0],[1,1]],R=[[1,1],[0,1]]", mat([[1, 0], [1, 1]]), mat([[1, 1], [0, 1]])),
                   ("L=[[1,1],[0,1]],R=[[1,0],[1,1]]", mat([[1, 1], [0, 1]]), mat([[1, 0], [1, 1]]))):
    LR = mmul(L, R); LR3 = mmul(mmul(LR, LR), LR)
    U = (LR3 - mat([[1, 0], [0, 1]])) // 4
    U2 = mmul(U, U)
    say("[LR] %s: LR=%s (LR)^3=%s U=%s det U=%d tr U=%d U^2 mod 5=%s" % (
        name, LR.tolist(), LR3.tolist(), U.tolist(), U[0][0] * U[1][1] - U[0][1] * U[1][0], U[0][0] + U[1][1], (U2 % 5).tolist()))
    for v in ((2, 0), (2, 1), (2, 3)):
        Uv = ((U[0][0] * v[0] + U[0][1] * v[1]) % 5, (U[1][0] * v[0] + U[1][1] * v[1]) % 5)
        eig = [lam for lam in range(5) if ((lam * v[0]) % 5, (lam * v[1]) % 5) == Uv]
        say("      U(%d,%d) = %s mod 5; eigenvalue(s): %s" % (v[0], v[1], Uv, eig or "none (not an eigenvector)"))
    # LR mod 5: eigen-lines
    lines = []
    for v in itertools.product(range(5), repeat=2):
        if v == (0, 0): continue
        LRv = ((LR[0][0] * v[0] + LR[0][1] * v[1]) % 5, (LR[1][0] * v[0] + LR[1][1] * v[1]) % 5)
        for lam in range(1, 5):
            if ((lam * v[0]) % 5, (lam * v[1]) % 5) == LRv: lines.append((v, lam))
    say("      LR mod 5: char poly x^2-3x+1 = (x+1)^2 mod 5; eigenvectors (v, lambda):", lines)

# the referee's action on (p1, p2) for w = p1 tau - p2:  M = [[2,-1],[-1,1]]
M = mat([[2, -1], [-1, 1]]); M3 = mmul(mmul(M, M), M)
say("[M_LR] referee's action M =", M.tolist(), " M^3 =", M3.tolist())
def act(A, p): return ((A[0][0] * p[0] + A[0][1] * p[1]) % 1, (A[1][0] * p[0] + A[1][1] * p[1]) % 1)
pts16 = [(F(a, 4), F(b, 4)) for a in range(4) for b in range(4)]
fix = [p for p in itertools.product([F(a, 40) for a in range(40)], repeat=2) if act(M3, p) == p]
say("      #Fix(M^3) on (1/40 Z)^2 =", len(fix), " all in (1/4 Z)^2:", all(p in pts16 for p in fix))
# orbits of the 15 nonzero fixed points under <M, -I>
seen, orbits = set(), []
for p in pts16:
    if p == (0, 0) or p in seen: continue
    o, frontier = {p}, [p]
    while frontier:
        q = frontier.pop()
        for r in (act(M, q), ((-q[0]) % 1, (-q[1]) % 1)):
            if r not in o: o.add(r); frontier.append(r)
    seen |= o; orbits.append(sorted(o))
say("      <M,-I>-orbits of the 15 nonzero points of Fix(M^3):", len(orbits), "sizes", [len(o) for o in orbits])
# the census's reduction group <T, -I>, T: tau -> tau+1, i.e. (p1, p2) -> (p1, p2 - p1)
seen, torbs = set(), []
for p in pts16:
    if p == (0, 0) or p in seen: continue
    o, frontier = {p}, [p]
    while frontier:
        q = frontier.pop()
        for r in ((q[0], (q[1] - q[0]) % 1), ((-q[0]) % 1, (-q[1]) % 1)):
            if r not in o: o.add(r); frontier.append(r)
    seen |= o; torbs.append(sorted(o))
say("      <T,-I>-orbits (T: p2 -> p2 - p1) of the 15 nonzero points of Fix(M^3):", len(torbs), "sizes", [len(o) for o in torbs],
    "reps", [tuple(map(str, o[0])) for o in torbs])
for p in ((F(2, 5), F(1, 5)), (F(2, 5), F(0)), (F(3, 8), F(3, 8)), (F(2, 5), F(1, 10)), (F(2, 5), F(3, 5))):
    Mp, M3p = act(M, p), act(M3, p)
    say("      p=%s: M p=%s  M^3 p=%s  in Fix(M^3): %s  M p == -p: %s" % (
        tuple(map(str, p)), tuple(map(str, Mp)), tuple(map(str, M3p)), M3p == p, Mp == ((-p[0]) % 1, (-p[1]) % 1)))

# ---------------------------------------------------------------- spin cosets of the 64 8-torsion points
U = mat([[3, 2], [2, 1]])
cos = {}
for a, b in itertools.product(range(8), repeat=2):
    e = ((U[0][0] * a + U[0][1] * b) % 2, (U[1][0] * a + U[1][1] * b) % 2)
    cos.setdefault(e, []).append((a, b))
say("[P2] spin cosets eps = U(a,b) mod 2, sizes:", {k: len(v) for k, v in sorted(cos.items())},
    "; eps=(0,0) are the 4-torsion points:", sorted(cos[(0, 0)]) == sorted((a, b) for a in range(0, 8, 2) for b in range(0, 8, 2)))
# Gamma(2) orbits on the odd-odd coset, acting on (p1, p2) (both actions: column vectors and row vectors)
gens = [mat([[1, 2], [0, 1]]), mat([[1, 0], [2, 1]]), mat([[-1, 0], [0, -1]])]
for label, tr in (("column", False), ("row", True)):
    seen, orbs = set(), []
    for p in cos[(1, 1)]:
        if p in seen: continue
        o, fr = {p}, [p]
        while fr:
            q = fr.pop()
            for g in gens:
                gg = g.T if tr else g
                r = ((gg[0][0] * q[0] + gg[0][1] * q[1]) % 8, (gg[1][0] * q[0] + gg[1][1] * q[1]) % 8)
                if r not in o: o.add(r); fr.append(r)
        seen |= o; orbs.append(sorted(o))
    say("      Gamma(2) (%s action) orbits on the 16 odd-odd points: %d, sizes %s; (3,3) with (1,1): %s" % (
        label, len(orbs), [len(o) for o in orbs], any((1, 1) in o and (3, 3) in o for o in orbs)))
    # <T^2, -I> only (the relay's 'Gamma(2) = <T^2, -I>')
seen, orbs = set(), []
for p in cos[(1, 1)]:
    if p in seen: continue
    o, fr = {p}, [p]
    while fr:
        q = fr.pop()
        for g in (gens[0], gens[2]):
            r = ((g[0][0] * q[0] + g[0][1] * q[1]) % 8, (g[1][0] * q[0] + g[1][1] * q[1]) % 8)
            if r not in o: o.add(r); fr.append(r)
    seen |= o; orbs.append(sorted(o))
say("      <T^2,-I> only: orbits %d sizes %s" % (len(orbs), [len(o) for o in orbs]))
say("      (2/5,3/5)+(0,1/2) mod 1 =", tuple(map(str, ((F(2, 5)) % 1, (F(3, 5) + F(1, 2)) % 1))))

# ---------------------------------------------------------------- hyperbolic apices
def apex(A):
    a, b, c, d = [float(x) for x in (A[0][0], A[0][1], A[1][0], A[1][1])]
    # fixed points c z^2 + (d - a) z - b = 0
    disc = (d - a) ** 2 + 4 * b * c
    r1, r2 = ((a - d) - math.sqrt(disc)) / (2 * c), ((a - d) + math.sqrt(disc)) / (2 * c)
    return complex((r1 + r2) / 2, abs(r2 - r1) / 2), (r1, r2), disc
LRs = mat([[2, 1], [1, 1]]); LR3 = mmul(mmul(LRs, LRs), LRs)
ap, roots, disc = apex(LR3)
say("[P6] (LR)^3 =", LR3.tolist(), "fixed points", roots, "apex", ap, " (1+i sqrt5)/2 =", complex(0.5, math.sqrt(5) / 2))
for name, L, R in (("L=[[1,0],[1,1]]", mat([[1, 0], [1, 1]]), mat([[1, 1], [0, 1]])), ("L=[[1,1],[0,1]]", mat([[1, 1], [0, 1]]), mat([[1, 0], [1, 1]]))):
    W = mat([[1, 0], [0, 1]])
    for g in [L] * 5 + [R] * 2 + [L, R]: W = mmul(W, g)
    a_, roots_, disc_ = apex(W)
    say("      W = L^5 R^2 L R (%s) = %s  det %d  tr %d  apex %s" % (name, W.tolist(), W[0][0] * W[1][1] - W[0][1] * W[1][0], W[0][0] + W[1][1], a_))
Wst = mat([[18, 13], [5, 4]])
say("      the relay's W = [[18,13],[5,4]]: det", Wst[0][0] * Wst[1][1] - Wst[0][1] * Wst[1][0], " tr", Wst[0][0] + Wst[1][1],
    " fixed-point discriminant (a-d)^2+4bc =", (18 - 4) ** 2 + 4 * 13 * 5, " stated apex 2/5 + i 4 sqrt14/5 =", complex(0.4, 4 * math.sqrt(14) / 5))

# ---------------------------------------------------------------- characters
w3 = cmath.exp(2j * math.pi / 3)
cu, cd, ce = -1j * math.sqrt(2), -cmath.sqrt(cmath.exp(1j * math.pi / 4) - 1), -1.0
say("[Thm7] |1+c^2| for (c_u, c_d, c_e) =", [round(abs(1 + c * c), 15) for c in (cu, cd, ce)],
    "(the relay: 'preserves |det S_s| = |h.h| identically in all three sectors')")
say("[Thm6] |1+c^2| for c in {w, -w, w^2, -w^2}:", [round(abs(1 + c * c), 15) for c in (w3, -w3, w3 ** 2, -w3 ** 2)], "; c_e = 0 ->", abs(1 + 0))
# k_R arithmetic of Theorem 9 part A
for nm, q1, q2 in (("up", 1, -4), ("down", 1, 2), ("lepton", -3, 6)):
    kR = q2 // 2
    say("      %s: k_R = q2//2 = %d, k_R^2 mod 8 = %d, exp(i pi k_R^2/4) = %s" % (nm, kR, kR * kR % 8, cmath.exp(1j * math.pi * (kR * kR % 8) / 4)))

# ---------------------------------------------------------------- T25 and ELEVATION arithmetic
Q2 = [1 + 16, 1 + 4, 9 + 36]
say("[T25] Q2 =", Q2, " sqrt(Q2_lep/Q2_down) =", math.sqrt(Q2[2] / Q2[1]), " (lepton (-3,6) = -3*(1,-2), |(1,-2)| = |(1,2)|)")
n = 266 * 13 * 8 * 2 * 9
say("[ELEV] 266*13*8*2*9 =", n, " log2 =", round(math.log2(n), 3), "; log2 266, 13, 9 =", [round(math.log2(v), 3) for v in (266, 13, 9)],
    "; log2 6 =", round(math.log2(6), 3), "; 16.341 =", round(math.log2(n) - math.log2(6), 3))

# ---------------------------------------------------------------- m004 torsion numbers
LRc = np.array([[2, 1], [1, 1]], dtype=complex)
say("[H6.1] det(LR - I) =", round(np.linalg.det(LRc - np.eye(2)).real), " |det(LR - w I)| =", abs(np.linalg.det(LRc - w3 * np.eye(2))),
    " |w - 3 + 1/w| =", abs(w3 - 3 + 1 / w3), " |3 - 3w| (the referee's intermediate) =", abs(3 - 3 * w3), " 4/|1-w| =", 4 / abs(1 - w3), "=4/sqrt3", 4 / math.sqrt(3))

# ---------------------------------------------------------------- commutants (P-564 / the lane's referee)
C3 = np.array([[0, 0, 1], [1, 0, 0], [0, 1, 0]], dtype=float)
p_refl = np.array([[1, 0, 0], [0, 0, -1], [0, -1, 0]], dtype=float)
p_perm = np.array([[1, 0, 0], [0, 0, 1], [0, 1, 0]], dtype=float)
def group(gens):
    G = [np.eye(3)]; fr = [np.eye(3)]
    while fr:
        g = fr.pop()
        for h in gens:
            x = h @ g
            if not any(np.allclose(x, y) for y in G): G.append(x); fr.append(x)
    return G
def sym_commutant_dim(G):
    basis = []
    for i in range(3):
        for j in range(i, 3):
            E = np.zeros((3, 3)); E[i, j] = E[j, i] = 1; basis.append(E)
    rows = []
    for g in G:
        rows.append(np.array([(g @ E @ g.T - E).ravel() for E in basis]).T)
    A = np.vstack(rows)
    return len(basis) - np.linalg.matrix_rank(A)
for nm, gg in (("<C3, p_refl (lane's, signed)>", [C3, p_refl]), ("<C3, pure transposition>", [C3, p_perm])):
    G = group(gg)
    say("[P-564] %s: order %d, dets %s, dim of the symmetric real commutant = %d" % (nm, len(G), sorted(set(int(round(np.linalg.det(g))) for g in G)), sym_commutant_dim(G)))

pathlib = __import__("pathlib")
pathlib.Path(__file__).with_name("c4_lattice_arithmetic_out.txt").write_text("\n".join(out) + "\n")
