#!/usr/bin/env python3
"""SM-C18, post hoc (labelled): the leptons' w + tau cell of K2, which overflowed in double precision (xi = -9w/2), at
extended precision on this seat's own code.  Same test: equal to Y(w) up to one phase? equal to the derived action
(k -> k + 3) up to one phase?"""
import json
import pathlib
import mpmath as mp

mp.mp.dps = 50


def theta(a, z, tau, nw=40):
    c = mp.nint(a + mp.im(z) / mp.im(tau))
    return mp.fsum(mp.exp(1j * mp.pi * (n + a - c) ** 2 * tau + 2j * mp.pi * (n + a - c) * z) for n in range(-nw, nw + 1))


def Y(tau, xi):
    y = mp.im(tau); pre = (3 * y) ** mp.mpf("0.25"); out = {}
    for i in range(3):
        for j in range(3):
            for m in (0, 1):
                k = (i + j + 1 + 3 * m) % 6; c = (i - j + 3 * m) % 6
                out[(i, j, k)] = pre * mp.exp(2j * mp.pi * k / 6) * mp.exp(6j * mp.pi * xi * mp.im(xi) / y) * theta(mp.mpf(c) / 6, 6 * xi, 6 * tau)
    return out


def section_equal(A, B):
    key = max(B, key=lambda q: abs(B[q])); ph = A[key] / B[key]
    return max(abs(A[q] - ph * B[q]) for q in B) / abs(B[key])


tau = mp.mpc("0.13", "1.1"); w = mp.mpf(2) / 5 * tau + mp.mpf(4) / 5
qL, qR = -3, 6
xi = lambda ww: (qL - qR) * ww / 2
Y0, Y1 = Y(tau, xi(w)), Y(tau, xi(w + tau))
Z = {}
for (i, j, k), v in Y0.items():
    Z[(i, j, (k + 3) % 6)] = v
out = {"leptons w + tau: equal up to one phase": float(section_equal(Y1, Y0)),
       "leptons w + tau: equal to the derived action (k -> k + 3) up to one phase": float(section_equal(Y1, Z))}
print(json.dumps(out, indent=1))
pathlib.Path(__file__).with_name("posthoc_leptons_mp.json").write_text(json.dumps(out, indent=1))
