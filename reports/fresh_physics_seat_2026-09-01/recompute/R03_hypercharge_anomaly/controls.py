#!/usr/bin/env python3
"""R03 controls: show the instrument CAN find excluded things when planted.

Control A (B1160): drop the grav^2 Y condition -> non-SM solutions must appear.
Control B (B1170): widen the alphabet with an adjoint G(8,1) -> new rigid
                   chiral survivors beyond the 2 must appear.
"""
import itertools, json
import sympy as sp

out = {}

# ---- Control A: B1160 without grav^2 Y --------------------------------------
Yq, Yu, Yd, Yl, Ye = sp.symbols('Yq Yu Yd Yl Ye')
lin2 = [2*Yq + Yu + Yd, 3*Yq + Yl]          # grav dropped
cubic = 6*Yq**3 + 3*Yu**3 + 3*Yd**3 + 2*Yl**3 + Ye**3
s = sp.solve(lin2, [Yd, Yl], dict=True)[0]
C = sp.expand(cubic.subs(s))                # homogeneous cubic in (Yq, Yu, Ye)
out['A_cubic_without_grav'] = str(sp.factor(C))
# find a concrete non-SM rational solution with Yq=1 (scale fixed), Ye free:
found = []
for yu in [sp.Rational(n, 6) for n in range(-30, 31)]:
    Ce = sp.expand(C.subs({Yq: 1, Yu: yu}))
    for r in sp.roots(sp.Poly(Ce, Ye), Ye):
        if r.is_rational:
            sol = (1, yu, s[Yd].subs({Yq: 1, Yu: yu}), s[Yl].subs({Yq: 1}), r)
            grav = 6*sol[0] + 3*sol[1] + 3*sol[2] + 2*sol[3] + sol[4]
            if grav != 0:                    # genuinely non-SM (violates grav)
                found.append([str(x) for x in sol])
    if len(found) >= 3:
        break
out['A_nonSM_solutions_found_when_grav_dropped'] = found[:3]
out['A_control_pass'] = len(found) > 0

# ---- Control B: census with adjoint letter G(8,1) ---------------------------
ALPHA = {
    'A(3,2)':  ('3', 2), 'B(3b,2)': ('3b', 2), 'C(3,1)': ('3', 1),
    'D(3b,1)': ('3b', 1), 'E(1,2)': ('1', 2), 'F(1,1)': ('1', 1),
    'G(8,1)':  ('8', 1),
}
CONJ3 = {'3': '3b', '3b': '3', '1': '1', '8': '8'}
CDIM = {'3': 3, '3b': 3, '1': 1, '8': 8}
ACOEF = {'3': 1, '3b': -1, '1': 0, '8': 0}          # SU(3)^3 anomaly coeff
TIDX = {'3': 1, '3b': 1, '1': 0, '8': 6}            # 2*T(R)/2T(fund): 3->1, 8->6

def states_of(content, charges):
    return [(ALPHA[n][0], ALPHA[n][1], y) for n, y in zip(content, charges)]

def is_vectorlike(states):
    ms = sorted(states, key=str)
    cs = sorted([(CONJ3[l], d, -y) for (l, d, y) in states], key=str)
    return ms == cs

def massable(states):
    n = len(states)
    for i in range(n):
        li, di, yi = states[i]
        if li in ('1', '8') and di == 1 and yi == 0:
            return True                     # real color rep, weak singlet, Y=0
        for j in range(i+1, n):
            lj, dj, yj = states[j]
            if dj == di and yj == -yi and lj == CONJ3[li]:
                return True
    return False

def analyze(content):
    ys = sp.symbols('y0:5')
    e_su3 = sp.Integer(0); e_su2 = sp.Integer(0)
    e_grav = sp.Integer(0); e_cub = sp.Integer(0)
    for k, name in enumerate(content):
        lbl, su2d = ALPHA[name]
        e_su3 += TIDX[lbl] * su2d * ys[k]
        if su2d == 2:
            e_su2 += CDIM[lbl] * ys[k]
        e_grav += CDIM[lbl] * su2d * ys[k]
        e_cub += CDIM[lbl] * su2d * ys[k]**3
    A, _ = sp.linear_eq_to_matrix([e_su3, e_su2, e_grav], ys)
    ns = A.nullspace()
    d = len(ns)
    rays = []
    if d == 2:
        a0, a1 = sp.symbols('a0 a1')
        yvec = [sp.expand(a0*ns[0][k] + a1*ns[1][k]) for k in range(5)]
        cub = sp.expand(e_cub.subs(dict(zip(ys, yvec))))
        if cub != 0:
            u = sp.symbols('u')
            q = sp.Poly(sp.expand(cub.subs({a0: u, a1: 1})), u)
            cand = [(r, sp.Integer(1)) for r in sp.roots(q, u) if r.is_rational] \
                if q.degree() >= 1 else []
            if sp.expand(cub.subs({a1: 0, a0: 1})) == 0:
                cand.append((sp.Integer(1), sp.Integer(0)))
            for r0, r1 in cand:
                y = [sp.nsimplify(v.subs({a0: r0, a1: r1})) for v in yvec]
                nz = [v for v in y if v != 0]
                if not nz:
                    continue
                y = [sp.nsimplify(v/nz[0]) for v in y]
                st = states_of(content, y)
                rays.append({'charges': [str(v) for v in y],
                             'vector_like': is_vectorlike(st),
                             'massable': massable(st)})
    return d, rays

contents = list(itertools.combinations_with_replacement(list(ALPHA), 5))
out['B_census_total_7letters'] = len(contents)     # C(11,5) = 462
color_safe = [c for c in contents
              if sum(ACOEF[ALPHA[n][0]] * ALPHA[n][1] for n in c) == 0]
out['B_color_safe'] = len(color_safe)

survivors = []
for c in color_safe:
    d, rays = analyze(c)
    ok = [r for r in rays if not r['vector_like'] and not r['massable']]
    if ok:
        survivors.append({'content': list(c), 'rays': [r['charges'] for r in ok]})
out['B_rigid_chiral_survivors_with_adjoint'] = len(survivors)
out['B_new_nonSM_survivors'] = [s for s in survivors
                                if 'G(8,1)' in s['content']][:5]
out['B_control_pass'] = len(survivors) > 2

with open('/home/user/origin-axiom/reports/fresh_physics_seat_2026-09-01/recompute/'
          'R03_hypercharge_anomaly/controls_output.json', 'w') as f:
    json.dump(out, f, indent=1, default=str)
for k, v in out.items():
    print(k, '=', json.dumps(v, default=str)[:400])
