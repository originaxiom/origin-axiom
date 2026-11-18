"""B1957: the physical lane's package 'physical transverse response' (P-C3c, 2026-11-16): the finite algebra of its
three hand proofs, rebuilt on main.  Nothing of the lane's is run.  The analysis (normalisable dual modes on the
complete surface, the nonlinear two-jet topology, the classical reduction's domain statements) is not verified here.
 T1  the protected quartic: from the cubic W = y A t+ t- the three F components are y t+ t-, y A t-, y A t+, and with the
     moment e (|t+|^2 - |t-|^2):  |y|^2 x z + (e^2/2)(x - z)^2 = (|y|^2/4)(x + z)^2 + (e^2/2 - |y|^2/4)(x - z)^2, so for
     |y|^2 >= 2 e^2 the sum is at least (e^2/2)(x + z)^2 (random values); for |y|^2 < 2 e^2 it can be smaller.
 T2  the projection bound: for a linear L and any B, |L beta + B|^2 >= |P B|^2 with P the projection on the orthogonal
     complement of the range, with equality reached (a finite model with a non-surjective L).
 T3  the potential's Hessian: for V = |R|^2, half of D^2 V (Y, Z) = <DR Y, DR Z> + <R, D^2 R (Y, Z)> (a random quadratic R).
 T4  the centraliser of the colour A2 in E8: the roots orthogonal to every colour root number 40 + 32 = 72; the note's
     six simple roots have the E6 Cartan matrix (determinant 3); no colour root added to a singlet half-root is a root;
     the grading by Q = (2/3)(e1 + e2 + e3) is 40 at 0, 16 at +1, 16 at -1; the other half-roots have Q = +-1/3; the
     roots +-e_i +- e_j on the first three coordinates have Q in {0, +-4/3}.
 T5  the character table of the neutral subgroup: an element of Pin(2) about the axis k has the character +1 if it is
     a rotation and -1 if it is a reflection; on the three state axes, at (a, b) -> (i, j) conjugated back by the
     representatives, the signs are (-1, -1), (-1, +1), (+1, -1)."""
import functools, itertools, math
from fractions import Fraction as Fr
import numpy as np
import sympy as sp
print = functools.partial(print, flush=True)
I2 = np.eye(2, dtype=complex); qi = np.array([[1j, 0], [0, -1j]]); qj = np.array([[0, 1], [-1, 0]], dtype=complex); qk = qi @ qj

