#!/usr/bin/env python3
"""W28 of the weave: THE END CONDITION'S ROUTES TO THREE, AND THE COMMON POINT AS THE QUBIT. The rule is W28_RULE.md,
committed before this ran (57f019ed).

Part I, the end condition at the puncture (the six local solutions, block basis as in W24's D0):
  E1 every lift of L and R is (an unsigned permutation of the parity blocks) (x) (one G of 2O in every block), the
     permutation being the move's action on the parities mod 2;
  E2 the two middle conditions: the diagonal V2 and the sum-zero V4; spin 1/2 and spin 3/2 under 2O (a vector-spinor);
  E3 the flavor group (the flat automorphisms of W): M3(C), normalised by the lifts, invariant subspaces lambda (x) C^3;
  E4 the part of the flavor algebra that keeps V2 (or V4): the scalars;
  E5 the index sets of the end conditions that keep each requirement (the moves, the flavor group, the parity grading,
     their joint actions, locality), read from the commutant's isotypic structure.
Part II, the common point as the qubit:
  I1 the Pauli group; I2 the Clifford group; I3 SU(2) level 1's modular data and the dictionary; I4 the three global
  forms of su(2); I5 't Hooft's twist-eater.

    python3 the_three_routes_and_the_qubit.py   ->  the_three_routes_and_the_qubit.json beside it
"""
import itertools
import json
import sys
from pathlib import Path

import numpy as np
import sympy as sp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import the_common_point as CP  # noqa: E402  (the moves as automorphisms, 2O, the lifts of the common point)
import the_chiral_triplet as CT  # noqa: E402  (the parities as exponents of i on a, b; u_after)
import the_spin_room as SR  # noqa: E402  (quaternion units as 2 x 2 matrices)
import the_six_dimensional_census as SC  # noqa: E402  (W24: the lifts on the six, the holonomy W, commutants)
import the_self_conjugate_weave as SW  # noqa: E402  (W25: matrix-group closure)

I2 = np.eye(2, dtype=complex)
X = np.array([[0, 1], [1, 0]], dtype=complex)
Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
Z = np.array([[1, 0], [0, -1]], dtype=complex)
PAULI = [X, Y, Z]
UNIT_NAMES = {"i": "Z", "j": "Y", "k": "X"}
TOL = 1e-8


def close(A, B, tol=TOL):
    return bool(np.allclose(A, B, atol=tol))


def nullspace(M, tol=1e-9):
    _, s, vh = np.linalg.svd(M)
    rank = int(sum(s > tol))
    return vh[rank:].conj().T


def lifts_of(moves=("L", "R")):
    return [SC.blocks_action(CP.AUT[m], g) for m in moves for g in CP.extend(CP.AUT[m])]


def grading():
    return [np.kron(np.diag([SC.chi_word(u, [gen]) for u in CT.PAR]), I2) for gen in (1, 2)]


