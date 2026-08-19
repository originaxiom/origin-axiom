#!/usr/bin/env python3
"""
INDEPENDENT verification (exact arithmetic over Q(sqrt2), via Python Fractions)
of a claimed order-96 group Ghat = < 2T-copy, g_tau, g_sigma > acting R-linearly
on R^7 = R^3 (+) H.

Written from scratch for an independent audit. Does NOT import, read, or in any
way consult cloud_handoff/certificates/g2cone.py or g2strata.py.

All group-closure and rank/nullspace computations are done EXACTLY in the field
Q(sqrt2) = {a + b*sqrt2 : a,b in Q}, represented as pairs of Python Fractions.
Rank of a matrix with entries in a subfield K of R is the same whether computed
over K or over R (rank = size of largest nonvanishing minor, and a minor is a
polynomial in the entries, hence vanishes in K iff it vanishes in R), so exact
K-rank computations below settle the real fixed-space dimensions exactly, with
no numerical tolerance anywhere in this script.
"""

from fractions import Fraction as F
import itertools
from collections import Counter

# =====================================================================
# Exact Q(sqrt2) arithmetic
# =====================================================================

class Q2:
    __slots__ = ('a', 'b')  # value = a + b*sqrt(2), a,b in Q

    def __init__(self, a=0, b=0):
        self.a = a if isinstance(a, F) else F(a)
        self.b = b if isinstance(b, F) else F(b)

    @staticmethod
    def _c(o):
        return o if isinstance(o, Q2) else Q2(o)

    def __add__(self, o):
        o = Q2._c(o)
        return Q2(self.a + o.a, self.b + o.b)
    __radd__ = __add__

    def __sub__(self, o):
        o = Q2._c(o)
        return Q2(self.a - o.a, self.b - o.b)

    def __rsub__(self, o):
        o = Q2._c(o)
        return Q2(o.a - self.a, o.b - self.b)

    def __neg__(self):
        return Q2(-self.a, -self.b)

    def __mul__(self, o):
        o = Q2._c(o)
        # (a+b*r)(c+d*r) = (ac+2bd) + (ad+bc)*r,  r=sqrt2, r^2=2
        return Q2(self.a * o.a + 2 * self.b * o.b, self.a * o.b + self.b * o.a)
    __rmul__ = __mul__

    def is_zero(self):
        return self.a == 0 and self.b == 0

    def __eq__(self, o):
        o = Q2._c(o)
        return self.a == o.a and self.b == o.b

    def __hash__(self):
        return hash((self.a, self.b))

    def inv(self):
        denom = self.a * self.a - 2 * self.b * self.b
        if denom == 0:
            raise ZeroDivisionError("Q2 element is not invertible (equals zero)")
        return Q2(self.a / denom, -self.b / denom)

    def __truediv__(self, o):
        o = Q2._c(o)
        return self * o.inv()

    def __repr__(self):
        return f"({self.a}+{self.b}*sqrt2)"


def sum_q2(it):
    s = Q2(0)
    for x in it:
        s = s + x
    return s


HALF = F(1, 2)
INV_SQRT2 = Q2(0, HALF)  # 0 + (1/2)*sqrt2 = sqrt2/2 = 1/sqrt2, exactly

assert INV_SQRT2 * INV_SQRT2 == Q2(HALF), "(1/sqrt2)^2 should equal 1/2"

# =====================================================================
# Quaternion arithmetic; components are Q2
# =====================================================================

def qmul(p, q):
    a1, b1, c1, d1 = p
    a2, b2, c2, d2 = q
    a = a1 * a2 - b1 * b2 - c1 * c2 - d1 * d2
    b = a1 * b2 + b1 * a2 + c1 * d2 - d1 * c2
    c = a1 * c2 - b1 * d2 + c1 * a2 + d1 * b2
    d = a1 * d2 + b1 * c2 - c1 * b2 + d1 * a2
    return (a, b, c, d)


def qnorm2(q):
    a, b, c, d = q
    return a * a + b * b + c * c + d * d


ONE_Q = (Q2(1), Q2(0), Q2(0), Q2(0))

E4 = [
    (Q2(1), Q2(0), Q2(0), Q2(0)),
    (Q2(0), Q2(1), Q2(0), Q2(0)),
    (Q2(0), Q2(0), Q2(1), Q2(0)),
    (Q2(0), Q2(0), Q2(0), Q2(1)),
]


def left_mult_matrix(q):
    """4x4 matrix M with M @ h == q*h (quaternion product), h a column 4-vector."""
    cols = [qmul(q, e) for e in E4]
    return [[cols[j][i] for j in range(4)] for i in range(4)]


