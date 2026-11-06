"""Data-free: P-717's approximants A_k = L^5 R (LR)^k; for the conjugate A' = g A g^-1 whose axis apex is the thread's highest
(Re 1/2 mod 1), the order-5 lines A' fixes (B1733's rule, row vectors v(A' -/+ I) = 0 mod 5), reduced mod T to Re tau in [0,1)."""
from sympy import Matrix, sqrt, Rational, floor, nsimplify
L = Matrix([[1,0],[1,1]]); R = Matrix([[1,1],[0,1]]); S = Matrix([[0,-1],[1,0]]); T = R
def word(s):
    M = Matrix.eye(2)
    for ch in s: M = M * (L if ch == 'L' else R)
    return M
def apex(M):
    a,b,c,d = M; 
    if c == 0: return None
    disc = (a+d)**2 - 4
    x1 = ((a - d) + sqrt(disc)) / (2*c); x2 = ((a - d) - sqrt(disc)) / (2*c)
    return ((x1 + x2)/2, abs(x1 - x2)/2)
def fixed5(A):
    out = set()
    for B in (A - Matrix.eye(2), A + Matrix.eye(2)):
        for x in range(5):
            for y in range(5):
                if (x, y) == (0, 0): continue
                w = Matrix([[x, y]]) * B
                if all(int(e) % 5 == 0 for e in w): out.add(min((x, y), ((-x) % 5, (-y) % 5)))
    return out
RL_eig = {(1, 2), (2, 4)}; LR_eig = {(1, 3), (2, 1)}
for k in (0, 4, 5, 9):
    s = 'L'*5 + 'R' + 'LR'*k; best = None
    for i in range(len(s)):
        for pre in ('', 'S'):
            g = (S if pre else Matrix.eye(2)) * word(s[:i]).inv()
            A = g * word(s) * g.inv()
            r = apex(A)
            if r and (best is None or float(r[1]) > float(best[0][1])): best = (r, g, A)
    (re, im), g, A = best
    n = int(floor(float(re)))          # shift by T^-n so Re tau in [0,1): A'' = T^-n A T^n
    Tn = T**(-n); A2 = Tn * A * Tn.inv()
    f = fixed5(A2)
    tag = "RL's eigenline" if f and f <= RL_eig else ("LR's eigenline" if f and f <= LR_eig else "neither")
    print("k=%d  apex Re %.6f Im %.9f  fixed order-5 lines %s -> %s" % (k, float(re) - n, float(im), sorted("(%d/5, %d/5)" % v for v in f) or "none", tag))

print("--- congruence mod 5 of the apex-coordinate thread with powers of RL ---")
RLm = word("RL")
def mod5(M): return Matrix(2, 2, [int(e) % 5 for e in M])
pw = {}
P = Matrix.eye(2)
for j in range(10):
    pw[j] = mod5(P); P = P * RLm
for k in (0, 1, 2, 3, 4, 5, 9, 10):
    s = 'L'*5 + 'R' + 'LR'*k; best = None
    for i in range(len(s)):
        for pre in ('', 'S'):
            g = (S if pre else Matrix.eye(2)) * word(s[:i]).inv()
            A = g * word(s) * g.inv(); r = apex(A)
            if r and (best is None or float(r[1]) > float(best[0][1])): best = (r, g, A)
    (re, im), g, A = best; n = int(floor(float(re))); Tn = T**(-n); A2 = Tn * A * Tn.inv()
    m = mod5(A2); mneg = mod5(-A2)
    hits = [j for j in range(10) if pw[j] == m] + [("-", j) for j in range(10) if pw[j] == mneg]
    print("k=%2d  A' mod 5 = %s  equals (RL)^j mod 5 for j in %s" % (k, m.tolist(), hits or "none"))
