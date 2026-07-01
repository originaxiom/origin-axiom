"""B346 -- the cross-structure map of the deviation space: one forced link, one independent grading.

Target 3 of the deviation-structure strategy (the "prize": a forced cross-sector relation, ideally a
second falsifier). Honest outcome: a forced cross-STRUCTURE relation exists (a form), but NO data-facing
second falsifier -- consistent with the whole arc (the object forces form, not values).

  LINKED (forced): the symplectic conjugation lambda -> 1/lambda (B344) EQUALS the Z/3 charge conjugation
      c -> -c mod 3 (B345). Verified at the symmetric centre: the reciprocal pair carries Z/3 charges
      (1,2); the un-paired direction (eigenvalue 1) is charge 0 = the Casimir/scale direction (B344).
      So the object's symplectic (metric) structure and its Z/3 (texture) structure COINCIDE at the centre.

  INDEPENDENT: the E6-exponent split {4,8} (escape) / {5,7,11} (trapped) (B265) is NOT graded by the Z/3
      charge (B345). So the E6-exponent is a THIRD, independent structure.

  => the deviation space carries ONE linked pair (symplectic <-> Z/3) + ONE independent grading
     (E6-exponent). The structures are otherwise ORTHOGONAL -- which is WHY the object can be the
     symmetric centre of independent physical sectors without correlating them.

VERDICT (honest): the cross-structure relation is a STRUCTURAL FORM (symplectic = Z/3 conjugation), not
a data-facing falsifier -- no second measured relation is predicted; the values stay external. NULL: the
'reciprocal = conjugate' link is generic to a Z/3-elliptic centre, which the object HAS (object-specific
realization). Firewalled; nothing to CLAIMS. Needs only sympy.
"""
import sympy as sp
import cmath

x, y, z = sp.symbols('x y z')


def Ta(p): X, Y, Z = p; return (X, Z, X*Z - Y)
def Tb(p): X, Y, Z = p; return (Z, Y, Y*Z - X)
def phi(p, m):
    for _ in range(m): p = Tb(p)
    for _ in range(m): p = Ta(p)
    return p


def _center_eigs():
    J = sp.Matrix([[sp.diff(fi, v) for v in (x, y, z)] for fi in phi((x, y, z), 1)]).subs({x: 0, y: 0, z: 0})
    return [complex(e) for e in J.eigenvals()]


def _charge(e): return round(cmath.phase(e) / (2 * cmath.pi / 3)) % 3


def symplectic_equals_charge_conjugation():
    """the reciprocal pairing lambda->1/lambda == Z/3 charge conjugation c->-c mod 3."""
    return all(_charge(1 / e) == (-_charge(e)) % 3 for e in _center_eigs())


def e6_exponent_independent_of_charge():
    """B265 escape {4,8} vs trapped {5,7,11} are NOT separated by Z/3 charge (both {1,2} mod 3)."""
    return ({e % 3 for e in (4, 8)} == {e % 3 for e in (5, 7, 11)})   # both {1,2} -> not separated


if __name__ == "__main__":
    print("center eigenvalue charges + reciprocals:",
          [(round(e.real, 2), _charge(e), _charge(1 / e)) for e in _center_eigs()])
    print("LINKED: symplectic conjugation == Z/3 charge conjugation:", symplectic_equals_charge_conjugation())
    print("INDEPENDENT: E6-exponent split not graded by Z/3 charge:", e6_exponent_independent_of_charge())
    print("=> one linked pair (symplectic<->Z/3) + one independent grading (E6-exponent).")
    print("   VERDICT: a structural FORM, not a data-facing second falsifier. Values external. Firewall holds.")
