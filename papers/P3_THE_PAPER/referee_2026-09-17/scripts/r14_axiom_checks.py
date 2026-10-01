"""Independent checks of the three claims, found in the 2026-10-01 sweep, that change how the chain's
axioms are GRADED (none changes how many there are).

  (1) SM lane B1380 (2026-09-26): "the puncture is the word's" -- among surfaces whose fundamental group is
      the description's group F2, only the once-punctured torus admits a homeomorphism realising the
      Fibonacci substitution sigma (a -> ab, b -> a) or its square.  If true, the paper's "puncture fork"
      is not an independent fragile choice: it is fixed once the carrier's group is F2.
  (2) SM lane B1379 / B1504 T1: the order bit A7 (LR versus RL) does not change the oriented manifold, so it
      is based data, not a choice of object.
  (3) sep16-branch I-31 (EARNED there): the monodromy's order-3 action at the quaternion node is the outer
      Z/3 of Q8.

Own code throughout; SnapPy only for (2)'s isometry check.
"""
from fractions import Fraction as Fr
import itertools, math

# ---------------------------------------------------------------- (1) the puncture
print("=" * 78)
print("(1) B1380: which surfaces with fundamental group F2 can realise sigma or sigma^2?")
print("=" * 78)

# The compact surfaces with free fundamental group of rank 2 are exactly those with nonempty boundary and
# Euler characteristic -1.  Orientable genus g with b boundary circles: 2-2g-b = -1.  Non-orientable with
# k crosscaps: 2-k-b = -1.  (A CLOSED surface never has free pi_1 of rank 2: orientable ones have pi_1
# trivial, Z^2 or H1 of rank >= 4; the closed chi = -1 surface N3 has 2-torsion in H1.)
surfaces = [("S(g=%d,b=%d)" % (g, b), "orientable", g, b) for g in range(0, 3) for b in range(1, 5)
            if 2 - 2 * g - b == -1]
surfaces += [("N(k=%d,b=%d)" % (k, b), "non-orientable", k, b) for k in range(1, 4) for b in range(1, 5)
             if 2 - k - b == -1]
print("   compact surfaces with pi_1 = F2:", [s[0] for s in surfaces])

# Boundary classes in H1 = Z^2, for a free basis (x, y) of pi_1 chosen in the standard way.
#   S(0,3), pair of pants: x, y two boundary loops; the third boundary is (xy)^-1.
#   S(1,1), once-punctured torus: the boundary is the commutator [x, y] -> 0 in H1.
#   N(2,1), Klein bottle minus a disk: the boundary is x^2 y^2.
#   N(1,2), projective plane minus two disks: boundaries c and x^2 c (x the crosscap, c a boundary loop).
boundary = {
    "S(g=0,b=3)": [(1, 0), (0, 1), (-1, -1)],
    "S(g=1,b=1)": [(0, 0)],
    "N(k=2,b=1)": [(2, 2)],
    "N(k=1,b=2)": [(0, 1), (2, 1)],
}

M1 = ((1, 1), (1, 0))          # sigma: a -> ab, b -> a, abelianised (columns are images of a, b); det -1
M2 = ((2, 1), (1, 1))          # sigma^2 = the golden monodromy LR-type matrix; det +1


def apply(M, v):
    return (M[0][0] * v[0] + M[0][1] * v[1], M[1][0] * v[0] + M[1][1] * v[1])


def mpow(M, n):
    R = ((1, 0), (0, 1))
    for _ in range(n):
        R = ((R[0][0] * M[0][0] + R[0][1] * M[1][0], R[0][0] * M[0][1] + R[0][1] * M[1][1]),
             (R[1][0] * M[0][0] + R[1][1] * M[1][0], R[1][0] * M[0][1] + R[1][1] * M[1][1]))
    return R


