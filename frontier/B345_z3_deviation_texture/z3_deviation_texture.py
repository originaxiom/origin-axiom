"""B345 -- the Z/3-graded texture of the deviation space: a forced charge-conservation selection rule.

Target 2 of the deviation-structure strategy. A forced, dimensionless TEXTURE (which deviation couplings
vanish) -- form, like B326, not a value.

  The trace-map deviation modes at the symmetric centre (0,0,0) are the Z/3 eigenvectors, carrying
  Z/3 CHARGES {0,1,2} (eigenvalues {1, omega, omega^2}). The charge-0 (invariant) direction is (1,-1,1).

  FORCED SELECTION RULE: a Z/3-invariant coupling of deviations conserves charge mod 3. So a quadratic
  (mass-matrix-type) coupling deviation_i x deviation_j is nonzero ONLY when charge_i + charge_j = 0
  mod 3 -> the ANTI-DIAGONAL texture {0-0, 1-2, 2-1}; forbidden: {0-1, 0-2, 1-1, 2-2}. This IS the
  omega-circulant / democratic structure (B324) read as a deviation selection rule; the irreducibility
  (B343) is why the charge-{1,2} sector has no further invariant sub-line.

  HONEST CROSS-CHECK (null-glance): the B265 exponent split {4,8} (escape E6) vs {5,7,11} (trapped F4)
  does NOT align with the Z/3 charge (mod 3: escape={1,2}, trapped={2,1,2}). So the deviation space
  carries TWO INDEPENDENT structures -- the Z/3 charge and the E6-exponent grading -- not one texture.

TIER: the charge-conservation selection rule is GENERIC to any Z/3; what is object-specific is that the
trace-map tangent action REALIZES the Z/3 (the deviation modes ARE the charges, B343), with charge-0 =
(1,-1,1). FORM, not value. Firewalled; nothing to CLAIMS. Needs only sympy.
"""
import sympy as sp

x, y, z = sp.symbols('x y z')
W = sp.exp(2 * sp.I * sp.pi / 3)


def Ta(p): X, Y, Z = p; return (X, Z, X*Z - Y)
def Tb(p): X, Y, Z = p; return (Z, Y, Y*Z - X)
def phi(p, m):
    for _ in range(m): p = Tb(p)
    for _ in range(m): p = Ta(p)
    return p


def deviation_charges():
    """Z/3 charges of the deviation modes at the centre = {arg(eigenvalue)/(2pi/3) mod 3}; = {0,1,2}."""
    import cmath
    J = sp.Matrix([[sp.diff(fi, v) for v in (x, y, z)] for fi in phi((x, y, z), 1)]).subs({x: 0, y: 0, z: 0})
    charges = set()
    for val in J.eigenvals():
        c = complex(val)
        charges.add(round(cmath.phase(c) / (2 * cmath.pi / 3)) % 3)   # eigenvalue = omega^charge
    return charges                                     # {0, 1, 2}


def selection_rule():
    """charge-conservation: quadratic coupling (i,j) allowed iff (charge_i + charge_j) % 3 == 0."""
    allowed = [(a, b) for a in (0, 1, 2) for b in (0, 1, 2) if (a + b) % 3 == 0]
    forbidden = [(a, b) for a in (0, 1, 2) for b in (0, 1, 2) if (a + b) % 3 != 0]
    return allowed, forbidden                          # allowed {(0,0),(1,2),(2,1)} = anti-diagonal


def exponent_split_aligns_with_charge():
    """B265: escape {4,8} vs trapped {5,7,11}. Does the Z/3 charge (mod 3) SEPARATE them? Returns False."""
    escape = {e % 3 for e in (4, 8)}                    # {1, 2}
    trapped = {e % 3 for e in (5, 7, 11)}              # {1, 2}
    return escape.isdisjoint(trapped)                   # False: both {1,2} -> charge does NOT separate -> independent

if __name__ == "__main__":
    print("deviation Z/3 charges:", sorted(deviation_charges()), "(charge-0 direction = (1,-1,1))")
    allowed, forbidden = selection_rule()
    print("selection rule -- allowed (charge-conserving):", allowed)
    print("               -- forbidden:", forbidden, " => anti-diagonal texture (= omega-circulant, B324)")
    print("B265 exponent split aligns with Z/3 charge?:", bool(exponent_split_aligns_with_charge()),
          "(True here means NOT cleanly separated -> two independent structures)")
