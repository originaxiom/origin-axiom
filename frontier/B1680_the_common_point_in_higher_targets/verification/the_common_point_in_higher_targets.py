#!/usr/bin/env python3
"""THE COMMON POINT IN TARGETS OF HIGHER RANK (P-209). B1679 settled SL(2, C): a non-trivial character of F_n fixed by
every move exists only at n = 2. Here the target is U(m), m = 3 or 5, with finite irreducible images.

A common point: a representation rho of F_n onto a finite irreducible subgroup G of U(m) such that for every move
phi (R_ij: a_i -> a_i a_j and L_ij: a_i -> a_j a_i, i != j) rho o phi is equivalent to rho -- tested EXACTLY by
solving for an intertwiner h with h rho(phi(a_k)) = rho(a_k) h for every k (Schur: a one-dimensional solution space,
h invertible). Search: every n-tuple of G that passes the exact necessary filter of W109's steps 1-3, valid in any
rank (tr g_i = tr g_i g_j = tr g_i g_j^-1 = tr g_i g_j g_k = t for distinct i, j, k), and generates G.

Targets (as matrices): the Heisenberg groups H(3) in U(3) and H(5) in U(5) (clock and shift); the rotation groups
A4, S4, A5 in SO(3) (from 2T, 2O, 2I by the adjoint action); Delta(54) in SU(3); Klein's 168-element group PSL(2, 7) in
SU(3); and the SU(2) controls Q8 and 2T. n = 2, 3, and n = 4 for the groups of order <= 60; H(5) at n = 2 only (a control; at n >= 3
the Sp(2) argument decides the Heisenberg family, and H(3) carries the census there).

Cells (sealed): C0 (n = 2) H(3) and H(5) have a common point (Stone-von Neumann), and Q8 has the quaternion point;
C1 (n = 3) no target has a common point; C2 (n = 4) none; the bite names any found. Writes the_common_point_in_higher_targets.json."""
import itertools, json, pathlib, time
import numpy as np

def close(gens, cap=2000):
    m = gens[0].shape[0]
    def key(x): return tuple(np.round(x, 8).ravel().view(float) + 0.0)
    I = np.eye(m, dtype=complex); G = {key(I): I}; frontier = [I]
    while frontier and len(G) <= cap:
        x = frontier.pop()
        for g in gens:
            y = x @ g; k = key(y)
            if k not in G: G[k] = y; frontier.append(y)
    return list(G.values())

def heis(p):
    w = np.exp(2j * np.pi / p)
    X = np.roll(np.eye(p, dtype=complex), 1, axis=0); Z = np.diag([w ** k for k in range(p)])
    return close([X, Z])

def quat_group(gens):                                         # unit quaternions -> 2x2 SU(2) matrices
    def q2m(q):
        a, b, c, d = q
        return np.array([[a + 1j * b, c + 1j * d], [-c + 1j * d, a - 1j * b]], dtype=complex)
    return close([q2m(g) for g in gens])

def adjoint(G2):                                              # SU(2) -> SO(3) via the Pauli basis
    P = [np.array([[0, 1], [1, 0]]), np.array([[0, -1j], [1j, 0]]), np.array([[1, 0], [0, -1]])]
    out = {}
    for g in G2:
        R = np.array([[0.5 * np.trace(P[i] @ g @ P[j] @ g.conj().T).real for j in range(3)] for i in range(3)], dtype=complex)
        out[tuple(np.round(R, 8).ravel().view(float) + 0.0)] = R
    return list(out.values())

def targets():
    h = 0.5; s = 1 / np.sqrt(2); ph = (1 + 5 ** 0.5) / 2
    Q8 = quat_group([(0, 1, 0, 0), (0, 0, 1, 0)])
    T2 = quat_group([(h, h, h, h), (0, 1, 0, 0)])
    O2 = quat_group([(h, h, h, h), (s, s, 0, 0)])
    I2 = quat_group([(h, h, h, h), (0, 0.5, ph / 2, 1 / (2 * ph))])
    w = np.exp(2j * np.pi / 3)
    shift = np.roll(np.eye(3, dtype=complex), 1, axis=0)
    D54 = close([shift, -np.array([[0, 1, 0], [1, 0, 0], [0, 0, 1]], dtype=complex), np.diag([w, w ** 2, 1])])
    z = np.exp(2j * np.pi / 7)
    a, b, c = z ** 4 - z ** 3, z ** 2 - z ** 5, z - z ** 6
    S = (1j / np.sqrt(7)) * np.array([[a, b, c], [b, c, a], [c, a, b]]); T = np.diag([z, z ** 2, z ** 4])
    K168 = close([S, T])
    return {"Q8 (SU2)": Q8, "2T (SU2)": T2, "H(3) (U3)": heis(3), "H(5) (U5)": heis(5), "A4 (SO3)": adjoint(T2),
            "S4 (SO3)": adjoint(O2), "A5 (SO3)": adjoint(I2), "Delta54 (SU3)": D54, "PSL27 (SU3)": K168}

