"""W59 (D1): the one-loop potential on the shared fibre, as far as it has closed forms. The rule (W59_RULE.md) was
committed before this script.

  K1  the twisted two-dimensional determinant by two routes (Chowla-Selberg; theta), and the three parities' product
  K2  the checkable steps of the matter determinant's derivation (the cover, zeta(0), the modular weights)
  K3  the stationary points in tau of log(y|eta|^4) and of E(tau, 3); the joint parity sum against E(tau, 3)
  K4  the Wilson line's stationary points for a joint-parity charged boson (and fermion), at two generic tau and
      at omega
  K5  which Standard Model fields see a 3-torsion and a 2-torsion hypercharge line
  plus the read-outs: the Higgs alone at omega, and the two-dimensional term's singular lines

Run: python3 the_one_loop_potential_on_the_fibre.py  ->  the_one_loop_potential_on_the_fibre.json beside it.
"""
import json
import math
import sys
from fractions import Fraction
from pathlib import Path

import numpy as np
from scipy.special import kv, zeta

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import the_weaves_functionals_on_tau as WF  # noqa: E402  (W51: theta and eta series, the census in tau)

OUT = HERE / "the_one_loop_potential_on_the_fibre.json"
OMEGA = complex(-0.5, math.sqrt(3) / 2)
TAU0, TAU1 = 0.17 + 1.13j, 0.05 + 1.40j
PARITIES = [(0.5, 0.0), (0.0, 0.5), (0.5, 0.5)]
CHARGES = {"Q": 1, "u^c": -4, "d^c": 2, "L": -3, "e^c": 6, "H": 3}  # in units of 6Y


# ------------------------------------------------------------------------------------------------------------------ K1
def theta1(z, t, K=30):
    n = np.arange(-K, K + 1)
    return complex(-1j * np.sum((-1.0) ** n * np.exp(1j * np.pi * t * (n + 0.5) ** 2 + 1j * np.pi * (2 * n + 1) * z)))


def logdet_theta(t, a, b):
    """route (ii): log det = log |theta1(a + b tau)/eta|^2 - 2 pi y b^2"""
    return math.log(abs(theta1(a + b * t, t) / complex(WF.eta(t))) ** 2) - 2 * math.pi * t.imag * b * b


def cs(t, a, b, N=80):
    """-Z'(0) for Z(s) = sum |m + a + (n + b) tau|^(-2s), b in (0, 1): Chowla-Selberg, then Sum z^k/k = -log(1 - z)"""
    x, y = t.real, t.imag
    zp = 2 * math.pi * y * (b * b - b + 1 / 6)
    for n in range(-N, N + 1):
        c = n + b
        zp -= math.log(abs(1 - np.exp(2j * math.pi * (a + c * x) - 2 * math.pi * abs(c) * y)) ** 2)
    return -zp


def logdet_cs(t, a, b):
    """route (i); for b an integer the roles swap: Z(s; a, b; tau) = |tau|^(-2s) Z(s; b, a; tau / |tau|^2)"""
    if abs(b - round(b)) > 1e-12:
        return cs(t, a, b % 1)
    return cs(t / abs(t) ** 2, b, a % 1)


def K1():
    samples = [(TAU0, 0.13, 0.37), (TAU1, 0.5, 0.25), (OMEGA, 0.2, 0.6), (1j, 0.71, 0.11),
               (0.3 + 0.9j, -0.4, 0.5), (-0.2 + 1.7j, 0.05, 0.93), (0.45 + 1.0j, 0.33, 0.33), (0.1 + 2.3j, 0.8, 0.45)]
    rows = []
    for t, a, b in samples:
        r1, r2 = logdet_cs(t, a, b), logdet_theta(t, a, b)
        rows.append({"tau": [t.real, t.imag], "(a, b)": [a, b], "route (i)": r1, "route (ii)": r2,
                     "|diff|": abs(r1 - r2)})
    prods = []
    for t in (TAU0, TAU1, OMEGA, 1j, 0.3 + 0.9j):
        p1 = math.exp(sum(logdet_cs(t, v, -u) for u, v in PARITIES))
        p2 = math.exp(sum(logdet_theta(t, v, -u) for u, v in PARITIES))
        prods.append({"tau": [t.real, t.imag], "product, route (i)": p1, "product, route (ii)": p2})
    worst = max(r["|diff|"] for r in rows)
    pworst = max(max(abs(p["product, route (i)"] - 4), abs(p["product, route (ii)"] - 4)) for p in prods)
    return {"the two routes": rows, "the largest difference": worst, "the parity products": prods,
            "the products' largest distance from 4": pworst, "holds": bool(worst < 1e-10 and pworst < 1e-10)}


