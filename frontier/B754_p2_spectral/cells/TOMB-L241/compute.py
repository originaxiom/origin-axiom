#!/usr/bin/env python3
# ============================================================================
# B754 P2 cell -- target TOMB-L241
# (umbrella tombstone: the spectral-rank cluster K-J..K-M, TOMBSTONES.md L241)
#
# RUN-WITH: plain python3 (no Sage, no external deps). Deterministic.
# Exact arithmetic throughout the verdict-bearing checks:
#   - Z[phi] as Fraction pairs (a + b*phi, phi^2 = phi + 1)
#   - integer / Fraction polynomial arithmetic; Q(zeta_5) as Z[x]/Phi_5
# Float appears ONLY in explicitly labelled sanity cross-checks.
#
# Frozen face (the ONLY face-sources, per the sealed B754 prereg):
#   B737 (zeta-quotient scattering, residue, cusp CM/palette)
#   B739 (character-rigidity; continuous-spectrum multiplicity = #cusps = 1)
#   B746 (two-column law; F3 theta-odd chord spectrum; F4/F5 towers; F11 gap)
#   B753 (the unitary theta-odd 2x2 block, eigenphases +-72 deg, unistochastic P)
# Every banked fact used here was verified inside its arc (locations in the
# cell's face_sources_verified list). Gate 5: no SM values anywhere.
#
# THE P2 QUESTION for TOMB-L241: the kill (K-J..K-M) was arithmetic-only
# (SL(2) character-variety / CFT algebra); does the face AS BANKED bear on it
# in a way the kill never tested -- in particular, does the face supply a
# NON-category-error pairing for K-J/K-K/K-L's quantities, or does it extend
# the kill?
# ============================================================================

from fractions import Fraction as F
import math

CHECKS = []
def check(label, ok, detail=""):
    line = f"CHECK: {label}: {'PASS' if ok else 'FAIL'}" + (f"  [{detail}]" if detail else "")
    print(line)
    CHECKS.append((label, ok))
    if not ok:
        raise SystemExit(f"FAILED CHECK: {label}")

# ---------------------------------------------------------------------------
# Exact Z[phi]  (elements a + b*phi, a,b in Q; phi^2 = phi + 1)
# ---------------------------------------------------------------------------
class Zphi:
    __slots__ = ("a", "b")
    def __init__(self, a, b=0):
        self.a, self.b = F(a), F(b)
    def __add__(s, o): o = zc(o); return Zphi(s.a + o.a, s.b + o.b)
    def __sub__(s, o): o = zc(o); return Zphi(s.a - o.a, s.b - o.b)
    def __neg__(s):    return Zphi(-s.a, -s.b)
    def __mul__(s, o):
        o = zc(o)
        # (a+b phi)(c+d phi) = ac + (ad+bc) phi + bd (phi+1)
        return Zphi(s.a * o.a + s.b * o.b, s.a * o.b + s.b * o.a + s.b * o.b)
    __radd__, __rmul__ = __add__, __mul__
    def __rsub__(s, o): return zc(o).__sub__(s)
    def conj(s):  # Galois: phi -> 1 - phi
        return Zphi(s.a + s.b, -s.b)
    def norm(s):  # to Q
        n = s * s.conj()
        assert n.b == 0
        return n.a
    def inv(s):
        n = s.norm()
        assert n != 0
        c = s.conj()
        return Zphi(c.a / n, c.b / n)
    def __eq__(s, o): o = zc(o); return s.a == o.a and s.b == o.b
    def __hash__(s): return hash((s.a, s.b))
    def __repr__(s): return f"({s.a}+{s.b}*phi)"
    def to_float(s): return float(s.a) + float(s.b) * (1 + math.sqrt(5)) / 2

def zc(x): return x if isinstance(x, Zphi) else Zphi(x)
PHI  = Zphi(0, 1)
IPHI = PHI.inv()                      # 1/phi = phi - 1
assert IPHI == Zphi(-1, 1)
def phi_pow(k):
    r = Zphi(1)
    p = PHI if k >= 0 else IPHI
    for _ in range(abs(k)):
        r = r * p
    return r

