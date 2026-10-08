#!/usr/bin/env python3
"""W30 of the weave: IS AN ORDER-3 FLUX FORCED ON THE SHARED FIBRE? The rule is W30_RULE.md, committed before this ran
(e611b54e).

  Q1 the lemma's check: Sym^n rho_Q and chi_p (x) Sym^n (n = 0..8) send [a, b] to (-1)^n;
  Q2 the qutrit pairs: each of the nine centre twists (w^i C3, w^j S3) is conjugate to (C3, S3);
  Q3 the moves on the qutrit class (L, R, -I, the swap P, P o K) for all nine twists; the qubit's P for contrast;
  Q5 the moves on the qutrit's C^3: the projective order, the commutant, the reflections; the same with the bare -I;
  Q6 the record re-read (W25's and W26's JSON);
  Q7 the verdict.
(Q4, the rank-3 cusp condition, is a choice stated in the rule; nothing is computed for it.)

    python3 the_order_three_flux.py   ->  the_order_three_flux.json beside it
"""
import itertools
import json
import sys
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import the_six_dimensional_census as SC  # noqa: E402  (commutant)
import the_spin_room as SR  # noqa: E402  (the quaternion units, the parity characters)
import the_chiral_triplet as CT  # noqa: E402  (the parities)
import the_z6_twist_eater as Z  # noqa: E402  (thin null space, isotypic components, subset sums: generic in n)

OMEGA = np.exp(2j * np.pi / 3)
C3 = np.diag([OMEGA ** k for k in range(3)])
S3 = np.zeros((3, 3), dtype=complex)
for _k in range(3):
    S3[(_k + 1) % 3, _k] = 1
inv = np.linalg.inv


def close(P, Q, tol=1e-8):
    return bool(np.allclose(P, Q, atol=tol))


def intertwiners(A, B, phiA, phiB):
    """the solutions U of U A = phi(A) U and U B = phi(B) U (n x n)"""
    n = A.shape[0]
    I = np.eye(n)
    M = np.vstack([np.kron(A.T, I) - np.kron(I, phiA), np.kron(B.T, I) - np.kron(I, phiB)])
    N_ = Z.nullspace(M)
    return [N_[:, i].reshape(n, n, order="F") for i in range(N_.shape[1])]


def comm(A, B):
    return A @ B @ inv(A) @ inv(B)


def sym_power(M, n):
    """Sym^n of a 2 x 2 matrix in the basis e1^(n-k) e2^k: column k is (M e1)^(n-k) (M e2)^k expanded"""
    out = np.zeros((n + 1, n + 1), dtype=complex)
    c1 = np.array([M[0, 0], M[1, 0]])                  # M e1 = c1[0] e1 + c1[1] e2
    c2 = np.array([M[0, 1], M[1, 1]])
    for k in range(n + 1):
        poly = np.array([1.0 + 0j])                    # coefficients by the power of e2
        for _ in range(n - k):
            poly = np.convolve(poly, c1)
        for _ in range(k):
            poly = np.convolve(poly, c2)
        out[:, k] = poly
    return out


def det1(U):
    return U / np.linalg.det(U) ** (1 / U.shape[0])


def pkey(M):
    """M up to a scalar: divided by its first non-zero entry in flat order (stable for monomial and Fourier patterns)"""
    flat = M.flatten()
    i = int(np.flatnonzero(abs(flat) > 1e-6)[0])
    return tuple(np.round(flat / flat[i], 6) + 0.0)


def projective_closure(gens, cap=5000):
    G = {pkey(np.eye(gens[0].shape[0])): np.eye(gens[0].shape[0], dtype=complex)}
    fr = list(G.values())
    while fr:
        nx = []
        for X in fr:
            for g in gens:
                Y = X @ g
                k = pkey(Y)
                if k not in G:
                    G[k] = Y
                    nx.append(Y)
        fr = nx
        assert len(G) <= cap
    return G


def reflection_centre(U, n):
    for c in range(n):
        R = np.zeros((n, n))
        for k in range(n):
            R[(c - k) % n, k] = 1
        D = U @ R.T
        if np.allclose(D, np.diag(np.diag(D)), atol=1e-9):
            return c
    return None


def moves_of(A, B):
    return {"L": (A, A @ B), "R": (A @ B, B), "-I": (inv(A), inv(B)), "P (the swap)": (B, A),
            "P o K (the swap with complex conjugation)": (B.conj(), A.conj())}


