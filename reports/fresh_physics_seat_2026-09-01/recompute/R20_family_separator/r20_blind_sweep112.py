#!/usr/bin/env python3
"""R20 blind recompute, stage 2: my own full sweep of snappy.OrientableCuspedCensus
(212,641) for criterion (B): every tetrahedron shape in Q(sqrt(-3)), denominator
bound 256. Candidates from double-precision shapes; each candidate then re-identified
at 212 bits (1e-40 agreement) and EXACTLY certified against the full rectangular
gluing-equation system over Q(sqrt3, i) via sympy.

Also: regular-ideal subcount (criterion A: all shapes == 1/2 + sqrt(3)i/2),
amphichirality for all members, H1=Z members, volume ladder, and t06829 detail.

Written BEFORE opening B1186/verification/.
"""
import json, fractions, sys, time
import snappy
import importlib.util

HERE = '/home/user/origin-axiom/reports/fresh_physics_seat_2026-09-01/recompute/R20_family_separator'
spec = importlib.util.spec_from_file_location('r20', HERE + '/r20_blind_census14.py')
r20 = importlib.util.module_from_spec(spec); spec.loader.exec_module(r20)

DEN_BOUND = 256
TOL_D = 1e-9

def double_prefilter(M):
    try:
        sh = [complex(z) for z in M.tetrahedra_shapes('rect')]
    except Exception:
        return None
    out = []
    for z in sh:
        a = fractions.Fraction(z.real).limit_denominator(DEN_BOUND)
        b = fractions.Fraction(z.imag / 3**0.5).limit_denominator(DEN_BOUND)
        if abs(z.real - float(a)) > TOL_D or abs(z.imag - float(b)*3**0.5) > TOL_D:
            return None
        out.append((a, b))
    return out

def main():
    t0 = time.time()
    cand_names = []
    total = 0
    for M in snappy.OrientableCuspedCensus:
        total += 1
        pf = double_prefilter(M)
        if pf is not None:
            cand_names.append((M.name(), pf))
    print(f"prefilter: {len(cand_names)} candidates of {total} in {time.time()-t0:.0f}s", flush=True)

    members = []
    import sympy as sp
    for nm, pf in cand_names:
        M = snappy.Manifold(nm)
        cands = r20.q_sqrt3_candidate(M)
        if cands is None:
            print(f"  {nm}: FAILED high-precision identification (prefilter false positive)", flush=True)
            continue
        if r20.certify_gluing(M, cands):
            dens = [max(fractions.Fraction(a).denominator, fractions.Fraction(b).denominator) for a, b in pf]
            regular = all(a == fractions.Fraction(1,2) and b == fractions.Fraction(1,2) for a, b in pf)
            members.append({'name': nm, 'tets': M.num_tetrahedra(), 'cusps': M.num_cusps(),
                            'volume': float(M.volume()), 'max_den': max(dens), 'regular': regular,
                            'h1_elem': [int(e) for e in M.homology().elementary_divisors()]})
            print(f"  MEMBER {nm} tets={M.num_tetrahedra()} cusps={M.num_cusps()} "
                  f"maxden={max(dens)} regular={regular}", flush=True)
        else:
            print(f"  {nm}: exact certification FAILED", flush=True)

    print(f"family size = {len(members)}  (regular = {sum(m['regular'] for m in members)})", flush=True)

    # amphichirality for all members
    import mpmath as mp
    mp.mp.dps = 50
    V_gie = mp.clsin(2, mp.pi/3)
    for m in members:
        M = snappy.Manifold(m['name'])
        m['amphichiral'] = r20.is_amphichiral(M)
        m['vol_over_Vgie'] = float(mp.mpf(repr(m['volume'])) / V_gie)
        m['h1_is_Z'] = m['h1_elem'] == [0]

    h1Z = [m['name'] for m in members if m['h1_is_Z']]
    amph = sum(1 for m in members if m['amphichiral'])
    non_amph = [m['name'] for m in members if m['amphichiral'] is not True]
    print('H1=Z members:', h1Z)
    print(f'amphichiral: {amph}/{len(members)}; not-confirmed: {non_amph}')
    ladder_bad = [m['name'] for m in members if abs(m['vol_over_Vgie'] - round(m['vol_over_Vgie'])) > 1e-9]
    print('volume-ladder violators:', ladder_bad)

    out = {'family_size': len(members), 'regular_count': sum(m['regular'] for m in members),
           'h1Z_members': h1Z, 'amphichiral_count': amph, 'non_amphichiral': non_amph,
           'ladder_violators': ladder_bad, 'V_gieseking': float(V_gie), 'members': members,
           'runtime_s': time.time()-t0}
    with open(HERE + '/r20_blind_sweep112_results.json', 'w') as fh:
        json.dump(out, fh, indent=1)
    print('done in %.0fs' % (time.time()-t0))

if __name__ == '__main__':
    main()
