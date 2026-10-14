#!/usr/bin/env python3
"""W21, a second route (after the read-out): THE HOLOMORPHIC TRIPLET FROM THE ACTUAL PERIODS.

W21's read-out found T holomorphic by the sign of the topological Hodge-Riemann form Q. This route uses no sign
convention of Q: it writes down the holomorphic twisted forms on the fibre E_tau minus the puncture and integrates them.

The form. For the common point rho_Q (a -> i, b -> j), F = (f(z), f(z + tau)) dz with
    f(z) = theta_3(z | 2 tau) / sqrt(theta_1(z | tau)),
continued along straight paths from a base point x0 = 0.3305 + 0.3458 tau, is holomorphic, square-integrable at the
lattice points (a square-root pole), and satisfies F(z + 1) = rho_Q(a) F(z) and F(z + tau) = rho_Q(b) F(z) along the
segments that represent a and b. (Of the four theta numerators only theta_3(z | 2 tau) gives both; it is checked at
every tau.) Since h^(1,0) = 1, it spans the holomorphic line of the spin doublet. In each parity's block the form is
C_p F, with C_p in Q8 conjugating rho_Q to chi_p (x) rho_Q (j, i and ij for the parities (1/2, 0), (0, 1/2), (1/2, 1/2)).

The read-outs, at three values of tau with the base point at fixed fractions of the periods (so one marking):
    - the periods z(a), z(b) of each form, written in V's coordinates: the holomorphic subspace of V;
    - whether it is T or T-bar (rank tests), and whether it is the same subspace at every tau;
    - Q on it, and, at the first tau, the twisted Riemann bilinear relation Q(z, z) = 2 int_E |F|^2, the integral done
      in polar coordinates about the puncture.

    python3 the_holomorphic_triplet_periods.py   ->  the_holomorphic_triplet_periods.json beside it
"""
import json
import sys
from pathlib import Path

import mpmath as mp
import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import the_chiral_triplet as CT  # noqa: E402
import the_holomorphic_triplet as HT  # noqa: E402
import the_spin_room as SR  # noqa: E402

mp.mp.dps = 20
RQ = {"a": SR.module((0, 0), 1), "b": SR.module((0, 0), 2)}
CONJ = {(2, 0): RQ["b"], (0, 2): RQ["a"], (2, 2): RQ["a"] @ RQ["b"]}
ALPHA, BETA = 0.3305, 0.3458
TAUS = (complex(0.23, 1.07), complex(-0.41, 0.83), complex(0.12, 2.31))


def thetas(tau):
    q = mp.exp(1j * mp.pi * mp.mpc(tau))
    return (lambda z: mp.jtheta(1, mp.pi * z, q)), (lambda n, z: mp.jtheta(n, mp.pi * z, q ** 2))


def periods(tau, n=2000):
    tau = mp.mpc(tau)
    th1, thN = thetas(tau)
    x0 = ALPHA + BETA * tau

    def path(z0, z1):
        return [z0 + (z1 - z0) * k / n for k in range(n + 1)]

    def cont(zs, s0):
        out = [s0]
        for z in zs[1:]:
            r = mp.sqrt(th1(z))
            out.append(-r if abs(r - out[-1]) > abs(r + out[-1]) else r)
        return out

    def simpson(v, zs):
        h = (zs[-1] - zs[0]) / (len(zs) - 1)
        return (v[0] + v[-1] + 4 * sum(v[1:-1:2]) + 2 * sum(v[2:-1:2])) * h / 3

    s0 = mp.sqrt(th1(x0))
    Pu, Pu2, Pa, Pa2 = path(x0, x0 + tau), path(x0 + tau, x0 + 2 * tau), path(x0, x0 + 1), path(x0 + tau, x0 + tau + 1)
    Su = cont(Pu, s0)
    Su2, Sa, Sa2 = cont(Pu2, Su[-1]), cont(Pa, s0), cont(Pa2, Su[-1])
    equiv = {}
    for m in (1, 2, 3, 4):
        F0 = np.array([complex(thN(m, x0) / s0), complex(thN(m, x0 + tau) / Su[-1])])
        Fa = np.array([complex(thN(m, Pa[-1]) / Sa[-1]), complex(thN(m, Pa2[-1]) / Sa2[-1])])
        Fb = np.array([complex(thN(m, Pu[-1]) / Su[-1]), complex(thN(m, Pu2[-1]) / Su2[-1])])
        equiv[m] = bool(np.allclose(Fa, RQ["a"] @ F0, atol=1e-10) and np.allclose(Fb, RQ["b"] @ F0, atol=1e-10))

    def f(zs, ss):
        return [thN(3, z) / s for z, s in zip(zs, ss)]

    za = np.array([complex(simpson(f(Pa, Sa), Pa)), complex(simpson(f(Pa2, Sa2), Pa))])
    zb = np.array([complex(simpson(f(Pu, Su), Pu)), complex(simpson(f(Pu2, Su2), Pu))])
    return za, zb, equiv


