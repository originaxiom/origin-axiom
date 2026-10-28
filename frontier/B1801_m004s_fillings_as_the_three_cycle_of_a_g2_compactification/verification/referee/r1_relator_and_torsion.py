"""Referee B1801, check 1+2.
(a) Is 'aBAbaBabAB' a figure-eight group relator?  Compare homomorphism counts into several finite groups with SnapPy's
    m004 group, and with the textbook presentation <x,y | y x y^-1 x y = x y x^-1 y x>.
(b) The order-3 torsion of Q = m004(p,q) recomputed WITHOUT the Alexander polynomial and WITHOUT the arc's r-formula:
    SnapPy's own (non-meridional) presentation of the cusped manifold, its own peripheral words, Fox calculus for the
    exterior's torsion (deficiency-one formula), the core class from SnapPy's own meridian/longitude, Turaev gluing.
(c) dim H^0, H^1 of Q with trivial and order-3 coefficients (Fox Jacobian of the FILLED group): is the order-3 bundle
    acyclic, and does a trivial-holonomy component keep a chiral (1-form) zero mode?"""
import itertools, math, cmath
import sympy as sp
import snappy
from sympy.combinatorics import Permutation, PermutationGroup
from sympy.combinatorics.named_groups import SymmetricGroup, AlternatingGroup

def word_eval(word, img, ident, inv):
    g = ident
    for ch in word:
        x = img[ch.lower()]
        g = g * (x if ch.islower() else inv[ch.lower()])
    return g

def count_homs(relators, gens, G):
    els = list(G.generate())
    ident = Permutation(list(range(G.degree)))
    n = 0
    for x, y in itertools.product(els, repeat=2):
        img = {gens[0]: x, gens[1]: y}; inv = {gens[0]: ~x, gens[1]: ~y}
        if all(word_eval(r, img, ident, inv) == ident for r in relators):
            n += 1
    return n

G = snappy.Manifold("m004").fundamental_group()
print("SnapPy m004:", G.generators(), G.relators(), "peripheral:", G.peripheral_curves())
arc = ["aBAbaBabAB"]
textbook = ["yxYxyXYxYX"]   # y x y^-1 x y (x y x^-1 y x)^-1 = y x Y x y X Y x Y X
groups = {"S3": SymmetricGroup(3), "S4": SymmetricGroup(4), "A5": AlternatingGroup(5), "S5": SymmetricGroup(5)}
# PSL(2,7) as permutations on 8 points (projective line over F7)
def psl27():
    pts = list(range(7)) + ["inf"]
    def mob(a, b, c, d):
        perm = []
        for z in pts:
            if z == "inf":
                w = "inf" if c % 7 == 0 else (a * pow(c, -1, 7)) % 7
            else:
                den = (c * z + d) % 7
                w = "inf" if den == 0 else ((a * z + b) * pow(den, -1, 7)) % 7
            perm.append(pts.index(w))
        return Permutation(perm)
    return PermutationGroup([mob(1, 1, 0, 1), mob(0, 6, 1, 0)])
groups["PSL27"] = psl27()
for name, H in groups.items():
    c_snappy = count_homs(G.relators(), G.generators(), H)
    c_arc = count_homs(arc, ["a", "b"], H)
    c_tb = count_homs(textbook, ["x", "y"], H)
    print(f"  |Hom(-, {name})| (order {H.order()}): SnapPy m004 {c_snappy}, arc relator {c_arc}, textbook 4_1 {c_tb}")

# ---- (b) torsion from SnapPy's own presentation + peripheral words -------------------------------------------------
t = sp.symbols("t")
def fox_abel(word, gen, phi):
    """Fox derivative d word / d gen, abelianised by phi: letter -> exponent of t."""
    total = 0; prefix = 0
    for ch in word:
        e = 1 if ch.islower() else -1; g = ch.lower()
        if g == gen:
            total += t**prefix if e == 1 else -t**(prefix - phi[g])
        prefix += e * phi[g]
    return sp.expand(total)

def abel_exp(word, phi):
    return sum((1 if ch.islower() else -1) * phi[ch.lower()] for ch in word)

gens = G.generators(); rel = G.relators()[0]
# abelianisation of the cusped group: H1 = Z; find phi: gen -> Z with phi(rel) = 0, primitive
cands = [(i, j) for i in range(-3, 4) for j in range(-3, 4) if (i, j) != (0, 0) and math.gcd(i, j) == 1]
phi = None
for i, j in cands:
    ph = {gens[0]: i, gens[1]: j}
    if abel_exp(rel, ph) == 0:
        phi = ph; break
