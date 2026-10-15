"""W89: main's B1656 ("the electron's zero", sealed 27e7e7482) checked on this seat's own code before main's run lands.
The rule (W89_RULE.md) was committed before this script; the predictions and priors are there.

  V1  the arithmetic, exact: on W59's 18 lines 9w is in the lattice, 3w is not, and 3w is fixed by z -> omega z;
      on the three non-fixed lines 9w is in the lattice and 3w is not fixed
  V2  the equal norms at omega: c_i = c_j = c_k on every line and sector, one gap c_1 - c_perp everywhere, |gap| > 1
  V3  the electron's zero: lepton R_1 = 0 and D = 0 on every line; the quarks lifted; the null quaternion
  V4  the quark |D|/|R|^2 take exactly three values
  V5  the controls: the generic tau on MIX3; the three non-fixed lines at omega

The kernels are K_s(z) = e^{2 pi i A z} theta_s(z + ub) theta_1'(0) / (theta_s(ub) theta_1(z)), A = Im ub / Im tau
(unitary multipliers), with theta_s(z) = theta_s(pi z | q); their norms by W87's polar quadrature (numpy). The residues
R_s = c_s theta_s(ub) theta_s(delta) from W85's 60-digit series (a common factor dropped). Units (1, i, j, k) <->
thetas (1, 2, 4, 3), c = (-i, -1, -1, i) (B1653).

Run: python3 the_electrons_zero_checked.py  ->  the_electrons_zero_checked.json beside it.
"""
import json
import math
from fractions import Fraction as Fr
from pathlib import Path

import mpmath as mp
import numpy as np

import the_b1651_cells_checked as W85

mp.mp.dps = 60
HERE = Path(__file__).resolve().parent
OUT = HERE / "the_electrons_zero_checked.json"
OMEGA = complex(-0.5, math.sqrt(3) / 2)
TAU0 = complex(0.13, 1.07)
UNITS = ["1", "i", "j", "k"]
TH = {"1": 1, "i": 2, "j": 4, "k": 3}
CC = {"1": mp.mpc(0, -1), "i": mp.mpc(-1), "j": mp.mpc(-1), "k": mp.mpc(0, 1)}
SECTORS = {"up": (1, -4), "down": (1, 2), "leptons": (-3, 6)}
LINES = [(b + Fr(i, 3), b + Fr(j, 3)) for b in (Fr(1, 9), Fr(2, 9)) for i in range(3) for j in range(3)]
MIX3 = [(Fr(1, 9), Fr(1, 9)), (Fr(4, 9), Fr(4, 9)), (Fr(2, 9), Fr(2, 9))]
NONFIXED = [(Fr(1, 9), Fr(2, 9)), (Fr(1, 9), Fr(0)), (Fr(2, 9), Fr(1, 9))]


# ----------------------------------------------------------------------------------------------- V1: exact arithmetic
def coords(k, psi):
    """k w in the basis (omega, 1), with w = psi1 omega - psi2"""
    return (k * psi[0], -k * psi[1])


def in_lattice(c):
    return c[0].denominator == 1 and c[1].denominator == 1


def omega_fixed(c):
    a, b = c
    return in_lattice((b - a - a, -a - b))          # omega (a, b) = (b - a, -a); fixed iff the difference is in Z^2


def V1():
    rows = {f"{p[0]},{p[1]}": {"9w in lattice": in_lattice(coords(9, p)), "3w in lattice": in_lattice(coords(3, p)),
                               "3w omega-fixed": omega_fixed(coords(3, p))} for p in LINES + NONFIXED}
    ok = all(rows[f"{p[0]},{p[1]}"]["9w in lattice"] and not rows[f"{p[0]},{p[1]}"]["3w in lattice"]
             and rows[f"{p[0]},{p[1]}"]["3w omega-fixed"] for p in LINES)
    ok = ok and all(rows[f"{p[0]},{p[1]}"]["9w in lattice"] and not rows[f"{p[0]},{p[1]}"]["3w omega-fixed"]
                    for p in NONFIXED)
    return {"rows": rows, "holds": bool(ok)}


