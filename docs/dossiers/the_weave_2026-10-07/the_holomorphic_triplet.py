#!/usr/bin/env python3
"""W21 of the weave: THE HAND BY HODGE TYPE. Which of the weave's two triplets is holomorphic (rule: W21_RULE.md).

V = H^1(F2; W), W the sum over the three parities chi_p of chi_p (x) rho_Q, is the fibre's twisted cohomology (W10). For
a complex structure tau on the fibre it splits into Hodge types, V = V^(1,0) + V^(0,1), one line of each per parity. The
moves act on V through a finite group (order 96), so the period map is constant and V^(1,0) is invariant under every
move: it is T or T-bar (the weave theorem of W21_RULE.md). The Hodge-Riemann form Q(u, v) = i int u ^ v-bar is positive
on V^(1,0) and negative on V^(0,1), and it is topological: the cup product on the relative class of the punctured torus,

    Q(u, v) = i * sum over the letters of the puncture loop of +-H(u(g), rho(g) v(h)),

with the chain of the loop [a, b] = a b a^-1 b^-1 (+[a | b] - [aba^-1 | a]) and u normalized so that u([a, b]) = 0. So
the sign of Q on each triplet names its Hodge type, with no period computed.

The controls (each must hold before the read-out is used): Q is the Riemann bilinear form on trivial coefficients; Q is
hermitian and does not depend on the cocycles chosen; three fundamental chains (the loop read from three starting
points) agree; Q is invariant under L, R and the sign with every lift; the swap P reverses it; the signature is (3, 3) on
V and (1, 1) on the spin doublet M = H^1(F2; rho_Q); T and T-bar are Q-orthogonal.

The read-outs: the sign of Q on T and on T-bar (T is the triplet on which Z = S^2, the braid lift of -I, acts as -i);
the same on M's two lines, and the holomorphic line's character as a power of eta's; Z on the holomorphic triplet; and
the holomorphic triplet as that character times a triplet of PSL(2, Z/4) = S4.

    python3 the_holomorphic_triplet.py   ->  the_holomorphic_triplet.json beside it
    python3 the_holomorphic_triplet.py --controls   (the controls only; no read-out)
"""
import cmath
import json
import sys
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import the_chiral_triplet as CT  # noqa: E402  (V, its basis per parity, the moves on V, T and T-bar)
import the_common_point as CP  # noqa: E402  (the moves as automorphisms, their lifts in 2O)
import the_spin_room as SR  # noqa: E402  (the module chi (x) rho_Q, cocycles on words)

I2 = np.eye(2, dtype=complex)
LOOPS = {"[a, b]": [1, 2, -1, -2], "its rotation by one letter": [2, -1, -2, 1],
         "its conjugate [a^-1, b^-1]": [-1, -2, 1, 2]}
ZERO = (0, 0)                                   # the zero parity: the spin doublet M


def word_matrix(u, w):
    M = I2.copy()
    for x in w:
        M = M @ SR.module(u, x)
    return M


def chain(loop):
    """the bar 2-chain of a relator word: +[p | x] for a letter x after the prefix p, -[p x^-1 | x] for x^-1"""
    terms, p = [], []
    for y in loop:
        if y > 0:
            terms.append((1, list(p), [y]))
            p = p + [y]
        else:
            p = p + [y]
            terms.append((-1, list(p), [-y]))
    return terms


def normalized(zab, u, loop):
    """the cocycle of the class with z(loop) = 0: z - delta x, x = (V(loop) - 1)^-1 z(loop)"""
    zr = SR.cocycle_on_word(zab, u, loop)
    x = np.linalg.solve(word_matrix(u, loop) - I2, zr)
    return [zab[0] - (SR.module(u, 1) - I2) @ x, zab[1] - (SR.module(u, 2) - I2) @ x]


def pairing(z1, z2, u, loop=LOOPS["[a, b]"]):
    """Q(z1, z2) = i * (z1 cup z2-bar)(fundamental chain), linear in z1, antilinear in z2"""
    n1 = normalized(z1, u, loop)
    s = 0j
    for sign, g, h in chain(loop):
        ug = SR.cocycle_on_word(n1, u, g)
        vh = SR.cocycle_on_word(z2, u, h)
        s += sign * np.vdot(word_matrix(u, g) @ vh, ug)
    return 1j * s


def pairing_trivial(za, zb, wa, wb):
    """the same chain on trivial coefficients (u(loop) = 0 automatically): i (u(a) v(b)-bar - u(aba^-1) v(a)-bar)"""
    return 1j * (za * np.conj(wb) - zb * np.conj(wa))


