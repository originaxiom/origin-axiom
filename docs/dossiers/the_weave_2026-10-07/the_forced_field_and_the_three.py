#!/usr/bin/env python3
"""W131 — the forced field and the chiral three (the rule: W131_RULE.md, committed and pushed before this script).

  J0  the instrument (mpmath, 40 digits, at three tau): the Szego kernels S_k(z) = th_k(z) th_1'(0) / (th_k(0) th_1(z)),
      k = 2, 3, 4, with periods pi and pi tau: the residue at 0 (contour integral), oddness, S_k^2 - S_l^2 constant
      in z, and the signs under z -> z + pi and z -> z + pi tau
  J1  type (exact, sympy): E = K^(1/2) + K^(-1/2) with S+ the first summand; N maps S+ to S-; Phi*_h = conj(c) y^-2 N^T
      annihilates S+; the weights (p, q) of every pairing linear in Phi, Phi* or h
  J2  parity: End(E (x) chi) = End E; an invariant coupling needs chi_a chi_b = 1; the period signs of S_a S_b (a != b)
      against S_c's
  J3  the residue: Y_X[a][b] = (the coefficient X puts in front of S_a S_b dz) times the residue of S_a S_b at the
      puncture, by a small circle and, for a = b, by the boundary of a fundamental parallelogram (the residue theorem)
  J4  the read-out

    python3 -B the_forced_field_and_the_three.py      # writes the_forced_field_and_the_three.json beside itself
"""
import json
from pathlib import Path

import mpmath as mp
import sympy as sp

HERE = Path(__file__).resolve().parent
OUT = HERE / "the_forced_field_and_the_three.json"
mp.mp.dps = 40
BAR = mp.mpf("1e-30")
TAUS = {"i": mp.mpc(0, 1), "omega": mp.exp(2j * mp.pi / 3), "0.2 + 1.3i": mp.mpc("0.2", "1.3")}
KS = (2, 3, 4)
C_PHI = mp.mpf(1) / 2                                         # Phi = c N, |c| = 1/2 (W130)
PROBES = (mp.mpc("0.37", "0.21"), mp.mpc("-0.83", "0.44"), mp.mpc("1.1", "-0.3"))


def szego(k, tau):
    q = mp.exp(1j * mp.pi * tau)
    d1 = mp.jtheta(1, 0, q, 1)
    tk0 = mp.jtheta(k, 0, q)
    return lambda z: mp.jtheta(k, z, q) * d1 / (tk0 * mp.jtheta(1, z, q))


def circle(f, r=mp.mpf("0.3")):
    """(1 / 2 pi i) times the integral of f around |z| = r"""
    g = lambda t: f(r * mp.exp(1j * t)) * 1j * r * mp.exp(1j * t)
    return mp.quad(g, mp.linspace(0, 2 * mp.pi, 9)) / (2j * mp.pi)


def parallelogram(f, tau):
    """(1 / 2 pi i) times the integral of f around a fundamental parallelogram holding 0 and no other lattice point"""
    z0 = -(mp.pi + mp.pi * tau) / 2 + mp.mpc("0.05", "0.03")
    corners = [z0, z0 + mp.pi, z0 + mp.pi + mp.pi * tau, z0 + mp.pi * tau, z0]
    tot = 0
    for a, b in zip(corners, corners[1:]):
        tot += mp.quad(lambda t: f(a + t * (b - a)) * (b - a), [0, mp.mpf(1) / 2, 1])
    return tot / (2j * mp.pi)


def sign_of(x):
    """+1 or -1 for a ratio that is +-1 to the bar, else None"""
    for s in (1, -1):
        if abs(x - s) < BAR:
            return s
    return None


