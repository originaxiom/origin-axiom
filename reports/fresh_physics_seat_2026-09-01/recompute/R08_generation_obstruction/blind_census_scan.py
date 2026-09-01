#!/usr/bin/env python3
"""R08 BLIND computation, part (ii): census scan for B307.

Banked claim to test: of 500 cusped census manifolds, 32 have degree-3 (invariant) trace
fields; all 32 have signature (1,1) => Galois group S3; zero are cyclic (C3).

Method (independent): OrientableCuspedCensus[:500]; shape field (= invariant trace field
for cusped manifolds, Neumann-Reid) computed from high-precision tetrahedron shapes via
PARI algdep on a primitive element (two independent coefficient sets must agree).
For every degree-3 field: exact nfdisc, signature (r1,r2), Galois group via polgalois.

CONTROLS (the exclusion must be findable when planted):
  * the three C3 target fields (conductors 7, 9, 13) run through the SAME classifier:
    must come out degree 3, disc a perfect square (49/81/169), signature (3,0), C3;
  * a planted fake 'manifold' whose shape list generates the conductor-7 C3 field must
    be flagged C3 by the same code path used for the census;
  * m015 (the 5_2 knot) must come out cubic, disc -23, signature (1,1), S3.
"""
import snappy
from snappy import pari
import json, sys, random, math

pari.set_real_precision(150)

def to_pari_c(z):
    return pari(str(z.real())) + pari(str(z.imag()))*pari('I')

def algdep_checked(w, maxdeg, tol_exp=-80):
    if abs(pari.imag(w)) < pari(10)**tol_exp:
        w = pari.real(w)
    for d in range(1, maxdeg+1):
        try:
            p = pari.algdep(w, d)
        except Exception:
            continue
        if p.poldegree() < 1:
            continue
        res = abs(pari.subst(p, pari('x'), w))
        scale = max(abs(int(c)) for c in pari.Vec(p))
        if res / scale < pari(10)**tol_exp and p.polisirreducible():
            return p
    return None

def field_of_shapes(pshapes, maxdeg=24):
    """Shape field via primitive element; two coefficient sets must agree on degree."""
    rng = random.Random(8)
    polys = []
    for _ in range(2):
        coeffs = [rng.randint(2, 9) * rng.choice([1, -1]) for _ in pshapes]
        w = sum(c*z for c, z in zip(coeffs, pshapes))
        p = algdep_checked(w, maxdeg)
        if p is None:
            return None, 'ALGDEP_FAIL'
        polys.append(p)
    if polys[0].poldegree() != polys[1].poldegree():
        # third tie-breaker with fresh coefficients
        coeffs = [rng.randint(10, 30) for _ in pshapes]
        w = sum(c*z for c, z in zip(coeffs, pshapes))
        p = algdep_checked(w, maxdeg)
        polys.append(p)
        deg = max(q.poldegree() for q in polys if q is not None)
        best = [q for q in polys if q is not None and q.poldegree() == deg][0]
        return best, 'TIEBREAK'
    return polys[0], 'OK'

def classify_cubic(p):
    nf = pari.nfinit(p)
    disc = int(pari.nfdisc(p))
    sig = [int(x) for x in nf[1]]
    gal = pari.polgalois(p)          # [order, sign, idx, name]
    name = str(gal[3]).strip('"')
    return {'poly': str(p), 'nfdisc': disc, 'signature': sig,
            'galois_order': int(gal[0]), 'galois': name,
            'disc_is_square': disc >= 0 and math.isqrt(disc)**2 == disc}

results = []
deg_counts = {}
cubics = []
N = 500
census = snappy.OrientableCuspedCensus()
for i, M in enumerate(census):
    if i >= N:
        break
    name = M.name()
    try:
        shapes = M.tetrahedra_shapes('rect', bits_prec=500)
        pshapes = [to_pari_c(z) for z in shapes]
        p, status = field_of_shapes(pshapes)
        if p is None:
            results.append({'name': name, 'error': status})
            continue
        deg = int(p.poldegree())
        deg_counts[deg] = deg_counts.get(deg, 0) + 1
        row = {'name': name, 'degree': deg, 'status': status}
        if deg == 3:
            row.update(classify_cubic(p))
            cubics.append(row)
        results.append(row)
    except Exception as e:
        results.append({'name': name, 'error': repr(e)})
    if (i+1) % 100 == 0:
        print(f'  ...{i+1} manifolds done', file=sys.stderr)

out = {
    'N': N,
    'degree_histogram': {str(k): v for k, v in sorted(deg_counts.items())},
    'num_degree3': len(cubics),
    'cubics': cubics,
    'num_C3_cubics': sum(1 for c in cubics if c['galois_order'] == 3),
    'num_sig_1_1': sum(1 for c in cubics if c['signature'] == [1, 1]),
    'errors': [r for r in results if 'error' in r],
}

with open(sys.path[0] + '/blind_census_output.json', 'w') as fh:
    json.dump(out, fh, indent=2)
with open(sys.path[0] + '/blind_census_all_rows.json', 'w') as fh:
    json.dump(results, fh, indent=2)

# controls moved to blind_controls.py (separate process; cypari heap crash isolation)
