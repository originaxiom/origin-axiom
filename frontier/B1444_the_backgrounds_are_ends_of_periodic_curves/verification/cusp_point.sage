# The complete-cusp point of the root's twisted period-3 curve, by machine.
import json
R.<t> = QQ[]
K.<a> = NumberField(t^4 - t^2 + 4)          # try: field containing sqrt5 and sqrt(-3):  a = (sqrt5 + sqrt(-3))/2 has a^2 = (1 + sqrt(-15))/2
print("a^2 satisfies:", (a^2).minpoly(), "  disc of field:", K.disc().factor(), "  is Galois:", K.is_galois())
print("sqrt5 in K:", K(5).is_square(), "  sqrt(-3) in K:", K(-3).is_square(), "  sqrt(-15) in K:", K(-15).is_square())
w = a^2; assert w^2 - w + 4 == 0
out = []
for sgn in (1, -1):
    u = (w + sgn * a) / 2
    assert u - 1/u == w
    X = u - 1; Z2 = 1 + 1/u^2; kap = X^2 + 2*Z2 + X*Z2 - 2          # Y = -Z:  X^2 + Y^2 + Z^2 - XYZ - 2 = X^2 + 2 Z^2 + X Z^2 - 2
    mm = -w*(w^2 - w + 4)
    N1 = 4*(u - 1)^2*(u + 1)                # tau tau' for the generation family (a = (0, j))
    E2 = 4 - N1                             # E^2
    rec = dict(sign=int(sgn), u_minpoly=str(u.minpoly()), X_minpoly=str(X.minpoly()), Zsq_minpoly=str(Z2.minpoly()), kappa=str(kap), m_plus_inv_minus_2=str(mm),
               tau_tauprime_minpoly=str(N1.minpoly()), E_squared_minpoly=str(E2.minpoly()), E_squared_is_square_in_K=bool(E2.is_square()), Zsq_is_square_in_K=bool(Z2.is_square()))
    out.append(rec); print(json.dumps(rec, indent=1))
json.dump(out, open("cusp_point.json", "w"), indent=1)
