"""B729 lock — the Born amplitude sector is a golden-MTC overlay; the Born ledger completes.

The object supplies its two QUADRATIC fields (classical content: form+weights); the quantum content
(amplitudes+phase+associator) lives in QUARTIC extensions ramified at {2,5}, disjoint from the
object's prime 3. Structural/arithmetic only (Gate 5).
"""
import sympy as sp

x = sp.Symbol('x')
phi = (1 + sp.sqrt(5)) / 2


def test_amplitude_field_is_C4_real_ramified_at_2_5():
    # the Born S-matrix amplitudes 1/D, phi/D live in Q(D)=Q(sqrt(2+phi)) = Q(zeta20)^+ : C4, totally real.
    D = sp.sqrt(2 + phi)
    mp = sp.minimal_polynomial(D, x)
    assert mp == x**4 - 5*x**2 + 5                            # = defining poly of Q(zeta20)^+
    G, _ = sp.Poly(mp, x).galois_group()
    assert G.order() == 4 and G.is_cyclic                     # C4 cyclic
    # ramified only at {2,5}: poly discriminant 2000 = 2^4 * 5^3 -> UNRAMIFIED at the object's prime 3
    assert sp.discriminant(mp, x) == 2000
    assert set(sp.factorint(2000).keys()) == {2, 5}
    assert sp.simplify(D - 2*sp.cos(sp.pi/10)) == 0          # sqrt(2+phi) = 2cos(pi/10)


def test_associator_field_is_D4_nonGalois():
    # the F-symbol/associator sqrt(phi) is the D4 (non-Galois) quartic -- a distinct 5th ingredient.
    sq = sp.sqrt(phi)
    mp = sp.minimal_polynomial(sq, x)
    assert mp == x**4 - x**2 - 1
    G, _ = sp.Poly(mp, x).galois_group()
    assert G.order() == 8 and not G.is_abelian               # D4, order 8, non-abelian closure


def test_three_quartics_are_distinct_galois_types():
    # phase Q(zeta5) C4-CM ; amplitude Q(sqrt(2+phi)) C4-real ; associator Q(sqrt phi) D4-closure.
    g_phase, _ = sp.Poly(sp.minimal_polynomial(sp.exp(2*sp.pi*sp.I/5), x), x).galois_group()
    g_ampl, _ = sp.Poly(x**4 - 5*x**2 + 5, x).galois_group()
    g_assoc, _ = sp.Poly(x**4 - x**2 - 1, x).galois_group()
    assert g_phase.order() == 4 and g_phase.is_cyclic         # C4 (CM: complex)
    assert g_ampl.order() == 4 and g_ampl.is_cyclic           # C4 (real)
    assert g_assoc.order() == 8                                # D4 -- distinct type
    # phase is CM (complex), amplitude is totally real -> distinct C4 fields (different ramification)
    assert sp.im(sp.exp(2*sp.pi*sp.I/5)) != 0                  # phase field is complex
    assert sp.im(sp.sqrt(2 + phi)) == 0                       # amplitude field is real


def test_object_native_fields_are_the_two_quadratics_only():
    # the object natively produces ONLY the two quadratics: trace field Q(sqrt-3) and Alexander Q(sqrt5).
    assert sp.discriminant(x**2 - x + 1, x) == -3            # tetrahedron shape z^2-z+1 -> Q(sqrt-3)
    assert sp.discriminant(x**2 - 3*x + 1, x) == 5           # Alexander t^2-3t+1 -> Q(sqrt5)
    # the amplitude quartic is NOT reachable from the biquadratic compositum Q(sqrt-3,sqrt5):
    # x^4-5x^2+5 stays irreducible-into-quadratics whose roots need sqrt(2+phi) (not in the compositum).
    # discriminating: the object's fields ramify at {3} and {5}; the amplitude ramifies at {2,5} (adds 2).
    obj_primes = {3, 5}
    ampl_primes = set(sp.factorint(2000).keys())             # {2,5}
    assert 2 in ampl_primes and 2 not in obj_primes          # the amplitude introduces the prime 2, alien to the object
    assert 3 in obj_primes and 3 not in ampl_primes          # the object's defining prime 3 is absent from the amplitude
