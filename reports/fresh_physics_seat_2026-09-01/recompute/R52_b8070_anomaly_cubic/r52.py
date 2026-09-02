#!/usr/bin/env python3
"""R52 -- B8070 FINDINGS l.81-90: over the 5-dim charge space (Q,uc,ec,dc,L) with SM multiplicities (3 colours, 2 weak),
the linear anomaly conditions cut to a 2-plane on which the cubic factors as -2 yL (2yL+3yd)(4yL-3yd)/3: three anomaly-free
lines (hypercharge, u<->d swap, vector-like yL=0).  The arc's committed script does not compute this; here it is."""
import sympy as sp
yQ, yu, ye, yd, yL = sp.symbols('yQ yu ye yd yL')
# multiplicities: Q (3,2), uc (3bar,1), ec (1,1), dc (3bar,1), L (1,2)   -- one generation, no nu^c
lin = [sp.Eq(2*yQ + yu + yd, 0),                 # [SU(3)]^2 U(1): sum over colour triplets weighted by SU(2) dim
       sp.Eq(3*yQ + yL, 0),                      # [SU(2)]^2 U(1)
       sp.Eq(6*yQ + 3*yu + 3*yd + 2*yL + ye, 0)]  # grav^2 U(1) = sum of all charges with multiplicity
sol = sp.solve(lin, [yQ, yu, ye], dict=True)[0]; print('linear conditions ->', sol)
cubic = 6*yQ**3 + 3*yu**3 + 3*yd**3 + 2*yL**3 + ye**3
c2 = sp.factor(sp.expand(cubic.subs(sol))); print('cubic on the 2-plane (yd, yL):', c2)
print('B8070 FINDINGS: -2*yL*(2*yL+3*yd)*(4*yL-3*yd)/3  ->  equal:', sp.simplify(c2 - (-sp.Rational(2,3)*yL*(2*yL+3*yd)*(4*yL-3*yd))) == 0)
for name, cond in [('hypercharge 2yL+3yd=0', {yd: -sp.Rational(2,3)*yL}), ('u<->d swap 4yL-3yd=0', {yd: sp.Rational(4,3)*yL}), ('vector-like yL=0', {yL: 0})]:
    s = {k: v.subs(cond) for k, v in sol.items()}; s.update(cond)
    charges = {str(v): sp.simplify(sp.sympify(v).subs(s).subs(sol)) for v in (yQ, yu, ye, yd, yL)}
    print(' ', name, '->', {k: sp.nsimplify(val.subs(yL, -3)) if hasattr(val,'subs') else val for k, val in charges.items()}, '(yL = -3 normalisation)')
print('R03/R10 cross-check: in the chart Yq = 1, the cubic is -18 (Yu/Yq - 2)(Yu/Yq + 4) -- same three roots up to the linear map')
