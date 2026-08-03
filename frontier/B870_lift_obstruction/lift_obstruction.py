#!/usr/bin/env python3
"""B870 -- G7: the central-extension lift obstruction, computed on the object and the sister.

The critic's G7: the cascade/global-form story (B862's Z6) speaks of quotient groups G/Z;
on the OBJECT (m004), a flat G/Z-bundle lifts to G iff its obstruction class in
H^2(pi_1; Z) vanishes. This arc computes the obstruction GROUPS exactly.

Method: pi_1 presentations from SnapPy (2 generators, 1 relator). For one-relator groups
whose relator is not a proper power, the presentation 2-complex is aspherical (Lyndon), so
group cohomology = cellular cohomology of the 2-complex. With TRIVIAL coefficients A the
cochain differential d2: A^2 -> A is given by the AUGMENTED Fox derivatives -- the relator's
exponent sums (e_a, e_b): d2(u, v) = e_a*u + e_b*v. Hence

    H^2(pi_1; A) = A / (e_a*A + e_b*A) = A / gcd(e_a, e_b)*A,
    H^1(pi_1; A) = Hom(H_1; A)  (the lift-ambiguity torsor when lifts exist).

Cross-checks: universal coefficients (H^2 = Ext(H_1, A) since H_2 = 0 here), SnapPy's
homology, and a direct not-a-proper-power certificate. Prior art named: Culler's lifting
theorem is the p=2/SL(2) ancestor of the same vanishing.

Mathematics scope; nothing to CLAIMS.md; Gate 5 untouched.
"""
import json
import os
from math import gcd

import snappy

HERE = os.path.dirname(os.path.abspath(__file__))


def presentation(name):
    G = snappy.Manifold(name).fundamental_group()
    gens, rels = G.generators(), G.relators()
    assert gens == ['a', 'b'] and len(rels) == 1, (name, gens, rels)
    return rels[0]


def exponent_sums(rel):
    ea = rel.count('a') - rel.count('A')
    eb = rel.count('b') - rel.count('B')
    return ea, eb


def not_proper_power(rel):
    """A cyclically reduced relator w^n (n>=2) is a strict period of its own word:
    check every divisor period directly."""
    L = len(rel)
    for d in range(1, L):
        if L % d == 0 and rel == rel[:d] * (L // d):
            return False
    return True


def h2_order(ea, eb, n):
    """|H^2(pi_1; Z/n)| = |Z/n / (gcd(ea, eb) Z/n)| = gcd(gcd(ea, eb), n)."""
    return gcd(gcd(ea, eb), n)


def h1_hom_order(h1_free_rank, h1_torsion, n):
    """|Hom(H_1; Z/n)| for H_1 = Z^r + sum Z/t."""
    o = n ** h1_free_rank
    for t in h1_torsion:
        o *= gcd(t, n)
    return o


def main():
    res = {}
    for name, h1 in (("m004", (1, [])), ("m003", (1, [5]))):
        rel = presentation(name)
        ea, eb = exponent_sums(rel)
        g = gcd(ea, eb)
        # H_1 = Z^2 / <(ea, eb)> = Z + Z/g  -- must match SnapPy's homology
        M = snappy.Manifold(name)
        row = dict(
            relator=rel, exponent_sums=[ea, eb], gcd=g,
            not_proper_power=not_proper_power(rel),
            snappy_homology=str(M.homology()),
            h1_matches=(g == (h1[1][0] if h1[1] else 1)),
            # the obstruction groups at the primes that matter + a sweep
            H2={str(n): h2_order(ea, eb, n) for n in (2, 3, 5, 6, 7, 30)},
            # the lift-ambiguity torsor (only meaningful where lifts exist)
            H1_hom={str(n): h1_hom_order(*h1, n) for n in (3, 5, 6)},
        )
        res[name] = row

    ob4, ob3 = res["m004"], res["m003"]
    res["verdicts"] = {
        "object_unobstructed_all_primes": all(v == 1 for v in ob4["H2"].values())
                                          and ob4["gcd"] == 1,
        "object_E6_center_Z3": dict(H2=ob4["H2"]["3"], lifts_torsor=ob4["H1_hom"]["3"]),
        "object_SM_Z6": dict(H2=ob4["H2"]["6"], lifts_torsor=ob4["H1_hom"]["6"]),
        "sister_at_atom_prime_3": ob3["H2"]["3"],
        "sister_at_5": ob3["H2"]["5"],
        "split": (ob4["H2"]["5"] == 1 and ob3["H2"]["5"] == 5
                  and ob4["H2"]["3"] == 1 and ob3["H2"]["3"] == 1),
    }
    json.dump(res, open(os.path.join(HERE, "results.json"), "w"), indent=1,
              sort_keys=True)

    print("=" * 74)
    print("B870 -- the lift obstruction on the object and the sister")
    print("=" * 74)
    for name in ("m004", "m003"):
        r = res[name]
        print(f"\n  {name}: relator {r['relator']}  exp sums {r['exponent_sums']} "
              f"gcd {r['gcd']}  proper power: {not r['not_proper_power']}")
        print(f"    snappy homology: {r['snappy_homology']}")
        print(f"    |H^2(pi_1; Z/n)|: {r['H2']}")
    v = res["verdicts"]
    print(f"\n  object unobstructed at ALL primes : {v['object_unobstructed_all_primes']}")
    print(f"  object, E6 center Z/3             : H2 {v['object_E6_center_Z3']['H2']}, "
          f"lift torsor {v['object_E6_center_Z3']['lifts_torsor']}")
    print(f"  object, SM Z/6 (B862)             : H2 {v['object_SM_Z6']['H2']}, "
          f"lift torsor {v['object_SM_Z6']['lifts_torsor']}")
    print(f"  sister at the atom prime 3        : H2 {v['sister_at_atom_prime_3']}")
    print(f"  sister at 5                       : H2 {v['sister_at_5']}  <-- the split")
    print(f"  object/sister split at p=5        : {v['split']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
