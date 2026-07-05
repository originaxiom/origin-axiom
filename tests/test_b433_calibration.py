"""Locks for B433 -- the SL(2) 3d-3d calibration. The sage/snappy run (calibration.sage) is the
provenance for divisibility: under (M^2,L^2) the DGG eliminant = -A_CL(M,L)*A_CL(M,-L), and the
three wrong conventions fail. Here we lock the exact algebraic identities that adjudication used."""
import sympy as sp

M, L = sp.symbols("M L")
CL = M**4*L**2 + (-M**8 + M**6 + 2*M**4 + M**2 - 1)*L + M**4          # banked B67 Cooper-Long
COF = M**4*L**2 + (M**8 - M**6 - 2*M**4 - M**2 + 1)*L + M**4          # computed sage cofactor


def test_cofactor_is_exactly_the_sign_twisted_lift():
    # the cofactor the sage elimination produced IS A_CL(M, -L): the second SL(2) lift
    assert sp.expand(COF - CL.subs(L, -L)) == 0


def test_the_two_lifts_are_distinct_components():
    # A_CL(M,L) and A_CL(M,-L) are coprime (genuinely two components, not a square)
    assert sp.gcd(CL, COF) == 1
