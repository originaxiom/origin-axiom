#!/usr/bin/env python3
"""R51 -- family-wide amphichirality re-test. B1186's family_census.py (main) and B1181's reproduce.sh test amphichirality by
M.is_isometric_to(W) with W = mirror of M; SnapPy's is_isometric_to allows orientation-REVERSING isometries, so that
test is True for every orientable manifold (vacuous).  Here: symmetry_group().is_amphicheiral() (the orientation-aware
test) and the Chern-Simons obstruction (amphichiral => 2 CS = 0 mod 1/2) on every member of B1186's census family."""
import json, snappy, time, math
d = json.load(open('family_census_b1186.json'))
B = d['members_B']; A = d['members_A']
print('B (shape field in Q(sqrt-3)):', len(B), '  A (all regular ideal):', len(A), '  banked amphichirality_failures:', d.get('amphichirality_failures'))
rows = []
for name in B:
    M = snappy.Manifold(name)
    try: S = M.symmetry_group(); amph = S.is_amphicheiral(); order = S.order()
    except Exception: amph = None; order = None
    try: cs = float(M.chern_simons())
    except Exception: cs = float('nan')
    twocs = (2 * cs) % 0.5; cs_ok = (min(twocs, 0.5 - twocs) < 1e-6) if not math.isnan(cs) else None
    W = M.copy(); W.reverse_orientation()
    try: iso = M.is_isometric_to(W)
    except Exception: iso = None
    rows.append(dict(name=name, in_A=name in A, sym_order=order, is_amphicheiral=amph, CS=cs, CS_compatible=cs_ok, is_isometric_to_mirror=iso, cusps=M.num_cusps(), vol=float(M.volume())))
json.dump(rows, open('r51_results.json', 'w'), indent=1)
chir = [r for r in rows if r['is_amphicheiral'] is False]
print('is_isometric_to(mirror) True for all %d members: %s  <- the instrument B1181/B1186 used' % (len(rows), all(r['is_isometric_to_mirror'] for r in rows)))
print('symmetry_group().is_amphicheiral(): True %d, False %d, failed %d' % (sum(r['is_amphicheiral'] is True for r in rows), len(chir), sum(r['is_amphicheiral'] is None for r in rows)))
print('CS-obstructed (2CS != 0 mod 1/2, i.e. provably chiral): %d ; of which symmetry test also says chiral: %d' % (sum(r['CS_compatible'] is False for r in rows), sum(1 for r in rows if r['CS_compatible'] is False and r['is_amphicheiral'] is False)))
print('among the all-regular A (%d): amphichiral %d, chiral %d' % (len(A), sum(r['is_amphicheiral'] is True for r in rows if r['in_A']), sum(r['is_amphicheiral'] is False for r in rows if r['in_A'])))
print('chiral members (name, in_A, sym order, CS):')
for r in chir: print('  %-14s A=%d order=%s CS=%+.6f cusps=%d vol=%.6f' % (r['name'], r['in_A'], r['sym_order'], r['CS'], r['cusps'], r['vol']))
print("B1181's five spot-checks:", {n: next((r['is_amphicheiral'], round(r['CS'], 6)) for r in rows if r['name'] == n) if any(r['name'] == n for r in rows) else 'not in B' for n in ['m004', 's955', 'o10_150700', 'o10_150684', 't12840']})