def reduced_basis(tau):
    """a Lagrange-Gauss reduced basis (w1, w2) of the lattice Z + tau Z (same lattice, so the same torus)"""
    w1, w2 = complex(1), complex(tau)
    while True:
        if abs(w2) < abs(w1):
            w1, w2 = w2, w1
        n = round((w2 / w1).real)
        if n == 0:
            return w1, w2
        w2 = w2 - n * w1


def l2_norm(tau, npts=48):
    """2 int_E (|f(z)|^2 + |f(z + tau)|^2) dx dy over a parallelogram centred on the puncture, polar in (s, t).

    The integrand is periodic on the lattice Z + tau Z (F's monodromy is unitary), so any fundamental parallelogram
    gives the same integral. It is taken on a reduced basis of the lattice: on the skewed (1, tau) parallelogram the
    polar quadrature loses accuracy at small Im tau (2.7e-11 at Im tau = 0.159, 5e-7 at 0.049; found by the independent
    review of 2026-10-08). The caller's mpmath precision is restored on return.
    """
    th1, thN = thetas(tau)
    w1, w2 = reduced_basis(tau)
    xs, ws = np.polynomial.legendre.leggauss(npts)
    total = 0.0
    with mp.workdps(15):
        for k in range(4):
            a0, a1 = -np.pi / 4 + k * np.pi / 2, np.pi / 4 + k * np.pi / 2
            for xt, wt in zip(xs, ws):
                th = (a1 - a0) / 2 * xt + (a1 + a0) / 2
                R = 0.5 / max(abs(np.cos(th)), abs(np.sin(th)))
                for xr, wr in zip(xs, ws):
                    r = R / 2 * (xr + 1)
                    z = r * np.cos(th) * w1 + r * np.sin(th) * w2
                    h = abs(thN(3, z)) ** 2 / abs(th1(z)) + abs(thN(3, z + tau)) ** 2 / abs(th1(z + tau))
                    total += wt * (a1 - a0) / 2 * wr * R / 2 * float(h) * r
    return 2 * total * tau.imag


def run():
    for u, C in CONJ.items():
        for x in (1, 2):
            assert np.allclose(C @ SR.module((0, 0), x) @ np.linalg.inv(C), SR.module(u, x)), (u, x)
    named, _ = HT.triplets()
    G = HT.gram_V()
    GM = HT.block_gram((0, 0))
    rows, spans, rel = [], [], None
    for k, tau in enumerate(TAUS):
        za, zb, equiv = periods(tau)
        cols = []
        for i, u in enumerate(CT.PAR):
            C = CONJ[u]
            c = np.linalg.solve(CT.basis(u), np.concatenate([C @ za, C @ zb]))
            v = np.zeros(6, dtype=complex)
            v[2 * i:2 * i + 2] = c[2:4]
            cols.append(v)
        H = np.array(cols).T
        spans.append(H)
        cM = np.linalg.solve(CT.basis((0, 0)), np.concatenate([za, zb]))[2:4]
        row = {"tau": [tau.real, tau.imag],
               "which theta numerators give rho_Q's monodromy (1..4)": [m for m, ok in equiv.items() if ok],
               "the holomorphic subspace is inside T": bool(np.linalg.matrix_rank(np.hstack([named["T"], H]), tol=1e-7) == 3),
               "... meets T-bar only in 0": bool(np.linalg.matrix_rank(np.hstack([named["T-bar"], H]), tol=1e-7) == 6),
               "Q on the holomorphic forms (eigenvalues)": [round(float(e), 9) for e in np.linalg.eigvalsh(H.conj().T @ G @ H)],
               "Q on the spin doublet's holomorphic form": round(float((cM.conj() @ GM @ cM).real), 12)}
        if k == 0:
            l2, qm = l2_norm(tau), float((cM.conj() @ GM @ cM).real)
            row["2 int_E |F|^2 (the twisted Riemann bilinear relation)"] = round(float(l2), 12)
            rel = abs(l2 - qm) / qm
        rows.append(row)
    same = [bool(np.linalg.matrix_rank(np.hstack([spans[0], S]), tol=1e-7) == 3) for S in spans[1:]]
    r0 = rows[0]
    out = {"route": "the actual holomorphic twisted forms and their periods (after W21's read-out)",
           "rows": rows,
           "the holomorphic subspace is the same at every tau": all(same),
           "the holomorphic subspace is T at every tau": all(r["the holomorphic subspace is inside T"] and
                                                            r["... meets T-bar only in 0"] for r in rows),
           "theta_3(z | 2 tau) alone gives the monodromy at every tau": all(
               r["which theta numerators give rho_Q's monodromy (1..4)"] == [3] for r in rows),
           "the twisted Riemann bilinear relation at the first tau (relative error)": float(f"{rel:.3g}")}
    return out


if __name__ == "__main__":
    res = run()
    with open(HERE / "the_holomorphic_triplet_periods.json", "w") as f:
        json.dump(res, f, indent=1, ensure_ascii=False)
    print(json.dumps({k: v for k, v in res.items() if k != "rows"}, indent=1))
    for r in res["rows"]:
        print(r)