# ----------------------------------------------------------------------------------------------- the kernels' norms
def np_theta(s, z, t, nt=40):
    q = np.exp(1j * np.pi * t)
    zz = np.pi * np.asarray(z)[..., None]
    n = np.arange(nt)
    m = np.arange(1, nt)
    if s == 1:
        return 2 * np.sum((-1.0) ** n * q ** ((n + 0.5) ** 2) * np.sin((2 * n + 1) * zz), -1)
    if s == 2:
        return 2 * np.sum(q ** ((n + 0.5) ** 2) * np.cos((2 * n + 1) * zz), -1)
    if s == 3:
        return 1 + 2 * np.sum(q ** (m ** 2) * np.cos(2 * m * zz), -1)
    return 1 + 2 * np.sum((-1.0) ** m * q ** (m ** 2) * np.cos(2 * m * zz), -1)


def np_th1p(t, nt=40):
    q = np.exp(1j * np.pi * t)
    n = np.arange(nt)
    return 2 * np.pi * np.sum((-1.0) ** n * (2 * n + 1) * q ** ((n + 0.5) ** 2))


def reduce(ub, t):
    """ub modulo the lattice Z + Z tau, to the parallelogram centred at 0 (K_s is invariant under it)"""
    beta = ub.imag / t.imag
    alpha = ub.real - beta * t.real
    return (alpha - round(alpha)) + (beta - round(beta)) * t


def norm(s, t, ub, ng=100, nr=60):
    ub = reduce(ub, t)
    A = ub.imag / t.imag
    d1 = np_th1p(t)
    den = np_theta(s, np.array(ub), t)
    y, xr = t.imag, t.real
    corners = [0.5 * a + 0.5 * b * t for a in (-1, 1) for b in (-1, 1)]
    cuts = sorted({0.0, 2 * np.pi} | {float(np.angle(c) % (2 * np.pi)) for c in corners})
    gx, gw = np.polynomial.legendre.leggauss(ng)
    rx, rw = np.polynomial.legendre.leggauss(nr)
    tot = 0.0
    for a0, a1 in zip(cuts[:-1], cuts[1:]):
        ang = 0.5 * (a1 - a0) * gx + 0.5 * (a1 + a0)
        wt = 0.5 * (a1 - a0) * gw
        sn, cs = np.sin(ang), np.cos(ang)
        with np.errstate(divide="ignore"):
            rm = np.minimum(np.abs(0.5 * y / sn), np.abs(0.5 / (cs - sn * xr / y)))
        rr = 0.5 * rm[:, None] * (rx[None, :] + 1)
        wr = 0.5 * rm[:, None] * rw[None, :]
        z = rr * np.exp(1j * ang)[:, None]
        K = np.exp(2j * np.pi * A * z) * np_theta(s, z + ub, t) * d1 / (den * np_theta(1, z, t))
        f = rr * np.abs(K) ** 2 - 1 / rr
        tot += float(np.sum(wt * (np.log(rm) + np.sum(wr * f, axis=1))))
    return tot


# ----------------------------------------------------------------------------------------------- the residues
def residues(t, ub, dl):
    tm = mp.mpc(t.real, t.imag) if not isinstance(t, mp.mpc) else t
    a = W85.thetas(mp.pi * ub, tm)
    b = W85.thetas(mp.pi * dl, tm)
    return {u: CC[u] * a[TH[u] - 1] * b[TH[u] - 1] for u in UNITS}


def tau_mp(t):
    return OMEGA_MP if t == OMEGA else mp.mpc(str(t.real), str(t.imag))


OMEGA_MP = mp.mpc(-0.5, mp.sqrt(3) / 2)


def sector_case(t, psi, qL, qR):
    tm = tau_mp(t)
    w = mp.mpf(psi[0].numerator) / psi[0].denominator * tm - mp.mpf(psi[1].numerator) / psi[1].denominator
    ub, dl = (qL + qR) * w, (qL - qR) * w
    R = residues(tm, ub, dl)
    R2 = mp.fsum(abs(R[u]) ** 2 for u in UNITS)
    null = abs(mp.fsum(R[u] ** 2 for u in UNITS)) / R2
    r1 = abs(R["1"]) / mp.sqrt(R2)
    cs = {u: norm(TH[u], t, complex(ub)) for u in UNITS}
    D = sum(cs[u] * complex(R[u]) ** 2 for u in UNITS)
    return {"c": cs, "|R1|/|R|": float(r1), "null": float(null), "|D|/|R|^2": float(abs(D) / float(R2)),
            "perp spread": max(cs[u] for u in "ijk") - min(cs[u] for u in "ijk"),
            "gap": cs["1"] - (cs["i"] + cs["j"] + cs["k"]) / 3}


