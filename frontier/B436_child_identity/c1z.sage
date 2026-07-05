import snappy
M = snappy.ManifoldHP('4_1'); M.dehn_fill((5,1))
volhp = M.volume()
RF = RealField(260)
R.<x> = QQ[]
K.<a> = NumberField(x^4 - x - 1)
L = K.zeta_function(prec=260)
zK2 = RF(L(2))
pred = RF(283)**(RF(3)/2) * zK2 / (RF(4)*RF(pi)**2)**3
ratio = RF(volhp)/pred
print("zeta_K(2) @260bits:", zK2)
print("ratio:", ratio)
print("|ratio - 12| =", abs(ratio - 12))
