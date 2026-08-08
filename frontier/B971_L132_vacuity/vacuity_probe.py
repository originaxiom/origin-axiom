"""
B971 / L132 (amended) -- the NON-VACUITY probe.

Computes, in-sandbox, the discriminating fact behind the MB12 question:

  Q1  On a COMPLETE 27 of E6, can the anomaly functional ever be nonzero?
  Q2  Is the anomaly functional a real instrument at all (can it FAIL on
      something)?   [MB12 requires: can pass AND can fail]
  Q3  On an INCOMPLETE 27 -- a proper sub-multiplet of the object's own
      landing site, the A2+A1 Levi -- does it become nonzero?

Nothing is cited.  Weights are generated as the Weyl orbit of the highest
weight from the Cartan matrix; anomaly polynomials are expanded symbolically
over a GENERIC Cartan element, so a single polynomial identity carries every
cubic / mixed / gravitational condition at once.

Key reduction used (derived, see FINDINGS 2.1): for H in the Cartan,
  A_cubic(H) = sum_weights lambda(H)^3 ,  A_grav(H) = sum_weights lambda(H).
Every U(1)^3, [SU(3)]^2 U(1), [SU(2)]^2 U(1) and U(1)-gravitational condition
is a COEFFICIENT of these two polynomials in the generic Cartan coordinates,
because all the generators involved can be conjugated into the Cartan.
"""

import itertools
import json
import sympy as sp

# ----------------------------------------------------------------- algebras


def cartan_matrix(n, edges):
    A = [[0] * n for _ in range(n)]
    for i in range(n):
        A[i][i] = 2
    for (i, j) in edges:
        A[i - 1][j - 1] = -1
        A[j - 1][i - 1] = -1
    return A


# Bourbaki E6: 1-3, 3-4, 4-5, 5-6 chain, node 2 hung off node 4
E6 = cartan_matrix(6, [(1, 3), (3, 4), (4, 5), (5, 6), (2, 4)])
A4 = cartan_matrix(4, [(1, 2), (2, 3), (3, 4)])   # su(5), the control
A2 = cartan_matrix(2, [(1, 2)])                   # su(3), the control


def weyl_orbit(A, hw):
    """Orbit of hw (Dynkin labels) under the Weyl group. Exact for minuscule
    weights, where the weight set IS a single orbit, all multiplicities 1."""
    n = len(A)
    seen = {tuple(hw)}
    frontier = [tuple(hw)]
    while frontier:
        nxt = []
        for lam in frontier:
            for i in range(n):
                mu = tuple(lam[j] - lam[i] * A[i][j] for j in range(n))
                if mu not in seen:
                    seen.add(mu)
                    nxt.append(mu)
        frontier = nxt
    return sorted(seen, reverse=True)


def anomaly_polys(weights, hvars):
    """(gravitational/linear, cubic) anomaly polynomials over a generic Cartan
    element H = sum h_i alpha_i^vee.  lambda(H) = sum_i h_i * (Dynkin label)_i."""
    lin = sp.expand(sum(sum(h * c for h, c in zip(hvars, lam)) for lam in weights))
    cub = sp.expand(sum(sum(h * c for h, c in zip(hvars, lam)) ** 3 for lam in weights))
    return sp.simplify(lin), sp.expand(cub)


R = {}

# ---------------------------------------------------------------- Q1 / Q2
h6 = sp.symbols('h1:7')
w27 = weyl_orbit(E6, (1, 0, 0, 0, 0, 0))          # 27 = minuscule, hw = omega_1
w78_check = None
R['dim_27'] = len(w27)

lin27, cub27 = anomaly_polys(w27, h6)
R['E6_27_linear_is_zero'] = (lin27 == 0)
R['E6_27_cubic_is_zero'] = (sp.expand(cub27) == 0)
R['E6_27_cubic_nterms'] = len(sp.Poly(cub27, *h6).terms()) if cub27 != 0 else 0

# the conjugate 27-bar, for completeness
w27b = weyl_orbit(E6, (0, 0, 0, 0, 0, 1))
lin27b, cub27b = anomaly_polys(w27b, h6)
R['dim_27bar'] = len(w27b)
R['E6_27bar_cubic_is_zero'] = (sp.expand(cub27b) == 0)
R['27_and_27bar_are_different_weight_sets'] = (set(w27) != set(w27b))

