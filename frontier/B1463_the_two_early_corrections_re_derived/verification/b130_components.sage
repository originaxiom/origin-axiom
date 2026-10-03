R.<x,y,z> = PolynomialRing(QQ, order='degrevlex')
def Ta(t): return (t[0], t[2], t[0]*t[2]-t[1])
def Tb(t): return (t[2], t[1], t[1]*t[2]-t[0])
def phi(m, t):
    for _ in range(m): t = Tb(t)
    for _ in range(m): t = Ta(t)
    return t
kap = lambda t: t[0]^2+t[1]^2+t[2]^2-t[0]*t[1]*t[2]-2
for m in (2,3,4):
    f = phi(m, (x,y,z)); J = R.ideal([f[0]-x, f[1]-y, f[2]-z])
    print("m =", m, " dim V(J) =", J.dimension())
    for Q in J.primary_decomposition():
        P = Q.radical()
        print("   component dim", P.dimension(), " degree", P.vector_space_dimension() if P.dimension()==0 else "-", " prime:", P.gens() if P.dimension()==0 or len(str(P.gens()))<160 else str(P.gens())[:160]+"...")
        if P.dimension()==0:
            for pt in P.variety(QQbar):
                print("        point", pt, " kappa =", kap((pt[x],pt[y],pt[z])))
