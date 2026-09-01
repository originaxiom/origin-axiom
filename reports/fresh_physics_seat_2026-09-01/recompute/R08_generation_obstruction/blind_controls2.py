#!/usr/bin/env python3
"""R08 controls v2 (two-precision algdep verification, same as blind_census_scan2.py).

Controls (the exclusion instrument must FIND the excluded thing when planted):
  1. The three C3 target fields (conductors 7, 9, 13) through the same classifier:
     expect degree 3, square disc (49/81/169), signature (3,0), galois C3.
  2. A planted fake 'manifold' whose shape list generates the conductor-7 C3 field,
     pushed through the same field_of_shapes -> classify path: must be flagged C3.
  3. m015 (5_2 knot): expect cubic, nfdisc -23, signature (1,1), S3.
  4. Sweep: every cyclic cubic of conductor < 200 is totally real (signature (3,0)).
"""
import snappy
from snappy import pari
import json, sys, random, math, os

_keepalive = []  # cypari workaround: GC of polsubcyclo t_VECs double-frees; keep them alive

def log(msg):
    print(msg, file=sys.stderr, flush=True)

def to_pari_c(z, digits):
    old = pari.set_real_precision(digits)
    w = pari(str(z.real())) + pari(str(z.imag()))*pari('I')
    pari.set_real_precision(old)
    return w

def algdep_verified(w_lo, w_hi, maxdeg, thresh_exp=-200):
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
    rng = random.Random(8)
    polys = []
    for _ in range(2):
        coeffs = [rng.randint(2, 9) * rng.choice([1, -1]) for _ in lo]
        p = algdep_verified(sum(c*z for c, z in zip(coeffs, lo)),
                            sum(c*z for c, z in zip(coeffs, hi)), maxdeg)
        if p is None:
            return None, 'ALGDEP_FAIL'
        polys.append(p)
    if polys[0].poldegree() != polys[1].poldegree():
        return None, 'DEGREE_DISAGREE'
    return polys[0], 'OK'

def classify_cubic(p):
    disc = int(pari.nfdisc(p))
    nreal = int(pari.polsturm(p))
    gal = pari.polgalois(p)
    return {'poly': str(p), 'nfdisc': disc, 'signature': [nreal, (3-nreal)//2],
            'galois_order': int(gal[0]), 'galois': str(gal[3]).strip('"'),
            'disc_is_square': disc >= 0 and math.isqrt(disc)**2 == disc}

def subcyclo_polys(f):
    q = pari.polsubcyclo(f, 3)
    qs = list(q) if q.type() == 't_VEC' else [q]
    _keepalive.append((q, qs))
    return [qq for qq in qs if qq.poldegree() == 3]

controls = {}

log('control 1: named C3 targets')
for f in (7, 9, 13):
    for j, p in enumerate(subcyclo_polys(f)):
        controls[f'C3_conductor_{f}' + ('' if j == 0 else f'_{j}')] = classify_cubic(p)

log('control 2: planted C3 manifold')
p7 = subcyclo_polys(7)[0]
r_lo = pari.polroots(p7, precision=500)[0]
r_hi = pari.polroots(p7, precision=1100)[0]
fake_lo = [r_lo, r_lo*r_lo - pari(2), pari(3)*r_lo + pari(1)]
fake_hi = [r_hi, r_hi*r_hi - pari(2), pari(3)*r_hi + pari(1)]
pf, statusf = field_of_shapes(fake_lo, fake_hi)
if pf is not None and pf.poldegree() == 3:
    controls['planted_C3_manifold'] = {'status': statusf, **classify_cubic(pf)}
else:
    controls['planted_C3_manifold'] = {'status': statusf, 'poly': str(pf)}

log('control 3: m015')
M = snappy.Manifold('m015')
lo = [to_pari_c(z, 150) for z in M.tetrahedra_shapes('rect', bits_prec=500)]
hi = [to_pari_c(z, 330) for z in M.tetrahedra_shapes('rect', bits_prec=1100)]
pm, statusm = field_of_shapes(lo, hi)
controls['m015_5_2_knot'] = {'status': statusm,
                             **(classify_cubic(pm) if pm is not None and pm.poldegree() == 3
                                else {'poly': str(pm)})}

log('control 4: cyclic cubic signature sweep')
sigs = []
for f in range(3, 200):
    try:
        polys = subcyclo_polys(f)
    except Exception:
        continue
    for qq in polys:
        nreal = int(pari.polsturm(qq))
        sigs.append([f, [nreal, (3 - nreal)//2]])
controls['all_cyclic_cubics_conductor_lt_200'] = {
    'count': len(sigs),
    'all_totally_real': all(s == [3, 0] for _, s in sigs),
}

with open(sys.path[0] + '/blind_controls_output.json', 'w') as fh:
    json.dump(controls, fh, indent=2)
log('controls written')
print(json.dumps(controls, indent=2))
sys.stdout.flush(); sys.stderr.flush()
os._exit(0)  # skip Py_FinalizeEx: cypari aborts (double free) tearing down polsubcyclo vectors
