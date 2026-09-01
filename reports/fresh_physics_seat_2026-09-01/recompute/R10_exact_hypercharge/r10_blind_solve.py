#!/usr/bin/env python3
"""R10 BLIND recomputation of B1102/B1109: the exact hypercharge solve at the A2 landing.

Written BEFORE opening any of the arc's solve scripts, results JSONs, or test locks.
Inputs used (claim-statement only, from FINDINGS.md of B1098/B1100/B1102/B1109):
  - The A2 landing's unbroken algebra is su(3)_A + su(3)_B (two trinification factors
    of e6 in su(3)^3), rank-4 Cartan = Cartan(A) + Cartan(B).            [B1098]
  - The 27 branches as (3,3bar,1) + (3bar,1,3) + (1,3,3bar) under su(3)^3; with
    factor 1 eaten, under (A,B) = (factor2, factor3):
        (3bar_A, 1_B) x mult 3,  (1_A, 3_B) x mult 3,  (3_A, 3bar_B) x mult 1.
    Fifteen exact weight classes, sizes 3^6 * 1^9.                        [B1100/B1102]
  - The banked 6Y target multiset over the 27:
        {1/6 x6, 1/3 x6, -1/2 x4, -2/3 x3, -1/3 x3, 0 x2, 1/2 x2, 1 x1}. [B1102]

Coordinates (MY OWN, chosen blind): t = (a1, a2, b1, b2) in the rank-4 Cartan dual,
where the 3 of su(3)_A has t-values (a1, a2, a3), a3 = -a1-a2, and the 3 of su(3)_B
has (b1, b2, b3), b3 = -b1-b2.  Then the 27's value multiset is
   M(t) = {-a1 x3, -a2 x3, -a3 x3}  u  {b1 x3, b2 x3, b3 x3}  u  {a_i - b_j : i,j}.

Completeness argument (my own): every size-3 weight class must take a target value of
multiplicity >= 3, i.e. one of the five values {1/6, 1/3, -1/2, -2/3, -1/3}.  The four
classes with values (-a1, -a2, b1, b2) are linearly independent functionals of t, so t
is fully determined by their assignment: enumerate all 5^4 = 625 assignments exactly
and verify each candidate on the full 27-value multiset.  This is exhaustive.

Everything exact (Fraction arithmetic).
"""
from fractions import Fraction as F
from itertools import product, permutations
import json, os

HERE = os.path.dirname(os.path.abspath(__file__))

# ---------------- target (banked claim data, B1102) ----------------
TARGET = sorted([F(1,6)]*6 + [F(1,3)]*6 + [F(-1,2)]*4 + [F(-2,3)]*3
                + [F(-1,3)]*3 + [F(0)]*2 + [F(1,2)]*2 + [F(1)]*1)
assert len(TARGET) == 27
assert sum(TARGET) == 0
ADMISSIBLE = [F(1,6), F(1,3), F(-1,2), F(-2,3), F(-1,3)]  # multiplicity >= 3 values

def triple(x1, x2):
    return (x1, x2, -x1 - x2)

def multiset(a1, a2, b1, b2):
    a = triple(a1, a2)
    b = triple(b1, b2)
    vals = []
    for ai in a:
        vals += [-ai] * 3           # (3bar_A, 1_B) classes, mult 3 each
    for bj in b:
        vals += [bj] * 3            # (1_A, 3_B) classes, mult 3 each
    for ai in a:
        for bj in b:
            vals.append(ai - bj)    # (3_A, 3bar_B) singles
    return sorted(vals)

def complete_search(target):
    """Exhaustive: assign the four independent size-3 classes (-a1,-a2,b1,b2)
    each one of the admissible (mult>=3) values of `target`."""
    tgt = sorted(target)
    # admissible values for THIS target: multiplicity >= 3
    from collections import Counter
    cnt = Counter(tgt)
    adm = [v for v, c in cnt.items() if c >= 3]
    sols = []
    for v1, v2, v3, v4 in product(adm, repeat=4):
        a1, a2, b1, b2 = -v1, -v2, v3, v4
        if multiset(a1, a2, b1, b2) == tgt:
            sols.append((a1, a2, b1, b2))
    return sorted(set(sols)), adm

