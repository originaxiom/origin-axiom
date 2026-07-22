import warnings; warnings.filterwarnings("ignore")
import snappy
from sage.all import PolynomialRing, QQ, NumberField, squarefree_part
Rx = PolynomialRing(QQ, "x"); x = Rx.gen()
# trace-7 classes: R^5 L (M51-class candidate) vs (RL)^2 (= m004's double cover)
for word, label in (("b++RRRRRL", "R^5L trace-7"), ("b++RLRL", "(RL)^2 trace-7 = the double cover"),
                    ("b++RRRRRRL", "R^6L trace-8 (M32-class)")):
    M = snappy.Manifold(word)
    vol = M.volume()
    A = M.alexander_polynomial()
    F = M.invariant_trace_field_gens().find_field(prec=1500, degree=16, optimize=True)
    if F is None:
        print(f"{label}: field not found"); continue
    K = F[0]; poly = Rx(K.defining_polynomial())
    fac = NumberField(poly, "a").ideal(5).factor()
    degs = sorted(P.residue_class_degree() for P, e in fac)
    print(f"{label} ({word}): vol {float(vol):.6f}, Alexander {A}, ITF deg {poly.degree()}, "
          f"field disc {K.discriminant()}, 5-residue-degrees {degs}")
M1, M2 = snappy.Manifold("b++RRRRRL"), snappy.Manifold("b++RLRL")
try:
    print("R^5L isometric to (RL)^2 (the cover)?", M1.is_isometric_to(M2))
except RuntimeError:
    print("isometry undecided at defaults")
print("Alexander disc check: trace 7 -> disc 45, squarefree part", squarefree_part(45),
      "(field Q(sqrt5), dilatation phi^4); trace 8 -> disc 60, squarefree part", squarefree_part(60))
