#!/usr/bin/env python3
"""B666 cell S' -- THE RIGIDITY STEP, verified exactly per banked group.

The lemma to be instantiated: Hom(G, R_+) = 0 for every finite group G,
because R_+ (the positive reals under multiplication) is torsion-free:
phi(g)^ord(g) = phi(g^ord(g)) = phi(1) = 1 forces phi(g) = 1.
Equivalently: any hom G -> R_+ factors through the abelianization G^ab
(R_+ abelian), and a FINITE abelian group has no nontrivial torsion-free
quotient, while every subgroup of R_+ except {1} is infinite torsion-free.

This script computes, EXACTLY (integer/modular arithmetic only, no floats
in any decisive step), for each banked symmetry structure:
  (1) the group, built from scratch (BFS over generators);
  (2) its order + a fingerprint (class equation where banked);
  (3) its derived subgroup [G,G] (normal-closure BFS) and G^ab = G/[G,G];
  (4) the exponent e of G^ab and the sympy-exact statement that the only
      positive real with x^e = 1 is x = 1  ==>  Hom(G, R_+) = 0.

Banked structures verified:
  A. Gal(L/Q(i)) = Klein four (B662 cellD, silver trace field descent)
  B. 2I = SL(2,5), the hearing image kernel-of-det (B640/B644)     [perfect]
  C. PSL(2,7) = GL(3,2), the kappa=14 stage shadow (B646, B666 cell3) [simple]
  D. 2I x Z/3, the full level-15 hearing image im(rho) (B640)
  E. SL(2,Z/15), the mod-conductor shadow group at conductor 15
     (B640: the factorization SL(2,Z/15) ~ SL(2,3) x SL(2,5))
  F. W(E6), |W| = 51840, the stage Weyl group (B570/B578 BFS pattern)

Output: cellS_output.txt (full transcript preserved).
"""
import sys
from fractions import Fraction
from itertools import product
from math import gcd

import sympy


def log(msg=""):
    print(msg, flush=True)


# ----------------------------------------------------------------------
# generic finite-group machinery over hashable elements
# ----------------------------------------------------------------------

class FiniteGroup:
    """A finite group given by generators + multiplication + inverse."""

    def __init__(self, gens, mul, inv, e):
        self.gens = list(gens)
        self.mul = mul
        self.inv = inv
        self.e = e
        self.elements = self._bfs(self.gens)

    def _bfs(self, seed):
        seen = {self.e}
        frontier = [self.e]
        while frontier:
            new = []
            for x in frontier:
                for g in seed:
                    for y in (self.mul(g, x), self.mul(self.inv(g), x)):
                        if y not in seen:
                            seen.add(y)
                            new.append(y)
            frontier = new
        return seen

    def subgroup_closure(self, seed):
        seen = {self.e}
        frontier = [self.e]
        seed = list(seed)
        while frontier:
            new = []
            for x in frontier:
                for g in seed:
                    for y in (self.mul(g, x), self.mul(self.inv(g), x)):
                        if y not in seen:
                            seen.add(y)
                            new.append(y)
            frontier = new
        return seen

    def commutator(self, a, b):
        return self.mul(self.mul(a, b), self.mul(self.inv(a), self.inv(b)))

    def derived_subgroup(self):
        """[G,G] = normal closure of {[g_i,g_j]}; iterate closure+normality."""
        seed = [self.commutator(a, b) for a in self.gens for b in self.gens]
        seed = [s for s in seed if s != self.e]
        while True:
            H = self.subgroup_closure(seed)
            extra = []
            for g in self.gens:
                gi = self.inv(g)
                for h in H:
                    c = self.mul(self.mul(g, h), gi)
                    if c not in H:
                        extra.append(c)
            if not extra:
                return H
            seed = seed + extra

    def element_order(self, a):
        n, x = 1, a
        while x != self.e:
            x = self.mul(x, a)
            n += 1
        return n

    def conjugacy_class_sizes(self):
        els = list(self.elements)
        remaining = set(els)
        sizes = []
        while remaining:
            a = next(iter(remaining))
            orbit = {self.mul(self.mul(g, a), self.inv(g)) for g in els}
            remaining -= orbit
            sizes.append(len(orbit))
        return sorted(sizes)

    def abelianization_order_and_exponent(self):
        """|G^ab| and exponent of G^ab (= lcm of coset orders in G/[G,G])."""
        H = self.derived_subgroup()
        n_ab = len(self.elements) // len(H)
        # exponent: lcm over generators g of min k>0 with g^k in H
        exp = 1
        for g in self.gens:
            x, k = g, 1
            while x not in H:
                x = self.mul(x, g)
                k += 1
            exp = exp * k // gcd(exp, k)
        return len(H), n_ab, exp


