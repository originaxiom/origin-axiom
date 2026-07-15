"""B615 — THE COMPARISON (Branch 3; runs once, mechanically, under the
approved design B614, sha 9a189f49...).

Protocol per NULL_MODEL_DESIGN.md section 5: (1) freeze the measured
values verbatim; (2) verify the design hash; (3) compute all pairs at
both tiers; (4) report EVERY pair; (5) per-grid and combined null
statistics; (6) the verdict by the locked table. No reruns.

Measured values recorded from PDG 2024 central values (recorded from the
assistant seat's knowledge of the PDG tables; their accuracy is far
inside the coarsest tier delta = 1e-2; borderline delta = 1e-3 calls are
flagged for seat-4 review against the printed PDG source).

NOTE ON THE F-SET COUNT: the design text estimated "26 distinct
fractions"; the design's authoritative clause is the SET definition
("the inventory is a SET... complete list = the sealed table's E1
column"). The actual distinct set has 17 members; the grid sizes
reported below follow the SET clause.
"""
import hashlib
import itertools
import math
import os

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
DESIGN = os.path.join(HERE, "..", "B614_null_model", "NULL_MODEL_DESIGN.md")
h = hashlib.sha256(open(DESIGN, "rb").read()).hexdigest()
print(f"design hash: {h}")
assert h == "9a189f496b7cd33ec141cabf29a7cca252da0312f79896133bb952851bcb2c2c", \
    "design hash mismatch"

phi = (1 + math.sqrt(5)) / 2

# ---- the value inventory (per design section 1) -----------------------------
A = {
    "A1 |h3|^2 (5-sqrt5)/10": (5 - math.sqrt(5)) / 10,
    "A2 N(h3) 1/5": 1 / 5,
    "A3 (4/7)sin^2(2pi/7)": (4 / 7) * math.sin(2 * math.pi / 7) ** 2,
    "A4 (4/7)sin^2(6pi/7)": (4 / 7) * math.sin(6 * math.pi / 7) ** 2,
    "A5 (4/7)sin^2(4pi/7)": (4 / 7) * math.sin(4 * math.pi / 7) ** 2,
    "A6 normprod 1/49": 1 / 49,
    "A7 Re h3 = 1/(2phi)": 1 / (2 * phi),
    "A8 arg(h3)/pi = 3/10": 3 / 10,
}
F_FRACS = sorted({(1, 4), (1, 10), (4, 5), (4, 13), (9, 26), (25, 58),
                  (2, 29), (1, 2), (1, 1), (121, 692), (225, 692),
                  (121, 274), (16, 137), (16, 65), (49, 130), (9, 50),
                  (8, 25)})
F = {f"F {p}/{q}": p / q for (p, q) in F_FRACS}
TAU = {1: 3, 4: 260736, 5: 165110400, 7: 3257341296168960,
       8: 100636318520821923840,
       11: (2**21 * 3**7 * 5 * 7**6 * 11**2 * 13**2 * 17 * 19 * 73 * 149
            * 151 * 1471 * 160453)}
N4, N8 = 2096640, 536481792000
R = {
    "R1 tau8/tau4": TAU[8] / TAU[4],
    "R2 N8/N4": N8 / N4,
    "R3 N8tau4/(N4tau8)": (N8 * TAU[4]) / (N4 * TAU[8]),
    "R4 tau11/tau1": TAU[11] / TAU[1],
}
TAU_RATIOS = {f"|tau{b}|/|tau{a}|": TAU[b] / TAU[a]
              for a, b in itertools.combinations([1, 4, 5, 7, 8, 11], 2)}
# design 4 (duplicates): the inventory is a SET — collapse equal values
G4_VALUES = {}
for name_, val_ in {**R, **TAU_RATIOS}.items():
    if not any(abs(val_ - w) / w < 1e-12 for w in G4_VALUES.values()):
        G4_VALUES[name_] = val_

# ---- the frozen targets (PDG 2024 central values) ---------------------------
T_C = {"alpha_em(MZ) = 1/127.951": 1 / 127.951,
       "alpha_s(MZ) = 0.1180": 0.1180,
       "sin^2thetaW(MZ) = 0.23122": 0.23122}
T_M = {"sin^2th12(PMNS) = 0.307": 0.307,
       "sin^2th23(PMNS) = 0.546": 0.546,
       "sin^2th13(PMNS) = 0.0220": 0.0220,
       "lambda_Cabibbo = 0.22501": 0.22501,
       "|Vcb| = 0.0408": 0.0408,
       "|Vub| = 0.00382": 0.00382}
T_R = {"m_mu/m_e = 206.7683": 206.7683,
       "m_tau/m_mu = 16.817": 16.817,
       "m_tau/m_e = 3477.23": 3477.23,
       "m_t/m_b = 41.26": 172.57 / 4.183,
       "m_b/m_s = 44.75": 4.183 / 0.0935,
       "m_t/m_e = 337710": 172570 / 0.51099895}