# CONTROL (MB12 "can it fail?"): su(5) 10 and su(3) 3 are anomalous.
h4 = sp.symbols('k1:5')
w10 = weyl_orbit(A4, (0, 1, 0, 0))
lin10, cub10 = anomaly_polys(w10, h4)
R['dim_su5_10'] = len(w10)
R['CONTROL_su5_10_cubic_is_zero'] = (sp.expand(cub10) == 0)

h2 = sp.symbols('m1:3')
w3 = weyl_orbit(A2, (1, 0))
lin3, cub3 = anomaly_polys(w3, h2)
R['dim_su3_3'] = len(w3)
R['CONTROL_su3_3_cubic_is_zero'] = (sp.expand(cub3) == 0)

# ---------------------------------------------------------------- Q3
# The object's own landing site: the A2+A1 Levi of e6 (B892/B951), node set S.
S = [1, 3, 6]          # {1,3} adjacent -> A2 (colour);  {6} isolated -> A1
notS = [i for i in range(1, 7) if i not in S]
R['levi_nodes_S'] = S
R['levi_dim'] = 6 + 8            # rank + #roots(A2)+#roots(A1) = 6 + (6+2)
R['levi_centre_dim'] = 6 - len(S)

# Centre of the Levi: H = sum h_i alpha_i^vee with alpha_j(H) = 0 for j in S,
# i.e. sum_i A[j][i] h_i = 0 for each j in S.  Solve exactly.
M = sp.Matrix([[E6[j - 1][i - 1] for i in range(1, 7)] for j in S])
ns = M.nullspace()                     # exact kernel over Q
free = sp.symbols('t1:%d' % (len(ns) + 1))
Hc = sp.zeros(6, 1)
for t, v in zip(free, ns):
    Hc += t * v
Hcentre = [sp.simplify(Hc[i]) for i in range(6)]
R['levi_centre_free_params'] = [str(s) for s in free]
R['levi_centre_solution'] = [str(e) for e in Hcentre]
R['levi_centre_check_alpha_j_vanishes'] = all(
    sp.simplify(sum(E6[j - 1][i - 1] * Hcentre[i - 1] for i in range(1, 7))) == 0 for j in S)
assert len(free) == 3, free            # rank 6 - |S| = 3 abelian directions

# W_S orbits on the 27 = the Levi irreps (exact: 27 is minuscule, mult 1)
def ws_orbits(A, weights, S):
    ws = set(map(tuple, weights))
    unseen = set(ws)
    orbits = []
    while unseen:
        start = max(unseen)
        orb, frontier = {start}, [start]
        while frontier:
            nxt = []
            for lam in frontier:
                for i in S:
                    mu = tuple(lam[j] - lam[i - 1] * A[i - 1][j] for j in range(len(A)))
                    if mu in ws and mu not in orb:
                        orb.add(mu)
                        nxt.append(mu)
            frontier = nxt
        orbits.append(sorted(orb, reverse=True))
        unseen -= orb
    return sorted(orbits, key=lambda o: (-len(o), o))


orbits = ws_orbits(E6, w27, S)
R['levi_orbit_sizes'] = [len(o) for o in orbits]
R['levi_orbit_count'] = len(orbits)

def y_of(lam):
    return sp.expand(sum(Hcentre[i] * lam[i] for i in range(6)))

# u(1) charge must be CONSTANT on each Levi irrep -- verify, do not assume
const_ok = []
orbit_y = []
for o in orbits:
    ys = {sp.simplify(y_of(l)) for l in o}
    const_ok.append(len(ys) == 1)
    orbit_y.append(sp.simplify(y_of(o[0])))
R['u1_constant_on_every_levi_irrep'] = all(const_ok)
R['levi_orbit_charges'] = [str(y) for y in orbit_y]

# su(2) content per orbit (node 6): doublet iff the orbit contains labels +-1 at node 6
def su2_dim(o):
    labs = {l[5] for l in o}
    return 2 if 1 in labs and -1 in labs else 1

