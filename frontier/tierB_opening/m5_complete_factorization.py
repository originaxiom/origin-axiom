import sympy as sp
x,y,z=sp.symbols('x y z')
def Lm(T,m):
    X,Y,Z=T; B=sp.Matrix([[0,1],[-1,Y]]); v=B**m*sp.Matrix([X,Z]); return (sp.expand(v[0]),Y,sp.expand(v[1]))
def Rm(T,m):
    X,Y,Z=T; A=sp.Matrix([[0,1],[-1,X]]); v=A**m*sp.Matrix([Y,Z]); return (X,sp.expand(v[0]),sp.expand(v[1]))
m=5
T=Rm(Lm((x,y,z),m),m)
eqs=[sp.expand(T[0]-x),sp.expand(T[1]-y),sp.expand(T[2]-z),sp.expand(x**2+y**2+z**2-x*y*z)]
G=sp.groebner(eqs,y,z,x,order='lex')
el=[g for g in G.exprs if g.free_symbols<={x}]
print("m=5 x-eliminant, ALL factors (closing cc3's 'is x^2+x-1 the only spurious one' fence):")
for p in el:
    for f,e in sp.factor_list(sp.expand(p))[1]:
        d=sp.degree(f,x)
        if d==1 and f.subs(x,0)==0:
            print(f"  deg {d}: {f}  -> TRIVIAL"); continue
        rts=sp.nroots(sp.Poly(f,x), n=20)
        ell=[r for r in rts if abs(sp.im(r))<1e-15 and abs(sp.re(r))<2]
        rl =[r for r in rts if abs(sp.im(r))<1e-15 and abs(sp.re(r))>=2]
        lox=[r for r in rts if abs(sp.im(r))>=1e-15]
        print(f"  deg {d}: irreducible={sp.Poly(f,x).is_irreducible}")
        print(f"      roots: {len(lox)} loxodromic(non-real), {len(ell)} ELLIPTIC(real |tr|<2), {len(rl)} real |tr|>=2")
        if d<=4: print(f"      poly: {sp.factor(f)}")
        if ell: print(f"      *** ELLIPTIC roots present -> component is NON-GEOMETRIC ***")
