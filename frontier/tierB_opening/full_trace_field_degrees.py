import sympy as sp
x,y,z,t = sp.symbols('x y z t')
def Lm(T,m):
    X,Y,Z=T; B=sp.Matrix([[0,1],[-1,Y]]); v=B**m*sp.Matrix([X,Z]); return (sp.expand(v[0]),Y,sp.expand(v[1]))
def Rm(T,m):
    X,Y,Z=T; A=sp.Matrix([[0,1],[-1,X]]); v=A**m*sp.Matrix([Y,Z]); return (X,sp.expand(v[0]),sp.expand(v[1]))
print("m | deg Q(x) | deg Q(x,y,z) via primitive element t=x+2y+3z")
for m in (1,2,3):
    T=Rm(Lm((x,y,z),m),m)
    eqs=[sp.expand(T[0]-x),sp.expand(T[1]-y),sp.expand(T[2]-z),sp.expand(x**2+y**2+z**2-x*y*z)]
    # deg Q(x): geometric factor of the x-eliminant
    Gx=sp.groebner(eqs,y,z,x,order='lex')
    el=[g for g in Gx.exprs if g.free_symbols<={x}]
    dx=[]
    for p in el:
        for f,e in sp.factor_list(sp.expand(p))[1]:
            d=sp.degree(f,x)
            if d==1 and f.subs(x,0)==0: continue          # trivial x
            rts=sp.Poly(f,x).all_roots() if d<=2 else None
            # elliptic test only meaningful for low degree; keep all, mark
            dx.append(d)
    # primitive element: add t - (x+2y+3z), eliminate x,y,z
    G2=sp.groebner(eqs+[t-(x+2*y+3*z)], x,y,z,t, order='lex')
    elt=[g for g in G2.exprs if g.free_symbols<={t}]
    dt=[]
    for p in elt:
        for f,e in sp.factor_list(sp.expand(p))[1]:
            d=sp.degree(f,t)
            if d==0: continue
            dt.append((d, sp.factor(f)))
    print(f"{m} | {sorted(dx)} | {[d for d,_ in sorted(dt)]}")
    for d,f in sorted(dt):
        if d<=2: print(f"     low-deg t-factor: {f}")
