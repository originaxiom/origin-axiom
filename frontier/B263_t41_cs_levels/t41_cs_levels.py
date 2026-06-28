"""B263 -- Rung 1b: the Chern-Simons structure of T[4_1] from the Neumann-Zagier symplectic frame.
FIREWALLED (3d-3d / quantum topology, not physics). Nothing to CLAIMS.md.

Completes the DEFINITION of T[4_1] (Rung 1 = B262 gave gauge group + matter; this gives the CS levels).

EXACT log-change-of-basis, SnapPy rect [a,b,c] -> Neumann-Zagier (Z, Z''):
  z=e^Z; z z' z''=-1 => Z+Z'+Z''=i*pi; z'=1/(1-z) => 1-z=e^{-Z'}=e^{Z+Z''-i*pi}, so log(1-z)=Z+Z''-i*pi.
  => prod z^a (1-z)^b = (-1)^c  becomes  sum[(a+b)Z + b Z''] = i*pi(c+sum b);  hence A=a+b, B=b, nu=c+sum(b).

From the figure-eight gluing data (B262):
  edge (gauge):     A=[1,1]  B=[-1,-1]
  meridian (flavor):A=[1,0]  B=[0,-1]
  longitude:        A=[0,2]  B=[0,-2]

Stacking (edge, meridian) as the position rows:  A=[[1,1],[1,0]], B=[[-1,-1],[0,-1]].
  * Neumann-Zagier symplectic property: A B^T = [[-2,-1],[-1,0]] SYMMETRIC -> a valid Lagrangian datum (the
    theory is well-defined; this is the rigor gate).
  * CS quadratic form: A^{-1} B = [[0,-1],[-1,0]] SYMMETRIC -> read off:
      k_uu (gauge-gauge)  = 0   (bare; the two chirals' -1/2 parity shifts make the UV gauge CS half-integer)
      k_um (gauge-flavor) = -1  (a UNIT mixed/BF coupling -- how the meridian fugacity m enters)
      k_mm (flavor-flavor)= 0

T[4_1] now fully defined (this frame): U(1) gauge (k_uu=0 bare), 2 chirals (gauge charge +1 from A_edge=(1,1)),
flavor U(1)_m coupled by a unit BF CS, monopole superpotential. HONEST caveat: CS levels are FRAME-dependent (the
Sp(2,Z) duality group); the frame-INVARIANT content is the partition function (Rung 3).

Run: python t41_cs_levels.py (pyenv, sympy).
"""
import sympy as sp


def rect_to_nz(a, b, c):
    """SnapPy rect exponents -> Neumann-Zagier (A,B,nu): A=a+b, B=b, nu=(c+sum b) mod 2."""
    A = [ai + bi for ai, bi in zip(a, b)]
    B = list(b)
    nu = (c + sum(b)) % 2
    return A, B, nu


# figure-eight gluing data (from B262 / SnapPy)
EDGE = rect_to_nz([2, 2], [-1, -1], 1)
MERIDIAN = rect_to_nz([1, 1], [0, -1], -1)
LONGITUDE = rect_to_nz([0, 4], [0, -2], 1)

A = sp.Matrix([EDGE[0], MERIDIAN[0]])    # rows: edge(gauge), meridian(flavor)
B = sp.Matrix([EDGE[1], MERIDIAN[1]])


def nz_symplectic_ok():
    """Neumann-Zagier theorem: A B^T is symmetric (the data is a valid Lagrangian)."""
    return (A * B.T) == (A * B.T).T


def cs_quadratic_form():
    """A^{-1} B = the CS quadratic form (symmetric); [[k_uu,k_um],[k_um,k_mm]] in the canonical frame."""
    return A.inv() * B


if __name__ == "__main__":
    print("=== B263 / Rung 1b: the CS structure of T[4_1] ===\n")
    for name, (Av, Bv, nu) in [("edge (gauge)", EDGE), ("meridian (flavor)", MERIDIAN), ("longitude", LONGITUDE)]:
        print(f"  {name:18}: A={Av}  B={Bv}  nu={nu}")
    print(f"\n  A B^T = {(A*B.T).tolist()}  symmetric: {nz_symplectic_ok()}   <-- valid Lagrangian (rigor gate)")
    CS = cs_quadratic_form()
    print(f"  A^(-1) B = {CS.tolist()}  symmetric: {CS == CS.T}")
    print(f"    k_uu (gauge)        = {CS[0,0]}  (bare; half-integer UV with the 2 chirals' parity shift)")
    print(f"    k_um (gauge-flavor) = {CS[0,1]}  <-- unit BF coupling: how the meridian m enters")
    print(f"    k_mm (flavor)       = {CS[1,1]}")
    assert nz_symplectic_ok() and CS == CS.T
    assert CS == sp.Matrix([[0, -1], [-1, 0]])
    print("\n  T[4_1] fully defined (this frame): U(1)_0 gauge, 2 chirals (charge +1), flavor U(1)_m via unit BF CS,")
    print("  monopole superpotential. CS levels FRAME-dependent (Sp(2,Z)); invariant = partition fn (Rung 3). PASS")
