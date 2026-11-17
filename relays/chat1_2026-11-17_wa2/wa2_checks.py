#!/usr/bin/env python3
"""W-A2 (card relays/cards/CHAT1_W-A2_deriving_postulate_d.md, e9f999307): postulate D from the ground, or not.
Algebra and theta series only; no frame output; no data.

    python3 -I -u wa2_checks.py

A  the lines of F_p^2 fixed by the act LR = [[2, 1], [1, 1]], every prime p < 60.
B  p = 5: Weyl operators W(a, b) = X^a Z^b (X|j> = |j+1>, Z = diag(zeta^j)); HS-orthogonality; XZ = zeta^-1 ZX; the
   Weil representation rho of W-A1 (rho(T) = diag(psi(2x^2)), rho(S) = -F, F_xy = psi(xy)/sqrt 5) conjugates W(v) to a
   phase times W(M_g v); M_g for S, T, -I; a linear identification phi of F_5^2 with phi M_g phi^-1 = R_g (or R_g^-1)
   for the record's transport R_T (a, b) -> (a, b - a), R_S (a, b) -> (-b, a) (B1724).
C  the flux-5 zero modes psi_j(u, tau) = sum_n exp(pi i 5 tau (n + j/5)^2 + 2 pi i 5 u (n + j/5)), j = 0..4: degree-5
   quasi-periodicity; u -> u + 1/5 acts as Z, u -> u + tau/5 as X times a factor common to all j; u -> -u maps psi_j to
   psi_{-j} (parity), so even and odd dimensions 3 and 2; independence.
D  the frame's generation triplet (B1724's triplet; T = W-F22's hand matrix [[w, 0, 0], [0, 0, w], [0, w^-3, 0]],
   w = e^{i pi/4}; S exchanging components 1 and 2): T-eigenphases against the Weil 3's (rho(T) on the even part); the
   permutation parts of T and S generate S_3 = SL(2, F_2) on three points; the frame's quaternion units {1, Q_I, Q_J,
   Q_K} (W-F22's transcription) are HS-orthogonal, square to -1 and anticommute pairwise (the level-2 Weyl operators up
   to phases).
E  the rivals p = 3, 7, 11, 13 (and 5): a Weil representation of SL(2, F_p) on C^p found by the same search (kernel
   psi(m x y), m in F_p*); rho(-I)'s split; the commutant's dimension; the group S(U(m) x U(n)); the U(1) anomalies
   (sum Y, sum Y^3, SU(m)^2 Y, SU(n)^2 Y) of Lambda^even(C^p) under the traceless commutant element; A's count.

EXPECTATIONS and FAILURE CRITERIA: as the card (e9f999307). A: exactly one fixed line at p = 5 only. F1 to F5 do not hold.
"""
import itertools
import math
import os
from fractions import Fraction as Fr
from math import comb

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))


def say(*a):
    print(*a, flush=True)


def primes(n):
    return [p for p in range(2, n) if all(p % d for d in range(2, int(p ** 0.5) + 1))]


# ---------------- A
def act_fixed_lines(p):
    M = ((2, 1), (1, 1))
    pts = [(1, x) for x in range(p)] + [(0, 1)]
    cnt = 0
    for v in pts:
        w = ((M[0][0] * v[0] + M[0][1] * v[1]) % p, (M[1][0] * v[0] + M[1][1] * v[1]) % p)
        if (w[0] * v[1] - w[1] * v[0]) % p == 0:
            cnt += 1
    return cnt


# ---------------- Weil representations of SL(2, F_p)
def sl2(p):
    return [(a, b, c, d) for a in range(p) for b in range(p) for c in range(p) for d in range(p) if (a * d - b * c) % p == 1]


def mul(g, h, p):
    a, b, c, d = g
    e, f, g2, h2 = h
    return ((a * e + b * g2) % p, (a * f + b * h2) % p, (c * e + d * g2) % p, (c * f + d * h2) % p)


def try_rep(rS, rT, p):
    GS, GT, I2 = (0, p - 1, 1, 0), (1, 1, 0, 1), (1, 0, 0, 1)
    rho = {I2: np.eye(p, dtype=complex)}
    todo = [I2]
    while todo:
        g = todo.pop()
        for gen, rg in ((GS, rS), (GT, rT)):
            h = mul(g, gen, p)
            M = rho[g] @ rg
            if h in rho:
                if np.max(np.abs(rho[h] - M)) > 1e-8:
                    return None
            else:
                rho[h] = M
                todo.append(h)
    return rho if len(rho) == p * (p * p - 1) else None