def right_mult_matrix(p):
    """4x4 matrix M with M @ h == h*p (quaternion product), h a column 4-vector."""
    cols = [qmul(e, p) for e in E4]
    return [[cols[j][i] for j in range(4)] for i in range(4)]


def qkey(q):
    return tuple((c.a, c.b) for c in q)


# sanity: standard Hamilton relations
i_q = (Q2(0), Q2(1), Q2(0), Q2(0))
j_q = (Q2(0), Q2(0), Q2(1), Q2(0))
k_q = (Q2(0), Q2(0), Q2(0), Q2(1))
neg1_q = (Q2(-1), Q2(0), Q2(0), Q2(0))
assert qkey(qmul(i_q, i_q)) == qkey(neg1_q)
assert qkey(qmul(j_q, j_q)) == qkey(neg1_q)
assert qkey(qmul(k_q, k_q)) == qkey(neg1_q)
assert qkey(qmul(i_q, j_q)) == qkey(k_q)
assert qkey(qmul(j_q, i_q)) == qkey((Q2(0), Q2(0), Q2(0), Q2(-1)))
assert qkey(qmul(j_q, k_q)) == qkey(i_q)
assert qkey(qmul(k_q, i_q)) == qkey(j_q)
print("[self-check] Hamilton relations i^2=j^2=k^2=-1, ij=k, ji=-k, jk=i, ki=j : OK")

# =====================================================================
# Generic exact matrix ops over Q2
# =====================================================================

def identity(n):
    return [[Q2(1) if i == j else Q2(0) for j in range(n)] for i in range(n)]


def zeros(n, m):
    return [[Q2(0) for _ in range(m)] for _ in range(n)]


def matmul(A, B):
    n = len(A); k = len(B); m = len(B[0])
    assert len(A[0]) == k
    return [[sum_q2(A[i][t] * B[t][j] for t in range(k)) for j in range(m)] for i in range(n)]


def mat_sub(A, B):
    return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]


def mat_vec(M, v):
    return [sum_q2(M[i][j] * v[j] for j in range(len(v))) for i in range(len(M))]


def transpose(A):
    return [[A[j][i] for j in range(len(A))] for i in range(len(A[0]))]


def block_diag(A, B):
    na = len(A); nb = len(B); n = na + nb
    M = zeros(n, n)
    for i in range(na):
        for j in range(na):
            M[i][j] = A[i][j]
    for i in range(nb):
        for j in range(nb):
            M[na + i][na + j] = B[i][j]
    return M


def mat_eq(A, B):
    return all(A[i][j] == B[i][j] for i in range(len(A)) for j in range(len(A[0])))


def mat_key(M):
    return tuple(tuple((e.a, e.b) for e in row) for row in M)


def diag3(a, b, c):
    return [[Q2(a), Q2(0), Q2(0)], [Q2(0), Q2(b), Q2(0)], [Q2(0), Q2(0), Q2(c)]]


# =====================================================================
# Exact RREF / rank / nullspace over Q2  (field, since Q(sqrt2) is a field)
# =====================================================================

def rref(mat):
    M = [row[:] for row in mat]
    nrows = len(M)
    ncols = len(M[0]) if nrows else 0
    pivots = []
    r = 0
    for c in range(ncols):
        piv = None
        for i in range(r, nrows):
            if not M[i][c].is_zero():
                piv = i
                break
        if piv is None:
            continue
        M[r], M[piv] = M[piv], M[r]
        inv = M[r][c].inv()
        M[r] = [x * inv for x in M[r]]
        for i in range(nrows):
            if i != r and not M[i][c].is_zero():
                f = M[i][c]
                M[i] = [M[i][jj] - f * M[r][jj] for jj in range(ncols)]
        pivots.append(c)
        r += 1
        if r == nrows:
            break
    return M, pivots


def rank(mat):
    _, piv = rref(mat)
    return len(piv)


def nullspace_basis(mat, ncols):
    R, pivots = rref(mat)
    free = [c for c in range(ncols) if c not in pivots]
    basis = []
    for fc in free:
        vec = [Q2(0) for _ in range(ncols)]
        vec[fc] = Q2(1)
        for i, pc in enumerate(pivots):
            vec[pc] = -R[i][fc]
        basis.append(vec)
    return basis


def canonical_subspace_key(row_vectors):
    if len(row_vectors) == 0:
        return tuple()
    R, pivots = rref(row_vectors)
    rk = len(pivots)
    nz = R[:rk]
    return tuple(tuple((v.a, v.b) for v in row) for row in nz)


print("[self-check] exact RREF/rank/nullspace routines defined over Q(sqrt2)")

