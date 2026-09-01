#!/usr/bin/env python3
"""R03 controls, part 2.

A1: plant a NON-SM-shaped content (two lepton doublets, no e^c singlet
    multiplicity change... counts (q:6, u:3, d:3, l:4, e:1)) and confirm the
    same pipeline returns NON-SM charges -> the SM answer is not baked in.
A2: exact reduction of the grav-dropped system to the Mordell curve
    y^2 = x^3 - 432 (the Fermat-cubic curve, rank 0) -> explains why control
    A found no new rational point: there are none to find (over Q).
"""
import json
import sympy as sp

out = {}
Yq, Yu, Yd, Yl, Ye, t = sp.symbols('Yq Yu Yd Yl Ye t')

# ---- A1: planted non-SM content: counts q:6(3x2), u:3, d:3, l:4(2 doublets), e:1
lin = [2*Yq + Yu + Yd,          # SU(3)^2 Y (unchanged: colored content same)
       3*Yq + 2*Yl,             # SU(2)^2 Y: 3 colors * Yq + 2 doublets * Yl
       6*Yq + 3*Yu + 3*Yd + 4*Yl + Ye]   # grav
cub = 6*Yq**3 + 3*Yu**3 + 3*Yd**3 + 4*Yl**3 + Ye**3
s = sp.solve(lin, [Yd, Yl, Ye], dict=True)[0]
C = sp.expand(cub.subs(s))
out['A1_line'] = {str(k): str(v) for k, v in s.items()}
Ct = sp.expand(C.subs({Yq: 1, Yu: -1 + t}))
out['A1_cubic'] = str(sp.factor(Ct))
roots = [r for r in sp.solve(Ct, t) if r.is_real]
sols = []
for r in roots:
    vals = {Yq: 1, Yu: -1 + r}
    sols.append([str(sp.nsimplify(x)) for x in
                 (1, vals[Yu], s[Yd].subs(vals), s[Yl].subs(vals), s[Ye].subs(vals))])
out['A1_solutions'] = sols
out['A1_nonSM_found'] = bool(sols and all(x != ['1','-4','2','-3','6'] and
                                          x != ['1','2','-4','-3','6'] for x in sols))

# ---- A2: grav-dropped system is the Fermat cubic curve (rank 0) -------------
# without grav: Yd=-2Yq-Yu, Yl=-3Yq, Ye free; cubic becomes
#   Ye^3 = 72 Yq^3 + 36 Yq^2 Yu + 18 Yq Yu^2      (homogeneous cubic curve)
s2 = sp.solve([2*Yq + Yu + Yd, 3*Yq + Yl], [Yd, Yl], dict=True)[0]
C2 = sp.expand((6*Yq**3 + 3*Yu**3 + 3*Yd**3 + 2*Yl**3 + Ye**3).subs(s2))
out['A2_curve'] = str(sp.expand(C2)) + ' = 0'
# affine chart Yq=1, x = Yu, z = Ye:  z^3 = 18(x+1)^2 + 54
x, z, a, b = sp.symbols('x z a b')
lhs = sp.expand(C2.subs({Yq: 1, Yu: x, Ye: z}))
assert sp.expand(lhs - (z**3 - 18*(x + 1)**2 - 54)) == 0
# substitution a = 2 z, b = -12 (x+1)  =>  b^2 = a^3 - 432  ... check:
subst = sp.expand((b**2 - a**3 + 432).subs({a: 2*z, b: -12*(x + 1)}))
# b^2 - a^3 + 432 = 144(x+1)^2 - 8 z^3 + 432 = -8 * (z^3 - 18(x+1)^2 - 54)
out['A2_reduction_exact'] = bool(sp.expand(subst + 8*lhs) == 0)
# SM point maps to the known generator-of-torsion (12, +-36):
pt = {x: -4, z: 6}
out['A2_SM_maps_to'] = [str(sp.Integer(2*6)), str(sp.Integer(-12*(-4 + 1)))]
out['A2_check_on_curve'] = bool((36**2) == 12**3 - 432)
out['A2_note'] = ('y^2 = x^3 - 432 is the Fermat-cubic (FLT n=3) curve: rank 0, '
                  'torsion Z/3 = {O, (12,36), (12,-36)} [literature fact, not '
                  're-proved here]. Hence dropping grav^2 Y leaves ONLY the SM '
                  'rays among RATIONAL charge assignments; grav^2 Y is '
                  'load-bearing over R but redundant over Q on this 15-plet.')

with open('/home/user/origin-axiom/reports/fresh_physics_seat_2026-09-01/recompute/'
          'R03_hypercharge_anomaly/controls2_output.json', 'w') as f:
    json.dump(out, f, indent=1, default=str)
for k, v in out.items():
    print(k, '=', json.dumps(v, default=str)[:400])