def weil(p, prefer=None):
    w = np.exp(2j * np.pi / p)
    X = np.arange(p)
    for k in ([prefer[0]] if prefer else range(1, p)):
        rT = np.diag(w ** ((k * X * X) % p))
        for m in ([prefer[1]] if prefer else range(1, p)):
            F = w ** ((m * np.outer(X, X)) % p) / np.sqrt(p)
            for c in (1, -1, 1j, -1j):
                rho = try_rep(c * F, rT, p)
                if rho is not None:
                    return (k, m, c), rho
    return None, None


def nullspace(A, tol=1e-9):
    u, s, vh = np.linalg.svd(A)
    return vh[int(np.sum(s > tol)):].conj().T


def commutant_dim(mats, p):
    rows = [np.kron(np.eye(p), M.T) - np.kron(M, np.eye(p)) for M in mats]
    return nullspace(np.vstack(rows)).shape[1]


# ---------------- B
def part_B():
    p = 5
    zeta = np.exp(2j * np.pi / p)
    X = np.zeros((p, p), dtype=complex)
    for j in range(p):
        X[(j + 1) % p, j] = 1
    Z = np.diag(zeta ** np.arange(p))
    Wop = {(a, b): np.linalg.matrix_power(X, a) @ np.linalg.matrix_power(Z, b) for a in range(p) for b in range(p)}
    G = np.array([[np.trace(Wop[u].conj().T @ Wop[v]) for v in Wop] for u in Wop])
    ortho = np.max(np.abs(G - p * np.eye(p * p))) < 1e-9
    heis = np.max(np.abs(X @ Z - zeta ** -1 * Z @ X)) < 1e-12
    (k, m, c), rho = weil(5, prefer=(2, 1))
    gens = {"S": (0, 4, 1, 0), "T": (1, 1, 0, 1), "-I": (4, 0, 0, 4)}
    Mg, lin = {}, True
    for name, g in gens.items():
        R = rho[g]
        img = {}
        for v, Wv in Wop.items():
            C = R @ Wv @ np.linalg.inv(R)
            best = max(Wop, key=lambda u: abs(np.trace(Wop[u].conj().T @ C)))
            if abs(abs(np.trace(Wop[best].conj().T @ C)) - p) > 1e-8:
                lin = False
            img[v] = best
        A = np.array([[img[(1, 0)][0], img[(0, 1)][0]], [img[(1, 0)][1], img[(0, 1)][1]]]) % p
        for v in Wop:
            lin &= tuple(int(x) for x in (A @ np.array(v)) % p) == img[v]
        Mg[name] = A
    Rrec = {"S": np.array([[0, 4], [1, 0]]), "T": np.array([[1, 0], [4, 1]]), "-I": np.array([[4, 0], [0, 4]])}
    inv5 = lambda A: (np.round(np.linalg.inv(A) * round(np.linalg.det(A))) * pow(int(round(np.linalg.det(A))) % 5, -1, 5)) % 5
    found = {}
    for variant in ("R_g", "R_g^-1"):
        for e in itertools.product(range(5), repeat=4):
            phi = np.array([[e[0], e[1]], [e[2], e[3]]])
            if int(round(np.linalg.det(phi))) % 5 == 0:
                continue
            pinv = inv5(phi)
            ok = True
            for name in ("S", "T"):
                target = Rrec[name] if variant == "R_g" else inv5(Rrec[name])
                ok &= np.array_equal((phi @ Mg[name] @ pinv) % 5, target % 5)
            if ok:
                found[variant] = phi.tolist()
                break
    say("B: Weyl operators HS-orthogonal (25):", ortho, "| XZ = zeta^-1 ZX:", heis, "| rho (k, m, c) =", (k, m, c))
    say("   conjugation by rho maps W(v) to a phase times W(M_g v), M_g linear on all 25:", lin)
    for name, A in Mg.items():
        say("   M_%s = %s" % (name, A.tolist()))
    say("   identification phi with phi M_g phi^-1 = the record's transport:", found if found else "none")
    f4 = (not lin) or (not found)
    say("F4 holds (the record's lines are not W's operators):", f4)
    return rho, f4


