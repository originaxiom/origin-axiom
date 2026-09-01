#!/usr/bin/env python3
"""R03 blind recomputation: B1160 anomaly-forced hypercharge + B1170 arena census.

Written BEFORE opening the arcs' verification/ scripts or tests/ locks.
All arithmetic exact (sympy Rationals / polynomial factorization).

Conventions (mine, chosen independently):
  One SM generation as left-handed Weyl fields (everything conjugated to LH):
    Q   = (3, 2)  Y_q   -> 6 states
    u^c = (3b,1)  Y_u   -> 3 states
    d^c = (3b,1)  Y_d   -> 3 states
    L   = (1, 2)  Y_l   -> 2 states
    e^c = (1, 1)  Y_e   -> 1 state
  Anomaly conditions (overall normalizations irrelevant, only zeros matter):
    [SU(3)]^2 Y : 2 Yq + Yu + Yd = 0
    [SU(2)]^2 Y : 3 Yq + Yl = 0
    grav^2  Y   : 6 Yq + 3 Yu + 3 Yd + 2 Yl + Ye = 0
    [Y]^3       : 6 Yq^3 + 3 Yu^3 + 3 Yd^3 + 2 Yl^3 + Ye^3 = 0
"""
import itertools, json
import sympy as sp

out = {}

# ---------------------------------------------------------------- B1160 ----
Yq, Yu, Yd, Yl, Ye = sp.symbols('Yq Yu Yd Yl Ye')
lin = [2*Yq + Yu + Yd, 3*Yq + Yl, 6*Yq + 3*Yu + 3*Yd + 2*Yl + Ye]
cubic = 6*Yq**3 + 3*Yu**3 + 3*Yd**3 + 2*Yl**3 + Ye**3

s = sp.solve(lin, [Yd, Yl, Ye], dict=True)[0]
out['linear_line'] = {str(k): str(sp.simplify(v)) for k, v in s.items()}
assert sp.simplify(s[Yl] + 3*Yq) == 0          # Yl = -3 Yq
assert sp.simplify(s[Ye] - 6*Yq) == 0          # Ye =  6 Yq
assert sp.simplify(s[Yd] + 2*Yq + Yu) == 0     # Yu + Yd = -2 Yq

C = sp.expand(cubic.subs(s))                   # homogeneous in (Yq, Yu)
out['cubic_on_line_factored'] = str(sp.factor(C))
out['cubic_full_factor_is_-18*Yq*(Yu+4Yq)*(Yu-2Yq)'] = bool(
    sp.simplify(C - (-18*Yq*(Yu + 4*Yq)*(Yu - 2*Yq))) == 0)

t = sp.symbols('t')
Ct = sp.expand(C.subs({Yq: 1, Yu: -1 + t}))
out['cubic_at_Yq1_Yu=-1+t'] = str(sp.factor(Ct))
out['matches_banked_-18(t-3)(t+3)'] = bool(sp.simplify(Ct - (-18*(t-3)*(t+3))) == 0)

roots = sp.solve(Ct, t)
out['t_roots'] = [str(r) for r in roots]
tuples = []
for r in sorted(roots, key=lambda x: -x):
    vals = {Yq: 1, Yu: -1 + r}
    tup = (sp.Integer(1), vals[Yu], s[Yd].subs(vals), s[Yl].subs(vals), s[Ye].subs(vals))
    tuples.append([str(x) for x in tup])
out['solutions_(Yq,Yu,Yd,Yl,Ye)'] = tuples
out['SM_times_6'] = [str(6*x) for x in
                     (sp.Rational(1,6), sp.Rational(-2,3), sp.Rational(1,3),
                      sp.Rational(-1,2), sp.Integer(1))]

# --- Yq = 0 branch ---
sol0 = sp.solve([e.subs(Yq, 0) for e in lin], [Yd, Yl, Ye], dict=True)[0]
c0 = sp.expand(cubic.subs(Yq, 0).subs(sol0))
out['Yq0_branch'] = {
    'linear_solution_at_Yq0': {str(k): str(v) for k, v in sol0.items()},
    'cubic_identically_zero_on_branch': bool(c0 == 0),
    'family': '(0, s, -s, 0, 0) for all s',
    'charge_multiset': '{+s x3, -s x3, 0 x9}: symmetric under Y -> -Y '
                       '(U(1) acts vector-like on the multiset of charges)',
    'doublets_all_neutral': True,
    'invariant_mass_bilinear': 'e^c e^c: (1,1,Y=0)^2 is gauge invariant -> not fully chiral',
}

# ---------------------------------------------------------------- B1170 ----
ALPHA = {
    'A(3,2)':  ('3', 2),
    'B(3b,2)': ('3b', 2),
    'C(3,1)':  ('3', 1),
    'D(3b,1)': ('3b', 1),
    'E(1,2)':  ('1', 2),
    'F(1,1)':  ('1', 1),
}
NAMES = list(ALPHA)
CONJ3 = {'3': '3b', '3b': '3', '1': '1'}

contents = list(itertools.combinations_with_replacement(NAMES, 5))
out['census_total'] = len(contents)             # expect 252

color_safe = [c for c in contents
              if sum({'3': 1, '3b': -1, '1': 0}[ALPHA[n][0]] * ALPHA[n][1]
                     for n in c) == 0]
out['killed_by_SU3_cubed'] = len(contents) - len(color_safe)   # expect 222
out['color_safe'] = len(color_safe)


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
        if li == '1' and di == 1 and yi == 0:
            return True                       # real singlet: Majorana mass
        for j in range(i+1, n):
            lj, dj, yj = states[j]
            if dj == di and yj == -yi and lj == CONJ3[li]:
                return True                   # Dirac pair (2bar ~ 2 via epsilon)
    return False