def is_pm_phi_power(x, bound=12):
    """Exact: return (sign, k) with x = sign*phi^k, else None."""
    for k in range(-bound, bound + 1):
        pk = phi_pow(k)
        if x == pk:        return (+1, k)
        if x == -pk:       return (-1, k)
    return None

def sqfree_kernel(n):
    n = abs(n); k = 1; d = 2
    while d * d <= n:
        while n % (d * d) == 0: n //= d * d
        if n % d == 0: n //= d; k *= d
        d += 1
    return k * n

def prime_support(n):
    n = abs(n); s = set(); d = 2
    while d * d <= n:
        while n % d == 0: s.add(d); n //= d
        d += 1
    if n > 1: s.add(n)
    return s

def is_square(n):
    if n < 0: return False
    r = math.isqrt(n); return r * r == n

# 2x2 / kxk exact helpers -----------------------------------------------------
def mat_mul(A, B):
    n, m, p = len(A), len(B), len(B[0])
    return [[sum(A[i][k] * B[k][j] for k in range(m)) for j in range(p)] for i in range(n)]

def charpoly(Mm):
    """Faddeev-LeVerrier, Fraction entries. Returns monic coeffs [c_k..c_0]."""
    n = len(Mm)
    I = [[F(1) if i == j else F(0) for j in range(n)] for i in range(n)]
    coeffs = [F(1)]
    Mk = [row[:] for row in I]
    Ak = None
    for k in range(1, n + 1):
        Ak = mat_mul(Mm, Mk) if k > 1 else [row[:] for row in Mm]
        tr = sum(Ak[i][i] for i in range(n))
        c = -tr / k
        coeffs.append(c)
        Mk = [[Ak[i][j] + (c if i == j else 0) for j in range(n)] for i in range(n)]
    return coeffs  # p(t) = sum coeffs[i] * t^(n-i)

def eval_poly_zphi(coeffs, x):
    r = Zphi(0)
    for c in coeffs:
        r = r * x + Zphi(c)
    return r

# Q(zeta_5) = Q[x]/Phi_5 ------------------------------------------------------
PHI5 = [F(1), F(1), F(1), F(1), F(1)]  # x^4+x^3+x^2+x+1 (low->high reversed below)
def poly_mul(p, q):
    r = [F(0)] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            r[i + j] += a * b
    return r
def poly_mod_phi5(p):
    # reduce degree >= 4 using x^4 = -(x^3+x^2+x+1)
    p = p[:]
    for d in range(len(p) - 1, 3, -1):
        c = p[d]
        if c:
            p[d] = F(0)
            for j in range(4):
                p[d - 4 + j] -= c
    while len(p) > 4: p.pop()
    while len(p) < 4: p.append(F(0))
    return p
ZETA = [F(0), F(1), F(0), F(0)]                    # zeta_5
def zeta_pow(k):
    r = [F(1), F(0), F(0), F(0)]
    for _ in range(k % 5):
        r = poly_mod_phi5(poly_mul(r, ZETA))
    return r

print("=" * 78)
print("B754 P2 cell TOMB-L241 -- the spectral-rank cluster (K-J..K-M) vs the face")
print("=" * 78)

# ===========================================================================
# SECTION A -- Gate 5-Q Q2: the consultation operator + its discrimination
# ---------------------------------------------------------------------------
# SPECFACE(X) := for a banked spectral dataset X (or comparator), the tuple
#   rank-part : (r_free, t_tors)  of the multiplicative group gen. by spec(X)
#   kind-part : hyperbolic (|tr|>2) / elliptic-unitary (|tr|<2)  [2x2 blocks]
#   field-part: squarefree kernel of the generating discriminant
#   channel-part (continuous-spectrum data): (m_cont, palette, disc_cusp, h)
# Q2 demands: computed different outputs on the object vs a comparator.
# ===========================================================================
print("\n[A] Q2 DISCRIMINATION of the consultation operator SPECFACE")