def rigidity_check(name, exp_ab):
    """sympy-exact: the only x in R_+ with x^e = 1 is x = 1  ==>  every
    hom G -> R_+ (which factors through G^ab, exponent e) is trivial."""
    x = sympy.symbols('x', positive=True)
    sols = sympy.solve(sympy.Eq(x**exp_ab, 1), x)
    assert sols == [1], (name, sols)
    log(f"  [{name}] exponent(G^ab) = {exp_ab}; positive-real solutions of "
        f"x^{exp_ab} = 1: {sols} == [1]  =>  Hom(G, R_+) = 0   OK")


# ----------------------------------------------------------------------
# A. Gal(L/Q(i)) = Klein four (B662 cellD)
# ----------------------------------------------------------------------

def check_klein_four():
    log("=" * 72)
    log("A. Gal(L/Q(i)) -- Klein four-group {1, sigma, tau, sigma*tau}")
    log("   (B662 cellD: sigma: s -> -s, tau: s -> 4i/s, both fixing i;")
    log("    sigma^2 = tau^2 = 1, sigma*tau = tau*sigma -- banked exact)")
    # realize as F_2^2: sigma = (1,0), tau = (0,1)
    mul = lambda a, b: ((a[0] + b[0]) % 2, (a[1] + b[1]) % 2)
    G = FiniteGroup([(1, 0), (0, 1)], mul, lambda a: a, (0, 0))
    assert len(G.elements) == 4
    orders = sorted(G.element_order(a) for a in G.elements)
    assert orders == [1, 2, 2, 2], orders
    dH, n_ab, exp = G.abelianization_order_and_exponent()
    log(f"  |G| = {len(G.elements)}, element orders {orders} "
        f"(noncyclic of order 4 => Klein four)")
    log(f"  |[G,G]| = {dH} (abelian), G^ab order {n_ab} = (Z/2)^2, "
        f"exponent {exp} -- pure 2-torsion")
    assert (dH, n_ab, exp) == (1, 4, 2)
    rigidity_check("Klein four", exp)


# ----------------------------------------------------------------------
# B/C. SL(2,p) and PSL(2,p) machinery
# ----------------------------------------------------------------------

def sl2_group(p):
    def mul(a, b):
        return ((a[0] * b[0] + a[1] * b[2]) % p, (a[0] * b[1] + a[1] * b[3]) % p,
                (a[2] * b[0] + a[3] * b[2]) % p, (a[2] * b[1] + a[3] * b[3]) % p)

    def inv(a):
        # det = 1: inverse = adjugate
        return (a[3] % p, (-a[1]) % p, (-a[2]) % p, a[0] % p)

    e = (1, 0, 0, 1)
    T = (1, 1, 0, 1)
    L = (1, 0, 1, 1)
    return FiniteGroup([T, L], mul, inv, e)


def psl2_group(p):
    def canon(a):
        b = tuple((-x) % p for x in a)
        return min(a, b)

    def mul(a, b):
        return canon(((a[0] * b[0] + a[1] * b[2]) % p,
                      (a[0] * b[1] + a[1] * b[3]) % p,
                      (a[2] * b[0] + a[3] * b[2]) % p,
                      (a[2] * b[1] + a[3] * b[3]) % p))

    def inv(a):
        return canon((a[3] % p, (-a[1]) % p, (-a[2]) % p, a[0] % p))

    e = (1, 0, 0, 1)
    T = canon((1, 1, 0, 1))
    L = canon((1, 0, 1, 1))
    return FiniteGroup([T, L], mul, inv, e)


def check_2i():
    log("=" * 72)
    log("B. 2I = SL(2,5) -- the hearing image ker(det), |2I| = 120")
    log("   (B640: class equation [1,1,12,12,12,12,20,20,30]; B644: the")
    log("    congruence-shadow theorem identifies it elementwise)")
    G = sl2_group(5)
    assert len(G.elements) == 120, len(G.elements)
    classes = G.conjugacy_class_sizes()
    log(f"  |G| = {len(G.elements)}; class equation {classes}")
    assert classes == [1, 1, 12, 12, 12, 12, 20, 20, 30], classes
    dH, n_ab, exp = G.abelianization_order_and_exponent()
    log(f"  |[G,G]| = {dH} = |G|  =>  PERFECT; G^ab order {n_ab} (trivial), "
        f"exponent {exp}")
    assert (dH, n_ab, exp) == (120, 1, 1)
    rigidity_check("2I = SL(2,5)", exp)


