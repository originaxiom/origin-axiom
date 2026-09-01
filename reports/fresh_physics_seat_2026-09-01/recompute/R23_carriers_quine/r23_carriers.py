"""R23 step 2/3: high-precision confirmation of the 112, cusp shapes,
2*sqrt(3)i carriers (SL2Z-reduced), quine.  Own code."""
import json, warnings; warnings.filterwarnings("ignore")
import snappy, mpmath
from fractions import Fraction
mpmath.mp.prec = 220
S3 = mpmath.sqrt(3)
I = mpmath.mpc(0, 1)
def tompc(z):
    return mpmath.mpc(str(z.real()).replace(' ',''), str(z.imag()).replace(' ','')) if hasattr(z, 'real') and callable(z.real) else mpmath.mpc(z)

def reduce_tau(t):
    """SL(2,Z)-reduce tau (Im>0) to |Re|<=1/2, |tau|>=1."""
    t = mpmath.mpc(t)
    for _ in range(200):
        t = t - mpmath.nint(t.real)
        if abs(t) < 1 - mpmath.mpf(10)**-30:
            t = -1 / t
        else:
            break
    t = t - mpmath.nint(t.real)
    return t

def exact_Q3(z, dmax=256, tol=mpmath.mpf(10)**-40):
    a = Fraction(str(mpmath.nstr(z.real, 60))).limit_denominator(dmax)
    b = Fraction(str(mpmath.nstr(z.imag / S3, 60))).limit_denominator(dmax)
    ok = abs(mpmath.mpf(a.numerator)/a.denominator - z.real) < tol and \
         abs(mpmath.mpf(b.numerator)/b.denominator - z.imag/S3) < tol
    return ok, a, b

cands = json.load(open('sweep_candidates.json'))['candidates']
TARGET = 2*S3*I
m004 = snappy.Manifold('m004')
v004 = mpmath.mpf(str(m004.volume(bits_prec=220)))
rows = []
for name in cands:
    M = snappy.Manifold(name)
    sh = M.tetrahedra_shapes('rect', bits_prec=220)
    exact = [exact_Q3(tompc(z)) for z in sh]
    conf = all(e[0] for e in exact)
    maxden = max(max(e[1].denominator, e[2].denominator) for e in exact)
    vol = mpmath.mpf(str(M.volume(bits_prec=220)))
    ratio = vol / v004
    cusps = []
    for ci in M.high_precision().cusp_info():
        tau_raw = tompc(ci['shape'])  # snappy default: longitude/meridian
        tau = reduce_tau(tau_raw)
        is_carrier = abs(tau - TARGET) < mpmath.mpf(10)**-30
        cusps.append({'tau_raw': str(mpmath.nstr(tau_raw, 20)),
                      'tau_reduced': str(mpmath.nstr(tau, 20)),
                      'is_2sqrt3i': bool(is_carrier)})
    rows.append({'name': name, 'ntet': M.num_tetrahedra(), 'ncusps': M.num_cusps(),
                 'Q3_confirmed_1e-40': bool(conf), 'max_denominator': maxden,
                 'vol_over_m004': str(mpmath.nstr(ratio, 25)),
                 'vol_ratio_int': int(mpmath.nint(ratio)) if abs(ratio - mpmath.nint(ratio)) < 1e-30 else None,
                 'cusps': cusps})

conf112 = sum(r['Q3_confirmed_1e-40'] for r in rows)
carriers = [r['name'] for r in rows if any(c['is_2sqrt3i'] for c in r['cusps'])]
carrier_cusps = [(r['name'], [i for i, c in enumerate(r['cusps']) if c['is_2sqrt3i']], r['ncusps'], r['vol_ratio_int']) for r in rows if r['name'] in carriers]
# quine: 1-cusped AND vol == vol(m004) AND cusp shape 2sqrt3 i
quine_hits = [r['name'] for r in rows if r['ncusps'] == 1 and r['vol_ratio_int'] == 1
              and any(c['is_2sqrt3i'] for c in r['cusps'])]
# weaker fingerprints for context
vol1 = [r['name'] for r in rows if r['vol_ratio_int'] == 1]
onecusp_carriers = [r['name'] for r in rows if r['ncusps'] == 1 and any(c['is_2sqrt3i'] for c in r['cusps'])]
print('confirmed at 1e-40:', conf112, '/', len(rows))
print('max denominator overall:', max(r['max_denominator'] for r in rows),
      [(r['name'], r['max_denominator']) for r in rows if r['max_denominator'] > 49])
print('m004 raw cusp shape:', mpmath.nstr(tompc(m004.high_precision().cusp_info()[0]['shape']), 20))
print('carriers (%d):' % len(carriers), carrier_cusps)
print('members at vol(m004):', vol1)
print('1-cusped carriers:', onecusp_carriers)
print('QUINE hits (1-cusped & vol=m004 & 2sqrt3i):', quine_hits)
print('vol ratios non-integer:', [(r['name'], r['vol_over_m004']) for r in rows if r['vol_ratio_int'] is None])
json.dump({'rows': rows, 'carriers': carrier_cusps, 'quine_hits': quine_hits,
           'vol1': vol1, 'onecusp_carriers': onecusp_carriers}, open('carriers_quine.json', 'w'), indent=1)