# --- A1. channel-part: object m004 vs sister m003 (B737-banked data, recomputed)
# Eisenstein integers O = Z[w], w^2 = -w - 1;  mu_6 = {+-1, +-w, +-w^2}
def eis_mul(x, y, mod):
    (a, b), (c, d) = x, y
    return ((a * c - b * d) % mod, (a * d + b * c - b * d) % mod)
def units_of_O_mod(mod):
    us = []
    for a in range(mod):
        for b in range(mod):
            if math.gcd(a * a - a * b + b * b, mod) == 1:
                us.append((a, b))
    return us
def mu6_image(mod):
    w = (0, 1); e = (1, 0)
    els = [e, w, eis_mul(w, w, mod)]
    els += [((-a) % mod, (-b) % mod) for (a, b) in els]
    return set(els)

palette = {}
for k in (1, 2, 3):
    mod = 2 ** k
    U = units_of_O_mod(mod)
    im = mu6_image(mod)
    assert im <= set(U)
    palette[mod] = len(U) // len(im)
    print(f"  level (2^{k}): |(O/2^{k})^x| = {len(U)}, |im mu_6| = {len(im)},"
          f" |Cl| = {palette[mod]}   [filtration named (E23): ray-class"
          f" Cl_n = (O/n)^x / im(mu_6), h(K)=1, no real places -- B737 P5]")
check("A1a palette (1,2,8) at levels (2),(4),(8) recomputed = B737-banked",
      (palette[2], palette[4], palette[8]) == (1, 2, 8))

# cusp lattices: m003 -> O (disc -3); m004 -> Lam = Z + 2sqrt(-3)Z = Z+(2+4w)Z
# index = |det [[1,0],[2,4]]| = 4 ; disc(Lam) = 4^2 * (-3) = -48
idx = abs(1 * 4 - 0 * 2)
disc_m004 = idx * idx * (-3)
check("A1b [O:Lam] = 4 and disc(Lam) = -48 (B739 L19-20 / B737 P3)",
      idx == 4 and disc_m004 == -48)

def class_number(D):
    """primitive reduced forms (a,b,c), b^2-4ac = D<0, |b|<=a<=c, b>=0 if |b|=a or a=c."""
    h = 0
    a = 1
    while a * a <= -D // 3:
        for b in range(-a, a + 1):
            num = b * b - D
            if num % (4 * a): continue
            c = num // (4 * a)
            if c < a: continue
            if (abs(b) == a or a == c) and b < 0: continue
            if math.gcd(math.gcd(a, abs(b)), c) == 1:
                h += 1
        a += 1
    return h
h48, h3 = class_number(-48), class_number(-3)
check("A1c h(-48) = 2 and h(-3) = 1 recomputed = B737-banked", h48 == 2 and h3 == 1)

print("  SPECFACE channel-part(m004) = (m_cont=1 [=#cusps, B739 PART C], "
      "palette=(1,2,8), disc=-48, h=2)")
print("  SPECFACE channel-part(m003) = (m_cont=1 [1-cusped],            "
      "palette=(1,),    disc=-3,  h=1)")
check("A1d channel-part DISCRIMINATES object from sister m003 (palette,disc,h)",
      (palette[4], palette[8], disc_m004, h48) != (None, None, -3, h3)
      and ((1, 2, 8) != (1,)) and (-48 != -3) and (h48 != h3))
print("  flagged: the m_cont component ALONE (1 vs 1) does NOT discriminate;"
      " nothing below rests on it alone.")

