"""The explore seat, 2026-11-07: CHARGE OR SYMMETRY AT THE RAMIFIED PRIME (P-738) -- PREREGISTRATION_CHARGE_OR_SYMMETRY.md.
Data-free: SL(2, F5) arithmetic and its level-5 Weil representation (B355's convention R = T, L = S T^-1 S^-1). No frame
value, no data, no held-out quantity.
  G   HG: H = +-<LR> mod 5, its conjugacy to +-{[[1,b],[0,1]]}, the order of LR in PSL(2, F5)
  Q0  the Weil representation is projective (every element by two words; S^2 ~ parity)
  Q1  scalars: on C^5 and on each parity sector
  Q2  the commutant of rho(LR)
  Q3  the spectrum of rho(LR) on each sector; ratios; rho((LR)^a) scalar iff 5 | a
  Q4  the two least-action candidates (6) and (2,1,1,1,2)
    python3 charge_or_symmetry_check.py
"""
import cmath
import importlib.util
import itertools
import pathlib
import sys

import numpy as np

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sp = importlib.util.spec_from_file_location("least_action_check", HERE / "least_action_check.py")
LA = importlib.util.module_from_spec(sp)
sys.modules["least_action_check"] = LA
sp.loader.exec_module(LA)
D0 = LA.D0
N = 5
INV2 = 3  # 2^-1 mod 5
e = lambda z: cmath.exp(2j * cmath.pi * z)


def mm(X, Y):
    return (((X[0][0] * Y[0][0] + X[0][1] * Y[1][0]) % N, (X[0][0] * Y[0][1] + X[0][1] * Y[1][1]) % N),
            ((X[1][0] * Y[0][0] + X[1][1] * Y[1][0]) % N, (X[1][0] * Y[0][1] + X[1][1] * Y[1][1]) % N))


def red(X):
    return ((X[0][0] % N, X[0][1] % N), (X[1][0] % N, X[1][1] % N))


I2, NEG = ((1, 0), (0, 1)), ((N - 1, 0), (0, N - 1))
Lm, Rm = ((1, 0), (1, 1)), ((1, 1), (0, 1))
Sm = ((0, N - 1), (1, 0))
LRm = mm(Lm, Rm)
G_all = [((a, b), (c, d)) for a, b, c, d in itertools.product(range(N), repeat=4) if (a * d - b * c) % N == 1]

# ---- the Weil representation (B355's convention)
rT = np.diag([e(INV2 * x * x / N) for x in range(N)])
rS = np.array([[e(-x * y / N) for x in range(N)] for y in range(N)]) / np.sqrt(N)
rR = rT
rL = rS @ np.linalg.inv(rT) @ np.linalg.inv(rS)
PAR = np.zeros((N, N))
for x in range(N):
    PAR[(-x) % N, x] = 1


def proportional(A, B, tol=1e-9):
    k = np.unravel_index(np.argmax(abs(B)), B.shape)
    if abs(B[k]) < tol:
        return False, None
    c = A[k] / B[k]
    return np.allclose(A, c * B, atol=tol), c


def is_scalar(A, tol=1e-9):
    return proportional(A, np.eye(A.shape[0]), tol)[0]


# BFS over words in L, R; every element reached, with consistency checks for repeated arrivals
rho = {I2: np.eye(N, dtype=complex)}
frontier, clashes, checks = [I2], 0, 0
while frontier:
    nxt = []
    for g in frontier:
        for M, rM in ((Lm, rL), (Rm, rR)):
            h = mm(g, M)
            mat = rho[g] @ rM
            if h in rho:
                checks += 1
                ok, _ = proportional(mat, rho[h])
                clashes += 0 if ok else 1
            else:
                rho[h] = mat
                nxt.append(h)
    frontier = nxt

# the parity sectors
even = np.array([[1, 0, 0, 0, 0], [0, 1, 0, 0, 1], [0, 0, 1, 1, 0]], dtype=complex).T
odd = np.array([[0, 1, 0, 0, -1], [0, 0, 1, -1, 0]], dtype=complex).T
even /= np.linalg.norm(even, axis=0)
odd /= np.linalg.norm(odd, axis=0)


def restrict(A, B):
    return B.conj().T @ A @ B