# ------------------------------------------------------------------------------------------------------------------ K2
def holomorphic_differentials(n, d):
    """x^a dx / w^b on w^n = f(x), f squarefree of degree d, gcd(n, d) = 1: order n - 1 - b at a finite branch point,
    and -n a - n - 1 + d b at the one point over infinity"""
    return [(a, b) for b in range(1, n) for a in range(0, d * n) if n - 1 - b >= 0 and -n * a - n - 1 + d * b >= 0]


def K2():
    g_over_E = 1 + (8 * (2 * 1 - 2) + 4 * (2 - 1)) // 2
    g_over_P1 = 1 + (4 * (0 - 2) + 4 * (4 - 1)) // 2
    diffs = holomorphic_differentials(4, 3)
    cone = 4 * Fraction(1, 12) * (Fraction(1, 2) - 2)
    zeta0 = cone - 1
    p = Fraction(1, 12) * 4 * Fraction(1 * 3, 2)
    pts = [TAU0, TAU1, 0.3 + 0.9j, -0.2 + 1.7j]

    def f1(t):
        return math.sqrt(t.imag) * abs(complex(WF.eta(t))) ** 2

    def f2(t):
        return (t.imag * abs(complex(WF.eta(t))) ** 4) ** -0.25
    inv = max(abs(f(g(t)) / f(t) - 1) for f in (f1, f2) for g in (lambda u: -1 / u, lambda u: u + 1) for t in pts)
    holds = (g_over_E == 3 and g_over_P1 == 3 and diffs == [(0, 2), (0, 3), (1, 3)] and zeta0 == Fraction(-3, 2)
             and zeta0 == -1 - p and inv < 1e-12)
    return {"genus by Riemann-Hurwitz, over E (degree 8, four points of index 2) and over P1 (Z4, four points)":
            [g_over_E, g_over_P1],
            "the holomorphic x^a dx / w^b on w^4 = cubic (a, b)": diffs,
            "zeta_Sigma(0) from the cone coefficients": str(zeta0), "Kokotov's homogeneity p": str(p),
            "-1 - p": str(-1 - p), "the largest change of y^(1/2)|eta|^2 and (y|eta|^4)^(-1/4) under S, T": inv,
            "holds": bool(holds)}


# ------------------------------------------------------------------------------------------------------------------ K3
def E3(t, N=40):
    """E(tau, 3) = Sum' y^3 / |m + n tau|^6, by the Chowla-Selberg expansion"""
    x, y = t.real, t.imag
    s = 3
    head = 2 * zeta(6) * y ** 3 + 2 * math.sqrt(math.pi) * (0.75 * math.sqrt(math.pi)) / 2 * zeta(5) * y ** -2
    tail = 0.0
    for k in range(1, N + 1):
        sig = sum(dd ** (1 - 2 * s) for dd in range(1, k + 1) if k % dd == 0)
        tail += k ** (s - 0.5) * sig * kv(s - 0.5, 2 * math.pi * k * y) * math.cos(2 * math.pi * k * x)
    return head + 8 * math.pi ** s * math.sqrt(y) / 2 * tail


def lattice(t, N):
    m, n = np.meshgrid(np.arange(-N, N + 1), np.arange(-N, N + 1), indexing="ij")
    m, n = m.ravel(), n.ravel()
    keep = (m != 0) | (n != 0)
    m, n = m[keep], n[keep]
    return m, n, t.imag ** 3 / np.abs(m + n * t) ** 6


