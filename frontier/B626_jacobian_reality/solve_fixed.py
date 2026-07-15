import sympy as sp

x,y,z = sp.symbols('x y z')

def R(v):
    x,y,z = v
    return (x, z, x*z - y)

def L(v):
    x,y,z = v
    return (z, y, z*y - x)

def apply_word(word, v):
    for ch in word:
        if ch=='R':
            v = R(v)
        elif ch=='L':
            v = L(v)
    return v

def analyze(word, kappa=-2):
    X,Y,Z = apply_word(word,(x,y,z))
    X,Y,Z = sp.expand(X), sp.expand(Y), sp.expand(Z)
    constraint = sp.expand(x**2+y**2+z**2-x*y*z - kappa)
    eqs = [sp.expand(X-x), sp.expand(Y-y), sp.expand(Z-z), constraint]
    sols = sp.solve(eqs, [x,y,z], dict=True)
    results = []
    J = sp.Matrix([X,Y,Z]).jacobian([x,y,z])
    for s in sols:
        xv,yv,zv = s[x], s[y], s[z]
        if xv.free_symbols or yv.free_symbols or zv.free_symbols:
            continue
        Js = J.subs(s)
        Js = sp.nsimplify(Js)
        ev = Js.eigenvals()
        results.append((s, ev))
    return results, (X,Y,Z), J

if __name__=='__main__':
    import sys
    word = sys.argv[1] if len(sys.argv)>1 else 'RL'
    res, XYZ, J = analyze(word)
    print("word:",word,"num solutions:",len(res))
    for s,ev in res:
        print("sol:", s)
        print("eigenvalues:", ev)
        print("---")
