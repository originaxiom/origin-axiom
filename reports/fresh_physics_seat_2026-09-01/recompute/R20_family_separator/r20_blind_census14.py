#!/usr/bin/env python3
"""R20 blind recompute, stage 1: rebuild the 14-member Q(sqrt(-3)) shape-field family
from the m+s portion (<= 6 ideal tetrahedra) of snappy.OrientableCuspedCensus, with my
own membership test, then compute the seven-property table and the separator column.

Written BEFORE opening B1136's verify_genericity.py / b1136_results.json.

Membership test (own):
  high-precision (212 bit) tetrahedron shapes; each shape z must be a + b*sqrt(3)*i
  with a, b rational of denominator <= 256 (identified by continued fractions), each
  agreeing to < 1e-40; candidates then certified EXACTLY by plugging the exact values
  into the full rectangular gluing equation system over Q(sqrt(3), i) with sympy.
"""
import json, fractions, sys
import snappy
import sympy as sp

PREC_BITS = 212
TOL = sp.Float(10, 50) ** (-40)
DEN_BOUND = 256

def norm_num(x):
    """normalize a snappy Number's string ('1.8 E-77' -> '1.8e-77')"""
    return str(x).replace(' E', 'e').replace('E', 'e')

def rat_approx(x_str, den_bound):
    """best rational approx with denominator <= den_bound, from a decimal string"""
    f = fractions.Fraction(x_str).limit_denominator(den_bound)
    return f

def q_sqrt3_candidate(M, den_bound=DEN_BOUND):
    """Return exact candidate shapes [a + b*sqrt(3)*I, ...] or None."""
    try:
        shapes = M.tetrahedra_shapes('rect', bits_prec=PREC_BITS)
    except Exception:
        return None
    s3 = sp.sqrt(3)
    cands = []
    for z in shapes:
        re = sp.Float(norm_num(z.real()), 60)
        im = sp.Float(norm_num(z.imag()), 60)
        a = rat_approx(norm_num(z.real()), den_bound)
        b_val = im / sp.sqrt(sp.Integer(3))
        b = rat_approx(str(sp.N(b_val, 60)), den_bound)
        a_s = sp.Rational(a.numerator, a.denominator)
        b_s = sp.Rational(b.numerator, b.denominator)
        if abs(re - sp.N(a_s, 60)) > TOL: return None
        if abs(im - sp.N(b_s * s3, 60)) > TOL: return None
        cands.append(a_s + b_s * s3 * sp.I)
    return cands

def certify_gluing(M, cands):
    """Exact check: candidate shapes satisfy ALL gluing equations (rect form) over
    Q(sqrt3, i). Rows: (a_coeffs, b_coeffs, c) meaning prod z_i^a * (1-z_i)^b = c."""
    eqns = M.gluing_equations('rect')
    for (A, B, c) in eqns:
        lhs = sp.Integer(1)
        for zi, ai, bi in zip(cands, A, B):
            if ai: lhs *= zi ** int(ai)
            if bi: lhs *= (1 - zi) ** int(bi)
        diff = sp.simplify(sp.expand(sp.radsimp(lhs - sp.Integer(int(c)))))
        if diff != 0:
            # try harder
            diff = sp.nsimplify(sp.simplify(diff))
            if sp.simplify(diff) != 0:
                return False
    return True

def is_amphichiral(M):
    Mm = M.copy()
    Mm.reverse_orientation()
    for _ in range(3):
        try:
            return M.is_isometric_to(Mm)
        except RuntimeError:
            M.randomize(); Mm.randomize()
    return None

def props(name):
    M = snappy.Manifold(name)
    h1 = M.homology()
    elem = h1.elementary_divisors()
    vol = float(M.volume())
    try:
        cs = float(M.chern_simons())
    except Exception:
        cs = None
    return {
        'name': name,
        'h1': str(h1),
        'elementary_divisors': [int(e) for e in elem],
        'h1_is_Z': elem == [0],
        'volume': vol,
        'tets': M.num_tetrahedra(),
        'cusps': M.num_cusps(),
        'torsion_free': all(e == 0 for e in elem),
        'amphichiral': is_amphichiral(M),
        'cs': cs,
        'cs_is_zero': (cs is not None) and (min(abs(cs), abs(abs(cs) - 0.5)) < 1e-9 and abs(cs) < 1e-9),
    }

