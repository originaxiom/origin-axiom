"""B722 lock — resurgence: two phases=being/hearing (rung 1); continuum arithmetically rigid over Q(sqrt-3)."""
import mpmath as mp, sympy as sp

def test_two_phases_carry_the_two_fields():
    t = sp.symbols('t')
    assert sp.discriminant(t**2 - t + 1, t) == -3     # phase 1: volume/A-poly -> Q(sqrt-3) BEING
    assert sp.discriminant(t**2 - 3*t + 1, t) == 5     # phase 2: Alexander -> Q(sqrt5) HEARING

def test_alexander_inside_apoly_L1_slice():
    M = sp.symbols('M')
    A1 = M**8 - M**6 - 4*M**4 - M**2 + 1                # fig-8 A-polynomial at L=1
    # A(M,1) = (M^2+1)^2 * Delta(M^2), Delta=t^2-3t+1 the Alexander poly (both faces in one A-poly)
    assert sp.expand(A1 - (M**2 + 1)**2 * (M**4 - 3*M**2 + 1)) == 0
    assert sp.rem(A1, M**4 - 3*M**2 + 1, M) == 0        # Delta(M^2) divides the A-poly slice

def test_one_loop_is_trace_field_discriminant_sqrt_minus3():
    # Phi''(t*) at the saddle t*=i pi/3 equals sqrt(-3) -> coefficients forced into Q(sqrt-3): RIGID
    mp.mp.dps = 30
    tstar = 1j*mp.pi/3; et = mp.e**tstar
    d2 = -(et + 1)/(et - 1)                            # Phi''(t) = -(e^t+1)/(e^t-1)
    assert abs(d2 - 1j*mp.sqrt(3)) < 1e-25             # = sqrt(-3), the trace-field discriminant