def check_psl27():
    log("=" * 72)
    log("C. PSL(2,7) = GL(3,2), |G| = 168 -- the kappa=14 stage shadow")
    log("   (B646: A1 mod 7 has order 8 in SL(2,7), order 4 in PSL(2,7);")
    log("    B666 cell3: the E6-stage shadow core)")
    G = psl2_group(7)
    assert len(G.elements) == 168, len(G.elements)
    classes = G.conjugacy_class_sizes()
    log(f"  |G| = {len(G.elements)}; class equation {classes}")
    assert classes == [1, 21, 24, 24, 42, 56], classes  # standard PSL(2,7)
    dH, n_ab, exp = G.abelianization_order_and_exponent()
    log(f"  |[G,G]| = {dH} = |G|  =>  PERFECT (simple); G^ab order {n_ab}, "
        f"exponent {exp}")
    assert (dH, n_ab, exp) == (168, 1, 1)
    rigidity_check("PSL(2,7)", exp)


# ----------------------------------------------------------------------
# D. 2I x Z/3 -- the full level-15 hearing image (B640)
# ----------------------------------------------------------------------

def check_hearing_image():
    log("=" * 72)
    log("D. 2I x Z/3 -- the full hearing image im(rho) at level 15 (B640)")
    S = sl2_group(5)
    Sels = S.elements

    def mul(a, b):
        return (S.mul(a[0], b[0]), (a[1] + b[1]) % 3)

    def inv(a):
        return (S.inv(a[0]), (-a[1]) % 3)

    e = (S.e, 0)
    gens = [(g, 0) for g in S.gens] + [(S.e, 1)]
    G = FiniteGroup(gens, mul, inv, e)
    assert len(G.elements) == 360, len(G.elements)
    dH, n_ab, exp = G.abelianization_order_and_exponent()
    log(f"  |G| = {len(G.elements)} = 120*3; |[G,G]| = {dH} (= 2I x 1), "
        f"G^ab order {n_ab} = Z/3, exponent {exp}")
    assert (dH, n_ab, exp) == (120, 3, 3)
    rigidity_check("2I x Z/3", exp)
    _ = Sels  # keep reference


# ----------------------------------------------------------------------
# E. SL(2,Z/15) -- the mod-conductor shadow group at conductor 15
# ----------------------------------------------------------------------

def check_sl2_z15():
    log("=" * 72)
    log("E. SL(2,Z/15) -- the mod-conductor shadow group, conductor 15")
    log("   (B640: the hearing factors through SL(2,Z/15) ~ SL(2,3) x SL(2,5))")
    n = 15

    def mul(a, b):
        return ((a[0] * b[0] + a[1] * b[2]) % n, (a[0] * b[1] + a[1] * b[3]) % n,
                (a[2] * b[0] + a[3] * b[2]) % n, (a[2] * b[1] + a[3] * b[3]) % n)

    def inv(a):
        return (a[3] % n, (-a[1]) % n, (-a[2]) % n, a[0] % n)

    G = FiniteGroup([(1, 1, 0, 1), (1, 0, 1, 1)], mul, inv, (1, 0, 0, 1))
    assert len(G.elements) == 24 * 120, len(G.elements)  # CRT: |SL(2,3)|*|SL(2,5)|
    dH, n_ab, exp = G.abelianization_order_and_exponent()
    log(f"  |G| = {len(G.elements)} = 24*120 (CRT); |[G,G]| = {dH}, "
        f"G^ab order {n_ab} = Z/3 (the SL(2,3)^ab factor; SL(2,5) perfect), "
        f"exponent {exp}")
    assert (dH, n_ab, exp) == (960, 3, 3)
    rigidity_check("SL(2,Z/15)", exp)


# ----------------------------------------------------------------------
# F. W(E6), |W| = 51840 (B570/B578 builder pattern, pure-int rebuild)
# ----------------------------------------------------------------------

C6 = [[2, 0, -1, 0, 0, 0], [0, 2, 0, -1, 0, 0], [-1, 0, 2, -1, 0, 0],
      [0, -1, -1, 2, -1, 0], [0, 0, 0, -1, 2, -1], [0, 0, 0, 0, -1, 2]]
EDGES = [(i, j) for i in range(6) for j in range(i + 1, 6) if C6[i][j] == -1]


def mat_mul(a, b):
    return tuple(tuple(sum(a[i][k] * b[k][j] for k in range(6)) for j in range(6))
                 for i in range(6))


