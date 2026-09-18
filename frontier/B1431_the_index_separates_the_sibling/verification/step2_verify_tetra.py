"""
Step 2.  Verify my tetrahedron index against the literature.

TWO CONVENTIONS ARE IN PLAY -- this is the crux of getting it right.

  PROMPT convention (as written in my task):
      I^P(m,e) = sum_n (-1)^n q^{ n(n+1)/2 - (n + m/2) e } / ( (q)_n (q)_{n+m} )
                                            ^^^^^^^^^^^^        ^^^^^^^^^
  GAROUFALIDIS convention (arXiv:1208.1663 eq. (1.2)):
      I^G(m,e) = sum_{n=(-e)_+} (-1)^n q^{ n(n+1)/2 - (n + e/2) m } / ( (q)_n (q)_{n+e} )
                                                      ^^^^^^^^^^^^        ^^^^^^^^^

  They are THE SAME FUNCTION WITH THE ARGUMENTS TRANSPOSED:   I^P(m,e) = I^G(e,m).

tet_index.I_delta implements the PROMPT convention.  IG() below is the
Garoufalidis one, which is what the published gluing formulas use.
"""
from tet_index import (I_delta, s_str, s_eq, s_trunc, s_mul, s_shift, s_scal,
                       s_add, sgn)

X = 40          # x-exponents, i.e. up to q^20


def IP(m, e, Xmax=X):
    """prompt convention"""
    return I_delta(m, e, Xmax)


def IG(m, e, Xmax=X):
    """Garoufalidis arXiv:1208.1663 eq (1.2) convention"""
    return I_delta(e, m, Xmax)


def delta_x(m, e):
    """Lemma 3.6 of arXiv:1208.1663, DOUBLED (i.e. in units of x = q^{1/2}).
       delta(m,e) = 1/2 ( m_+ (m+e)_+ + (-m)_+ e_+ + (-e)_+ (-e-m)_+ + max{0,m,-e} )"""
    p = lambda t: max(0, t)
    return p(m) * p(m + e) + p(-m) * p(e) + p(-e) * p(-e - m) + max(0, m, -e)


print("=" * 78)
print("STEP 2: controls on the tetrahedron index")
print("=" * 78)

# ---------------------------------------------------------------- vs published values
print("\n[C1] Against printed values in the AMSI/VRS report of E. McQuire (Monash),")
print("     'Knots & Combinatorics', Example 3.2 (Garoufalidis convention):")
pub = {
    (0, 0):  "1 - q - 2q^2 - 2q^3 - 2q^4 + q^6 + 5q^7 + 7q^8 + 11q^9 + 13q^10 + 16q^11",
    (1, -1): "q^{1/2}(-1 + q^2 + 2q^3 + 3q^4 + 3q^5 + 3q^6 + q^7 - q^8 - 5q^9 - 9q^10 - 15q^11)",
    (2, 2):  "q^5 + q^6 + 2q^7 + 2q^8 + 3q^9 + 2q^10 + 2q^11 - 2q^13 - 6q^14 - 10q^15 - 16q^16",
}
# published coefficient lists, as x-exponent -> coeff
pub_series = {
    (0, 0):  {0:1, 2:-1, 4:-2, 6:-2, 8:-2, 10:0, 12:1, 14:5, 16:7, 18:11, 20:13, 22:16},
    (1, -1): {1:-1, 5:1, 7:2, 9:3, 11:3, 13:3, 15:1, 17:-1, 19:-5, 21:-9, 23:-15},
    (2, 2):  {10:1, 12:1, 14:2, 16:2, 18:3, 20:2, 22:2, 24:0, 26:-2, 28:-6, 30:-10, 32:-16},
}
allok = True
for (m, e), txt in pub.items():
    mine = IG(m, e)
    hi = max(pub_series[(m, e)])
    mine_t = {k: v for k, v in s_trunc(mine, hi).items() if v}
    pub_t = {k: v for k, v in pub_series[(m, e)].items() if v}
    ok = mine_t == pub_t
    allok &= ok
    print(f"   I^G({m},{e}): {'MATCH' if ok else 'MISMATCH'}   (compared through x^{hi} = q^{hi/2})")
    print(f"      mine     : {s_str(mine, hi)}")
    if not ok:
        print(f"      published: {txt}")
        print(f"      diff     : { {k: mine_t.get(k,0)-pub_t.get(k,0) for k in set(mine_t)|set(pub_t) if mine_t.get(k,0)!=pub_t.get(k,0)} }")
print(f"   => published tetrahedron-index values reproduced: {allok}")

