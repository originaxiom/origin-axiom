#!/usr/bin/env python3
"""R16 of the weave's laws, reduced: the room of the weave's spin vacuum, on every thread at once (design-time structure,
no count).

The frame at the weave's vacuum (W8) reads rank-one lines on every tick and, by Lemma V, never an interior one. On the
forced spin cover (W3's kernel of the common point, fibre genus 3) its lines are the cover's own characters, and by
Shapiro a character pulled back from the thread reads, among the irreducible representations sigma of the image, the
spin ones: H^1(M; nu (x) rho_Q (x) ...). The rank-one sigma are excluded by Lemma V. So the room of the weave's vacuum
on its forced spin cover is the twisted cohomology of each thread with coefficients in the common point itself.

For the module u (x) rho_Q on the fibre group F2 (u a character of the fibre that the act fixes, of order dividing 4;
rho_Q(a) = i, rho_Q(b) = j) and an extension t -> kappa g (g in 2O with g rho_Q(x) g^-1 = rho_Q(phi(x)), W3):
  - H^0(F2; u (x) rho_Q) = 0, so H^1 is two-dimensional (the free group of rank two);
  - the act gives S: [z] -> [g^-1 (z o phi)] on it, and H^1(M; nu (x) rho) = ker(S - kappa);
  - every such class is interior: rho_Q([a, b]) = -1, so the module has no invariant vector on the cusp, and H^1 of the
    cusp torus vanishes.
So the members are exactly the kappa that are eigenvalues of S and roots of unity. The two choices +-g change S to -S.

The rule, named before the run: every state of GENESIS to length 6 (24), its automorphism as the_common_point.py
composes it, every extension g in 2O, every fibre character u of order dividing 4 fixed by the act; the eigenvalues of
S, and which are roots of unity of order dividing 24. One pass.

    python3 the_spin_room.py   ->  the_spin_room.json beside it
"""
import cmath
import json
import sys
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import the_common_point as CP  # noqa: E402  (the moves as automorphisms, 2O, the extension of the common point)
import the_parity_sectors as S  # noqa: E402  (the state list)

I2 = np.eye(2, dtype=complex)
QM = {"1": I2, "i": np.array([[1j, 0], [0, -1j]]), "j": np.array([[0, 1], [-1, 0]], dtype=complex),
      "k": np.array([[0, 1j], [1j, 0]])}


def qmat(q):
    w, x, y, z = q
    return w * QM["1"] + x * QM["i"] + y * QM["j"] + z * QM["k"]


RHO = {1: QM["i"], 2: QM["j"]}


def char_val(u, x):
    """u = (e_a, e_b) exponents of i; the value on the generator x (+-1, +-2)"""
    e = u[abs(x) - 1] * (1 if x > 0 else -1)
    return 1j ** (e % 4)


def module(u, x):
    """(u (x) rho_Q)(x) for a letter x"""
    M = RHO[abs(x)] if x > 0 else np.linalg.inv(RHO[abs(x)])
    return char_val(u, x) * M


def cocycle_on_word(zab, u, w):
    """z(w) from z(a), z(b) by z(xy) = z(x) + V(x) z(y); z(x^-1) = -V(x)^-1 z(x)"""
    val = np.zeros(2, dtype=complex)
    pref = I2.copy()
    for x in w:
        if x > 0:
            zx = zab[x - 1]
        else:
            zx = -np.linalg.inv(module(u, -x)) @ zab[-x - 1]
        val = val + pref @ zx
        pref = pref @ module(u, x)
    return val


def act_matrix(phi, g, u):
    """the map z -> g^-1 (z o phi) on Z^1 = C^4 (coordinates z(a), z(b)), and the projection to H^1"""
    gi = np.linalg.inv(qmat(g))
    cols = []
    for k in range(4):
        e = np.zeros(4, dtype=complex)
        e[k] = 1
        zab = [e[0:2], e[2:4]]
        img = [gi @ cocycle_on_word(zab, u, phi[x]) for x in (1, 2)]
        cols.append(np.concatenate(img))
    A = np.array(cols).T
    # B^1: v -> ((V(a) - 1) v, (V(b) - 1) v)
    Bm = np.vstack([module(u, 1) - I2, module(u, 2) - I2])
    assert np.linalg.matrix_rank(Bm, tol=1e-9) == 2
    # a basis: B^1 then a complement; the induced map on the quotient
    Q, _ = np.linalg.qr(np.hstack([Bm, np.eye(4)]))
    basis = np.hstack([Bm, Q[:, 2:4]])
    if abs(np.linalg.det(basis)) < 1e-9:
        basis = np.hstack([Bm, np.eye(4)[:, [0, 2]]])
    C = np.linalg.solve(basis, A @ basis)
    assert np.allclose(C[2:4, 0:2], 0, atol=1e-8), "B^1 is not preserved"
    return C[2:4, 2:4]


def root_order(lam, nmax=48):
    if abs(abs(lam) - 1) > 1e-9:
        return None
    for n in range(1, nmax + 1):
        if abs(lam ** n - 1) < 1e-9:
            return n
    return None


def eighths(ev):
    """the eigenvalues as multiples of an eighth of a turn (each a root of unity of order dividing 8 here)"""
    out = []
    for e in ev:
        assert root_order(e, 8) is not None, ("not an eighth root of unity", e)
        out.append(int(round(cmath.phase(e) / (2 * cmath.pi) * 8)) % 8)
    return sorted(out)


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


