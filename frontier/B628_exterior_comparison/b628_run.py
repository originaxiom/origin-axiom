"""B628/B629 — the exterior held-out comparison (one mechanical run under
the sealed design, sha 7c9ca77e...)."""
import hashlib
import itertools
import math
import os

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
h = hashlib.sha256(open(os.path.join(HERE, "COMPARISON_DESIGN.md"), "rb").read()).hexdigest()
print("design hash:", h)
assert h == "7c9ca77e0d603f97f7a85e8e949f8fefc5d65f8cdacd3afbf8a2d75f09057880"

# the sealed silver values (B627, verbatim moduli)
TAU = {
    1: 16.0,
    4: 11682800640.0,
    5: 1357126041600000.0,
    7: abs(complex(-1.9633485709495167e28, -3.036269925981126)),
    8: abs(complex(2.502525465140358e36, -2.808950507468694e17)),
    11: abs(complex(-1.5198184023599080e51, -8.897827401785689e50)),
}
RATIOS = {f"|t{b}|/|t{a}|": TAU[b] / TAU[a]
          for a, b in itertools.combinations([1, 4, 5, 7, 8, 11], 2)}

T_R = {"m_mu/m_e": 206.7683, "m_tau/m_mu": 16.817, "m_tau/m_e": 3477.23,
       "m_t/m_b": 172.57 / 4.183, "m_b/m_s": 4.183 / 0.0935,
       "m_t/m_e": 172570 / 0.51099895}
T_H = {"M_GUT/M_Z": 2e16 / 91.1876}
TIERS = (1e-2, 1e-3)

print("\nXG3 (15 ratios x 6 mass targets, linear tiers):", flush=True)
k3 = [0, 0]
ps3 = []
for vn, v in RATIOS.items():
    for tn, t in T_R.items():
        dev = abs(v - t) / t
        for ti, d in enumerate(TIERS):
            if dev <= d:
                k3[ti] += 1
                print(f"  {vn} vs {tn}: v={v:.6g} t={t:.6g} dev={dev:.4f} "
                      f"MATCH@{d}", flush=True)
        ps3.append(math.log10(1.01 / 0.99) / 25)
exp3 = sum(ps3)
print(f"XG3: matches (1e-2, 1e-3) = {k3}; expected@1e-2 ~ {exp3:.3f}",
      flush=True)

print("\nXG4 (15 ratios x hierarchy, half-decade log window):", flush=True)
k4 = 0
for vn, v in RATIOS.items():
    for tn, t in T_H.items():
        dev = abs(math.log10(v / t))
        if dev <= 0.5:
            k4 += 1
            print(f"  {vn}: v={v:.4g} log-dev={dev:.3f} WITHIN", flush=True)
exp4 = 15 * (1.0 / 25)
print(f"XG4: matches = {k4}; expected ~ {exp4:.2f}", flush=True)

null3 = k3[0] <= max(1, round(exp3 + 3 * math.sqrt(max(exp3, 1e-9))))
null4 = k4 <= max(1, round(exp4 + 3 * math.sqrt(exp4)))
print(f"\nREADING (per the locked table): "
      f"{'both grids null-compatible — the exterior families are SM-silent on both objects' if (null3 and null4) else 'EXCESS — registered anomaly, third object decides'}",
      flush=True)
print("B628 RUN DONE", flush=True)