# A homeomorphism permutes boundary circles, so in H1 it maps the finite set of boundary classes into
# itself up to sign.  If some power of the induced matrix fixes a nonzero class up to sign, that power has
# eigenvalue +-1.  Check directly, for every power up to 60 (eigenvalues are phi^n and (-1/phi)^n, so no
# power can, but the check does not rely on that).
for M, name in ((M1, "sigma"), (M2, "sigma^2")):
    tr, det = M[0][0] + M[1][1], M[0][0] * M[1][1] - M[0][1] * M[1][0]
    disc = tr * tr - 4 * det
    print(f"   {name}: trace {tr}, det {det}, discriminant {disc}  -> eigenvalues irrational reals "
          f"{(tr - math.sqrt(disc)) / 2:+.6f}, {(tr + math.sqrt(disc)) / 2:+.6f}")
    for n in range(1, 61):
        P = mpow(M, n)
        for v in [(1, 0), (0, 1), (1, 1), (1, -1), (2, 1), (1, 2), (2, 2)]:
            w = apply(P, v)
            assert w != v and w != (-v[0], -v[1]), (name, n, v)
    print(f"      no power 1..60 fixes any of the test classes up to sign: True")

for s in surfaces:
    nm = s[0]
    classes = [c for c in boundary[nm] if c != (0, 0)]
    blocked = []
    for M, name in ((M1, "sigma"), (M2, "sigma^2")):
        # the classes must be permuted up to sign by M: test whether M maps the set into itself
        S = set(classes) | {(-a, -b) for a, b in classes}
        ok = all(apply(M, c) in S for c in classes) if classes else True
        blocked.append((name, ok))
    verdict = "CAN be realised (boundary class is 0 in H1)" if not classes else (
        "CANNOT: " + ", ".join(f"{n} does not permute the boundary classes" for n, ok in blocked if not ok))
    print(f"   {nm:<12s} boundary classes {boundary[nm]}  -> {verdict}")
print("   The table is in one basis and only illustrates.  The proof is basis-free: a homeomorphism permutes the")
print("   b boundary circles, so its b!-th power fixes every boundary class up to sign; a NONZERO such class would")
print("   make +-1 an eigenvalue of M^(b!), and M's eigenvalues are phi and -1/phi (sigma) or their squares, never")
print("   roots of unity.  So every boundary class must vanish in H1, which happens only on S(1,1).")
print("   => only the once-punctured torus remains; on it sigma and sigma^2 are realised (Nielsen: Out(F2) = GL(2,Z)")
print("      is the extended mapping class group of S(1,1)).  B1380's claim holds.")

# ---------------------------------------------------------------- (2) the order bit
print()
print("=" * 78)
print("(2) B1379 / B1504 T1: LR versus RL")
print("=" * 78)
L = ((1, 0), (1, 1)); R = ((1, 1), (0, 1))


def mul(A, B):
    return ((A[0][0] * B[0][0] + A[0][1] * B[1][0], A[0][0] * B[0][1] + A[0][1] * B[1][1]),
            (A[1][0] * B[0][0] + A[1][1] * B[1][0], A[1][0] * B[0][1] + A[1][1] * B[1][1]))


LR, RL = mul(L, R), mul(R, L)
Linv = ((1, 0), (-1, 1))
print(f"   LR = {LR}, RL = {RL}, L^-1 (LR) L = {mul(mul(Linv, LR), L)}  (det L = +1)")
print(f"   conjugate by an orientation-preserving element: {mul(mul(Linv, LR), L) == RL}")
try:
    import snappy, warnings
    warnings.filterwarnings("ignore")
    a, b, m = snappy.Manifold("b++LR"), snappy.Manifold("b++RL"), snappy.Manifold("m004")
    print(f"   SnapPy: b++LR ~ m004: {a.is_isometric_to(m)},  b++RL ~ m004: {b.is_isometric_to(m)},"
          f"  b++LR ~ b++RL: {a.is_isometric_to(b)}")
    isos = a.is_isometric_to(b, return_isometries=True)
    pres = sum(1 for i in isos if round(float(i.cusp_maps()[0].det())) == 1)
    print(f"   isometries b++LR -> b++RL: {len(isos)}, orientation-preserving: {pres}"
          f"  (B1504 states 8 and 4)")
except Exception as e:
    print("   SnapPy check skipped:", type(e).__name__, e)
print("   => the order bit does not change the oriented manifold: based data, as B1379 says.")

# ---------------------------------------------------------------- (3) I-31
print()
print("=" * 78)
print("(3) sep16 I-31: the monodromy at the quaternion node is the OUTER Z/3 of Q8")
print("=" * 78)


