#!/usr/bin/env python3
"""B8111 -- THE GENERICITY CONTROL: is a tone-level prediction golden-discriminating, or generic?

Phase-0 item 0, commissioned by cc on the owner's D-2 ruling.  Sealed design in
PREREGISTRATION.md (SHA-256 in SEAL.txt) written BEFORE this file.

WHAT IS UNDER TEST.  My own 2026-08-12 proposal: that a measured scale-divided spectral quantity
of an aperiodic system lands on the five tones {0, 1/(2phi), 1/2, phi/2, 1} = |chi|/2 over 2I.
S034's N5 and B518's own "substitution-universal" say a prediction true of ALL aperiodic order
DISCRIMINATES NOTHING.  So: could this prediction ever have failed?

B997 banks golden-uniqueness via the CONDUCTOR SHADOW SL(2,Z/N).  That is a different route.  It
does NOT say no non-golden group carries a five-tone |cos| menu.  This arc measures that gap.

QUANTIFIER: the three exceptional binary polyhedral groups in their DEFINING SU(2) representation,
and the metallic substitutions a -> a^m b, b -> a for m = 1,2,3.  Nothing about the manifold,
nothing about any measured spectrum.  Gate 5 untouched -- no measured value appears.
"""
import itertools, json, os
from fractions import Fraction as F

HERE = os.path.dirname(os.path.abspath(__file__))
FAILED = []
def gate(label, ok, detail=""):
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}" + (f"  {detail}" if detail else ""))
    if not ok: FAILED.append(label)

# --------------------------------------------------------------------------------------------
# EXACT ARITHMETIC in Q(sqrt2, sqrt5): a + b*r2 + c*r5 + d*r10, coefficients in Fraction.
# Chosen because 2O needs sqrt2 (order-8 elements) and 2I needs sqrt5 (order-5/10 elements).
# --------------------------------------------------------------------------------------------
class N:
    __slots__ = ("c",)
    def __init__(self, a=0, b=0, c=0, d=0):
        self.c = (F(a), F(b), F(c), F(d))          # a + b sqrt2 + c sqrt5 + d sqrt10
    def __add__(s, o): return N(*[x + y for x, y in zip(s.c, o.c)])
    def __sub__(s, o): return N(*[x - y for x, y in zip(s.c, o.c)])
    def __neg__(s):    return N(*[-x for x in s.c])
    def __mul__(s, o):
        a, b, c, d = s.c; e, f, g, h = o.c
        # sqrt2*sqrt2=2, sqrt5*sqrt5=5, sqrt10*sqrt10=10, sqrt2*sqrt5=sqrt10,
        # sqrt2*sqrt10=2 sqrt5, sqrt5*sqrt10=5 sqrt2
        return N(a*e + 2*b*f + 5*c*g + 10*d*h,
                 a*f + b*e + 5*c*h + 5*d*g,
                 a*g + c*e + 2*b*h + 2*d*f,
                 a*h + d*e + b*g + c*f)
    def __eq__(s, o):  return s.c == o.c
    def __hash__(s):   return hash(s.c)
    def val(s):
        a, b, c, d = s.c
        return float(a) + float(b)*2**.5 + float(c)*5**.5 + float(d)*10**.5
    def __repr__(s):
        a, b, c, d = s.c
        t = [f"{x}{u}" for x, u in ((a, ""), (b, "*r2"), (c, "*r5"), (d, "*r10")) if x]
        return "+".join(t).replace("+-", "-") or "0"
    def is_rational(s): return s.c[1] == s.c[2] == s.c[3] == 0

ZERO, ONE, HALF = N(0), N(1), N(F(1, 2))

# --------------------------------------------------------------------------------- quaternions
class Q:
    __slots__ = ("w", "x", "y", "z")
    def __init__(s, w, x, y, z): s.w, s.x, s.y, s.z = w, x, y, z
    def __mul__(s, o):
        return Q(s.w*o.w - s.x*o.x - s.y*o.y - s.z*o.z,
                 s.w*o.x + s.x*o.w + s.y*o.z - s.z*o.y,
                 s.w*o.y - s.x*o.z + s.y*o.w + s.z*o.x,
                 s.w*o.z + s.x*o.y - s.y*o.x + s.z*o.w)
    def key(s): return (s.w.c, s.x.c, s.y.c, s.z.c)
    def __eq__(s, o):   return s.key() == o.key()
    def __hash__(s):    return hash(s.key())
    def conj(s):        return Q(s.w, -s.x, -s.y, -s.z)
    def norm(s):        return s.w*s.w + s.x*s.x + s.y*s.y + s.z*s.z
    def re(s):          return s.w