mer, lon = G.peripheral_curves()[0]
mu_exp, la_exp = abel_exp(mer, phi), abel_exp(lon, phi)
if mu_exp < 0:
    phi = {k: -v for k, v in phi.items()}; mu_exp, la_exp = -mu_exp, -la_exp
print("phi on generators:", phi, "| meridian word", mer, "-> t^%d" % mu_exp, "| longitude word", lon, "-> t^%d" % la_exp)
assert mu_exp == 1 and la_exp == 0
# exterior torsion (Turaev convention): tau(X) = det(d r/d x_j) / (phi(x_i) - 1), i != j  -> should be Delta(t)/(t-1)
for gi, gj in ((gens[0], gens[1]), (gens[1], gens[0])):
    Dj = fox_abel(rel, gj, phi)
    tauX = sp.simplify(Dj / (t**phi[gi] - 1))
    print(f"  tau(X) via d r/d {gj} / (t^phi({gi}) - 1) =", sp.factor(tauX))

def tau_Q(p, q, k):
    """|tau(Q = X(p mu + q lambda), chi)| with chi(mu) = zeta = e^{2 pi i k/p}; core = r mu + s lambda with p s - q r = 1."""
    z = cmath.exp(2j * math.pi * k / p)
    # choose x_i with phi(x_i) != 0 for the denominator, differentiate in the other generator
    gi = gens[0] if phi[gens[0]] != 0 else gens[1]; gj = gens[1] if gi == gens[0] else gens[0]
    Dj = fox_abel(rel, gj, phi)
    num = complex(sp.N(Dj.subs(t, z)))
    tauX = num / (z**phi[gi] - 1)
    # core class: any (r, s) with p s - q r = 1  (its class in H1(X) = r, lambda is null-homologous)
    r = None
    for rr in range(-60, 61):
        if (1 + q * rr) % p == 0:
            r = rr; break
    core_char = z**r
    return abs(tauX / (core_char - 1)), r

print("\n(b) |tau(Q, order-3 chi)| from SnapPy's own words (no Alexander polynomial, no r-formula):")
for (p, q) in [(3, 2), (3, 4), (3, 5), (3, -2), (6, 1), (6, 5), (9, 1), (9, 2), (12, 1), (15, 2), (21, 4), (30, 7)]:
    for k in (p // 3, 2 * p // 3):
        val, r = tau_Q(p, q, k)
        print(f"  m004({p},{q}) k={k}: |tau| = {val:.12f}   (core class r = {r}; arc's r = {(-pow(q, -1, p)) % p})")
# a control: characters of other orders give other values (the instrument can fail)
print("  control, m004(6,1) order-6 char:", round(tau_Q(6, 1, 1)[0], 9), "; m004(10,3) order-10 char:", round(tau_Q(10, 3, 1)[0], 9),
      "; m004(10,3) order-5 char:", round(tau_Q(10, 3, 2)[0], 9))

# ---- (c) twisted cohomology of the CLOSED filled manifold from its own presentation ---------------------------------
print("\n(c) dim H^0, H^1 of Q with coefficients C_chi (Fox Jacobian of the filled group):")
for (p, q) in [(3, 2), (6, 1), (9, 2), (12, 1)]:
    M = snappy.Manifold("m004"); M.dehn_fill((p, q))
    GQ = M.fundamental_group()
    gQ = GQ.generators(); rQ = GQ.relators()
    # abelianisation Z/p: find phi: gens -> Z/p killing every relator with phi surjective
    sol = None
    for vals in itertools.product(range(p), repeat=len(gQ)):
        ph = dict(zip(gQ, vals))
        if all(abel_exp(r, ph) % p == 0 for r in rQ) and math.gcd(math.gcd(*vals) if len(vals) > 1 else vals[0], p) == 1:
            sol = ph; break
    for label, kk in (("trivial", 0), ("order-3", p // 3)):
        z = cmath.exp(2j * math.pi * kk / p)
        J = []
        for r in rQ:
            row = []
            for g in gQ:
                total = 0; prefix = 0
                for ch in r:
                    e = 1 if ch.islower() else -1; gg = ch.lower()
                    if gg == g:
                        total += z**prefix if e == 1 else -z**(prefix - sol[gg])
                    prefix += e * sol[gg]
                row.append(total)
            J.append(row)
        import numpy as np
        rank = np.linalg.matrix_rank(np.array(J, dtype=complex), tol=1e-9)
        h0 = 1 if kk == 0 else 0
        # Z^1 = {derivations} has dim = #gens - rank(J); B^1 has dim (1 - h0) ; H^1 = Z^1 - B^1
        h1 = (len(gQ) - rank) - (1 - h0)
        print(f"  m004({p},{q}) [{len(gQ)} gens, {len(rQ)} rels] {label:8s}: H^0 = {h0}, H^1 = {h1}")
print("r1 exit 0")
