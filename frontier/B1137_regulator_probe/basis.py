"""R48-3 -- basis assembly (STEP 1 continued). Builds the fixed regulator/constant basis
from regulators.compute_all(), at a declared working precision. Gate 5: no SM value enters here.
"""
from mpmath import mp, mpf, pi, sqrt, log
import regulators as regmod

PHI_LABEL = 'logphi'

def build_basis(dps=90):
    R = regmod.compute_all(dps=dps)
    mp.dps = dps + 15
    b = {}
    # E6 end: K = Q(sqrt(-3))
    for n in range(1, 7):
        b[f'Lm3_{n}'] = R['L_chi_m3'][n]
    for n in range(2, 7):
        b[f'zetaK_{n}'] = R['zetaK'][n]
        b[f'zetaK_{n}_pinorm'] = R['zetaK'][n] / pi**n
    # E8 end: K = Q(sqrt(5))
    for n in range(1, 5):
        b[f'L5_{n}'] = R['L_chi_5'][n]
    for n in range(2, 5):
        b[f'zetaF_{n}'] = R['zetaF'][n]
        b[f'zetaF_{n}_pinorm'] = R['zetaF'][n] / pi**n
    # admitted transcendental constants (sec A)
    b['pi'] = +pi
    b['sqrt3'] = sqrt(3)
    b['sqrt5'] = sqrt(5)
    b['logphi'] = log((1 + sqrt(5)) / 2)
    b['zeta3'] = R['zeta_plain'][3]

    forms = {
        'FULL': list(b.keys()),
        'E6_only': [k for k in b if k.startswith(('Lm3_', 'zetaK_')) or k in ('pi', 'sqrt3', 'zeta3')],
        'E8_only': [k for k in b if k.startswith(('L5_', 'zetaF_')) or k in ('pi', 'sqrt5', 'logphi')],
    }
    return b, forms, R

# Empirically pruned basis (see basis_hygiene_check.py for the derivation + full provenance log):
# removes exact LINEAR redundancies among the raw+pi-normalized regulators (found by running PSLQ
# on the basis alone, V-free, at dps=220/H=1e6 -- each drop verified to be an EXACT rational
# multiple of a surviving entry, so no S:A discriminating power is lost, only duplicate directions).
PRUNED_DROP = ['zetaF_2_pinorm', 'zetaF_2', 'zetaK_2_pinorm', 'zetaF_4_pinorm',
               'zetaK_4_pinorm', 'zetaK_6_pinorm']

def build_pruned_basis(dps=90):
    b, forms, R = build_basis(dps=dps)
    pruned_full = [k for k in forms['FULL'] if k not in PRUNED_DROP]
    forms_p = {
        'FULL': pruned_full,
        'E6_only': [k for k in pruned_full if k.startswith(('Lm3_', 'zetaK_')) or k in ('pi', 'sqrt3', 'zeta3')],
        'E8_only': [k for k in pruned_full if k.startswith(('L5_', 'zetaF_')) or k in ('pi', 'sqrt5', 'logphi')],
    }
    return b, forms_p, R

if __name__ == '__main__':
    b, forms, R = build_pruned_basis(dps=90)
    print(f"PRUNED basis size FULL = {len(forms['FULL'])}")
    print(f"PRUNED basis size E6_only = {len(forms['E6_only'])}")
    print(f"PRUNED basis size E8_only = {len(forms['E8_only'])}")
    for k in forms['FULL']:
        print(f"  {k:20s} = {mp.nstr(b[k], 25)}")
