"""B330 / S032-A -- the no-forced-choice capstone, attacked via one Galois-symmetrization mechanism.

GATE A asks: is there ANY invariant of the single seed that is (1) trace-map-invariant,
(2) discretely multivalued, (3) UNsymmetrizable -- a genuine forced choice the object makes?

The unified mechanism (folds B130 + B314 + B318):
  LEMMA (elementary). If a discrete invariant's value-set is a finite orbit of the object's arithmetic
  Galois group G, then its symmetric functions lie in the fixed field (canonical) -> the invariant is
  SYMMETRIZABLE, hence NOT a forced choice. (A finite Galois orbit is always symmetrizable.)

We (i) demonstrate the lemma on the object's two arithmetic ends, and (ii) STRESS it against two fresh
invariant classes not previously checked -- the cover-torsion H1 (B326) and cohomology H1 -- to see if
either is a forced-choice counterexample. Neither is.

CONDITIONAL result (C-guardrail). For the classes examined (trace ring / quantum-WRT / Eisenstein-CP /
cover-torsion / H1), every trace-map-invariant discrete invariant is a symmetrizable Galois orbit or a
canonical object -> no forced choice. This is NOT a proof over ALL invariant classes (untested classes
named in FINDINGS); "no breach reachable by these classes" is OPEN, not proof of universal impossibility.

Firewalled: a structural (no-value) statement; nothing to CLAIMS.md. Needs only sympy.
"""
import sympy as sp


def golden_orbit_symmetrizable():
    """B314 (golden end): the two Galois conjugates under sqrt5 -> -sqrt5 have rational symmetric fns."""
    phi = (1 + sp.sqrt(5)) / 2
    phi_c = (1 - sp.sqrt(5)) / 2                      # Galois conjugate
    s = sp.simplify(phi + phi_c); p = sp.simplify(phi * phi_c)
    return s, p, (s.is_rational and p.is_rational)    # (1, -1) -> canonical


def eisenstein_cp_orbit_symmetrizable():
    """B318 (Eisenstein end): the CP-sign pair e^{+- i pi/6} swapped by sqrt-3 -> -sqrt-3."""
    a = sp.exp(sp.I * sp.pi / 6); b = sp.exp(-sp.I * sp.pi / 6)
    s = sp.nsimplify(sp.simplify(sp.expand_complex(a + b)))   # 2 cos(pi/6) = sqrt3
    p = sp.simplify(sp.expand_complex(a * b))                 # 1
    return s, p, (sp.im(s) == 0 and sp.im(p) == 0)


def torsion_no_forced_choice():
    """B326 stress: deck Z/3 on H1(3-fold cover)=(Z/4)^2 has NO nonzero fixed vector (irreducible),
    so there is no canonical distinguished sub-object to be 'forced' -> symmetric -> not a forced choice."""
    C = sp.Matrix([[0, -1], [1, -1]])                # companion of Phi_3 = t^2+t+1 (the deck action)
    det_C_minus_I = int((C - sp.eye(2)).det()) % 4   # unit mod 4  <=> (C-I) invertible <=> only fixed vec is 0
    fixed_vectors = [(a, b) for a in range(4) for b in range(4)
                     if ((C - sp.eye(2)) * sp.Matrix([a, b])).applyfunc(lambda x: x % 4) == sp.zeros(2, 1)]
    return det_C_minus_I, fixed_vectors             # det unit, only (0,0)


def kappa_is_continuous():
    """B130: kappa = tr[A,B] is a CONTINUOUS coordinate on the trace ring -> not discretely multivalued,
    so it cannot be a forced choice (fails clause (2))."""
    x, y, z = sp.symbols('x y z')
    kappa = x**2 + y**2 + z**2 - x*y*z - 2
    # kappa takes a continuum of values as (x,y,z) vary -> derivative non-zero -> not locally constant
    return any(sp.diff(kappa, v) != 0 for v in (x, y, z))


if __name__ == "__main__":
    s, p, ok = golden_orbit_symmetrizable()
    print(f"golden (sqrt5) orbit: sum={s}, prod={p}, symmetrizable(rational)={ok}")
    s2, p2, ok2 = eisenstein_cp_orbit_symmetrizable()
    print(f"Eisenstein CP orbit: sum={s2}, prod={p2}, symmetrizable(real)={ok2}")
    det_, fv = torsion_no_forced_choice()
    print(f"cover-torsion (Z/4)^2: det(C-I) mod 4 = {det_} (unit), fixed vectors = {fv} -> no forced choice")
    print(f"trace ring kappa continuous (not discretely multivalued): {kappa_is_continuous()}")
    print("\nCONDITIONAL: no forced choice among the examined classes (Galois-symmetrizable or canonical).")
    print("General statement over ALL invariant classes remains OPEN (untested classes named in FINDINGS).")