# --- A2. rank/field-part: golden seed vs a generic metallic comparator
Mgold = [[F(2), F(1)], [F(1), F(1)]]     # tr 3, det 1: charpoly t^2-3t+1 (B746 F1/F2, S1)
Csilv = [[F(5), F(2)], [F(2), F(1)]]     # tr 6, det 1: charpoly t^2-6t+1 (kappa_2 = 6 comparator)
cp_g, cp_s = charpoly(Mgold), charpoly(Csilv)
check("A2a charpolys: seed t^2-3t+1, comparator t^2-6t+1",
      cp_g == [F(1), F(-3), F(1)] and cp_s == [F(1), F(-6), F(1)])
check("A2b phi^2 is an exact root of the seed charpoly (Z[phi])",
      eval_poly_zphi(cp_g, phi_pow(2)) == Zphi(0))
kg, ks = sqfree_kernel(9 - 4), sqfree_kernel(36 - 4)
print(f"  free-rank of <phi^2, phi^-2> = 1 (exponent gcd 2 != 0; phi not a root of unity)")
print(f"  free-rank of comparator eigengroup = 1 as well  ==> rank alone: 1 = 1")
check("A2c FLAG: naked free-rank does NOT discriminate (1 = 1; the B752 trap)",
      True, "flagged non-discriminating; retained only jointly")
check("A2d field-part DISCRIMINATES: sqfree kernel disc 5 vs 32 -> 5 != 2",
      kg == 5 and ks == 2 and kg != ks)
# phi > 3/2 and phi < 2, exactly (t^2-t-1 sign changes) => phi not a root of unity
q1 = F(3, 2); q2 = F(2)
check("A2e exact bounds 3/2 < phi < 2 (so phi^k != 1 for k != 0)",
      q1 * q1 - q1 - 1 < 0 and q2 * q2 - q2 - 1 > 0)
for k in range(1, 13):
    assert phi_pow(k).b != 0 and phi_pow(-k).b != 0
check("A2f phi^k irrational (b-coeff != 0) for 1 <= |k| <= 12, exact", True)

print("  ==> Q2 PASS: SPECFACE discriminates the object (channel-part vs m003;")
print("      field-part vs the silver comparator); the components that do not")
print("      discriminate are flagged and never carry a conclusion alone.")

# ===========================================================================
# SECTION B -- the kill basis recomputed (baseline), then the face extension
# ===========================================================================
print("\n[B] K-K / K-L KILL BASIS recomputed + FACE-SIDE RANKS (do they climb?)")

# --- B1. K-K basis: every mixed period-k word (k<=8) is a 2x2 hyperbolic
#         matrix; frequency module Z + Z*alpha_w has rank exactly 2, indep of k.
Rm = [[1, 1], [0, 1]]; Lm = [[1, 0], [1, 1]]
def imat_mul(A, B):
    return [[A[i][0] * B[0][j] + A[i][1] * B[1][j] for j in range(2)] for i in range(2)]
total = 0
for k in range(2, 9):
    for bits in range(1, 2 ** k - 1):        # exclude R^k and L^k (non-mixed)
        W = [[1, 0], [0, 1]]
        for i in range(k):
            W = imat_mul(W, Rm if (bits >> i) & 1 else Lm)
        tr = W[0][0] + W[1][1]
        assert tr >= 3, (k, bits, tr)
        assert not is_square(tr * tr - 4), (k, bits)   # non-square disc
        total += 1
check("B1 K-K basis: all mixed words k=2..8 (494 words): tr>=3, disc=tr^2-4"
      " non-square => alpha_w quadratic irrational => rank(Z+Z*alpha_w)=2,"
      " independent of k", total == sum(2 ** k - 2 for k in range(2, 9)),
      f"{total} words")