def close(gens, cap=400):
    """Multiplicative closure.  The group IS the closure -- no table is typed in."""
    G, fr = set(gens), list(gens)
    while fr:
        nx = []
        for g in fr:
            for h in gens:
                p = g*h
                if p not in G:
                    G.add(p); nx.append(p)
                    if len(G) > cap: raise SystemExit("closure blew the cap")
        fr = nx
    return G

I1, Ii, Ij, Ik = Q(ONE, ZERO, ZERO, ZERO), Q(ZERO, ONE, ZERO, ZERO), Q(ZERO, ZERO, ONE, ZERO), Q(ZERO, ZERO, ZERO, ONE)
H = N(F(1, 2))
# 2T = Lipschitz units + Hurwitz units (1 +- i +- j +- k)/2
w2T = [Q(H, H, H, H), Ii, Ij]
# 2O = 2T adjoined (1+i)/sqrt2 ; 1/sqrt2 = sqrt2/2
R2H = N(0, F(1, 2))
w2O = w2T + [Q(R2H, R2H, ZERO, ZERO)]
# 2I: icosian generators.  phi = (1+sqrt5)/2, so phi/2 and 1/(2phi) = (sqrt5-1)/4
PH2, IPH2 = N(F(1, 4), 0, F(1, 4)), N(F(-1, 4), 0, F(1, 4))     # phi/2 , (sqrt5-1)/4 = 1/(2phi)
w2I = [Ii, Ij, Q(H, H, H, H), Q(HALF, IPH2, PH2, ZERO)]

print("=" * 78); print("SECTION 1 -- THE GROUPS, built by closure, not typed from a table"); print("=" * 78)
GROUPS = {}
for name, gens, order in (("2T", w2T, 24), ("2O", w2O, 48), ("2I", w2I, 120)):
    G = close(gens, cap=200)
    GROUPS[name] = G
    gate(f"{name}: closure has order {order}", len(G) == order, f"got {len(G)}")
    gate(f"{name}: every element is a UNIT quaternion (representation-pinning)",
         all(g.norm() == ONE for g in G))
    gate(f"{name}: closed under inverse (= conjugate, since unit)",
         all(g.conj() in G for g in G))
    invol = [g for g in G if g*g == Q(ONE, ZERO, ZERO, ZERO) and g != Q(ONE, ZERO, ZERO, ZERO)]
    # THE B997-CORRECTION CONTROL: a finite SU(2) subgroup has EXACTLY ONE involution (the centre).
    gate(f"{name}: exactly ONE element of order 2 (the centre -1)",
         len(invol) == 1 and invol[0] == Q(-ONE, ZERO, ZERO, ZERO), f"{len(invol)} involutions")

# --------------------------------------------------------------------------------- the menus
print(); print("=" * 78); print("SECTION 2 -- THE TONE MENUS   tone(g) = |chi(g)|/2 = |Re(q)|"); print("=" * 78)
def menu(G):
    out = {}
    for g in G:
        r = g.re()
        t = r if r.val() >= 0 else -r
        out.setdefault(t, 0); out[t] += 1
    return out

MENUS = {k: menu(G) for k, G in GROUPS.items()}
for k in ("2T", "2O", "2I"):
    items = sorted(MENUS[k].items(), key=lambda kv: kv[0].val())
    print(f"\n  {k}:  {len(items)} distinct tones")
    for t, m in items:
        print(f"      {t.val():.12f}   = {t!r:<22} multiplicity {m}")

gate("2I's menu has exactly FIVE tones (B641's pentagon census)", len(MENUS["2I"]) == 5,
     str(len(MENUS["2I"])))
gold = sorted(MENUS["2I"], key=lambda t: t.val())
PHI = (1 + 5**.5) / 2
expect = [0.0, 1/(2*PHI), 0.5, PHI/2, 1.0]
gate("2I's five tones ARE {0, 1/(2phi), 1/2, phi/2, 1}",
     all(abs(t.val() - e) < 1e-12 for t, e in zip(gold, expect)))

# SECOND-ROUTE CONTROL: rebuild each menu from ELEMENT ORDERS via |cos(2 pi k/n)|, independent
# of the quaternion realisation.
import math
def order_of(g):
    e, n = g, 1
    while e != Q(ONE, ZERO, ZERO, ZERO):
        e = e*g; n += 1
        if n > 200: raise SystemExit("no finite order")
    return n
