"""Run with sage -python. Interval certificates, not floating-point verdicts."""
import json
import time

import sage.all as sa  # Must precede snappy for its Sage interval mode.
import snappy

INPUT = 'kLLLPLQkcefegijjiijiieldllxtxa_aBbBabBbbacb'


def safe(fn):
    try:
        return dict(value=fn())
    except Exception as e:
        return dict(error=type(e).__name__+': '+str(e))


def quarter_lattice(interval):
    lo = int(sa.floor(4*interval.lower()))-1
    hi = int(sa.ceil(4*interval.upper()))+1
    points = [sa.QQ(k)/4 for k in range(lo, hi+1)]
    hits = [str(x) for x in points if x in interval]
    distance_lower = min(abs(interval-x).lower() for x in points)
    return dict(hits=hits, excludes=bool(not hits and distance_lower > 0),
                distance_lower=str(distance_lower))


def interval_summary(interval):
    return dict(display=str(interval), lower=str(interval.lower()), upper=str(interval.upper()),
                diameter=str(interval.absolute_diameter()))


def certify(M, bits):
    ok, shapes = M.verify_hyperbolicity(bits_prec=bits)
    out = dict(hyperbolic=bool(ok), shapes=[str(z) for z in shapes],
               cusps=int(M.num_cusps()), complete=[bool(x) for x in M.cusp_info('is_complete')])
    if not ok:
        return out, None, None
    cv = M.complex_volume(verified_modulo_2_torsion=True, bits_prec=bits)
    real = cv.real().parent()
    normalized = cv.imag()/(2*real.pi()**2)
    out.update(volume=interval_summary(cv.real()), cs_mod_quarter=interval_summary(normalized),
               lattice=quarter_lattice(normalized))
    return out, normalized, cv.real()


def run():
    start = time.monotonic()
    C = snappy.Manifold(INPUT)
    N = C.copy()
    N.dehn_fill((2, 1), 0)
    F = N.filled_triangulation([0])
    F.simplify()
    R = F.copy()
    R.reverse_orientation()
    objects = dict(m004=snappy.Manifold('m004'), control_5_2=snappy.Manifold('5_2'), cover=C, filled=F, reverse=R)
    out = dict(sage_version=sa.version(), snappy_version=snappy.version(), input=INPUT,
               filled_signature=F.triangulation_isosig(ignore_orientation=False),
               partial_hyperbolicity={}, certificates={}, comparisons={})
    intervals = {}
    for bits in (100, 160):
        out['partial_hyperbolicity'][str(bits)] = safe(lambda: bool(N.verify_hyperbolicity(bits_prec=bits)[0]))
        for name, M in objects.items():
            try:
                row, cs, volume = certify(M, bits)
                out['certificates'][name+'_'+str(bits)] = row
                intervals[name, bits] = (cs, volume)
            except Exception as e:
                out['certificates'][name+'_'+str(bits)] = dict(error=type(e).__name__+': '+str(e))
    for bits in (100, 160):
        if ('filled', bits) in intervals and ('reverse', bits) in intervals:
            c, v = intervals['filled', bits]
            cr, vr = intervals['reverse', bits]
            if c is not None and cr is not None:
                out['comparisons'][str(bits)] = dict(opposite_mod_quarter=not quarter_lattice(c+cr)['excludes'],
                                                     equal_volume=bool((v-vr).contains_zero()))
    for name in objects:
        if (name, 100) in intervals and (name, 160) in intervals:
            c0, _ = intervals[name, 100]
            c1, _ = intervals[name, 160]
            if c0 is not None and c1 is not None:
                out['comparisons'][name] = dict(compatible=bool((c0-c1).contains_zero()),
                                                diameter_shrinks=bool(c1.absolute_diameter() < c0.absolute_diameter()))
    real = sa.RealIntervalField(100)
    out['synthetic'] = dict(zero=quarter_lattice(real(0)), quarter=quarter_lattice(real(sa.QQ(1)/4)),
                             twenty_fourth=quarter_lattice(real(sa.QQ(1)/24)))
    out['runtime_seconds'] = time.monotonic()-start
    return out


def assert_certificate(out):
    for bits in (100, 160):
        assert out['partial_hyperbolicity'][str(bits)] == dict(value=True)
        for name in ('filled', 'reverse', 'control_5_2'):
            row = out['certificates'][name+'_'+str(bits)]
            assert row['hyperbolic'] and row['lattice']['excludes']
        for name in ('m004', 'cover'):
            row = out['certificates'][name+'_'+str(bits)]
            assert row['hyperbolic'] and not row['lattice']['excludes']
        F = out['certificates']['filled_'+str(bits)]
        assert F['cusps'] == 2 and all(F['complete'])
        assert sa.QQ(F['lattice']['distance_lower']) > sa.QQ(9)/100
        assert out['comparisons'][str(bits)] == dict(opposite_mod_quarter=True, equal_volume=True)
    for name in ('m004', 'cover', 'filled', 'reverse', 'control_5_2'):
        assert out['comparisons'][name] == dict(compatible=True, diameter_shrinks=True)
    assert not out['synthetic']['zero']['excludes']
    assert not out['synthetic']['quarter']['excludes']
    assert out['synthetic']['twenty_fourth']['excludes']


if __name__ == '__main__':
    result = run()
    print(json.dumps(result, indent=2, sort_keys=True), flush=True)
    assert_certificate(result)
    print('INTERVAL CERTIFICATE: PASS', flush=True)