def key(M):
    return tuple(np.round(M.flatten(), 6).tolist())


def group_on_doublet(names):
    gens = []
    for m in names:
        for g in CP.extend(CP.AUT[m]):
            gens.append(act_matrix(CP.AUT[m], g, (0, 0)))
    G = {key(np.eye(2, dtype=complex)): np.eye(2, dtype=complex)}
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
    orders = {}
    for A in G.values():
        P, n = A, 1
        while not np.allclose(P, np.eye(2), atol=1e-8):
            P, n = P @ A, n + 1
        orders[n] = orders.get(n, 0) + 1
    irr = sum(abs(np.trace(A)) ** 2 for A in G.values()) / len(G)
    return {"order": len(G), "element orders": dict(sorted(orders.items())), "sum |tr|^2 / order": round(irr, 6),
            "abelian": all(np.allclose(A @ B, B @ A) for A in G.values() for B in G.values())}


def fox_h1(phi, g, kap, u, k=1):
    """route 2: h1 of u (x) rho on <a, b, t | t x t^-1 = phi(x)> with t -> kap g, by Fox calculus"""
    def mod(x):
        if abs(x) in (1, 2):
            return module(u, x)
        G = kap * qmat(g)
        return G if x > 0 else np.linalg.inv(G)

    def d(word, gen):
        tot, pref = np.zeros((2, 2), dtype=complex), np.eye(2, dtype=complex)
        for x in word:
            if x == gen:
                tot = tot + pref
            elif x == -gen:
                tot = tot - pref @ np.linalg.inv(mod(gen))
            pref = pref @ mod(x)
        return tot
    rels = [[3, x, -3] + CP.inv(phi[x]) for x in (1, 2)]
    F = np.block([[d(r, gen) for gen in (1, 2, 3)] for r in rels])
    z1 = 6 - np.linalg.matrix_rank(F, tol=1e-8)
    b1 = np.linalg.matrix_rank(np.vstack([mod(x) - np.eye(2) for x in (1, 2, 3)]), tol=1e-8)
    return int(z1 - b1)


PAR = {(2, 0): "(1/2, 0)", (0, 2): "(0, 1/2)", (2, 2): "(1/2, 1/2)"}


def run():
    out = {"(A) the doublet's group": {"L and R": group_on_doublet(["L", "R"]),
                                       "L, R and the sign": group_on_doublet(["L", "R", "-I"]),
                                       "all four moves": group_on_doublet(["L", "R", "-I", "P"])}}
    states, tally = [], {"states": 0, "own tick: every lift of finite order": 0,
                         "resolving tick: the three parities alike for every inherited lift": 0}
    for sw in S.states():
        sign = 1 if sw[0] == "+" else -1
        w = sw[1:]
        k = S.resolving_tick(w)
        phi1 = CP.word_aut(w, sign)
        phik = power(phi1, k)                       # the deck-compatible tick (eps w)^k
        own, ticks = [], []
        for g in CP.extend(phi1):
            ev = np.linalg.eigvals(act_matrix(phi1, g, (0, 0)))
            own.append(eighths(ev))
            per = {nm: eighths(np.linalg.eigvals(act_matrix(phik, qpow(g, k), u))) for u, nm in PAR.items()}
            ticks.append(per)
        alike = all(len({tuple(v) for v in per.values()}) == 1 for per in ticks)
        tally["states"] += 1
        tally["own tick: every lift of finite order"] += 1
        tally["resolving tick: the three parities alike for every inherited lift"] += int(alike)
        states.append({"state": sw, "resolving tick": k,
                       "own tick, untwisted doublet: kappa (eighths of a turn) per lift": own,
                       "resolving tick, parity-twisted doublets: kappa per parity, per inherited lift": ticks,
                       "the three parities alike": alike})
        print(sw, k, own, ticks, alike, flush=True)
    # route 2, the control: h1 by Fox calculus on the bundle group at the predicted kappa
    control = []
    for sw in ("+LR", "-LR", "+LLR", "-LLRR", "+LLLR"):
        sign = 1 if sw[0] == "+" else -1
        phi1 = CP.word_aut(sw[1:], sign)
        for g in CP.extend(phi1):
            ev = eighths(np.linalg.eigvals(act_matrix(phi1, g, (0, 0))))
            for e in sorted(set(ev)):
                kap = cmath.exp(-2j * cmath.pi * e / 8)          # S z = kappa^-1-twisted convention: try both
                h_a = fox_h1(phi1, g, kap, (0, 0))
                h_b = fox_h1(phi1, g, 1 / kap, (0, 0))
                control.append({"state": sw, "eigenvalue (eighths)": e, "multiplicity": ev.count(e),
                                "route 2 h1 at kappa and at its inverse": [h_a, h_b]})
    out["(B, C) every state"] = states
    out["route 2 control"] = control
    out["tally"] = tally
    return out


if __name__ == "__main__":
    res = run()
    with open(HERE / "the_spin_room.json", "w") as f:
        json.dump(res, f, indent=1)
    print(json.dumps(res["(A) the doublet's group"]))
    print(json.dumps(res["tally"]))
    print(json.dumps(res["route 2 control"]))