def block_gram(u, loop=LOOPS["[a, b]"]):
    """the 2 x 2 matrix G with Q(v, w) = w^H G v in the H^1 coordinates of CT.basis(u)"""
    B = CT.basis(u)
    e = [B[:, 2 + k] for k in (0, 1)]
    G = np.zeros((2, 2), dtype=complex)
    for k in (0, 1):
        for m in (0, 1):
            G[m, k] = pairing([e[k][0:2], e[k][2:4]], [e[m][0:2], e[m][2:4]], u, loop)
    return G


def gram_V(loop=LOOPS["[a, b]"]):
    G = np.zeros((6, 6), dtype=complex)
    for i, u in enumerate(CT.PAR):
        G[2 * i:2 * i + 2, 2 * i:2 * i + 2] = block_gram(u, loop)
    return G


def inertia(H):
    ev = np.linalg.eigvalsh((H + H.conj().T) / 2)
    return int(sum(ev > 1e-9)), int(sum(ev < -1e-9)), int(sum(abs(ev) <= 1e-9))


def on_M(m, g):
    return SR.act_matrix(CP.AUT[m], g, ZERO)


def lift_choices():
    """the pairs (lift of L, lift of R) for which the braid relation L R^-1 L = R^-1 L R^-1 holds on V"""
    out = []
    for iL, gL in enumerate(CP.extend(CP.AUT["L"])):
        for iR, gR in enumerate(CP.extend(CP.AUT["R"])):
            A, B = CT.on_V(CP.AUT["L"], gL), CT.on_V(CP.AUT["R"], gR)
            Bi = np.linalg.inv(B)
            if np.allclose(A @ Bi @ A, Bi @ A @ Bi, atol=1e-9):
                out.append(((iL, iR), gL, gR))
    return out


def restrict(C, X):
    return np.linalg.lstsq(C, X @ C, rcond=None)[0]


def triplets():
    """T and T-bar, named by Z: T is the piece on which Z = S^2 (braid lifts) acts as -i"""
    lr = [CT.on_V(CP.AUT[m], g) for m in ("L", "R") for g in CP.extend(CP.AUT[m])]
    G = CT.closure(lr)
    _, comps = CT.decompose(lr, G)
    assert len(comps) == 2 and all(C.shape[1] == 3 for C in comps)
    (_, gL, gR) = lift_choices()[0]
    A, B = CT.on_V(CP.AUT["L"], gL), CT.on_V(CP.AUT["R"], gR)
    S = np.linalg.inv(A @ np.linalg.inv(B) @ A)
    Z = S @ S
    named = {}
    for C in comps:
        z = restrict(C, Z)
        assert np.allclose(z, z[0, 0] * np.eye(3), atol=1e-8), "Z is not a scalar on a triplet"
        named["T" if abs(z[0, 0] + 1j) < 1e-8 else "T-bar"] = C
    assert set(named) == {"T", "T-bar"}
    return named, len(G)