sols, adm = complete_search(TARGET)
print(f"admissible (mult>=3) target values: {sorted(adm)}  (count {len(adm)}) -> {len(adm)**4} assignments")
print(f"NUMBER OF EXACT SOLUTIONS: {len(sols)}")

# denominators
dens = sorted({x.denominator for s in sols for x in s})
print(f"denominators occurring across all solution coords: {dens} (all divide 6: {all(6 % d == 0 for d in dens)})")

# purity check (Side 2, Cartan level): no solution pure on either ideal
pure_A = [s for s in sols if s[2] == 0 and s[3] == 0]  # zero on B => pure A component
pure_B = [s for s in sols if s[0] == 0 and s[1] == 0]
print(f"solutions with zero B-component: {len(pure_A)}; with zero A-component: {len(pure_B)}")

# Y-neutral roots per solution: roots of su(3)_A are a_i - a_j (i != j); neutral iff a_i == a_j
def neutral_root_pairs(s):
    a = triple(s[0], s[1]); b = triple(s[2], s[3])
    na = sum(1 for i in range(3) for j in range(i+1, 3) if a[i] == a[j])  # unordered pairs => 2 roots each
    nb = sum(1 for i in range(3) for j in range(i+1, 3) if b[i] == b[j])
    return na, nb
neut = [neutral_root_pairs(s) for s in sols]
print(f"Y-neutral root count (unordered pairs, per ideal) over all solutions: {sorted(set(neut))}")
print(f"  (each pair = 2 roots; claim 'exactly two Y-neutral roots, one per ideal' <=> (1,1) with a-triple, b-triple not all equal)")

# ---------------- Weyl orbits: W(A2) x W(A2) = S3 x S3, order 36 ----------------
def act(sigma, tau, s):
    a = triple(s[0], s[1]); b = triple(s[2], s[3])
    ap = [a[sigma[i]] for i in range(3)]
    bp = [b[tau[i]] for i in range(3)]
    return (ap[0], ap[1], bp[0], bp[1])

perms = list(permutations(range(3)))
solset = set(sols)
# sanity: the full order-36 group preserves the solution set
preserved = all(act(sg, tu, s) in solset for sg in perms for tu in perms for s in sols)
print(f"all 36 Weyl moves preserve the 18-solution set: {preserved}")

# orbit partition
unseen = set(sols)
orbits = []
while unseen:
    s0 = sorted(unseen)[0]
    orb = {act(sg, tu, s0) for sg in perms for tu in perms}
    assert orb <= solset
    orbits.append(sorted(orb))
    unseen -= orb
print(f"ORBITS under W(A2)xW(A2): {len(orbits)}, sizes {[len(o) for o in orbits]}")

# ideal swap tests (B1109 F4b): plain swap (a,b)->(b,a); and swap-with-sign (a,b)->(-b,-a)
def swap_plain(s):  return (s[2], s[3], s[0], s[1])
def swap_sign(s):   return (-s[2], -s[3], -s[0], -s[1])
n_plain = sum(1 for s in sols if swap_plain(s) in solset)
n_sign  = sum(1 for s in sols if swap_sign(s)  in solset)
print(f"plain ideal swap maps solutions to solutions: {n_plain}/18")
print(f"swap-with-sign (a,b)->(-b,-a) maps solutions to solutions: {n_sign}/18")
if n_sign and len(orbits) == 2:
    o0 = set(orbits[0])
    cross = sum(1 for s in orbits[0] if swap_sign(s) not in o0)
    print(f"swap-with-sign sends orbit-0 members OUT of orbit-0: {cross}/{len(orbits[0])}")