def qmul(p, q):
    a1, b1, c1, d1 = p; a2, b2, c2, d2 = q
    return (a1 * a2 - b1 * b2 - c1 * c2 - d1 * d2, a1 * b2 + b1 * a2 + c1 * d2 - d1 * c2,
            a1 * c2 - b1 * d2 + c1 * a2 + d1 * b2, a1 * d2 + b1 * c2 - c1 * b2 + d1 * a2)


one, i, j, k = (1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1)
neg = lambda q: tuple(-x for x in q)
Q8 = [one, i, j, k, neg(one), neg(i), neg(j), neg(k)]
# rho(a) = i, rho(b) = j; the monodromy phi(a) = ab, phi(b) = bab
rho_a, rho_b = i, j
img_a, img_b = qmul(rho_a, rho_b), qmul(qmul(rho_b, rho_a), rho_b)
print(f"   phi(a) = ab -> {img_a} (= k),  phi(b) = bab -> {img_b} (= i)")
# the induced map on Q8: i -> k, j -> i, extended multiplicatively
f = {i: k, j: i}
f[k] = qmul(f[i], f[j]); f[one] = one
for x in (i, j, k, one):
    f[neg(x)] = neg(f[x])
hom = all(f[qmul(x, y)] == qmul(f[x], f[y]) for x in Q8 for y in Q8)


def it(fn, x, n):
    for _ in range(n):
        x = fn[x]
    return x


order = next(n for n in range(1, 13) if all(it(f, x, n) == x for x in Q8))
inner = []
for g in Q8:
    ginv = (g[0], -g[1], -g[2], -g[3])
    inner.append({x: qmul(qmul(g, x), ginv) for x in Q8})
is_inner = any(all(f[x] == h[x] for x in Q8) for h in inner)
print(f"   (i, j, k) -> ({f[i]}, {f[j]}, {f[k]}) = (k, i, j);  a homomorphism on all 64 products: {hom}")
print(f"   order {order};  inner: {is_inner}  -> an OUTER automorphism of order 3, as I-31 states")

# The row's side A is the derivative of the trace map at the node.  Trace identities give, for phi(a) = ab,
# phi(b) = bab and (x, y, z) = (tr a, tr b, tr ab):  F(x, y, z) = (z, yz - x, z(yz - x) - y)
# (tr bab = tr b tr ab - tr a;  tr(uv) = tr u tr v - tr(u v^-1) with u v^-1 = b^-1).  Checked on random
# SL(2, C) pairs rather than trusted, then differentiated at the node (0, 0, 0), where kappa = -2.
import random, cmath
random.seed(1)


def m2(A, B):
    return [[A[0][0] * B[0][0] + A[0][1] * B[1][0], A[0][0] * B[0][1] + A[0][1] * B[1][1]],
            [A[1][0] * B[0][0] + A[1][1] * B[1][0], A[1][0] * B[0][1] + A[1][1] * B[1][1]]]


def rand_sl2():
    a, b, c = (complex(random.uniform(-2, 2), random.uniform(-2, 2)) for _ in range(3))
    return [[a, b], [c, (1 + b * c) / a]]


def F(x, y, z):
    return (z, y * z - x, z * (y * z - x) - y)


worst = 0.0
for _ in range(200):
    A_, B_ = rand_sl2(), rand_sl2()
    tr = lambda M: M[0][0] + M[1][1]
    u = m2(A_, B_); v = m2(m2(B_, A_), B_)
    lhs = (tr(u), tr(v), tr(m2(u, v)))
    rhs = F(tr(A_), tr(B_), tr(m2(A_, B_)))
    worst = max(worst, max(abs(p - q) / (1 + abs(p)) for p, q in zip(lhs, rhs)))