# =====================================================================
# Build 2T (binary tetrahedral group), order 24, as Hurwitz units
# =====================================================================

twoT = []
for idx in range(4):
    for s in (1, -1):
        vec = [Q2(0), Q2(0), Q2(0), Q2(0)]
        vec[idx] = Q2(s)
        twoT.append(tuple(vec))
for signs in itertools.product((1, -1), repeat=4):
    twoT.append(tuple(Q2(F(s, 2)) for s in signs))

assert len(twoT) == 24, len(twoT)
for q in twoT:
    assert qnorm2(q) == Q2(1), ("not unit norm", q)

twoT_set = set(qkey(q) for q in twoT)
assert len(twoT_set) == 24  # no duplicates

closed = True
for p in twoT:
    for q in twoT:
        if qkey(qmul(p, q)) not in twoT_set:
            closed = False
print(f"[self-check] 2T: 24 distinct unit Hurwitz quaternions, closed under multiplication "
      f"(all 576 pairwise products checked): {closed}")

# element-order distribution within 2T (bonus sanity check against known SL(2,3) structure)
def qorder(q):
    cur = q
    o = 1
    while qkey(cur) != qkey(ONE_Q):
        cur = qmul(cur, q)
        o += 1
        if o > 24:
            raise RuntimeError("2T element order exceeds group order -- bug")
    return o

order_dist = Counter(qorder(q) for q in twoT)
print(f"[self-check] 2T element-order distribution: {dict(sorted(order_dist.items()))} "
      f"(expected {{1:1, 2:1, 4:6, 3:8, 6:8}} for the binary tetrahedral group)")

# =====================================================================
# Build the 7x7 generators
# =====================================================================

I3 = identity(3)
I4 = identity(4)
I7 = identity(7)

rot_axis1 = diag3(1, -1, -1)   # pi-rotation of R^3 about axis 1 (x-axis)
rot_axis3 = diag3(-1, -1, 1)   # pi-rotation of R^3 about axis 3 (z-axis)

w_q = (INV_SQRT2, INV_SQRT2, Q2(0), Q2(0))   # w = (1+i)/sqrt2
assert qnorm2(w_q) == Q2(1), "w should be a unit quaternion"

R_i = right_mult_matrix(i_q)
R_k = right_mult_matrix(k_q)
L_w = left_mult_matrix(w_q)

g_tau_H = R_i
g_tau = block_diag(rot_axis1, g_tau_H)

g_sigma_H = matmul(L_w, R_k)
g_sigma = block_diag(rot_axis3, g_sigma_H)

twoT_matrices = [block_diag(I3, left_mult_matrix(q)) for q in twoT]
generators = twoT_matrices + [g_tau, g_sigma]

# structural pre-check: every generator is block-diagonal (R^3 (+) H, no mixing)
for M in generators:
    for i in range(3):
        for j in range(3, 7):
            assert M[i][j].is_zero()
    for i in range(3, 7):
        for j in range(3):
            assert M[i][j].is_zero()
print("[self-check] all 26 generators (24 from 2T + g_tau + g_sigma) are block-diagonal "
      "on R^3 (+) H: OK")

# orthogonality pre-check: M^T M == I for every generator (catches formula bugs early)
ortho_ok = True
for M in generators:
    P = matmul(transpose(M), M)
    if not mat_eq(P, I7):
        ortho_ok = False
print(f"[self-check] all generators orthogonal (M^T M = I_7), exactly: {ortho_ok}")
assert ortho_ok

# order of g_tau, g_sigma individually (diagnostic only)
def mat_order(M, cap=200):
    cur = M
    o = 1
    while mat_key(cur) != mat_key(I7):
        cur = matmul(cur, M)
        o += 1
        if o > cap:
            return None
    return o

print(f"[self-check] order(g_tau) = {mat_order(g_tau)}, order(g_sigma) = {mat_order(g_sigma)}")

# =====================================================================
# ITEM 1: BFS closure of < 2T-copy, g_tau, g_sigma >
# =====================================================================

MAX_GROUP_SIZE = 20000
seen = {mat_key(I7): I7}
frontier = [I7]
while frontier:
    nxt = []
    for M in frontier:
        for g in generators:
            P = matmul(M, g)
            k = mat_key(P)
            if k not in seen:
                seen[k] = P
                nxt.append(P)
    frontier = nxt
    if len(seen) > MAX_GROUP_SIZE:
        break

group = list(seen.values())
print()
print("=" * 70)
print(f"ITEM 1: |Ghat| (exact closure) = {len(group)}   (claim: 96)")

