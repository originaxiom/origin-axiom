"""Run 1b: plant P2 placed where it can be seen.
(a) sign error in d(g^-1)/dg on m004's base characters: the Milnor match must break.
(b) dropped factor g^-1 on b+-LR's mixed characters (fibre generators carry nontrivial rho): tau = +-zeta^m (rho(l)-1)
    must break, or the k=0 non-acyclicity must break.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tcore import *

gens, rels = hnn(phi_word('LR', 1))
broken = 0
for e in characters(gens, rels):
    if e['t'] == 0:
        continue
    tau, _ = wada(gens, rels, e, planted_bad_inverse='sign')
    x = zpow(e['t'])
    mt = div(add(sub(mul(x, x), scal(3, x)), ONE), sub(x, ONE))
    if is0(tau) or unit_root(div(tau, mt)) is None:
        broken += 1
print(f'P2a (sign error) on m004 base characters: Milnor match broken on {broken}/4 -> '
      f'{"CAUGHT" if broken else "NOT CAUGHT"}')

for mode in (True, 'sign'):
    gens, rels = hnn(phi_word('LR', -1))
    broken = 0
    tot = 0
    for e in characters(gens, rels):
        if (e['a'], e['b']) == (0, 0):
            continue
        tot += 1
        tau, _ = wada(gens, rels, e, planted_bad_inverse=mode)
        good_tau, _ = wada(gens, rels, e)
        if e['t'] == 0:
            ok = is0(tau)
        else:
            ok = (not is0(tau)) and unit_root(div(tau, sub(zpow(e['t']), ONE))) is not None
        if not ok:
            broken += 1
    print(f'P2b mode={mode!r} on b+-LR fibre-nontrivial characters: identity broken on {broken}/{tot} -> '
          f'{"CAUGHT" if broken else "NOT CAUGHT"}')
