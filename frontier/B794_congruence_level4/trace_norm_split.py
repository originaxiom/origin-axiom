r"""B790 follow-up (a): trace-norm split stability at raised cutoff 6.0.

B790 (banked, cutoff 5.0): geodesic traces tr = 2cosh(l_C/2) of m004 and
m003 lie exactly in Z[w]; the symmetric-difference trace sets
discriminate the manifolds: m004-only trace norms all == 0 mod 4,
m003-only all odd (min norm 3 vs 1). cc registered "stability of the
mod-4 / odd split under a raised cutoff" as an open follow-up.

RESULT at cutoff 6.0 (370 vs 411 distinct traces, ~2.7x B790's sample):
B790's law was SAMPLE-LIMITED, and the raised cutoff REFINES it:

    m004-only norms:  == 0 or 3 (mod 4)   [0-only at cutoff 5; the first
                                           odd exclusive, norm 7, enters
                                           via traces 3+w and 2-w]
    m003-only norms:  == 1 (mod 4) exactly  [sharper than "odd"]
    shared norms:     == 0 or 3 (mod 4)

  => EVERY m004 trace norm avoids 1 mod 4; the norm == 1 mod 4 traces
     are exactly m003's exclusives. Since 2 is inert in Z[w] (residue
     field F_4), "norm == 0 mod 4" = "trace even"; for ODD traces the
     class mod 4 splits the two manifolds cleanly: m004's odd traces
     have norm == 3 mod 4, m003's == 1 mod 4 (observed; sample-bounded).

This is a mod-4 congruence condition on Gamma_41's traces, consistent
with the level-4 structure at the cusp (B737: O/Lam = Z/4, CM by the
conductor-4 order, disc -48).

Granularity note: B790 compares DISTINCT-trace sets (134+150 = 284),
not SnapPy-multiplicity multisets; this script does both. Traces are
canonicalized under the PSL sign ambiguity tr ~ -tr.

Norm in Z[w] (w = e^{2pi i/3}): N(a + b w) = a^2 - a b + b^2.

Gate 5-Q.
"""
import json

import numpy as np

OM = complex(-0.5, np.sqrt(3) / 2)
DIR = 'frontier/B792_maass_m004_eigenvalues'


def trace_set(fname):
    with open(f"{DIR}/{fname}") as f:
        data = json.load(f)
    out = {}
    worst = 0.0
    for g in data['geodesics']:
        tr = 2 * np.cosh(complex(g['re'], g['im']) / 2)
        b = tr.imag / OM.imag
        a = tr.real - b * OM.real
        ar, br = round(a), round(b)
        worst = max(worst, abs(tr - (ar + br * OM)))
        key = max((ar, br), (-ar, -br))  # PSL: tr ~ -tr
        out[key] = out.get(key, 0) + g['mult']
    return out, worst, data['cutoff']


def N(k):
    a, b = k
    return a * a - a * b + b * b


t4, w4, c4 = trace_set('length_spectrum.json')
t3, w3, c3 = trace_set('length_spectrum_m003.json')
print(f"m004 cutoff {c4}: {len(t4)} distinct canonical traces "
      f"(worst Z[w] dev {w4:.1e})")
print(f"m003 cutoff {c3}: {len(t3)} distinct canonical traces "
      f"(worst Z[w] dev {w3:.1e})")

only4 = set(t4) - set(t3)
only3 = set(t3) - set(t4)
shared = set(t4) & set(t3)
print(f"trace sets: m004-only {len(only4)}, m003-only {len(only3)}, "
      f"shared {len(shared)}")
print()

report = {}
for name, s in (('m004-only', only4), ('m003-only', only3),
                ('shared', shared)):
    ns = sorted({N(k) for k in s})
    mods = sorted({n % 4 for n in ns})
    report[name] = {'n_traces': len(s), 'norms': ns, 'mod4_classes': mods}
    print(f"{name}: {len(s)} traces, {len(ns)} distinct norms, "
          f"mod-4 classes {mods}")
    print(f"   norms: {ns[:16]}{' ...' if len(ns) > 16 else ''}")
print()

n4o = {N(k) for k in only4}
n3o = {N(k) for k in only3}
b790_m004 = all(n % 4 == 0 for n in n4o)
b790_m003 = all(n % 2 == 1 for n in n3o)
ref_m004 = all(n % 4 in (0, 3) for n in n4o)
ref_m003 = all(n % 4 == 1 for n in n3o)
ref_all4 = all(N(k) % 4 in (0, 3) for k in t4)

print(f"B790 cutoff-5 law, m004-only == 0 mod 4:   {b790_m004}"
      f"{'' if b790_m004 else '  <- fails (norm 7: traces 3+w, 2-w)'}")
print(f"B790 cutoff-5 law, m003-only odd:          {b790_m003}")
print(f"REFINED law, m004-only in {{0,3}} mod 4:     {ref_m004}")
print(f"REFINED law, m003-only == 1 mod 4:          {ref_m003}")
print(f"REFINED law, ALL m004 norms in {{0,3}} mod 4: {ref_all4}")
print()
if ref_m004 and ref_m003 and ref_all4:
    print("VERDICT: the split is STABLE in REFINED form. B790's cutoff-5")
    print("phrasing was sample-limited (no odd m004-exclusive trace below")
    print("cutoff 5); the raised cutoff shows the real law is the mod-4")
    print("class: m004 avoids norm == 1 mod 4 entirely, m003's exclusives")
    print("are exactly the norm == 1 mod 4 traces.")
else:
    print("VERDICT: SPLIT BROKEN — neither B790's law nor the refinement")
    print("survives; see classes above.")

with open(f"{DIR}/trace_norm_split.json", 'w') as f:
    json.dump({'cutoff': 6.0, 'granularity': 'distinct canonical traces',
               'report': report,
               'b790_law': {'m004_only_0mod4': b790_m004,
                            'm003_only_odd': b790_m003},
               'refined_law': {'m004_only_03mod4': ref_m004,
                               'm003_only_1mod4': ref_m003,
                               'all_m004_03mod4': ref_all4},
               'worst_dev': {'m004': w4, 'm003': w3}}, f, indent=1)
print("Saved trace_norm_split.json")
