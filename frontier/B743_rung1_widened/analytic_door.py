"""The analytic door: L(E15a8,2), L'(E,0), periods, Mahler — vs the 18 PDG targets.
Plus the deg-8 real compositum Q(zeta60)+ PSLQ on the >=10-digit targets."""
import json, random
from mpmath import mp, mpf, mpc, sqrt, cos, pi, exp, gamma, pslq, nstr, zeta
from snappy.pari import pari

mp.dps = 40
pari.set_real_precision(60)

# --- the curve: 15a8 candidate model [1,1,1,0,0]; VERIFY conductor 15, j=-1/15 ---
E = pari.ellinit([1,1,1,0,0])
cond = E.ellglobalred()[0]
j = pari(E[12])   # j-invariant = component 12 of ellinit
print('curve check: conductor =', cond, ' j =', j)
assert str(cond) == '15' and str(j) == '-1/15', 'wrong curve model!'

# --- L-values via PARI lfun (high precision) ---
L2  = mpf(str(pari.lfun(E, 2)))                    # L(E,2)
L1  = mpf(str(pari.lfun(E, 1)))                    # L(E,1) (rank 0, nonzero)
Lp0 = mpf(str(pari.lfun(E, 0, 1)))                 # L'(E,0)
om  = E.ellperiods() if hasattr(E,'ellperiods') else None
Ore = mpf(str(pari(E[14][0]).real())) if om is None else mpf(str(pari(om[0]).real()))
print('L(E,2) =', nstr(L2, 20)); print("L'(E,0) =", nstr(Lp0, 20)); print('L(E,1) =', nstr(L1, 20))
print('Omega_re =', nstr(Ore, 20))

VOL = mpf('2.029883212819307250042405108549')       # Vol(4_1)
names = {
 'L(E,2)':          L2,
 "L'(E,0)":         Lp0,
 'Mahler=Vol/2pi':  VOL/(2*pi),                     # banked normalization (L3: being volume); flag
 'Mahler=Vol/pi':   VOL/pi,                         # alt normalization, flagged
 'Omega_re':        Ore,
 'L2/(pi*Omega)':   L2/(pi*Ore),
 "L'0/pi":          Lp0/pi,
}
targets = json.load(open('pdg_targets.json'))
hits, chance_sum = [], 0.0
for nm, x in names.items():
    for t in targets:
        v, ru = mpf(t['value']), float(t['rel_unc'])
        chance_sum += 2*ru   # per-pair chance a fixed number lands in +-1sigma (unit log-density)
        if v != 0 and abs(x - v)/abs(v) <= ru:
            hits.append({'number': nm, 'value': nstr(x, 12), 'target': t['name'],
                         'measured': str(t['value']), 'rel_unc': ru, 'per_pair_chance': 2*ru})
print('pairs tested:', len(names)*len(targets), ' summed chance-expectation ~', round(chance_sum,3))
print('ANALYTIC HITS (within 1sigma):', json.dumps(hits, indent=1) if hits else 'NONE')

# --- deg-8 door: Q(zeta60)+ on >=10-digit targets ---
mp.dps = 30
c60 = 2*cos(pi/30)          # 2cos(2pi/60), generator of Q(zeta60)+, degree 8
basis = [c60**i for i in range(8)]
prec10 = [t for t in targets if t['digits'] >= 10]
random.seed(23)
nullhits = 0
for _ in range(50):
    dc = 10
    sur = mpf(random.uniform(0.2,5.0)) * mpf(10)**random.randint(-3,3)
    sur = mpf(nstr(sur, dc))
    mp.dps = max(16, dc+6)
    r = pslq([sur]+basis, maxcoeff=8, maxsteps=300000, tol=mpf(10)**(-(dc-1)))
    if r is not None and r[0] != 0: nullhits += 1
print(f'zeta60+ null (d10, maxcoeff 8): {nullhits}/50')
d8 = []
for t in prec10:
    dps = int(t['digits']); mp.dps = max(16, dps+6)
    r = pslq([mpf(t['value'])]+basis, maxcoeff=8, maxsteps=300000, tol=mpf(10)**(-(dps-1)))
    d8.append({'target': t['name'], 'digits': dps, 'found': bool(r and r[0]!=0),
               'coeffs': [int(x) for x in r] if r else None})
print('deg-8 zeta60+ on ultra-precise targets:', json.dumps(d8))
json.dump({'analytic_hits': hits, 'chance_sum': chance_sum, 'deg8': d8, 'null_z60': nullhits/50,
           'L2': nstr(L2,25), 'Lp0': nstr(Lp0,25), 'Omega_re': nstr(Ore,25)},
          open('analytic_report.json','w'), indent=1)
