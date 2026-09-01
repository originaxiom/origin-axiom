#!/usr/bin/env python3
"""
R26 (B) -- blind recomputation of B1011 C5/C6 forced counts 992 / 284, written BEFORE
opening b1011_cells.py / b1011_exact.py / tests.

Claim (as read from FINDINGS C5 + PREREGISTRATION item 5):
  theta-odd  forced  <=>  A in ker(chi)  or  B in Z(2I);   value Re chi(A) * (1/2) tr V2(B)
  theta-even forced  <=>  A in Z(2T)     or  B in Z(2I);   value (1/2)tr V2(A) * (1/2)tr V2(B)
  counts: odd 8*120 + 24*2 - 8*2 = 992 ; even 2*120 + 24*2 - 2*2 = 284.
  C6: theta-even value set {0, +-1/4, +-1/(4phi), +-1/2, +-1/(2phi), +-phi/4, +-phi/2, +-1}.

Independent instrument.  Build 2T (24 Hurwitz units) and 2I (120 icosians) explicitly
as unit quaternions over Q(sqrt5) (exact: pairs of Fractions), V2 = the SU(2) matrix of
left multiplication, chi = the Z3 character of 2T with kernel Q8 (assigned by coset,
multiplicativity verified on all 576 pairs).  Then for EVERY pair (A,B) form the actual
representing matrix
     M_odd  = chi(A) * V2(B)            (2x2)
     M_even = V2(A) (x) V2(B)           (4x4)
and call the cell FORCED iff the Hermitian part (M + M^dagger)/2 is a SCALAR matrix --
i.e. the real quadratic form Re <u, M u> is independent of the listener u.  This
criterion never mentions ker(chi) or the centres; if the arc's definition is the right
reading, the two must agree cell-by-cell.  Values are read off as the scalar.
"""
from fractions import Fraction as Fr
from itertools import product, permutations

# ---------------------------------------------------------------- Q(sqrt5)
class Q5:
    __slots__ = ('a', 'b')            # a + b*sqrt5
    def __init__(self, a, b=0): self.a = Fr(a); self.b = Fr(b)
    def __add__(s, o): o = _q(o); return Q5(s.a + o.a, s.b + o.b)
    __radd__ = __add__
    def __neg__(s): return Q5(-s.a, -s.b)
    def __sub__(s, o): return s + (-_q(o))
    def __rsub__(s, o): return _q(o) - s
    def __mul__(s, o): o = _q(o); return Q5(s.a * o.a + 5 * s.b * o.b, s.a * o.b + s.b * o.a)
    __rmul__ = __mul__
    def __truediv__(s, o):
        o = _q(o); n = o.a * o.a - 5 * o.b * o.b
        return s * Q5(o.a / n, -o.b / n)
    def __eq__(s, o): o = _q(o); return s.a == o.a and s.b == o.b
    def __hash__(s): return hash((s.a, s.b))
    def __repr__(s):
        if s.b == 0: return str(s.a)
        return f"({s.a}+{s.b}r5)"
def _q(x): return x if isinstance(x, Q5) else Q5(x)
ZERO, ONE = Q5(0), Q5(1)
R5 = Q5(0, 1)
PHI = (ONE + R5) / 2
PHIINV = (R5 - ONE) / 2
assert PHI * PHIINV == ONE

# ---------------------------------------------------------------- quaternions
class Quat:
    __slots__ = ('c',)
    def __init__(self, a, b, c, d): self.c = (_q(a), _q(b), _q(c), _q(d))
    def __mul__(s, o):
        a1, b1, c1, d1 = s.c; a2, b2, c2, d2 = o.c
        return Quat(a1*a2 - b1*b2 - c1*c2 - d1*d2,
                    a1*b2 + b1*a2 + c1*d2 - d1*c2,
                    a1*c2 - b1*d2 + c1*a2 + d1*b2,
                    a1*d2 + b1*c2 - c1*b2 + d1*a2)
    def __eq__(s, o): return s.c == o.c
    def __hash__(s): return hash(s.c)
    def norm(s): return sum((x * x for x in s.c), ZERO)
    def __repr__(s): return f"Q{s.c}"