EXPECTED = {"Q8 (SU2)": 8, "2T (SU2)": 24, "H(3) (U3)": 27, "H(5) (U5)": 125, "A4 (SO3)": 12, "S4 (SO3)": 24,
            "A5 (SO3)": 60, "Delta54 (SU3)": 54, "PSL27 (SU3)": 168}

def moves(n):
    for i in range(n):
        for j in range(n):
            if i != j: yield ("R", i, j); yield ("L", i, j)

def apply(tup, mv):
    side, i, j = mv; t = list(tup)
    t[i] = tup[i] @ tup[j] if side == "R" else tup[j] @ tup[i]
    return t

def equivalent(A, B):                                         # is there invertible h with h A_k = B_k h for all k?
    m = A[0].shape[0]; I = np.eye(m)
    M = np.vstack([np.kron(I, a.T) - np.kron(b, I) for a, b in zip(A, B)])   # vec(h A - B h) = 0, row-major vec
    _, sv, Vh = np.linalg.svd(M)
    null = Vh[np.sum(sv > 1e-8):].conj()
    if null.shape[0] == 0: return False
    h = null[0].reshape(m, m)
    return abs(np.linalg.det(h)) > 1e-8

def common_points(G, n, order):
    tr = [np.trace(g) for g in G]; found = 0; tested = 0
    for t0 in sorted({complex(round(x.real, 7), round(x.imag, 7)) for x in tr}, key=lambda c: (c.real, c.imag)):
        cands = [g for g, x in zip(G, tr) if abs(x - t0) < 1e-6]
        if len(cands) * 1.0 ** n == 0: continue
        for tup in itertools.product(cands, repeat=n):
            ok = True
            for i in range(n):
                for j in range(n):
                    if i == j: continue
                    if abs(np.trace(tup[i] @ tup[j]) - t0) > 1e-6 or abs(np.trace(tup[i] @ np.linalg.inv(tup[j])) - t0) > 1e-6: ok = False; break
                    for k in range(n):
                        if k in (i, j): continue
                        if abs(np.trace(tup[i] @ tup[j] @ tup[k]) - t0) > 1e-6: ok = False; break
                    if not ok: break
                if not ok: break
            if not ok: continue
            if len(close(list(tup), cap=order + 1)) != order: continue
            tested += 1
            if all(equivalent(apply(tup, mv), list(tup)) for mv in moves(n)): found += 1
    return found, tested

def main():
    t0 = time.time(); out = {"targets": {}, "cells": {}}
    T = targets()
    orders = {k: len(v) for k, v in T.items()}
    assert orders == EXPECTED, orders
    for n in (2, 3, 4):
        for name, G in T.items():
            if n == 4 and len(G) > 60: continue
            if n >= 3 and name == "H(5) (U5)": continue          # the Sp(2) argument decides it; the census is too slow (disclosed)
            found, tested = common_points(G, n, len(G))
            out["targets"][f"n={n} {name}"] = {"order": len(G), "filtered generating tuples": tested, "tuples fixed by every move": found}
            print(f"n={n} {name:14s} order {len(G):4d}: filtered generating tuples {tested:7d}; fixed by every move {found}", flush=True)
    g = out["targets"]
    out["cells"]["C0 n = 2: H(3), H(5) and Q8 have a common point"] = all(g[f"n=2 {k}"]["tuples fixed by every move"] > 0 for k in ("H(3) (U3)", "H(5) (U5)", "Q8 (SU2)"))
    out["cells"]["C1 n = 3: no target has a common point"] = all(v["tuples fixed by every move"] == 0 for k, v in g.items() if k.startswith("n=3"))
    out["cells"]["C2 n = 4: no target (order <= 60) has a common point"] = all(v["tuples fixed by every move"] == 0 for k, v in g.items() if k.startswith("n=4"))
    out["n=2 targets with a common point"] = [k for k, v in g.items() if k.startswith("n=2") and v["tuples fixed by every move"] > 0]
    out["seconds"] = round(time.time() - t0, 1)
    json.dump(out, open(pathlib.Path(__file__).with_name("the_common_point_in_higher_targets.json"), "w"), indent=1)
    print("cells:", out["cells"]); print("n = 2 targets with a common point:", out["n=2 targets with a common point"])

if __name__ == "__main__":
    main()
