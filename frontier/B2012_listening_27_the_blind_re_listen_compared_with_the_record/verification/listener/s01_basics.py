# s01_basics.py -- exact symbolic checks of the moves (sympy)
import sympy as sp
x, y, z = sp.symbols('x y z')

def L(p):  x, y, z = p; return (x, z, sp.expand(x*z - y))
def R(p):  x, y, z = p; return (z, y, sp.expand(y*z - x))
def Li(p): x, y, z = p; return (x, sp.expand(x*y - z), y)
def Ri(p): x, y, z = p; return (sp.expand(x*y - z), y, x)

P = (x, y, z)
k = lambda p: sp.expand(p[0]**2 + p[1]**2 + p[2]**2 - p[0]*p[1]*p[2])
print("k invariant under L,R,Li,Ri:", [sp.expand(k(f(P)) - k(P)) == 0 for f in (L, R, Li, Ri)])
print("L Li = id:", tuple(sp.expand(c) for c in L(Li(P))) == P, " Li L = id:", tuple(sp.expand(c) for c in Li(L(P))) == P)
print("R Ri = id:", tuple(sp.expand(c) for c in R(Ri(P))) == P, " Ri R = id:", tuple(sp.expand(c) for c in Ri(R(P))) == P)

def word(w, p):
    # w is a string read left to right as composition: "LR" means apply R first then L (function composition L(R(p)))
    f = {'L': L, 'R': R, 'l': Li, 'r': Ri}
    for c in reversed(w):
        p = f[c](p)
    return tuple(sp.expand(c) for c in p)

for w in ["Lr", "rL", "LrL", "rLr", "Lrl", "LrLr", "LrLrLr", "LrLLrL", "LRl", "lR"]:
    print(w, "->", word(w, P))
print("braid L r L == r L r :", word("LrL", P) == word("rLr", P))
print("(L r)^3 == id :", word("LrLrLr", P) == P)
print("(L r L)^2 == id :", word("LrLLrL", P) == P)

# swap symmetry tau(x,y,z)=(y,x,z): tau L tau == R ?
tau = lambda p: (p[1], p[0], p[2])
print("tau L tau == R:", tau(L(tau(P))) == R(P), "  tau R tau == L:", tau(R(tau(P))) == L(P))
# sign changes
sig = {'s12': lambda p: (-p[0], -p[1], p[2]), 's13': lambda p: (-p[0], p[1], -p[2]), 's23': lambda p: (p[0], -p[1], -p[2])}
for nm, s in sig.items():
    for mn, M in (('L', L), ('R', R)):
        lhs = M(s(P))
        found = [n2 for n2, s2 in sig.items() if tuple(sp.expand(c) for c in s2(M(P))) == tuple(sp.expand(c) for c in lhs)]
        print(f"{mn} o {nm} = {found} o {mn}")

# fixed points of L and R together
sol = sp.solve([L(P)[i] - P[i] for i in range(3)] + [R(P)[i] - P[i] for i in range(3)], [x, y, z], dict=True)
print("common fixed points over C:", sol, [k((s[x], s[y], s[z])) for s in sol])
# singular points of the leaves
g = [sp.diff(k(P), v) for v in (x, y, z)]
sol2 = sp.solve(g, [x, y, z], dict=True)
print("critical points of k:", sol2, "k values:", [k((s[x], s[y], s[z])) for s in sol2])
# fixed points of L alone
sol3 = sp.solve([L(P)[i] - P[i] for i in range(3)], [x, y, z], dict=True)
print("fixed set of L:", sol3)
