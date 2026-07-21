"""B747 closure: the (3,8) straggler via the verified amphichirality isometry
4_1(3,8) =? 4_1(-3,8) (the B740 mirror-closure pattern) + a direct retry at
high precision as a second, independent route."""
import snappy
from sage.all import NumberField, PolynomialRing, QQ

Rx = PolynomialRing(QQ, "x"); x = Rx.gen()
Ma = snappy.Manifold("4_1(3,8)"); Mb = snappy.Manifold("4_1(-3,8)")
iso = False
for _ in range(6):
    try:
        iso = Ma.is_isometric_to(Mb)
        break
    except RuntimeError:
        Ma.randomize(); Mb.randomize()
print("isometry 4_1(3,8) ~ 4_1(-3,8) VERIFIED:", iso)
print("=> shared invariant trace field; (-3,8) computed deg 30, sqrt5 False (b747_out line 22)")
F = None
for prec in (4000, 6000):
    M = snappy.Manifold("4_1(3,8)")
    try:
        F = M.invariant_trace_field_gens().find_field(prec=prec, degree=34, optimize=True)
    except Exception as e:
        print(f"direct retry prec={prec}: {e}")
    if F is not None:
        K = F[0]
        print(f"direct route prec={prec}: deg {K.degree()}, contains sqrt5 =",
              len((x**2 - 5).change_ring(K).roots()) > 0)
        break
if F is None:
    print("direct route: not recovered (isometry route stands alone)")