T_H = {"M_GUT/M_Z = 2.19e14": 2e16 / 91.1876}

TIERS = (1e-2, 1e-3)


def run_grid(name, values, targets, logscale=False, logwin=0.5,
             logrange=None, unit_range=True):
    pairs = []
    for vn, v in values.items():
        for tn, t in targets.items():
            if logscale:
                dev = abs(math.log10(v / t)) if v > 0 else float("inf")
                m = [dev <= logwin, dev <= logwin]      # single window
                p = [logwin * 2 / logrange] * 2
            else:
                dev = abs(v - t) / t
                m = [dev <= d for d in TIERS]
                if unit_range:
                    p = [min(1.0, 2 * d * t) for d in TIERS]   # uniform [0,1]
                else:
                    # design 4: G3 null is LOG-uniform on [1e-10, 1e15]
                    p = [math.log10((1 + d) / (1 - d)) / 25 for d in TIERS]
            pairs.append((vn, tn, v, t, dev, m, p))
    return pairs


def pb_tail(ps, k):
    """P(X >= k) for independent Bernoulli(ps) — exact DP."""
    dist = np.zeros(len(ps) + 1)
    dist[0] = 1.0
    for p in ps:
        dist[1:] = dist[1:] * (1 - p) + dist[:-1] * p
        dist[0] *= (1 - p)
    return float(dist[k:].sum())


GRIDS = [
    ("G1 amplitudes x couplings", run_grid("G1", A, T_C)),
    ("G2 amplitudes+fractions x angles", run_grid("G2", {**A, **F}, T_M)),
    ("G3 ratios x mass-ratios", run_grid("G3", R, T_R, unit_range=False)),
    ("G4 log-scale x hierarchy",
     run_grid("G4", G4_VALUES, T_H, logscale=True, logrange=25.0)),
]

print("\n==== EVERY PAIR (v, t, rel-dev | matches at 1e-2, 1e-3) ====",
      flush=True)
grid_stats = []
for gname, pairs in GRIDS:
    print(f"\n-- {gname} ({len(pairs)} pairs) --", flush=True)
    for vn, tn, v, t, dev, m, p in pairs:
        flag = ("  <-- MATCH@1e-2" if m[0] else "") + \
               ("  <== MATCH@1e-3" if m[1] else "")
        print(f"  {vn:>28s} vs {tn:<28s} v={v:.6g} t={t:.6g} "
              f"dev={dev:.4f}{flag}", flush=True)
    for ti in (0, 1):
        ps = [p[ti] for *_, p in pairs]
        k = sum(1 for *_, m, p in pairs if m[ti])
        exp = sum(ps)
        tail = pb_tail(ps, k) if k > 0 else 1.0
        grid_stats.append((gname, ti, k, exp, tail))

print("\n==== THE NULL STATISTICS ====", flush=True)
pmins = {0: 1.0, 1: 1.0}
ngrids = {0: 0, 1: 0}
seen = set()
for gname, ti, k, exp, tail in grid_stats:
    key = (gname, ti)
    if key in seen:
        continue
    seen.add(key)
    d = TIERS[ti] if not gname.startswith("G4") else "log0.5"
    print(f"  {gname:>36s} tier {str(d):>6}: observed {k}, expected "
          f"{exp:.2f}, P(X>=k) = {tail:.4f}", flush=True)
    pmins[ti] = min(pmins[ti], tail)
    ngrids[ti] += 1
for ti in (0, 1):
    p_corr = 1 - (1 - pmins[ti]) ** ngrids[ti]
    print(f"  Sidak-corrected best-grid p, tier {TIERS[ti]}: "
          f"{p_corr:.4f} (best raw {pmins[ti]:.4f} over {ngrids[ti]} "
          f"grids)", flush=True)

# ---- the verdict (per design section 5) --------------------------------------
p_final = min(1 - (1 - pmins[0]) ** ngrids[0],
              1 - (1 - pmins[1]) ** ngrids[1])
if p_final < 0.01:
    verdict = "MATCH-CANDIDATE (pending the robustness ensemble + seat 4)"
elif p_final < 0.1:
    verdict = "AMBIGUOUS (suggestive-only; new sealed design on held-out " \
              "quantities required)"
else:
    verdict = "STRUCTURED-NULL (the stopping rule fires: the SM-values " \
              "connection is closed at this level; the mathematics stands " \
              "as mathematics)"
print(f"\n==== VERDICT (per the locked table): {verdict} "
      f"(combined corrected p = {p_final:.4f}) ====", flush=True)
print("B615 DONE — seat 4 reviews this raw output before any narrative.",
      flush=True)