def isotypic(ops, n=6):
    """the isotypic structure [(d_i, m_i)] of the algebra the operators generate on C^n: d_i the irreducible's
    dimension, m_i its multiplicity (the commutant is the sum of the M_{m_i})"""
    k, B = SC.commutant(ops, n)
    if k == 1:
        return [(n, 1)]
    blocks = [np.column_stack([(Bj @ Bk - Bk @ Bj).flatten() for Bj in B]) for Bk in B]
    N = nullspace(np.vstack(blocks))
    centre = [sum(c[j] * B[j] for j in range(k)) for c in N.T]
    rng = np.random.default_rng(11)
    Zc = sum(complex(rng.normal(), rng.normal()) * C for C in centre)
    ev, vec = np.linalg.eig(Zc)
    groups = []
    for i, e in enumerate(ev):
        for gr in groups:
            if abs(gr[0] - e) < 1e-6:
                gr[1].append(i)
                break
        else:
            groups.append([e, [i]])
    out = []
    for _, idx in groups:
        Q, _ = np.linalg.qr(vec[:, idx])
        kW = SC.commutant([Q.conj().T @ A @ Q for A in ops], len(idx))[0]
        m = int(round(kW ** 0.5))
        out.append((len(idx) // m, m))
    return sorted(out)


def index_set(structure, half=3):
    dims = {sum(k * d for k, (d, _) in zip(ks, structure))
            for ks in itertools.product(*[range(m + 1) for _, m in structure])}
    return sorted(dm - half for dm in dims)


def kernel_vec(u):
    """the non-zero vector of the records mod 2 on which the parity u = (e_a, e_b) (exponents of i) is trivial"""
    return (u[1] // 2 % 2, u[0] // 2 % 2)


def units_of_parities():
    """W24 D1: for each parity the quaternion unit u_p with u_p rho_Q u_p^-1 = chi_p rho_Q"""
    out = {}
    for u in CT.PAR:
        for nm in ("i", "j", "k"):
            Q = SR.QM[nm]
            if all(close(Q @ SR.RHO[gen] @ np.linalg.inv(Q), SR.char_val(u, gen) * SR.RHO[gen]) for gen in (1, 2)):
                out[u] = nm
    return out


# ------------------------------------------------------------------------------------------------------------- Part I
def partI():
    res = {}
    units = units_of_parities()
    U = [SR.QM[units[u]] for u in CT.PAR]
    Phi = np.zeros((6, 6), dtype=complex)
    for p in range(3):
        Phi[2 * p:2 * p + 2, 2 * p:2 * p + 2] = U[p]
    Phi_inv = np.linalg.inv(Phi)
    lifts = lifts_of()
    hol = [SC.W_of([1]), SC.W_of([2])]

    # E1
    e1 = {}
    ok_block, ok_mod2, ok_int, ok_vector = True, True, True, True
    for m in ("L", "R", "P", "-I"):
        phi = CP.AUT[m]
        M = np.array(CP.MAT[m])
        for g in CP.extend(phi):
            A = SC.blocks_action(phi, g)
            G = SR.qmat(g)
            Pi = np.zeros((3, 3), dtype=int)
            for i, u in enumerate(CT.PAR):
                Pi[i, CT.PAR.index(CT.u_after(u, phi))] = 1
            blk = close(A, np.kron(Pi, G))
            mod2 = all(tuple(int(v) % 2 for v in M @ np.array(kernel_vec(CT.PAR[j]))) == kernel_vec(CT.PAR[i])
                       for i in range(3) for j in range(3) if Pi[i, j])
            inter = all(close(A @ SC.W_of([gen]) @ np.linalg.inv(A), SC.W_of(phi[gen])) for gen in (1, 2))
            B = Phi_inv @ A @ Phi
            S = np.array([[(-0.5 * np.trace(U[i] @ G @ U[j] @ np.linalg.inv(G))).real for j in range(3)]
                          for i in range(3)])
            vec_ok = close(B, np.kron(S, G)) and SC.is_signed_perm(np.round(S).astype(int)) and \
                round(float(np.linalg.det(S))) == 1
            if m in ("L", "R"):
                ok_block &= blk
                ok_mod2 &= mod2
                ok_int &= inter
                ok_vector &= vec_ok
            e1.setdefault(m, {"block permutation (row i <- column j)": Pi.tolist(),
                              "Pi (x) G": blk, "Pi is the move's action on the parities' kernels mod 2": mod2,
                              "intertwines the holonomy": inter,
                              "in rho_Q (x) C^3 coordinates: S (x) G, S the rotation Ad(G) on (u_1, u_2, u_3)": vec_ok,
                              "S": np.round(S).astype(int).tolist()})
    res["E1 the lifts, move by move"] = e1
    res["E1 every lift of L and R is Pi (x) G, Pi the move's action on the parities mod 2"] = bool(ok_block and ok_mod2)
    res["E1 the lifts of L and R intertwine the holonomy"] = bool(ok_int)
    res["E1 in rho_Q (x) C^3 coordinates every lift of L and R is Ad(G) (x) G: the six are vector (x) doublet"] = bool(
        ok_vector)

    # E2
    Q2 = np.vstack([I2, I2, I2]) / np.sqrt(3)
    P2 = Q2 @ Q2.conj().T
    P4 = np.eye(6) - P2
    Q4 = nullspace(Q2.conj().T)
    k, basis = SC.commutant(lifts, 6)
    span_rank = np.linalg.matrix_rank(np.column_stack([b.flatten() for b in basis] + [P2.flatten(), P4.flatten()]),
                                      tol=1e-7)
    inv2 = all(close(A @ P2, P2 @ A) for A in lifts)
    res["E2 V2 = {(v, v, v)} and V4 = {v1 + v2 + v3 = 0} are invariant under every lift"] = bool(inv2)
    res["E2 the commutant (W24 D0: 2) is spanned by their projections"] = bool(k == 2 and span_rank == 2)
    G6 = SW.closure(lifts, 6)
    rows = []
    ok2, ok4 = True, True
    for h in G6:
        jb = [j for j in range(3) if np.linalg.norm(h[0:2, 2 * j:2 * j + 2]) > 0.5][0]
        G = h[0:2, 2 * jb:2 * jb + 2]
        t = np.trace(G).real
        c2 = np.trace(Q2.conj().T @ h @ Q2)
        c4 = np.trace(Q4.conj().T @ h @ Q4)
        ok2 &= abs(c2 - t) < 1e-8
        ok4 &= abs(c4 - (t ** 3 - 2 * t)) < 1e-8
        rows.append((c2, c4, h))
    n = len(G6)
    norm2 = sum(abs(c2) ** 2 for c2, _, _ in rows) / n
    norm4 = sum(abs(c4) ** 2 for _, c4, _ in rows) / n
    fs2 = sum(np.trace(Q2.conj().T @ h @ h @ Q2) for _, _, h in rows).real / n
    fs4 = sum(np.trace(Q4.conj().T @ h @ h @ Q4) for _, _, h in rows).real / n
    res["E2 the group the lifts generate on the six: order"] = n
    res["E2 V2's character is tr G (the spin doublet)"] = bool(ok2)
    res["E2 V4's character is (tr G)^3 - 2 tr G (spin 3/2 restricted to 2O)"] = bool(ok4)
    res["E2 norms of the two characters (1 = irreducible)"] = [round(norm2, 9), round(norm4, 9)]
    res["E2 Frobenius-Schur indicators (-1 = quaternionic)"] = [round(fs2, 9), round(fs4, 9)]
    Q2p = np.vstack(U) / np.sqrt(3)
    res["E2 V2 is the Clebsch-Gordan copy {sum_p u_p v (x) e_p} of the doublet in rho_Q (x) C^3"] = bool(close(
        P2 @ Phi @ Q2p, Phi @ Q2p) and np.linalg.matrix_rank(Phi @ Q2p) == 2)

    # E3
    kF, F = SC.commutant(hol, 6)
    res["E3 the flat automorphisms of W (the commutant of W(a), W(b)): dimension"] = kF
    flav_form = all(close(Phi_inv @ Fk @ Phi, np.kron(np.array([[(Phi_inv @ Fk @ Phi)[2 * i, 2 * j] for j in range(3)]
                                                                 for i in range(3)]), I2)) for Fk in F)
    res["E3 in rho_Q (x) C^3 coordinates they are X (x) 1, X in M3(C)"] = bool(flav_form)
    Fmat = np.column_stack([Fk.flatten() for Fk in F])
    norm_ok = True
    for A in lifts:
        Ai = np.linalg.inv(A)
        for Fk in F:
            v = (A @ Fk @ Ai).flatten()
            c, *_ = np.linalg.lstsq(Fmat, v, rcond=None)
            norm_ok &= np.linalg.norm(Fmat @ c - v) < 1e-8
    res["E3 the lifts normalise the flavor algebra"] = bool(norm_ok)
    sF = isotypic(F)
    res["E3 the flavor algebra's isotypic structure on the six [(dimension, multiplicity)]"] = sF
    res["E3 its invariant subspaces' indices"] = index_set(sF)

    # E4
    def stabiliser(Pw):
        cols = np.column_stack([((np.eye(6) - Pw) @ Fk @ Pw).flatten() for Fk in F])
        N = nullspace(cols)
        sol = [sum(c[j] * F[j] for j in range(len(F))) for c in N.T]
        scalar = all(close(S_ / S_[0, 0], np.eye(6)) for S_ in sol) if sol else False
        return N.shape[1], bool(scalar)

    d2, s2 = stabiliser(P2)
    d4, s4 = stabiliser(P4)
    res["E4 the part of the flavor algebra that keeps V2: dimension, and is it the scalars"] = [d2, s2]
    res["E4 ... that keeps V4"] = [d4, s4]

    # E5
    puncture = SC.W_of([1, 2, -1, -2])
    res["E5 the puncture's holonomy W([a, b]) = -1 on all six"] = close(puncture, -np.eye(6))
    kloc, loc = SC.commutant([puncture], 6)
    res["E5 the commutant of the puncture's holonomy: dimension (36 = all of M6)"] = kloc
    reqs = {"the moves (the lifts of L and R)": lifts,
            "the flavor group": F,
            "the parity grading": grading(),
            "the moves and the flavor group": lifts + F,
            "the moves and the parity grading": lifts + grading(),
            "locality: the commutant of the puncture's own holonomy": loc}
    table = {}
    for name, ops in reqs.items():
        st = isotypic(ops)
        table[name] = {"commutant": SC.commutant(ops, 6)[0], "isotypic structure [(dimension, multiplicity)]": st,
                       "index set": index_set(st)}
    res["E5 the index sets"] = table
    predicted = {"the moves (the lifts of L and R)": [-3, -1, 1, 3], "the flavor group": [-3, 0, 3],
                 "the parity grading": [-3, -2, -1, 0, 1, 2, 3], "the moves and the flavor group": [-3, 3],
                 "the moves and the parity grading": [-3, 3],
                 "locality: the commutant of the puncture's own holonomy": [-3, 3]}
    res["E5 every index set as the rule predicted"] = all(table[k]["index set"] == v for k, v in predicted.items())
    res["E5 neither the moves alone nor the flavor group alone fixes the count; jointly they force +-3"] = bool(
        table["the moves (the lifts of L and R)"]["index set"] != [-3, 3]
        and table["the flavor group"]["index set"] != [-3, 3]
        and table["the moves and the flavor group"]["index set"] == [-3, 3])
    return res


# ------------------------------------------------------------------------------------------------------------ Part II
def ad(Um):
    Ui = np.linalg.inv(Um)
    return np.array([[0.5 * np.trace(PAULI[a] @ Um @ PAULI[b] @ Ui).real for b in range(3)] for a in range(3)])


def rkey(Rm):
    return tuple(np.round(Rm, 6).flatten() + 0.0)


def rclosure(gens):
    G = {rkey(np.eye(3)): np.eye(3)}
    fr = [np.eye(3)]
    while fr:
        nx = []
        for A in fr:
            for g in gens:
                B = A @ g
                if rkey(B) not in G:
                    G[rkey(B)] = B
                    nx.append(B)
        fr = nx
        assert len(G) <= 1000
    return G


def axis_angle(Rm):
    c = (np.trace(Rm) - 1) / 2
    th = float(np.degrees(np.arccos(np.clip(c, -1, 1))))
    if th < 1e-6:
        return [0.0, 0.0, 0.0], 0.0
    if abs(th - 180) < 1e-6:
        w, v = np.linalg.eig(Rm)
        nvec = np.real(v[:, int(np.argmin(abs(w - 1)))])
        nvec = nvec * np.sign(nvec[np.argmax(abs(nvec))])
    else:
        nvec = np.array([Rm[2, 1] - Rm[1, 2], Rm[0, 2] - Rm[2, 0], Rm[1, 0] - Rm[0, 1]]) / (2 * np.sin(np.radians(th)))
    return [round(float(v), 6) + 0.0 for v in nvec], round(th, 6)


def up_to_sign(A, B):
    return close(A, B) or close(A, -B)


def partII():
    res = {}
    QM = SR.QM
    rho_a, rho_b = SR.RHO[1], SR.RHO[2]
    rho_ab = rho_a @ rho_b
    # I1
    i1 = {"rho(a) = iZ, rho(b) = iY, rho(ab) = iX": close(rho_a, 1j * Z) and close(rho_b, 1j * Y) and close(
        rho_ab, 1j * X),
          "the quaternion units i, j, k are iZ, iY, iX": close(QM["i"], 1j * Z) and close(QM["j"], 1j * Y) and close(
              QM["k"], 1j * X)}
    units = units_of_parities()
    hol_axis = {"a": "Z", "b": "Y", "ab": "X"}
    words = {"a": (1, 0), "b": (0, 1), "ab": (1, 1)}
    par = {}
    ok_ker = True
    for u, name in zip(CT.PAR, CT.NAMES):
        kv = kernel_vec(u)
        kw = [w for w, v in words.items() if v == kv][0]
        axis = UNIT_NAMES[units[u]]
        ok_ker &= hol_axis[kw] == axis
        par[name] = {"unit u_p": units[u], "Pauli axis": axis, "kernel on the records mod 2": kw,
                     "the kernel's holonomy lies on that axis": hol_axis[kw] == axis}
    i1["the parities"] = par
    i1["each parity is one Pauli axis, its kernel the holonomies along it"] = bool(ok_ker)
    bases = [np.linalg.eigh(P)[1] for P in PAULI]
    mub = all(abs(abs(np.vdot(bases[s][:, a], bases[t][:, b])) ** 2 - 0.5) < 1e-12
              for s in range(3) for t in range(3) if s != t for a in range(2) for b in range(2))
    i1["the three eigenbases are mutually unbiased"] = bool(mub)
    res["I1 the Pauli group"] = i1
    # I2
    named = {"L": lambda: np.diag([np.exp(1j * np.pi / 4), np.exp(-1j * np.pi / 4)]),
             "R": lambda: (I2 - 1j * Y) / np.sqrt(2),
             "P": lambda: 1j * (Z + Y) / np.sqrt(2),
             "-I": lambda: 1j * X}
    named_txt = {"L": "e^{i pi Z/4}, a quarter turn about Z (the phase gate up to a phase)",
                 "R": "e^{-i pi Y/4}, a quarter turn about Y", "P": "(iZ + iY)/sqrt2, a half turn about (Z + Y)/sqrt2",
                 "-I": "iX"}
    i2 = {}
    lift_ok = True
    for m in ("L", "R", "P", "-I"):
        gs = CP.extend(CP.AUT[m])
        G = SR.qmat(gs[0])
        ax, th = axis_angle(ad(G))
        same = up_to_sign(G, named[m]())
        lift_ok &= same
        i2[m] = {"lifts in 2O": len(gs), "axis (X, Y, Z) and angle of Ad(g)": [ax, th],
                 "equals, up to sign": named_txt[m], "holds": same}
    i2["every lift as named in the rule"] = bool(lift_ok)
    gens = [SR.qmat(g) for m in ("L", "R") for g in CP.extend(CP.AUT[m])]
    G2O = SW.closure(gens, 2)
    Q8 = SW.closure([QM["i"], QM["j"]], 2)
    keyq = lambda M: tuple(np.round(M.flatten(), 7))  # noqa: E731
    q8keys = {keyq(q) for q in Q8}
    normalises = all(keyq(h @ q @ np.linalg.inv(h)) in q8keys for h in G2O for q in Q8)
    order4 = [q for q in Q8 if close(q @ q, -I2)]
    auts = 0
    for x_, y_ in itertools.product(order4, order4):
        if up_to_sign(x_, y_):
            continue
        if close(y_ @ x_ @ np.linalg.inv(y_), np.linalg.inv(x_)) and len(SW.closure([x_, y_], 2)) == 8:
            auts += 1
    kernel = [h for h in G2O if all(close(h @ q, q @ h) for q in Q8)]
    i2["the lifts of L and R generate: order"] = len(G2O)
    i2["it normalises Q8"] = bool(normalises)
    i2["|Aut(Q8)|"] = auts
    i2["kernel of the conjugation map 2O -> Aut(Q8)"] = len(kernel)
    i2["so 2O is the normaliser of Q8 in SU(2) (onto Aut(Q8); the centraliser of Q8 in SU(2) is +-1, Schur)"] = bool(
        normalises and auts == 24 and len(G2O) // len(kernel) == 24)
    img_weave = rclosure([ad(g) for g in gens])
    H = (X + Z) / np.sqrt(2)
    Sg = np.diag([1, 1j])
    img_cliff = rclosure([ad(H), ad(Sg)])
    i2["images in SO(3): the weave's lifts, the Clifford group <H, S>"] = [len(img_weave), len(img_cliff)]
    i2["the same 24 rotations"] = bool(set(img_weave) == set(img_cliff) and len(img_weave) == 24)
    res["I2 the Clifford group"] = i2
    # I3
    S1 = np.array([[1, 1], [1, -1]], dtype=complex) / np.sqrt(2)
    T1 = np.exp(-2j * np.pi / 24) * np.diag([1, 1j])
    T7 = np.exp(-2j * np.pi * 7 / 24) * np.diag([1, np.exp(2j * np.pi * 3 / 4)])
    i3 = {}
    for nm, T_ in (("SU(2)_1 (the semion)", T1), ("(E7)_1 (the anti-semion)", T7)):
        rel = close(S1 @ S1, I2) and close(np.linalg.matrix_power(S1 @ T_, 3), S1 @ S1)
        WA = np.diag([S1[1, b] / S1[0, b] for b in range(2)])
        WB = S1 @ WA @ np.linalg.inv(S1)
        anti = close(WA @ WB, -WB @ WA)
        cov = close(T_ @ WA @ np.linalg.inv(T_), WA)
        TWB = T_ @ WB @ np.linalg.inv(T_)
        lam = np.trace(np.linalg.inv(WA @ WB) @ TWB) / 2
        cov &= close(TWB, lam * WA @ WB)
        R_ = S1 @ np.linalg.inv(T_) @ np.linalg.inv(S1)
        img = rclosure([ad(S1), ad(T_)])
        targets = [ad(WA), ad(WB), ad(T_), ad(R_)]
        sources = [ad(rho_a), ad(rho_b), ad(SR.qmat(CP.extend(CP.AUT["L"])[0])), ad(SR.qmat(CP.extend(CP.AUT["R"])[0]))]
        found = []
        for Mx in SC.signed_perms():
            if round(np.linalg.det(Mx)) != 1:
                continue
            if all(close(Mx @ s @ Mx.T, t_) for s, t_ in zip(sources, targets)):
                found.append(Mx.tolist())
        i3[nm] = {"S^2 = 1 and (ST)^3 = S^2": bool(rel),
                  "Verlinde's loops W_A, W_B are Z, X": close(WA, Z) and close(WB, X),
                  "W_A W_B = -W_B W_A (the common point's commutator -1)": bool(anti),
                  "T fixes W_A and sends W_B to a multiple of W_A W_B": bool(cov),
                  "image of <S, T> in SO(3): order": len(img),
                  "the same rotations as the weave's": bool(set(img) == set(img_weave)),
                  "the cube's rotations M with M (rho(a), rho(b), g_L, g_R) M^-1 = (W_A, W_B, T, S T^-1 S^-1)": found}
    i3["exactly one M for each (the projective data match both; the hand is in the phases)"] = all(
        len(v["the cube's rotations M with M (rho(a), rho(b), g_L, g_R) M^-1 = (W_A, W_B, T, S T^-1 S^-1)"]) == 1
        for k, v in i3.items() if isinstance(v, dict))
    i3["the semion's M is x -> -y, y -> -x, z -> -z"] = (
        i3["SU(2)_1 (the semion)"]["the cube's rotations M with M (rho(a), rho(b), g_L, g_R) M^-1 = (W_A, W_B, T, S T^-1 S^-1)"]
        == [[[0, -1, 0], [-1, 0, 0], [0, 0, -1]]])
    t_ = ad(SR.qmat(CP.extend(CP.AUT["L"])[0]))
    gL, gR = SR.qmat(CP.extend(CP.AUT["L"])[0]), SR.qmat(CP.extend(CP.AUT["R"])[0])
    s_ = ad(gL @ np.linalg.inv(gR) @ gL)
    lrl = (np.array(CP.MAT["L"]) @ np.round(np.linalg.inv(np.array(CP.MAT["R"]))).astype(int) @ np.array(CP.MAT["L"]))
    i3["the weave's images: t = Ad g_L, s = Ad(g_L g_R^-1 g_L); s^2 = (st)^3 = t^4 = 1"] = bool(
        close(s_ @ s_, np.eye(3)) and close(np.linalg.matrix_power(s_ @ t_, 3), np.eye(3))
        and close(np.linalg.matrix_power(t_, 4), np.eye(3)))
    i3["L R^-1 L as a matrix (S-duality, up to sign)"] = lrl.tolist()
    i3["so the moves act on the common point through the (2, 3, 4) triangle group, PSL(2, Z/4) = S4, order"] = len(
        img_weave)
    res["I3 SU(2) at level 1"] = i3
    # I4
    vecs = [(0, 0), (1, 0), (0, 1), (1, 1)]
    om = lambda x_, y_: (x_[0] * y_[1] - x_[1] * y_[0]) % 2  # noqa: E731
    add = lambda x_, y_: ((x_[0] + y_[0]) % 2, (x_[1] + y_[1]) % 2)  # noqa: E731
    subgroups = []
    for r in range(1, 5):
        for S_ in itertools.combinations(vecs, r):
            if (0, 0) in S_ and all(add(a_, b_) in S_ for a_ in S_ for b_ in S_):
                subgroups.append(frozenset(S_))
    iso = [S_ for S_ in subgroups if all(om(a_, b_) == 0 for a_ in S_ for b_ in S_)]
    lag = [S_ for S_ in iso if not any(S_ < T_ for T_ in iso)]
    asy = {(1, 0): "SU(2) (the Wilson line genuine)", (0, 1): "SO(3)+ (the 't Hooft line)",
           (1, 1): "SO(3)- (the dyonic line)"}
    rowsI4 = {}
    ok_char = True
    for u, name in zip(CT.PAR, CT.NAMES):
        chi = lambda x_: (-1) ** ((u[0] // 2) * x_[0] + (u[1] // 2) * x_[1])  # noqa: E731
        ker = frozenset(v for v in vecs if chi(v) == 1)
        v0 = [v for v in ker if v != (0, 0)][0]
        ok_char &= all(chi(x_) == (-1) ** om(v0, x_) for x_ in vecs)
        rowsI4[name] = {"kernel": sorted(ker), "a Lagrangian": ker in lag, "global form": asy[v0]}
    equi = True
    acts = {}
    for m in ("L", "R", "P", "-I"):
        M = np.array(CP.MAT[m])
        Mi = np.round(np.linalg.inv(M)).astype(int)
        for u in CT.PAR:
            lhs = kernel_vec(CT.u_after(u, CP.AUT[m]))
            rhs = tuple(int(v) % 2 for v in Mi @ np.array(kernel_vec(u)))
            equi &= lhs == rhs
        acts[m] = {asy[kernel_vec(u)]: asy[tuple(int(v) % 2 for v in M @ np.array(kernel_vec(u)))] for u in CT.PAR}
    res["I4 the three global forms of su(2)"] = {
        "maximal isotropic subgroups of F2^2": [sorted(S_) for S_ in lag], "their number (|P^1(F2)|)": len(lag),
        "the parities": rowsI4,
        "each parity's kernel is a Lagrangian, all three met": bool(
            all(r["a Lagrangian"] for r in rowsI4.values()) and len({r["global form"] for r in rowsI4.values()}) == 3),
        "mutual locality is the character: chi_v(x) = (-1)^omega(v, x)": bool(ok_char),
        "equivariant: kernel(u o phi) = M_phi^-1 kernel(u) for every move": bool(equi),
        "the moves on the global forms (genuine line v -> M v)": acts,
        "L is theta -> theta + 2 pi (fixes SU(2), swaps SO(3)+ and SO(3)-)": bool(
            acts["L"] == {asy[(1, 0)]: asy[(1, 0)], asy[(0, 1)]: asy[(1, 1)], asy[(1, 1)]: asy[(0, 1)]})}
    # I5
    p = sp.symbols("p0:4", real=True)
    q = sp.symbols("q0:4", real=True)

    def qm(a_, b_):
        return (a_[0] * b_[0] - a_[1] * b_[1] - a_[2] * b_[2] - a_[3] * b_[3],
                a_[0] * b_[1] + a_[1] * b_[0] + a_[2] * b_[3] - a_[3] * b_[2],
                a_[0] * b_[2] - a_[1] * b_[3] + a_[2] * b_[0] + a_[3] * b_[1],
                a_[0] * b_[3] + a_[1] * b_[2] - a_[2] * b_[1] + a_[3] * b_[0])

    Aq = [sp.expand(s1 + s2) for s1, s2 in zip(qm(p, q), qm(q, p))]
    n2p = sum(v ** 2 for v in p)
    n2q = sum(v ** 2 for v in q)
    id1 = sp.expand(q[0] * n2p - (p[0] * Aq[0] + p[1] * Aq[1] + p[2] * Aq[2] + p[3] * Aq[3]) / 2) == 0
    id2 = sp.expand(p[0] * n2q - (q[0] * Aq[0] + q[1] * Aq[1] + q[2] * Aq[2] + q[3] * Aq[3]) / 2) == 0
    id3 = sp.expand(Aq[0].subs({p[0]: 0, q[0]: 0}) + 2 * (p[1] * q[1] + p[2] * q[2] + p[3] * q[3])) == 0
    kc, _ = SC.commutant([rho_a, rho_b], 2)
    centre = {}
    ok_eat = True
    for ea, eb in ((1, -1), (-1, 1), (-1, -1)):
        found = [nm for nm in ("i", "j", "k")
                 if close(QM[nm] @ rho_a @ np.linalg.inv(QM[nm]), ea * rho_a)
                 and close(QM[nm] @ rho_b @ np.linalg.inv(QM[nm]), eb * rho_b)]
        pars = [name for u, name in zip(CT.PAR, CT.NAMES) if (SR.char_val(u, 1), SR.char_val(u, 2)) == (ea, eb)]
        ok_eat &= len(found) == 1 and len(pars) == 1
        centre[str((ea, eb))] = {"conjugation by": found, "the parity with these signs": pars}
    res["I5 't Hooft's twist-eater"] = {
        "q0 |p|^2 = (p . {p, q})/2 and p0 |q|^2 = (q . {p, q})/2 (exact)": bool(id1 and id2),
        "so anticommuting unit quaternions are pure, and then orthogonal (exact)": bool(id1 and id2 and id3),
        "so every pair in SU(2) with commutator -1 is conjugate to the common point (SO(3) is transitive on "
        "orthonormal pairs)": bool(id1 and id2 and id3),
        "commutant of the common point on C^2 (1: its centraliser in SU(2) is +-1)": kc,
        "the centre symmetry (A, B) -> (e_a A, e_b B)": centre,
        "each non-trivial element is conjugation by one unit, and is one parity (the twist-eater eats the centre "
        "symmetry)": bool(ok_eat)}
    return res


def run():
    out = {"rule": "W28_RULE.md (committed 57f019ed before this ran)"}
    A = partI()
    B = partII()
    out["Part I the end condition"] = A
    out["Part II the common point as the qubit"] = B
    i3 = B["I3 SU(2) at level 1"]
    out["verdict"] = {
        "E1 block form and the vector-spinor coordinates": bool(
            A["E1 every lift of L and R is Pi (x) G, Pi the move's action on the parities mod 2"]
            and A["E1 in rho_Q (x) C^3 coordinates every lift of L and R is Ad(G) (x) G: the six are vector (x) doublet"]),
        "E2 the middle conditions are spin 1/2 and spin 3/2": bool(
            A["E2 V2's character is tr G (the spin doublet)"]
            and A["E2 V4's character is (tr G)^3 - 2 tr G (spin 3/2 restricted to 2O)"]
            and A["E2 the commutant (W24 D0: 2) is spanned by their projections"]),
        "E3 the flavor group M3, normalised by the lifts, indices -3, 0, 3": bool(
            A["E3 the flat automorphisms of W (the commutant of W(a), W(b)): dimension"] == 9
            and A["E3 the lifts normalise the flavor algebra"] and A["E3 its invariant subspaces' indices"] == [-3, 0, 3]),
        "E4 the middle conditions keep only the scalars of the flavor algebra": bool(
            A["E4 the part of the flavor algebra that keeps V2: dimension, and is it the scalars"] == [1, True]
            and A["E4 ... that keeps V4"] == [1, True]),
        "E5 the index sets as predicted": A["E5 every index set as the rule predicted"],
        "I1 Pauli": B["I1 the Pauli group"]["each parity is one Pauli axis, its kernel the holonomies along it"],
        "I2 Clifford": bool(B["I2 the Clifford group"]["every lift as named in the rule"]
                            and B["I2 the Clifford group"]["the same 24 rotations"]),
        "I3 SU(2)_1, one dictionary each for the semion and the anti-semion": bool(
            i3["exactly one M for each (the projective data match both; the hand is in the phases)"]
            and i3["the semion's M is x -> -y, y -> -x, z -> -z"]),
        "I4 the global forms": bool(B["I4 the three global forms of su(2)"]["each parity's kernel is a Lagrangian, all three met"]
                                    and B["I4 the three global forms of su(2)"]["equivariant: kernel(u o phi) = M_phi^-1 kernel(u) for every move"]),
        "I5 the twist-eater": bool(
            B["I5 't Hooft's twist-eater"]["so anticommuting unit quaternions are pure, and then orthogonal (exact)"]
            and B["I5 't Hooft's twist-eater"]["each non-trivial element is conjugation by one unit, and is one parity (the twist-eater eats the centre symmetry)"])}
    return out


if __name__ == "__main__":
    res = run()
    with open(HERE / "the_three_routes_and_the_qubit.json", "w") as f:
        json.dump(res, f, indent=1, ensure_ascii=False, default=str)
    print(json.dumps(res, indent=1, ensure_ascii=False, default=str))
