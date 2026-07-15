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

def get_system(word, kappa_val=-2):
    X,Y,Z = apply_word(word,(x,y,z))
    X,Y,Z = sp.expand(X), sp.expand(Y), sp.expand(Z)
    eq1 = sp.expand(X-x)
    eq2 = sp.expand(Y-y)
    eq3 = sp.expand(Z-z)
    constraint = sp.expand(x**2+y**2+z**2-x*y*z - kappa_val)
    return [eq1,eq2,constraint], (X,Y,Z)

if __name__=='__main__':
    import sys
    word = sys.argv[1] if len(sys.argv)>1 else 'RL'
    eqs, XYZ = get_system(word)
    print("Computing groebner basis (lex x>y>z)...")
    G = sp.groebner(eqs, z, y, x, order='lex')
    print(G)