if __name__ == "__main__":
    print("CHARGE OR SYMMETRY AT THE RAMIFIED PRIME -- data-free check (the explore seat, 2026-11-07)")

    print("\nG. HG -- the object's own level-5 group")
    H, P = set(), I2
    for k in range(20):
        H.add(P)
        H.add(mm(NEG, P))
        P = mm(P, LRm)
    upper = {((1, b), (0, 1)) for b in range(N)} | {mm(NEG, ((1, b), (0, 1))) for b in range(N)}
    conj = [g for g in G_all if {mm(mm(g, h), ((g[1][1], -g[0][1] % N), (-g[1][0] % N, g[0][0]))) for h in H} == upper]
    ordPSL = next(k for k in range(1, 61) if (lambda Q: Q in (I2, NEG))(
        __import__("functools").reduce(lambda A, B: mm(A, B), [LRm] * k, I2)))
    print("  |H| = %d; conjugate to +-{[[1,b],[0,1]]} (the image of +-Gamma1(5)): %s (%d conjugators); ord(LR) in PSL(2,F5) = %d" % (
        len(H), len(conj) > 0, len(conj), ordPSL))

    print("\nQ0. the Weil representation is projective")
    print("  elements reached: %d of %d; repeated arrivals checked: %d; clashes (not proportional): %d" % (
        len(rho), len(G_all), checks, clashes))
    print("  rho(S)^2 proportional to parity: %s; rho(-I) proportional to parity: %s" % (
        proportional(rS @ rS, PAR)[0], proportional(rho[NEG], PAR)[0]))

    print("\nQ1. scalars")
    sc_full = sorted(g for g in G_all if is_scalar(rho[g]))
    sc_even = sorted(g for g in G_all if is_scalar(restrict(rho[g], even)))
    sc_odd = sorted(g for g in G_all if is_scalar(restrict(rho[g], odd)))
    print("  scalar on C^5: %s" % sc_full)
    print("  scalar on the even sector (dim 3): %s" % sc_even)
    print("  scalar on the odd sector (dim 2): %s" % sc_odd)
    print("  HQ1 (C^5: only I; each sector: exactly +-I): %s" % (sc_full == [I2] and set(sc_even) == {I2, NEG} and set(sc_odd) == {I2, NEG}))

    print("\nQ2. the commutant of rho(LR)")
    rLR = rho[LRm]
    comm = sorted(g for g in G_all if proportional(rho[g] @ rLR @ np.linalg.inv(rho[g]), rLR)[0])
    print("  |{E : rho(E) rho(LR) rho(E)^-1 ~ rho(LR)}| = %d; equals +-<LR>: %s" % (len(comm), set(comm) == H))

    print("\nQ3. the tick on each sector")
    hq3 = True
    for name, B in (("even", even), ("odd", odd)):
        ev = np.linalg.eigvals(restrict(rLR, B))
        angs = sorted((cmath.phase(z) / (2 * cmath.pi)) % 1 for z in ev)
        ratios = []
        for i, j in itertools.combinations(range(len(ev)), 2):
            r = ev[i] / ev[j]
            k = round(5 * (cmath.phase(r) / (2 * cmath.pi)) % 5) % 5
            ratios.append((k, abs(r - e(k / 5)) < 1e-9))
        distinct = all(abs(ev[i] - ev[j]) > 1e-9 for i, j in itertools.combinations(range(len(ev)), 2))
        prim = all(ok and k % 5 != 0 for k, ok in ratios)
        hq3 &= distinct and prim
        powers = [a for a in range(10) if is_scalar(restrict(np.linalg.matrix_power(rLR, a), B))]
        print("  %s sector: eigenvalue angles (turns) %s; distinct: %s; ratios as 5th-root exponents %s; all primitive: %s" % (
            name, ["%.4f" % a for a in angs], distinct, ratios, prim))
        print("     rho((LR)^a) scalar on this sector for a in 0..9: %s" % powers)
    print("  HQ3 (distinct, every ratio a primitive 5th root, in every sector): %s" % hq3)

    print("\nQ4. the two least-action candidates")
    for runs in ((6,), (2, 1, 1, 1, 2)):
        E = red(D0.mul(LA.mat(runs), D0.inv(LA.mat([1] * len(runs)))))
        a = next((k for k in range(10) if (lambda Q: Q == E or mm(NEG, Q) == E)(
            __import__("functools").reduce(lambda A, B: mm(A, B), [LRm] * k, I2))), None)
        rE = rho[E]
        on_eig = []
        w, V = np.linalg.eig(rLR)
        for col in V.T:
            v2 = rE @ col
            k = np.argmax(abs(col))
            on_eig.append(np.allclose(v2, (v2[k] / col[k]) * col, atol=1e-9))
        print("  %-16s E mod 5 = %s; golden phase a = %s; scalar on C^5: %s; on even: %s; on odd: %s; a phase on every eigenvector of rho(LR): %s" % (
            runs, E, a, is_scalar(rE), is_scalar(restrict(rE, even)), is_scalar(restrict(rE, odd)), all(on_eig)))
    print("\ncharge_or_symmetry_check exit 0")