def controls():
    out = {}
    rng = np.random.default_rng(21)
    # (1) the Riemann bilinear form on trivial coefficients
    tau = complex(0.31, 1.27)
    out["(1) trivial coefficients: Q(dz, dz) = 2 Im tau"] = bool(
        abs(pairing_trivial(1, tau, 1, tau) - 2 * tau.imag) < 1e-12)
    # (2) hermitian, and independent of the cocycles chosen
    herm, indep = True, True
    for u in CT.PAR + [ZERO]:
        G = block_gram(u)
        herm &= bool(np.allclose(G, G.conj().T, atol=1e-10))
        for _ in range(3):
            z1 = [rng.normal(size=2) + 1j * rng.normal(size=2) for _ in (0, 1)]
            z2 = [rng.normal(size=2) + 1j * rng.normal(size=2) for _ in (0, 1)]
            x = rng.normal(size=2) + 1j * rng.normal(size=2)
            y = rng.normal(size=2) + 1j * rng.normal(size=2)
            dx = [(SR.module(u, 1) - I2) @ x, (SR.module(u, 2) - I2) @ x]
            dy = [(SR.module(u, 1) - I2) @ y, (SR.module(u, 2) - I2) @ y]
            q = pairing(z1, z2, u)
            indep &= bool(abs(pairing([z1[0] + dx[0], z1[1] + dx[1]], z2, u) - q) < 1e-9)
            indep &= bool(abs(pairing(z1, [z2[0] + dy[0], z2[1] + dy[1]], u) - q) < 1e-9)
    out["(2) hermitian on every parity and on M"] = herm
    out["(2) independent of the cocycles chosen"] = indep
    # (3) three fundamental chains agree
    G0 = gram_V()
    out["(3) the three chains of the puncture loop agree on V"] = bool(
        all(np.allclose(gram_V(lp), G0, atol=1e-9) for lp in LOOPS.values()))
    out["(3) ... and on M"] = bool(
        all(np.allclose(block_gram(ZERO, lp), block_gram(ZERO), atol=1e-9) for lp in LOOPS.values()))
    # (4) invariance under L, R and the sign with every lift; the swap reverses Q
    inv = {}
    for m in ("L", "R", "-I"):
        inv[m] = bool(all(np.allclose(M.conj().T @ G0 @ M, G0, atol=1e-9)
                          for M in (CT.on_V(CP.AUT[m], g) for g in CP.extend(CP.AUT[m]))))
    GM = block_gram(ZERO)
    for m in ("L", "R", "-I"):
        inv[m + " on M"] = bool(all(np.allclose(M.conj().T @ GM @ M, GM, atol=1e-9)
                                    for M in (on_M(m, g) for g in CP.extend(CP.AUT[m]))))
    out["(4) Q invariant under each move, every lift"] = inv
    out["(4) the swap P reverses Q on V"] = bool(all(np.allclose(M.conj().T @ G0 @ M, -G0, atol=1e-9)
                                                    for M in (CT.on_V(CP.AUT["P"], g)
                                                              for g in CP.extend(CP.AUT["P"]))))
    out["(4) ... and on M"] = bool(all(np.allclose(M.conj().T @ GM @ M, -GM, atol=1e-9)
                                       for M in (on_M("P", g) for g in CP.extend(CP.AUT["P"]))))
    # (5) signature
    out["(5) signature on V (+, -, 0)"] = inertia(G0)
    out["(5) signature on M (+, -, 0)"] = inertia(GM)
    # (6) T and T-bar orthogonal
    named, order = triplets()
    out["(6) T and T-bar are Q-orthogonal"] = bool(
        np.allclose(named["T-bar"].conj().T @ G0 @ named["T"], 0, atol=1e-9))
    out["the group of L and R on V (order)"] = order
    out["braid-consistent lift choices (indices into the lifts of L, R)"] = [list(c[0]) for c in lift_choices()]
    ok = (out["(1) trivial coefficients: Q(dz, dz) = 2 Im tau"] and herm and indep
          and out["(3) the three chains of the puncture loop agree on V"] and out["(3) ... and on M"]
          and all(inv.values()) and out["(4) the swap P reverses Q on V"] and out["(4) ... and on M"]
          and out["(5) signature on V (+, -, 0)"] == (3, 3, 0) and out["(5) signature on M (+, -, 0)"] == (1, 1, 0)
          and out["(6) T and T-bar are Q-orthogonal"] and order == 96)
    out["every control holds"] = bool(ok)
    return out


def turns(z):
    return round((cmath.phase(z) / (2 * cmath.pi)) % 1.0, 9)


