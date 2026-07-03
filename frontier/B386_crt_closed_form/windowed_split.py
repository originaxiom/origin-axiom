"""B386 L2 -- the closed form: slot class partials as products of local factor sums.

Using L1 (C = C3*C5 at (2,2)): the slot partial over det-class K splits as
  partial(K) = (1/240) * sum_{j-parity p, l-parity q in the shared 2-part}
                 T3[K3](p,q) * T5[K5](p,q)
where T3(p,q) = sum over the 3-side sublattice with those parities of
  (zeta4-part of windows) * C3 * ind3, and T5 the 5-side analog -- ALL evaluated exactly.
Gate: exact equality with the banked partials (0,0,-1/16,-1/16) and (0,0,-1/48,-1/48).
Then each T-factor is printed in H-components for recognition (Gauss sums / phi-units)."""
import json, os, sys
from fractions import Fraction as Fr
from math import gcd
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "B358_seam_certification"))
sys.path.insert(0, os.path.join(HERE, "..", "B367_value_map"))
import cyclo_engine as E
import seam_certification as SC
from tensor_gate import local_partrace_table

o1, o2 = 20, 12
T3 = local_partrace_table(3, 2, 1, 2, o1, o2)
T5 = local_partrace_table(5, 2, 1, 2, o1, o2)

# gamma bookkeeping (mod 3 and mod 5 separately)
def A(m, n): return [[(1+m*m) % n, m % n], [m % n, 1 % n]]
def mm(a, b, n): return [[(a[0][0]*b[0][0]+a[0][1]*b[1][0]) % n, (a[0][0]*b[0][1]+a[0][1]*b[1][1]) % n],
                         [(a[1][0]*b[0][0]+a[1][1]*b[1][0]) % n, (a[1][0]*b[0][1]+a[1][1]*b[1][1]) % n]]
def ind_table(n):
    g1, g2 = A(1, n), A(2, n)
    G1 = [[[1 % n, 0], [0, 1 % n]]]
    for _ in range(o1-1): G1.append(mm(G1[-1], g1, n))
    G2 = [[[1 % n, 0], [0, 1 % n]]]
    for _ in range(o2-1): G2.append(mm(G2[-1], g2, n))
    out = {}
    for j in range(o1):
        for l in range(o2):
            g = mm(G1[j], G2[l], n)
            d = ((-g[0][0]-1)*(-g[1][1]-1) - g[0][1]*g[1][0]) % n
            out[(j, l)] = (gcd(d, n) == 1)
    return out
I3, I5 = ind_table(3), ind_table(5)

# windows: w1(j) = zeta20^{-6j} - zeta20^{-14j}; w2(l) = zeta12^{-2l} - zeta12^{-10l}
def w1(j): return E.sub(E.zeta((-18*j) % 60), E.zeta((-42*j) % 60))
def w2(l): return E.sub(E.zeta((-10*l) % 60), E.zeta((-50*l) % 60))
# split each window into (5-side char) x (4-side char) etc. is implicit; here we split the
# GRID by CRT and keep windows whole on each side using zeta20 = zeta4*zeta5 decompositions:
# zeta20^{-6j} = zeta4^{-6j mod 4} * zeta5^{-6j mod 5}? NO -- 1/20 = a/4 + b/5 with
# -6/20 = -3/10 = ... cleaner: zeta20^k = zeta4^{k * inv4} * zeta5^{k * inv5} where
# 1/20 = inv4/4 + inv5/5 mod 1: 1/20 = (1*5^{-1 mod 4}=1? ) use CRT: k/20 = k*(-1)/4 + k*(1)/5
# mod 1 since -5 + 4*? ... verify: 1/20 = x/4 + y/5 -> 1 = 5x + 4y -> x=1,y=-1: 1/20 = 1/4 - 1/5.
def z20pow(k):  # returns (zeta4-part exponent, zeta5-part exponent) with zeta20^k = zeta4^k * zeta5^{-k}
    return (k % 4, (-k) % 5)
