import sympy as sp
import itertools

x,y,z = sp.symbols('x y z')

def R(v):
    x,y,z = v
    return (x, z, x*z - y)
def Ri(v):
    x,y,z = v
    return (x, x*y-z, y)
def L(v):
    x,y,z = v
    return (z, y, z*y - x)
def Li(v):
    x,y,z = v
    return (x*y-z, y, x)

MAPS = {'R':R,'L':L,'r':Ri,'l':Li}
M2 = {
 'R': sp.Matrix([[1,1],[0,1]]),
 'L': sp.Matrix([[1,0],[1,1]]),
}
M2['r'] = M2['R'].inv()
M2['l'] = M2['L'].inv()

def apply_word(word, v):
    for ch in word:
        v = MAPS[ch](v)
    return v

def h1_matrix(word):
    Mtot = sp.eye(2)
    for ch in word:
        Mtot = M2[ch]*Mtot   # leftmost applied first => total = M_last*...*M_first
    return Mtot

def h1_trace(word):
    return h1_matrix(word).trace()

def find_fixed_J(word, kappa_val, sx, sy):
    X,Y,Z = apply_word(word,(x,y,z))
    X,Y,Z = sp.expand(X), sp.expand(Y), sp.expand(Z)
    sz = sx*sy
    constraint = sp.expand(x**2+y**2+z**2-x*y*z - kappa_val)
    eqs = [sp.expand(X-sx*x), sp.expand(Y-sy*y), constraint]
    try:
        sols = sp.solve(eqs,[x,y,z],dict=True)
    except Exception as e:
        return []
    Jmat = sp.Matrix([X,Y,Z]).jacobian([x,y,z])
    # adjust jacobian for sign map derivative: fixed pt of (X,Y,Z) - (sx x, sy y, sz z)=0
    Jmat2 = Jmat - sp.diag(sx,sy,sz)
    out = []
    for s in sols:
        xv,yv,zv = s.get(x), s.get(y), s.get(z)
        if xv is None or yv is None or zv is None: continue
        if xv.free_symbols or yv.free_symbols or zv.free_symbols: continue
        zcheck = sp.simplify(Z.subs(s) - sz*zv)
        if zcheck != 0: continue
        Js = sp.Matrix([X,Y,Z]).jacobian([x,y,z]).subs(s)
        # eigen of the map v -> M v where at fixed pt of X=sx x etc, consider derivative of (X,Y,Z) w.r.t (x,y,z) directly (call it Dmap)
        ev = Js.eigenvals()
        out.append((s, ev, sx,sy,sz))
    return out

# search short words with trace 3
words = []
for length in range(2,5):
    for combo in itertools.product('RLrl', repeat=length):
        w = ''.join(combo)
        words.append(w)

target_trace = 3
candidates = []
for w in words:
    t = h1_trace(w)
    if t == target_trace or t == -target_trace:
        candidates.append(w)

print("candidates with |trace|=3, count:", len(candidates))
print(candidates[:40])