def K3():
    WF.YMAX = 6.0
    a = WF.census(lambda t: np.log(np.imag(t) * np.abs(WF.eta(t)) ** 4))
    b = WF.census(lambda t: E3(complex(t)))
    m, n, w = lattice(TAU0, 400)
    control = abs(float(np.sum(w)) / E3(TAU0) - 1)
    rows = []
    for t in (TAU0, TAU1, OMEGA, 1j, 0.3 + 0.9j):
        m, n, w = lattice(t, 400)
        joint = float(sum(np.sum(np.cos(2 * np.pi * (m * u + n * v)) * w) for u, v in PARITIES))
        rows.append({"tau": [t.real, t.imag], "joint / E(tau, 3)": joint / E3(t)})
    c_ok = all(abs(r["joint / E(tau, 3)"] + 15 / 16) < 1e-9 for r in rows)

    def only_i_and_rho(c, ti, tr):
        return (c["i"]["type"] == ti and c["rho"]["type"] == tr and not c["critical points in the interior"]
                and not any(c["critical points on the boundary pieces (corners excluded)"].values()))
    holds = (only_i_and_rho(a, "saddle", "maximum") and only_i_and_rho(b, "saddle", "minimum")
             and b["along x = 0 at y = 4, 6, 8"] == sorted(b["along x = 0 at y = 4, 6, 8"]) and c_ok
             and control < 1e-9)
    return {"(a) log(y|eta|^4)": a, "(b) E(tau, 3)": b, "(b) control: the direct sum (N = 400) / Chowla-Selberg - 1":
            control, "(c) the joint parity sum against E(tau, 3)": rows, "holds": bool(holds)}


# ------------------------------------------------------------------------------------------------------------------ K4
class Joint:
    """V(psi) = sign * (-Sum_p Sum' cos 2 pi (m (p1 + psi1) + n (p2 + psi2)) y^3/|m + n tau|^6), psi = q w"""

    def __init__(self, t, sign=1, N=48):
        m, n, w = lattice(t, N)
        c = sum(np.cos(2 * np.pi * (m * u + n * v)) for u, v in PARITIES)
        self.m, self.n, self.cw, self.sign = m, n, c * w, sign

    def value(self, ps):
        return float(-self.sign * np.sum(self.cw * np.cos(2 * np.pi * (self.m * ps[0] + self.n * ps[1]))))

    def grad(self, ps):
        s = np.sin(2 * np.pi * (self.m * ps[0] + self.n * ps[1])) * self.cw * 2 * np.pi * self.sign
        return np.array([np.sum(s * self.m), np.sum(s * self.n)])

    def hess(self, ps):
        c = np.cos(2 * np.pi * (self.m * ps[0] + self.n * ps[1])) * self.cw * (2 * np.pi) ** 2 * self.sign
        return np.array([[np.sum(c * self.m * self.m), np.sum(c * self.m * self.n)],
                         [np.sum(c * self.m * self.n), np.sum(c * self.n * self.n)]])


def stationary(V, grid=72):
    found = []
    for i in range(grid):
        for j in range(grid):
            p = np.array([(i + 0.5) / grid, (j + 0.5) / grid])
            for _ in range(60):
                g = V.grad(p)
                if np.linalg.norm(g) < 1e-12:
                    break
                try:
                    step = np.linalg.solve(V.hess(p), g)
                except np.linalg.LinAlgError:
                    break
                if np.linalg.norm(step) > 0.05:
                    step *= 0.05 / np.linalg.norm(step)
                p = p - step
            if np.linalg.norm(V.grad(p)) < 1e-10:
                q = p % 1.0
                q[np.abs(q - 1) < 1e-9] = 0.0
                if not any(np.max(np.abs(((q - r) + 0.5) % 1.0 - 0.5)) < 1e-6 for r, _, _ in found):
                    ev = np.linalg.eigvalsh(V.hess(q))
                    kind = "minimum" if ev.min() > 0 else ("maximum" if ev.max() < 0 else "saddle")
                    found.append((q, kind, V.value(q)))
    return [{"psi": [round(float(q[0]), 9), round(float(q[1]), 9)], "type": k, "value": v} for q, k, v in
            sorted(found, key=lambda r: (round(r[0][0], 6), round(r[0][1], 6)))]


def near(pt, target):
    return max(abs(((a - b) + 0.5) % 1.0 - 0.5) for a, b in zip(pt, target)) < 1e-6


