#!/usr/bin/env python3
"""B1359 -- THE K3 ALTERNATIVE, DECIDED BY THE FIXED-POINT COUNTS.

A finite group G acting on a surface with isolated fixed points: the number of fixed points of g is the sum over point-orbits G/H
of the number of cosets aH fixed by g, which is |C_G(g)| |cl(g) cap H| / |H|.  For G = 2T (binary tetrahedral, SL(2,3)) the
conjugacy classes of subgroups that can be stabilisers of isolated fixed points in SU(2)-type actions are 2T, Q8, Z6, Z4, Z3, Z2
(and 1 for free points, which enter no count).  The per-element fixed-point numbers are:
  * on the Hurwitz torus T^4 = H/Lambda (B1357, computed):   order 2: 16, order 3: 9, order 4: 4, order 6: 1
  * on a K3 surface with a symplectic 2T (Nikulin/Mukai):    order 2: 8,  order 3: 6, order 4: 4, order 6: 2
We solve the linear system for the orbit multiplicities n_H >= 0 exactly, list every solution, and check the Euler characteristics
(chi of the quotient by the orbifold formula, chi of the minimal resolution = chi(quotient) + sum of ranks, which must be 24).
The torus case must return B1357's census (E6 + D4 + A1 + 4A2) once the origin (a 2T-fixed point) is required; the K3 case is
decided against Xiao's table.
"""
from fractions import Fraction as Fr
import itertools

def qmul(a, b):
    a0, a1, a2, a3 = a; b0, b1, b2, b3 = b
    return (a0*b0 - a1*b1 - a2*b2 - a3*b3, a0*b1 + a1*b0 + a2*b3 - a3*b2,
            a0*b2 - a1*b3 + a2*b0 + a3*b1, a0*b3 + a1*b2 - a2*b1 + a3*b0)
def conj(a):
    return (a[0], -a[1], -a[2], -a[3])
def closure(gens):
    G = {(Fr(1), Fr(0), Fr(0), Fr(0))}
    frontier = list(G)
    while frontier:
        new = []
        for g in frontier:
            for h in gens:
                p = qmul(g, h)
                if p not in G:
                    G.add(p); new.append(p)
        frontier = new
    return sorted(G)
ONE = (Fr(1), Fr(0), Fr(0), Fr(0))
I = (Fr(0), Fr(1), Fr(0), Fr(0)); J = (Fr(0), Fr(0), Fr(1), Fr(0))
H6 = (Fr(1, 2), Fr(1, 2), Fr(1, 2), Fr(1, 2)); H3 = (Fr(-1, 2), Fr(1, 2), Fr(1, 2), Fr(1, 2))
T2 = closure([I, J, H6])
assert len(T2) == 24
def order(g):
    p = g; n = 1
    while p != ONE:
        p = qmul(p, g); n += 1
    return n
subgroups = {
    "2T": T2,
    "Q8": closure([I, J]),
    "Z6": closure([H6]),
    "Z4": closure([I]),
    "Z3": closure([H3]),
    "Z2": closure([(Fr(-1), Fr(0), Fr(0), Fr(0))]),
}
rank = {"2T": 6, "Q8": 4, "Z6": 5, "Z4": 3, "Z3": 2, "Z2": 1}
adetype = {"2T": "E6", "Q8": "D4", "Z6": "A5", "Z4": "A3", "Z3": "A2", "Z2": "A1"}
names = list(subgroups)

def fixed_cosets(g, H):
    """number of cosets aH of 2T/H fixed by g = #{aH : a^-1 g a in H}"""
    Hs = set(H)
    n = 0
    seen = set()
    for a in T2:
        # canonical coset representative: the set aH
        coset = frozenset(qmul(a, h) for h in H)
        if coset in seen:
            continue
        seen.add(coset)
        if qmul(qmul(conj(a), g), a) in Hs:
            n += 1
    return n

reps = {2: (Fr(-1), Fr(0), Fr(0), Fr(0)), 3: H3, 4: I, 6: H6}
M = {o: [fixed_cosets(reps[o], subgroups[h]) for h in names] for o in reps}
print("fixed cosets of a representative element of each order on the orbits 2T/H:")
print("   H      : " + "  ".join(f"{h:>3}" for h in names))
for o in reps:
    print(f"   order {o}: " + "  ".join(f"{x:>3}" for x in M[o]))
# consistency: the counts are class functions (check with all elements of each order)
for o in reps:
    for g in T2:
        if order(g) == o:
            assert [fixed_cosets(g, subgroups[h]) for h in names] == M[o], "the count depends on the element within its order"
print("the counts agree for every element of the same order (both order-3 and both order-6 classes): True")

def solve(counts, label, require_2T_point=False):
    print("\n" + "=" * 100)
    print(f"{label}: per-order fixed-point numbers {counts}")
    print("=" * 100)
    sols = []
    bound = max(counts.values())
    for n in itertools.product(range(bound + 1), repeat=len(names)):
        ok = True
        for o, c in counts.items():
            if sum(n[i] * M[o][i] for i in range(len(names))) != c:
                ok = False; break
        if ok and (not require_2T_point or n[0] >= 1):
            sols.append(n)
    for n in sols:
        types = " + ".join((f"{n[i]}" if n[i] > 1 else "") + adetype[h] for i, h in enumerate(names) if n[i] > 0)
        npts = sum(n[i] * 24 // len(subgroups[h]) for i, h in enumerate(names))
        total_rank = sum(n[i] * rank[h] for i, h in enumerate(names))
        # orbifold Euler characteristic of the quotient: (chi(X) + sum_{g != 1} |Fix g|) / 24
        chiX = 0 if label.startswith("T^4") else 24
        chi_q = Fr(chiX + sum(counts[o] * sum(1 for g in T2 if order(g) == o) for o in counts), 24)
        print(f"  n = {dict(zip(names, n))}: {types}; {npts} singular points; total rank {total_rank}; "
              f"chi(quotient) = {chi_q}; chi(resolution) = {chi_q + total_rank}")
    return sols

t4 = solve({2: 16, 3: 9, 4: 4, 6: 1}, "T^4 = H/Lambda (B1357's counts)")
t4r = solve({2: 16, 3: 9, 4: 4, 6: 1}, "T^4 with the origin required to be 2T-fixed", require_2T_point=True)
k3 = solve({2: 8, 3: 6, 4: 4, 6: 2}, "K3 with a symplectic 2T (Nikulin: 8, 6, 4, 2)")
print("\nSUMMARY")
print(f"  T^4: {len(t4)} solutions of the counts, {len(t4r)} with a 2T-fixed point (B1357's census E6 + D4 + A1 + 4A2: "
      f"{t4r == [(1, 1, 0, 0, 4, 1)]})")
print(f"  K3: {len(k3)} solutions of the counts: " + "; ".join(
    " + ".join((f"{n[i]}" if n[i] > 1 else "") + adetype[h] for i, h in enumerate(names) if n[i] > 0) for n in k3))
print("  every K3 solution has total rank 19 and resolution chi = 24 (both K3 candidates are rank-19 configurations); Xiao's table decides.")
