import snappy
z = CC(-0.24812606280262192, 1.0339820609759678)
for d in (2,3,4):
    p = algdep(z, d)
    print(f"deg {d}: {p}   |p(z)| = {abs(p(z)):.2e}")
p = algdep(z, 4)
K.<a> = NumberField(p)
print("disc:", K.discriminant().factor())
print("quadratic subfields:", [f[0].defining_polynomial() for f in K.subfields(2)])
Mh = snappy.Manifold('4_1'); Mh.chern_simons(); Mh.dehn_fill((5,1))
print("CS(4_1(5,1)) =", Mh.chern_simons())
