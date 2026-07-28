r"""THE LAST DOOR: handoff Tests 1-3 at achievable precision.

Pre-registered protocol (fixed BEFORE looking at outcomes; B743 rules):

  SPECTRAL SET: all stable distinct eigenvalues of m004 from
  eigenvalues_final.json + scanD_refined.json; both r_n and
  lam_n = 1 + r_n^2. Eigenvalue precision: ~1e-9 relative; the
  spectral digit budget is capped at 8.

  TEST 1 (direct match): x in {r_n, lam_n} vs each of the 18 banked
  PDG targets v: candidate iff |x/v - 1| < tau_v,
  tau_v = max(2 * rel_unc_v, 1e-8). NULL: 500 surrogate spectra
  (Weyl-distributed: density ~ r^2 over the observed window, same
  count), same test => expected candidate count. A candidate is a HIT
  only if its per-target surrogate probability < 0.02 (B743 Gate 3).

  TEST 2 (ratios): all pairwise ratios r_m/r_n (m != n) and
  lam_m/lam_n vs each target, same rule, same surrogate null.

  TEST 3-lite (algebraicity at 8 digits): PSLQ of each r_n, lam_n
  against the six B743 bases (caps: 64 for deg-2, 16 for deg-4;
  dps = 14, tol = 1e-7, maxsteps 200000). NULL: 50 surrogates per
  basis; a relation is a HIT only if surrogate rate < 0.02. NOTE:
  8-digit PSLQ can only exclude LOW-HEIGHT relations; the deep
  algebraicity test (50+ digits, handoff Test 3) remains open and is
  NOT claimed here in either direction.

Verdict semantics: this either produces gated hits (extraordinary,
goes to cc for adversarial re-derivation) or clean nulls (the honest
expectation; the banked H0 'the object is valueless' stands, now at
the spectral level too — the last door's answer).

Gate 5-Q.
"""
import json

import mpmath as mp
import numpy as np

mp.mp.dps = 14
OUTDIR = 'frontier/B792_maass_m004_eigenvalues'
RNG = np.random.default_rng(31)

# ---- spectral set ----
eigs = []
with open(f"{OUTDIR}/eigenvalues_final.json") as f:
    eigs += [e['r'] for e in json.load(f)['eigenvalues']]
with open(f"{OUTDIR}/scanD_refined.json") as f:
    eigs += [e['r'] for e in json.load(f)['eigenvalues']]
rs = sorted(set(round(r, 9) for r in eigs))
lams = [1 + r * r for r in rs]
print(f"Spectral set: {len(rs)} distinct eigenvalues, "
      f"r in [{rs[0]:.4f}, {rs[-1]:.4f}]")

with open('frontier/B743_rung1_widened/pdg_targets.json') as f:
    targets = json.load(f)
print(f"Targets: {len(targets)} (B743 banked PDG list)")
print()

# ---- surrogate spectra (Weyl-distributed, r ~ density r^2) ----
NSURR = 500
r_lo, r_hi = rs[0], rs[-1]


def weyl_draw(n):
    u = RNG.uniform(r_lo ** 3, r_hi ** 3, n)
    return np.sort(u ** (1 / 3))


SURR = [weyl_draw(len(rs)) for _ in range(NSURR)]

# ---- TEST 1: direct ----
print("=" * 72)
print("TEST 1: DIRECT MATCH (r_n and lam_n vs targets)")
print("=" * 72)
t1_hits = []
for tg in targets:
    v = float(tg['value'])
    tau = max(2 * tg['rel_unc'], 1e-8)
    cands = [('r', x) for x in rs if abs(x / v - 1) < tau]
    cands += [('lam', x) for x in lams if abs(x / v - 1) < tau]
    # surrogate probability of >= 1 candidate for this target
    cnt = 0
    for s in SURR:
        sl = 1 + s * s
        if np.any(np.abs(s / v - 1) < tau) or np.any(np.abs(sl / v - 1) < tau):
            cnt += 1
    p_null = cnt / NSURR
    for kind, x in cands:
        gated = p_null < 0.02
        t1_hits.append({'target': tg['name'], 'kind': kind, 'x': x,
                        'p_null': p_null, 'gated': gated})
        print(f"  candidate: {kind} = {x:.8f} ~ {tg['name']} = {v} "
              f"(tau {tau:.1e}, surrogate p = {p_null:.3f}) "
              f"{'** GATED HIT **' if gated else '-> fails base rate'}")
if not t1_hits:
    print("  no candidates at any target. CLEAN NULL.")
print()

# ---- TEST 2: ratios ----
print("=" * 72)
print("TEST 2: RATIOS (r_m/r_n and lam_m/lam_n vs targets)")
print("=" * 72)
ratios_r = [rs[i] / rs[j] for i in range(len(rs)) for j in range(len(rs))
            if i != j]
ratios_l = [lams[i] / lams[j] for i in range(len(lams))
            for j in range(len(lams)) if i != j]