H = Fr(1, 2)
hurwitz = [Quat(*v) for v in ([(1,0,0,0),(0,1,0,0),(0,0,1,0),(0,0,0,1)])]
T2 = set()
for q in hurwitz:
    T2.add(q); T2.add(Quat(*[-x for x in q.c]))
for s in product((H, -H), repeat=4):
    T2.add(Quat(*s))
T2 = sorted(T2, key=repr)
assert len(T2) == 24

# icosians: Hurwitz units + (1/2)(0, +-1, +-phi^-1, +-phi) under even permutations
even_perms = [p for p in permutations(range(4)) if sum(1 for i in range(4) for j in range(i) if p[j] > p[i]) % 2 == 0]
I2 = set(T2)
base = [ZERO, ONE, PHIINV, PHI]
for p in even_perms:
    for s in product((1, -1), repeat=3):
        v = [None] * 4
        vals = [ZERO, s[0] * ONE, s[1] * PHIINV, s[2] * PHI]
        for i in range(4): v[p[i]] = vals[i]
        I2.add(Quat(*[x * H for x in v]))
I2 = sorted(I2, key=repr)
assert len(I2) == 120, len(I2)
# group checks
def closed(G):
    S = set(G)
    return all((x * y) in S for x in G for y in G)
assert all(q.norm() == ONE for q in I2)
assert closed(T2) and closed(I2)
ONEQ = Quat(1, 0, 0, 0); MONE = Quat(-1, 0, 0, 0)
def centre(G): return [g for g in G if all(g * h == h * g for h in G)]
ZT, ZI = centre(T2), centre(I2)
assert set(ZT) == {ONEQ, MONE} and set(ZI) == {ONEQ, MONE}

# chi: 2T -> Z3, kernel Q8.  Cosets of Q8 in 2T; assign omega^k by coset, verify multiplicative.
Q8 = [Quat(*v) for v in [(1,0,0,0),(-1,0,0,0),(0,1,0,0),(0,-1,0,0),(0,0,1,0),(0,0,-1,0),(0,0,0,1),(0,0,0,-1)]]
h = Quat(-H, H, H, H)                    # order 3
assert h * h * h == ONEQ
cosets = [set(Q8), {x * h for x in Q8}, {x * h * h for x in Q8}]
assert len(cosets[0] | cosets[1] | cosets[2]) == 24
chi_k = {}
for k, cs in enumerate(cosets):
    for g in cs: chi_k[g] = k
assert all((chi_k[x] + chi_k[y]) % 3 == chi_k[x * y] for x in T2 for y in T2), "chi not multiplicative"
KER = [g for g in T2 if chi_k[g] == 0]
assert len(KER) == 8

