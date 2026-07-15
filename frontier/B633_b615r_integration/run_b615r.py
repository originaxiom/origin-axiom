"""B615-R — the target-uncertainty re-analysis (cc2 advisory cell).

Object-side inventory copied VERBATIM from the recorded
frontier/B615_comparison/b615_comparison.py (Branch 3, design 9a189f49...).
Statistic machinery byte-equivalent; the two preregistered corrections are
(i) current central values, (ii) 2-sigma window/null inflation. Three
variants (a) old+width, (b) new+point, (c) new+width [headline].

TARGETS: (t_old, t_new, sigma) — t_new/sigma pasted from the sourced fetch
(see DESIGN.md Inputs and SEAL.txt). sigma = max(sigma+, sigma-).
"""
import itertools
import math

import numpy as np

phi = (1 + math.sqrt(5)) / 2

# ---- the object inventory (verbatim from the recorded run) -------------------
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
G4_VALUES = {}
for name_, val_ in {**R, **TAU_RATIOS}.items():
    if not any(abs(val_ - w) / w < 1e-12 for w in G4_VALUES.values()):
        G4_VALUES[name_] = val_

# ---- targets: name -> (t_old, t_new, sigma) ----------------------------------
# Sourced: NuFIT 6.1 (2025); PDG RPP-2026 (2026-06-01). See DESIGN.md Inputs.
T_C = {
    "alpha_em(MZ) MS-bar":      (1 / 127.951, 1 / 127.95, 0.02 / 127.95 ** 2),
    "alpha_s(MZ)":              (0.1180, 0.1180, 0.0009),
    "sin^2thetaW(MZ)":          (0.23122, 0.23122, 0.00006),
}
T_M = {
    "sin^2th12(PMNS)":          (0.307, 0.3088, 0.0067),
    "sin^2th23(PMNS)":          (0.546, 0.470, 0.017),     # NuFIT 6.1 NO best (lower octant)
    "sin^2th13(PMNS)":          (0.0220, 0.02249, 0.00057),
    "lambda_Cabibbo":           (0.22501, 0.22517, 0.00068),
    "|Vcb|":                    (0.0408, 0.0407, 0.0013),
    "|Vub|":                    (0.00382, 0.00389, 0.00016),
}
TH23_ALT = 0.550, 0.016            # variant (c2): the other-octant minimum
T_R = {
    "m_mu/m_e":                 (206.7683, 206.768283, 5e-6),
    "m_tau/m_mu":               (16.817, 16.8177, 0.0009),
    "m_tau/m_e":                (3477.23, 3477.37, 0.18),
    "m_t/m_b [A recorded]":     (172.57 / 4.183, 41.24, 0.28),
    "m_b/m_s [A recorded]":     (4.183 / 0.0935, 45.06, 0.35),
    "m_t/m_e [A recorded]":     (172570 / 0.51099895, 337766, 530),
}
# scheme-consistency columns (correction iii): swapped in for variant 'c3'
T_R_SCHEME_C = {
    "m_mu/m_e":                 (206.7683, 206.768283, 5e-6),
    "m_tau/m_mu":               (16.817, 16.8177, 0.0009),
    "m_tau/m_e":                (3477.23, 3477.37, 0.18),
    "m_t/m_b [C MS-bar @ mt]":  (None, 60.1, 0.7),
    "m_b/m_s [C common mu]":    (None, 53.6, 0.6),
    "m_t/m_e [C MS-bar]":       (None, 318980, 800),
}
T_R_SCHEME_B = {"m_t/m_b [B pole/pole]": (None, 36.1, 0.5)}
T_H = {
    "M_GUT/M_Z [CONVENTION]":   (2e16 / 91.1876, 2e16 / 91.1876, 0.0),
}

TIERS = (1e-2, 1e-3)
LOGWIN, LOGRANGE, G3_LO, G3_HI = 0.5, 25.0, 1e-10, 1e15


