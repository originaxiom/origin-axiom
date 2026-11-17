"""Post hoc (labelled): the sealed script's L(s, chi_5) root search failed (real variable given a complex function).
Same check, with the root found in the complex s-plane."""
import importlib.util, sys
spec = importlib.util.spec_from_file_location('c1', 'c1_hecke_period.py')
src = open('c1_hecke_period.py').read().split("g5 = findroot")[0]
ns = {}
exec(compile(src.split("# validate the expansion")[0] + src[src.index("# the act's axis"):].split("for s in [mpf(2)")[0], 'c1', 'exec'), ns)
from mpmath import mp, mpc, mpf, findroot
L5, period = ns['L5'], ns['period']
r5 = findroot(L5, mpc('0.5', '6.65'))
print('first zero of L(s, chi_5):', mp.nstr(r5, 20), ' |L5| =', mp.nstr(abs(L5(r5)), 3))
for d in [0, -0.4, 0.4]:
    s = r5 + mpc(0, d)
    print('  |I(', mp.nstr(s, 12), ')| =', mp.nstr(abs(period(s)), 6))