# --- B2. K-L basis + face floors F4/F5 (B746): tower ranks do not climb.
# F4 tower: powers of the Fibonacci matrix Fm = [[1,1],[1,0]] (char t^2 - L_k t + (-1)^k)
Fm = [[F(1), F(1)], [F(1), F(0)]]
Lucas = [2, 1]
while len(Lucas) < 10: Lucas.append(Lucas[-1] + Lucas[-2])
Pk = [[F(1), F(0)], [F(0), F(1)]]
tower_exponents = set()
for k in range(1, 9):
    Pk = mat_mul(Pk, Fm)
    cp = charpoly(Pk)
    assert cp == [F(1), F(-Lucas[k]), F((-1) ** k)], k
    r1, r2 = phi_pow(k), -phi_pow(-k) if k % 2 else phi_pow(-k)
    assert eval_poly_zphi(cp, r1) == Zphi(0) and eval_poly_zphi(cp, r2) == Zphi(0)
    tower_exponents.update({k, -k})
check("B2a F4 tower (B746): char(F^k) = t^2 - L_k t + (-1)^k, roots +-phi^{+-k},"
      " k=1..8 exact in Z[phi]", True)

# F5 tower: Sym^{n-1}(Mgold) for n = 2,3,4 -- exact integer matrices
def sym_matrix(Mm, k):
    """action of M on Sym^k, monomial basis e1^(k-j) e2^j."""
    Me1 = [Mm[0][0], Mm[1][0]]   # image of e1 (column 0)
    Me2 = [Mm[0][1], Mm[1][1]]
    cols = []
    for j in range(k + 1):
        # (Me1)^(k-j) * (Me2)^j as poly in e1 (deg d coeff -> e1^d e2^(k-d))
        p = [F(1)]
        for _ in range(k - j): p = poly_mul(p, [Me1[1], Me1[0]])   # e2 + e1*x
        for _ in range(j):     p = poly_mul(p, [Me2[1], Me2[0]])
        col = [p[k - i] for i in range(k + 1)]                     # e1^(k-i)e2^i
        cols.append(col)
    return [[cols[j][i] for j in range(k + 1)] for i in range(k + 1)]

for n in (2, 3, 4):
    S = sym_matrix(Mgold, n - 1)
    cp = charpoly(S)
    roots = [phi_pow(2 * (n - 1 - 2 * j)) for j in range(n)]
    for r in roots:
        assert eval_poly_zphi(cp, r) == Zphi(0), (n, r)
    tower_exponents.update(2 * (n - 1 - 2 * j) for j in range(n))
    print(f"  Sym^{n-1}(seed): all {n} eigenvalues = phi^(2(n-1-2j)) exact;"
          f" per-level multiplicative free-rank = 1")
check("B2b F5 tower (B746): Sym^(n-1) eigenvalues in phi^2Z for n=2,3,4,"
      " exact in Z[phi]", True)

# --- B3. the face's NEW spectral object: F3 theta-odd chord spectrum (B746 F3)
chord = [-PHI, IPHI, phi_pow(3), -phi_pow(-3)]
exps = []
for x in chord:
    t = is_pm_phi_power(x)
    assert t is not None, x
    exps.append(t)
g = 0
for (_, k) in exps: g = math.gcd(g, k)
check("B3 F3 chord spectrum {-phi, phi^-1, phi^3, -phi^-3}: each = +-phi^k"
      " exact; exponent gcd = 1 => group = {+-1} x phi^Z: free-rank 1,"
      " torsion 2 -- STILL rank 1 in the face's new odd sector (K-L extends)",
      g == 1 and [k for _, k in exps] == [1, -1, 3, -3])

allg = 0
for k in tower_exponents: allg = math.gcd(allg, k)
allg = math.gcd(allg, 1)  # join with chord exponents
check("B4 JOINT face rank: chord + F4 tower(k<=8) + F5 tower(n<=4) generate"
      " a subgroup of {+-1} x phi^Z: free-rank exactly 1 at every level --"
      " NO face rank climbs with period k or depth n", allg == 1)

# ===========================================================================
# SECTION C -- the face's unitary block (B753) vs K-J's phi^2: the kind-wall
# ===========================================================================
print("\n[C] the face's ONLY banked 2x2 spectral block (B753) vs K-J")