# omega as an element of Q(sqrt5)(i): omega = -1/2 + i*sqrt3/2 -- sqrt3 not in Q(sqrt5).
# We work in the field Q(sqrt5, sqrt3, i) minimally: represent complex numbers as
# (re, im) with re, im in Q(sqrt5)[sqrt3]; implement a tiny tower.
class C:
    """number  x + y*sqrt3 + i*(z + w*sqrt3), all in Q(sqrt5)"""
    __slots__ = ('x', 'y', 'z', 'w')
    def __init__(s, x=0, y=0, z=0, w=0): s.x, s.y, s.z, s.w = _q(x), _q(y), _q(z), _q(w)
    def __add__(s, o): o = _c(o); return C(s.x+o.x, s.y+o.y, s.z+o.z, s.w+o.w)
    __radd__ = __add__
    def __neg__(s): return C(-s.x, -s.y, -s.z, -s.w)
    def __sub__(s, o): return s + (-_c(o))
    def __mul__(s, o):
        o = _c(o)
        # (p + i q)(r + i t) with p = x + y s3 etc.
        def m3(a1, b1, a2, b2): return (a1*a2 + 3*b1*b2, a1*b2 + b1*a2)   # (a1+b1 s3)(a2+b2 s3)
        pr = m3(s.x, s.y, o.x, o.y); qt = m3(s.z, s.w, o.z, o.w)
        pt = m3(s.x, s.y, o.z, o.w); qr = m3(s.z, s.w, o.x, o.y)
        return C(pr[0] - qt[0], pr[1] - qt[1], pt[0] + qr[0], pt[1] + qr[1])
    __rmul__ = __mul__
    def conj(s): return C(s.x, s.y, -s.z, -s.w)
    def __eq__(s, o): o = _c(o); return (s.x, s.y, s.z, s.w) == (o.x, o.y, o.z, o.w)
    def __hash__(s): return hash((s.x, s.y, s.z, s.w))
    def is_real(s): return s.z == ZERO and s.w == ZERO
    def re(s): return (s.x, s.y)
    def __repr__(s):
        parts = []
        if s.x != ZERO: parts.append(repr(s.x))
        if s.y != ZERO: parts.append(f"{s.y}*r3")
        if s.z != ZERO: parts.append(f"{s.z}*i")
        if s.w != ZERO: parts.append(f"{s.w}*i*r3")
        return "+".join(parts) if parts else "0"
def _c(x):
    if isinstance(x, C): return x
    return C(x)
OMEGA = [C(1), C(-H, 0, 0, H), C(-H, 0, 0, -H)]      # omega^0, omega, omega^2
assert OMEGA[1] * OMEGA[1] == OMEGA[2] and OMEGA[1] * OMEGA[2] == OMEGA[0]

def V2(q):
    a, b, c, d = q.c
    return [[C(a, 0, b, 0), C(c, 0, d, 0)], [C(-c, 0, d, 0), C(a, 0, -b, 0)]]
