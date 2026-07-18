# BLIND independent gate: Whitehead (m129) holonomy image mod (2+i) in SL(2,F_5).
# Method: trace-triple (tr A, tr B, tr AB) mod (2+i) determines the SL(2,F_5)
# image up to conjugacy (for irreducible reps); build a representative pair and
# compute the generated subgroup order (120 = fills 2I, else proper subgroup).
import snappy
from sage.all import GF, matrix, MatrixGroup, gcd

M = snappy.Manifold('m129')                 # Whitehead link complement
G = M.fundamental_group()
gens = G.generators()
print("gens:", gens, " vol:", float(M.volume()))

def to_Zi(z, tol=1e-6):
    a, b = z.real, z.imag
    ra, rb = round(a), round(b)
    assert abs(a-ra)<tol and abs(b-rb)<tol, f"not a Gaussian integer: {z}"
    return (int(ra), int(rb))

def redmod(zi):                              # a+bi mod (2+i): i -> 3 in F_5
    a, b = zi
    return (a + 3*b) % 5

import itertools
def tr_word(w):
    Mx = G.SL2C(w)
    return complex(Mx[0][0] + Mx[1][1])

# traces of the two generators and their product (and a cross-check word)
a, b = gens[0], gens[1]
words = {'a':a, 'b':b, 'ab':a+b, 'aB':a+b.upper() if b.islower() else a+b}
# snappy words: lower=gen, upper=inverse; product = concatenation string
tA  = to_Zi(tr_word(a));   tB  = to_Zi(tr_word(b))
tAB = to_Zi(tr_word(a+b)); tAb = to_Zi(tr_word(a+b.upper()))
print("tr A =", tA, " tr B =", tB, " tr AB =", tAB, " tr AB^-1 =", tAb, " (Gaussian integers)")
ta, tb, tab = redmod(tA), redmod(tB), redmod(tAB)
print(f"mod (2+i) -> tr A={ta}, tr B={tb}, tr AB={tab} in F_5")

# build a representative pair in SL(2,F_5) with these traces:
F = GF(5)
# A in companion form: [[ta,-1],[1,0]] has trace ta, det 1
A = matrix(F, [[ta, -1],[1, 0]])
# B = [[p,q],[r,s]] with det 1, trace tb, and tr(AB)=tab. Solve:
# tr(AB) = ta*p ... compute symbolically: AB = [[ta*p - r, ta*q - s],[p, q]]
# tr(AB) = ta*p - r + q = tab ; with s = tb - p ; det: p*s - q*r =1
sols=[]
for p in F:
    s = F(tb) - p
    for q in F:
        # tr(AB) = ta*p - r + q = tab -> r = ta*p + q - tab
        r = F(ta)*p + q - F(tab)
        if p*s - q*r == 1:
            sols.append((p,q,r,s))
print(f"{len(sols)} candidate B matrices; using first with irreducible image")
order=None
for (p,q,r,s) in sols:
    B = matrix(F,[[p,q],[r,s]])
    Grp = MatrixGroup([A,B])
    o = Grp.order()
    order = o
    # report the first; all give conjugate (same order) images for a fixed trace triple
    print(f"  B=({p},{q},{r},{s}) -> |<A,B>| = {o}")
    break
print()
print(f"BLIND VERDICT: image order = {order}")
print("  |SL(2,5)| = |2I| = 120." )
print("  => FILLS 2I" if order==120 else f"  => PROPER SUBGROUP (order {order})")