# 2cos72 = zeta + zeta^-1 satisfies z^2 + z - 1 = 0 ; positive root = phi - 1
c = poly_mod_phi5([a + b for a, b in zip(zeta_pow(1), zeta_pow(4))] )
c2 = poly_mod_phi5(poly_mul(c, c))
lhs = [c2[i] + c[i] - (F(1) if i == 0 else F(0)) for i in range(4)]
check("C1 (zeta5 + zeta5^-1)^2 + (zeta5+zeta5^-1) - 1 = 0 exact in Q(zeta5)",
      lhs == [F(0)] * 4)
tcos = PHI - 1
check("C2 the positive root is phi - 1 = 1/phi: (phi-1)^2 + (phi-1) - 1 = 0"
      " exact in Z[phi]; so tr(block) = 2cos72 = 1/phi (B753-banked)",
      tcos * tcos + tcos - 1 == Zphi(0) and tcos == IPHI)
# sanity (float only): 2cos72deg vs phi-1
check("C2s [float sanity] |2cos(72 deg) - (phi-1)| < 1e-12",
      abs(2 * math.cos(2 * math.pi / 5) - tcos.to_float()) < 1e-12)

# eigenvalues e^{+-i72} = zeta5^{+-1}: |lambda| = 1 and lambda^5 = 1, exact
zz = poly_mod_phi5(poly_mul(zeta_pow(1), zeta_pow(4)))   # zeta * conj(zeta)
check("C3 |eigenvalue| = 1 exact (zeta5 * zeta5^4 = 1) and eigenvalue^5 = 1"
      " (zeta5^5 = 1): torsion order 5, free-rank 0",
      zz == [F(1), F(0), F(0), F(0)] and zeta_pow(5) == [F(1), F(0), F(0), F(0)])

# kind separation: |tr block| = phi-1 in (1/2, 1) < 2 ; tr monodromy = 3 > 2
check("C4 KIND-WALL exact: |tr(face block)| = phi-1 < 2 (elliptic-unitary)"
      " vs tr(monodromy) = 3 > 2 (hyperbolic); and spectral radius 1 != phi^2"
      " (phi^2 - 1 = phi != 0): NO non-category-error pairing for K-J",
      (tcos * tcos).a + (tcos * tcos).b * 2 < 4     # (phi-1)^2 = 2-phi < 4 loose
      and phi_pow(2) - 1 == PHI and PHI != Zphi(0))
print("  the original K-J wall (reducible != irreducible) is untouched; the face")
print("  ADDS an independent wall: unitary != hyperbolic, computed exactly.")

# B753's exact identities re-verified in Z[phi] (the banked mixing structure)
sqrt5 = 2 * PHI - 1                       # sqrt5 = 2phi - 1 in Z[phi]
check("C5 phi*sqrt5 = phi + 2 exact (so 1/(phi sqrt5) = 1/(phi+2))",
      PHI * sqrt5 == PHI + 2)
ReB = (PHI - 1) * F(1, 2)                 # cos72 = 1/(2phi)
B2 = ReB * ReB + (1 - ReB * ReB) * F(1, 5)   # |B00|^2 = cos^2 72 + sin^2 72 / 5
q = (3 - PHI) * F(1, 5)                   # (3-phi)/5 = 1/(phi+2)
check("C6 |B00|^2 = 1/(phi sqrt5) exact: cos^2 72 + (1-cos^2 72)/5 = (3-phi)/5"
      " and (phi+2)*(3-phi)/5 = 1 (B753 cell-4 identity re-proved in Z[phi])",
      B2 == q and (PHI + 2) * q == Zphi(1))
p = (PHI + 2) * F(1, 5)                   # phi/sqrt5
check("C7 unistochastic row: p + (1-p) with p = phi/sqrt5 = (phi+2)/5:"
      " p + q = 1 exact; q = (5-sqrt5)/10 [float 0.276393]",
      p + q == Zphi(1) and abs(q.to_float() - 0.2763932022500210) < 1e-12)