def check_we6():
    log("=" * 72)
    log("F. W(E6), the stage Weyl group, |W| = 51840 (B570/B578 pattern)")
    log(f"   Cartan matrix edges (all bonds m_ij = 3, odd): {EDGES}")
    # simple reflections in the root basis: s_j = I - E_j C6 (row op)
    gens = []
    for j in range(6):
        M = [[1 if i == k else 0 for k in range(6)] for i in range(6)]
        for k in range(6):
            M[j][k] -= C6[k][j]
        gens.append(tuple(tuple(r) for r in M))
    I6 = tuple(tuple(1 if i == k else 0 for k in range(6)) for i in range(6))
    # (i) BFS the full group with the determinant sign carried along
    seen = {I6: 1}
    frontier = [(I6, 1)]
    while frontier:
        new = []
        for M, s in frontier:
            for g in gens:
                Mg = mat_mul(g, M)
                if Mg not in seen:
                    seen[Mg] = -s
                    new.append((Mg, -s))
        frontier = new
    order = len(seen)
    log(f"  BFS complete: |W| = {order}")
    assert order == 51840, order
    n_minus = sum(1 for v in seen.values() if v == -1)
    log(f"  det character: {order - n_minus} elements +1, {n_minus} elements -1"
        f"  =>  det: W ->> {{+1,-1}} SURJECTIVE  =>  |W^ab| >= 2")
    assert n_minus == order // 2
    # (ii) odd-bond conjugacy: for each edge (i,j), (s_i s_j) s_i (s_i s_j)^-1 = s_j
    for (i, j) in EDGES:
        w = mat_mul(gens[i], gens[j])
        winv = mat_mul(gens[j], gens[i])  # s_j s_i, since s^2 = 1
        assert mat_mul(mat_mul(w, gens[i]), winv) == gens[j], (i, j)
    log(f"  odd-bond conjugacy: (s_i s_j) s_i (s_i s_j)^-1 = s_j EXACT for all "
        f"{len(EDGES)} edges; the diagram is connected  =>  all 6 generators")
    log("  are conjugate  =>  W^ab is cyclic, generated by one involution")
    log("  image  =>  |W^ab| <= 2.  Combined with det: W^ab = Z/2 EXACTLY.")
    # (iii) independent confirmation: derived subgroup by normal-closure BFS
    seeds = []
    for (i, j) in EDGES:
        c = mat_mul(mat_mul(gens[i], gens[j]), mat_mul(gens[i], gens[j]))
        if c != I6:
            seeds.append(c)  # [s_i,s_j] = (s_i s_j)^2 for involutions
    seenH = {I6}
    frontier = [I6]
    inv_seeds = [mat_mul(s, s) for s in seeds]  # order 3: s^2 = s^-1
    while frontier:
        new = []
        for x in frontier:
            for g in seeds + inv_seeds:
                y = mat_mul(g, x)
                if y not in seenH:
                    seenH.add(y)
                    new.append(y)
        frontier = new
    log(f"  derived-subgroup BFS: |<[s_i,s_j]>| = {len(seenH)}")
    assert len(seenH) == 25920, len(seenH)
    # index 2 => normal automatically; contains all generator commutators
    # => W/H abelian => H = [W,W]; |W^ab| = 51840/25920 = 2
    log("  index 51840/25920 = 2  =>  H normal, W/H abelian  =>  H = [W,W],")
    log("  W^ab = Z/2 (independent confirmation), exponent 2")
    rigidity_check("W(E6)", 2)


# ----------------------------------------------------------------------
# The profinite half of the lemma (stated; the archimedean witness exact)
# ----------------------------------------------------------------------

def check_profinite_remark():
    log("=" * 72)
    log("G. The profinite half (the mod-conductor shadow tower)")
    log("  A continuous hom phi: G -> R_+ from a profinite (compact) G has")
    log("  compact image; via the iso log: (R_+,*) ~ (R,+), a compact (hence")
    log("  bounded) subgroup B of (R,+) with some t != 0 in B would contain")
    log("  all integer multiples n*t, unbounded (archimedean) -- contradiction;")
    log("  so B = {0}, phi trivial. Exact witness of the archimedean step:")
    t = Fraction(1, 10**6)  # arbitrarily small positive element
    bound = Fraction(10**9)  # any proposed bound
    n = int(bound / t) + 1
    assert n * t > bound
    log(f"  for t = {t} and any bound {bound}: n = {n} gives n*t = {n * t} "
        f"> {bound}   OK")
    log("  (Each finite shadow SL(2,Z/m) in the tower ALSO dies individually")
    log("   by the torsion argument -- conductor-15 instance verified in E.)")


def main():
    log("B666 cell S' -- verify_rigidity.py")
    log("The rigidity step: Hom(G, R_+) = 0 for every banked symmetry group.")
    log("All decisive arithmetic exact (int/Fraction/sympy; no floats).")
    check_klein_four()
    check_2i()
    check_psl27()
    check_hearing_image()
    check_sl2_z15()
    check_we6()
    check_profinite_remark()
    log("=" * 72)
    log("ALL GATES PASSED: every banked symmetry structure has finite")
    log("abelianization of pure torsion => Hom(G, R_+) = 0 in every case;")
    log("the profinite tower dies by compactness + no-small-subgroups.")
    log("THE RIGIDITY STEP IS VERIFIED EXACTLY ON ALL BANKED STRUCTURES.")


if __name__ == "__main__":
    sys.exit(main())