def main():
    # stage 1: scan m+s census (<= 6 tets)
    fam = []
    scanned = 0
    for M in snappy.OrientableCuspedCensus:
        nm = M.name()
        if not (nm.startswith('m') or nm.startswith('s')):
            break
        scanned += 1
        # cheap double-precision prefilter
        try:
            sh = [complex(z) for z in M.tetrahedra_shapes('rect')]
        except Exception:
            continue
        ok = True
        for z in sh:
            a = fractions.Fraction(z.real).limit_denominator(DEN_BOUND)
            b = fractions.Fraction(z.imag / 3**0.5).limit_denominator(DEN_BOUND)
            if abs(z.real - float(a)) > 1e-9 or abs(z.imag - float(b)*3**0.5) > 1e-9:
                ok = False; break
        if not ok:
            continue
        cands = q_sqrt3_candidate(M)
        if cands is None:
            continue
        if certify_gluing(M, cands):
            fam.append((nm, [str(c) for c in cands]))
            print(f"MEMBER {nm} shapes={[str(c) for c in cands]}", flush=True)
    print(f"scanned {scanned} m+s manifolds; family size = {len(fam)}")
    names = [f[0] for f in fam]

    # negative control: m006 must NOT be a member
    m006 = q_sqrt3_candidate(snappy.Manifold('m006'))
    print("control m006 candidate (expect None):", m006)

    # stage 2: property table
    table = [props(nm) for nm in names]

    # separator determination: a property separates m004 iff no other member shares
    # m004's value
    m004 = next(r for r in table if r['name'] == 'm004')
    seps = {}
    def sharers(key, eq):
        return [r['name'] for r in table if r['name'] != 'm004' and eq(r[key], m004[key])]
    seps['h1_is_Z'] = sharers('h1_is_Z', lambda x, y: x == y and y)
    seps['volume'] = sharers('volume', lambda x, y: abs(x - y) < 1e-9)
    seps['tets'] = sharers('tets', lambda x, y: x == y)
    seps['cusps'] = sharers('cusps', lambda x, y: x == y)
    seps['torsion_free'] = sharers('torsion_free', lambda x, y: x == y and y)
    seps['amphichiral'] = sharers('amphichiral', lambda x, y: x == y and y)
    seps['cs_is_zero'] = sharers('cs_is_zero', lambda x, y: x == y and y)
    separators = [k for k, v in seps.items() if len(v) == 0]

    # volume ladder: vol / V_gieseking, V_gie = 2*Lobachevsky(pi/6)
    import mpmath as mp
    mp.mp.dps = 50
    V_gie = mp.mpf(2) * (mp.clsin(2, mp.pi/3) / 2)  # Lobachevsky(pi/6)? compute properly below
    # Lobachevsky Lambda(theta) = 1/2 * Cl_2(2 theta); V_gie = 2*Lambda(pi/6) -> Cl_2(pi/3)
    V_gie = mp.clsin(2, mp.pi / 3)
    ladder = {r['name']: float(mp.mpf(repr(r['volume'])) / V_gie) for r in table}

    out = {
        'family': names,
        'family_size': len(fam),
        'shapes': dict(fam),
        'table': table,
        'shared_with_m004': seps,
        'separators': separators,
        'V_gieseking': float(V_gie),
        'volume_over_Vgie': ladder,
    }
    with open(sys.path[0] + '/r20_blind_census14_results.json', 'w') as fh:
        json.dump(out, fh, indent=1)
    print(json.dumps({k: out[k] for k in ['family', 'separators', 'shared_with_m004', 'volume_over_Vgie']}, indent=1))

if __name__ == '__main__':
    main()
