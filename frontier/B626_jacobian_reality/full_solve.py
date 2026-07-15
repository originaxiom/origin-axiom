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

# check invariance of kappa under R
kappa = lambda x,y,z: x**2+y**2+z**2-x*y*z
kR = sp.expand(kappa(*R((x,y,z))) - kappa(x,y,z))
kL = sp.expand(kappa(*L((x,y,z))) - kappa(x,y,z))
print("kappa invariance under R:", kR)
print("kappa invariance under L:", kL)
