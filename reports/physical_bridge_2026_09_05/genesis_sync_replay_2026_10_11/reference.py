"""Separate-method local safeguards; no imports from genesis producers."""
import json
import sympy as s

facts = {}
def check(name, value):
    assert name not in facts
    facts[name] = bool(value)
    assert facts[name], name

def equal(a, b):
    return (a-b).applyfunc(s.expand) == s.zeros(*a.shape)

def inverse_word(w):
    return w[::-1].swapcase()

def comm(a, b):
    return a+b+inverse_word(a)+inverse_word(b)

def reduce_word(w):
    while True:
        previous = w
        for pair in ("aA", "Aa", "bB", "Bb"):
            w = w.replace(pair, "")
        if w == previous:
            return w

def affine_word(w, A, B, ua, ub):
    # Direct pairs, with symbolic coordinates; no Fox/chart helper imported.
    I = s.eye(2)
    reps = {"a": A, "b": B, "A": A.inv(), "B": B.inv()}
    shifts = {"a": ua, "b": ub, "A": -A.inv()*ua, "B": -B.inv()*ub}
    R, z = I, s.zeros(2, 1)
    for letter in w:
        z = z + R*shifts[letter]
        R = R*reps[letter]
    return R, z.applyfunc(s.expand)

c = comm("a", "b")
r = comm(c, "a"+c+"A")
t = comm(r, "a"+r+"A")
check("nonempty_second_derived_word", reduce_word(r) != "")
check("nonempty_third_derived_word", reduce_word(t) != "")
u = s.symbols("u0:4")
ua, ub = s.Matrix(u[:2]), s.Matrix(u[2:])
for i, (pa, pb) in enumerate(((0,0), (1,0), (0,1), (1,1))):
    A = (-1)**pa*s.diag(s.I, -s.I)
    B = (-1)**pb*s.Matrix([[0,1],[-1,0]])
    normalized = ub - (B-s.eye(2))*(A-s.eye(2)).inv()*ua
    Rr, zr = affine_word(r, A, B, ua, ub)
    Rt, zt = affine_word(t, A, B, ua, ub)
    check(f"r_image_{i}", equal(Rr, s.eye(2)))
    check(f"r_all_coordinate_chart_{i}", equal(zr, 4*normalized))
    check(f"t_image_{i}", equal(Rt, s.eye(2)))
    check(f"t_all_coordinates_invisible_{i}", equal(zt, s.zeros(2,1)))
    concrete = zr.subs(dict(zip(u, (0,0,1,0))))
    check(f"r_nonzero_opposing_control_{i}", not equal(concrete, s.zeros(2,1)))

x, flux = s.symbols("x flux", real=True)
y, coupling = s.symbols("y coupling", positive=True)
phi = 12*flux*s.log(y)
Fxy = s.expand(s.I*(s.diff(phi,x,2)+s.diff(phi,y,2))/2)
def scalar_equal(name, a, b):
    check(name, s.simplify(a-b) == 0)
scalar_equal("curvature_for_arbitrary_real_flux", Fxy, -6*s.I*flux/y**2)
scalar_equal("bulk_YM_star_constant", s.diff(Fxy*y**2,y), 0)
area = s.pi/3  # independently inspected fundamental-region area proof, not reproved here
measured = s.simplify(s.I*Fxy*y**2*area/(2*s.pi))
energy = s.simplify(s.conjugate(Fxy*y**2)*(Fxy*y**2)*area/(2*coupling**2))
scalar_equal("effective_flux", measured, flux)
scalar_equal("fixed_sector_energy", energy, 6*s.pi*flux**2/coupling**2)
check("zero_energy_less_than_unit", (energy.subs(flux,1)-energy.subs(flux,0)).is_positive)
scalar_equal("open_half_flux_control", measured.subs(flux,s.Rational(1,2)), s.Rational(1,2))
bad_F = s.I*s.diff(y**2,y,2)/2
check("nonharmonic_metric_fails_YM", s.diff(bad_F*y**2,y) != 0)
harmonic = x**2-y**2
scalar_equal("harmonic_metric_preserves_curvature",
             s.I*(s.diff(harmonic,x,2)+s.diff(harmonic,y,2))/2, 0)
assert len(facts) == 30, ("unexpected reference count", len(facts))
print(json.dumps({"status":"PASS","exact_local_checks":len(facts),"facts":facts,
    "scope":"arbitrary symbolic cocycle coordinates and conditional open-base local curvature",
    "independent_producer_imports":False,"full_genesis_or_physics_certificate":False},indent=2))

