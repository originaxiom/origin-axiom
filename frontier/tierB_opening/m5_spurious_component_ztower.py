import sympy as sp
x,y,z=sp.symbols('x y z')
def Lm(T,m):
    X,Y,Z=T; B=sp.Matrix([[0,1],[-1,Y]]); v=B**m*sp.Matrix([X,Z]); return (sp.expand(v[0]),Y,sp.expand(v[1]))
def Rm(T,m):
    X,Y,Z=T; A=sp.Matrix([[0,1],[-1,X]]); v=A**m*sp.Matrix([Y,Z]); return (X,sp.expand(v[0]),sp.expand(v[1]))
m=5
T=Rm(Lm((x,y,z),m),m)
eqs=[sp.expand(T[0]-x),sp.expand(T[1]-y),sp.expand(T[2]-z),sp.expand(x**2+y**2+z**2-x*y*z)]
# restrict to the spurious component x^2+x-1=0, then eliminate to z
G=sp.groebner(eqs+[x**2+x-1], x, y, z, order='lex')
zel=[g for g in G.exprs if g.free_symbols<={z}]
print("m=5, on the component x^2+x-1=0:")
print("  z-eliminant factors:", [sp.factor(p) for p in zel] if zel else "(none pure-z)")
for p in zel:
    for f,e in sp.factor_list(sp.expand(p))[1]:
        d=sp.degree(f,z)
        rts=sp.roots(sp.Poly(f,z))
        print(f"   z-factor deg {d}: {sp.factor(f)}")
        for r in rts:
            r=sp.simplify(r); im=sp.simplify(sp.im(r))
            kind="LOXODROMIC" if im!=0 else ("ELLIPTIC" if abs(float(sp.re(r)))<2 else "hyp/par")
            print(f"      z = {sp.nsimplify(r)}  ({kind})")
print()
print("x-roots on this component:", [sp.nsimplify(r) for r in sp.roots(sp.Poly(x**2+x-1,x))])