# ------------------------------------------------------------------ J0
def J0():
    rows, ok = {}, True
    for name, tau in TAUS.items():
        S = {k: szego(k, tau) for k in KS}
        res = {k: circle(S[k]) for k in KS}
        odd = max(abs(S[k](-z) + S[k](z)) / abs(S[k](z)) for k in KS for z in PROBES)
        const = {}
        for k, l in ((2, 3), (2, 4), (3, 4)):
            vals = [S[k](z) ** 2 - S[l](z) ** 2 for z in PROBES]
            const[f"{k}{l}"] = (vals[0], max(abs(v - vals[0]) for v in vals) / abs(vals[0]))
        signs = {k: (sign_of(S[k](PROBES[0] + mp.pi) / S[k](PROBES[0])),
                     sign_of(S[k](PROBES[0] + mp.pi * tau) / S[k](PROBES[0]))) for k in KS}
        c = {"residue 1 at 0": all(abs(res[k] - 1) < BAR for k in KS),
             "odd": odd < BAR,
             "S_k^2 - S_l^2 constant in z": all(v[1] < BAR for v in const.values()),
             "period signs (+,-), (-,-), (-,+)": [signs[k] for k in KS] == [(1, -1), (-1, -1), (-1, 1)],
             "the three non-trivial characters of H_1": sorted(signs.values()) == [(-1, -1), (-1, 1), (1, -1)]}
        ok &= all(c.values())
        rows[name] = {"checks": c, "max |residue - 1|": float(max(abs(res[k] - 1) for k in KS)),
                      "max oddness defect": float(odd),
                      "S_k^2 - S_l^2 (value, max relative spread)": {
                          kl: [mp.nstr(v[0], 20), float(v[1])] for kl, v in const.items()},
                      "signs under (pi, pi tau)": {str(k): signs[k] for k in KS}}
    return rows, ok


# ------------------------------------------------------------------ J1
def J1():
    y = sp.symbols("y", positive=True)
    c = sp.symbols("c")
    N = sp.Matrix([[0, 0], [1, 0]])
    H = sp.diag(y, 1 / y)                                       # W130's metric on K^(1/2) + K^(-1/2)
    e1, e2 = sp.Matrix([1, 0]), sp.Matrix([0, 1])
    phi_star = sp.simplify(H.inv() * (c * N).conjugate().T * H)
    W = {"S+": (sp.Rational(1, 2), 0), "S-": (sp.Rational(-1, 2), 0), "K": (1, 0), "Kbar": (0, 1), "O": (0, 0)}
    add = lambda *ws: (sum(w[0] for w in ws), sum(w[1] for w in ws))
    phi_psi = add(W["S-"], W["K"])                              # Phi psi lies in S- (x) K
    pair_phi = add(W["S+"], phi_psi)                            # eps(psi_a, Phi psi_b): S+ (x) S- (x) K -> K
    h_part = add(W["S-"], (sp.Rational(1, 2), 0))               # h = (0, +-i): its part in S- (x) K^(1/2) = O
    eps_h = add(h_part, W["S+"])                                # eps(h, psi_b) in K^(1/2)
    pair_h = add(W["S+"], eps_h)                                # psi_a . eps(h, psi_b)
    herm = sp.simplify((e1.T * H * (c * N) * e1)[0]) == 0       # h(psi_a, Phi psi_b), psi in S+
    c_ = {"N maps S+ to S-": N * e1 == e2,
          "Phi*_h = conj(c) y^-2 N^T": sp.simplify(phi_star - sp.conjugate(c) / y ** 2 * N.T) == sp.zeros(2),
          "Phi* annihilates S+": sp.simplify(phi_star * e1) == sp.zeros(2, 1),
          "eps(psi_a, Phi psi_b) is a (1, 0)-form": pair_phi == (1, 0),
          "h's part lies in the trivial summand": h_part == W["O"],
          "psi_a . eps(h, psi_b) is a (1, 0)-form": pair_h == (1, 0),
          "the hermitian pairing h(psi_a, Phi psi_b) is 0 (different summands)": bool(herm),
          "no pairing linear in the field is a (1, 1)-form": (1, 1) not in (pair_phi, pair_h)}
    return {"checks": c_, "Phi*_h": str(phi_star), "weights": {"eps(psi, Phi psi)": str(pair_phi),
                                                                  "psi . eps(h, psi)": str(pair_h)}}, all(c_.values())


