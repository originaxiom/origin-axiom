import sympy as sp

x,y,z = sp.symbols('x y z')

def R(v):
    x,y,z = v
    return (x, z, x*z - y)

def L(v):
    x,y,z = v
    return (z, y, z*y - x)

def apply_word(word, v):
    # word is string of 'R','L', applied left to right as composition order
    # We need to decide composition convention; apply letters left-to-right meaning
    # first letter applied first? We'll test both and calibrate with fig-8.
    for ch in word:
        if ch=='R':
            v = R(v)
        elif ch=='L':
            v = L(v)
    return v

def fixed_point_system(word):
    X,Y,Z = apply_word(word, (x,y,z))
    return sp.Poly(sp.expand(X-x)), (X,Y,Z)

# test word RL
X,Y,Z = apply_word('RL',(x,y,z))
print("RL image:", sp.expand(X), sp.expand(Y), sp.expand(Z))
