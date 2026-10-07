#!/usr/bin/env python3
"""W12 of the weave: the joined vacuum, a thread's geometry tensored with the weave's common point, has no interior class.

The module. On a state M at tick k, A = lambda (x) rho_hyp (x) rho_Q:
  - rho_hyp is a lift to SL(2, C) of M's holonomy (sm:B1527's hyperbolic_sl2 at 60 digits, read in the weave's marking);
  - rho_Q is the common point a -> i, b -> j with a lift g of the stable letter (W3);
  - lambda is a parity character on the fibre and kappa on the stable letter.
This is the vacuum the relay THE CHIRAL TRIPLET'S COUNT named as the next read. Its puncture acts by (-U) (x) (-1) = U,
which fixes a vector, so W11's theorem does not apply to it.

The statement (PROVED, from the literature). n(A) = 0: no class of H^1(M; A) is interior. So F-HE, which extends by an
interior class, reads nothing at this vacuum, on any state at any tick.

The proof.
  (i)  By Shapiro's lemma, H^*(M; A) is a summand of H^*(N; rho_hyp), where N is the finite cover on which lambda (x)
       rho_Q is trivial. Restriction to the boundary is compatible with this.
  (ii) On a complete hyperbolic 3-manifold of finite volume, restriction H^1(N; rho_n) -> H^1(dN; rho_n) is injective
       for the n-dimensional representation composed with any lift of the holonomy (Menal-Ferrer and Porti, "Twisted
       cohomology for hyperbolic three manifolds", Osaka J. Math. 49 (2012)). For n = 2 this is rho_hyp itself.
  (iii) So the interior part of H^1(M; A), a summand of the interior part of H^1(N; rho_hyp), is zero.
The frame's own module at the hyperbolic point is the balanced four rho_hyp (x) conj(rho_hyp), whose cuspidal
cohomology need not vanish. That is where the record's members live.

What this script checks (50 digits, sm:B1549's cohomology three_lib.cohom on this file's presentation
<a, b, t | t x t^-1 = phi^k(x)>, peripheral pair ([a, b], u^-1 t)):
  on every state of GENESIS to length 6 (24), at tick 1 and at its resolving tick, for both signs of the stable letter's
  holonomy and both lifts of the common point, at every parity that is a character at that tick:
  - at every kappa in mu_24 where the peripheral torus fixes a vector of A (the only kappa where H^1 can be non-zero:
    the eigenvalues of rho_Q(u^-1 t) lie in mu_8 or mu_6), h1 = r1 = h0(T; A) and n = 0;
  - at two controls, kappa = exp(2 pi i / 7) and kappa = 2, h1 = 0.

    python3 the_joined_vacuum.py   ->  the_joined_vacuum.json beside it
"""
import json
import sys
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(ROOT / "frontier" / "B1552_the_chiral_triplets_count" / "verification"))
import chiral_lib as CL  # noqa: E402  (the states, the moves, the lifts, sm:B1549's three_lib)
import the_parity_sectors as S  # noqa: E402

T, CP = CL.T, CL.CP
mp.mp.dps = 50
T.DPS = 50


def tr3(A, B):
    return [A[0, 0] + A[1, 1], B[0, 0] + B[1, 1], (A * B)[0, 0] + (A * B)[1, 1]]


def mword(w, A, B):
    X = mp.eye(2)
    for x in w:
        X = X * {1: A, 2: B, -1: A ** -1, -2: B ** -1}[x]
    return X


def marked_holonomy(sw, phi):
    """rho_hyp on a, b in the weave's marking: the pair whose character phi fixes"""
    A0, B0, _, _ = T.family_lib().hyperbolic_sl2(sw[0], sw[1:])
    mp.mp.dps = 50
    for A, B in ((B0, A0), (A0, B0), (A0, B0 ** -1), (B0, A0 ** -1)):
        d = max(abs(x - y) for x, y in zip(tr3(mword(phi[1], A, B), mword(phi[2], A, B)), tr3(A, B)))
        if d < mp.mpf(10) ** -40:
            return A, B
    raise RuntimeError("no marking of the holonomy is fixed by the state's automorphism: " + sw)


def stable_letter(phi, A, B):
    """T with T x T^-1 = rho(phi(x)), det T = 1 (one of the two signs)"""
    Ap, Bp = mword(phi[1], A, B), mword(phi[2], A, B)
    rows = []
    for X, Xp in ((A, Ap), (B, Bp)):
        for i in range(2):
            for j in range(2):
                # (T X - Xp T)[i, j] as a linear form in T's entries t00, t01, t10, t11
                row = [mp.mpc(0)] * 4
                for l in range(2):
                    row[2 * i + l] += X[l, j]
                    row[2 * l + j] -= Xp[i, l]
                rows.append(row)
    ker, _ = T.nullspace(rows, 4)
    assert len(ker) == 1, "the stable letter is not unique up to scale"
    v = ker[0]
    Tm = mp.matrix([[v[0], v[1]], [v[2], v[3]]])
    Tm = Tm / mp.sqrt(mp.det(Tm))
    err = max(mp.mnorm(Tm * A * Tm ** -1 - Ap, 1), mp.mnorm(Tm * B * Tm ** -1 - Bp, 1))
    assert err < mp.mpf(10) ** -40, err
    return Tm


