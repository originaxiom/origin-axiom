"""
B971 / L132 (amended) -- THE NON-VACUITY MAP.

The vacuity probe shows the complete 27 cannot fail and that dropping a Levi
irrep makes it fail.  This probe maps the whole space between those two poles,
intrinsically -- WITHOUT choosing an SU(5) or SO(10) subgroup (the B951 trap).

Setup: the object's own landing site, the A2+A1 Levi of e6 (B892/B951), whose
centre is 3-dimensional.  The 27 splits into 11 Levi irreps.  For EVERY subset
of those 11 we ask:

  (i)   is the SU(3)^3 anomaly zero?            [Q-independent]
  (ii)  is the Witten SU(2) parity even?        [Q-independent]
  (iii) does there exist a NONZERO abelian direction Q in the 3-dim centre
        killing grav, [SU(3)]^2 Q, [SU(2)]^2 Q and Q^3 ?

(iii) is the honest intrinsic form of "does hypercharge fall out": no branching
table is read, no SU(5) is chosen.  A subset is COUNTED only if a nonzero
anomaly-free direction exists; the dimension of the solution space is recorded,
because a 3-dim solution space means the check is VACUOUS on that subset
(every direction works) while a 1-dim one means it SELECTS a direction.
"""

import itertools
import json
import sympy as sp
import pathlib as _pl
_REPO = _pl.Path(__file__).resolve().parents[2]


def cartan_matrix(n, edges):
    A = [[0] * n for _ in range(n)]
    for i in range(n):
        A[i][i] = 2
    for (i, j) in edges:
        A[i - 1][j - 1] = -1
        A[j - 1][i - 1] = -1
    return A


E6 = cartan_matrix(6, [(1, 3), (3, 4), (4, 5), (5, 6), (2, 4)])
S = [1, 3, 6]                       # A2 = {1,3} (colour), A1 = {6} (isospin)


def weyl_orbit(A, hw, nodes=None):
    n = len(A)
    nodes = nodes or list(range(1, n + 1))
    seen, fr = {tuple(hw)}, [tuple(hw)]
    while fr:
        nxt = []
        for lam in fr:
            for i in nodes:
                mu = tuple(lam[j] - lam[i - 1] * A[i - 1][j] for j in range(n))
                if mu not in seen:
                    seen.add(mu)
                    nxt.append(mu)
        fr = nxt
    return sorted(seen, reverse=True)


w27 = weyl_orbit(E6, (1, 0, 0, 0, 0, 0))
assert len(w27) == 27

# Levi irreps = W_S orbits (exact: 27 minuscule, all multiplicities 1)
ws = set(w27)
unseen, orbits = set(ws), []
while unseen:
    start = max(unseen)
    orb, fr = {start}, [start]
    while fr:
        nxt = []
        for lam in fr:
            for i in S:
                mu = tuple(lam[j] - lam[i - 1] * E6[i - 1][j] for j in range(6))
                if mu in ws and mu not in orb:
                    orb.add(mu); nxt.append(mu)
        fr = nxt
    orbits.append(sorted(orb, reverse=True))
    unseen -= orb
orbits.sort(key=lambda o: (-len(o), o))

# abelian centre of the Levi (exact kernel)
M = sp.Matrix([[E6[j - 1][i - 1] for i in range(1, 7)] for j in S])
ns = M.nullspace()
t = sp.symbols('t1:4')
Hc = sp.zeros(6, 1)
for s_, v in zip(t, ns):
    Hc += s_ * v
Hc = [sp.simplify(Hc[i]) for i in range(6)]


def y_of(lam):
    return sp.expand(sum(Hc[i] * lam[i] for i in range(6)))


def su3_type(o):
    """A2 highest weight of the orbit -> '3', '3bar' or '1'."""
    hi = [l for l in o if l[0] >= 0 and l[2] >= 0]
    # restrict to the A2 sub-orbit through a representative
    reps = []
    for l in o:
        sub = weyl_orbit(E6, l, nodes=[1, 3])
        sub = [x for x in sub if x in ws]
        reps.append(tuple(sorted(sub, reverse=True)))
    sub = reps[0]
    hw = [x for x in sub if x[0] >= 0 and x[2] >= 0][0]
    lab = (hw[0], hw[2])
    return {(1, 0): '3', (0, 1): '3bar', (0, 0): '1'}[lab]


def su2_dim(o):
    labs = {l[5] for l in o}
    return 2 if (1 in labs and -1 in labs) else 1


A3 = {'3': 1, '3bar': -1, '1': 0}          # SU(3)^3 anomaly coefficient
T3 = {'3': sp.Rational(1, 2), '3bar': sp.Rational(1, 2), '1': 0}

irreps = []
for o in orbits:
    ys = {sp.simplify(y_of(l)) for l in o}
    assert len(ys) == 1
    irreps.append({
        'size': len(o),
        'su3': su3_type(o),
        'su2': su2_dim(o),
        'y': sp.simplify(y_of(o[0])),
    })

