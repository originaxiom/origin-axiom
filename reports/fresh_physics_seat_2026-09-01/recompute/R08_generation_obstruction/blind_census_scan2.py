#!/usr/bin/env python3
"""R08 BLIND census scan, v2. v1 (blind_census_scan.py) had a broken acceptance
criterion: pari.algdep at ~150 digits will fit a SPURIOUS low-degree polynomial with
~10^50-size coefficients to any number, and 'residual/scale < 1e-80' accepts it (it
reported all 500 manifolds as degree 2 — including m015, whose cubic trace field is
textbook). v2 fixes this the standard way: find the candidate relation from the shapes
at 500 bits, then VERIFY it against the same shapes recomputed independently at 1100
bits (~331 digits); a spurious relation holds only to ~the search precision and dies
at the higher one. Genuine relation: residual ~1e-300; spurious: ~1e-100. Threshold 1e-200.

Claim under test (B307): of 500 cusped census manifolds, 32 have degree-3 trace
fields, all with signature (1,1) => S3, zero C3.
"""
import snappy
from snappy import pari
import json, sys, random, math

def to_pari_c(z, digits):
    """Parse at the value's NATIVE precision: parsing a 150-digit string while PARI's
    real precision is higher pads with zeros and algdep then fits the padded fake."""
    old = pari.set_real_precision(digits)
    w = pari(str(z.real())) + pari(str(z.imag()))*pari('I')
    pari.set_real_precision(old)
    return w

def algdep_verified(w_lo, w_hi, maxdeg, thresh_exp=-200):
    """Search min poly of w_lo (500-bit value); accept only if it annihilates w_hi
    (1100-bit value) to 1e-200 relative to max coefficient, and is irreducible."""
    if abs(pari.imag(w_lo)) < pari(10)**-80:
        w_lo, w_hi = pari.real(w_lo), pari.real(w_hi)
    for d in range(1, maxdeg+1):
        try:
            p = pari.algdep(w_lo, d)
        except Exception:
            continue
        if p.poldegree() < 1:
            continue
        scale = max(abs(int(c)) for c in pari.Vec(p))
        res = abs(pari.subst(p, pari('x'), w_hi))
        if res / scale < pari(10)**thresh_exp and p.polisirreducible():
            return p
    return None

def field_of_shapes(lo, hi, maxdeg=24):
    """Shape field via primitive element; two coefficient sets must agree on degree."""
    rng = random.Random(8)
    polys = []
    for _ in range(2):
        coeffs = [rng.randint(2, 9) * rng.choice([1, -1]) for _ in lo]
        w_lo = sum(c*z for c, z in zip(coeffs, lo))
        w_hi = sum(c*z for c, z in zip(coeffs, hi))
        p = algdep_verified(w_lo, w_hi, maxdeg)
        if p is None:
            return None, 'ALGDEP_FAIL'
        polys.append(p)
    if polys[0].poldegree() != polys[1].poldegree():
        return None, 'DEGREE_DISAGREE(%d,%d)' % (polys[0].poldegree(), polys[1].poldegree())
    return polys[0], 'OK'

def classify_cubic(p):
    disc = int(pari.nfdisc(p))
    nreal = int(pari.polsturm(p))
    gal = pari.polgalois(p)
    return {'poly': str(p), 'nfdisc': disc, 'signature': [nreal, (3-nreal)//2],
            'galois_order': int(gal[0]), 'galois': str(gal[3]).strip('"'),
            'disc_is_square': disc >= 0 and math.isqrt(disc)**2 == disc}

results, cubics, deg_counts = [], [], {}
N = 500
for i, M in enumerate(snappy.OrientableCuspedCensus()):
    if i >= N:
        break
    name = M.name()
    try:
        lo = [to_pari_c(z, 150) for z in M.tetrahedra_shapes('rect', bits_prec=500)]
        hi = [to_pari_c(z, 330) for z in M.tetrahedra_shapes('rect', bits_prec=1100)]
        p, status = field_of_shapes(lo, hi)
        if p is None:
            results.append({'name': name, 'error': status})
            continue
        deg = int(p.poldegree())
        deg_counts[deg] = deg_counts.get(deg, 0) + 1
        row = {'name': name, 'degree': deg, 'poly': str(p)}
        if deg == 3:
            row.update(classify_cubic(p))
            cubics.append(row)
        results.append(row)
    except Exception as e:
        results.append({'name': name, 'error': repr(e)})
    if (i+1) % 50 == 0:
        print(f'  ...{i+1} done', file=sys.stderr, flush=True)

out = {
    'N': N,
    'degree_histogram': {str(k): v for k, v in sorted(deg_counts.items())},
    'num_degree3': len(cubics),
    'cubics': cubics,
    'num_C3_cubics': sum(1 for c in cubics if c['galois_order'] == 3),
    'num_sig_1_1': sum(1 for c in cubics if c['signature'] == [1, 1]),
    'errors': [r for r in results if 'error' in r],
}
with open(sys.path[0] + '/blind_census_output_v2.json', 'w') as fh:
    json.dump(out, fh, indent=2)
with open(sys.path[0] + '/blind_census_all_rows_v2.json', 'w') as fh:
    json.dump(results, fh, indent=2)
print(json.dumps({k: v for k, v in out.items() if k != 'cubics'}, indent=2))
