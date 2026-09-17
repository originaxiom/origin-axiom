"""Referee check of the paper's SS6 content census:
   252 candidates -> colour cubic kills 222 -> the remaining conditions leave exactly TWO,
   the SM 15-plet and its conjugate, under the two stated extra conditions
   (exactly five multiplets; no multiplet of zero hypercharge) plus rigidity and chirality.
Everything below is written from the paper's own description; no repository code is used."""
import itertools
from sympy import symbols, Rational, Matrix, solve, groebner, QQ, simplify, expand, Poly

# six SM-visible field types under SU(3) x SU(2): (dim3, dim2, conjugate?)
# name, SU(3) cubic anomaly coeff, #SU(2) doublets, T(3)*d(2), T(2)*d(3), d(R)
TYPES = {
 'Q' : dict(c3= 2, nd=3, t3=Rational(1,2)*2, t2=Rational(1,2)*3, d=6, conj='Qb'),  # (3,2)
 'Qb': dict(c3=-2, nd=3, t3=Rational(1,2)*2, t2=Rational(1,2)*3, d=6, conj='Q' ),  # (3b,2)
 'U' : dict(c3= 1, nd=0, t3=Rational(1,2)*1, t2=0,               d=3, conj='Ub'),  # (3,1)
 'Ub': dict(c3=-1, nd=0, t3=Rational(1,2)*1, t2=0,               d=3, conj='U' ),  # (3b,1)
 'L' : dict(c3= 0, nd=1, t3=0,               t2=Rational(1,2)*1, d=2, conj='L' ),  # (1,2)
 'E' : dict(c3= 0, nd=0, t3=0,               t2=0,               d=1, conj='E' ),  # (1,1)
}
names = list(TYPES)
cands = list(itertools.combinations_with_replacement(names, 5))
print("candidate contents  C(10,5) =", len(cands))

# --- step 1: pure colour cubic [SU(3)]^3 ---
def colour_ok(c): return sum(TYPES[t]['c3'] for t in c) == 0
after_colour = [c for c in cands if colour_ok(c)]
print("killed by the colour cubic alone:", len(cands)-len(after_colour),
      " -> survivors:", len(after_colour))

# --- step 2: Witten global SU(2) anomaly: total number of doublets even ---
def witten_ok(c): return sum(TYPES[t]['nd'] for t in c) % 2 == 0
after_witten = [c for c in after_colour if witten_ok(c)]
print("after Witten parity:", len(after_witten))

# --- step 3: the three linear conditions + the cubic, with rigidity ---
Y = symbols('y0 y1 y2 y3 y4')
def conditions(c):
    lin = [
      sum(TYPES[t]['t3']*Y[i] for i,t in enumerate(c)),                  # [SU(3)]^2 Y
      sum(TYPES[t]['t2']*Y[i] for i,t in enumerate(c)),                  # [SU(2)]^2 Y
      sum(TYPES[t]['d'] *Y[i] for i,t in enumerate(c)),                  # grav^2 Y
    ]
    cub = sum(TYPES[t]['d']*Y[i]**3 for i,t in enumerate(c))             # [Y]^3
    return lin, cub

def is_vectorlike(c, yvals):
    """content is vector-like if its multiplets pair off into conjugate pairs with opposite Y"""
    items = sorted(zip(c, yvals), key=lambda p:(p[0],str(p[1])))
    used=[False]*len(items)
    for i,(t,y) in enumerate(items):
        if used[i]: continue
        cj = TYPES[t]['conj']
        found=False
        for j in range(len(items)):
            if j==i or used[j]: continue
            t2,y2 = items[j]
            if t2==cj and y2==-y:
                used[i]=used[j]=True; found=True; break
        if not found: return False
    return all(used)

survivors=[]
for c in after_witten:
    lin, cub = conditions(c)
    M = Matrix([[l.coeff(y) for y in Y] for l in lin])
    ns = M.nullspace()
    k = len(ns)                                  # dim of the linear solution space
    if k == 0: continue
    # parametrise and impose the cubic
    ps = symbols('t0:%d' % k)
    vec = sum((ps[i]*ns[i] for i in range(k)), Matrix([0]*5))
    cubp = expand(cub.subs({Y[i]: vec[i] for i in range(5)}))
    if cubp == 0:
        rigid = False                             # cubic identically satisfied -> a whole family
        sols = ['<cubic vacuous: %d-dim family>' % k]
    else:
        # solve the cubic on the projective space of the linear solutions
        sols = solve(cubp, list(ps), dict=True)
        rigid = True
    for s in (sols if cubp != 0 else []):
        yv=[simplify(v.subs(s)) for v in vec]
        if all(x == 0 for x in yv): continue      # trivial ray
        free = [p for p in ps if p not in s]
        # a genuine point needs the solution to be a single ray: at most one free scale
        if len(free) > 1: continue                # continuous deformation survives -> not rigid
        if any(x == 0 for x in yv): continue      # "no multiplet of zero hypercharge"
        if is_vectorlike(c, yv): continue         # must be chiral
        survivors.append((c, tuple(yv), tuple(free)))

# normalise each survivor ray and deduplicate
norm=set()
for c,yv,free in survivors:
    sc=next((v for v in yv if v!=0), None)
    key=(c, tuple(simplify(v/sc) for v in yv))
    norm.add(key)
print("\nrigid, chiral, zero-hypercharge-free, fully anomaly-free contents:", len(norm))
for c,yv in sorted(norm, key=str):
    print("   content", c, "  hypercharge ray", yv)
print("\npaper: 'exactly TWO contents survive as rigid, chiral and fully anomaly-free:")
print("        the Standard Model 15-plet and its complex conjugate -- one theory, not two'")