twoT_copy_set = set(mat_key(M) for M in twoT_matrices)
assert len(twoT_copy_set) == 24
is_subgroup = twoT_copy_set.issubset(seen.keys())
index = len(group) / 24 if is_subgroup else None
print(f"ITEM 1: 2T-copy (24 elts) subset of Ghat: {is_subgroup};  |Ghat|/24 = {index}   (claim: index 4)")
item1_pass = (len(group) == 96) and is_subgroup and (index == 4)
print(f"ITEM 1 RESULT: {'PASS' if item1_pass else 'FAIL'}")

# =====================================================================
# ITEM 2: fixed-subspace dimension census over the 95 nonidentity elements
# =====================================================================

census = {}
type_counts = {}
id_key = mat_key(I7)
for M in group:
    if mat_key(M) == id_key:
        continue
    # confirm block-diagonal structure persists for every group element
    for i in range(3):
        for j in range(3, 7):
            assert M[i][j].is_zero(), "off-diagonal block nonzero -- representation not R^3(+)H-preserving!"
    for i in range(3, 7):
        for j in range(3):
            assert M[i][j].is_zero()
    M3 = [row[:3] for row in M[:3]]
    M4 = [row[3:] for row in M[3:]]
    d3 = 3 - rank(mat_sub(M3, I3))
    d4 = 4 - rank(mat_sub(M4, I4))
    dtot = 7 - rank(mat_sub(M, I7))
    assert dtot == d3 + d4, (dtot, d3, d4)
    census[dtot] = census.get(dtot, 0) + 1
    type_counts[(d3, d4)] = type_counts.get((d3, d4), 0) + 1

print()
print("=" * 70)
print(f"ITEM 2: fixed-space dimension census over 95 nonidentity elements: {census}")
print(f"ITEM 2: (dim_fix_R3, dim_fix_H) type breakdown: {type_counts}")
claimed_census = {3: 53, 1: 42}
item2_pass = (census == claimed_census) and (0 not in census) and set(census.keys()) == {3, 1}
print(f"ITEM 2 RESULT: {'PASS' if item2_pass else 'FAIL'}  (claim: {claimed_census}, no dim-0, no other dims)")

# =====================================================================
# ITEM 3: pointwise stabilizer of R^3 (+) 0
# =====================================================================

S3 = [M for M in group if mat_eq([row[:3] for row in M[:3]], I3)]
S3_keys = set(mat_key(M) for M in S3)
equals_2T = (S3_keys == twoT_copy_set)
print()
print("=" * 70)
print(f"ITEM 3: |pointwise-stabilizer(R^3 (+) 0)| = {len(S3)}   (claim: 24)")
print(f"ITEM 3: equals the left-2T copy exactly: {equals_2T}")
item3_pass = (len(S3) == 24) and equals_2T
print(f"ITEM 3 RESULT: {'PASS' if item3_pass else 'FAIL'}")

# =====================================================================
# ITEM 5 (computed before 4 since item 4 uses the axis machinery too):
# stabilizers of the three coordinate axis lines
# =====================================================================

axis_vectors = []
for idx in range(3):
    v = [Q2(0)] * 7
    v[idx] = Q2(1)
    axis_vectors.append(v)

axis_stab_orders = []
axis_stab_sets = []
for v in axis_vectors:
    stab = [M for M in group if all(mat_vec(M, v)[t] == v[t] for t in range(7))]
    axis_stab_orders.append(len(stab))
    axis_stab_sets.append(set(mat_key(M) for M in stab))

print()
print("=" * 70)
print(f"ITEM 5: pointwise-stabilizer orders of the three coordinate axis lines "
      f"(x,y,z) = {axis_stab_orders}   (claim: [48,48,48])")
item5_pass = all(o == 48 for o in axis_stab_orders)
print(f"ITEM 5 RESULT: {'PASS' if item5_pass else 'FAIL'}")

# cross-check: each axis-stabilizer should contain the 2T-copy (order 24) as an index-2 subgroup
for idx, sset in enumerate(axis_stab_sets):
    contains2T = twoT_copy_set.issubset(sset)
    print(f"    axis {idx+1} stabilizer contains 2T-copy: {contains2T}, "
          f"index of 2T-copy in it: {len(sset)/24 if contains2T else 'n/a'}")

# =====================================================================
# ITEM 4: planes of the form (axis line in R^3) (+) (2-plane in H)
#         with pointwise stabilizer Z2; count + orbit sizes under Ghat
# =====================================================================