# ---------------- C
def part_C():
    tau = complex(0.13, 1.1)
    us = [complex(0.07, 0.11), complex(-0.23, 0.31), complex(0.31, -0.17), complex(0.02, 0.43), complex(-0.4, -0.05)]
    NK = 30

    def psi(j, u):
        n = np.arange(-NK, NK + 1)
        m = n + j / 5
        return np.sum(np.exp(1j * np.pi * 5 * tau * m * m + 2j * np.pi * 5 * u * m))

    ok_per = ok_Z = ok_X = ok_par = True
    for u in us:
        fX = np.exp(-1j * np.pi * tau / 5 - 2j * np.pi * u)
        for j in range(5):
            a = psi(j, u)
            ok_per &= abs(psi(j, u + 1) - a) < 1e-9 * abs(a) and \
                abs(psi(j, u + tau) - np.exp(-5j * np.pi * tau - 10j * np.pi * u) * a) < 1e-8 * abs(psi(j, u + tau))
            ok_Z &= abs(psi(j, u + 0.2) - np.exp(2j * np.pi * j / 5) * a) < 1e-9 * abs(a)
            ok_X &= abs(psi(j, u + tau / 5) - fX * psi((j + 1) % 5, u)) < 1e-9 * abs(psi(j, u + tau / 5))
            ok_par &= abs(psi(j, -u) - psi((-j) % 5, u)) < 1e-9 * abs(a)
    Mx = np.array([[psi(j, u) for j in range(5)] for u in us])
    rank = np.linalg.matrix_rank(Mx, tol=1e-9 * np.max(np.abs(Mx)))
    P = np.zeros((5, 5))
    for j in range(5):
        P[(-j) % 5, j] = 1
    ev = np.round(np.linalg.eigvals(P).real).astype(int).tolist()
    split = (ev.count(1), ev.count(-1))
    say("C: degree-5 quasi-periodicity:", ok_per, "| u + 1/5 acts as Z:", ok_Z, "| u + tau/5 acts as X (common factor):", ok_X,
        "| u -> -u maps psi_j to psi_-j:", ok_par, "| rank:", rank, "| parity split (even, odd):", split)
    f5 = not (ok_per and ok_Z and ok_X and ok_par and rank == 5 and split == (3, 2))
    say("F5 holds (the flux-5 zero modes fail):", f5)
    return f5


# ---------------- D
def part_D(rho5):
    w = np.exp(1j * np.pi / 4)
    T3 = np.array([[w, 0, 0], [0, 0, w], [0, w ** -3, 0]])
    S3 = np.array([[0, 1, 0], [1, 0, 0], [0, 0, 1]], dtype=complex)
    ph_frame = sorted((np.angle(np.linalg.eigvals(T3)) / (2 * np.pi)) % 1)
    P = rho5[(4, 0, 0, 4)]
    Ev = nullspace(P - np.eye(5))
    T5 = Ev.conj().T @ rho5[(1, 1, 0, 1)] @ Ev
    ph_weil = sorted((np.angle(np.linalg.eigvals(T5)) / (2 * np.pi)) % 1)
    order = lambda phs: min(n for n in range(1, 200) if all(abs((n * x) - round(n * x)) < 1e-9 for x in phs))
    o_frame, o_weil = order(ph_frame), order(ph_weil)
    perm = lambda M: tuple(int(np.argmax(np.abs(M[:, j]))) for j in range(3))
    pT, pS = perm(T3), perm(S3)
    grp = {(0, 1, 2)}
    frontier = [(0, 1, 2)]
    while frontier:
        g = frontier.pop()
        for h in (pT, pS):
            c = tuple(h[g[i]] for i in range(3))
            if c not in grp:
                grp.add(c)
                frontier.append(c)
    D = os.path.join(os.path.dirname(HERE), "chat1_2026-11-14_wf22")
    src = open(os.path.join(D, "wf22_outputs.py")).read()
    ns = {"__file__": os.path.join(D, "wf22_outputs.py")}
    exec(src[:src.index("def dev(x, y):")], ns)
    Q = [np.eye(2), ns["QI"], ns["QJ"], ns["QK"]]
    G = np.array([[np.trace(a.conj().T @ b) for b in Q] for a in Q])
    ortho = np.max(np.abs(G - 2 * np.eye(4))) < 1e-12
    sq = all(np.max(np.abs(q @ q + np.eye(2))) < 1e-12 for q in Q[1:])
    anti = all(np.max(np.abs(Q[i] @ Q[j] + Q[j] @ Q[i])) < 1e-12 for i in (1, 2, 3) for j in (1, 2, 3) if i < j)
    say("D: the frame's triplet T-eigenphases %s (level %d) | the Weil 3's %s (level %d)" % (
        [round(x, 6) for x in ph_frame], o_frame, [round(x, 6) for x in ph_weil], o_weil))
    say("   permutation parts T %s, S %s generate a group of order %d (S_3 = SL(2, F_2) on three points: %s)" % (
        pT, pS, len(grp), len(grp) == 6))
    say("   quaternion units: HS-orthogonal %s, square to -1 %s, anticommute pairwise %s (level-2 Weyl operators up to phases)" % (
        ortho, sq, anti))
    f3 = (ph_frame == ph_weil) or (math.gcd(o_frame, o_weil) != 1 and o_frame == o_weil)
    say("F3 holds (families and colour collide):", f3)
    return f3


