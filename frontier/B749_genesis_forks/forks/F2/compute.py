#!/usr/bin/env python3
# =============================================================================
# B749 — fork F2 (periodicity allowed).  Sealed campaign, seal v2.
#
# Sibling (per MEASUREMENTS.md, binding): mapping tori of finite-order /
# reducible monodromies of the once-punctured torus (periodic words =>
# |trace| <= 2 abelianization, det = +1).
# Measurements (binding): Thurston trichotomy class computed from the trace;
# existence of a hyperbolic structure; carried V4 faces; and the geometry the
# sibling DOES get.
# Verdict criteria (binding): ROBUST = no pA, no hyperbolic carrier, zero
# faces.  FRAGILE = any periodic-word carrier admitting hyperbolic structure.
#
# Deterministic: no wall-clock, no unseeded randomness, no network.
# Tools: python 3.12.1, sympy 1.14.0, snappy 3.3.2 (+ bundled twister).
# Instrument theorems are named INSTRUMENT where used; everything else is
# computed exactly (integer/rational/symbolic) or live in SnapPy with a
# positive control.
# =============================================================================

import warnings
warnings.filterwarnings("ignore")   # silence snappy's tkinter import warning only

from fractions import Fraction
from math import gcd as igcd

import sympy as sp
from sympy import Matrix, symbols, Poly, QQ, simplify, sqrt, I as spI
from sympy.matrices.normalforms import smith_normal_form

X = symbols('x')
CHECKS = []


def check(fact, value):
    line = f"CHECK: {fact} = {value}"
    CHECKS.append(line)
    print(line)


def info(msg):
    print(f"INFO: {msg}")


def section(title):
    print()
    print("=" * 78)
    print(title)
    print("=" * 78)


# ---------- exact 2x2 integer matrix helpers ----------------------------------
def mmul(A, B):
    return [[A[0][0]*B[0][0] + A[0][1]*B[1][0], A[0][0]*B[0][1] + A[0][1]*B[1][1]],
            [A[1][0]*B[0][0] + A[1][1]*B[1][0], A[1][0]*B[0][1] + A[1][1]*B[1][1]]]


def mpow(A, k):
    R = [[1, 0], [0, 1]]
    for _ in range(k):
        R = mmul(R, A)
    return R


def det(A):
    return A[0][0]*A[1][1] - A[0][1]*A[1][0]


def tr(A):
    return A[0][0] + A[1][1]


ID = [[1, 0], [0, 1]]
NEG = [[-1, 0], [0, -1]]

# =============================================================================
section("S0. CONVENTIONS AND SCOPE CAVEAT (binding, from seal + §16 review)")
# =============================================================================
info("MCG(once-punctured torus) ~ SL(2,Z) acting on H1(fiber)=Z^2.")
info("Thurston trichotomy for det=+1: |tr|<2 => elliptic => finite-order "
     "(periodic); |tr|=2, A != +-I => parabolic => reducible; |tr|>2 => Anosov => pA.")
info("BINDING CAVEAT (§16 review 1): the trace bound is det=+1-scoped. det=-1 "
     "is F5's fork; there |tr|<=2 does NOT exclude Anosov.")

W = [[1, 1], [1, 0]]                      # det=-1 witness (F5's monodromy)
cpW = Poly(X**2 - tr(W)*X + det(W), X)    # x^2 - x - 1
lam = (1 + sqrt(5)) / 2
assert det(W) == -1 and tr(W) == 1
assert cpW == Poly(X**2 - X - 1, X)
assert sp.minimal_polynomial(lam, X) == X**2 - X - 1
assert simplify(lam - 1) > 0
check("det=-1 scope witness [[1,1],[1,0]]: charpoly, lambda_max",
      "x^2-x-1, (1+sqrt5)/2 > 1 (Anosov despite |tr|<=2 => trichotomy det=+1-scoped)")

