#!/usr/bin/env python3
"""MEMO-104 CELL (CLOSURE ROUTES, route g first step): THE E6 BOUNDARY
OBJECT BUILT — L154's one untouched route (the E6-lattice boundary
construction) gets its first actual construction: the (E6)_1 lattice
theory's boundary data computed EXACTLY, and it is object-arithmetic
through and through.

FOUR PREREGISTERED FACTS (each two-outcome: the stated identity holds
exactly, or the route banks a refutation at that step):
  F1 (EISENSTEIN STRUCTURE): the E6 root lattice carries a fixed-
     point-free order-3 isometry M (the Coxeter element's 4th power)
     with M^2 + M + I = 0 as an exact matrix identity => E6 is a
     module over the lane's OWN ring Z[omega] (omega^2 = omega - 1,
     omega acting as 1 + M), and the module is FREE OF RANK 3
     (an explicit basis with unimodular determinant is searched;
     found => certified).  The boundary lattice computes in the same
     ring as the whole 27-stack.
  F2 (THE Z/3 = F_3 = Z[omega]/theta): disc(E6) = 3; the discriminant
     group E6*/E6 is Z/3 (Smith form diag(1,1,1,1,1,3)); and M acts
     TRIVIALLY on it ((M - I)*adj(G) = 0 mod 3 exactly) — the disc
     group is the residue field of the SAME theta = sqrt(-3) whose
     double memo 100 derived as the cusp modulus (tau = +-2 theta)
     from a grammar word.  One theta, both ends.
  F3 (THE PRIMARY CONTENT IS THE 27-STACK): enumerating E6* exactly
     (Fincke-Pohst with exact rational partial norms): the trivial
     coset's norm-2 count is 72 (the e6 roots); each nontrivial
     coset's minimal vectors number EXACTLY 27 at norm 4/3 — the
     boundary theory's three primaries have ground multiplicities
     {1, 27, 27} and conformal weights {0, 2/3, 2/3}: the record's
     27 + its conjugate, nothing else.
  F4 (THE CURRENT ALGEBRA IS e6): the vacuum character's level-1
     coefficient, computed from the lattice alone (theta series /
     eta^6 as an exact q-expansion), is 6 + 72 = 78 = dim e6 — the
     boundary current algebra is the lane's own e6; central charge
     c = rank = 6 (automatic for a lattice theory; = 6 sigma at
     sigma = 1, cc's census-row typing, interpretive label).
FENCES: this cell builds the BOUNDARY OBJECT and certifies its
content; it does NOT build the bridge to the record's q-series —
GC-12's exclusion (no banked q-series candidate on either seat's
artifacts) stands, and the bridge remains the route's open half.
"Boundary CFT" is L154's language; every claim made here is
lattice-arithmetic and exact.  Modular S-matrix not computed
(documentary note only).  Gate 5 untouched.
"""
from fractions import Fraction as Fr
from itertools import product, combinations
import sympy as sp
from sympy import Matrix, ZZ
from sympy.matrices.normalforms import smith_normal_form

# ---- E6 Cartan/Gram (Bourbaki numbering: chain 1-3-4-5-6, node 2 on 4)
G = Matrix([
    [ 2,  0, -1,  0,  0,  0],
    [ 0,  2,  0, -1,  0,  0],
    [-1,  0,  2, -1,  0,  0],
    [ 0, -1, -1,  2, -1,  0],
    [ 0,  0,  0, -1,  2, -1],
    [ 0,  0,  0,  0, -1,  2]])
assert G.T == G and G.det() == 3
I6 = sp.eye(6)

# simple reflections on the root basis: s_i = I - e_i (row_i of G)
def refl(i):
    S = sp.eye(6)
    for j in range(6):
        S[i, j] -= G[i, j]
    return S
c = sp.eye(6)
for i in range(6):
    c = c * refl(i)
assert (c.T * G * c - G) == sp.zeros(6, 6)
assert c**12 == I6 and all(c**k != I6 for k in (1, 2, 3, 4, 6))   # Coxeter order 12
M = c**4
assert M**3 == I6 and M != I6
assert (M**2 + M + I6) == sp.zeros(6, 6)                          # FIXED-POINT-FREE, exactly
assert (M.T * G * M - G) == sp.zeros(6, 6)
print("F1a: the Coxeter element c has order 12; M = c^4 satisfies M^2 + M + I = 0")
print("     EXACTLY and preserves the Gram form — a fixed-point-free order-3")
print("     isometry: E6 is a Z[omega]-lattice (omega := 1 + M; omega^2 = omega - 1")
print("     holds because (1+M)^2 - (1+M) + I = M^2 + M + I = 0).")