special = []  # (M, basis) with (d3,d4) = (1,2)
for M in group:
    if mat_key(M) == id_key:
        continue
    M3 = [row[:3] for row in M[:3]]
    M4 = [row[3:] for row in M[3:]]
    d3 = 3 - rank(mat_sub(M3, I3))
    d4 = 4 - rank(mat_sub(M4, I4))
    if (d3, d4) == (1, 2):
        basis = nullspace_basis(mat_sub(M, I7), 7)
        assert len(basis) == 3
        special.append((M, basis))

print()
print("=" * 70)
print(f"ITEM 4: number of nonidentity elements with (dim_fix_R3, dim_fix_H) = (1,2): {len(special)}")

plane_map = {}  # canonical key -> list of M's whose fixed space equals this plane
plane_basis = {}
for M, basis in special:
    key = canonical_subspace_key(basis)
    plane_map.setdefault(key, []).append(M)
    plane_basis.setdefault(key, basis)

print(f"ITEM 4: number of DISTINCT planes among these fixed spaces: {len(plane_map)}")
mult_dist = Counter(len(v) for v in plane_map.values())
print(f"ITEM 4: (elements-per-plane) multiplicity distribution: {dict(mult_dist)}")

# direct pointwise-stabilizer computation for every distinct plane (not assumed -- checked
# against ALL 96 group elements)
plane_keys = list(plane_map.keys())
pw_stab_orders = []
pw_stab_details = []
for key in plane_keys:
    basis = plane_basis[key]
    stab = [M for M in group if all(all(mat_vec(M, v)[t] == v[t] for t in range(7)) for v in basis)]
    pw_stab_orders.append(len(stab))
    pw_stab_details.append(stab)

pw_stab_dist = Counter(pw_stab_orders)
print(f"ITEM 4: pointwise-stabilizer-order distribution over the {len(plane_keys)} planes: "
      f"{dict(pw_stab_dist)}   (claim: all exactly 2)")
item4_stab_pass = all(o == 2 for o in pw_stab_orders)

# which coordinate axis does each plane's line-component sit on? (diagnostic)
def axis_of_plane(basis):
    # basis has 3 vectors in R^7; the R^3-part (coords 0,1,2) spans a line.
    r3parts = [row[:3] for row in basis]
    _, piv = rref(r3parts)
    assert len(piv) == 1, ("expected a 1-dim R^3 part", r3parts)
    # find the nonzero coordinate pattern
    R, pivots = rref(r3parts)
    nzrow = R[0]
    nz_idx = [i for i in range(3) if not nzrow[i].is_zero()]
    return tuple(nz_idx)

axis_tally = Counter(axis_of_plane(plane_basis[k]) for k in plane_keys)
print(f"ITEM 4: axis-line diagnostic (which R^3 coordinate is nonzero in each plane's line part): "
      f"{dict(axis_tally)}")

# orbits of Ghat acting on these planes by pushforward: h . P = h(P)
plane_key_set = set(plane_keys)
visited = set()
orbits = []
orbit_membership = {}
for key in plane_keys:
    if key in visited:
        continue
    basis = plane_basis[key]
    orbit_keys = set()
    for M in group:
        image_basis = [mat_vec(M, v) for v in basis]
        ik = canonical_subspace_key(image_basis)
        orbit_keys.add(ik)
    for k in orbit_keys:
        assert k in plane_key_set, "Ghat-action left the family of 30 planes -- unexpected!"
    visited |= orbit_keys
    orbits.append(sorted(orbit_keys))

orbit_sizes = sorted(len(o) for o in orbits)
print(f"ITEM 4: number of orbits under Ghat = {len(orbits)}, orbit sizes = {orbit_sizes}   (claim: [6,12,12])")

item4_pass = (len(special) == 30 and len(plane_map) == 30 and item4_stab_pass
              and orbit_sizes == [6, 12, 12])
print(f"ITEM 4 RESULT: {'PASS' if item4_pass else 'FAIL'}")

# =====================================================================
# FINAL SUMMARY
# =====================================================================
print()
print("=" * 70)
print("FINAL SUMMARY (exact Q(sqrt2) arithmetic)")
print("=" * 70)
print(f"ITEM 1 (order 96, 2T index 4):                {'PASS' if item1_pass else 'FAIL'}")
print(f"ITEM 2 (census {{3:53,1:42}}, no dim-0):        {'PASS' if item2_pass else 'FAIL'}")
print(f"ITEM 3 (stab(R^3)=2T-copy, order 24):          {'PASS' if item3_pass else 'FAIL'}")
print(f"ITEM 4 (3 orbits of 30 planes, sizes 6,12,12, stab Z2): {'PASS' if item4_pass else 'FAIL'}")
print(f"ITEM 5 (3 axis stabilizers all order 48):      {'PASS' if item5_pass else 'FAIL'}")