# ---------------------------------------------------------------- threefold symmetry (3.2)
print("\n[C2] Garoufalidis eq. (3.2) threefold symmetry:")
print("     I(m,e) = (-q^{1/2})^{-e} I(e,-e-m) = (-q^{1/2})^{m} I(-e-m,m)")
bad1 = bad2 = 0
tested = 0
CMP = X - 20          # compare well inside the reliable range
for m in range(-6, 7):
    for e in range(-6, 7):
        tested += 1
        lhs = IG(m, e)
        # (-q^{1/2})^{-e} = (-1)^e x^{-e}
        r1 = s_scal(s_shift(IG(e, -e - m), -e, X), sgn(e))
        # (-q^{1/2})^{m} = (-1)^m x^{m}
        r2 = s_scal(s_shift(IG(-e - m, m), m, X), sgn(m))
        if not s_eq(lhs, r1, CMP):
            bad1 += 1
        if not s_eq(lhs, r2, CMP):
            bad2 += 1
print(f"   pairs tested {tested};  failures of 1st identity: {bad1};  of 2nd: {bad2}")

# ---------------------------------------------------------------- prompt-convention symmetry
print("\n[C3] In the PROMPT convention the same identity reads")
print("     I^P(m,e) = (-q^{1/2})^{-m} I^P(-m-e, m) = (-q^{1/2})^{e} I^P(e, -m-e)")
b1 = b2 = 0
for m in range(-6, 7):
    for e in range(-6, 7):
        lhs = IP(m, e)
        r1 = s_scal(s_shift(IP(-m - e, m), -m, X), sgn(m))
        r2 = s_scal(s_shift(IP(e, -m - e), e, X), sgn(e))
        if not s_eq(lhs, r1, CMP): b1 += 1
        if not s_eq(lhs, r2, CMP): b2 += 1
print(f"   failures: {b1} and {b2}")
print("   plus the plain (no-prefactor) symmetry I(m,e)=I(-e,-m) verified in step 1.")

# ---------------------------------------------------------------- degree lemma 3.6
print("\n[C4] Lemma 3.6 (minimal degree) against the computed series:")
bad = []
n = 0
for m in range(-7, 8):
    for e in range(-7, 8):
        s = IG(m, e)
        if not s:
            continue
        n += 1
        if min(s) != delta_x(m, e):
            bad.append((m, e, min(s), delta_x(m, e)))
print(f"   pairs checked {n}; disagreements with Lemma 3.6: {len(bad)}")
if bad:
    print("   ", bad[:12])

# ---------------------------------------------------------------- special pentagon
print("\n[C5] Special pentagon (Remark 3.8):  I(0,0)^2 = sum_{e in Z} I(0,e)^3 q^e")
lhs = s_mul(IG(0, 0), IG(0, 0), X)
rhs = {}
for e in range(-30, 31):
    t = IG(0, e)
    if not t:
        continue
    cube = s_mul(s_mul(t, t, X), t, X)
    rhs = s_add(rhs, s_shift(cube, 2 * e, X))
CMP5 = 24
print("   LHS =", s_str(lhs, CMP5))
print("   RHS =", s_str(rhs, CMP5))
print("   EQUAL through q^%d : %s" % (CMP5 // 2, s_eq(lhs, rhs, CMP5)))

# ---------------------------------------------------------------- full pentagon, a few instances
print("\n[C6] Full pentagon (3.5) at a few (m1,m2,e1,e2):")
import itertools
for (m1, m2, e1, e2) in [(0,0,0,0), (1,0,0,1), (1,-1,2,0), (2,1,-1,1), (-1,2,1,-2)]:
    L = s_mul(IG(m1 - e2, e1), IG(m2 - e1, e2), X)
    R = {}
    for e3 in range(-30, 31):
        t = s_mul(s_mul(IG(m1, e1 + e3), IG(m2, e2 + e3), X), IG(m1 + m2, e3), X)
        if t:
            R = s_add(R, s_shift(t, 2 * e3, X))
    print(f"   (m1,m2,e1,e2)=({m1},{m2},{e1},{e2}): equal through q^10 -> {s_eq(L, R, 20)}")

# ---------------------------------------------------------------- recursions 3.1a/b
print("\n[C7] Defining recursions (3.1a),(3.1b):")
print("     q^{e/2} f(m+1,e) + q^{-m/2} f(m,e+1) - f(m,e) = 0   and the (m-1,e-1) version")
ba = bb = 0
for m in range(-6, 7):
    for e in range(-6, 7):
        a = s_add(s_add(s_shift(IG(m + 1, e), e, X), s_shift(IG(m, e + 1), -m, X)),
                  s_scal(IG(m, e), -1))
        b = s_add(s_add(s_shift(IG(m - 1, e), e, X), s_shift(IG(m, e - 1), -m, X)),
                  s_scal(IG(m, e), -1))
        if {k: v for k, v in a.items() if k <= CMP and v}: ba += 1
        if {k: v for k, v in b.items() if k <= CMP and v}: bb += 1
print(f"   failures: (3.1a) {ba}, (3.1b) {bb}")
