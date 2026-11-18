#!/usr/bin/env python3
"""The SM seat's check of the physical lane's W-P1 response (audit/physical-bridge-2026-09-05 at d37e42695,
reports/physical_bridge_2026_09_05/tick_higgs_alignment_2026_11_18/W_P1_PROCESS_ORBIT_RESPONSE.md), every finite claim
on this seat's own code.  U_M, T6, S6 from main's level6_higgs.py; Sigma = T6 S6 K and P T6 S6 K (M41).
    python3 check_w_p1.py MAIN_CHECKOUT"""
import importlib.util
import itertools
import json
import math
import pathlib
import sys

import numpy as np
import sympy as sp

CHK = pathlib.Path(sys.argv[1]).resolve() / "frontier/B1957_the_seats_claims_register/verification/checks"
sys.path.insert(0, str(CHK))
spec = importlib.util.spec_from_file_location("l6", CHK / "level6_higgs.py"); L6 = importlib.util.module_from_spec(spec); spec.loader.exec_module(L6)
UM, T6, S6 = L6.UM, L6.T6, L6.S6
k = np.arange(6); P = np.zeros((6, 6)); P[(-k) % 6, k] = 1
ev, V = np.linalg.eig(UM); ph = np.angle(ev) / np.pi
vp = V[:, np.argmin(abs(ph - 1 / 6))]; vm = V[:, np.argmin(abs(ph + 1 / 6))]; vp /= np.linalg.norm(vp); vm /= np.linalg.norm(vm)
rng = np.random.default_rng(1)
out = {}


def coords(h):
    return np.vdot(vp, h), np.vdot(vm, h)


for name, A in (("T6 S6 K", T6 @ S6), ("P T6 S6 K", P @ T6 @ S6)):
    Sig = lambda h, A=A: A @ h.conj()
    r = {}
    r["Sigma^2 = U_M on E"] = float(max(np.abs(Sig(Sig(v)) - UM @ v).max() for v in (vp, vm)))
    dev_ratio, dev_avg, dev_d, dev_two = 0.0, 0.0, 0.0, 0.0
    for _ in range(50):
        z = rng.normal(size=2) + 1j * rng.normal(size=2)
        h = z[0] * vp + z[1] * vm
        orbit = [h]
        for _ in range(11):
            orbit.append(Sig(orbit[-1]))
        N0 = sum(abs(c) ** 2 for c in coords(h)); D0 = abs(coords(h)[0]) ** 2 - abs(coords(h)[1]) ** 2
        ds = []
        for x in orbit:
            a, b = coords(x); N = abs(a) ** 2 + abs(b) ** 2; D = abs(a) ** 2 - abs(b) ** 2
            dev_ratio = max(dev_ratio, abs(abs(D) / N - abs(D0) / N0)); ds.append(D / N)
        dev_d = max(dev_d, max(abs(ds[j] - (-1) ** j * ds[0]) for j in range(12)))
        Pavg = sum(np.outer([*coords(x)], np.conj([*coords(x)])) for x in orbit) / (12 * N0)
        dev_avg = max(dev_avg, float(np.abs(Pavg - np.eye(2) / 2).max()))
        for l in range(12):
            st = sum(ds[j] * ds[(j + l) % 12] for j in range(12)) / 12
            dev_two = max(dev_two, abs(st - (-1) ** l * ds[0] ** 2))
        # Sigma^12 = -I on E
        r.setdefault("Sigma^12 h = -h", 0.0)
        s12 = h
        for _ in range(12):
            s12 = Sig(s12)
        r["Sigma^12 h = -h"] = max(r["Sigma^12 h = -h"], float(np.abs(s12 + h).max()))
    r["(2) |Delta|/N constant on orbits"] = float(dev_ratio)
    r["(3) the 12-point average is I_E/2"] = dev_avg
    r["d_k = (-1)^k d_0"] = float(dev_d)
    r["(4) the two-time statistic (-1)^l d_0^2"] = float(dev_two)
    out[name] = r
U6 = np.linalg.matrix_power(UM, 6)
out["U^6 = -I on E"] = float(max(np.abs(U6 @ v + v).max() for v in (vp, vm)))
# section 3: the axis radius of conjugates of gamma = [[2,1],[1,1]] in SL(2,Z)
a, b, c, d = sp.symbols("a b c d")
roots = sp.solve(c * sp.Symbol("z") ** 2 + (d - a) * sp.Symbol("z") - b, sp.Symbol("z"))
sep = sp.simplify((roots[0] - roots[1]) ** 2 - ((a + d) ** 2 - 4 * (a * d - b * c)) / c ** 2)
out["fixed-point separation^2 = ((a+d)^2 - 4 det)/c^2"] = str(sep) == "0"
g = np.array([[2, 1], [1, 1]]); worst_c0 = 0; radii = set()
for q in itertools.product(range(-4, 5), repeat=4):
    Qm = np.array([[q[0], q[1]], [q[2], q[3]]])
    if round(np.linalg.det(Qm)) != 1:
        continue
    gp = Qm @ g @ np.array([[q[3], -q[1]], [-q[2], q[0]]])
    if gp[1, 0] == 0:
        worst_c0 += 1
    radii.add(round(math.sqrt(5) / (2 * abs(gp[1, 0])), 6) if gp[1, 0] else None)
out["conjugates with c = 0 (must be none)"] = worst_c0
out["largest axis radius over conjugates (sqrt5/2 = %.6f)" % (math.sqrt(5) / 2)] = max(x for x in radii if x is not None)
print(json.dumps(out, indent=1))
pathlib.Path(__file__).with_name("check_w_p1.json").write_text(json.dumps(out, indent=1))