def presentation(phik):
    conv = lambda w: [(abs(x) - 1, 1 if x > 0 else -1) for x in w]   # noqa: E731
    rels = [[(2, 1), (x - 1, 1), (2, -1)] + conv(CP.inv(phik[x])) for x in (1, 2)]
    u = CL.peripheral_u(phik)
    periph = [(conv(CL.ELL), conv(CP.inv(u)) + [(2, 1)])]
    return T.Pres(3, rels, periph), u


def kron(X, Y):
    n, m = X.rows, Y.rows
    return [[X[i // m, j // m] * Y[i % m, j % m] for j in range(n * m)] for i in range(n * m)]


def peripheral_mats(mats1, u):
    """the module's matrices on the peripheral pair ([a, b], u^-1 t) at kappa = 1; kappa multiplies the second"""
    mod = T.Mod(mats1)
    conv = [(abs(x) - 1, 1 if x > 0 else -1) for x in CL.ELL]
    conv2 = [(abs(x) - 1, 1 if x > 0 else -1) for x in CP.inv(u)] + [(2, 1)]
    return mod.word(conv), mod.word(conv2)


def cusp_h0(per, kap):
    """h0 of A on the peripheral torus: common fixed vectors of A([a, b]) and kappa A(u^-1 t)"""
    X, Y = per
    e = len(X)
    rows = [[X[i][j] - (1 if i == j else 0) for j in range(e)] for i in range(e)]
    rows += [[kap * Y[i][j] - (1 if i == j else 0) for j in range(e)] for i in range(e)]
    return e - T.rank(rows, e)[0]


def run():
    QI = mp.matrix([[1j, 0], [0, -1j]])
    QJ = mp.matrix([[0, 1], [-1, 0]])
    tally = {"(state, tick)": 0, "readings with a class": 0, "n = 0 there": 0, "h1 = r1 = h0(T; A) there": 0,
             "controls": 0, "controls with h1 = 0": 0}
    states = []
    for sw in S.states(6):
        sign = 1 if sw[0] == "+" else -1
        w = sw[1:]
        phi1 = CP.word_aut(w, sign)
        A, B = marked_holonomy(sw, phi1)
        T1 = stable_letter(phi1, A, B)
        kres = S.resolving_tick(w)
        for k in sorted({1, kres}):
            phik = CL.power(phi1, k)
            P, u = presentation(phik)
            lifts = []
            for g in CP.extend(phi1):
                q = (1.0, 0.0, 0.0, 0.0)
                for _ in range(k):
                    q = CP.qmul(q, g)
                lifts.append(CL.qmat_mp(q))
            rows = []
            for eps in (1, -1):
                Tk = (eps * T1) ** k
                for li, G in enumerate(lifts):
                    for p in [(0, 0)] + CL.PARITIES:
                        found = []
                        # kappa cancels from the relators t x t^-1 phi^k(x)^-1, so one check at kappa = 1 decides
                        # whether this parity is a character at this tick
                        mats1 = [[[[(-1) ** p[0], (-1) ** p[1], 1][j] * x for x in row] for row in kron(H, Q)]
                                 for j, (H, Q) in enumerate(((A, QI), (B, QJ), (Tk, G)))]
                        if T.relator_defect(T.Mod(mats1), P) > mp.mpf(10) ** -35:
                            continue
                        per = peripheral_mats(mats1, u)
                        for e in list(range(24)) + ["c7", "c2"]:
                            kap = mp.expjpi(mp.mpf(e) / 12) if isinstance(e, int) else (
                                mp.expjpi(mp.mpf(2) / 7) if e == "c7" else mp.mpf(2))
                            lam = [(-1) ** p[0], (-1) ** p[1], kap]
                            mats = [[[lam[j] * x for x in row] for row in kron(H, Q)]
                                    for j, (H, Q) in enumerate(((A, QI), (B, QJ), (Tk, G)))]
                            mod = T.Mod(mats)
                            if isinstance(e, int):
                                t0 = cusp_h0(per, kap)
                                if t0 == 0:
                                    continue
                                s = T.cohom(mod, P)
                                tally["readings with a class"] += int(s["h1"] > 0)
                                tally["n = 0 there"] += int(s["h1"] > 0 and s["n"] == 0)
                                tally["h1 = r1 = h0(T; A) there"] += int(s["h1"] == s["r1"] == t0)
                                found.append({"kappa (24ths)": e, "h0(T; A)": t0,
                                              "(h0, h1, r1, n)": [s["h0"], s["h1"], s["r1"], s["n"]]})
                            else:
                                s = T.cohom(mod, P)
                                tally["controls"] += 1
                                tally["controls with h1 = 0"] += int(s["h1"] == 0)
                        if found:
                            rows.append({"stable letter sign": eps, "lift": li, "parity": list(p), "readings": found})
            tally["(state, tick)"] += 1
            states.append({"state": sw, "tick": k, "rows": rows})
            print(sw, k, sum(len(r["readings"]) for r in rows), json.dumps(tally), flush=True)
    return {"tally": tally, "states": states,
            "all held": bool(tally["readings with a class"] == tally["n = 0 there"] == tally["h1 = r1 = h0(T; A) there"]
                             and tally["controls"] == tally["controls with h1 = 0"] and tally["readings with a class"] > 0)}


if __name__ == "__main__":
    out = run()
    with open(HERE / "the_joined_vacuum.json", "w") as f:
        json.dump(out, f, indent=1)
    print(json.dumps(out["tally"]), "all held:", out["all held"])