# free rank-3 basis: v1, M v1, v2, M v2, v3, M v3 unimodular
basis = None
for tri in combinations(range(6), 3):
    vs = [Matrix([1 if k == t else 0 for k in range(6)]) for t in tri]
    B = Matrix.hstack(*[col for v in vs for col in (v, M*v)])
    if abs(B.det()) == 1:
        basis = (tri, B)
        break
assert basis is not None, "no unimodular triple among standard vectors — enlarge search"
tri, B = basis
print(f"F1b: FREE RANK 3 — {{alpha_{tri[0]+1}, alpha_{tri[1]+1}, alpha_{tri[2]+1}}} with their")
print(f"     M-images form a Z-basis (det = {B.det()}): E6 = Z[omega]^3 as a module")
print("     over the lane's pair-field ring.  The boundary lattice is Eisenstein.")

# ---- F2: disc group Z/3, M trivial on it, theta tie
D = smith_normal_form(G, domain=ZZ)
sdiag = sorted(abs(D[i, i]) for i in range(6))
assert sdiag == [1, 1, 1, 1, 1, 3], sdiag
adjG = G.adjugate()
assert G * adjG == 3 * I6
T = (M - I6) * adjG
assert all(T[i, j] % 3 == 0 for i in range(6) for j in range(6))
print("F2: Smith(G) = diag(1,1,1,1,1,3) — E6*/E6 = Z/3;  (M - I) adj(G) = 0 mod 3")
print("    EXACTLY => M acts trivially on the disc group: E6*/E6 is a module over")
print("    Z[omega]/theta = F_3, the residue field of theta = sqrt(-3) = 2 omega - 1 —")
print("    the SAME theta whose double is memo 100's grammar-derived cusp modulus.")

# label functional: l with G l = 0 mod 3 (kernel of G over F_3 is 1-dimensional)
lvec = None
for cand in product(range(3), repeat=6):
    if any(cand) and all(sum(G[i, j]*cand[j] for j in range(6)) % 3 == 0 for i in range(6)):
        lvec = cand
        break
assert lvec is not None
print(f"    label functional l = {lvec} (G l = 0 mod 3): coset(y) = l . a mod 3.")

# ---- F3: exact enumeration of E6* up to norm 4 (Fincke-Pohst, exact at the leaf)
Q = G.inv()                       # Gram of the dual basis; norms a^T Q a
n = 6
# rational Cholesky q[i][j] (Cohen alg. 2.7.3 style)
q = [[Fr(int(Q[i, j].p), int(Q[i, j].q)) for j in range(n)] for i in range(n)]
for i in range(n):
    for j in range(i+1, n):
        q[j][i] = q[i][j]
        q[i][j] = q[i][j] / q[i][i]
    for k in range(i+1, n):
        for l in range(k, n):
            q[k][l] = q[k][l] - q[k][i]*q[i][l]
BOUND = Fr(4)
import math
counts = {}                       # (norm as Fraction, coset label) -> count
def enum(level, center, remaining, partial):
    """x[level] loop; center/remaining exact; partial = list of chosen coords above."""
    if remaining < 0:
        return
    span = math.sqrt(float(remaining / q[level][level])) + 1.0
    lo = math.ceil(float(-center) - span)
    hi = math.floor(float(-center) + span)
    for xl in range(lo, hi + 1):
        t = q[level][level] * (Fr(xl) + center)**2
        if t > remaining:
            continue
        coords = [xl] + partial
        if level == 0:
            a = coords
            norm = BOUND - (remaining - t)
            lab = sum(lvec[i]*a[i] for i in range(n)) % 3
            key = (norm, lab)
            counts[key] = counts.get(key, 0) + 1
        else:
            # center for level-1: sum_{j >= level} q[level-1][j] x_j
            cc_ = sum(q[level-1][j] * Fr(coords[j - level]) for j in range(level, n))
            enum(level - 1, cc_, remaining - t, coords)
