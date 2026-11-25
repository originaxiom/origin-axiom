"""B2000, listening card 15 (main, 2026-11-25; data-free): agy-exp's NI-1 and NI-3 checked on main's own code.
N1-N4: the moves' Jacobians at (0,0,0) and (3,3,3) (sympy, exact), read in the charge basis of the cyclic exchange C (B1994).
F1-F3: realisations of the common point in Q8, 2O, 2I (unit quaternions), two- and three-body collisions (A1A2, B1B2),
kappa = tr[A,B] = 2 Re(A B A^-1 B^-1) classified to the nearest of the nine levels (residual reported); fractions exact.
    python3 -B native.py > native_run.txt"""
import itertools
from fractions import Fraction as Fr
import numpy as np
import sympy as sp
x, y, z = sp.symbols("x y z")
MOVES = {"L": (x, z, x*z - y), "R": (z, y, y*z - x), "Li": (x, x*y - z, y), "Ri": (x*y - z, y, x)}
JAC = {k: sp.Matrix(v).jacobian([x, y, z]) for k, v in MOVES.items()}
C = sp.Matrix([[0, 1, 0], [0, 0, 1], [1, 0, 0]])           # Jacobian of the cyclic exchange (x,y,z) -> (y,z,x)
w = sp.exp(2 * sp.pi * sp.I / 3)
V = [sp.Matrix([1, w**q, w**(2*q)]) / sp.sqrt(3) for q in range(3)]   # charge basis: C v_q = w^q-conjugate eigen
for q in range(3):
    lam = sp.simplify((C * V[q])[0] / V[q][0]); assert sp.simplify(C * V[q] - lam * V[q]) == sp.zeros(3, 1)
U = sp.Matrix.hstack(*V)
def read(name, M):
    Mc = sp.simplify(U.H * M * U)
    diag = [sp.nsimplify(sp.simplify(Mc[i, i])) for i in range(3)]
    off = sp.sqrt(sum(abs(sp.N(Mc[i, j], 30))**2 for i in range(3) for j in range(3) if i != j))
    comm = sp.simplify(M * C - C * M)
    ev = sp.Matrix(M).eigenvals()
    print("%s: charge-basis diagonal (q = 0, 1, 2) %s; off-diagonal norm %s; commutes with C: %s; eigenvalues %s" % (
        name, diag, sp.N(off, 6), comm == sp.zeros(3, 3), {sp.nsimplify(k): v for k, v in ev.items()}))
    return diag, comm == sp.zeros(3, 3)
for pt in ((0, 0, 0), (3, 3, 3)):
    sub = dict(zip((x, y, z), pt)); J = {k: v.subs(sub) for k, v in JAC.items()}
    print("== at %s: images under L, R: %s, %s" % (pt, tuple(e.subs(sub) for e in MOVES["L"]), tuple(e.subs(sub) for e in MOVES["R"])))
    S2 = J["L"] + J["R"]; read("S2 = J_L + J_R", S2)
    S6 = sum((C**k * S2 * C**(-k) for k in range(3)), sp.zeros(3, 3)); read("S6 = sum_k C^k S2 C^-k", S6)
    S4 = J["L"] + J["R"] + J["Li"] + J["Ri"]; read("S4 = J_L + J_R + J_L^-1 + J_R^-1", S4)
    S12 = sum((C**k * S4 * C**(-k) for k in range(3)), sp.zeros(3, 3)); read("S12 = sum_k C^k S4 C^-k", S12)

# ---------------- F: collisions of the common point's realisations ----------------
phi = (1 + 5 ** 0.5) / 2
def qmul(a, b):
    a0, a1, a2, a3 = a[..., 0], a[..., 1], a[..., 2], a[..., 3]; b0, b1, b2, b3 = b[..., 0], b[..., 1], b[..., 2], b[..., 3]
    return np.stack([a0*b0 - a1*b1 - a2*b2 - a3*b3, a0*b1 + a1*b0 + a2*b3 - a3*b2, a0*b2 - a1*b3 + a2*b0 + a3*b1, a0*b3 + a1*b2 - a2*b1 + a3*b0], -1)
