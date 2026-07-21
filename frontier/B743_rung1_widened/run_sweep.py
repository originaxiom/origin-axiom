"""Fire the widened rung-1 sweep: cached nulls + PSLQ + transcendental forced-limit interval check."""
import json
exec(open('rung1_widened.py').read().split("if __name__")[0])

targets = json.load(open('pdg_targets.json'))
nulls = json.load(open('null_rates.json'))
CACHED = [4,5,6,8,10,12]
def null_for(bname, dps):
    dc = max([c for c in CACHED if c <= dps] or [4])
    return nulls[f'{bname}|d{dc}']   # conservative: lower digit-class overestimates noise

B = bases()
usable = [t for t in targets if t['digits'] >= 4]
skipped = [t['name'] for t in targets if t['digits'] < 4]
rows, hits = [], []
for t in usable:
    v, dps, ru = t['value'], int(t['digits']), float(t['rel_unc'])
    for bname, (basis, mc) in B.items():
        res = try_pslq(v, basis, mc, dps)
        row = {'target': t['name'], 'basis': bname, 'digits': dps, 'found': bool(res)}
        if res:
            coeffs, exact = res
            mp.dps = dps + 20
            dev = abs(exact - mpf(v)) / abs(mpf(v))
            nr = null_for(bname, dps)
            row.update({'coeffs': coeffs, 'exact_dec': nstr(exact, dps + 4),
                        'within_1sigma': bool(dev <= ru), 'null_rate': nr})
            if row['within_1sigma'] and nr < 0.02:
                hits.append(row)
        rows.append(row)

# transcendental forced-limits: direct interval check (no transforms — pre-registered)
fl = json.load(open('forced_limits.json'))
trans = [f for f in fl if 'transcendental' in str(f.get('field','')).lower()]
tl_hits = []
for f in trans:
    try: x = float(str(f['value_decimal']).replace('i','j').split('+')[0]) if 'i' in str(f['value_decimal']) else float(f['value_decimal'])
    except Exception: continue
    for t in targets:
        v, ru = float(t['value']), float(t['rel_unc'])
        if v != 0 and abs(x - v)/abs(v) <= ru:
            tl_hits.append({'limit': f['name'], 'value': x, 'target': t['name'], 'measured': v})

rep = {'rows': rows, 'hits': hits, 'skipped_low_digits': skipped, 'transcendental_hits': tl_hits,
       'n_targets': len(usable), 'n_bases': len(B)}
json.dump(rep, open('rung1_report.json','w'), indent=1)
found = [r for r in rows if r['found']]
print(f"targets: {len(usable)} usable, skipped(<4 digits): {skipped}")
print(f"PSLQ relations found (pre-gate): {len(found)}")
for r in found: print('  pre-gate:', r['target'], r['basis'], 'coeffs', r.get('coeffs'), '1sig', r.get('within_1sigma'), 'null', r.get('null_rate'))
print(f"GATED HITS (within 1-sigma AND null<2%): {len(hits)}")
for h in hits: print('  HIT:', json.dumps(h))
print(f"transcendental direct hits: {tl_hits if tl_hits else 'NONE'}")