def grid_pairs(values, targets, variant, logscale=False, unit_range=True):
    """variant: 'a' old+width, 'b' new+point, 'c' new+width."""
    pairs = []
    for vn, v in values.items():
        for tn, (t_old, t_new, sig) in targets.items():
            t = t_old if variant == 'a' else t_new
            if t is None:
                continue
            s = 0.0 if variant == 'b' else (sig or 0.0)
            if logscale:
                slog = (s / t) / math.log(10) if (t and s) else 0.0
                half = LOGWIN + 2 * slog
                dev = abs(math.log10(v / t)) if v > 0 else float("inf")
                m = [dev <= half] * 2
                p = [min(1.0, half * 2 / LOGRANGE)] * 2
            else:
                dev = abs(v - t)
                m, p = [], []
                for d in TIERS:
                    half = d * t + 2 * s
                    m.append(dev <= half)
                    if unit_range:
                        p.append(min(1.0, 2 * half))
                    else:
                        lo = max(t - half, 1e-300)
                        p.append(min(1.0, math.log10((t + half) / lo) /
                                     math.log10(G3_HI / G3_LO)))
            pairs.append((vn, tn, v, t, dev, m, p))
    return pairs


def pb_tail(ps, k):
    dist = np.zeros(len(ps) + 1)
    dist[0] = 1.0
    for p in ps:
        dist[1:] = dist[1:] * (1 - p) + dist[:-1] * p
        dist[0] *= (1 - p)
    return float(dist[k:].sum())


def run_variant(variant, t_m=None, t_r=None, label=None, verbose=True):
    t_m = t_m or T_M
    t_r = t_r or T_R
    grids = [
        ("G1 amplitudes x couplings", grid_pairs(A, T_C, variant)),
        ("G2 amplitudes+fractions x angles", grid_pairs({**A, **F}, t_m, variant)),
        ("G3 ratios x mass-ratios", grid_pairs(R, t_r, variant, unit_range=False)),
        ("G4 log-scale x hierarchy", grid_pairs(G4_VALUES, T_H, variant, logscale=True)),
    ]
    print(f"\n########## VARIANT ({label or variant}) ##########")
    pmins = {0: 1.0, 1: 1.0}
    for gname, pairs in grids:
        for ti in (0, 1):
            ps = [p[ti] for *_, p in pairs]
            k = sum(1 for *_, m, p in pairs if m[ti])
            exp = sum(ps)
            sat = " [SATURATED-WINDOW GRID]" if exp >= len(ps) * 0.5 else ""
            tail = pb_tail(ps, k) if k > 0 else 1.0
            tname = f"{TIERS[ti]}" if not gname.startswith('G4') else 'log'
            print(f"  {gname:>36s} tier {tname:>6}: observed {k}, "
                  f"expected {exp:.2f}, P(X>=k) = {tail:.4f}{sat}")
            if verbose and ti == 0 and k:
                for vn, tn, v, t, dev, m, p in pairs:
                    if m[0]:
                        print(f"      MATCH {vn} vs {tn}: v={v:.6g} t={t:.6g} "
                              f"absdev={dev:.3g}")
            pmins[ti] = min(pmins[ti], tail)
    out = {}
    for ti in (0, 1):
        out[ti] = 1 - (1 - pmins[ti]) ** 4          # Sidak over the 4 grids
        print(f"  Sidak-corrected best-grid p, tier {TIERS[ti]}: {out[ti]:.4f}")
    return min(out.values())


if __name__ == '__main__':
    run_variant('a', label='a: old centrals + width correction')
    run_variant('b', label='b: new centrals, point windows')
    p = run_variant('c', label='c: new centrals + width correction [HEADLINE]')
    th23_alt = dict(T_M)
    th23_alt["sin^2th23(PMNS)"] = (0.546, TH23_ALT[0], TH23_ALT[1])
    p2 = run_variant('c', t_m=th23_alt, label='c2: other-octant th23 sensitivity')
    p3 = run_variant('c', t_r={**T_R_SCHEME_C, **T_R_SCHEME_B},
                     label='c3: scheme-consistent G3 (correction iii)')
    verdict = 'A (dissolves; closure hardened)' if p >= 0.1 else \
              'B (ambiguous stands)' if p >= 0.01 else \
              'C (strengthens; reopen)'
    print(f"\n==== HEADLINE (variant c): p_final = {p:.4f} -> VERDICT {verdict}")
    print(f"==== sensitivities: c2 (octant) p = {p2:.4f}; c3 (scheme) p = {p3:.4f}")