print(f"   trace map F(x,y,z) = (z, yz-x, z(yz-x)-y): max relative error on 200 random SL(2,C) pairs {worst:.1e}")
# Jacobian at the origin, exactly: d/dx, d/dy, d/dz of each component at (0,0,0)
D = [[0, 0, 1], [-1, 0, 0], [0, -1, 0]]
h = Fr(1, 10 ** 6)
num = [[(F(*[h if t == c else 0 for t in range(3)])[r] - F(0, 0, 0)[r]) / h for c in range(3)] for r in range(3)]
# the components are polynomials whose quadratic terms vanish to first order at 0; the exact derivative is the
# linear part, read off the finite difference up to O(h)
assert all(abs(num[r][c] - D[r][c]) <= 2 * h for r in range(3) for c in range(3))
D2 =[[sum(D[r][t] * D[t][c] for t in range(3)) for c in range(3)] for r in range(3)]
D3 = [[sum(D2[r][t] * D[t][c] for t in range(3)) for c in range(3)] for r in range(3)]
print(f"   D = dF at the node = {D}  (the row's matrix);  D^3 = I: {D3 == [[1,0,0],[0,1,0],[0,0,1]]},"
      f"  D != I: {D != [[1,0,0],[0,1,0],[0,0,1]]}")
print("   => I-31's mathematics holds as stated.  It is a mathematical identity (both sides are the object's own")
print("      structure), so EARNED here does not reduce any input of a physical reading.")

# ---------------------------------------------------------------- (4) B1382: the spin bit and the parent's Pin type
print()
print("=" * 78)
print("(4) SM lane B1382: m004's two spin structures are the pullbacks of the Gieseking manifold's Pin+ and Pin-")
print("=" * 78)
# Exact arithmetic in Q(w), w^2 + w + 1 = 0: an element is (p, q) = p + q w.
W0 = (Fr(0), Fr(0)); W1 = (Fr(1), Fr(0)); OM = (Fr(0), Fr(1))


def wadd(x, y): return (x[0] + y[0], x[1] + y[1])
def wneg(x): return (-x[0], -x[1])
def wmul(x, y):                                   # (a + b w)(c + d w) = ac + (ad + bc) w + bd w^2, w^2 = -1 - w
    a, b = x; c, d = y
    return (a * c - b * d, a * d + b * c - b * d)
def wconj(x):                                     # conj(w) = w^2 = -1 - w
    a, b = x
    return (a - b, -b)


def M(*e): return [[e[0], e[1]], [e[2], e[3]]]
def mm(X, Y): return [[wadd(wmul(X[r][0], Y[0][c]), wmul(X[r][1], Y[1][c])) for c in range(2)] for r in range(2)]
def minv(X): return [[X[1][1], wneg(X[0][1])], [wneg(X[1][0]), X[0][0]]]     # det 1
def mconj(X): return [[wconj(X[r][c]) for c in range(2)] for r in range(2)]
def mneg(X): return [[wneg(X[r][c]) for c in range(2)] for r in range(2)]


I2 = M(W1, W0, W0, W1)
A_ = M(W1, W1, W0, W1)                             # B1141's holonomy, as B1382 S1 states it
B_ = M(W1, W0, wneg(OM), W1)
gen = {"a": A_, "b": B_, "A": minv(A_), "B": minv(B_)}


def word(wd, g=gen):
    R = I2
    for ch in wd:
        R = mm(R, g[ch])
    return R


rel = "abABaBAbaB"
print(f"   relator {rel} on (A, B): {word(rel) == I2};  on (-A, -B): "
      f"{word(rel, {'a': mneg(A_), 'b': mneg(B_), 'A': mneg(minv(A_)), 'B': mneg(minv(B_))}) == I2};  on (A, -B): "
      f"{word(rel, {'a': A_, 'b': mneg(B_), 'A': minv(A_), 'B': mneg(minv(B_))}) == I2}")
Wt = M(W1, wneg(OM), W0, W1)                       # B1382's intertwiner W = [[1, -w], [0, 1]]
print(f"   W conj(A) W^-1 = A (beat(a) = a): {mm(mm(Wt, mconj(A_)), minv(Wt)) == A_}")
print(f"   W conj(B) W^-1 = rho(b^-1 a b a^-1 b) (beat(b)): {mm(mm(Wt, mconj(B_)), minv(Wt)) == word('BabAb')}")
WWb = mm(Wt, mconj(Wt))
print(f"   W conj(W) = +A: {WWb == A_}")