def conj(a): return a * np.array([1, -1, -1, -1])
def evenperms(v):
    out = []
    for p in itertools.permutations(range(4)):
        inv = sum(1 for i in range(4) for j in range(i + 1, 4) if p[i] > p[j])
        if inv % 2 == 0: out.append(tuple(v[p[i]] for i in range(4)))
    return out
def group(name):
    els = set()
    for i in range(4):
        for s in (1, -1):
            e = [0, 0, 0, 0]; e[i] = s; els.add(tuple(e))
    if name in ("2O", "2I"):
        for s in itertools.product((0.5, -0.5), repeat=4): els.add(s)
    if name == "2O":
        r = 2 ** -0.5
        for i, j in itertools.combinations(range(4), 2):
            for s1 in (r, -r):
                for s2 in (r, -r):
                    e = [0, 0, 0, 0]; e[i] = s1; e[j] = s2; els.add(tuple(e))
    if name == "2I":
        for s in itertools.product((1, -1), repeat=3):
            for v in evenperms((0, s[0] * 0.5, s[1] * 0.5 / phi, s[2] * 0.5 * phi)): els.add(tuple(round(c, 15) for c in v))
    return np.array(sorted(els))
LEVELS = [(-2, "-2"), (-phi, "-phi"), (-1, "-1"), (-1 / phi, "-1/phi"), (0, "0"), (1 / phi, "1/phi"), (1, "1"), (phi, "phi"), (2, "2")]
LV = np.array([l[0] for l in LEVELS])
def classify(kap):
    d = np.abs(kap[:, None] - LV[None, :]); idx = d.argmin(1); return idx, d.min(1).max()
def states(G):
    n = len(G); A, B = np.repeat(G, n, 0), np.tile(G, (n, 1)); AB = qmul(A, B)
    keep = (np.abs(A[:, 0]) < 1e-12) & (np.abs(B[:, 0]) < 1e-12) & (np.abs(AB[:, 0]) < 1e-12)
    return A[keep], B[keep]
def kappa(A, B): return 2 * qmul(qmul(A, B), qmul(conj(A), conj(B)))[:, 0]
def fractions(idx, total):
    c = np.bincount(idx, minlength=9); return {LEVELS[i][1]: Fr(int(c[i]), total) for i in range(9) if c[i]}
for name in ("Q8", "2O", "2I"):
    G = group(name); As, Bs = states(G); n = len(As)
    assert np.allclose(np.linalg.norm(G, axis=1), 1) and len({tuple(np.round(g, 9)) for g in G}) == len(G)
    i1, i2 = np.repeat(np.arange(n), n), np.tile(np.arange(n), n)
    idx, res = classify(kappa(qmul(As[i1], As[i2]), qmul(Bs[i1], Bs[i2])))
    print("F (%s): group order %d; realisations of the common point %d; two-body collisions %d; fractions %s; max residual %.1e" % (name, len(G), n, n * n, fractions(idx, n * n), res))
    if name == "2I":
        tot = Fr(0); counts = np.zeros(9, dtype=np.int64); worst = 0
        for a in range(n):
            P = qmul(np.repeat(As[a:a + 1], n * n, 0), qmul(As[i1], As[i2])); Q = qmul(np.repeat(Bs[a:a + 1], n * n, 0), qmul(Bs[i1], Bs[i2]))
            idx3, r3 = classify(kappa(P, Q)); counts += np.bincount(idx3, minlength=9); worst = max(worst, r3)
        N3 = n ** 3
        print("F3 (2I three-body, %d collisions): fractions in ascending level order %s = %s/%d; max residual %.1e" % (
            N3, [str(Fr(int(c), N3)) for c in counts], [int(c) * 225 // N3 if (int(c) * 225) % N3 == 0 else "%d/%d" % (c, N3) for c in counts], 225, worst))
