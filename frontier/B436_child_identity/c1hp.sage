import snappy, math
M = snappy.ManifoldHP('4_1'); M.dehn_fill((5,1))
volhp = M.volume()
print("HP vol(child):", volhp)
RF = RealField(400)
R.<x> = QQ[]
K.<a> = NumberField(x^4 - x - 1)
zK2 = RF(K.zeta_function()(2))
pred = RF(283)**(RF(3)/2) * zK2 / (RF(4)*RF(pi)**2)**3
ratio = RF(volhp)/pred
print("HP ratio vol/pred:", ratio)
print("|ratio - 12| =", abs(ratio - 12))
# CS at high precision + honest scan vs vol-normalized combos
M0hp = snappy.ManifoldHP("4_1"); M0hp.chern_simons(); M0hp.dehn_fill((5,1)); cshp = M0hp.chern_simons()
print("HP CS:", cshp)
# sibling control: trace field degree bound push
S = snappy.Manifold('4_1'); S.dehn_fill((7,1))
try:
    res = S.trace_field_gens().find_field(prec=600, degree=14, optimize=True)
    print("sibling field (deg<=14):", res[1] if isinstance(res,tuple) else res)
except Exception as e:
    print("sibling: no field at deg<=14 ->", type(e).__name__)