t2_hits = []
for tg in targets:
    v = float(tg['value'])
    tau = max(2 * tg['rel_unc'], 1e-8)
    cands = [('r-ratio', x) for x in ratios_r if abs(x / v - 1) < tau]
    cands += [('lam-ratio', x) for x in ratios_l if abs(x / v - 1) < tau]
    cnt = 0
    for s in SURR:
        sl = 1 + s * s
        rr = s[:, None] / s[None, :]
        ll = sl[:, None] / sl[None, :]
        off = ~np.eye(len(s), dtype=bool)
        if (np.any(np.abs(rr[off] / v - 1) < tau)
                or np.any(np.abs(ll[off] / v - 1) < tau)):
            cnt += 1
    p_null = cnt / NSURR
    for kind, x in cands:
        gated = p_null < 0.02
        t2_hits.append({'target': tg['name'], 'kind': kind, 'x': x,
                        'p_null': p_null, 'gated': gated})
        print(f"  candidate: {kind} = {x:.8f} ~ {tg['name']} = {v} "
              f"(surrogate p = {p_null:.3f}) "
              f"{'** GATED HIT **' if gated else '-> fails base rate'}")
if not t2_hits:
    print("  no candidates at any target. CLEAN NULL.")
print()

# ---- TEST 3-lite: PSLQ algebraicity ----
print("=" * 72)
print("TEST 3-lite: PSLQ ALGEBRAICITY (8-digit; low-height only)")
print("=" * 72)
sqrt5 = mp.sqrt(5)
phi = (1 + sqrt5) / 2
BASES = {
    'B1 Q(sqrt5)': ([mp.mpf(1), sqrt5], 64),
    'B2 Q(sqrt3)': ([mp.mpf(1), mp.sqrt(3)], 64),
    'B3 Q(sqrt15)': ([mp.mpf(1), mp.sqrt(15)], 64),
    'B4 Q(zeta15+)': ([mp.mpf(1)] + [(2 * mp.cos(2 * mp.pi / 15)) ** k
                                     for k in (1, 2, 3)], 16),
    'B5 Q(zeta20+)': ([mp.mpf(1)] + [mp.sqrt(2 + phi) ** k
                                     for k in (1, 2, 3)], 16),
    'B6 Q(sqrt-phi)': ([mp.mpf(1)] + [mp.sqrt(phi) ** k
                                      for k in (1, 2, 3)], 16),
}


def pslq_hit(x, basis, cap):
    try:
        rel = mp.pslq([mp.mpf(x)] + basis, tol=mp.mpf(10) ** -7,
                      maxcoeff=cap, maxsteps=200000)
    except Exception:
        return None
    if rel is None or rel[0] == 0:
        return None
    return rel


t3_hits = []
null_rates = {}
for bname, (basis, cap) in BASES.items():
    hits = [(x, pslq_hit(x, basis, cap))
            for x in rs + lams]
    hits = [(x, r_) for x, r_ in hits if r_ is not None]
    # surrogate null at the same scales
    cnt = 0
    nsur = 50
    for _ in range(nsur):
        xs = RNG.uniform(rs[0], rs[-1])
        if pslq_hit(xs, basis, cap) is not None:
            cnt += 1
    null_rates[bname] = cnt / nsur
    for x, rel in hits:
        gated = null_rates[bname] < 0.02
        t3_hits.append({'basis': bname, 'x': x, 'relation': list(rel),
                        'p_null': null_rates[bname], 'gated': gated})
        print(f"  {bname}: x = {x:.8f} relation {rel} "
              f"(null rate {null_rates[bname]:.2f}) "
              f"{'** GATED HIT **' if gated else '-> fails base rate'}")
    if not hits:
        print(f"  {bname}: no relations (null rate {null_rates[bname]:.2f})")
print()

# ---- verdict ----
gated = ([h for h in t1_hits if h['gated']]
         + [h for h in t2_hits if h['gated']]
         + [h for h in t3_hits if h['gated']])
print("=" * 72)
print("VERDICT")
print("=" * 72)
print(f"Test 1 candidates {len(t1_hits)}, gated {sum(h['gated'] for h in t1_hits)}")
print(f"Test 2 candidates {len(t2_hits)}, gated {sum(h['gated'] for h in t2_hits)}")
print(f"Test 3 relations  {len(t3_hits)}, gated {sum(h['gated'] for h in t3_hits)}")
if not gated:
    print()
    print("CLEAN NULL across all three tests at 8-digit precision.")
    print("The SM values are NOT in the low Maass spectrum of m004 at")
    print("testable precision (n <= {} eigenvalues, r <= {:.2f}).".format(
        len(rs), rs[-1]))
    print("The banked H0 (the object is valueless; values live in the")
    print("observer-object coupling) STANDS at the spectral level.")
    print("Open remainder: handoff Test 3 at 50+ digits (algebraicity),")
    print("blocked pending high-precision eigenvalues.")
else:
    print()
    print("GATED HIT(S) FOUND — extraordinary. Do NOT bank: relay to cc")
    print("for adversarial re-derivation per protocol.")

with open(f"{OUTDIR}/sm_comparison_results.json", 'w') as f:
    json.dump({'n_eigenvalues': len(rs), 'r_max': rs[-1],
               'test1': t1_hits, 'test2': t2_hits, 'test3': t3_hits,
               'pslq_null_rates': null_rates,
               'clean_null': not gated}, f, indent=1, default=float)
print()
print("Saved sm_comparison_results.json")