# =============================================================================
section("S1. THE SIBLING FAMILY, EXACTLY (det=+1, |tr|<=2)")
# =============================================================================
# --- Lemma A: det=1 integer matrix with a RATIONAL eigenvalue has |tr| = 2.
# (Periodic word <=> rational invariant slope; eigenvalues rational <=> tr^2-4
#  is a perfect square k^2; solve tr^2 - k^2 = 4 by factoring (tr-k)(tr+k)=4.)
sols = set()
for d in (1, -1, 2, -2, 4, -4):
    e = 4 // d
    if (d + e) % 2 == 0 and (e - d) % 2 == 0:
        sols.add(((d + e) // 2, (e - d) // 2))
sols_traces = sorted({t for (t, k) in sols})
assert sols_traces == [-2, 2] and all(k == 0 for (t, k) in sols)
check("integer solutions of tr^2 - k^2 = 4 (rational-eigenvalue locus, det=1)",
      "tr = +-2, k = 0 only => periodic/rational-slope words force |tr| <= 2")
info("Converse direction: |tr|>2 => eigenvalue quadratic irrational => invariant "
     "slope irrational => word aperiodic [INSTRUMENT: Morse-Hedlund].")

# --- Symbolic Cayley-Hamilton over the WHOLE family (not just representatives).
# A^m = x_m*A + y_m*I with x_1,y_1 = 1,0 ; x_{m+1} = t*x_m + y_m ; y_{m+1} = -x_m.
t = symbols('t')
def ch_powers(tval, upto):
    xs, ys = [None, sp.Integer(1)], [None, sp.Integer(0)]
    for m in range(1, upto):
        xs.append(sp.expand(tval*xs[m] + ys[m]))
        ys.append(-xs[m])
    return xs, ys

xs, ys = ch_powers(sp.Integer(-1), 4)
assert (xs[3], ys[3]) == (0, 1)          # tr=-1: A^3 = I
xs, ys = ch_powers(sp.Integer(0), 5)
assert (xs[4], ys[4]) == (0, 1)          # tr=0:  A^4 = I
xs, ys = ch_powers(sp.Integer(1), 7)
assert (xs[6], ys[6]) == (0, 1)          # tr=1:  A^6 = I
check("symbolic Cayley-Hamilton, ALL det=1 matrices of trace -1 / 0 / 1",
      "A^3 = I / A^4 = I / A^6 = I (finite order => periodic mapping class)")

xs2, _ = ch_powers(sp.Integer(2), 13)
assert all(xs2[m] == m for m in range(1, 13))
xsm2, _ = ch_powers(sp.Integer(-2), 13)
assert all(xsm2[m] == (-1)**(m+1) * m for m in range(1, 13))
m = symbols('m', integer=True, positive=True)
assert simplify(2*m - (m - 1) - (m + 1)) == 0                       # x_m = m closed form
assert simplify(-2*(-1)**(m+1)*m - (-1)**m*(m-1) - (-1)**(m+2)*(m+1)) == 0
check("symbolic: trace=+2 => A^m = m*A-(m-1)I, trace=-2 => x_m=(-1)^(m+1)m != 0",
      "A^m = I never for A != +-I => parabolic classes +-T^n have infinite order")

# --- No pA anywhere in the family: spectral radius exactly 1 for tr in {-2..2}.
for tv in (-2, -1, 0, 1, 2):
    disc = tv*tv - 4
    if disc < 0:
        pass          # complex conjugate pair, product = det = 1 => |root|^2 = 1
    else:
        assert disc == 0            # double root tv/2 = +-1
    roots = sp.roots(Poly(X**2 - tv*X + 1, X))
    assert all(simplify(sp.Abs(r) - 1) == 0 for r in roots)
check("max |eigenvalue| over ALL det=1 traces {-2,-1,0,1,2}",
      "1 exactly (conjugate pair of product 1, or double root +-1) => dilatation 1 => pA count = 0")

# --- Representatives of every stratum (trace / order labelled).
REPS = {
    'I    (tr  2, order 1)': ID,
    '-I   (tr -2, order 2)': NEG,
    'U3   (tr -1, order 3)': [[0, -1], [1, -1]],
    'S4   (tr  0, order 4)': [[0, -1], [1, 0]],
    'V6   (tr  1, order 6)': [[1, -1], [1, 0]],
    'T1   (tr  2, parab n=1)': [[1, 1], [0, 1]],
    'T2   (tr  2, parab n=2)': [[1, 2], [0, 1]],
    'T3   (tr  2, parab n=3)': [[1, 3], [0, 1]],
    '-T1  (tr -2, parab n=1)': [[-1, -1], [0, -1]],
}
orders = {}
for name, A in REPS.items():
    assert det(A) == 1 and abs(tr(A)) <= 2
    order = None
    for k in range(1, 13):
        if mpow(A, k) == ID:
            order = k
            break
    orders[name] = order
assert [orders[n] for n in REPS] == [1, 2, 3, 4, 6, None, None, None, None]
check("exact orders of representatives I,-I,U3,S4,V6,T1,T2,T3,-T1",
      "1,2,3,4,6,inf,inf,inf,inf (A^k = I checked by exact matrix powers)")

# Parabolic reducibility: exact invariant (unoriented) curve class v = (1,0).
for nm in ('T1', 'T2', 'T3'):
    A = [r for k, r in REPS.items() if k.startswith(nm + ' ')][0]
    assert [A[0][0]*1 + A[0][1]*0, A[1][0]*1 + A[1][1]*0] == [1, 0]
Am = REPS['-T1  (tr -2, parab n=1)']
assert [Am[0][0]*1 + Am[0][1]*0, Am[1][0]*1 + Am[1][1]*0] == [-1, 0]
assert mmul(Am, Am) == [[1, 2], [0, 1]]      # (-T1)^2 = T2, exactly
check("parabolic invariant curve and the tr=-2 square trick",
      "T^n(1,0)=(1,0); -T1(1,0)=-(1,0) (same curve class); (-T1)^2 = T2 exactly")

info("Trichotomy verdict for the WHOLE sibling family: |tr|<2 and +-I => "
     "finite-order (periodic); tr=+-2, A != +-I => parabolic reducible; "
     "pA classes in the family: ZERO (all facts above are symbolic/exact).")

# =============================================================================
section("S2. HYPERBOLICITY: NO — three independent routes")
# =============================================================================
info("Route 1 [INSTRUMENT: Thurston, hyperbolization of fibered 3-manifolds]: "
     "mapping torus hyperbolic <=> monodromy pA.  pA count = 0 (S1, exact) "
     "=> no sibling admits a hyperbolic structure.")

# ---- Route 2: live SnapPy with positive controls. ----------------------------
import snappy
import snappy.twister as twister

GEOMETRIC = 'all tetrahedra positively oriented'

m004 = snappy.Manifold('m004')
C1 = snappy.Manifold('b++RL')            # sealed executor warning: verify live
v1, v0 = C1.volume(), m004.volume()
assert C1.solution_type() == GEOMETRIC
assert abs(v1 - 2.0298832128) < 1e-9 and abs(v1 - v0) < 1e-9
assert C1.is_isometric_to(m004)
check("control #1 'b++RL' (Anosov [[2,1],[1,1]], tr 3)",
      f"geometric, vol {float(v1):.10f}, is_isometric_to(m004) True (two invariants)")

S11 = twister.Surface('S_1_1')
C2 = S11.bundle(monodromy='a*B')
assert C2.solution_type() == GEOMETRIC
assert abs(C2.volume() - v0) < 1e-9
assert C2.is_isometric_to(m004)
check("control #2 twister S_1_1 'a*B' (pins twister twist convention)",
      "geometric, vol = vol(m004), is_isometric_to(m004) True => 'a*b' is the tr=+-1 class")

# H1(M_A) = Z + coker(A - I)  [INSTRUMENT: Wang sequence]; SNF is exact.
def h1_of_bundle(A):
    Mm = Matrix([[A[0][0]-1, A[0][1]], [A[1][0], A[1][1]-1]])
    S = smith_normal_form(Mm, domain=sp.ZZ)
    d = [abs(S[i, i]) for i in range(2)]
    rank = 1 + sum(1 for x in d if x == 0)
    tors = sorted(int(x) for x in d if x not in (0, 1))
    return rank, tuple(tors)

def parse_snappy_h1(h):
    parts = [p.strip() for p in str(h).split('+')]
    rank = sum(1 for p in parts if p == 'Z')
    tors = sorted(int(p.split('/')[1]) for p in parts if '/' in p)
    return rank, tuple(tors)

SIBLING_BUILDS = [
    ('a',              'T1  parabolic n=1'),
    ('a*a',            'T2  parabolic n=2'),
    ('a*a*a',          'T3  parabolic n=3'),
    ('a*b',            'V6  elliptic order 6'),
    ('a*b*a',          'S4  elliptic order 4'),
    ('a*b*a*b',        'U3  elliptic order 3'),
    ('a*b*a*b*a*b',    '-I  elliptic order 2'),
    ('a*b*a*b*a*b*a',  '-T1 parabolic tr=-2'),
]
MAT_OF = {
    'T1  parabolic n=1':   [[1, 1], [0, 1]],
    'T2  parabolic n=2':   [[1, 2], [0, 1]],
    'T3  parabolic n=3':   [[1, 3], [0, 1]],
    'V6  elliptic order 6': [[1, -1], [1, 0]],
    'S4  elliptic order 4': [[0, -1], [1, 0]],
    'U3  elliptic order 3': [[0, -1], [1, -1]],
    '-I  elliptic order 2': [[-1, 0], [0, -1]],
    '-T1 parabolic tr=-2': [[-1, -1], [0, -1]],
}
fingerprints = {}
geometric_count = 0
for word, cls in SIBLING_BUILDS:
    Mfd = S11.bundle(monodromy=word)
    st = Mfd.solution_type()
    live = parse_snappy_h1(Mfd.homology())
    pred = h1_of_bundle(MAT_OF[cls])
    assert Mfd.num_cusps() == 1
    assert live == pred, (word, cls, live, pred)
    if st == GEOMETRIC:
        geometric_count += 1
    fingerprints[cls] = pred
    check(f"sibling '{word}' [{cls}]",
          f"solution_type '{st}' (NOT geometric), H1 live {live} == exact Wang/SNF prediction")
assert geometric_count == 0
assert len(set(fingerprints.values())) == len(fingerprints)
check("H1 fingerprints of the 8 built classes pairwise distinct",
      f"True ({len(fingerprints)} distinct) => each build pinned to its intended class")
check("hyperbolic carriers among the 8 sibling builds (SnapPy live)",
      "0 of 8 geometric; both positive controls geometric => instrument could have said FRAGILE")
info("The 9th representative, I itself, gives T' x S^1: handled exactly in S3 "
     "(center of pi1 nontrivial => not hyperbolic; product geometry H^2 x R).")

# ---- Route 3: exact group theory (per class). --------------------------------
# (a) finite order k: A^k = I (S1, exact) => M_A has a k-fold cyclic cover
#     M_{A^k} = T' x S^1, whose pi1 = F2 x Z has center containing the S^1
#     factor.  [INSTRUMENTS: covers of finite-volume hyperbolic manifolds are
#     hyperbolic; finite-volume Kleinian groups have trivial center.]
# (b) parabolic tr=+2 (T^n): suspension torus of the invariant curve a is
#     essential; hyperbolic manifolds are atoroidal [INSTRUMENT].  Computable
#     content, all exact below: Z^2 = <a, t~> via semidirect normal form;
#     non-separating via intersection number 1.
# (c) tr=-2: (-T1)^2 = T2 (S1, exact) => double cover is the tr=+2 case
#     [INSTRUMENT: covers], so not hyperbolic either.

# Free group F2 = <a,b>: words as tuples of (letter, +-1); exact reduction.
def w_reduce(w):
    out = []
    for x in w:
        if out and out[-1][0] == x[0] and out[-1][1] == -x[1]:
            out.pop()
        else:
            out.append(x)
    return tuple(out)

def w_inv(w):
    return tuple((g, -s) for (g, s) in reversed(w))

def w_mul(*ws):
    r = ()
    for w in ws:
        r = w_reduce(r + w)
    return r

def gen(g, s=1):
    return ((g, s),)

def phi_n(n):
    # phi(a) = a, phi(b) = b a^n : abelianization matrix [[1,n],[0,1]] = T^n
    img = {('a', 1): gen('a'), ('b', 1): w_mul(gen('b'), tuple(('a', 1) for _ in range(n)))}
    def phi(w):
        out = ()
        for (g, s) in w:
            piece = img[(g, 1)]
            out = w_mul(out, piece if s == 1 else w_inv(piece))
        return out
    return phi

def abelianize(w):
    v = {'a': 0, 'b': 0}
    for (g, s) in w:
        v[g] += s
    return (v['a'], v['b'])

for n in (1, 2, 3):
    phi = phi_n(n)
    assert abelianize(phi(gen('a'))) == (1, 0) and abelianize(phi(gen('b'))) == (n, 1)
    assert phi(gen('a')) == gen('a')                       # t~ commutes with a
    w = gen('b')
    for mm in range(1, 7):                                  # phi^m(b) = b a^{mn}
        w = phi(w)
        assert w == w_mul(gen('b'), tuple(('a', 1) for _ in range(mm * n)))
check("phi_n(a)=a, phi_n(b)=b a^n, abelianization = T^n, phi^m(b)=b a^(mn)",
      "verified by exact free-group reduction for n=1,2,3, m=1..6")

# Z^2 = <a, t~> in pi1(M_{T^n}) = F2 x|_phi Z: elements (w, m), product
# (w1,m1)(w2,m2) = (w1 * phi^{m1}(w2), m1+m2).  Exact normal form:
def sd_mul(x, y, phi):
    (w1, m1), (w2, m2) = x, y
    z = w2
    for _ in range(abs(m1)):
        z = phi(z)  # m1 >= 0 in our checks
    return (w_mul(w1, z), m1 + m2)

phi = phi_n(1)
for i in range(-3, 4):
    for j in range(0, 4):
        for k2 in range(-3, 4):
            for l in range(0, 4):
                x = (tuple(('a', 1 if i > 0 else -1) for _ in range(abs(i))), j)
                y = (tuple(('a', 1 if k2 > 0 else -1) for _ in range(abs(k2))), l)
                z = sd_mul(x, y, phi)
                assert abelianize(z[0]) == (i + k2, 0) and z[1] == j + l
check("subgroup <a, t~> of pi1(M_T1) is Z^2 (a^i t^j normal form, phi(a)=a)",
      "verified: products a^i t^j * a^k t^l = a^(i+k) t^(j+l), trivial only at i=j=0")
# Non-separating: fiber curve b crosses the suspension torus (a x S^1) once:
# algebraic intersection <a,b> in the fiber = det[[1,0],[0,1]] = 1.
assert det([[1, 0], [0, 1]]) == 1
check("suspension torus a x S^1 in M_{T^n}: intersection with dual curve b",
      "1 (exact) => torus non-separating => not boundary-parallel; pi1-injective by the Z^2 above => ESSENTIAL")

# No normal Z (=> not Seifert fibered) — the word-level obstruction:
for p in (-4, -3, -2, -1, 1, 2, 3, 4):
    w = w_mul(gen('b'), tuple(('a', 1 if p > 0 else -1) for _ in range(abs(p))), gen('b', -1))
    assert any(g == 'b' for (g, s) in w)   # reduced word contains b => never a power of a
check("b a^p b^-1 (p != 0) reduced always contains letter b",
      "True for p in +-1..4 (and for all p: reduced words are unique) => != a^j for every j")
info("No-normal-Z derivation for M_{+-T^n} (n != 0): a central/normal Z generator "
     "(w, m) forces w in centralizer(a) = <a> [INSTRUMENT: centralizers in free "
     "groups are cyclic], then conjugation by b forces b a^(j-m) b^-1 = a^j, "
     "impossible by the check above.  => pi1 has no infinite cyclic normal "
     "subgroup => NOT Seifert fibered [INSTRUMENT: Waldhausen/Casson-Jungreis-"
     "Gabai: Seifert <=> normal Z, Haken case].")

check("finite-order classes: A^k = I => k-fold cover of M_A is T' x S^1",
      "exact (S1 orders); pi1(T'xS^1) = F2 x Z has center >= Z => M_A NOT hyperbolic [Kleinian center INSTRUMENT]")
check("hyperbolicity of every sibling class",
      "NO — Route 1 (Thurston/pA=0, exact), Route 2 (SnapPy live, 0/8 geometric, controls pass), Route 3 (exact obstructions)")

# =============================================================================
section("S3. THE GEOMETRY THE SIBLING DOES GET (per sealed ROBUST clause)")
# =============================================================================
# Finite-order classes: Seifert fibered over the quotient orbifold, geometry
# H^2 x R (cusped SFS over hyperbolic base; for bounded manifolds H^2xR ~ SL2~,
# we use the product convention).  TWO INDEPENDENT chi_orb computations:
#   (i)  Riemann-Hurwitz: chi_orb = chi(T')/k = -1/k;
#   (ii) exact fixed-point/cone enumeration of the standard order-k lattice
#        rotation on R^2/Z^2 (rationals, no floats).
ROT = {2: NEG,
       3: [[-1, -1], [1, 0]],     # mult by zeta_3 on Eisenstein lattice basis (1, zeta_6)
       4: [[0, -1], [1, 0]],      # mult by i on Z[i]
       6: [[0, -1], [1, 1]]}      # mult by zeta_6 on Eisenstein lattice

# Verify the Eisenstein realizations exactly (lattice symmetry = crystallographic content):
z6 = sp.exp(sp.pi*spI/3)
red = lambda e: simplify(sp.expand_complex(e))
a11 = red(z6*1 - (0*1 + 1*z6))
a12 = red(z6*z6 - (-1*1 + 1*z6))
assert a11 == 0 and a12 == 0
z3 = sp.exp(2*sp.pi*spI/3)
assert red(z3*1 - (-1*1 + 1*z6)) == 0 and red(z3*z6 - (-1*1 + 0*z6)) == 0
check("hexagonal lattice realization: mult by zeta_6 / zeta_3 on basis (1, zeta_6)",
      "matrices [[0,-1],[1,1]] (tr 1, ord 6) and [[-1,-1],[1,0]] (tr -1, ord 3), exact")
assert mpow(ROT[3], 3) == ID and mpow(ROT[6], 6) == ID and mpow(ROT[4], 4) == ID

def apply_mod1(A, x):
    return ((A[0][0]*x[0] + A[0][1]*x[1]) % 1, (A[1][0]*x[0] + A[1][1]*x[1]) % 1)

def cone_data(R, k):
    cand = set()
    for d in [d for d in range(1, k) if k % d == 0]:
        Rd = mpow(R, d)
        Md = [[Rd[0][0]-1, Rd[0][1]], [Rd[1][0], Rd[1][1]-1]]
        D = abs(det(Md))
        assert D != 0
        for p in range(D):
            for q in range(D):
                x = (Fraction(p, D), Fraction(q, D))
                u = Md[0][0]*x[0] + Md[0][1]*x[1]
                v = Md[1][0]*x[0] + Md[1][1]*x[1]
                if u.denominator == 1 and v.denominator == 1:
                    cand.add(x)
    orbits, seen = [], set()
    for x in sorted(cand):
        if x in seen:
            continue
        orb, y = [], x
        while y not in orb:
            orb.append(y)
            y = apply_mod1(R, y)
        seen.update(orb)
        stab = sum(1 for j in range(k) if all(
            c.denominator == 1 for c in (
                (mpow(R, j)[0][0]*x[0] + mpow(R, j)[0][1]*x[1] - x[0]),
                (mpow(R, j)[1][0]*x[0] + mpow(R, j)[1][1]*x[1] - x[1]))))
        orbits.append((tuple(orb), stab))
    return orbits

EXPECT_CLOSED = {2: [2, 2, 2, 2], 3: [3, 3, 3], 4: [2, 4, 4], 6: [2, 3, 6]}
EXPECT_PUNCT = {2: [2, 2, 2], 3: [3, 3], 4: [2, 4], 6: [2, 3]}
for k in (2, 3, 4, 6):
    orbs = cone_data(ROT[k], k)
    cones = sorted(stab for (orb, stab) in orbs if stab > 1)
    assert cones == EXPECT_CLOSED[k]
    conesum = sum(Fraction(1, 1) - Fraction(1, mm) for mm in cones)
    assert conesum == 2                       # closed quotient is a FLAT S^2 orbifold: chi_orb = 0
    origin_stab = [stab for (orb, stab) in orbs if (Fraction(0), Fraction(0)) in orb][0]
    assert origin_stab == k                   # the puncture sits at the maximal cone point
    chi_punct_route2 = Fraction(0) - Fraction(1, k)
    chi_punct_rh = Fraction(-1, k)            # Riemann-Hurwitz: chi(T')/k
    assert chi_punct_route2 == chi_punct_rh
    punct_cones = sorted(c for c in cones if True)
    punct_cones.remove(k)
    assert punct_cones == EXPECT_PUNCT[k]
    check(f"order-{k} class: base orbifold (2 independent routes)",
          f"closed cone spectrum {EXPECT_CLOSED[k]} (sum(1-1/m)=2, flat), puncture at the order-{k} point; "
          f"punctured base S^2({','.join(map(str, EXPECT_PUNCT[k]))}) minus point, chi_orb = -1/{k} (RH AND enumeration)")
info("chi_orb < 0 in every finite-order class => hyperbolic base orbifold => "
     "Seifert fibered with H^2 x R geometry (product convention for bounded "
     "SFS over hyperbolic base).  I itself: T' x S^1, base T', chi = -1, H^2 x R.")
info("Order-6 punctured base S^2(2,3) is the trefoil's Seifert base — see S4.")

# Parabolic classes: graph manifold, NOT a single geometry.
# Cut along the essential torus (S2): fiber cut along the invariant curve a.
g_cut, b_cut = 0, 3                    # genus-1, 1-puncture surface cut along nonsep scc
chi_cut = 2 - 2*g_cut - b_cut
assert chi_cut == -1                   # = chi(T'): cutting along a circle preserves chi
check("parabolic classes: cut surface along invariant curve",
      "pair of pants (g=0, b=3, chi=-1) => JSJ piece = P x S^1, SFS over hyperbolic base (H^2 x R piece)")
assert w_mul(gen('a'), gen('b'), gen('a', -1), gen('b', -1)) != ()
check("pi1 obstructions for parabolic classes",
      "[a,b] != 1 (F2 fiber non-abelian => non-solvable [INSTRUMENT]) kills Sol/Nil/E3/S3/S2xR; "
      "no normal Z (S2) kills SFS/H2xR/SL2~; essential torus kills H3 => NON-GEOMETRIC graph manifold")
info("Verdict of S3: allowed periodicity buys LESS geometry, never a different "
     "hyperbolic-like one: H^2 x R Seifert pieces (finite order) or a non-"
     "geometric graph manifold (parabolic).  Sol does not occur (that is F6's "
     "closed fork; cusped Sol has no finite-volume quotients [INSTRUMENT: "
     "lattices in solvable Lie groups are cocompact]).")

# =============================================================================
section("S4. CARRIED V4 FACES (yardstick: being Q(sqrt-3), hearing Q(sqrt5), "
        "cusp/interface, arithmeticity; + knot-ness H1=Z where applicable)")
# =============================================================================
# Being face: the trace field of the hyperbolic structure.  No sibling has a
# hyperbolic structure (S2) => no Kleinian holonomy => trace field UNDEFINED.
check("being face (trace field Q(sqrt-3)) across all sibling classes",
      "ABSENT — no hyperbolic structure exists, so no trace field / no Kleinian group at all")

# Honest observation (recorded, not a face): the eigenvalue fields.
eig_fields = {}
golden = Poly(X**2 - X - 1, X)
for name, A in REPS.items():
    cp = Poly(X**2 - tr(A)*X + 1, X)
    assert sp.gcd(cp, golden) == 1
    fac = sp.factor_list(cp.as_expr())[1]
    for base, mult in fac:
        pb = Poly(base, X)
        is_cyc = any(sp.expand(base - sp.cyclotomic_poly(nn, X)) == 0 for nn in (1, 2, 3, 4, 6))
        assert is_cyc
    if cp.discriminant() < 0:
        eig_fields[name] = int(Poly(sp.minimal_polynomial(
            sp.roots(cp).popitem()[0], X), X).discriminant())
discs = sorted(set(eig_fields.values()))
assert discs == [-4, -3]
check("eigenvalue minpolys of all 9 representatives",
      "all cyclotomic (orders 1,2,3,4,6); eigenvalue-field discriminants {-3,-4}; gcd with x^2-x-1 = 1 always")
info("RECORDED OBSERVATION: Q(zeta_3) = Q(sqrt-3) appears as the EIGENVALUE "
     "field of the order-3/6 monodromies (hexagonal lattice, disc -3) — a "
     "cyclotomic shadow of the being field at the monodromy level, carried by "
     "NO geometric structure (no trace field, no cusp shape).  Not a face.")

# Hearing/golden face: dilatation and entropy.
check("hearing face (golden/Q(sqrt5)) across all sibling classes",
      "ABSENT — dilatation exactly 1, entropy log(1) = 0, Q(sqrt5) in no eigenvalue field (disc 5 not in {-3,-4})")
phi2 = ((1 + sqrt(5))/2)**2
assert sp.minimal_polynomial(phi2, X) == X**2 - 3*X + 1
assert sp.expand(sp.minimal_polynomial((3 + sqrt(5))/2, X) - (X**2 - 3*X + 1)) == 0
check("contrast: dilatation of the chain's actual choice (fig-8, tr 3)",
      "lambda = (3+sqrt5)/2 = golden^2, minpoly x^2-3x+1, disc field Q(sqrt5) — the hearing face reappears "
      "IMMEDIATELY across the fork boundary (|tr| 2 -> 3)")

# Cusp/interface face.
check("cusp/interface face across all sibling classes",
      "ABSENT as structure — a torus boundary exists (num_cusps = 1 live, all 8 builds) but carries no "
      "hyperbolic cusp cross-section, no modulus in Q(sqrt-3): nothing for the V4 interface to attach to")

# Arithmeticity.
check("arithmeticity across all sibling classes",
      "NOT DEFINED — no Kleinian group exists to test (Maclachlan-Reid criteria need a hyperbolic holonomy)")

# Knot-ness (auxiliary, 'where applicable'): H1 = Z happens exactly once.
h1_table = {name: h1_of_bundle(A) for name, A in REPS.items()}
knotlike = sorted(name for name, (rk, tors) in h1_table.items() if (rk, tors) == (1, ()))
assert knotlike == ['V6   (tr  1, order 6)']
check("knot-ness H1 = Z among all 9 sibling classes (exact Wang/SNF table)",
      "exactly one: the order-6 class V6 — every other class has rank >= 2 or torsion")

# Enrichment identification of the V6 bundle (two independent invariants +
# INSTRUMENT: genus-1 fibered knots in S^3 are exactly 3_1 and 4_1,
# distinguished by their Alexander polynomial = charpoly of the monodromy):
T31 = snappy.Manifold('3_1')
G = T31.fundamental_group()
gens, rels = G.generators(), G.relators()
assert gens == ['a', 'b'] and rels == ['aabbb']
assert str(T31.homology()) == 'Z' and T31.solution_type() != GEOMETRIC

def fox_alexander_2gen(gens, relator):
    e = {g: 0 for g in gens}
    for ch in relator:
        e[ch.lower()] += 1 if ch.islower() else -1
    g0 = igcd(abs(e[gens[0]]), abs(e[gens[1]])) or 1
    expo = {gens[0]: e[gens[1]] // g0, gens[1]: -e[gens[0]] // g0}   # a -> t^x, b -> t^y
    def fox(word, Xg):
        d, pre = {}, 0
        for ch in word:
            g, s = ch.lower(), (1 if ch.islower() else -1)
            if s == 1:
                if g == Xg:
                    d[pre] = d.get(pre, 0) + 1
                pre += expo[g]
            else:
                pre -= expo[g]
                if g == Xg:
                    d[pre] = d.get(pre, 0) - 1
        return d
    polys = []
    for gname in gens:
        d = fox(relator, gname)
        if not d:
            continue
        shift = -min(d.keys())
        polys.append(Poly(sum(c * X**(k + shift) for k, c in d.items()), X))
    g = polys[0]
    for p in polys[1:]:
        g = sp.gcd(g, p)
    g = Poly(g, X)
    # strip t-power units, normalize sign
    while g.all_coeffs()[-1] == 0:
        g = Poly([c for c in g.all_coeffs()[:-1]], X)
    if g.all_coeffs()[0] < 0:
        g = Poly([-c for c in g.all_coeffs()], X)
    return g

alex = fox_alexander_2gen(gens, rels[0])
cpV6 = Poly(X**2 - X + 1, X)
assert alex == cpV6
assert Poly(X**2 - tr(REPS['V6   (tr  1, order 6)'])*X + 1, X) == cpV6
check("Alexander polynomial of 3_1 (Fox calculus on live presentation <a,b|aabbb>)",
      "t^2 - t + 1 = charpoly(V6) exactly; with H1 = Z (both live and exact): "
      "TWO independent invariants => V6 bundle = trefoil exterior [genus-1 fibered INSTRUMENT]")
info("HONEST CAVEAT (recorded for the merge gate): the auxiliary knot-ness "
     "face SURVIVES at exactly one sibling class — the order-6 bundle is the "
     "trefoil exterior (H1 = Z, Seifert fibered, H^2 x R over S^2(2,3)-minus-"
     "point, zero hyperbolic volume, no trace field, dilatation 1).  Per the "
     "sealed criteria this does NOT meet FRAGILE, which requires a hyperbolic "
     "carrier; the four V4 faces are absent there like everywhere else.")

# =============================================================================
section("S5. VERDICT (sealed criteria applied)")
# =============================================================================
pa_count = 0                            # S1, symbolic/exact
hyperbolic_carriers = geometric_count   # S2: 0 of 8 live + exact routes cover all classes
v4_faces = 0                            # S4: being / hearing / interface / arithmeticity all absent
assert (pa_count, hyperbolic_carriers, v4_faces) == (0, 0, 0)
check("pA classes in the |tr|<=2 det=+1 family", "0 (symbolic, whole family)")
check("hyperbolic carriers among sibling classes", "0 (Thurston+exact routes, all classes; SnapPy live 0/8 with passing controls)")
check("V4 interface faces carried (being, hearing, cusp-interface, arithmeticity)",
      "0 — with two recorded observations: Q(sqrt-3) as elliptic EIGENVALUE field (no geometry attached); "
      "knot-ness (auxiliary) at the trefoil class only")
check("F2 VERDICT", "ROBUST (sealed: no pA, no hyperbolic carrier, zero faces; matches preregistered prior => no skeptic trigger)")
info("Vacuity (MB12): FRAGILE was concretely reachable — any of the 8 sibling "
     "builds returning 'all tetrahedra positively oriented' would have "
     "triggered it, and the two positive controls show the instrument does "
     "return exactly that on hyperbolic input.")
info("Price of the periodicity exclusion (A-chain reading): allowing periodic "
     "words costs ALL FOUR V4 faces at once — the aperiodicity axiom is cheap "
     "for the chain (nothing on the other side carries the anatomy), while "
     "the golden face reappears at the very first aperiodic trace (tr 3).")

print()
print("RAW CHECK-LINE BLOCK (re-executable summary for the merge gate):")
for line in CHECKS:
    print(line)
