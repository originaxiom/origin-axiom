#!/usr/bin/env python3
"""W10 of the weave: the parity-twisted spin space, its group, and the chiral triplet (design-time structure, no count).

The space is V = H1(F2; chi_1 (x) rho_Q) + H1(F2; chi_2 (x) rho_Q) + H1(F2; chi_3 (x) rho_Q), the three parity-twisted spin
doublets of W9: six-dimensional and the same for every thread. A move m with a lift g sends H1(chi (x) rho_Q) to
H1((chi o m) (x) rho_Q) by z -> g^-1 (z o m), so the moves act on V, permuting the parities.

What it computes:
  (1) the group the moves generate on V: with L and R (and the sign), and with all four;
  (2) its commutant and the decomposition of V: the dimensions of the pieces, whether their characters are real, and
      whether they are complex conjugates of each other;
  (3) on every state of GENESIS to length 6 at its resolving tick (the deck-compatible act, the inherited lift), the
      eigenvalues of the act on each piece: when the two pieces sit at different kappa, a single kappa carries one
      piece alone.
The groups are finite, so every thread at every tick acts on V with finite order and carries interior classes there
(each class is interior, because rho_Q([a, b]) = -1).

    python3 the_chiral_triplet.py   ->  the_chiral_triplet.json beside it
"""
import cmath
import json
import sys
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import the_common_point as CP  # noqa: E402
import the_spin_room as SR  # noqa: E402
import the_parity_sectors as S  # noqa: E402

PAR = [(2, 0), (0, 2), (2, 2)]                 # (1/2, 0), (0, 1/2), (1/2, 1/2) as exponents of i on a, b
NAMES = ["(1/2, 0)", "(0, 1/2)", "(1/2, 1/2)"]
I2 = np.eye(2, dtype=complex)


def basis(u):
    """B^1 then a fixed complement in Z^1 = C^4"""
    Bm = np.vstack([SR.module(u, 1) - I2, SR.module(u, 2) - I2])
    Q, _ = np.linalg.qr(np.hstack([Bm, np.eye(4)]))
    return np.hstack([Bm, Q[:, 2:4]])


def u_after(u, phi):
    out = []
    for x in (1, 2):
        out.append(sum(u[abs(y) - 1] * (1 if y > 0 else -1) for y in phi[x]) % 4)
    return tuple(out)


def on_V(phi, g):
    """the 6 x 6 matrix of z -> g^-1 (z o phi) on V, blocks between the parities"""
    gi = np.linalg.inv(SR.qmat(g))
    M = np.zeros((6, 6), dtype=complex)
    for i, u in enumerate(PAR):
        up = u_after(u, phi)
        Bu, Bup = basis(u), basis(up)
        cols = []
        for k in (2, 3):
            e = Bu[:, k]
            img = np.concatenate([gi @ SR.cocycle_on_word([e[0:2], e[2:4]], u, phi[x]) for x in (1, 2)])
            cols.append(np.linalg.solve(Bup, img)[2:4])
        j = PAR.index(up)
        M[2 * j:2 * j + 2, 2 * i:2 * i + 2] = np.array(cols).T
    return M


def key(M):
    return tuple(np.round(M.flatten(), 5).tolist())


def closure(gens):
    G = {key(np.eye(6, dtype=complex)): np.eye(6, dtype=complex)}
    fr = list(G.values())
    while fr:
        nx = []
        for A in fr:
            for g in gens:
                B = A @ g
                if key(B) not in G:
                    G[key(B)] = B
                    nx.append(B)
        fr = nx
    return list(G.values())