def anomaly_polys(content, ys):
    e_su3 = sp.Integer(0); e_su2 = sp.Integer(0)
    e_grav = sp.Integer(0); e_cub = sp.Integer(0)
    for k, name in enumerate(content):
        lbl, su2d = ALPHA[name]
        colr = 3 if lbl != '1' else 1
        if lbl != '1':
            e_su3 += su2d * ys[k]
        if su2d == 2:
            e_su2 += colr * ys[k]
        e_grav += colr * su2d * ys[k]
        e_cub += colr * su2d * ys[k]**3
    return e_su3, e_su2, e_grav, e_cub

def rational_rays_2d(cub, a0, a1):
    """All rational projective roots of homogeneous cubic cub(a0,a1); also flag
    whether irrational/complex roots exist."""
    rays, irr = [], False
    u = sp.symbols('u')
    # roots with a1 != 0:
    q = sp.Poly(sp.expand(cub.subs({a0: u, a1: 1})), u)
    if q.degree() >= 1:
        rr = sp.roots(q, u)
        nrat = 0
        for r, m in rr.items():
            if r.is_rational:
                rays.append((r, sp.Integer(1))); nrat += m
        if nrat < q.degree():
            irr = True
    # ray a1 = 0:
    if sp.expand(cub.subs({a1: 0, a0: 1})) == 0:
        rays.append((sp.Integer(1), sp.Integer(0)))
    return rays, irr

def analyze(content):
    ys = sp.symbols('y0:5')
    e_su3, e_su2, e_grav, e_cub = anomaly_polys(content, ys)
    A, _ = sp.linear_eq_to_matrix([e_su3, e_su2, e_grav], ys)
    ns = A.nullspace()
    d = len(ns)
    res = {'content': list(content), 'null_dim': d, 'rays': [],
           'continuum': False, 'irrational_rays': False,
           'chiral_massless_point_in_continuum': None}
    if d == 0:
        return res
    params = sp.symbols('a0:%d' % d)
    yvec = [sp.expand(sum(params[m]*ns[m][k] for m in range(d))) for k in range(5)]
    cub = sp.expand(e_cub.subs({ys[k]: yvec[k] for k in range(5)},
                               simultaneous=True))
    cub = sp.expand(sum(params[m]**0 * 0 for m in range(d)) +
                    sp.expand(e_cub.subs(dict(zip(ys, yvec)))))
    if cub == 0:
        res['continuum'] = True
        res['continuum_dim'] = d
    elif d == 1:
        pass  # cubic = c*a0^3, c != 0: only trivial solution
    elif d == 2:
        rays, irr = rational_rays_2d(cub, params[0], params[1])
        res['irrational_rays'] = irr
        seen = []
        for (r0, r1) in rays:
            y = [sp.nsimplify(sp.expand(v.subs({params[0]: r0, params[1]: r1})))
                 for v in yvec]
            nz = [v for v in y if v != 0]
            if nz:
                g = nz[0]
                y = [sp.nsimplify(v/g) for v in y]
            key = tuple(y)
            if key in seen or tuple(-v for v in y) in seen:
                continue
            seen.append(key)
            st = states_of(content, y)
            res['rays'].append({
                'charges': [str(v) for v in y],
                'nonzero': bool(any(v != 0 for v in y)),
                'vector_like': is_vectorlike(st),
                'massable': massable(st),
            })
    else:
        # cubic hypersurface in a projective space of dim d-1 >= 2:
        # always positive-dimensional solution set over C; over Q search for
        # points to characterize (never rigid).
        res['continuum'] = True
        res['continuum_dim'] = 'cubic hypersurface in %d params' % d
    # for continuum cases, search a small rational box for a chiral massless point
    if res['continuum']:
        found = None
        rng = [sp.Rational(v) for v in range(-6, 7)]
        import itertools as it
        for pt in it.product(rng, repeat=d):
            if all(v == 0 for v in pt):
                continue
            y = [sp.expand(v.subs(dict(zip(params, pt)))) for v in yvec]
            if sp.expand(e_cub.subs(dict(zip(ys, y)))) != 0:
                continue
            st = states_of(content, y)
            if any(v != 0 for v in y) and not is_vectorlike(st) and not massable(st):
                found = [str(v) for v in y]
                break
        res['chiral_massless_point_in_continuum'] = found
    return res

reports = [analyze(c) for c in color_safe]
out['per_content'] = reports

# survivor criteria
strict = []          # isolated rational ray, nonzero, chiral (not VL), massless
loose = []           # any nonzero non-vector-like ray (isolated only)
continuum_chiral = []
for rec in reports:
    ok = [r for r in rec['rays']
          if r['nonzero'] and not r['vector_like'] and not r['massable']]
    if ok:
        strict.append((tuple(rec['content']), [r['charges'] for r in ok]))
    if [r for r in rec['rays'] if r['nonzero'] and not r['vector_like']]:
        loose.append(tuple(rec['content']))
    if rec['continuum'] and rec['chiral_massless_point_in_continuum']:
        continuum_chiral.append(tuple(rec['content']))

out['strict_survivors'] = [{'content': list(c), 'chiral_massless_rays': ch}
                           for c, ch in strict]
out['strict_survivor_count'] = len(strict)
out['loose_isolated_chiral_count'] = len(loose)
out['continuum_with_chiral_massless_point'] = [list(c) for c in continuum_chiral]

with open('/home/user/origin-axiom/reports/fresh_physics_seat_2026-09-01/recompute/'
          'R03_hypercharge_anomaly/blind_output.json', 'w') as f:
    json.dump(out, f, indent=1, default=str)

for k, v in out.items():
    if k != 'per_content':
        print(k, '=', json.dumps(v, default=str)[:400])
