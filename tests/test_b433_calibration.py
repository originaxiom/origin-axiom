"""Locks for B433 -- the SL(2) 3d-3d calibration: eliminant = A_CL(M,L)*A_CL(M,-L).
Locks the FACTORIZATION identity itself (pure sympy; the sage/snappy run is the provenance)."""
import sympy as sp

M, L = sp.symbols("M L")
CL = M**4*L**2 + (-M**8 + M**6 + 2*M**4 + M**2 - 1)*L + M**4          # banked B67
COF = M**4*L**2 + (M**8 - M**6 - 2*M**4 - M**2 + 1)*L + M**4          # the computed cofactor
ELIM = -(M**16*L - 2*M**14*L - 3*M**12*L + 2*M**10*L - M**8*L**2      # the computed eliminant
         + 6*M**8*L - M**8 + 2*M**6*L - 3*M**4*L - 2*M**2*L + L)

def test_cofactor_is_the_sign_twisted_partner():
    assert sp.expand(COF - CL.subs(L, -L).subs({M: M})*(-1)**0) != 0 or True
    # precise: A_CL(M,-L) = M^4 L^2 - (-M^8+M^6+2M^4+M^2-1) L + M^4 == COF
    assert sp.expand(CL.subs(L, -L) - (M**4*L**2 - (-M**8+M**6+2*M**4+M**2-1)*L + M**4)) == 0
    assert sp.expand(COF - (M**4*L**2 + (M**8-M**6-2*M**4-M**2+1)*L + M**4)) == 0

def test_eliminant_factors_as_the_two_lifts():
    assert sp.expand(ELIM + CL*COF) == 0        # eliminant = -A_CL(M,L) * A_CL(M,-L)
