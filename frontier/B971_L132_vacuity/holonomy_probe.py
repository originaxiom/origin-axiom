"""
B971 / L132 (amended) -- the OBJECT-SIDE probe.

The vacuity probe settles what happens on a complete 27.  This probe settles
the prior question: what does the OBJECT's own holonomy see of the 27, and is
there any unbroken gauge group for an anomaly condition to be written against?

Two computations, both exact, both from the Cartan matrix only:

  P1  The 27 under the principal sl(2) of e6 -- the object's 27-local-system is
      rho = principal o rho_geo (B575/B632), so the holonomy acts through the
      principal sl(2).  If the decomposition EXHAUSTS the 27, no state is
      projected out and the multiplet the object carries is COMPLETE.

  P2  dim of the centralizer of the principal sl(2) in e6.  In the
      cohomological ("heterotic-style") reading, matter = H^1(M; 27_rho) and
      the unbroken gauge group is the commutant of the holonomy's Zariski
      closure.  If that commutant is 0-dimensional there is no gauge group,
      hence no gauge-anomaly conditions to write at all.
"""

import json
import sympy as sp


def cartan_matrix(n, edges):
    A = sp.zeros(n, n)
    for i in range(n):
        A[i, i] = 2
    for (i, j) in edges:
        A[i - 1, j - 1] = -1
        A[j - 1, i - 1] = -1
    return A


E6 = cartan_matrix(6, [(1, 3), (3, 4), (4, 5), (5, 6), (2, 4)])


def weyl_orbit(A, hw):
    n = A.shape[0]
    seen = {tuple(hw)}
    fr = [tuple(hw)]
    while fr:
        nxt = []
        for lam in fr:
            for i in range(n):
                mu = tuple(lam[j] - lam[i] * A[i, j] for j in range(n))
                if mu not in seen:
                    seen.add(mu)
                    nxt.append(mu)
        fr = nxt
    return sorted(seen, reverse=True)


R = {}

# principal sl(2): h_pr = sum c_i alpha_i^vee with alpha_j(h_pr) = 2 for all j
c = E6.solve(sp.Matrix([2] * 6))
R['principal_h_coeffs'] = [str(x) for x in c]
R['principal_h_is_integral'] = all(x == int(x) for x in c)


def eig(lam):
    return sum(c[i] * lam[i] for i in range(6))


def peel_strings(evs):
    """Peel an sl(2) weight multiset into irreducible strings.  Returns the
    list of highest weights (2*spin) and the string dimensions."""
    from collections import Counter
    m = Counter(evs)
    tops = []
    while sum(m.values()) > 0:
        top = max(k for k in m if m[k] > 0)
        for v in range(top, -top - 1, -2):
            assert m[v] > 0, (top, v, dict(m))
            m[v] -= 1
        tops.append(int(top))
    return sorted(tops, reverse=True)


# ---- P1: the 27 ----
w27 = weyl_orbit(E6, (1, 0, 0, 0, 0, 0))
R['dim_27'] = len(w27)
ev27 = [eig(l) for l in w27]
tops27 = peel_strings(ev27)
R['27_principal_highest_weights'] = tops27
R['27_principal_spins'] = [sp.Rational(t, 2) for t in tops27]
R['27_principal_block_dims'] = [t + 1 for t in tops27]
R['27_block_dims_sum'] = sum(t + 1 for t in tops27)
R['27_decomposition_EXHAUSTS_the_27'] = (sum(t + 1 for t in tops27) == 27)
R['27_no_state_projected_out'] = (sum(t + 1 for t in tops27) == len(w27))

# ---- P2: the adjoint 78, and the centralizer of the principal sl(2) ----
w78_roots = weyl_orbit(E6, (0, 1, 0, 0, 0, 0))          # 72 roots
R['n_roots'] = len(w78_roots)
ev78 = [eig(l) for l in w78_roots] + [0] * 6            # + rank zero-weights
R['dim_78'] = len(ev78)
tops78 = peel_strings(ev78)
R['78_principal_highest_weights'] = tops78
R['78_exponents'] = [sp.Rational(t, 2) for t in tops78]
R['78_block_dims_sum'] = sum(t + 1 for t in tops78)

# centralizer of the principal sl(2) in e6 = multiplicity of the TRIVIAL
# sl(2) module V(0) in the adjoint = number of zero highest weights
R['dim_centralizer_of_principal_sl2_in_e6'] = sum(1 for t in tops78 if t == 0)
R['no_continuous_commutant_of_the_holonomy'] = (
    sum(1 for t in tops78 if t == 0) == 0)

# sanity: exponents of E6 are 1,4,5,7,8,11 -- DERIVED here, not looked up
R['exponents_derived'] = [int(t // 2) for t in tops78]

print(json.dumps(R, indent=2, default=str))
with open('/Users/dri/origin-axiom/frontier/B971_L132_vacuity/holonomy_probe_out.json', 'w') as f:
    json.dump(R, f, indent=2, default=str)