def run():
    res = {"rule": "W30_RULE.md (committed e611b54e before this ran)"}
    # Q1
    ra, rb = SR.RHO[1], SR.RHO[2]
    q1 = {}
    ok1 = True
    for n in range(9):
        sa, sb = sym_power(ra, n), sym_power(rb, n)
        hom = close(sym_power(ra @ rb, n), sa @ sb)
        c = comm(sa, sb)
        scal = (-1) ** n
        par_ok = True
        for u in CT.PAR:
            ca, cb = SR.char_val(u, 1), SR.char_val(u, 2)
            par_ok &= close(comm(ca * sa, cb * sb), scal * np.eye(n + 1))
        row = {"Sym^n is a representation (on a b)": hom, "[a, b] -> (-1)^n": close(c, scal * np.eye(n + 1)),
               "chi_p (x) Sym^n, all three parities, the same": bool(par_ok)}
        ok1 &= all(row.values())
        q1[str(n)] = row
    res["Q1 the lemma's check: the puncture in every Sym^n of the forced point"] = q1
    res["Q1 no order-3 flux from the forced rank-2 data (order of the puncture's image at most 2)"] = bool(ok1)
    # Q2, Q3
    base_comm = comm(C3, S3)
    q2 = {"det C3, det S3": [round(float(np.real(np.linalg.det(C3))), 9), round(float(np.real(np.linalg.det(S3))), 9)],
          "[C3, S3] = w 1": close(base_comm, OMEGA * np.eye(3))}
    twists = {}
    q3 = {}
    ok2, ok3 = True, True
    expected = {"L": 1, "R": 1, "-I": 1, "P (the swap)": 0, "P o K (the swap with complex conjugation)": 1}
    for i, j in itertools.product(range(3), range(3)):
        A, B = OMEGA ** i * C3, OMEGA ** j * S3
        d = len(intertwiners(C3, S3, A, B))
        twists["(%d, %d)" % (i, j)] = d
        ok2 &= d == 1
        row = {}
        for nm, (pa, pb) in moves_of(A, B).items():
            row[nm] = len(intertwiners(A, B, pa, pb))
        q3["(%d, %d)" % (i, j)] = row
        ok3 &= row == expected
    q2["each centre twist (w^i C3, w^j S3) conjugate to (C3, S3): intertwiner dimensions"] = twists
    q2["one class"] = bool(ok2)
    res["Q2 the qutrit pairs"] = q2
    qa, qb = 1j * np.diag([1, -1]), 1j * np.array([[0, -1j], [1j, 0]])
    qubit = {nm: len(intertwiners(qa, qb, pa, pb)) for nm, (pa, pb) in moves_of(qa, qb).items()}
    res["Q3 the moves on the qutrit class (intertwiner dimensions, every twist)"] = q3
    res["Q3 L, R and -I keep it; P sends it to the w-bar class; P o K keeps it (all nine twists)"] = bool(ok3)
    res["Q3 for contrast, the qubit point (iZ, iY): the same moves"] = qubit
    res["Q3 the qubit's swap keeps its class (-1 is its own inverse)"] = bool(qubit["P (the swap)"] == 1)
    # Q5
    UL = det1(intertwiners(C3, S3, C3, C3 @ S3)[0])
    UR = det1(intertwiners(C3, S3, C3 @ S3, S3)[0])
    UI = det1(intertwiners(C3, S3, inv(C3), inv(S3))[0])
    G_lr = projective_closure([UL, UR])
    G_lri = projective_closure([UL, UR, UI])
    k_lr = SC.commutant([UL, UR], 3)[0]
    k_lri = SC.commutant([UL, UR, UI], 3)[0]
    st = sorted((d, m) for _, d, m in Z.components([UL, UR], 3))
    W2 = np.linalg.matrix_power(UL @ inv(UR) @ UL, 2)
    res["Q5 the moves on the qutrit's C^3"] = {
        "projective order of the lifts of L and R (SL(2, F3) = 2T: 24)": len(G_lr),
        "their commutant on C^3": k_lr,
        "their isotypic structure [(dimension, multiplicity)]": st,
        "the lift of (L R^-1 L)^2: a phase times the reflection k -> c - k, with c": reflection_centre(W2, 3),
        "the bare -I's lift: a phase times the reflection k -> c - k, with c": reflection_centre(UI, 3),
        "with the bare -I added: projective order": len(G_lri),
        "with the bare -I added: commutant": k_lri,
        "as the rule stated (24; commutant 2, split 2 + 1; reflections 2 and 0; with -I: commutant 1)": bool(
            len(G_lr) == 24 and k_lr == 2 and st == [(1, 1), (2, 1)] and reflection_centre(W2, 3) == 2
            and reflection_centre(UI, 3) == 0 and k_lri == 1)}
    # Q6
    w25 = json.load(open(HERE / "the_self_conjugate_weave.json"))
    w26 = json.load(open(HERE / "the_weaves_mirror.json"))
    ext = w25["F4 centralisers in E8 (dimensions by characters)"]["the odd-trace extension: Q8 with the order-3 move's lift"]
    flips = w26["N3 the order-3 orientation on the parities, tick by tick"][
        "the 3-cycle's direction flips at every tick on all of them"]
    res["Q6 the record's order-3 structures, re-read"] = {
        "W25: the odd-trace extension (a thread object): order, centraliser, multiplicity of the complex character w": [
            ext["order"], ext["centraliser dimension"],
            ext["multiplicity of the complex character omega (trivial on Q8)"]],
        "W26: the 3-cycle's direction flips at every tick (all odd-trace words to length 10)": bool(flips),
        "mod 3 the fibre's puncture goes to -1; the order-3 part is on the meridian (sm:B1536's preregistration; B284; "
        "main's B1601)": "cited",
        "B1280 (PROVED): order-3 central twists on the stable letter give N = 0": "cited",
        "B955 is a knot-group fact (H1 = Z); the fibre has H1 = Z^2": "cited"}
    # Q7
    res["Q7 the verdict"] = {
        "the forced data give no order-3 flux (Q1)": bool(ok1),
        "the qutrit class exists, one class (Q2)": bool(ok2),
        "the grammar's moves keep it, the swap does not, the swap with conjugation does (Q3)": bool(ok3),
        "so it is a common point only on one branch of the swap's fork (GENESIS GM5c, FK3)": bool(ok3),
        "the record's order-3 structures are on threads or on the meridian (Q6)": bool(flips),
        "an order-3 flux is allowed on a fork, not forced": bool(ok1 and ok2 and ok3 and flips)}
    return res


if __name__ == "__main__":
    out = run()
    with open(HERE / "the_order_three_flux.json", "w") as f:
        json.dump(out, f, indent=1, ensure_ascii=False, default=str)
    print(json.dumps(out, indent=1, ensure_ascii=False, default=str))
