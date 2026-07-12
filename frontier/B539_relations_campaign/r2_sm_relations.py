#!/usr/bin/env python3
"""B539 R2: the relation test — positive control (E8, forced bin), then the
SM bin against the frozen catalog, with the magnitude-matched null."""
import numpy as np

PHI = (1 + np.sqrt(5)) / 2

# ── the frozen catalog (R0) ──
CATALOG = {
    'SQ':     lambda x, y: (y - x**2,          max(abs(y), x*x)),
    'GOLD':   lambda x, y: (y*y - y - 1,       max(y*y, abs(y), 1)),
    'QUART':  lambda x, y: (x**4 - x**2 - 1,   max(x**4, x*x, 1)),
    'CUBE':   lambda x, y: (y - x**3,          max(abs(y), abs(x)**3)),
    'RECIP':  lambda x, y: (x*y - 1,           max(abs(x*y), 1)),
    'PERRON': lambda x, y: (y*(x - 1) - 1,     max(abs(y*(x-1)), 1)),
    'SHIFT':  lambda x, y: (y - x**2 + 1,      max(abs(y), x*x, 1)),
}


def hits(values, tol):
    """Count (relation, ordered-pair) hits among the value set."""
    out = []
    vals = list(values.items()) if isinstance(values, dict) else \
        [(str(i), v) for i, v in enumerate(values)]
    for name, rel in CATALOG.items():
        for nx, x in vals:
            for ny, y in vals:
                if nx == ny:
                    continue
                P, s = rel(x, y)
                if s > 0 and abs(P) / s < tol:
                    out.append((name, nx, ny))
    return out


# ── positive control: the E8 ladder at published tolerance ──
E8 = [1, 1.6180340, 1.9890438, 2.4048672, 2.9562952, 3.2183405,
      3.8911568, 4.7833861]
ratios = {f"m{i+1}/m{j+1}": E8[i]/E8[j]
          for i in range(8) for j in range(8) if i > j}
ctrl = hits(ratios, 0.015)          # Coldea's 1.5% tolerance
gold_hits = [h for h in ctrl if h[0] == 'GOLD']
sq_hits = [h for h in ctrl if h[0] == 'SQ']
print("── POSITIVE CONTROL (E8 forced bin, tol = 1.5%) ──")
print(f"  GOLD (y = phi) hits: {len(gold_hits)} "
      f"(includes m2/m1: {any(h[2] == 'm2/m1' for h in gold_hits)})")
print(f"  golden self-similarity: m6/m3, m7/m4, m8/m5 all = m2/m1: "
      f"{all(abs(ratios[k]/ratios['m2/m1'] - 1) < 1e-6 for k in ('m6/m3', 'm7/m4', 'm8/m5'))}")
print(f"  total catalog hits in forced-bin data: {len(ctrl)}")
CONTROL_PASSES = len(gold_hits) > 0
print(f"  CONTROL: {'PASSES' if CONTROL_PASSES else 'FAILS - R2 VOID'}")

# ── the SM bin (frozen list = B533 Gate 3) ──
m_e, m_mu, m_tau = 0.51099895e-3, 0.1056583755, 1.77686
m_u, m_d, m_s, m_c, m_b, m_t = 2.16e-3, 4.67e-3, 93.4e-3, 1.27, 4.18, 172.69
m_W, m_Z, m_H = 80.3692, 91.1876, 125.25
# NOTE: 'alpha' (= 1/(1/alpha)) and 'gW/gY' (= f(sin2W)) are EXCLUDED as
# list-tautologies: relations between a value and a function of itself in
# the same list are artifacts of list construction, not structure. The
# first run included them and the null correctly flagged RECIP(1/a, a)
# as non-random — because it is definitional, not discovered.
SM = {
    '1/alpha': 137.035999084,
    'alpha_s': 0.1180, 'sin2W': 0.23122,
    'mmu/me': m_mu/m_e, 'mtau/me': m_tau/m_e, 'mtau/mmu': m_tau/m_mu,
    'mu/md': m_u/m_d, 'ms/md': m_s/m_d, 'mc/ms': m_c/m_s,
    'mb/ms': m_b/m_s, 'mt/mb': m_t/m_b, 'mc/mu': m_c/m_u, 'mt/mu': m_t/m_u,
    'mW/mZ': m_W/m_Z, 'mH/mZ': m_H/m_Z, 'mH/mW': m_H/m_W,
    'Vus': 0.22500, 'Vcb': 0.04182, 'Vub': 0.00365,
}

print("\n── SM BIN ──")
rng = np.random.RandomState(42)
N_NULL = 500
for tol in (1e-2, 1e-3, 1e-4):
    obs = hits(SM, tol)
    null_counts = []
    for _ in range(N_NULL):
        fake = {k: v * np.exp(rng.uniform(-np.log(2), np.log(2)))
                for k, v in SM.items()}
        null_counts.append(len(hits(fake, tol)))
    null_counts = np.array(null_counts)
    p = float(np.mean(null_counts >= len(obs)))
    print(f"  tol {tol:g}: SM hits = {len(obs)}, null mean = "
          f"{null_counts.mean():.1f} (max {null_counts.max()}), "
          f"family-wise p = {p:.3f}")
    if tol == 1e-3 and obs:
        for h in obs[:12]:
            x, y = SM[h[1]], SM[h[2]]
            P, s = CATALOG[h[0]](x, y)
            print(f"    {h[0]}({h[1]}, {h[2]}): residual {abs(P)/s:.2e}")

# precision tightening on any tol-1e-3 hits
obs3 = hits(SM, 1e-3)
tight = [h for h in obs3
         if abs(CATALOG[h[0]](SM[h[1]], SM[h[2]])[0]) /
            CATALOG[h[0]](SM[h[1]], SM[h[2]])[1] < 1e-5]
print(f"\n  hits at tol 1e-3 surviving tightening to 1e-5: {len(tight)}")
print(f"\nVERDICT per prereg: "
      f"{'NO-MATCH' if not tight else 'candidate hits - examine'}"
      f" (real requires family-wise p < 0.001 at tol <= 1e-3 AND survival)")
