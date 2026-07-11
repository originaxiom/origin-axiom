import sympy as sp
z = sp.symbols('z')
q5 = z**4 - 3*z**3 + 7*z**2 - 4*z + 4
print("d=5 quartic irreducible over Q:", sp.Poly(q5,z).is_irreducible)
K = sp.QQ.algebraic_field(sp.CRootOf(q5,0))  # not needed; use resultant approach for subfield
# quadratic subfield: does sqrt(5) generate it (splits over Q(sqrt5))? does sqrt(41)?
for d in [5, 41, -7, -3]:
    fac = sp.factor_list(q5, extension=sp.sqrt(d))[1]
    print(f"  over Q(sqrt({d})): factors into {[ (str(f),m) for f,m in fac]}  -> splits into quadratics: {all(sp.Poly(f,z).degree()<=2 for f,m in fac) and len(fac)>1}")
disc = sp.discriminant(sp.Poly(q5,z))
print("disc(d5 quartic) =", disc, "=", sp.factor(disc), " squarefree part:", sp.sign(disc)*sp.prod([p for p,e in sp.factorint(abs(disc)).items() if e%2]))