def K4():
    two = [(0.0, 0.0), (0.5, 0.0), (0.0, 0.5), (0.5, 0.5)]
    three = [(1 / 3, 1 / 3), (2 / 3, 2 / 3)]
    out, ok = {}, True
    for name, t in (("tau0", TAU0), ("tau1", TAU1), ("omega", OMEGA)):
        for sign, label in ((1, "boson"), (-1, "fermion")):
            pts = stationary(Joint(t, sign))
            mins = [p for p in pts if p["type"] == "minimum"]
            out[f"{name}, {label}"] = pts
            if label == "boson" and name != "omega":
                ok &= (len(pts) == 4 and all(any(near(p["psi"], s) for p in pts) for s in two)
                       and len(mins) == 1 and not near(mins[0]["psi"], (0, 0)))
            if label == "boson" and name == "omega":
                kinds = {tuple(s): next((p["type"] for p in pts if near(p["psi"], s)), None) for s in two + three}
                ok &= (len(pts) == 6 and kinds[(0.0, 0.0)] == "maximum"
                       and all(kinds[s] == "saddle" for s in two[1:]) and all(kinds[s] == "minimum" for s in three)
                       and abs(mins[0]["value"] - mins[-1]["value"]) < 1e-9)
            if label == "fermion":
                ok &= len(mins) == 1 and near(mins[0]["psi"], (0, 0))
    out["holds"] = bool(ok)
    return out


# ------------------------------------------------------------------------------------------------------------------ K5
def twisted(q, w):
    return any((q * c).denominator != 1 for c in w)


def K5():
    third = [(Fraction(i, 3), Fraction(j, 3)) for i in range(3) for j in range(3) if (i, j) != (0, 0)]
    half = [(Fraction(1, 2), Fraction(0)), (Fraction(0), Fraction(1, 2)), (Fraction(1, 2), Fraction(1, 2))]
    at3 = {str(w): sorted(f for f, q in CHARGES.items() if twisted(q, w)) for w in third}
    at2 = {str(w): sorted(f for f, q in CHARGES.items() if twisted(q, w)) for w in half}
    colourless_equal = []
    for t in (TAU0, OMEGA):
        V = Joint(t, 1)
        for q in (-3, 3, 6):
            colourless_equal.append(abs(V.value((q / 3, q / 3)) - V.value((0.0, 0.0))))
    holds = (all(v == ["Q", "d^c", "u^c"] for v in at3.values())
             and all(v == ["H", "L", "Q"] for v in at2.values()) and max(colourless_equal) < 1e-12)
    return {"twisted at each nonzero 3-torsion line": at3, "twisted at each nonzero 2-torsion line": at2,
            "colourless fields: |V(3-torsion) - V(0)|, largest": max(colourless_equal), "holds": bool(holds)}


# ------------------------------------------------------------------------------------------------------------- read-out
def readouts():
    pts = stationary(Joint(OMEGA, 1))
    mins = [p["psi"] for p in pts if p["type"] == "minimum"]
    higgs = []
    for ps in mins:
        for i in range(3):
            for j in range(3):
                w = (Fraction(round(ps[0] * 3), 9) + Fraction(i, 3),
                     Fraction(round(ps[1] * 3), 9) + Fraction(j, 3))
                w = (w[0] % 1, w[1] % 1)
                seen = {f: [str((q * c) % 1) for c in w] for f, q in CHARGES.items()}
                higgs.append({"w": [str(c) for c in w], "the twist each field sees (q w mod 1)": seen,
                              "d^c and e^c see different twists": seen["d^c"] != seen["e^c"]})
    singular = [list(p) for p in [(0.5, 0.0), (0.0, 0.5), (0.5, 0.5)]]
    return {"the Higgs alone at omega (charge 3, a joint-parity boson): its minima in psi = 3w": mins,
            "the lines w there, and the twists": higgs,
            "the two-dimensional joint parity term's singular lines (psi), a parity sector untwisted": singular}


def main():
    out = {"status": "W59 (D1): the one-loop potential on the shared fibre, its closed-form sectors (the rule "
                     "W59_RULE.md first; one run)",
           "K1": K1(), "K2": K2(), "K3": K3(), "K4": K4(), "K5": K5(), "read-outs": readouts()}
    out["cells"] = {k: out[k]["holds"] for k in ("K1", "K2", "K3", "K4", "K5")}
    out["every cell holds"] = all(out["cells"].values())
    OUT.write_text(json.dumps(out, indent=1, default=float) + "\n", encoding="utf-8")
    print(json.dumps(out["cells"], indent=1), "\nevery cell holds:", out["every cell holds"])


if __name__ == "__main__":
    main()