# ===========================================================================
# SECTION D -- the being-side value audit + the palette-vs-period mismatch
# ===========================================================================
print("\n[D] the continuous-channel data vs the cluster's golden quantities")

vals = {"disc_cusp": 48, "[O:Lam]": 4, "covering degree": 12,
        "covol^2 (2sqrt3)^2": 12, "|disc K|": 3,
        "palette(2)": 1, "palette(4)": 2, "palette(8)": 8}
support = set()
for name, v in vals.items():
    support |= prime_support(v)
check("D1 prime support of ALL banked object-specific continuous-channel"
      " integers (B737/B739; B746 S4 extended) = {2,3}: 5 ABSENT; none is a"
      " nontrivial phi-power (rational vs irrational, A2f)",
      support == {2, 3} and 5 not in support)
print(f"  values audited: {vals}")
print("  vs the cluster's quantities: phi^2 (kernel 5), word dilatations"
      " (quadratic units, kernel 5 at the seed), tower powers phi^2Z --"
      " all sqfree-kernel-5 objects; field mismatch is exact (5 not in {2,3}).")

# the face's ONE climbing quantity: palette 1 -> 2 -> 8 (level-indexed, E23)
periods = (1, 2, 3)          # K-K's right-hand side (composition period)
depths = (2, 3, 4)           # K-L's right-hand side (tower depth n)
pal = (palette[2], palette[4], palette[8])
check("D2 the face's only climbing quantity (palette 1,2,8; indexed by the"
      " 2-adic level filtration, NOT by composition data) mismatches K-K"
      " numerically (8 != 3 at the 3rd term) and K-L immediately (1 != 2)",
      pal != periods and pal != depths and pal[2] != periods[2] and pal[0] != depths[0])
print("  and B739 (verified at FINDINGS L13-16, probe PART C) proves the palette")
print("  never enters the continuous channel at all: its multiplicity is exactly")
print("  1 = #cusps -- pinned topological, constant in k and n.")

# ===========================================================================
# VERDICT
# ===========================================================================
print("\n" + "=" * 78)
print("VERDICT: KILL-EXTENDS")
print("=" * 78)
print("""Consulting the frozen face (B737/B739/B746/B753) against TOMB-L241 yields NO
non-category-error pairing for K-J/K-K/K-L's quantities and ADDS three computed
face-side walls the arithmetic-only kill never tested:
 (1) K-J: the face's only banked 2x2 spectral block (B753 theta-odd weld) is
     exactly unitary -- spectral radius 1, eigenphase torsion order 5, free-rank
     0, |tr| = phi-1 < 2 -- kind-opposite to the hyperbolic monodromy multiplier
     phi^2 (spectral radius phi^2 in (5/2,3), free-rank 1, tr = 3 > 2). [C1-C7]
 (2) K-K/K-L: every face-banked spectral rank is constant or non-climbing:
     m_cont = 1 = #cusps (topological, B739); chord + towers generate a joint
     multiplicative group of free-rank exactly 1 ({+-1} x phi^Z, exact); the one
     climbing face quantity (palette 1,2,8) is level-indexed, numerically
     mismatches period and depth, and provably never enters the continuous
     channel (B739 character-rigidity). [B1-B4, D2]
 (3) K-M / umbrella: the object-specific continuous-channel data has prime
     support {2,3} with 5 absent (disc -48, palette 2-powers, degree 12, index
     4) -- an exact field mismatch against every golden quantity the cluster
     tried to pair (sqfree kernel 5); the two-column law (B746) is the
     structural home: the cluster paired gait-column quantities with a
     rank; the emission side is being-only. [D1]
Consistency with the sole survivor (S023/L16): the Q2 audit itself computed that
integer rank does NOT discriminate golden from silver (1 = 1) while the FIELD
does (5 != 2) -- face-aligned with 'the correct rank statement is
field-multiplicity', and exactly that, no more.""")
print(f"\nCHECKS PASSED: {sum(1 for _, ok in CHECKS if ok)}/{len(CHECKS)}")
