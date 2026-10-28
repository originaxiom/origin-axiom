"""Referee B1804, check 7: the frame in which the monodromy acts HOLOMORPHICALLY on the fibre T^4.

T^4 = R^4 / Z^4 with coordinates (x1, y1, x2, y2) = H (x) W (factor-index ordering), A = LR acting on W: v -> (A (x) I) v
(conjugate in SL(4, Z) to the draft's diagonal action, r6).  The complex structures on which A is holomorphic: the
holomorphic 1-forms are A-eigenvectors, dz_+ = f_+ . (dx + tau1 dy), dz_- = f_- . (dx + tau2 dy) with f_+ = (1, phi),
f_- = (1, 1 - phi) the eigenvectors of A on W (eigenvalues phi^2, phi^-2): a two-parameter family (tau1, tau2), the
abelian surfaces with real multiplication by Z[phi] (the Hilbert modular family of Q(sqrt5)); tau1 = tau2 is E_tau (x) Z^2.
Question: do two independent LR-invariant integral classes become (1,1) together at isolated points of this family?
"""
import itertools
import sympy as sp

t1, t2 = sp.symbols("tau1 tau2")
phi = (1 + sp.sqrt(5)) / 2
L = sp.Matrix([[1, 0], [1, 1]]); R = sp.Matrix([[1, 1], [0, 1]])
A = L * R
g = sp.Matrix(sp.BlockMatrix([[A[i, j] * sp.eye(2) for j in range(2)] for i in range(2)]))
pairs = list(itertools.combinations(range(4), 2))

fp, fm = sp.Matrix([[1, phi]]), sp.Matrix([[1, 1 - phi]])
for f, mu in ((fp, phi ** 2), (fm, phi ** -2)):
    assert sp.simplify(f * A - mu * f) == sp.zeros(1, 2)
# 1-forms as rows on (dx1, dy1, dx2, dy2)
dzp = sp.Matrix([[fp[0], fp[0] * t1, fp[1], fp[1] * t1]])
dzm = sp.Matrix([[fm[0], fm[0] * t2, fm[1], fm[1] * t2]])
print("holomorphic: pullbacks are multiples:", sp.simplify(dzp * g - phi ** 2 * dzp) == sp.zeros(1, 4),
      sp.simplify(dzm * g - phi ** -2 * dzm) == sp.zeros(1, 4))


def two_form(a, b):  # a ^ b as antisymmetric matrix coefficients on pairs
    return {(i, j): sp.expand(a[i] * b[j] - a[j] * b[i]) for (i, j) in pairs}


Om = two_form(dzp, dzm)


def wedge4(F, Om):  # F ^ Om coefficient of vol for 2-forms given as dicts on pairs
    # vol coefficient of e_ij ^ e_kl
    def s(i, j, k, l):
        idx = (i, j, k, l)
        if len(set(idx)) < 4:
            return 0
        perm = list(idx); sign = 1
        for a in range(4):
            for b in range(3 - a):
                if perm[b] > perm[b + 1]:
                    perm[b], perm[b + 1] = perm[b + 1], perm[b]; sign = -sign
        return sign
    return sp.expand(sum(F[p] * Om[q] * s(*p, *q) for p in pairs for q in pairs))


fs = sp.symbols("f0:6")
Fm = sp.zeros(4, 4)
for k, (i, j) in enumerate(pairs):
    Fm[i, j] = fs[k]; Fm[j, i] = -fs[k]
sol = sp.solve(list(g.T * Fm * g - Fm), fs, dict=True)[0]
Fg = Fm.subs(sol); fr = sorted(Fg.free_symbols, key=str)
B = [Fg.subs({f: (1 if f == h else 0) for f in fr}) for h in fr]
conds = [sp.expand(wedge4({p: Bk[p] for p in pairs}, Om)) for Bk in B]
print("invariant basis (coefficients on dx1dy1, dx1dx2, dx1dy2, dy1dx2, dy1dy2, dx2dy2):")
for Bk, c in zip(B, conds):
    print("   ", [Bk[p] for p in pairs], " -> F ^ Omega =", sp.simplify(c))
# check: the two non-invariant eigen-classes are (1,1) identically (real multiplication classes)
ev = (g.T).eigenvects()


def pf(F):
    return sp.expand(F[0, 1] * F[2, 3] - F[0, 2] * F[1, 3] + F[0, 3] * F[1, 2])


Fgen = sum((sp.Symbol("c%d" % k) * Bk for k, Bk in enumerate(B)), sp.zeros(4, 4))
print("intersection form 2 Pf on the invariant lattice:", sp.expand(2 * pf(Fgen)))

# Two invariant classes are (1,1) together iff Omega is orthogonal to both.  Take negative-definite pairs (K) from the
# invariant lattice (Hodge index: invariant (1,1) classes here are orthogonal to Omega, which spans a positive plane in
# the (2,2) invariant lattice, so they form a negative-definite lattice), and solve the two conditions exactly.
Q = sp.expand(2 * pf(Fgen))
cs = sp.symbols("c0:%d" % len(B))
G = sp.hessian(Q, cs) / 2


def gram(v1, v2):
    V = sp.Matrix([v1, v2])
    return V * G * V.T


cands = [(1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1), (1, 0, 1, 0), (1, 1, 0, 0), (0, 1, 0, 1), (1, 0, 0, 1),
         (1, 0, -1, 0), (0, 1, 1, 0), (1, 1, 1, 0), (2, 0, 1, 0), (1, 0, 2, 0), (0, 1, 0, -1)]
seen = set(); rows = []
for v1, v2 in itertools.combinations(cands, 2):
    Gm = gram(v1, v2)
    if not (Gm[0, 0] < 0 and Gm.det() > 0):
        continue
    e1 = sp.expand(sum(a * c for a, c in zip(v1, conds)))
    e2 = sp.expand(sum(a * c for a, c in zip(v2, conds)))
    # e1, e2 are affine in each tau separately: solve e1 for tau2, substitute
    s2 = sp.solve(e1, t2)
    for r2 in s2:
        num = sp.numer(sp.together(sp.simplify(e2.subs(t2, r2))))
        for r1 in sp.solve(num, t1):
            r1s = sp.radsimp(sp.simplify(r1)); r2s = sp.radsimp(sp.simplify(r2.subs(t1, r1)))
            a, b = complex(sp.N(r1s)), complex(sp.N(r2s))
            if abs(a.imag) > 1e-12 and abs(b.imag) > 1e-12:
                key = (round(a.real, 9), round(a.imag, 9), round(b.real, 9), round(b.imag, 9))
                if key in seen:
                    continue
                seen.add(key)
                x = sp.symbols("x")
                mp1 = sp.minimal_polynomial(r1s, x); mp2 = sp.minimal_polynomial(r2s, x)
                rows.append((v1, v2, Gm.tolist(), r1s, r2s, mp1, mp2))
print("negative-definite pairs solved; isolated points with tau1, tau2 non-real:", len(rows))
for v1, v2, Gm, r1s, r2s, mp1, mp2 in rows:
    print("  K = %s, %s (Gram %s): tau1 = %s, tau2 = %s" % (v1, v2, Gm, r1s, r2s))
    print("        minimal polynomials: %s | %s" % (sp.factor(mp1), sp.factor(mp2)))
print("r7 exit 0")