def readout():
    G0 = gram_V()
    GM = block_gram(ZERO)
    named, _ = triplets()
    res = {}
    # (1) the sign of Q on each triplet
    signs = {}
    for name, C in named.items():
        ev = np.linalg.eigvalsh(C.conj().T @ G0 @ C)
        signs[name] = {"eigenvalues of Q on it (any basis; the signs are what count)": [round(float(e), 9) for e in ev],
                       "definite": bool(all(ev > 1e-9) or all(ev < -1e-9)),
                       "sign": "+" if all(ev > 1e-9) else ("-" if all(ev < -1e-9) else "indefinite")}
    res["(1) Q on the triplets"] = signs
    hol = [n for n, s in signs.items() if s["sign"] == "+"]
    res["(1) the holomorphic triplet (Q > 0)"] = hol[0] if len(hol) == 1 else None
    if len(hol) != 1:
        return res
    Th = named[hol[0]]
    # one line per parity: the holomorphic triplet meets each parity's block in a line
    per_block = []
    for i in range(3):
        P = np.zeros((6, 6))
        P[2 * i:2 * i + 2, 2 * i:2 * i + 2] = np.eye(2)
        per_block.append(int(np.linalg.matrix_rank(P @ Th, tol=1e-8)))
    res["(1) the holomorphic triplet's rank in each parity's block"] = per_block
    rows = []
    for (idx, gL, gR) in lift_choices():
        row = {"lifts (L, R)": list(idx)}
        A, B = CT.on_V(CP.AUT["L"], gL), CT.on_V(CP.AUT["R"], gR)
        S = np.linalg.inv(A @ np.linalg.inv(B) @ A)
        Z = S @ S
        zT = restrict(Th, Z)
        row["(3) Z on the holomorphic triplet (turns)"] = turns(zT[0, 0])
        # (2) the spin doublet M: its two lines, Q on each, the holomorphic line's character
        AM, BM = on_M("L", gL), on_M("R", gR)
        assert np.allclose(AM @ BM, BM @ AM, atol=1e-9), "L and R do not commute on M"
        w, U = np.linalg.eig(AM + 0.37 * BM)
        lines = []
        for k in range(2):
            v = U[:, k:k + 1]
            q = float((v.conj().T @ GM @ v).real[0, 0])
            lines.append({"Q": q, "L": complex(restrict(v, AM)[0, 0]), "R": complex(restrict(v, BM)[0, 0]),
                          "Z": complex(restrict(v, np.linalg.matrix_power(
                              np.linalg.inv(AM @ np.linalg.inv(BM) @ AM), 2))[0, 0])})
        hl = [ln for ln in lines if ln["Q"] > 1e-9]
        assert len(hl) == 1
        mu = hl[0]
        j = int(round(turns(mu["L"]) * 24)) % 24
        row["(2) M's holomorphic line: mu(L), mu(R), Z (turns)"] = [turns(mu["L"]), turns(mu["R"]), turns(mu["Z"])]
        row["(2) mu = chi_eta^j, j (mod 24)"] = j
        row["(2) mu(R) = mu(L)^-1 (a character of the braid group)"] = bool(abs(mu["L"] * mu["R"] - 1) < 1e-9)
        row["(2) M's other line: Q < 0"] = bool([ln for ln in lines if ln is not mu][0]["Q"] < -1e-9)
        # (4) the holomorphic triplet over mu: P = mu^-1 T_hol, through S4?
        PL, PR = restrict(Th, A) / mu["L"], restrict(Th, B) / mu["R"]
        PS = np.linalg.inv(PL @ np.linalg.inv(PR) @ PL)
        grp = [np.eye(3, dtype=complex)]
        seen = {tuple(np.round(np.eye(3).flatten(), 5))}
        fr = list(grp)
        while fr:
            nx = []
            for X in fr:
                for g in (PL, PR):
                    Y = X @ g
                    k = tuple(np.round(Y.flatten(), 5))
                    if k not in seen:
                        seen.add(k)
                        grp.append(Y)
                        nx.append(Y)
            fr = nx
            assert len(grp) < 10000
        I3 = np.eye(3)
        row["(4) P = mu^-1 T_hol: order of its group"] = len(grp)
        row["(4) P(L)^4 = 1, P(S)^2 = 1, (P(S) P(L))^3 = 1"] = [
            bool(np.allclose(np.linalg.matrix_power(PL, 4), I3, atol=1e-8)),
            bool(np.allclose(PS @ PS, I3, atol=1e-8)),
            bool(np.allclose(np.linalg.matrix_power(PS @ PL, 3), I3, atol=1e-8))]
        row["(4) traces of P at S, L, SL (a transposition, a 4-cycle, a 3-cycle)"] = [
            round(float(np.trace(PS).real), 9), round(float(np.trace(PL).real), 9),
            round(float(np.trace(PS @ PL).real), 9)]
        row["(4) P's characters are real"] = bool(all(abs(np.trace(X).imag) < 1e-8 for X in grp))
        rows.append(row)
    res["per braid-consistent lift choice"] = rows
    tr = rows[0]["(4) traces of P at S, L, SL (a transposition, a 4-cycle, a 3-cycle)"]
    res["(4) P is S4's"] = ("3 (the standard: transpositions are reflections)" if tr == [1.0, -1.0, 0.0] else
                           "3' (the rotations: 4-cycles are quarter turns)" if tr == [-1.0, 1.0, 0.0] else str(tr))
    return res


if __name__ == "__main__":
    c = controls()
    print(json.dumps(c, indent=1))
    if "--controls" in sys.argv:
        sys.exit(0 if c["every control holds"] else 1)
    assert c["every control holds"], "a control failed: no read-out"
    r = readout()
    out = {"rule": "W21_RULE.md (committed before this ran)", "controls": c, "read-out": r}
    with open(HERE / "the_holomorphic_triplet.json", "w") as f:
        json.dump(out, f, indent=1, ensure_ascii=False)
    print(json.dumps(r, indent=1, ensure_ascii=False))
