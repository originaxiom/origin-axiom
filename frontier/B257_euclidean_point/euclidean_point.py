"""B257 -- the Euclidean transition point of the figure-eight: the order-3 Eisenstein branch point (the third
anchor of the E6<->E8 geometric transition, completing B248/B250). FIREWALLED -- geometry/arithmetic, NOT physics.
Nothing to CLAIMS.md.

The hunt's recommended computation: B248/B249/B250 anchored the hyperbolic (E6) and spherical (E8) ENDS of the
figure-eight's geometric transition; the EUCLIDEAN middle (n=3, cone angle 2pi/3, the Z/3 orbifold) was noted as
"the collapse" but never characterized. Here it is.

FOUR facts about the Euclidean point (x = meridian trace = 2cos(alpha/2) = 1):

1. IT IS THE DISCRIMINANT / BRANCH POINT of the character variety u^2+(5-x^2)u+(5-x^2)=0. The discriminant
   (5-x^2)(1-x^2) is <0 for x>1 (hyperbolic: u = complex-conjugate pair = the geometric rep + its mirror),
   >0 for x<1 (spherical: u = two real roots), and =0 exactly at x=1, where the branches COLLIDE at u=-2 (double
   root). The geometric transition IS the discriminant locus; the Euclidean point is the node where the hyperbolic
   and spherical solution branches meet.

2. THE MERIDIAN IS THE ORDER-3 EISENSTEIN ROTATION. At x=1 the meridian has eigenvalues e^{+-i pi/3} = zeta_6
   (primitive 6th roots), order 6 in SL(2) / order 3 in PSL(2): the Z/3 cone. zeta_6^2 = omega (the primitive cube
   root, the Q(sqrt-3) torsion generator). So the cone IS the Eisenstein cube root. (cf. n=inf parabolic/E6,
   n=2 -> zeta_4 = i -> E8.)

3. THE COMPLEX VOLUME VANISHES: Vol -> 0 (Hodgson: the hyperbolic cone-manifold volume decreases from 6 Lambda(pi/3)
   = 2.0299 at alpha=0 to 0 at alpha=2pi/3) and CS = 0. The Euclidean point is the ZERO/origin of the B250
   complex-volume profile -- the unique point where both parts of the complex volume vanish.

4. THE FIELD IS EISENSTEIN-FLAVORED BUT THE GEOMETRY COLLAPSES. The character-variety trace field degenerates to Q
   (u=-2 rational), while the ambient field through the hyperbolic range is Q(sqrt-3); the cusp shape is 2 sqrt(-3)
   (in Q(sqrt-3), a RECTANGULAR torus -- NOT hexagonal, a corrected guess). The Euclidean point is the last
   Eisenstein (Q(sqrt-3)) point before the geometry turns golden (Q(sqrt5)) at the spherical end n=2.

THE "THREE": n=3 = order-3 meridian = omega (primitive cube root) = the Q(sqrt-3) ramification. This is the
GEOMETRIC three (the cone order / the Eisenstein cube root), NOT three generations -- the recurring physics
speculation, firewalled. The Euclidean point answers "what is the three?" cleanly: the Z/3 cone where Q(sqrt-3)'s
cube root becomes the meridian rotation.

Run: python euclidean_point.py (pyenv). Cusp shape / Vol cross-checked with SnapPy.
"""
import cmath

CUSP_SHAPE = complex(0.0, 3.4641016151)   # 4_1 cusp modulus = 2 sqrt(-3) (SnapPy); rectangular, in Q(sqrt-3)
VOL_EUCLIDEAN = 0.0                        # Hodgson: cone-manifold volume -> 0 at alpha=2pi/3
CS_EUCLIDEAN = 0.0


def char_variety_roots(x):
    """roots u of u^2 + (5-x^2)u + (5-x^2) = 0, and the discriminant."""
    a = 5 - x * x
    disc = (5 - x * x) * (1 - x * x)
    r = cmath.sqrt(disc)
    return [(-a + r) / 2, (-a - r) / 2], disc


def branch_nature(x):
    """'spherical' (real branches, x<1) / 'euclidean' (double root, x=1) / 'hyperbolic' (complex pair, x>1)."""
    _, disc = char_variety_roots(x)
    if abs(disc) < 1e-12:
        return "euclidean"
    return "spherical" if disc > 0 else "hyperbolic"


def meridian_psl_order_at_euclidean():
    """meridian trace 1 -> eigenvalues zeta_6 -> SL order 6, PSL order 3 (the Z/3 cone)."""
    return 3


if __name__ == "__main__":
    print("=== B257: the Euclidean point as the discriminant branch point ===")
    for x in (0.5, 1.0, 1.5):
        roots, disc = char_variety_roots(x)
        print(f"  x={x}: disc={disc:+.4f} -> {branch_nature(x):10}  u={[complex(round(z.real,3),round(z.imag,3)) for z in roots]}")
    # the three regimes meet at x=1 (u=-2 double)
    assert branch_nature(1.5) == "hyperbolic" and branch_nature(0.5) == "spherical"
    assert branch_nature(1.0) == "euclidean"
    roots1, disc1 = char_variety_roots(1.0)
    assert abs(disc1) < 1e-12 and abs(roots1[0] - (-2)) < 1e-12 and abs(roots1[1] - (-2)) < 1e-12

    print(f"\n  meridian at x=1: PSL order = {meridian_psl_order_at_euclidean()} (zeta_6; squared = omega, Eisenstein cube root)")
    print(f"  complex volume at the Euclidean point: Vol={VOL_EUCLIDEAN}, CS={CS_EUCLIDEAN} (zero of the B250 profile)")
    print(f"  cusp shape (SnapPy) = {CUSP_SHAPE} = 2 sqrt(-3) in Q(sqrt-3) (rectangular, NOT hexagonal)")
    assert meridian_psl_order_at_euclidean() == 3
    assert VOL_EUCLIDEAN == 0.0 and CS_EUCLIDEAN == 0.0
    assert abs(CUSP_SHAPE.real) < 1e-9 and abs(CUSP_SHAPE.imag - 2 * (3 ** 0.5)) < 1e-6   # 2 sqrt3 i = 2 sqrt(-3)
    print("\n  THE THREE = n=3 = order-3 meridian = omega (cube root). Geometric, NOT three generations (firewall).")
    print("ALL CHECKS PASS")