enum(n - 1, Fr(0), BOUND, [])
# drop the zero vector from coset-0 count bookkeeping explicitly:
assert counts[(Fr(0), 0)] == 1
roots = counts.get((Fr(2), 0), 0)
min1 = counts.get((Fr(4, 3), 1), 0)
min2 = counts.get((Fr(4, 3), 2), 0)
assert roots == 72, roots
assert min1 == 27 and min2 == 27, (min1, min2)
# no nontrivial-coset vector below 4/3; coset-0 norms are even integers (E6 even);
# nontrivial-coset norms are 1/3 mod 1:
assert all(lab == 0 or nm >= Fr(4, 3) for (nm, lab) in counts)
assert all(nm.denominator == 1 and int(nm) % 2 == 0 for (nm, lab) in counts if lab == 0)
assert all(nm % 1 == Fr(1, 3) for (nm, lab) in counts if lab != 0)
print("F3: EXACT enumeration of E6* (norm <= 4):")
for key in sorted(counts, key=lambda k: (k[0], k[1])):
    print(f"      norm {str(key[0]):>4s}  coset {key[1]}:  {counts[key]} vectors")
print("    the trivial coset has 72 norm-2 vectors (the e6 ROOTS); each nontrivial")
print("    coset has EXACTLY 27 minimal vectors at norm 4/3 => the three primaries")
print("    carry ground multiplicities {1, 27, 27} at conformal weights {0, 2/3, 2/3}")
print("    — the boundary theory's matter content IS the record's 27 + conjugate.")

# ---- F4: vacuum character level-1 coefficient from the lattice alone
# chi_0 = Theta_0(q) / eta(q)^6 ~ q^{-1/4} (sum_m dim_m q^m);  dim_1 = 6 + 72
NCUT = 4
theta0 = [0]*(NCUT+1)
for (nm, lab), cnt in counts.items():
    if lab == 0 and int(nm)//2 <= NCUT:      # even lattice: exponent m = norm/2
        theta0[int(nm)//2] += cnt
# 1/phi(q)^6 coefficients (phi = Euler function), exact by convolution:
euler = [1] + [0]*NCUT
for k in range(1, NCUT+1):                     # multiply by (1 - q^k) each
    for m in range(NCUT, k-1, -1):
        euler[m] -= euler[m-k]
inv6 = [Fr(1)] + [Fr(0)]*NCUT                  # invert euler^6 as a power series
e6s = [Fr(c_) for c_ in euler]
pw = [Fr(0)]*(NCUT+1)                          # euler^6
pw[0] = Fr(1)
for _ in range(6):
    new = [Fr(0)]*(NCUT+1)
    for a_ in range(NCUT+1):
        for b_ in range(NCUT+1-a_):
            new[a_+b_] += pw[a_]*e6s[b_]
    pw = new
for m in range(1, NCUT+1):                     # series inverse of pw
    inv6[m] = -sum(pw[k]*inv6[m-k] for k in range(1, m+1)) / pw[0]
vac = [sum(Fr(theta0[a_])*inv6[m-a_] for a_ in range(m+1)) for m in range(NCUT+1)]
assert vac[0] == 1 and vac[1] == 78, vac[:2]
# the 27-primary's level-1 coefficient, same machinery on coset 1:
theta1 = {}
for (nm, lab), cnt in counts.items():
    if lab == 1:
        theta1[nm] = cnt
c27 = [Fr(0)]*(NCUT+1)
for nm, cnt in theta1.items():
    m = (nm - Fr(4, 3)) / 2                    # weight above the primary: (|y|^2 - 4/3)/2
    assert m.denominator == 1
    if int(m) <= NCUT:
        c27[int(m)] += cnt
lev27 = [sum(c27[a_]*inv6[m-a_] for a_ in range(m+1)) for m in range(NCUT+1)]
print(f"F4: vacuum character (exact, from the lattice alone): dims {[int(v) for v in vac[:3]]} —")
print("    level 1 = 6 + 72 = 78 = dim e6 EXACTLY: the boundary current algebra is")
print(f"    the lane's own e6.  The 27-primary's tower begins {[int(v) for v in lev27[:2]]}.")
print("    c = rank = 6 (lattice theory; = 6 sigma at sigma = 1 — census-row typing,")
print("    interpretive label).")

print("""
THE ROUTE'S FIRST STEP IS BUILT: L154's E6-lattice boundary object
exists, is EISENSTEIN (a free rank-3 module over the lane's own
Z[omega]), has discriminant group F_3 = Z[omega]/theta with the SAME
theta as the grammar-derived cusp modulus (memo 100), and its exact
content is {vacuum + 27 + 27-bar} with current algebra e6 (78) at
c = 6.  Every number the boundary theory opens with is a banked
number of the record.  WHAT REMAINS OPEN on this route (stated, not
waved at): the BRIDGE — a map between this boundary theory's
characters and a record-side q-series; GC-12's exclusion (no banked
q-series candidate in either seat's artifacts) still stands, so the
bridge needs NEW mathematics, not retrieval.  Gate 5 untouched.""")