# Is W the only intertwiner up to scale?  W conj(g) = rho(beat g) W for g = a, b is C-linear in W's four entries
# with coefficients in Q(w): eight equations; B1382 S2 states rank 3.  Exact elimination over Q(w).
def winv(x):                                      # 1/(a + b w) = conj / norm, norm = a^2 - ab + b^2
    a, b = x; n = a * a - a * b + b * b
    c = wconj(x)
    return (c[0] / n, c[1] / n)


rows = []
for X, Y in ((mconj(A_), A_), (mconj(B_), word("BabAb"))):
    for r in range(2):
        for c in range(2):
            coef = [W0] * 4                       # unknowns w11, w12, w21, w22 at index 2*row + col
            for t in range(2):
                coef[2 * r + t] = wadd(coef[2 * r + t], X[t][c])          # (W X)_{rc} = sum_t W_{rt} X_{tc}
                coef[2 * t + c] = wadd(coef[2 * t + c], wneg(Y[r][t]))    # - (Y W)_{rc} = - sum_t Y_{rt} W_{tc}
            rows.append(coef)
rank, rr = 0, [list(r) for r in rows]
for col in range(4):
    p = next((i for i in range(rank, len(rr)) if rr[i][col] != W0), None)
    if p is None:
        continue
    rr[rank], rr[p] = rr[p], rr[rank]
    iv = winv(rr[rank][col]); rr[rank] = [wmul(iv, x) for x in rr[rank]]
    for i in range(len(rr)):
        if i != rank and rr[i][col] != W0:
            fct = rr[i][col]; rr[i] = [wadd(x, wneg(wmul(fct, y))) for x, y in zip(rr[i], rr[rank])]
    rank += 1
print(f"   intertwiner equations: exact rank {rank} of 4 unknowns -> solution space dimension {4 - rank}"
      f" (B1382 S2: rank 3, one-dimensional)")
lon = word("bABaaBAb")
fmt = lambda x: str(x[0]) if x[1] == 0 else f"{x[0]}+{x[1]}w"
print(f"   cusp traces of B1141's lift: tr(a) = {fmt(wadd(A_[0][0], A_[1][1]))}, tr(bABaaBAb) = "
      f"{fmt(wadd(lon[0][0], lon[1][1]))};  the longitude commutes with a: {mm(lon, A_) == mm(A_, lon)}")
print("   the table below is the sign law applied to the computed W conj(W) = +A, not a separate computation:")
# In G_eps the element (lambda W, c) squares to (eps |lambda|^2 W conj(W), 0) = (eps |lambda|^2 A, 0).  The beat t
# satisfies t^2 = a, so a lift with a -> s A extends into G_eps iff eps |lambda|^2 = s, i.e. eps = s (the other
# relations are eps-free: conjugation by (X, 1) is X conj(.) X^-1 whatever eps is).  W is unique up to scale
# (B1382 S2: the intertwiner space is one-dimensional), so there is no other candidate.
for s in (+1, -1):
    ok = {eps: (eps == s) for eps in (+1, -1)}
    print(f"   lift a -> {'+' if s > 0 else '-'}A: extends into G+ (Pin+): {ok[+1]},  into G- (Pin-): {ok[-1]}")
try:
    import snappy
    N, Mo = snappy.Manifold("m000"), snappy.Manifold("m004")
    print(f"   SnapPy: m000 orientable {N.is_orientable()}, H1 {N.homology()};  m004 H1 {Mo.homology()};"
          f"  orientation cover of m000 is m004: {N.orientation_cover().is_isometric_to(Mo)}")
except Exception as e:
    print("   SnapPy check skipped:", type(e).__name__, e)
print("   chi(m000) = 0 and H1 = Z free => H2 = 0 => H^2(m000; Z/2) = 0 => w2 = w1^2 = 0: both Pin types exist,")
print("   two structures each; the cover map on H1 is x2 (the fibre's monodromy is sigma, the cover's sigma^2),")
print("   so H^1(m000; Z/2) pulls back to 0 and each Pin type gives exactly ONE spin structure on m004 -- and by")
print("   the sign law above the two types give DIFFERENT ones.  B1382's theorem holds.  Consequence for main:")
print("   the spin lift is not assigned by the object; it is traded for the parent's Pin type (one bit, not zero).")
