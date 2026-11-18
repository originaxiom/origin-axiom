#!/usr/bin/env python3
"""SM-C18: checks of the triple overlap's derived covariance (card relays/cards/SM_C18_the-triple-overlaps-covariance.md,
pushed before this run).  This seat's own code; main's closed form is imported only for K4.  No coupling value is
printed: only ratios of a quantity to itself, residuals and booleans.
    python3 run_c18.py MAIN_CHECKOUT"""
import cmath
import importlib.util
import itertools
import json
import math
import pathlib
import random
import sys

import numpy as np

HERE = pathlib.Path(__file__).resolve().parent
MAIN = pathlib.Path(sys.argv[1]).resolve()


def theta(a, z, tau, nw=30):
    n = np.arange(-nw, nw + 1) + a - round(a + z.imag / tau.imag)
    return np.exp(1j * np.pi * n ** 2 * tau + 2j * np.pi * n * z).sum()


def psi(j, N, z, tau):
    """a zero mode of flux N on C/(Z + tau Z), with its non-holomorphic factor"""
    return np.exp(1j * np.pi * N * z * z.imag / tau.imag) * theta(j / N, N * z, N * tau)


def integrand(z, tau, zL, zR, zH, i=0, j=1, k=2):
    return psi(i, 3, z + zL, tau) * psi(j, 3, z + zR, tau) * np.conj(psi(k, 6, z + zH, tau))


def Y(tau, xi):
    """this seat's closed form (the addition formula, derived independently; same object as main's)"""
    out = np.zeros((3, 3, 6), complex); y = tau.imag; pre = (3 * y) ** 0.25
    for i in range(3):
        for j in range(3):
            for m in (0, 1):
                k = (i + j + 1 + 3 * m) % 6; c = (i - j + 3 * m) % 6
                out[i, j, k] = pre * cmath.exp(2j * math.pi * k / 6) * cmath.exp(6j * math.pi * xi * xi.imag / y) * theta(c / 6, 6 * xi, 6 * tau)
    return out


def section_equal(A, B):
    """A = phase * B with one common phase"""
    idx = np.unravel_index(np.argmax(np.abs(B)), B.shape)
    ph = A[idx] / B[idx]
    return float(np.max(np.abs(A - ph * B)) / np.max(np.abs(B))), complex(ph)


def main():
    rng = random.Random(18)
    out = {}
    # ---------------- K1: periodicity of the integrand
    k1 = {"flux-weighted mean": [], "plant -(zL + zR)": []}
    for _ in range(20):
        tau = complex(rng.uniform(-0.5, 0.5), rng.uniform(0.8, 2.0))
        zL = complex(rng.uniform(-1, 1), rng.uniform(-1, 1)); zR = complex(rng.uniform(-1, 1), rng.uniform(-1, 1))
        z = complex(rng.uniform(0, 1), rng.uniform(0, 1))
        for name, zH in (("flux-weighted mean", (zL + zR) / 2), ("plant -(zL + zR)", -(zL + zR))):
            f0 = integrand(z, tau, zL, zR, zH)
            r = max(abs(integrand(z + 1, tau, zL, zR, zH) - f0), abs(integrand(z + tau, tau, zL, zR, zH) - f0)) / abs(f0)
            k1[name].append(float(r))
    out["K1"] = {k: max(v) for k, v in k1.items()}
    out["K1 holds"] = out["K1"]["flux-weighted mean"] < 1e-9 and out["K1"]["plant -(zL + zR)"] > 1e-3
    # ---------------- K2: single-valuedness in w
    tau = 0.13 + 1.1j
    w = (2 / 5) * tau + 4 / 5
    k2 = {}
    for name, (qL, qR) in {"down (1, 2)": (1, 2), "up (1, -4)": (1, -4), "leptons (-3, 6)": (-3, 6),
                           "even control (1, 3)": (1, 3), "even control (2, -4)": (2, -4)}.items():
        xi = lambda ww: (qL - qR) * ww / 2
        Y0 = Y(tau, xi(w))
        row = {}
        for sh_name, sh in (("w + 1", 1), ("w + tau", tau)):
            Y1 = Y(tau, xi(w + sh))
            res, ph = section_equal(Y1, Y0)
            row[sh_name + ": equal up to one phase"] = res < 1e-9
            if res >= 1e-9:
                # the derived action: signs (-1)^(i - j + m) along 1, and k -> k + 3 along tau, up to one phase
                Z = np.zeros_like(Y0)
                for i in range(3):
                    for j in range(3):
                        for m in (0, 1):
                            k = (i + j + 1 + 3 * m) % 6
                            if sh == 1:
                                Z[i, j, k] = (-1) ** (i - j + m) * Y0[i, j, k]
                            else:
                                Z[i, j, (k + 3) % 6] = Y0[i, j, k]
                r2, _ = section_equal(Y1, Z)
                row[sh_name + ": equal to the derived action up to one phase"] = r2 < 1e-9
        k2[name] = row
    out["K2"] = k2
    # ---------------- K3: the T-phase, and whether it splits
    tau = 0.21 + 1.3j; xi = 0.31 * tau - 0.17
    A, B = Y(tau + 1, xi), Y(tau, xi)
    resid = 0.0; cs = {}
    for i in range(3):
        for j in range(3):
            for m in (0, 1):
                k = (i + j + 1 + 3 * m) % 6; c = (i - j + 3 * m) % 6
                resid = max(resid, abs(A[i, j, k] / B[i, j, k] - cmath.exp(1j * math.pi * c * c / 6)))
                cs[(i, j, m)] = (c * c) % 12
    out["K3 T-phase = e^(i pi c^2/6)"] = float(resid)
    sols = 0
    for a1, a2, b1, b2 in itertools.product(range(12), repeat=4):
        al = [0, a1, a2]; be = [0, b1, b2]; ga = {}
        ok = True
        for (i, j, m), v in cs.items():
            k = (i + j + 1 + 3 * m) % 6; g = (v - al[i] - be[j]) % 12
            if ga.setdefault(k, g) != g:
                ok = False; break
        if ok:
            sols += 1
    out["K3 splittings mod 12 (alpha_0 = beta_0 = 0)"] = sols
    out["K3 splits"] = sols > 0
    # ---------------- K4: against main's closed form
    spec = importlib.util.spec_from_file_location("cim", MAIN / "frontier/B1957_the_seats_claims_register/verification/checks/cim_closed.py")
    cim = importlib.util.module_from_spec(spec); spec.loader.exec_module(cim)
    worst = 0.0
    for _ in range(10):
        tau = complex(rng.uniform(-0.5, 0.5), rng.uniform(0.9, 2.5)); xi = complex(rng.uniform(-1, 1), rng.uniform(-1, 1))
        Ym, Yo = cim.Y(tau, xi), Y(tau, xi)
        worst = max(worst, float(np.max(np.abs(Ym - Yo)) / np.max(np.abs(Ym))))
    out["K4 relative difference to main's closed form"] = worst
    (HERE / "c18_results.json").write_text(json.dumps(out, indent=1))
    print(json.dumps(out, indent=1))


if __name__ == "__main__":
    main()