# ---------------- E
def lam_content(m, n, ym, yn):
    out = []
    for k in range(0, m + n + 1, 2):
        for i in range(0, min(k, m) + 1):
            j = k - i
            if j > n:
                continue
            out.append((i, j, comb(m, i) * comb(n, j), i * ym + j * yn))
    return out


def dynkin_lambda(N, i):
    return Fr(comb(N - 2, i - 1), 2) if 1 <= i <= N - 1 else Fr(0)


def part_E():
    rows = {}
    for p in (3, 5, 7, 11, 13):
        params, rho = weil(p)
        P = rho[(p - 1, 0, 0, p - 1)]
        ev = np.round(np.linalg.eigvals(P).real).astype(int).tolist()
        dims = sorted((ev.count(1), ev.count(-1)), reverse=True)
        cd = commutant_dim([rho[(0, p - 1, 1, 0)], rho[(1, 1, 0, 1)]], p)
        m, n = dims
        ym, yn = Fr(n), Fr(-m)
        cont = lam_content(m, n, ym, yn)
        sY = sum(Fr(d) * y for i, j, d, y in cont)
        sY3 = sum(Fr(d) * y ** 3 for i, j, d, y in cont)
        sm = sum(dynkin_lambda(m, i) * comb(n, j) * y for i, j, d, y in cont)
        sn = sum(dynkin_lambda(n, j) * comb(m, i) * y for i, j, d, y in cont)
        sm_group = (m, n) == (3, 2)
        rows[p] = dict(params=params, split=dims, commutant=cd, group="S(U(%d) x U(%d))" % (m, n),
                       anomalies=(str(sY), str(sY3), str(sm), str(sn)), act_lines=act_fixed_lines(p), sm=sm_group)
        say("E: p %2d  Weil (k, m, c) %s  split %s  commutant %d  group %s  anomalies (sumY, sumY3, SU(m)^2Y, SU(n)^2Y) %s"
            "  act's fixed lines %d  SU(3) x SU(2) x U(1): %s" % (p, params, dims, cd, rows[p]["group"], rows[p]["anomalies"],
                                                                 rows[p]["act_lines"], sm_group))
    f2 = any(r["sm"] for q, r in rows.items() if q != 5)
    say("F2 holds (a rival gives SU(3) x SU(2) x U(1)):", f2)
    return f2


def main():
    A = {p: act_fixed_lines(p) for p in primes(60)}
    ones = [p for p, c in A.items() if c == 1]
    say("A: lines fixed by the act mod p:", A)
    say("   primes with exactly one fixed line:", ones)
    f1 = ones != [5]
    say("F1 holds (a prime other than 5 has exactly one fixed line, or 5 does not):", f1)
    rho5, f4 = part_B()
    f5 = part_C()
    f3 = part_D(rho5)
    f2 = part_E()
    say("FAILURE CRITERIA: F1 %s, F2 %s, F3 %s, F4 %s, F5 %s" % (f1, f2, f3, f4, f5))


if __name__ == "__main__":
    main()