# banked representative t = (1/6, 1/6, 2/3, -1/3) in THEIR adapted crystal Cartan.
rep = (F(1,6), F(1,6), F(2,3), F(-1,3))
print(f"banked representative coords {tuple(map(str, rep))} in MY solution set (literal): {rep in solset}")
# also check up to the conjugation relabeling t -> plain-swap (covers 27-vs-27bar convention)
print(f"  ... its plain-swap image in my set: {swap_plain(rep) in solset}")
print(f"  ... its negation in my set: {tuple(-x for x in rep) in solset}")

# orbit invariant: sorted a-triple / b-triple value content per orbit (Weyl-invariant)
def orbit_signature(orb):
    sigs = sorted({(tuple(sorted(triple(s[0], s[1]))), tuple(sorted(triple(s[2], s[3])))) for s in orb})
    return sigs
for k, o in enumerate(orbits):
    sig = orbit_signature(o)
    print(f"orbit {k}: size {len(o)}, (sorted a-triple, sorted b-triple) signatures: "
          + "; ".join("a=" + str(tuple(map(str, x[0]))) + " b=" + str(tuple(map(str, x[1]))) for x in sig))

# ---------------- CONTROL: the instrument CAN find planted things ----------------
# Control 1 (exclusion control): plant a PURE-on-one-ideal direction, target its own
# multiset, confirm the complete search finds it (so the pure-solution absence above
# is a real exclusion, not instrument blindness).
plant = (F(0), F(0), F(1,3), F(1,6))   # pure on ideal B
tgt_p = multiset(*plant)
sols_p, adm_p = complete_search(tgt_p)
print(f"CONTROL-1: planted pure direction {tuple(map(str, plant))}; search returns {len(sols_p)} solutions; planted found: {plant in set(sols_p)}")

# Control 2: plant a generic mixed direction and confirm recovery.
plant2 = (F(1,6), F(-1,3), F(1,3), F(1,6))
tgt2 = multiset(*plant2)
sols2, _ = complete_search(tgt2)
print(f"CONTROL-2: planted mixed direction {tuple(map(str, plant2))}; search returns {len(sols2)} solutions; planted found: {plant2 in set(sols2)}")

# Control 3 (Weyl-orbit control): a target whose solution set is a single orbit should
# come back as ONE orbit — the orbit machinery can distinguish counts.
if sols2:
    unseen2 = set(sols2); orbs2 = []
    while unseen2:
        s0 = sorted(unseen2)[0]
        orb = {act(sg, tu, s0) for sg in perms for tu in perms}
        orbs2.append(orb); unseen2 -= orb
    print(f"CONTROL-3: planted-target solution set splits into {len(orbs2)} orbit(s), sizes {[len(o) for o in orbs2]}")

# dump results
out = {
    "n_solutions": len(sols),
    "solutions_a1_a2_b1_b2": [[str(x) for x in s] for s in sols],
    "denominators": [int(d) for d in dens],
    "pure_on_ideal": {"zero_B_component": len(pure_A), "zero_A_component": len(pure_B)},
    "neutral_root_pair_counts": sorted({tuple(n) for n in neut}),
    "orbits": {"count": len(orbits), "sizes": [len(o) for o in orbits],
               "members": [[[str(x) for x in s] for s in o] for o in orbits]},
    "swap_plain_hits": n_plain, "swap_sign_hits": n_sign,
    "banked_rep_literal_in_my_set": rep in solset,
    "controls": {"pure_plant_found": plant in set(sols_p), "pure_plant_nsols": len(sols_p),
                 "mixed_plant_found": plant2 in set(sols2), "mixed_plant_nsols": len(sols2)},
}
with open(os.path.join(HERE, "r10_blind_results.json"), "w") as f:
    json.dump(out, f, indent=1, default=str)
print("\nwrote r10_blind_results.json")
print("\nALL 18 SOLUTIONS (a1,a2,b1,b2):")
for s in sols:
    print("  ", tuple(map(str, s)))