if __name__ == "__main__":
    rng = np.random.default_rng(44)
    y, e, x, z = sp.symbols("y e x z", positive=True)
    ident = sp.expand(y ** 2 * x * z + e ** 2 / 2 * (x - z) ** 2 - (y ** 2 / 4 * (x + z) ** 2 + (e ** 2 / 2 - y ** 2 / 4) * (x - z) ** 2))
    worst = np.inf; fail = False
    for _ in range(20000):
        ev = abs(rng.normal()) + 0.1; yv = math.sqrt(2) * ev * (1 + abs(rng.normal())); xv, zv, Av = abs(rng.normal()), abs(rng.normal()), abs(rng.normal())
        full = yv ** 2 * (xv * zv + Av ** 2 * (xv + zv)) + ev ** 2 / 2 * (xv - zv) ** 2; low = ev ** 2 / 2 * (xv + zv) ** 2 + yv ** 2 * Av ** 2 * (xv + zv); worst = min(worst, full - low)
        ys = 0.5 * math.sqrt(2) * ev; fail |= ys ** 2 * xv * zv + ev ** 2 / 2 * (xv - zv) ** 2 < ev ** 2 / 2 * (xv + zv) ** 2 - 1e-12
    A, tp, tm = sp.symbols("A t_plus t_minus"); W = y * A * tp * tm
    print("T1: the gradient of the cubic: %s; the identity: %s; over 20,000 random draws with |y|^2 >= 2 e^2 the least value of (the bound's left side minus its right side) is %.2e; with |y|^2 = e^2/2 the bound fails somewhere: %s" % ([sp.diff(W, v) for v in (A, tp, tm)], ident == 0, worst, fail))
    L = rng.normal(size=(7, 4)); Bv = rng.normal(size=7); U_, s_, _ = np.linalg.svd(L); P = np.eye(7) - U_[:, :4] @ U_[:, :4].T; least = np.linalg.lstsq(L, -Bv, rcond=None)
    vals = [np.linalg.norm(L @ rng.normal(size=4) * 3 + Bv) ** 2 for _ in range(2000)]
    print("T2: |P B|^2 = %.6f; the least of |L beta + B|^2 over 2,000 random beta: %.6f; at the least-squares beta: %.6f" % (np.linalg.norm(P @ Bv) ** 2, min(vals), np.linalg.norm(L @ least[0] + Bv) ** 2))
    n, m = 5, 6; R0 = rng.normal(size=m); R1 = rng.normal(size=(m, n)); R2 = rng.normal(size=(m, n, n)); R2 = (R2 + R2.transpose(0, 2, 1)) / 2
    Rf = lambda X: R0 + R1 @ X + np.einsum("mij,i,j->m", R2, X, X); Vf = lambda X: Rf(X) @ Rf(X); X0, Y, Z = rng.normal(size=n), rng.normal(size=n), rng.normal(size=n); h = 1e-4
    num = (Vf(X0 + h * Y + h * Z) - Vf(X0 + h * Y - h * Z) - Vf(X0 - h * Y + h * Z) + Vf(X0 - h * Y - h * Z)) / (4 * h * h)
    DR = lambda X, Yv: R1 @ Yv + 2 * np.einsum("mij,i,j->m", R2, X, Yv); form = DR(X0, Y) @ DR(X0, Z) + Rf(X0) @ (2 * np.einsum("mij,i,j->m", R2, Y, Z))
    print("T3: half of D^2 V (Y, Z) numerically %.6f; <DR Y, DR Z> + <R, D^2 R (Y, Z)> = %.6f" % (num / 2, form))
    # T4
    roots = set()
    for i, j in itertools.combinations(range(8), 2):
        for si in (1, -1):
            for sj in (1, -1):
                v = [Fr(0)] * 8; v[i] = Fr(si); v[j] = Fr(sj); roots.add(tuple(v))
    for signs in itertools.product((1, -1), repeat=8):
        if sum(1 for s in signs if s < 0) % 2 == 0: roots.add(tuple(Fr(s, 2) for s in signs))
    assert len(roots) == 240
    dot = lambda a, b: sum(p * q for p, q in zip(a, b)); colour = [r for r in roots if all(c == 0 for c in r[3:]) and sum(r[:3]) == 0]
    single = [r for r in roots if all(dot(r, c) == 0 for c in colour)]; half = [r for r in single if r[0].denominator == 2]; integ = [r for r in single if r[0].denominator == 1]
    Qv = lambda r: Fr(2, 3) * (r[0] + r[1] + r[2]); from collections import Counter
    grade = Counter(Qv(r) for r in single); others = Counter(Qv(r) for r in roots if r not in set(single) and r[0].denominator == 2); a3 = Counter(Qv(r) for r in roots if all(c == 0 for c in r[3:]))
    e_ = lambda i: tuple(Fr(int(k == i - 1)) for k in range(8)); sub = lambda a, b: tuple(p - q for p, q in zip(a, b)); add = lambda a, b: tuple(p + q for p, q in zip(a, b))
    simple = [sub(e_(4), e_(5)), sub(e_(5), e_(6)), sub(e_(6), e_(7)), sub(e_(7), e_(8)), add(e_(7), e_(8)), tuple(Fr(-1, 2) for _ in range(8))]
    Cm = sp.Matrix(6, 6, lambda i, j: dot(simple[i], simple[j])); edges = sorted((i + 1, j + 1) for i in range(6) for j in range(i + 1, 6) if Cm[i, j] == -1)
    noadd = all(add(hr, c) not in roots for hr in half for c in colour)
    print("T4: colour roots %d; roots orthogonal to all of them: %d (%d integer, %d half-integer); the simple roots are among them: %s; their edges %s and Cartan determinant %s; no colour root added to a singlet half-root is a root: %s; the grading by Q: %s; the other half-roots: %s; the roots on the first three coordinates: %s" % (
        len(colour), len(single), len(integ), len(half), all(s in set(single) for s in simple), edges, Cm.det(), noadd, {str(k): v for k, v in sorted(grade.items())}, {str(k): v for k, v in sorted(others.items())}, {str(k): v for k, v in sorted(a3.items())}))
    # T5
    def chi(g):
        # g in Pin(2) about k: a rotation commutes with k, a reflection anticommutes with it
        if np.allclose(g @ qk, qk @ g): return 1
        if np.allclose(g @ qk, -qk @ g): return -1
        return None
    reps = {"k": I2, "j": (I2 + qi) / np.sqrt(2), "i": (I2 - qj) / np.sqrt(2)}
    print("T5: the character on (a, b) at the three state axes: %s" % {ax: (chi(np.linalg.inv(g) @ qi @ g), chi(np.linalg.inv(g) @ qj @ g)) for ax, g in reps.items()})
