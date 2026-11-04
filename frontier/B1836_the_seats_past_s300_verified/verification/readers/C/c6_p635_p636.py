"""C6: (P-635) dim H^1 of the flat Q8 bundle with holonomies (Q_I, Q_J), adjoint coefficients su(2) = R^3, on
 (a) the closed torus (pi_1 = Z^2; the lane's Theorem 62 Part 3), (b) the once-punctured torus (pi_1 = F_2 = <a, b>, the
 fibre of m004), and (c) (b) relative to the boundary loop c = [a, b] (rho(c) = -I, Ad(c) = 1): the parabolic part.
(P-636) Theorem 56's selection: over ALL positive words in L = [[1,1],[0,1]], R = [[1,0],[1,1]] up to length 10 (not only
 L^a R^b), the minimal hyperbolic trace and its fixed-point count |2 - tr|; the words with |2 - tr| = 3; and whether the
 rule 'prime count > 2, a != b' differs from 'prime count > 2'.  Exact (sympy / integers).  No SM quantity."""
import itertools, pathlib
import numpy as np
import sympy as sp

out = []
QI = sp.Matrix([[sp.I, 0], [0, -sp.I]]); QJ = sp.Matrix([[0, 1], [-1, 0]]); QK = QI * QJ
basis = [QI, QJ, QK]
def Ad(g):
    M = sp.zeros(3)
    for c, X in enumerate(basis):
        img = g * X * g.inv()
        for r, Yb in enumerate(basis):
            M[r, c] = sp.simplify((img * Yb.H).trace() / 2)
    return M
Aa, Ab = Ad(QI), Ad(QJ); I3 = sp.eye(3)
out.append("P-635: Ad(Q_I) = diag%s, Ad(Q_J) = diag%s ; Q_I Q_J Q_I^-1 Q_J^-1 = %s" % (
    tuple(Aa[i, i] for i in range(3)), tuple(Ab[i, i] for i in range(3)), (QI * QJ * QI.inv() * QJ.inv()).tolist()))
H0 = 3 - (sp.Matrix.vstack(Aa - I3, Ab - I3)).rank()
# (a) Z^2: cocycles satisfy (Aa - 1) u_b = (Ab - 1) u_a
d1 = sp.Matrix.hstack(-(Ab - I3), Aa - I3)
Z1a = 6 - d1.rank(); B1 = 3 - H0
out.append("  (a) closed torus Z^2: dim H^0 = %d, dim Z^1 = %d, dim B^1 = %d, dim H^1 = %d" % (H0, Z1a, B1, Z1a - B1))
# (b) F_2: every (u_a, u_b) is a cocycle
out.append("  (b) once-punctured torus F_2: dim H^0 = %d, dim Z^1 = 6, dim H^1 = %d" % (H0, 6 - B1))
# (c) parabolic: u_c for c = a b a^-1 b^-1 lies in (Ad(c) - 1) V = 0
def u_c(ua, ub):
    # u_{a b a^-1 b^-1} = u_a + a u_b - a b a^-1 u_a - a b a^-1 b^-1 u_b
    return ua + Aa * ub - Aa * Ab * Aa.inv() * ua - Aa * Ab * Aa.inv() * Ab.inv() * ub
cols = []
for i in range(6):
    e = sp.zeros(6, 1); e[i] = 1
    cols.append(u_c(e[:3, :], e[3:, :]))
UC = sp.Matrix.hstack(*cols)
out.append("  (c) relative to the boundary (Ad(c) = 1, so u_c must vanish): rank of (u_a, u_b) -> u_c = %d, dim H^1_par = %d"
           % (UC.rank(), (6 - UC.rank()) - B1))

# ---- P-636
L = np.array([[1, 1], [0, 1]], dtype=object); R = np.array([[1, 0], [1, 1]], dtype=object)
def mul(word):
    M = np.array([[1, 0], [0, 1]], dtype=object)
    for ch in word: M = M.dot(L if ch == "L" else R)
    return M
def canon(word):                       # cyclic class representative
    return min(word[i:] + word[:i] for i in range(len(word)))
seen = {}
for n in range(1, 11):
    for wd in itertools.product("LR", repeat=n):
        s = "".join(wd)
        if "L" not in s or "R" not in s: continue           # parabolic powers excluded
        c = canon(s)
        if c in seen: continue
        tr = int(mul(c).trace()); seen[c] = (tr, abs(2 - tr))
by_tr = {}
for c, (tr, lf) in seen.items(): by_tr.setdefault(tr, []).append(c)
trs = sorted(by_tr)
out.append("P-636: positive hyperbolic classes up to length 10: %d ; minimal trace %d, its classes %s, fixed-point count |2 - tr| = %d"
           % (len(seen), trs[0], by_tr[trs[0]], abs(2 - trs[0])))
out.append("  classes with |2 - tr| = 3 (trace 5): %s" % by_tr.get(5))
out.append("  traces 3..7 and their classes: %s" % {t: by_tr.get(t) for t in range(3, 8)})
isprime = lambda m: m > 1 and all(m % p for p in range(2, int(m ** .5) + 1))
single = [(a, b) for a in range(1, 7) for b in range(1, 7)]
r1 = sorted((a * b, a, b) for a, b in single if isprime(a * b) and a * b > 2 and a != b)[0]
r2 = sorted((a * b, a, b) for a, b in single if isprime(a * b) and a * b > 2)[0]
r3 = sorted((a * b, a, b) for a, b in single if isprime(a * b))[0]
out.append("  the lane's rule (prime, > 2, a != b) -> %s ; without 'a != b' -> %s ; without '> 2' -> %s (count 2, L^2 R)" % (r1, r2, r3))
print("\n".join(out))
pathlib.Path(__file__).with_name("c6_run.txt").write_text("\n".join(out) + "\n")
