# B440 (C3 foreign control) -- the SL(2,C) character variety of the CLOSED manifolds K(5,1),
# computed convention-free from pi_1: A=[[m,1],[0,mi]], B=[[k,0],[t,ki]], both relators = I,
# eliminate to the meridian trace x = tr(A). Emits charvar.json for the pyenv-side verifier.
# Reproduces 4_1's B439 A-polynomial quartic by a wholly independent method.
import snappy, json, os
def build(name):
    G = snappy.Manifold(name).fundamental_group(); rels = G.relators()
    R = PolynomialRing(QQ, ['m','mi','k','ki','t','x']); m,mi,k,ki,t,x = R.gens()
    Mat = MatrixSpace(R.fraction_field(), 2)
    A=Mat([[m,1],[0,mi]]); Ai=Mat([[mi,-1],[0,m]]); B=Mat([[k,0],[t,ki]]); Bi=Mat([[ki,0],[-t,k]])
    lett={'a':A,'A':Ai,'b':B,'B':Bi}
    def word(w):
        P=Mat.one()
        for ch in w: P=P*lett[ch]
        return P
    polys=[m*mi-1,k*ki-1,x-(m+mi)]
    for w in rels:
        P=word(w)
        for i in range(2):
            for j in range(2):
                polys.append(R((P[i,j]-(1 if i==j else 0)).numerator()))
    return R.ideal(polys), R, x
out={}
for name in ['4_1(5,1)','5_2(5,1)','6_1(5,1)','3_1(5,1)']:
    I,R,x = build(name)
    E = I.elimination_ideal([g for g in R.gens() if g!=x])
    gens=[g for g in E.gens() if g!=0 and g.degree(x)>0]
    S.<X>=PolynomialRing(QQ); g=min(gens,key=lambda p:p.degree())
    gx=S(g.polynomial(x)); gx=gx/gx.leading_coefficient()
    facs=[[str(f).replace('X','x'), int(f.degree()), (int(f.discriminant()) if f.degree()>=2 else None)]
          for f,mtail in gx.factor()]
    out[name]=dict(trace_poly=str(gx).replace('X','x'), total_vacua=int(gx.degree()), factors=facs)
    print(name, "->", out[name]['total_vacua'], "vacua;", [ (f[1],f[2]) for f in facs])
json.dump(out, open("frontier/B440_foreign_vacuum_control/charvar.json","w"), indent=1)
print("[written] charvar.json")
