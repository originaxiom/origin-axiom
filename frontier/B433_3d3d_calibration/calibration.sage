import snappy
M = snappy.Manifold('4_1')
G = M.gluing_equations()
R.<z,w,Mv,Lv> = QQ[]
F = R.fraction_field()
def rowexpr(row):
    a1,b1,c1,a2,b2,c2 = row
    return (F(z)^a1 * F(1/(1-z))^b1 * F((z-1)/z)^c1 *
            F(w)^a2 * F(1/(1-w))^b2 * F((w-1)/w)^c2)
CL = Mv^4*Lv^2 + (-Mv^8+Mv^6+2*Mv^4+Mv^2-1)*Lv + Mv^4     # banked B67 Cooper-Long
for mexp, lexp, tag in [(2,1,"M^2,L"),(2,2,"M^2,L^2"),(1,1,"M,L"),(1,2,"M,L^2")]:
    I = R.ideal([ (rowexpr(G[0])-1).numerator(),
                  (rowexpr(G[2])-Mv^mexp).numerator(),
                  (rowexpr(G[3])-Lv^lexp).numerator() ])
    E = I.elimination_ideal([z,w])
    g = E.gens()[0]
    # containment: does Cooper-Long divide the eliminant (curve contained in DGG variety)?
    q, r = g.quo_rem(CL)
    print(tag, ": CL divides eliminant:", r == 0,
          ("cofactor: "+str(factor(q)) if r == 0 else ""))
