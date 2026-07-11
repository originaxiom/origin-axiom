"""
Movement XII — the eigenvector geometry of the growth: how the object contracts,
and the plane the breath turns in.

Neutral census item (METHOD.md). The growth matrix M has char poly
x^4-2x^3-5x^2-4x-1. Its four modes, read for their geometry:

  * ONE expanding mode  beta = 3.6762  (the frequency direction; the growth).
  * a COMPLEX breath pair  gamma  with  |gamma| = 1/sqrt(phi),  Re(gamma) = -1/phi,
    and rotation angle  theta = arccos(-1/sqrt phi) ~ 141.83 deg per inflation.
    The breath is doubly golden: its RADIUS and the COSINE of its ANGLE are both
    (up to sign) 1/sqrt(phi).
  * ONE real negative mode  -0.4401  (an orientation-flip + contraction).

So the object EXPANDS in 1 dimension and CONTRACTS in a 3-space; the breath is a
rotation-with-contraction in a 2-plane inside that stable 3-space.

ANTI-ANTICIPATION (report the flat): the breath angle 141.83 deg is NOT the golden
angle 137.51 deg (off by +4.32 deg). The golden ratio sets the breath's radius and
the cosine of its turn, but the turn itself is not the sunflower angle. Say so.

No physics. The geometry of the object's own growth operator.
"""
import numpy as np

PHI = (1 + np.sqrt(5)) / 2
# M = abelianization / growth matrix of phi: a->abAAB, b->aAB, A->abAB, B->aA  (rows=a,b,A,B)
M = np.array([[1, 1, 1, 1],
              [1, 0, 1, 0],
              [2, 1, 1, 1],
              [1, 1, 1, 0]], float)


def report():
    vals = np.linalg.eigvals(M)
    beta = max(vals, key=lambda z: z.real).real
    gamma = [v for v in vals if abs(v.imag) > 1e-9][0]
    realneg = [v for v in vals if abs(v.imag) < 1e-9 and v.real < 0][0].real
    theta = np.angle(gamma)

    print("modes of the growth matrix (char poly x^4-2x^3-5x^2-4x-1):")
    print(f"  expanding : beta   = {beta:+.5f}                       (growth; the frequency direction)")
    print(f"  breath    : gamma  = {gamma.real:+.5f} +/- {abs(gamma.imag):.5f}i   "
          f"|gamma|={abs(gamma):.5f}=1/sqrt(phi)")
    print(f"              Re(gamma) = -1/phi = {-1/PHI:+.5f}")
    print(f"              cos(theta) = {np.cos(theta):+.5f} = -1/sqrt(phi);  theta = {np.degrees(theta):.2f} deg")
    print(f"  flip      : lambda = {realneg:+.5f}                       (orientation-flip + contraction)")
    print(f"  spectrum |lambda| = {sorted([round(abs(v),4) for v in vals], reverse=True)}"
          f"  -> expand in 1, contract in 3")

    golden_angle = np.degrees(2 * np.pi / PHI**2)
    print(f"\nanti-anticipation: breath angle {np.degrees(theta):.2f} deg vs golden angle "
          f"{golden_angle:.2f} deg  -> NOT equal ({np.degrees(theta)-golden_angle:+.2f} deg).")
    print(f"non-normality: ||[M,M^T]|| = {np.linalg.norm(M@M.T - M.T@M):.3f} != 0  (the breath needs it).")


def checks():
    """The exact relations, for the lock."""
    vals = np.linalg.eigvals(M)
    gamma = [v for v in vals if abs(v.imag) > 1e-9][0]
    theta = np.angle(gamma)
    assert abs(abs(gamma) - 1 / np.sqrt(PHI)) < 1e-9          # radius = 1/sqrt(phi)
    assert abs(gamma.real - (-1 / PHI)) < 1e-9                # Re = -1/phi
    assert abs(np.cos(theta) - (-1 / np.sqrt(PHI))) < 1e-9    # cos(angle) = -1/sqrt(phi)
    assert abs(np.degrees(theta) - np.degrees(2 * np.pi / PHI**2)) > 3   # NOT the golden angle
    mags = sorted([abs(v) for v in vals], reverse=True)
    assert mags[0] > 1 and all(m < 1 for m in mags[1:])       # expand in 1, contract in 3
    return True


if __name__ == "__main__":
    report()
    print("\nchecks:", checks())
