import sympy as sp
from search import h1_trace, apply_word, MAPS

x,y,z = sp.symbols('x y z')

def analyze_word(word):
    X,Y,Z = apply_word(word,(x,y,z))
    X,Y,Z = sp.expand(X), sp.expand(Y), sp.expand(Z)
    constraint = sp.expand(x**2+y**2+z**2-x*y*z)  # tr[A,B]=-2
    eqs = [sp.expand(X-x), sp.expand(Y-y), constraint]
    sols = sp.solve(eqs, [x,y,z], dict=True)
    J = sp.Matrix([X,Y,Z]).jacobian([x,y,z])
    results=[]
    for s in sols:
        xv,yv,zv = s.get(x), s.get(y), s.get(z)
        if xv is None or xv.free_symbols: continue
        # skip trivial x=y=z=0
        if xv==0 and yv==0 and zv==0: continue
        Zcheck = sp.simplify(Z.subs(s)-zv)
        if Zcheck != 0: continue
        Js = J.subs(s)
        ev = Js.eigenvals()
        vals = list(ev.keys())
        sums = set()
        for i in range(len(vals)):
            for j in range(len(vals)):
                if i != j:
                    sums.add(sp.nsimplify(sp.simplify(vals[i]+vals[j])))
        results.append((s, ev, sums))
    return results

if __name__=='__main__':
    words = ['RL','R2L'.replace('2','')]  # placeholder
