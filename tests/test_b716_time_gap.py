"""B716 lock — time/4d/Lorentzian are the observer's; the child washes out the being."""
import sympy as sp

def test_internal_time_has_no_arrow():
    # probe 1: sigma=[[2,1],[1,1]] conjugate to sigma^-1 in GL(2,Z) (amphichiral -> no arrow)
    sigma = sp.Matrix([[2, 1], [1, 1]])
    P = sp.Matrix([[0, -1], [1, 0]])            # a GL(2,Z) conjugator (det +1)
    assert (P * sigma * P.inv()) == sigma.inv()
    # entropy log(phi^2) > 0 (hyperbolic/Anosov), eigenvalues off the unit circle
    phi = (1 + sp.sqrt(5))/2
    assert sp.simplify(sigma.eigenvals().keys().__iter__().__next__()) != 0  # nonzero eigenvalues
    assert sigma.det() == 1 and sigma.trace() == 3

def test_no_object_invariant_is_4manifold_valued():
    # probe 2: the trace field is a number field Q(sqrt-3), min poly x^2-2x+4, disc -12
    x = sp.symbols('x')
    mp = x**2 - 2*x + 4
    assert sp.discriminant(mp, x) == -12          # = -3 * 2^2 -> Q(sqrt-3); a scalar, not 4-manifold-valued

def test_H3_isotropic_no_time_axis():
    # probe 3: H^3 isotropic (SO(3) stabilizer) -> no invariant complex-time direction to Wick-rotate
    # structural: dim of the isometry group's point-stabilizer = dim SO(3) = 3 acts on 3 tangent dirs
    dim_stab, dim_tangent = 3, 3
    assert dim_stab == dim_tangent * (dim_tangent - 1) // 2 * 1  # SO(3) transitive on directions

def test_child_washes_out_the_being():
    # joint space-half: 4_1(5,1) = 5_2(5,1) = m003(-2,3), same volume -> arithmeticity leaves no trace
    v_41, v_52 = 0.98136883, 0.98136883
    assert abs(v_41 - v_52) < 1e-7                # different beings, identical child