R = {}
R['levi_irreps'] = [{'size': d['size'], 'su3': d['su3'], 'su2': d['su2'],
                     'y': str(d['y'])} for d in irreps]
R['n_irreps'] = len(irreps)
R['dims_sum'] = sum(d['size'] for d in irreps)


def conditions(sub):
    """sub = list of irrep dicts. Returns the Q-independent checks and the
    three linear forms + the cubic form in (t1,t2,t3)."""
    su3cubic = sum(A3[d['su3']] * d['su2'] for d in sub)
    doublets = sum(d['size'] // 2 for d in sub if d['su2'] == 2)
    grav = sp.expand(sum(d['size'] * d['y'] for d in sub))
    a33 = sp.expand(sum(T3[d['su3']] * d['su2'] * d['y'] for d in sub))
    a22 = sp.expand(sum(sp.Rational(1, 2) * (d['size'] // 2) * d['y']
                        for d in sub if d['su2'] == 2))
    cub = sp.expand(sum(d['size'] * d['y'] ** 3 for d in sub))
    return su3cubic, doublets, grav, a33, a22, cub


# ---------- the complete 27 ----------
c3, dbl, g, m3, m2, cb = conditions(irreps)
R['complete27_SU3cubed'] = int(c3)
R['complete27_doublets'] = dbl
R['complete27_witten_even'] = (dbl % 2 == 0)
R['complete27_grav'] = str(g)
R['complete27_SU3sq_U1'] = str(m3)
R['complete27_SU2sq_U1'] = str(m2)
R['complete27_U1cubed'] = str(cb)
R['complete27_solution_space_dim'] = 3 if (g == 0 and m3 == 0 and m2 == 0 and cb == 0) else None
R['complete27_VACUOUS_every_direction_works'] = (
    c3 == 0 and dbl % 2 == 0 and g == 0 and m3 == 0 and m2 == 0 and cb == 0)

# ---------- every subset ----------
n = len(irreps)
tally = {'total_nonempty': 0, 'pass_su3cubed': 0, 'pass_witten': 0,
         'admit_nonzero_Q': 0, 'sel_dim1': 0, 'sel_dim2': 0, 'sel_dim3': 0}
selective = []      # subsets where a UNIQUE (1-dim) anomaly-free direction exists
for r in range(1, n + 1):
    for combo in itertools.combinations(range(n), r):
        sub = [irreps[i] for i in combo]
        tally['total_nonempty'] += 1
        c3, dbl, g, m3, m2, cb = conditions(sub)
        if c3 != 0:
            continue
        tally['pass_su3cubed'] += 1
        if dbl % 2 != 0:
            continue
        tally['pass_witten'] += 1
        L = sp.Matrix([[sp.expand(f).coeff(x) for x in t] for f in (g, m3, m2)])
        ker = L.nullspace()
        if not ker:
            continue
        # impose the cubic on the kernel
        params = sp.symbols('u1:%d' % (len(ker) + 1))
        Q = sp.zeros(3, 1)
        for p, v in zip(params, ker):
            Q += p * v
        cub_on_ker = sp.expand(cb.subs({t[i]: Q[i] for i in range(3)}))
        if cub_on_ker == 0:
            d = len(ker)
        else:
            # solutions of a nonzero cubic form: a nonzero solution may still
            # exist on a proper subvariety -- record as 'cubic-constrained'
            sols = sp.solve(cub_on_ker, params, dict=True)
            nz = [s for s in sols if any(v != 0 for v in s.values())] or sols
            d = 'cubic-constrained' if nz else None
        if d is None:
            continue
        tally['admit_nonzero_Q'] += 1
        if d in (1, 2, 3):
            tally['sel_dim%d' % d] += 1
        if d == 1:
            selective.append({
                'irreps': [{'size': irreps[i]['size'], 'su3': irreps[i]['su3'],
                            'su2': irreps[i]['su2']} for i in combo],
                'n_states': sum(irreps[i]['size'] for i in combo),
                'Q_direction': [str(sp.simplify(x)) for x in ker[0]],
            })

R['subset_tally'] = tally
R['n_selective_dim1'] = len(selective)
R['selective_state_counts'] = sorted({s['n_states'] for s in selective})
R['selective_examples'] = selective[:12]

# is an SM-generation-shaped subset among the selective ones?
def shape(s):
    from collections import Counter
    return Counter((d['su3'], d['su2']) for d in s['irreps'])

gen_shape = None
for s in selective:
    sh = shape(s)
    if s['n_states'] == 15 and sh.get(('3', 2), 0) + sh.get(('3bar', 2), 0) == 1:
        gen_shape = s
        break
R['a_15_state_selective_subset'] = gen_shape

print(json.dumps(R, indent=2, default=str))
with open(str(_REPO / "frontier/B971_L132_vacuity/nonvacuity_map_out.json"), 'w') as f:
    json.dump(R, f, indent=2, default=str)
