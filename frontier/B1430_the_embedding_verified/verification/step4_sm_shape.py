"""Step 4: A2 + A1 + u(1) inside E6.

(a) closed subsystems of type A2 (+) A1  -- the regular su(3)+su(2)
(b) W-orbits, and orbits under the full automorphism group of the root
    system (W extended by the diagram automorphism)
(c) the 27 of E6, built as the W-orbit of the fundamental weight omega_1
(d) the u(1): the freedom left after fixing A2+A1, and a CONJUGACY
    INVARIANT (the branching of the 27) evaluated on many choices of Y
"""
from fractions import Fraction as F
from rootsys import *
from collections import Counter, defaultdict
from itertools import product
import json

simple = E6_simple()
roots = generate_roots(simple)
idx = {r: i for i, r in enumerate(roots)}
gens = simple_reflection_perms(roots, simple)
order, group = weyl_group_order(roots, simple)
Rset = set(roots)

print("=== STEP 4a: A2 (+) A1 CLOSED SUBSYSTEMS OF E6 ===")
A2 = a2_subsystems(roots)
A2A1 = a2_a1_subsystems(roots, A2)
print("A2 subsystems:", len(A2))
print("A2+A1 subsystems (8 roots: the A2's six plus +-c, c _|_ A2),")
print("  counted as SETS of 8 roots, closure under addition re-verified:")
print("  COUNT =", len(A2A1))

# per-A2 count of orthogonal A1's
per = Counter()
for fs in A2A1:
    for g in A2:
        if g <= fs:
            per[tuple(sorted(g))] += 1
print("orthogonal A1's per A2 (should be constant):", sorted(set(per.values())))

orbs = orbits_of_subsets(A2A1, gens)
print("W-orbits on A2+A1 subsystems:", len(orbs), "sizes:",
      sorted(len(o) for o in orbs))

# --- diagram automorphism -------------------------------------------------
# express every root in the simple-root basis, then permute the basis
A = cartan_matrix(simple)          # = Gram matrix (simply laced, |a|^2 = 2)


def solve_exact(M, b):
    """Solve M x = b exactly (M square, invertible), Fractions."""
    n = len(M)
    Mx = [list(map(F, M[i])) + [F(b[i])] for i in range(n)]
    for c in range(n):
        piv = next(i for i in range(c, n) if Mx[i][c] != 0)
        Mx[c], Mx[piv] = Mx[piv], Mx[c]
        pv = Mx[c][c]
        Mx[c] = [x / pv for x in Mx[c]]
        for i in range(n):
            if i != c and Mx[i][c] != 0:
                f = Mx[i][c]
                Mx[i] = [x - f * y for x, y in zip(Mx[i], Mx[c])]
    return [Mx[i][n] for i in range(n)]


def to_simple_coords(v):
    """coordinates of v in the simple-root basis (v must lie in the span)."""
    b = [ip(v, simple[j]) for j in range(6)]
    return solve_exact(A, b)          # since (sum c_k a_k, a_j) = sum c_k A_kj


def from_simple_coords(c):
    out = [F(0)] * len(simple[0])
    for ck, a in zip(c, simple):
        out = [x + ck * y for x, y in zip(out, a)]
    return tuple(out)


# my node labelling: edges (0,2),(1,3),(2,3),(3,4),(4,5)
# chain 0-2-3-4-5, node 1 hangs off node 3 -> automorphism 0<->5, 2<->4
sigma = {0: 5, 5: 0, 2: 4, 4: 2, 1: 1, 3: 3}
for (i, j, _) in dynkin_edges(simple):
    assert (sigma[i], sigma[j]) in [(x, y) for (x, y, _) in dynkin_edges(simple)] \
        or (sigma[j], sigma[i]) in [(x, y) for (x, y, _) in dynkin_edges(simple)]
print("diagram automorphism sigma =", sigma, "(checked: preserves the edges)")


def apply_sigma(v):
    c = to_simple_coords(v)
    d = [F(0)] * 6
    for k in range(6):
        d[sigma[k]] = c[k]
    return from_simple_coords(d)


sigma_perm = tuple(idx[apply_sigma(r)] for r in roots)
print("sigma permutes the 72 roots:", len(set(sigma_perm)) == 72)
print("sigma preserves inner products:",
      all(ip(roots[sigma_perm[i]], roots[sigma_perm[j]]) == ip(roots[i], roots[j])
          for i in range(72) for j in range(72)))
print("sigma is in W:", sigma_perm in group)
minus1 = tuple(idx[neg(r)] for r in roots)
print("-1 (r -> -r) is in W(E6):", minus1 in group)
print("-1 * sigma is in W(E6):", compose(minus1, sigma_perm) in group)

gens_aut = gens + [sigma_perm]
orbs_aut = orbits_of_subsets(A2A1, gens_aut)
print("Aut-orbits on A2+A1 subsystems:", len(orbs_aut), "sizes:",
      sorted(len(o) for o in orbs_aut))
orbs_aut_A2 = orbits_of_subsets(A2, gens_aut)
print("Aut-orbits on A2 subsystems:", len(orbs_aut_A2), "sizes:",
      sorted(len(o) for o in orbs_aut_A2))

# --- centraliser data for one A2+A1 --------------------------------------
rep = A2A1[0]
S = [roots[k] for k in rep]
print()
print("=== STEP 4b: WHAT IS LEFT FOR THE u(1) ===")
print("rank of the span of one A2+A1:", rank_of(S))
perp_roots = [r for r in roots if all(ip(r, s) == 0 for s in S)]
print("roots orthogonal to it:", len(perp_roots),
      "rank:", rank_of(perp_roots) if perp_roots else 0)
print("dim of the Cartan directions commuting with it: 6 -", rank_of(S),
      "=", 6 - rank_of(S))
stab = setwise_stabilizer_order(rep, group)
print("setwise stabiliser of this A2+A1 in W has order:", stab,
      "(orbit-stabiliser check:", order // stab, "==", len(orbs[0]), ")")

json.dump([sorted(x) for x in A2A1], open("e6_a2a1_subsystems.json", "w"))

# --- the 27 ---------------------------------------------------------------
print()
print("=== STEP 4c: THE 27 OF E6, BUILT FROM SCRATCH ===")
Ainv_cols = [solve_exact(A, [1 if k == i else 0 for k in range(6)])
             for i in range(6)]
omegas = [from_simple_coords(c) for c in Ainv_cols]
for i, w in enumerate(omegas):
    assert all(ip(w, simple[j]) == (1 if i == j else 0) for j in range(6))
print("fundamental weights constructed: (omega_i, alpha_j) = delta_ij  OK")


def weight_orbit(w):
    seen = {w}
    q = [w]
    while q:
        x = q.pop()
        for a in simple:
            y = refl(x, a)
            if y not in seen:
                seen.add(y)
                q.append(y)
    return sorted(seen)


sizes = [len(weight_orbit(w)) for w in omegas]
print("W-orbit sizes of the six fundamental weights:", sizes)
W27 = weight_orbit(omegas[0])
print("orbit of omega_1 has size", len(W27), "-> this is the minuscule 27")
assert len(W27) == 27
W27b = weight_orbit(omegas[5])
print("orbit of omega_6 has size", len(W27b), "(the conjugate 27-bar)")