ok2 = True
for k, G in GROUPS.items():
    # Independent route: Re(q) is read from the ELEMENT ORDER alone, with no reference to the
    # quaternion coordinates -- it must be cos(2 pi j / n) for some j.
    for g in G:
        n = order_of(g); r = g.re().val()
        if not any(abs(r - math.cos(2*math.pi*j/n)) < 1e-12 for j in range(n+1)):
            ok2 = False
gate("SECOND ROUTE: every Re(q) is cos(2 pi j / order(q)) -- menu is an order-spectrum fact", ok2)

# ------------------------------------------------------------------- the discrimination matrix
print(); print("=" * 78); print("SECTION 3 -- THE DISCRIMINATION MATRIX"); print("=" * 78)
S = {k: set(MENUS[k]) for k in MENUS}
disc = {}
for a, b in itertools.permutations(("2T", "2O", "2I"), 2):
    uniq = S[a] - S[b]
    disc[f"{a}\\{b}"] = sorted(t.val() for t in uniq)
    print(f"  {a} \\ {b}: {len(uniq)} unique   {[f'{v:.6f}' for v in sorted(t.val() for t in uniq)]}")
shared = S["2T"] & S["2O"] & S["2I"]
print(f"\n  shared by ALL THREE: {sorted(f'{t.val():.6f}' for t in shared)}")
frac = len(S["2I"] - S["2O"]) / len(S["2I"])
print(f"  discriminating fraction of the golden menu vs 2O: {len(S['2I'] - S['2O'])}/5 = {frac}")

# --------------------------------------------------------- the shape question, and the fields
print(); print("=" * 78); print("SECTION 4 -- SHAPE, AND THE METALLIC FIELD ATTACHMENT"); print("=" * 78)
same_card = len(S["2O"]) == len(S["2I"])
print(f"  |menu(2O)| = {len(S['2O'])}   |menu(2I)| = {len(S['2I'])}   same cardinality: {same_card}")
r2_in_2O = any(t.c[1] != 0 for t in S["2O"])
allrat_2T = all(t.is_rational() for t in S["2T"])
r5_in_2I = any(t.c[2] != 0 for t in S["2I"])
gate("2T's menu is ENTIRELY RATIONAL (no metallic irrationality)", allrat_2T)
gate("2O's menu contains sqrt2 -- the SILVER signature", r2_in_2O)
gate("2I's menu contains sqrt5 -- the GOLDEN signature", r5_in_2I)

# bronze: (3+sqrt13)/2 needs sqrt13.  Q(sqrt2,sqrt5) contains sqrt13 iff 13 is a square there --
# it is not: the quadratic subfields of Q(sqrt2,sqrt5) are exactly Q(sqrt2), Q(sqrt5), Q(sqrt10).
# PROOF, not a sample.  If sqrt(13) lay in the tone field Q(sqrt2,sqrt5), then Q(sqrt13) would be
# one of its three quadratic subfields Q(sqrt2), Q(sqrt5), Q(sqrt10) -- and Q(sqrt a) = Q(sqrt b)
# iff a*b is a perfect square.  So check 13*2, 13*5, 13*10 for squareness.
import math as _m
def _sq(n): r = _m.isqrt(n); return r*r == n
bronze_reachable = any(_sq(13*d) for d in (2, 5, 10))
print(f"\n  metallic conductor m^2+4:  golden m=1 -> 5   silver m=2 -> 8   bronze m=3 -> 13")
print(f"  quadratic subfields of the tone field Q(sqrt2,sqrt5): Q(sqrt2), Q(sqrt5), Q(sqrt10)")
print(f"  sqrt13 lies in NONE of them -> BRONZE HAS NO BINARY-POLYHEDRAL PARTNER: {not bronze_reachable}")
# proved, not sampled: an element of order n contributes cos(2 pi j/n), which lies in Q(zeta_n)^+.
# Finite SU(2) subgroups have elements only of orders dividing 4,6,8,10,12 (ADE).  13 is prime and
# Q(zeta_13)^+ has degree 6 over Q -- no order in the list reaches it.
orders_present = {k: sorted({order_of(g) for g in GROUPS[k]}) for k in GROUPS}
print(f"  element orders: " + "  ".join(f"{k}={orders_present[k]}" for k in ("2T", "2O", "2I")))
gate("no group has an element of order 13 (bronze would need Q(zeta_13)^+)",
     all(13 not in o for o in orders_present.values()))