def z12pow(k):  # 1/12 = x/4 + y/3: 1 = 3x + 4y -> x=1? 3*1+4*0=3 no; x=-1,y=1: -3+4=1: 1/12 = -1/4 + 1/3
    return ((-k) % 4, k % 3)

# factor windows: w1(j) = z4^{-6j}z5^{6j} - z4^{-14j}z5^{14j}; each term is a product ->
# the j-sum with C3 (depends on j via local powers; period divides 12? verify) and C5.
# STRATEGY (exact, no hand algebra): compute the class-partials DIRECTLY from the tensor
# tables as the double sum, THEN verify the product/branch structure by computing the
# candidate factor sums and checking the assembly identity exactly.
def hproj(t): return SC.solve_H(SC.H_avg(t))

def partial(K):
    tot = E.ZERO
    for j in range(o1):
        for l in range(o2):
            in3, in5 = I3[(j, l)], I5[(j, l)]
            cls = (1 if in3 else 3) * (1 if in5 else 5)
            if cls != K: continue
            tot = E.add(tot, E.mul(E.mul(w1(j), w2(l)), E.mul(T3[(j, l)], T5[(j, l)])))
    return E.scal(Fr(1, 240), tot)

p1, p5c = partial(1), partial(5)
print("tensor-assembled class-1 partial:", hproj(p1), " target (0,0,-1/16,-1/16)")
print("tensor-assembled class-5 partial:", hproj(p5c), " target (0,0,-1/48,-1/48)")

# THE FACTOR SUMS: for each window term (a1,a2) in {6,14}x{2,10} with signs s=(+,-,-,+),
# and each parity branch, the 3-side and 5-side sums:
#   S3(a1,a2 | j4,l4-lattice) = sum_{j,l} z4^{...} C3 ind3 restricted to (j mod 2, l mod 2) parities
# We verify: partial(K) = (1/240) sum_{terms} s * sum_{p,q in Z2xZ2} S3^{term,K}(p,q) * S5^{term,K}(p,q)
# with S3 summed over (j,l) with (j%2,l%2)=(p,q) of [z4-part of windows]*C3*ind3-part,
# and S5 over the same-parity classes of [z5-part]*C5*ind5-part -- BUT S3 and S5 each sum over
# the FULL grid restricted to parity, so the product double-counts unless the factors are
# genuinely parity-only-coupled. Test the sharpest version: C3(j,l) depends only on
# (j mod P13, l mod P23); find the true periods first.
def period(T, axis):
    for P in (1, 2, 3, 4, 5, 6, 10, 12, 20):
        if axis == 0 and all(T[(j, l)] == T[((j+P) % o1, l)] for j in range(o1) for l in range(o2)):
            return P
        if axis == 1 and P <= o2 and all(T[(j, l)] == T[(j, (l+P) % o2)] for j in range(o1) for l in range(o2)):
            return P
    return None
print("C3 periods (j,l):", period(T3, 0), period(T3, 1), " C5 periods:", period(T5, 0), period(T5, 1))
print("ind3 periods:", period({k: E.scal(Fr(1 if v else 0), E.ONE) for k, v in I3.items()}, 0),
      period({k: E.scal(Fr(1 if v else 0), E.ONE) for k, v in I3.items()}, 1))
print("ind5 periods:", period({k: E.scal(Fr(1 if v else 0), E.ONE) for k, v in I5.items()}, 0),
      period({k: E.scal(Fr(1 if v else 0), E.ONE) for k, v in I5.items()}, 1))
json.dump(dict(class1=[str(x) for x in hproj(p1)], class5=[str(x) for x in hproj(p5c)],
               periods=dict(C3=[period(T3,0), period(T3,1)], C5=[period(T5,0), period(T5,1)])),
          open(os.path.join(HERE, "windowed_split.json"), "w"), indent=1)
print("DONE")
