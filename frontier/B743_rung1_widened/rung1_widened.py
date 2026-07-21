"""RUNG-1 WIDENED — the real-subfield PSLQ sweep (prereg ea860988).
Bases = the programme's REAL tower (the CM-collapse correction): sqrt5 (control), sqrt3, sqrt15,
Q(zeta15)+, Q(zeta20)+ = Q(sqrt(2+phi)) [the Born amplitude field], Q(sqrt(phi)) [F-symbol].
Gates: digits budget per target; height caps 64 (deg2) / 16 (deg4); exact value inside +-1 sigma;
empirical null (50 surrogates per basis x digit-class) must make the hit's chance < 0.02."""
import json, random, sys
from mpmath import mp, mpf, sqrt, cos, pi, pslq, nstr

PHI = None

def bases():
    global PHI
    PHI = (1 + sqrt(5)) / 2
    c15 = 2 * cos(2 * pi / 15)          # deg-4 generator of Q(zeta15)+
    d20 = 2 * cos(pi / 10)              # = sqrt(2+phi), deg-4, Born amplitude field
    sph = sqrt(PHI)                     # deg-4, F-symbol field
    return {
        'B1_sqrt5':   ([mpf(1), sqrt(5)], 64),
        'B2_sqrt3':   ([mpf(1), sqrt(3)], 64),
        'B3_sqrt15':  ([mpf(1), sqrt(15)], 64),
        'B4_z15plus': ([c15**i for i in range(4)], 16),
        'B5_z20plus': ([d20**i for i in range(4)], 16),
        'B6_sqrtphi': ([sph**i for i in range(4)], 16),
    }

def try_pslq(v, basis, maxcoeff, dps):
    """Run PSLQ at the target's own digit budget. Return (coeffs, exact_value) or None."""
    mp.dps = max(16, dps + 6)          # pslq needs >=53 bits; the digit budget lives in tol
    vec = [mpf(v)] + [mp.mpf(b) for b in basis]
    rel = pslq(vec, maxcoeff=maxcoeff, maxsteps=200000, tol=mpf(10) ** (-(dps - 1)))
    if rel is None or rel[0] == 0:
        return None
    exact = -sum(rel[i + 1] * vec[i + 1] for i in range(len(basis))) / rel[0]
    return [int(x) for x in rel], exact

def sweep(targets, nulls_per=50, seed=17):
    random.seed(seed)
    B = bases()
    report = {'hits': [], 'rows': [], 'null_rates': {}}
    # empirical nulls, per basis x digit-class actually present
    digit_classes = sorted(set(t['digits'] for t in targets))
    for bname, (basis, mc) in B.items():
        for dc in digit_classes:
            k = 0
            for _ in range(nulls_per):
                mp.dps = dc + 6
                sur = mpf(random.uniform(0.2, 5.0)) * mpf(10) ** random.randint(-3, 3)
                sur = mpf(nstr(sur, dc))          # truncate to the digit budget
                if try_pslq(sur, basis, mc, dc) is not None:
                    k += 1
            report['null_rates'][f'{bname}|d{dc}'] = k / nulls_per
    # the real targets
    for t in targets:
        v, dps, ru = t['value'], t['digits'], t['rel_unc']
        for bname, (basis, mc) in B.items():
            res = try_pslq(v, basis, mc, dps)
            row = {'target': t['name'], 'basis': bname, 'digits': dps, 'found': bool(res)}
            if res:
                coeffs, exact = res
                mp.dps = dps + 20
                dev = abs(exact - mpf(v)) / abs(mpf(v))
                row.update({'coeffs': coeffs, 'exact_dec': nstr(exact, dps + 4),
                            'within_1sigma': bool(dev <= ru),
                            'null_rate': report['null_rates'][f'{bname}|d{dps}']})
                if row['within_1sigma'] and row['null_rate'] < 0.02:
                    report['hits'].append(row)
            report['rows'].append(row)
    return report

if __name__ == '__main__':
    targets = json.load(open('pdg_targets.json'))
    # honesty filter: PSLQ is meaningless under ~4 digits
    usable = [t for t in targets if t['digits'] >= 4]
    skipped = [t['name'] for t in targets if t['digits'] < 4]
    rep = sweep(usable)
    rep['skipped_low_digits'] = skipped
    json.dump(rep, open('rung1_report.json', 'w'), indent=1)
    print(f"targets swept: {len(usable)}  skipped(<4 digits): {skipped}")
    print(f"null rates: {json.dumps(rep['null_rates'], indent=0)}")
    print(f"GATED HITS: {len(rep['hits'])}")
    for h in rep['hits']:
        print(json.dumps(h))