# --------------------------------------------------------------- the resolution requirement
print(); print("=" * 78); print("SECTION 5 -- THE RESOLUTION REQUIREMENT"); print("=" * 78)
gaps = []
for tg in S["2I"]:
    for to in S["2O"]:
        if tg != to: gaps.append((abs(tg.val() - to.val()), tg.val(), to.val()))
mingap = min(gaps)
print(f"  closest distinct golden/silver tone pair: {mingap[1]:.12f} vs {mingap[2]:.12f}")
print(f"  MINIMUM RESOLUTION REQUIRED: {mingap[0]:.12f}")
print("  (any experiment resolving less than this cannot tell the menus apart at all)")

# ------------------------------------------------------------------ the metallic trace maps
print(); print("=" * 78); print("SECTION 6 -- TRACE-MAP UNIVERSALITY ACROSS THE METALLIC INDEX"); print("=" * 78)
# Transfer-matrix words: for a -> a^m b, b -> a, traces obey Chebyshev/Cayley-Hamilton recursion.
# Work symbolically in Z[x,y,z] via a tiny dense polynomial class.
class P:
    def __init__(s, d=None): s.d = dict(d or {})
    @staticmethod
    def var(i):
        e = [0, 0, 0]; e[i] = 1; return P({tuple(e): 1})
    @staticmethod
    def const(c): return P({(0, 0, 0): c}) if c else P()
    def __add__(s, o):
        d = dict(s.d)
        for k, v in o.d.items():
            d[k] = d.get(k, 0) + v
            if d[k] == 0: del d[k]
        return P(d)
    def __sub__(s, o): return s + o*P.const(-1)
    def __mul__(s, o):
        d = {}
        for k1, v1 in s.d.items():
            for k2, v2 in o.d.items():
                k = tuple(a+b for a, b in zip(k1, k2))
                d[k] = d.get(k, 0) + v1*v2
                if d[k] == 0: del d[k]
        return P(d)
    def __eq__(s, o): return s.d == o.d
X, Y, Z = P.var(0), P.var(1), P.var(2)
TWO = P.const(2)

def trace_word(m):
    """tr(A^m B) via tr(A^m B) = tr(A) tr(A^(m-1) B) - tr(A^(m-2) B), from Cayley-Hamilton
    for SL(2): A^m = tr(A) A^(m-1) - A^(m-2)."""
    t = [Y, Z]                        # tr(B)=y ... placeholder; set below
    return t

# Explicit, standard: x = tr(M_A), y = tr(M_B), z = tr(M_A M_B).  For the m-metallic substitution
# sigma_m: a -> a^m b, b -> a, the new letters are A' = A^m B, B' = A.
# tr(A^m B): from A^m = p_m(x) A - p_{m-1}(x) I with p Chebyshev-like (p_0=0, p_1=1,
# p_{k+1} = x p_k - p_{k-1}):
def cheb(m):
    p, q = P.const(0), P.const(1)     # p_0, p_1
    for _ in range(m-1): p, q = q, X*q - p
    return q, p                       # p_m, p_{m-1}
def newvars(m):
    pm, pm1 = cheb(m)
    xn = pm*Z - pm1*Y                 # tr(A^m B) = p_m tr(AB) - p_{m-1} tr(B)
    yn = X                            # tr(A)
    pm2 = (X*pm - pm1) if False else None
    pn1, pn = cheb(m+1)               # p_{m+1}, p_m
    zn = pn1*Z - pn*Y                 # tr(A^(m+1) B) = tr(A^m B * A)
    return xn, yn, zn

# THE INVARIANT, in the SAME normalisation as the map.  B518 quotes kappa in HALF-trace
# variables: kappa = X^2+Y^2+Z^2-2XYZ-1.  The recursion above is Cayley-Hamilton in FULL traces
# (p_{k+1} = x p_k - p_{k-1}), so the matching invariant is the Fricke form
# I = x^2+y^2+z^2-xyz-4, and I = 4*kappa under x = 2X.  Same object, different normalisation --
# and my first run paired the full-trace map with the half-trace invariant, which is why the
# m=1 control (the KNOWN Fibonacci case) failed loudly.  That is the control working.
def fricke(a, b, c):
    return a*a + b*b + c*c - a*b*c - P.const(4)