def main():
    out = {"status": "W89: B1656's cells on this seat's own code (script committed before its one run)",
           "lines": [f"{p[0]},{p[1]}" for p in LINES]}
    out["V1"] = V1()
    cases = {}
    for p in LINES:
        for name, (qL, qR) in SECTORS.items():
            cases[f"{p[0]},{p[1]}|{name}"] = sector_case(OMEGA, p, qL, qR)
    out["cases at omega"] = cases
    perp = max(c["perp spread"] for c in cases.values())
    gaps = [c["gap"] for c in cases.values()]
    gap_spread = max(gaps) - min(gaps)
    v2 = perp < 1e-9 and gap_spread < 1e-8 and abs(gaps[0]) > 1
    out["V2"] = {"worst perp spread": perp, "gap": gaps[0], "gap spread": gap_spread, "holds": bool(v2)}
    lep = [c for k, c in cases.items() if k.endswith("|leptons")]
    qua = [c for k, c in cases.items() if not k.endswith("|leptons")]
    nulls = max(c["null"] for c in cases.values())
    v3 = (max(c["|R1|/|R|"] for c in lep) < 1e-12 and max(c["|D|/|R|^2"] for c in lep) < 1e-10
          and min(c["|R1|/|R|"] for c in qua) > 0.1 and min(c["|D|/|R|^2"] for c in qua) > 0.5 and nulls < 1e-40)
    out["V3"] = {"leptons: worst |R1|/|R|": max(c["|R1|/|R|"] for c in lep),
                 "leptons: worst |D|/|R|^2": max(c["|D|/|R|^2"] for c in lep),
                 "quarks: least |R1|/|R|": min(c["|R1|/|R|"] for c in qua),
                 "quarks: least |D|/|R|^2": min(c["|D|/|R|^2"] for c in qua),
                 "worst null quaternion": nulls, "holds": bool(v3)}
    vals = sorted(c["|D|/|R|^2"] for c in qua)
    classes = [vals[0]]
    for v in vals[1:]:
        if v - classes[-1] > 1e-8:
            classes.append(v)
    v4 = len(classes) == 3 and [round(v, 4) for v in classes] == [1.0312, 2.4629, 2.7416]
    out["V4"] = {"classes": classes, "spread within classes": max(
        max(v for v in vals if abs(v - c0) < 1e-6) - min(v for v in vals if abs(v - c0) < 1e-6) for c0 in classes),
        "holds": bool(v4)}
    ctrl_a = {f"{p[0]},{p[1]}": sector_case(TAU0, p, -3, 6) for p in MIX3}
    ctrl_b = {f"{p[0]},{p[1]}": sector_case(OMEGA, p, -3, 6) for p in NONFIXED}
    v5 = (min(c["|D|/|R|^2"] for c in ctrl_a.values()) > 0.1
          and max(c["|R1|/|R|"] for c in ctrl_b.values()) < 1e-12
          and min(c["perp spread"] for c in ctrl_b.values()) > 1e-3
          and min(c["|D|/|R|^2"] for c in ctrl_b.values()) > 0.1)
    out["V5"] = {"(a) leptons at the generic tau on MIX3": ctrl_a, "(b) leptons on the non-fixed lines at omega": ctrl_b,
                 "holds": bool(v5)}
    out["cells"] = {k: out[k]["holds"] for k in ("V1", "V2", "V3", "V4", "V5")}
    out["every cell holds"] = all(out["cells"].values())
    OUT.write_text(json.dumps(out, indent=1, default=float) + "\n", encoding="utf-8")
    print("written", OUT.name)
    print(json.dumps(out["cells"], indent=1))


if __name__ == "__main__":
    main()