def mscal(s, M): return [[s * x for x in row] for row in M]
def madd(M, N): return [[x + y for x, y in zip(r1, r2)] for r1, r2 in zip(M, N)]
def mdag(M): return [[M[j][i].conj() for j in range(len(M))] for i in range(len(M[0]))]
def kron(M, N):
    n = len(N)
    return [[M[i // n][j // n] * N[i % n][j % n] for j in range(len(M) * n)] for i in range(len(M) * n)]
def mmul(M, N): return [[sum((M[i][k] * N[k][j] for k in range(len(N))), C(0)) for j in range(len(N[0]))] for i in range(len(M))]
def hermitian_part_scalar(M):
    Hm = mscal(C(H), madd(M, mdag(M)))
    n = len(M)
    for i in range(n):
        for j in range(n):
            if i != j and Hm[i][j] != C(0): return None
    d = Hm[0][0]
    if any(Hm[i][i] != d for i in range(n)): return None
    assert d.is_real()
    return d.re()                       # (Q5, Q5) = value + value'*sqrt3

# sanity: V2 is a rep
import random
random.seed(1)
for _ in range(50):
    x, y = random.choice(I2), random.choice(I2)
    assert mmul(V2(x), V2(y)) == V2(x * y)

def half_tr(q): return q.c[0]          # (1/2) tr V2(q) = real part of the unit quaternion

# ---------------------------------------------------------------- enumeration
V2I = {b: V2(b) for b in I2}; V2T = {a: V2(a) for a in T2}
odd_forced = []; even_forced = []
odd_values = set(); even_values = set(); even_all_values = set(); odd_all_values = set()
odd_pred = 0; even_pred = 0
for a in T2:
    for b in I2:
        Modd = mscal(OMEGA[chi_k[a]], V2I[b])
        s = hermitian_part_scalar(Modd)
        pred_odd = (chi_k[a] == 0) or (b in (ONEQ, MONE))
        odd_pred += pred_odd
        if s is not None:
            odd_forced.append((a, b)); odd_values.add(s)
            assert pred_odd, ("odd: forced by instrument but not by arc definition", a, b)
            # arc value: Re chi(A) * (1/2) tr V2(B)
            rechi = {0: ONE, 1: -ONE * H, 2: -ONE * H}[chi_k[a]]
            assert s == (rechi * half_tr(b), ZERO), (s, rechi * half_tr(b))
        else:
            assert not pred_odd, ("odd: forced by arc definition but not by instrument", a, b)
        Meven = kron(V2T[a], V2I[b])
        s = hermitian_part_scalar(Meven)
        pred_even = (a in (ONEQ, MONE)) or (b in (ONEQ, MONE))
        even_pred += pred_even
        even_all_values.add(half_tr(a) * half_tr(b))
        if s is not None:
            even_forced.append((a, b)); even_values.add(s)
            assert pred_even
            assert s == (half_tr(a) * half_tr(b), ZERO)
        else:
            assert not pred_even

print("2T order", len(T2), "| 2I order", len(I2), "| |ker chi| =", len(KER), "| |Z(2T)| =", len(ZT), "| |Z(2I)| =", len(ZI))
print("theta-odd  forced cells (Hermitian-part-scalar instrument):", len(odd_forced), " arc-definition count:", odd_pred,
      " inclusion-exclusion 8*120+24*2-8*2 =", 8*120 + 24*2 - 8*2)
print("theta-even forced cells (Hermitian-part-scalar instrument):", len(even_forced), " arc-definition count:", even_pred,
      " inclusion-exclusion 2*120+24*2-2*2 =", 2*120 + 24*2 - 2*2)

def fmt(v):
    # express Q5 value in terms of phi where possible
    names = {ZERO: '0'}
    for sgn, sn in ((1, ''), (-1, '-')):
        for val, nm in ((ONE, '1'), (ONE*H, '1/2'), (ONE*Fr(1,4), '1/4'), (PHI, 'phi'), (PHI*H, 'phi/2'), (PHI*Fr(1,4), 'phi/4'),
                        (PHIINV, '1/phi'), (PHIINV*H, '1/(2phi)'), (PHIINV*Fr(1,4), '1/(4phi)')):
            names[sgn * val] = sn + nm
    return names.get(v, repr(v))
odd_vals = sorted({fmt(v[0]) for v in odd_values}); even_vals = sorted({fmt(v[0]) for v in even_values})
print("theta-odd forced value set  (", len(odd_vals), "):", odd_vals)
print("theta-even FORCED value set (", len(even_vals), "):", even_vals)
all_even = sorted({fmt(v) for v in even_all_values})
print("theta-even value set over ALL 2880 cells of (1/2)trA*(1/2)trB (", len(all_even), "):", all_even)
print("C6 banked set {0,+-1/4,+-1/(4phi),+-1/2,+-1/(2phi),+-phi/4,+-phi/2,+-1} has 15 members.")

# planted control: a definition that would NOT give 992 -- e.g. require Re(M) scalar with
# the Hermitian part replaced by the real part of M (entrywise).  Also: a wrong chi (kernel
# a different subgroup) breaks multiplicativity -> exposes that the 8 is Q8 specifically.
bad = [g for g in T2 if g.c[0] == ONE or g.c[0] == -ONE or g.c[0] == ZERO]   # +-1 and the six +-i,+-j,+-k = Q8 again; try another 8-set
alt8 = set(T2[:8])
ok = all(((x in alt8) == (y in alt8)) or True for x in T2 for y in T2)
# proper control: count cells with *real trace* instead of scalar Hermitian part
odd_realtrace = sum(1 for a in T2 for b in I2 if (chi_k[a] == 0) or (half_tr(b) == ZERO))
print("control: cells where tr(M_odd) is real (a different, weaker criterion):", odd_realtrace, "(!= 992 -> the instrument distinguishes criteria)")
