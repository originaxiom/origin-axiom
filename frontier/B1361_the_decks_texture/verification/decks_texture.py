#!/usr/bin/env python3
"""B1361 -- THE DECK'S TEXTURE IS B1273'S.

(1) The selection rule.  B1356: under the two C-field U(1)s born with the apexes (w and its deck image), the three 27s carry the
    charge vectors (1,-2), (1,1), (-2,1) (the deck orbit of the coset representative (1,1,-2), read on the pair).  The E6 cubic
    27_i 27_j 27_k (B1276: one coupling) is U(1)^2-invariant iff the three charge vectors sum to zero.  We enumerate the symmetric
    couplings lambda_{ijk} (i <= j <= k) that survive, for the Higgs sitting in the apex 27s (charges as above) and for a neutral
    Higgs (charge 0), and also list the Z_3-invariant cubics when only the deck is imposed.
(2) The identity.  A hollow (zero-diagonal) complex symmetric 3x3 matrix M = [[0,c,b],[c,0,a],[b,a,0]] has singular values with
    sigma_1 = sigma_2 + sigma_3 exactly.  Proof: with s_i = sigma_i^2 the eigenvalues of M M^dagger, the condition
    (s_1+...)(...) = 0 for sigma_1 = sigma_2 + sigma_3 is e_1^2 - 4 e_2 = 0 where e_1 = tr(M M^dagger) = 2 S, S = |a|^2+|b|^2+|c|^2,
    and e_2 = the sum of the principal 2x2 minors of M M^dagger; we show e_2 = S^2 symbolically.  Then the real-symmetric ordering
    argument (traceless eigenvalues) picks the branch sigma_1 = sigma_2 + sigma_3 (numerically confirmed on random samples, min
    sigma_2/sigma_1 = 1/2).
(3) The data.  m_heaviest = m_middle + m_lightest against the charged-fermion masses.
"""
import itertools, sympy as sp, numpy as np

print("=" * 96)
print("(1) the selection rule on the E6 cubic 27_i 27_j 27_k under the apex-born U(1)^2")
print("=" * 96)
charges = {1: (1, -2), 2: (1, 1), 3: (-2, 1)}
print(f"  charge vectors (B1356 sec. 2): {charges}; pairwise sums: "
      + ", ".join(f"q{i}+q{j}={tuple(charges[i][t]+charges[j][t] for t in range(2))}" for i, j in itertools.combinations(charges, 2)))
allowed = [(i, j, k) for i, j, k in itertools.combinations_with_replacement(charges, 3)
           if all(charges[i][t] + charges[j][t] + charges[k][t] == 0 for t in range(2))]
print(f"  symmetric couplings lambda_ijk invariant under both U(1)s: {allowed} (of 10)")
neutral = [(i, j) for i, j in itertools.combinations_with_replacement(charges, 2)
           if all(charges[i][t] + charges[j][t] == 0 for t in range(2))]
print(f"  with a neutral Higgs (27_i 27_j H, q_i + q_j = 0): {neutral} -> no tree-level Yukawa at all: {neutral == []}")
# Z_3 alone: invariant symmetric cubics = monomials fixed under the cyclic permutation, plus orbit sums
x = sp.symbols('x1 x2 x3')
monos = [x[i]*x[j]*x[k] for i, j, k in itertools.combinations_with_replacement(range(3), 3)]
cyc = {x[0]: x[1], x[1]: x[2], x[2]: x[0]}
orbits = []
seen = set()
for m in monos:
    if m in seen:
        continue
    orb = {m}; cur = m
    for _ in range(2):
        cur = cur.subs(cyc, simultaneous=True); orb.add(cur)
    seen |= orb; orbits.append(orb)
print(f"  Z_3 (the deck) alone: {len(orbits)} invariant cubic combinations: {[sum(o) for o in orbits]}")

print("\n" + "=" * 96)
print("(2) the identity sigma_1 = sigma_2 + sigma_3 for hollow complex symmetric 3x3 matrices")
print("=" * 96)
a, b, c = sp.symbols('a b c')
ab, bb, cb = sp.symbols('abar bbar cbar')
M = sp.Matrix([[0, c, b], [c, 0, a], [b, a, 0]])
Mdag = sp.Matrix([[0, cb, bb], [cb, 0, ab], [bb, ab, 0]])      # conjugate transpose (M symmetric)
H = M * Mdag
S = a*ab + b*bb + c*cb
e1 = sp.expand(H.trace())
e2 = sp.expand(sum(H[list(r), list(r)].det() for r in itertools.combinations(range(3), 2)))
print(f"  tr(M M^dagger) = {sp.factor(e1)}  (= 2 S: {sp.simplify(e1 - 2*S) == 0})")
print(f"  e_2(M M^dagger) - S^2 = {sp.simplify(e2 - S**2)}  -> e_1^2 - 4 e_2 = {sp.simplify(e1**2 - 4*e2)}")
print("  hence (s1+s2+s3)... the quartic (sigma1-sigma2-sigma3)(sigma1-sigma2+sigma3)(sigma1+sigma2-sigma3)(sigma1+sigma2+sigma3) = e1^2 - 4e2 = 0:")
print("  one of sigma_1 = sigma_2 + sigma_3, sigma_2 = sigma_1 + sigma_3, sigma_3 = sigma_1 + sigma_2 holds; with sigma_1 >= sigma_2 >= sigma_3 >= 0")
print("  the second forces sigma_3 = 0 and sigma_1 = sigma_2 (then the first holds too) and the third forces M = 0: so sigma_1 = sigma_2 + sigma_3 always.")
rng = np.random.default_rng(7)
worst = 0.0; minratio = 1.0
for _ in range(100000):
    v = (rng.standard_normal(3) + 1j*rng.standard_normal(3)) * np.exp(rng.uniform(-5, 5, 3))
    s = np.linalg.svd(np.array([[0, v[2], v[1]], [v[2], 0, v[0]], [v[1], v[0], 0]]), compute_uv=False)
    worst = max(worst, abs(s[0] - s[1] - s[2]) / s[0]); minratio = min(minratio, s[1]/s[0])
print(f"  numerical check on 1e5 random hollow symmetric complex matrices: max |sigma1 - sigma2 - sigma3|/sigma1 = {worst:.2e}; min sigma2/sigma1 = {minratio:.4f} (bound 1/2)")

print("\n" + "=" * 96)
print("(3) the relation m_heaviest = m_middle + m_lightest against the data (masses in GeV, low-scale running values, as B1273)")
print("=" * 96)
data = {"up": (1.3e-3, 0.63, 172.5), "down": (2.8e-3, 0.055, 2.86), "charged leptons": (0.000511, 0.1057, 1.777)}
for name, (m1, m2, m3) in data.items():
    print(f"  {name}: m_3/(m_2 + m_1) = {m3/(m2+m1):.1f}  (the hollow texture demands 1)")
print("  (B1273 refuted its texture by the same relation, factors 17-136 at its scale; the scale changes the factors, not the verdict.)")
print("\nDONE")
