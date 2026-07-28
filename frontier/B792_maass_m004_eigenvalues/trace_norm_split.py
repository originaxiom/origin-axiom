r"""B790 follow-up (a): trace-norm split stability at raised cutoff 6.0.

B790 (banked, cutoff 5.0): geodesic traces tr = 2cosh(l_C/2) of m004 and
m003 lie exactly in Z[w]; the SYMMETRIC-DIFFERENCE trace multisets
discriminate the manifolds: m004-only trace norms all == 0 mod 4,
m003-only all odd (min norm 3 vs 1). cc registered "stability of the
mod-4 / odd split under a raised cutoff" as an open follow-up.

This script checks the split at cutoff 6.0 (m004: 7513 geodesics with
multiplicity vs 134 at 5.0 — a ~5x larger sample by count of distinct
lengths).

Norm in Z[w] (w = e^{2pi i/3}): N(a + b w) = a^2 - a b + b^2.

Gate 5-Q.
"""
import json
from collections import Counter

import numpy as np

OM = complex(-0.5, np.sqrt(3) / 2)
DIR = 'frontier/B792_maass_m004_eigenvalues'


def to_eisenstein(z, tol=1e-6):
    """Nearest a + b*omega; returns (a, b, deviation)."""
    b = z.imag / OM.imag
    a = z.real - b * OM.real
    ar, br = round(a), round(b)
    dev = abs(z - (ar + br * OM))
    return ar, br, dev


def norms(fname, key='geodesics'):
    with open(f"{DIR}/{fname}") as f:
        data = json.load(f)
    out = Counter()
    worst = 0.0
    nrows = 0
    for g in data[key]:
        tr = 2 * np.cosh(complex(g['re'], g['im']) / 2)
        a, b, dev = to_eisenstein(tr)
        worst = max(worst, dev)
        n = a * a - a * b + b * b
        out[n] += g['mult']
        nrows += 1
    return out, worst, nrows, data['cutoff']


m004, w4, n4, c4 = norms('length_spectrum.json')
print(f"m004 cutoff {c4}: {n4} distinct lengths, worst Z[w] deviation "
      f"{w4:.2e}")

try:
    m003, w3, n3, c3 = norms('length_spectrum_m003.json')
except FileNotFoundError:
    print("m003 spectrum not yet computed - run the m003 job first.")
    raise SystemExit

print(f"m003 cutoff {c3}: {n3} distinct lengths, worst Z[w] deviation "
      f"{w3:.2e}")
print()

only4 = m004 - m003
only3 = m003 - m004
shared = m004 & m003

print(f"norm multiset sizes (with multiplicity): "
      f"m004 = {sum(m004.values())}, m003 = {sum(m003.values())}, "
      f"shared = {sum(shared.values())}")
print()

n4_only = sorted(only4)
n3_only = sorted(only3)
print(f"m004-only norms ({len(n4_only)} distinct): {n4_only[:20]}"
      f"{' ...' if len(n4_only) > 20 else ''}")
print(f"m003-only norms ({len(n3_only)} distinct): {n3_only[:20]}"
      f"{' ...' if len(n3_only) > 20 else ''}")
print()

mod4_ok = all(n % 4 == 0 for n in n4_only)
odd_ok = all(n % 2 == 1 for n in n3_only)
print(f"B790 split at cutoff 6.0:")
print(f"  m004-only norms all == 0 mod 4:  {mod4_ok}")
if not mod4_ok:
    bad = [n for n in n4_only if n % 4 != 0]
    print(f"    VIOLATIONS: {bad[:10]}")
print(f"  m003-only norms all odd:         {odd_ok}")
if not odd_ok:
    bad = [n for n in n3_only if n % 2 == 0]
    print(f"    VIOLATIONS: {bad[:10]}")
print(f"  min m004-only norm: {min(n4_only) if n4_only else '-'}  "
      f"(B790 at 5.0: 3? -> expect 4-divisible min)")
print(f"  min m003-only norm: {min(n3_only) if n3_only else '-'}")
print()
verdict = ("SPLIT STABLE at raised cutoff" if (mod4_ok and odd_ok)
           else "SPLIT BROKEN at raised cutoff")
print(f"VERDICT: {verdict}")

with open(f"{DIR}/trace_norm_split.json", 'w') as f:
    json.dump({'cutoff': 6.0,
               'm004_only_norms': {str(k): only4[k] for k in n4_only},
               'm003_only_norms': {str(k): only3[k] for k in n3_only},
               'mod4_ok': bool(mod4_ok), 'odd_ok': bool(odd_ok),
               'worst_dev_m004': w4, 'worst_dev_m003': w3}, f, indent=1)
print("Saved trace_norm_split.json")
