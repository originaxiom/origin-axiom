import warnings; warnings.filterwarnings("ignore")
import snappy
from sage.all import PolynomialRing, QQ, NumberField
Rx = PolynomialRing(QQ, "x"); x = Rx.gen()
for name in ("m022", "m009", "m039"):
    M = snappy.Manifold(name)
    K = M.invariant_trace_field_gens().find_field(prec=800, degree=12, optimize=True)[0]
    poly = Rx(K.defining_polynomial())
    deg = poly.degree()
    print(f"{name}: ITF degree {deg}, poly {poly}, field disc {K.discriminant()}")
    fac = NumberField(poly, "a").ideal(5).factor()
    degs = sorted(P.residue_class_degree() for P, e in fac)
    print(f"   5 factorization residue degrees: {degs} -> "
          f"{'TOTALLY INERT' if degs == [deg] else 'split/mixed'}")
    A = M.alexander_polynomial()
    print(f"   Alexander: {A}")