def su3_dim(o):
    # A2 at nodes {1,3}: orbit size in the A2 directions
    seen, fr = {o[0]}, [o[0]]
    oset = set(o)
    while fr:
        nxt = []
        for lam in fr:
            for i in (1, 3):
                mu = tuple(lam[j] - lam[i - 1] * E6[i - 1][j] for j in range(6))
                if mu in oset and mu not in seen:
                    seen.add(mu); nxt.append(mu)
        fr = nxt
    return len(seen)

R['levi_orbit_su3_su2_dims'] = [[su3_dim(o), su2_dim(o)] for o in orbits]

# Witten SU(2) parity: number of doublets in the 27
n_doublets = sum(1 for l in w27 if l[5] == 1)
R['witten_su2_doublets_in_27'] = n_doublets
R['witten_parity_even'] = (n_doublets % 2 == 0)

# ---- the four anomaly families on the COMPLETE 27, over the Levi centre ----
def T(d):            # Dynkin index of the fundamental/singlet, normalised T(fund)=1/2
    return sp.Rational(1, 2) if d > 1 else 0

A_cubic = sp.expand(sum(len(o) * orbit_y[k] ** 3 for k, o in enumerate(orbits)))
A_grav = sp.expand(sum(len(o) * orbit_y[k] for k, o in enumerate(orbits)))
A_33Y = sp.expand(sum(T(su3_dim(o)) * su2_dim(o) * orbit_y[k] for k, o in enumerate(orbits)))
A_22Y = sp.expand(sum(T(su2_dim(o)) * su3_dim(o) * orbit_y[k] for k, o in enumerate(orbits)))

R['complete27_A_U1cubed'] = str(A_cubic)
R['complete27_A_grav'] = str(A_grav)
R['complete27_A_SU3sq_U1'] = str(A_33Y)
R['complete27_A_SU2sq_U1'] = str(A_22Y)
R['complete27_all_four_vanish'] = all(sp.expand(x) == 0 for x in (A_cubic, A_grav, A_33Y, A_22Y))

# ---- INCOMPLETE: drop one Levi irrep at a time ----
drops = []
for k, o in enumerate(orbits):
    keep = [j for j in range(len(orbits)) if j != k]
    c = sp.expand(sum(len(orbits[j]) * orbit_y[j] ** 3 for j in keep))
    g = sp.expand(sum(len(orbits[j]) * orbit_y[j] for j in keep))
    m3 = sp.expand(sum(T(su3_dim(orbits[j])) * su2_dim(orbits[j]) * orbit_y[j] for j in keep))
    m2 = sp.expand(sum(T(su2_dim(orbits[j])) * su3_dim(orbits[j]) * orbit_y[j] for j in keep))
    drops.append({
        'dropped_orbit_size': len(o),
        'dropped_su3_su2': [su3_dim(o), su2_dim(o)],
        'dropped_charge': str(orbit_y[k]),
        'A_U1cubed_nonzero': sp.expand(c) != 0,
        'A_grav_nonzero': sp.expand(g) != 0,
        'A_SU3sq_U1_nonzero': sp.expand(m3) != 0,
        'A_SU2sq_U1_nonzero': sp.expand(m2) != 0,
    })
R['incomplete_drop_one_levi_irrep'] = drops
R['incomplete_ANY_condition_fails'] = any(
    d['A_U1cubed_nonzero'] or d['A_grav_nonzero'] or d['A_SU3sq_U1_nonzero']
    or d['A_SU2sq_U1_nonzero'] for d in drops)

# also: drop a SINGLE weight (the crudest incompleteness)
one_missing = sp.expand(cub27 - sum(h * c for h, c in zip(h6, w27[0])) ** 3)
R['drop_one_weight_cubic_nonzero'] = (sp.expand(one_missing) != 0)

# ---- vector-like control: 27 + 27bar (any incompleteness, still zero?) ----
pairs = [(l, tuple(-x for x in l)) for l in w27[:5]]
vl = sp.expand(sum(sum(h * c for h, c in zip(h6, a)) ** 3
                   + sum(h * c for h, c in zip(h6, b)) ** 3 for a, b in pairs))
R['vectorlike_subset_cubic_is_zero'] = (sp.expand(vl) == 0)

print(json.dumps(R, indent=2, default=str))
with open('/Users/dri/origin-axiom/frontier/B971_L132_vacuity/vacuity_probe_out.json', 'w') as f:
    json.dump(R, f, indent=2, default=str)
