import sympy as sp
x,y,z = sp.symbols('x y z')

def Lm(t, m):           # L^m : y fixed, (x,z) -> B^m (x,z),  B=[[0,1],[-1,y]]
    X,Y,Z = t
    B = sp.Matrix([[0,1],[-1,Y]])
    v = B**m * sp.Matrix([X,Z])
    return (sp.expand(v[0]), Y, sp.expand(v[1]))

def Rm(t, m):           # R^m : x fixed, (y,z) -> A^m (y,z),  A=[[0,1],[-1,x]]
    X,Y,Z = t
    A = sp.Matrix([[0,1],[-1,X]])
    v = A**m * sp.Matrix([Y,Z])
    return (X, sp.expand(v[0]), sp.expand(v[1]))

def classify(tr):
    tr = sp.nsimplify(sp.simplify(tr))
    if sp.simplify(sp.im(tr)) != 0: return "LOXODROMIC (non-real trace)"
    r = float(sp.re(tr))
    return f"ELLIPTIC (real, |tr|={abs(r):.4f} < 2)" if abs(r)<2 else f"hyp/par (real, |tr|={abs(r):.4f})"

for m in (1,2,3):
    M = sp.Matrix([[1,1],[0,1]])**m * sp.Matrix([[1,0],[1,1]])**m
    print(f"\n===== m={m}:  phi_m^2 = R^{m}L^{m} = {M.tolist()}, trace {sp.trace(M)} =====")
    t = Rm(Lm((x,y,z), m), m)
    eqs = [sp.expand(t[0]-x), sp.expand(t[1]-y), sp.expand(t[2]-z),
           sp.expand(x**2+y**2+z**2-x*y*z)]
    G = sp.groebner(eqs, y, z, x, order='lex')
    elim = [sp.factor(g) for g in G.exprs if g.free_symbols <= {x}]
    print("   eliminant(s) in x:", elim if elim else "(none pure-x)")
    for p in elim:
        for r in sp.roots(sp.Poly(sp.expand(p), x), multiple=True):
            r = sp.simplify(r)
            if r == 0: continue
            mp = sp.minimal_polynomial(r, x)
            print(f"     x={sp.nsimplify(r)}  deg={sp.degree(mp,x)}  minpoly={mp}")
            print(f"        {classify(r)}")