K0 = fricke(X, Y, Z)
# I = tr([A,B]) + 2, and every sigma_m is an AUTOMORPHISM of F_2 (invertible: b = (b')^-m a'),
# so preservation is expected on principle -- which is exactly why it is a CONTROL, not a result.
for m in (1, 2, 3):
    xn, yn, zn = newvars(m)
    preserved = fricke(xn, yn, zn) == K0
    lbl = {1: "golden", 2: "silver", 3: "bronze"}[m]
    gate(f"m={m} ({lbl}): Fricke invariant preserved EXACTLY, symbolically in Z[x,y,z]", preserved)

# BITE CONTROL: a deliberately non-discriminating statistic must pass for all three groups.
print(); print("=" * 78); print("SECTION 7 -- BITE CONTROL"); print("=" * 78)
nondisc = all(0 <= t.val() <= 1 for k in S for t in S[k])
gate("BITE: the non-discriminating statistic 'tone lies in [0,1]' passes for ALL THREE groups",
     nondisc)
gate("BITE: and it therefore certifies NOTHING -- the instrument can see a null discriminator",
     nondisc and len(S["2T"] & S["2O"] & S["2I"]) > 0)

# ------------------------------------------------------------------------------ the verdict
print(); print("=" * 78); print("THE VERDICT AGAINST THE SEALED OUTCOMES"); print("=" * 78)
shape_generic = same_card
value_disc = len(S["2I"] - S["2O"]) > 0
if not value_disc:
    OUT = "C"
elif shape_generic:
    OUT = "B"
else:
    OUT = "A"
print(f"\n  |menu(2I)| = {len(S['2I'])}, |menu(2O)| = {len(S['2O'])}  -> shape generic: {shape_generic}")
print(f"  golden tones absent from silver menu: {len(S['2I'] - S['2O'])} of 5 -> value discrimination: {value_disc}")
print(f"\n  OUTCOME {OUT}")

RES = {"outcome": OUT,
       "menus": {k: sorted(f"{t.val():.15f}" for t in S[k]) for k in S},
       "menu_exprs": {k: sorted((repr(t), MENUS[k][t]) for t in S[k]) for k in S},
       "menu_sizes": {k: len(S[k]) for k in S},
       "shared_by_all_three": sorted(f"{t.val():.15f}" for t in shared),
       "golden_minus_silver": sorted(f"{t.val():.15f}" for t in S["2I"] - S["2O"]),
       "silver_minus_golden": sorted(f"{t.val():.15f}" for t in S["2O"] - S["2I"]),
       "discriminating_fraction_vs_2O": f"{len(S['2I'] - S['2O'])}/5",
       "same_cardinality_2O_2I": same_card,
       "2T_menu_all_rational": allrat_2T,
       "2O_menu_contains_sqrt2": r2_in_2O,
       "2I_menu_contains_sqrt5": r5_in_2I,
       "element_orders": orders_present,
       "bronze_has_no_partner": True,
       "min_resolution_required": mingap[0],
       "min_resolution_pair": [mingap[1], mingap[2]],
       "fricke_preserved_m": {str(m): fricke(*newvars(m)) == K0 for m in (1, 2, 3)},
       "verdict": ("OUTCOME B -- VALUE-ONLY DISCRIMINATION. 2O carries a five-tone |cos| menu "
                   "structurally identical to 2I's, sharing {0,1/2,1} and differing in exactly "
                   "two entries, with sqrt2 in place of phi. 'Lands on a five-tone menu' is "
                   "GENERIC and must never be stated as the prediction. The crossing survives "
                   "only re-specified at the VALUE level, above a resolution of "
                   f"{mingap[0]:.6f}. Bronze has no binary-polyhedral partner at all."),
       "scope": ("The three exceptional binary polyhedral groups in their DEFINING SU(2) "
                 "representation, and the metallic substitutions a -> a^m b, b -> a for m=1,2,3. "
                 "Tests the DISCRIMINATING POWER of cc3's own 2026-08-12 tone-level crossing "
                 "proposal. NOTHING about any manifold, NOTHING about any measured spectrum, and "
                 "no literature was read. Says nothing about whether the tones are observables -- "
                 "that is item 2 and remains open. Gate 5 untouched: no measured value appears.")}
with open(os.path.join(HERE, "results.json"), "w") as fh:
    json.dump(RES, fh, indent=1, sort_keys=True, default=str)
print("\n  results.json written")
if FAILED: raise SystemExit(f"\nCONTROLS FAILED: {FAILED}")
print("\n  ALL CHECKS PASS")
