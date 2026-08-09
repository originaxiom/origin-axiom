r"""S3-a: the two clocks, and the check that the observer's clock spectrum is
the banked length spectrum. Gate 5-Q; structure only."""
from mpmath import mp, mpf, sqrt, log

mp.dps = 30
BANKED_SYSTOLE = mpf('1.08707014499574')          # B850

phi = (1 + sqrt(5)) / 2
h_suspension = log(phi ** 2)                       # clock 1: object, hearing
h_geodesic = mpf(2)                                # clock 2: observer, = n-1

kappa = (3 + sqrt(-3)) / 2                         # shortest loxodromic trace
lam = (kappa + sqrt(kappa ** 2 - 4)) / 2
ell = 2 * log(abs(lam))

print(f'clock 1  suspension of RL : entropy {mp.nstr(h_suspension,15)}  (II_1, tracial)')
print(f'clock 2  geodesic flow    : entropy {mp.nstr(h_geodesic,15)}  (III_1, core II_inf)')
assert abs(h_suspension - h_geodesic) > mpf('1'), 'the clocks must differ'
print('  -> distinct flows: B721\'s "two clocks" confirmed')

print(f'\nobserver clock spectrum vs banked length spectrum:')
print(f'  ell from Q(sqrt-3) traces : {mp.nstr(ell,18)}')
print(f'  banked systole (B850)     : {mp.nstr(BANKED_SYSTOLE,18)}')
print(f'  |difference|              : {mp.nstr(abs(ell-BANKED_SYSTOLE),6)}')
assert abs(ell - BANKED_SYSTOLE) < mpf('1e-13')
print('  MATCH — the observer clock\'s periods are the banked length spectrum')
