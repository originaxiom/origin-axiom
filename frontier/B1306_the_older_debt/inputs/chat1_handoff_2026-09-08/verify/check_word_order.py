#!/usr/bin/env python3
"""Does the mirror choice ab vs ba pay the chirality bit?  Computed, not argued."""
import sympy as sp

# ---------- free group F2 on a,b  (A = a^-1, B = b^-1) ----------
INV = {'a':'A','A':'a','b':'B','B':'b'}
def red(w):
    out=[]
    for c in w:
        if out and out[-1]==INV[c]: out.pop()
        else: out.append(c)
    return ''.join(out)
def inv(w): return red(''.join(INV[c] for c in reversed(w)))
def sub_word(w, img):           # apply a substitution given as {'a':...,'b':...}
    return red(''.join(img[c] if c in img else inv(img[INV[c]]) for c in w))

gold   = {'a':'ab', 'b':'a'}    # a -> ab,  b -> a
mirror = {'a':'ba', 'b':'a'}    # a -> ba,  b -> a
invert = {'a':'A',  'b':'b'}    # a -> a^-1

# claim: mirror = inn_{a^-1} o gold, i.e. a^-1 * gold(w) * a = mirror(w) for w in {a,b}
g = 'A'
checks = {w: red(g + sub_word(w,gold) + inv(g)) == sub_word(w,mirror) for w in ('a','b')}
print("=== ab vs ba : are they inner-equivalent in Aut(F2)? ===")
for w in ('a','b'):
    print(f"   a^-1 * gold({w}) * a = {red(g+sub_word(w,gold)+inv(g)):6s}   mirror({w}) = {sub_word(w,mirror)}")
inner_equiv = all(checks.values())
print(f"   INNER-EQUIVALENT: {inner_equiv}")

# ---------- trace maps, computed from generic SL(2,C) matrices ----------
x,y,z = sp.symbols('x y z')
a1,a2,a3,b1,b2,b3 = sp.symbols('a1 a2 a3 b1 b2 b3')
A_ = sp.Matrix([[a1,a2],[a3,(1+a2*a3)/a1]])
B_ = sp.Matrix([[b1,b2],[b3,(1+b2*b3)/b1]])
Ai = sp.Matrix([[A_[1,1],-a2],[-a3,a1]])
X,Y,Z = sp.trace(A_), sp.trace(B_), sp.trace(A_*B_)
def as_xyz(M, cand):
    """verify trace(M) equals cand(x,y,z) after x->X etc."""
    return sp.simplify(sp.together(sp.trace(M) - cand.subs({x:X,y:Y,z:Z}, simultaneous=True)))

W = {'gold'  : (A_*B_, A_,  A_*B_*A_),          # (a', b', a'b') for a->ab, b->a
     'mirror': (B_*A_, A_,  B_*A_*A_),          # for a->ba, b->a
     'invert': (Ai,    B_,  Ai*B_)}             # for a->a^-1, b->b
cand = {'gold'  : (z, x, x*z - y),
        'mirror': (z, x, x*z - y),
        'invert': (x, y, x*y - z)}
print("\n=== induced trace maps (residual 0 = the claimed map is correct) ===")
ok=True
for k,(m1,m2,m3) in W.items():
    r = [as_xyz(m1,cand[k][0]), as_xyz(m2,cand[k][1]), as_xyz(m3,cand[k][2])]
    good = all(v==0 for v in r); ok &= good
    print(f"   {k:7s} -> {str(cand[k]):22s} residuals {r}  ok={good}")
same = (cand['gold'] == cand['mirror'])
print(f"\n   gold and mirror induce the SAME map on the character variety: {same}")
print(f"   inversion induces a DIFFERENT map: {cand['invert'] != cand['gold']}")

print("\n=== VERDICT ===")
print("   ab vs ba differ by the inner automorphism conj(a^-1); inner automorphisms act")
print("   trivially on the character variety, so the WORD-ORDER MIRROR IS INVISIBLE on X.")
print("   It pays no bit. Inversion (a -> a^-1) is NOT inner and does act.")
raise SystemExit(0 if (inner_equiv and ok and same) else 1)
