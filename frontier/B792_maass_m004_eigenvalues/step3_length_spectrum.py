r"""B792 (ex-B788) Step 3 groundwork: geodesic length spectrum of m004.

Method B input (Selberg trace formula consistency check) per the Maass
handoff. SnapPy computes complex lengths (length + i*torsion) of closed
geodesics up to a cutoff. Sanity: counting vs the prime geodesic theorem
N(l) ~ e^{2l}/(2l) for H^3.

Gate 5-Q.
"""
import json

import snappy

M = snappy.Manifold('m004')

spec = None
used = None
for cutoff in (6.0, 5.0, 4.0):
    try:
        try:
            spec = M.length_spectrum(cutoff, include_words=True)
        except TypeError:
            spec = M.length_spectrum(cutoff)
        used = cutoff
        break
    except Exception as e:
        print(f"  cutoff {cutoff} failed: {e}")

print(f"Length spectrum of m004, cutoff {used}:")
print()
print(f"{'mult':>4}  {'length':>20}  {'torsion':>20}  topology  word")

rows = []
for g in spec:
    L = complex(g.length)
    mult = int(g.multiplicity)
    topo = str(getattr(g, 'topology', '?'))
    word = str(getattr(g, 'word', ''))
    rows.append({'re': L.real, 'im': L.imag, 'mult': mult,
                 'topology': topo, 'word': word})
    print(f"{mult:>4}  {L.real:>20.15f}  {L.imag:>20.15f}  {topo}  {word}")

print()
print(f"Total geodesics (with multiplicity) up to {used}: "
      f"{sum(r['mult'] for r in rows)}")

# Prime geodesic theorem check: N(l) ~ e^{2l}/(2l) (H^3, primitive)
import math
prim = [r for r in rows if 'wrapped' not in r['topology'].lower()]
for l in (2.0, 3.0, 4.0, used):
    n_obs = sum(r['mult'] for r in rows if r['re'] <= l)
    n_pgt = math.exp(2 * l) / (2 * l)
    print(f"  N({l}) observed = {n_obs},  PGT ~ e^(2l)/(2l) = {n_pgt:.1f}")

print()
print("Shortest geodesic (systole):",
      min(r['re'] for r in rows))

with open('frontier/B792_maass_m004_eigenvalues/length_spectrum.json', 'w') as f:
    json.dump({'manifold': 'm004', 'cutoff': used, 'geodesics': rows}, f,
              indent=1)
print("Saved length_spectrum.json")
