#!/usr/bin/env python3
"""R08 controls for the B307 exclusion, in a separate process (cypari showed heap
corruption when everything ran in one process; each control here is cheap and the
script writes its JSON at the very end of a short run).

Controls (the instrument must be able to FIND the excluded thing when planted):
  1. The three C3 target fields (conductors 7, 9, 13) through the same classifier:
     expect degree 3, square disc (49/81/169), signature (3,0), galois C3.
  2. A planted fake 'manifold' whose shape list generates the conductor-7 C3 field,
     through the same field_of_shapes -> classify path used for the census: must be
     flagged C3.
  3. m015 (5_2 knot): expect cubic, nfdisc -23, signature (1,1), S3.
  4. Sweep: every cyclic cubic of conductor < 200 is totally real (signature (3,0)).
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
        coeffs = [rng.randint(10, 30) for _ in pshapes]
        w = sum(c*z for c, z in zip(coeffs, pshapes))
        p = algdep_checked(w, maxdeg)
        polys.append(p)
        deg = max(q.poldegree() for q in polys if q is not None)
        return [q for q in polys if q is not None and q.poldegree() == deg][0], 'TIEBREAK'
    return polys[0], 'OK'

def classify_cubic(p):
    disc = int(pari.nfdisc(p))
    nroots = int(pari.polsturm(p))          # number of real roots
    sig = [nroots, (3 - nroots)//2]
    gal = pari.polgalois(p)
    return {'poly': str(p), 'nfdisc': disc, 'signature': sig,
            'galois_order': int(gal[0]), 'galois': str(gal[3]).strip('"'),
            'disc_is_square': disc >= 0 and math.isqrt(disc)**2 == disc}

def subcyclo_polys(f):
    q = pari.polsubcyclo(f, 3)
    qs = list(q) if q.type() == 't_VEC' else [q]
    return [qq for qq in qs if qq.poldegree() == 3]

controls = {}

# 1. named C3 targets
for f in (7, 9, 13):
    for j, p in enumerate(subcyclo_polys(f)):
        controls[f'C3_conductor_{f}' + ('' if j == 0 else f'_{j}')] = classify_cubic(p)

# 2. planted C3 'manifold' through the census pipeline
p7 = subcyclo_polys(7)[0]
r = pari.polroots(p7)[0]
fake_shapes = [r, r*r - pari(2), pari(3)*r + pari(1)]
pf, statusf = field_of_shapes(fake_shapes)
if pf is not None and pf.poldegree() == 3:
    controls['planted_C3_manifold'] = {'status': statusf, **classify_cubic(pf)}
else:
    controls['planted_C3_manifold'] = {'status': statusf, 'poly': str(pf)}

# 3. m015 = 5_2 knot
M = snappy.Manifold('m015')
shapes = M.tetrahedra_shapes('rect', bits_prec=500)
pm, statusm = field_of_shapes([to_pari_c(z) for z in shapes])
controls['m015_5_2_knot'] = {'status': statusm,
                             **(classify_cubic(pm) if pm is not None and pm.poldegree() == 3
                                else {'poly': str(pm)})}

# 4. every cyclic cubic of conductor < 200 is totally real
sigs = []
for f in range(3, 200):
    try:
        polys = subcyclo_polys(f)
    except Exception:
        continue
    for qq in polys:
        nroots = int(pari.polsturm(qq))
        sigs.append([f, [nroots, (3 - nroots)//2]])
controls['all_cyclic_cubics_conductor_lt_200'] = {
    'count': len(sigs),
    'all_totally_real': all(s == [3, 0] for _, s in sigs),
}

print(json.dumps(controls, indent=2))
with open(sys.path[0] + '/blind_controls_output.json', 'w') as fh:
    json.dump(controls, fh, indent=2)