# ------------------------------------------------------------------ J2
def J2():
    chars = {2: (1, -1), 3: (-1, -1), 4: (-1, 1)}
    prod = lambda u, v: (u[0] * v[0], u[1] * v[1])
    triv = (1, 1)
    rows, ok = {}, True
    for name, tau in TAUS.items():
        S = {k: szego(k, tau) for k in KS}
        z = PROBES[1]
        got = {}
        for a, b in ((2, 3), (2, 4), (3, 4)):
            f = lambda w: S[a](w) * S[b](w)
            got[f"{a}{b}"] = (sign_of(f(z + mp.pi) / f(z)), sign_of(f(z + mp.pi * tau) / f(z)))
        third = {"23": chars[4], "24": chars[3], "34": chars[2]}
        c = {"S_a S_b carries the third parity's character": all(got[k] == third[k] for k in got)}
        ok &= all(c.values())
        rows[name] = {"checks": c, "signs of S_a S_b": got}
    c = {"End(E (x) chi) = End E: chi chi^-1 = 1 for each parity": all(prod(v, v) == triv for v in chars.values()),
         "chi_a chi_b = 1 iff a = b": all((prod(chars[a], chars[b]) == triv) == (a == b) for a in KS for b in KS)}
    ok &= all(c.values())
    return {"checks": c, "per tau": rows}, ok


# ------------------------------------------------------------------ J3
def J3():
    coeff = {"Phi": C_PHI, "Phi*": mp.mpf(0), "h (+i)": 1j * mp.sqrt(C_PHI), "h (-i)": -1j * mp.sqrt(C_PHI)}
    rows, ok, Y = {}, True, {}
    for name, tau in TAUS.items():
        S = {k: szego(k, tau) for k in KS}
        res = {(a, b): circle(lambda z: S[a](z) * S[b](z)) for a in KS for b in KS}
        box = {a: parallelogram(lambda z: S[a](z) ** 2, tau) for a in KS}
        Ytau = {X: [[coeff[X] * res[(a, b)] for b in KS] for a in KS] for X in coeff}
        worst = max(abs(v) for M in Ytau.values() for row in M for v in row)
        c = {"the small-circle residue of S_a S_b is 0 for every a, b": max(abs(v) for v in res.values()) < BAR,
             "the parallelogram (residue theorem) gives 0 for S_a^2": max(abs(v) for v in box.values()) < BAR,
             "Y = 0 through Phi, Phi* and h": worst < BAR}
        ok &= all(c.values())
        rows[name] = {"checks": c, "max |residue|": float(max(abs(v) for v in res.values())),
                      "max |parallelogram|": float(max(abs(v) for v in box.values())), "max |Y|": float(worst)}
        Y[name] = {X: [[mp.nstr(v, 5) for v in row] for row in M] for X, M in Ytau.items()}
    return {"per tau": rows, "Y": Y}, ok


def main():
    j0, ok0 = J0()
    j1, ok1 = J1()
    j2, ok2 = J2()
    j3, ok3 = J3()
    rd = {"the coupling matrix": "Y (3 x 3, through Phi, Phi* and h) as computed in J3",
          "a READING by hand (in the record, not here)": "what a non-zero coupling would need"}
    cells = {"J0": ok0, "J1": ok1, "J2": ok2, "J3": ok3}
    out = {"arc": "W131", "rule": "W131_RULE.md", "status": "one run", "J0": j0, "J1": j1, "J2": j2, "J3": j3,
           "J4 (read-out)": rd, "cells": {k: bool(v) for k, v in cells.items()},
           "every cell holds": bool(all(cells.values()))}
    OUT.write_text(json.dumps(out, indent=1, default=str) + "\n", encoding="utf-8")
    print(json.dumps(out["cells"], indent=1))
    print("every cell holds:", out["every cell holds"])


if __name__ == "__main__":
    main()
