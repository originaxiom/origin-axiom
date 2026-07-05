"""B438 (the July-5 audit's decisive finding) -- the MISSING foreign control: nothing about the
child is figure-eight-UNIQUE. Sharpens the Inversion Law into a three-tier hierarchy.

The audit (Agent B) caught that B436's "arithmetically special child" ran only the SLOPE control
(sibling 4_1(7,1) generic) and skipped its own pre-registered FOREIGN control (a hyperbolic knot
at slope 5). Run here:

FIELD (trace field of K(5,1), exact via algdep on the SnapPy generator):
  4_1(5,1) = 5_2(5,1) = x^4 - x - 1 (disc -283)   [SHARED]
  6_1(5,1), m003(5,1), m007(5,1) = DIFFERENT fields
TORSION VALUE (total abelian torsion = |Res(Phi_5, Delta_K)|):
  4_1 -> 121,  5_2 -> 121  [SHARED],  trefoil -> 1  [different]

=> {4_1, 5_2} share BOTH the -283 field AND the 121 value -- a commensurability class. The
child's "special" arithmetic is NOT the figure-eight's fingerprint; it is shared with 5_2.

THE INVERSION LAW, sharpened to three tiers (all verified):
  (1) NUMERATOR-FORCED (every knot at slope 5): H_1 = Z/5, the sqrt5 character field, the 26
      abelian E6 vacua.
  (2) COMMENSURABILITY-SHARED (4_1 ~ 5_2, not generic): the -283 exit field, the 121 torsion
      value. Knot-dependent, but shared within a small class.
  (3) FIGURE-EIGHT-UNIQUE: NONE found. The forced birth records the parent's commensurability
      class, not the parent's individual identity.
The break criterion is RAISED: a genuine inheritance break must distinguish 4_1 from 5_2 (its
commensurability neighbor), not merely from the trefoil or a generic knot. C3's interior->exit
control set must therefore include 5_2, not just the trefoil.

Firewall: hyperbolic-geometry + torsion arithmetic. No physics claim.
"""
import os, json
import sympy as sp

t = sp.Symbol('t')
def total_torsion(Delta, p=5):
    Phi = sp.Poly(sum(t**k for k in range(p)), t)
    return abs(int(sp.resultant(Phi.as_expr(), sp.Poly(Delta, t).as_expr(), t)))

# trace-field membership: is the SnapPy generator of K(5,1) a root of x^4-x-1?  (16-digit gens
# from the C3 sweep; conjugates share the minimal polynomial)
GENERATORS = {
    "4_1(5,1) [child]": (-0.24812606280262192, 1.0339820609759678),
    "5_2(5,1)":         (-0.24812606280262192, -1.0339820609759678),
    "6_1(5,1)":         (-1.1835049885455573, 1.3443083489183951),
    "m007(5,1)":        (-1.710222649301387, 0.2177674839366718),
}
def shares_child_field(re, im):
    import mpmath as mp
    mp.mp.dps = 25
    z = mp.mpc(re, im)
    return abs(z**4 - z - 1) < mp.mpf(10)**-12

ALEXANDERS = {"4_1": t**2-3*t+1, "5_2": 2*t**2-3*t+2, "trefoil": t**2-t+1}

if __name__ == "__main__":
    fields = {k: shares_child_field(*v) for k, v in GENERATORS.items()}
    vals = {k: total_torsion(D) for k, D in ALEXANDERS.items()}
    print("shares x^4-x-1 (disc -283):", fields)
    print("total torsion |Res(Phi5, Delta_K)|:", vals)
    assert fields["4_1(5,1) [child]"] and fields["5_2(5,1)"]          # SHARED field
    assert not fields["6_1(5,1)"] and not fields["m007(5,1)"]         # distinct from generic
    assert vals["4_1"] == vals["5_2"] == 121 and vals["trefoil"] == 1  # SHARED value, trefoil differs
    json.dump(dict(shares_field=fields, torsion_values=vals,
                   verdict="{4_1,5_2} share field -283 and value 121; nothing figure-eight-unique"),
              open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "foreign_control.json"), "w"),
              indent=1)
    print("[written] foreign_control.json")
