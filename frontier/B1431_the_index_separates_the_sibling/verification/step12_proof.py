"""Step 12.  IS IT A THEOREM?  The 3D index state sum depends only on
      (edge rows E_1..E_N ;  the weight k -> sum k_i ;  the boundary map v: Lambda -> Z^{3N}).
   Symmetries of that data which leave EVERY I(gamma) unchanged:
      * permuting the tetrahedra and cyclically rotating the three slots inside each one
        (J_D is cyclically invariant),
      * permuting the edge rows (preserves q^{sum k}),
      * v -> v + sum_i n_i E_i with sum_i n_i = 0 (each E_i multiplies I by q^{-1};
        checked numerically in step10),
      * relabelling the boundary lattice by A in GL(Lambda).
   If m003's data maps onto m004's under such a transformation, then
        I_m003(gamma) = I_m004(A gamma)  for EVERY gamma -- a proof, not an observation.
"""
import itertools, json
from fractions import Fraction as F
from idx import rows, bdry_vector, index_class
from tet_index import s_str, s_eq, s_trunc

def rot(t, r): return tuple(t[(i + r) % 3] for i in range(3))
def apply_P(vec, n, perm, rots):
    """permute tet blocks by perm (new block i = old block perm[i]) and rotate each."""
    out = []
    for j in range(n):
        blk = tuple(vec[3 * perm[j] + s] for s in range(3))
        out.extend(rot(blk, rots[j]))
    return out

M3, n3, r3, E3, Mr3, Ln3 = rows("m003")
M4, n4, r4, E4, Mr4, Ln4 = rows("m004")
print("m003  E:", E3, " Mr:", Mr3[0], " Ln:", Ln3[0])
print("m004  E:", E4, " Mr:", Mr4[0], " Ln:", Ln4[0])

print("\n--- search: a relabelling P of m003's slots carrying its EDGE rows onto m004's ---")
hits = []
for perm in itertools.permutations(range(2)):
    for rots in itertools.product(range(3), repeat=2):
        img = [apply_P(E3[i], 2, perm, rots) for i in range(2)]
        for eperm in itertools.permutations(range(2)):
            if [img[eperm[i]] for i in range(2)] == E4:
                hits.append((perm, rots, eperm))
for h in hits: print("   P =", h)
assert hits, "no slot relabelling matches the edge rows"

print("\n--- with that P, solve for A on the boundary lattice ---")
# m003 class (x,y) = x*mu3 + y*lam3 ;  m004 class (X,Y) = X*mu4 + Y*lam4
# require   P(v3(x,y)) = v4(X,Y) + n0 E4_0 + n1 E4_1 ,  n0+n1 = 0.
perm, rots, eperm = hits[0]
import sympy
x, y, Xs, Ys, nn = sympy.symbols("x y X Y n", rational=True)
v3 = [-(x * Mr3[0][s] + y * Ln3[0][s]) for s in range(6)]
Pv3 = []
for j in range(2):
    blk = tuple(v3[3 * perm[j] + s] for s in range(3))
    Pv3.extend(rot(blk, rots[j]))
v4 = [-(Xs * Mr4[0][s] + Ys * Ln4[0][s]) + nn * E4[0][s] - nn * E4[1][s] for s in range(6)]
sol = sympy.solve([sympy.Eq(Pv3[s], v4[s]) for s in range(6)], [Xs, Ys, nn], dict=True)
print("   P(v3) =", Pv3)
print("   v4(X,Y)+n(E0-E1) =", v4)
print("   SOLUTION:", sol)
S = sol[0]
print(f"\n   ==> A : (x,y)_m003  |-->  (X,Y)_m004 = ({S[Xs]}, {S[Ys]}),  n = {S[nn]}")

print("\n--- the same map in SATURATED-lattice coordinates ---")
print("   Lambda(m003) = <mu/2, lam>   (x=c/2, y=d);   Lambda(m004) = <mu, lam/2>   (X=a, Y=b/2)")
c, d = sympy.symbols("c d")
a_ = S[Xs].subs({x: c / 2, y: d}); b_ = 2 * S[Ys].subs({x: c / 2, y: d})
print(f"   (c,d) |--> (a,b) = ({sympy.simplify(a_)}, {sympy.simplify(b_)})   "
      f"determinant of the matrix: {sympy.Matrix([[sympy.diff(a_,c),sympy.diff(a_,d)],[sympy.diff(b_,c),sympy.diff(b_,d)]]).det()}")

print("\n--- numerical confirmation of the theorem over a wide range, to q^30 ---")
X = 64; CUT = 60
bad = []; ok = 0
for cc in range(-6, 7):
    for dd in range(-6, 7):
        xv, yv = F(cc, 2), F(dd)
        Xv = F(S[Xs].subs({x: xv, y: yv})); Yv = F(S[Ys].subs({x: xv, y: yv}))
        try:
            s3 = index_class("m003", ((xv, yv),), X)
            s4 = index_class("m004", ((Xv, Yv),), X)
        except AssertionError as e:
            bad.append((cc, dd, "box " + str(e)[:40])); continue
        if s_eq(s3, s4, CUT): ok += 1
        else: bad.append((cc, dd, (xv, yv), (Xv, Yv)))
print(f"   classes checked: {ok} agree, {len(bad)} disagree.   failures: {bad[:6]}")