def decompose(gens, G):
    rows = [np.kron(g.T, np.eye(6)) - np.kron(np.eye(6), g) for g in gens]
    _, s, vh = np.linalg.svd(np.vstack(rows))
    dim = int(sum(s < 1e-8))
    out = {"commutant dimension": dim}
    if dim == 1:
        out["pieces"] = [{"dimension": 6}]
        return out, [np.eye(6, dtype=complex)]
    X = (vh[-1] + 0.37 * vh[-2]).conj().reshape(6, 6, order="F")
    w, V = np.linalg.eig(X)
    vals = []
    for z in w:
        if not any(abs(z - v) < 1e-5 for v in vals):
            vals.append(z)
    comps = [V[:, [i for i in range(6) if abs(w[i] - v) < 1e-5]] for v in vals]
    chars = [[np.trace(np.linalg.lstsq(C, A @ C, rcond=None)[0]) for A in G] for C in comps]
    out["pieces"] = [{"dimension": C.shape[1], "character real": bool(all(abs(c.imag) < 1e-6 for c in ch)),
                      "irreducible (norm 1)": bool(abs(sum(abs(c) ** 2 for c in ch) / len(G) - 1) < 1e-6)}
                     for C, ch in zip(comps, chars)]
    if len(chars) == 2:
        out["the two pieces are complex conjugates"] = bool(all(abs(a - np.conj(b)) < 1e-6 for a, b in zip(*chars)))
    return out, comps


def power(phi, k):
    out = {1: [1], 2: [2]}
    for _ in range(k):
        out = CP.compose(out, phi)
    return out


def qpow(g, k):
    q = (1.0, 0.0, 0.0, 0.0)
    for _ in range(k):
        q = CP.qmul(q, g)
    return q


def run():
    res = {}
    lr = [on_V(CP.AUT[m], g) for m in ("L", "R") for g in CP.extend(CP.AUT[m])]
    G_lr = closure(lr)
    dec, comps = decompose(lr, G_lr)
    res["(1, 2) L and R"] = {"order": len(G_lr), **dec}
    lrs = lr + [on_V(CP.AUT["-I"], g) for g in CP.extend(CP.AUT["-I"])]
    G_lrs = closure(lrs)
    res["(1) L, R and the sign"] = {"order": len(G_lrs), "the same group": bool(len(G_lrs) == len(G_lr))}
    allm = lrs + [on_V(CP.AUT["P"], g) for g in CP.extend(CP.AUT["P"])]
    G_all = closure(allm)
    d_all, _ = decompose(allm, G_all)
    res["(1, 2) all four moves"] = {"order": len(G_all), **d_all}
    # (3) every state at its resolving tick: the act on V, and on each piece
    T, Tb = comps if len(comps) == 2 else (None, None)
    states, tally = [], {"states": 0, "the two pieces at different kappa": 0}
    for sw in S.states():
        sign = 1 if sw[0] == "+" else -1
        w = sw[1:]
        k = S.resolving_tick(w)
        phi1 = CP.word_aut(w, sign)
        phik = power(phi1, k)
        per_lift = []
        for g in CP.extend(phi1):
            A = on_V(phik, qpow(g, k))
            # the act fixes each parity at the resolving tick: block diagonal
            assert all(np.allclose(A[2 * i:2 * i + 2, 2 * j:2 * j + 2], 0, atol=1e-8)
                       for i in range(3) for j in range(3) if i != j)
            eT = np.linalg.eigvals(np.linalg.lstsq(T, A @ T, rcond=None)[0])
            eTb = np.linalg.eigvals(np.linalg.lstsq(Tb, A @ Tb, rcond=None)[0])
            def eighths(ev):
                return sorted(int(round(cmath.phase(z) / (2 * cmath.pi) * 8)) % 8 for z in ev)
            per_lift.append({"kappa on the first triplet (eighths)": eighths(eT),
                             "kappa on the second triplet (eighths)": eighths(eTb)})
        apart = bool(all(set(p["kappa on the first triplet (eighths)"]).isdisjoint(p["kappa on the second triplet (eighths)"])
                    for p in per_lift))
        tally["states"] += 1
        tally["the two pieces at different kappa"] += int(apart)
        states.append({"state": sw, "resolving tick": k, "lifts": per_lift, "the two triplets at different kappa": apart})
        print(sw, k, per_lift, apart, flush=True)
    res["(3) every state at its resolving tick"] = states
    res["tally"] = tally
    return res


if __name__ == "__main__":
    out = run()
    with open(HERE / "the_chiral_triplet.json", "w") as f:
        json.dump(out, f, indent=1)
    for k in ("(1, 2) L and R", "(1) L, R and the sign", "(1, 2) all four moves", "tally"):
        print(k, json.dumps(out[k]))
