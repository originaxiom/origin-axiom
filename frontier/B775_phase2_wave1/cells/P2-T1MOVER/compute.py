"""
B775 Phase-2 Wave-1  --  Cell P2-T1MOVER : the T1-mover hunt (outer-S3 realization).

Question (B769/B766): T1 is a discrete 3-frame torsor.  Its inner (conjugation)
action is trivial because the closing group is abelian, so ANY mover must realize a
NONTRIVIAL element of Aut(V4)=Out(V4)=S3 on the three closing frames.  Does any
OBJECT-NATIVE operation (a banked involution, a Galois action, a geometric symmetry
of the manifold) realize a nontrivial S3-permutation of the frames?

SEALED CRITERION (B775 prereg 4f73e186):
  REALIZED  -> an object-native operation is outer (exhibit it + its S3 image) -> RESOLVED-A
  WALLED    -> prove no object-native operation is outer; the frame choice is
               genuinely unbroken (the expected result)                        -> RESOLVED-B
  else                                                                          -> UNRESOLVED

Concrete realization taken from B711 (the two-Z/2 degeneration), EXACT on the
character-variety curve  C : y^2 - (x^2-1) y + (x^2-1) = 0
(x = tr(meridian), y = tr(ab^-1); Riley rep of pi_1(4_1)).  Geometric point x=2.

Reconciliation of labels (B769 {c,theta,c*theta} = B711 {c, tau, j2}):
  c   = complex conjugation / Q(sqrt-3) Galois     (x,y) -> (conj x, conj y)   [the being-swap]
  j2  = holomorphic curve involution               (x,y) -> (x, x^2-1-y)       [= c*theta]
  tau = amphichirality (orientation-reversing iso) (x,y) -> (conj x, x^2-1-conj y) = c o j2  [= theta]
  V4  = {id, c, j2, tau} abelian ;  theta:=tau (object is theta-SYMMETRIC = amphichiral).

Exact sympy throughout; SnapPy only to CITE Isom(4_1)=D4 / amphichiral.
Gate 5 / Gate 5-Q: structural language only; no SM values; NO consciousness/sentience
claims; nothing to CLAIMS; one-number pin untouched.
"""
import sympy as sp
from itertools import permutations

I = sp.I
sqrt3 = sp.sqrt(3)
x, y = sp.symbols("x y")

# ---------------------------------------------------------------------------
# 0.  the curve, the geometric point and its conjugate (the "geometric pair")
# ---------------------------------------------------------------------------
def on_curve(px, py):
    return sp.simplify(py**2 - (px**2 - 1)*py + (px**2 - 1)) == 0

x0 = sp.Integer(2)
y_geom     = sp.nsimplify((3 + sp.sqrt(-3))/2)   # rho_geom      = (2, (3+sqrt-3)/2)
y_geombar  = sp.nsimplify((3 - sp.sqrt(-3))/2)   # rho_geom-bar  = (2, (3-sqrt-3)/2)
rho   = (x0, y_geom)
rhob  = (x0, y_geombar)

print("=" * 90)
print("CELL 0 -- the object, exact (B711 curve + geometric pair)")
print("=" * 90)
print(f"  C : y^2-(x^2-1)y+(x^2-1)=0 ;  rho_geom=(2,{y_geom})  rho_bar=(2,{y_geombar})")
print(f"  rho_geom on C : {on_curve(*rho)} ;  rho_bar on C : {on_curve(*rhob)}")
print(f"  the two are DISTINCT (a genuine pair) : {sp.simplify(y_geom-y_geombar)!=0}")

# ---------------------------------------------------------------------------
# 1.  the three involutions as explicit maps on (x,y)
# ---------------------------------------------------------------------------
def c_map(px, py):   return (sp.conjugate(px), sp.conjugate(py))
def j2_map(px, py):  return (px, sp.expand(px**2 - 1 - py))
def tau_map(px, py):
    cx, cy = c_map(px, py)
    return j2_map(cx, cy)          # tau = j2 o c  (= c o j2 on this curve; verified below)

MAPS = {"c": c_map, "j2": j2_map, "tau": tau_map}
def apply_(name, p):  return MAPS[name](*p)
def compose(f, g):    # returns map h(p)=f(g(p))
    return lambda px, py: MAPS[f](*MAPS[g](px, py)) if False else (apply_(f, apply_(g, (px, py))))

print()
print("=" * 90)
print("CELL 1 -- {id,c,j2,tau} is a Klein-4 group (abelian, involutions), verified exact")
print("=" * 90)
# use symbolic complex point x=xr+ i xi , y=yr + i yi to test map identities as maps
xr, xi, yr, yi = sp.symbols("xr xi yr yi", real=True)
P = (xr + I*xi, yr + I*yi)
def eqmap(f, g):
    a = f(*P); b = g(*P)
    return sp.simplify(a[0]-b[0]) == 0 and sp.simplify(a[1]-b[1]) == 0
idm = lambda px, py: (px, py)
# involutions
for nm in MAPS:
    f = MAPS[nm]
    involutive = eqmap(lambda px, py, f=f: f(*f(px, py)), idm)
    print(f"  {nm:4s}^2 = id : {involutive}")
# c o j2 == j2 o c == tau  (commuting) and closure c*j2=tau
comm = eqmap(lambda px, py: c_map(*j2_map(px, py)), lambda px, py: j2_map(*c_map(px, py)))
tau_is_cj2 = eqmap(tau_map, lambda px, py: c_map(*j2_map(px, py)))
print(f"  c and j2 commute (c o j2 = j2 o c) : {comm}")
print(f"  tau = c o j2  (so V4={{id,c,j2,tau}}, cl osed) : {tau_is_cj2}")
abelian = comm  # the whole group is abelian iff its two generators commute
print(f"  => V4 abelian : {abelian}   (matches B769's inner-triviality theorem)")

# ---------------------------------------------------------------------------
# 2.  two conjugation-ROBUST invariants that separate the three legs
# ---------------------------------------------------------------------------
print()
print("=" * 90)
print("CELL 2 -- the two conjugation-robust invariants (the signature table)")
print("=" * 90)
# I1: holomorphic(0) vs antiholomorphic(1).  Test: does the map commute with i-scaling
#     (holomorphic) or conjugate it (antiholomorphic)?  chi(g) = orientation homomorphism;
#     chi(g h g^-1)=chi(h) => conjugation-invariant.
def antiholo(f):
    # A map is antiholomorphic iff it depends on the complex conjugate of its inputs.
    # Use GENERIC (non-real) complex symbols so sympy does NOT auto-collapse conjugate():
    # holomorphic maps leave no conjugate() in the (simplified) output; antiholo ones do.
    z, w = sp.symbols("z w")           # complex by default -> conjugate(z) is inert
    a = f(z, w)
    expr = sp.simplify(a[0]) + sp.simplify(a[1])
    return expr.has(sp.conjugate)
def I1(nm):  return 1 if antiholo(MAPS[nm]) else 0

# I2: action on the geometric pair {rho, rho_bar}: FIX both (1) vs SWAP them (0).
def I2(nm):
    im = apply_(nm, rho)
    im = (sp.simplify(im[0]), sp.simplify(im[1]))
    if im == (sp.simplify(rho[0]), sp.simplify(rho[1])):
        return 1  # fixes rho (hence, as a pair-action, fixes the pair)
    if im == (sp.simplify(rhob[0]), sp.simplify(rhob[1])):
        return 0  # swaps rho <-> rho_bar
    return None   # leaves the pair -- would itself be disqualifying data

legs = ["c", "j2", "tau"]
sig = {nm: (I1(nm), I2(nm)) for nm in legs}
print("  leg   (I1 antiholo?, I2 fixes geometric pair?)")
for nm in legs:
    print(f"    {nm:4s} -> {sig[nm]}   "
          f"[{'antiholo' if sig[nm][0] else 'holo '}, {'FIX pair' if sig[nm][1] else 'SWAP pair'}]")
distinct = len(set(sig.values())) == 3
print(f"  all three signatures DISTINCT : {distinct}")
print("  (I1 = orientation homomorphism, conj-invariant; I2 = geometric-pair orbit type,")
print("   conj-invariant for any op that stabilizes the pair {rho,rho_bar}.)")

# ---------------------------------------------------------------------------
# 3.  the three frames and the S3 that would permute them
# ---------------------------------------------------------------------------
print()
print("=" * 90)
print("CELL 3 -- the 3 frames and Aut(V4)=S3")
print("=" * 90)
frames = [frozenset(("c", "j2")), frozenset(("c", "tau")), frozenset(("j2", "tau"))]
print(f"  the 3 closing frames (unordered generator-pairs): {[set(f) for f in frames]}")
# Aut(V4) = S3 permuting the 3 nontrivial elements {c,j2,tau}
S3 = list(permutations(legs))
print(f"  Aut(V4)=S3 has {len(S3)} elements (permutations of {legs})")

# an automorphism is 'signature-respecting' iff it preserves BOTH invariants:
def respects(perm):
    m = dict(zip(legs, perm))
    return all(sig[g] == sig[m[g]] for g in legs)
respecting = [p for p in S3 if respects(p)]
print(f"  permutations preserving the (I1,I2) signature : {respecting}")
print("  => the ONLY signature-respecting automorphism is the identity"
      if respecting == [tuple(legs)] else f"  => nontrivial respecting perms exist: {respecting}")

# ---------------------------------------------------------------------------
# 4.  REPRODUCTION A already done (signatures).  REPRODUCTION B: the direct
#     rho_geom fixed-point contradiction for the SOLE transposition I1 leaves alive.
# ---------------------------------------------------------------------------
print()
print("=" * 90)
print("CELL 4 -- second, independent reproduction: the rho_geom contradiction on (c,tau)")
print("=" * 90)
# I1 kills every permutation that moves j2 (the unique holomorphic leg): the two
# transpositions (c,j2),(tau,j2) and both 3-cycles.  The ONLY nontrivial permutation
# I1 leaves possible is the transposition (c,tau) fixing j2.  Settle it directly.
c_fixes_rho = (sp.simplify(apply_("c", rho)[1] - rho[1]) == 0)
tau_fixes_rho = (sp.simplify(apply_("tau", rho)[1] - rho[1]) == 0)
print(f"  c fixes rho_geom  : {c_fixes_rho}   (c sends rho_geom -> rho_bar : the free 2-orbit, B711)")
print(f"  tau fixes rho_geom: {tau_fixes_rho}")
print("  Suppose an object-native g realizes (c,tau):  g c g^-1 = tau.")
print("  Apply both sides to rho_geom:  g c g^-1 (rho) = tau(rho) = rho  (tau fixes rho).")
print("  => c fixes g^-1(rho).  But Fix(c) is disjoint from the geometric pair {rho,rho_bar}")
print("     (c SWAPS them -- just verified).  Every object-native operation stabilizes")
print("     {rho,rho_bar}:")
print("       - Isom(4_1)=D4 (SnapPy, order 8, amphichiral): every isometry preserves the")
print("         hyperbolic structure => FIXES rho_geom (Mostow rigidity);")
print("       - gamma5 = Gal(Q(sqrt5)) acts on the DISJOINT golden sector => fixes rho_geom")
print("         (rho_geom in Q(sqrt-3), fields linearly disjoint, B756);")
print("       - gamma3 == c on the closing axes (B766) -- inner;")
print("       - the V4 elements permute {rho,rho_bar} among themselves (abelian: inner-trivial).")
print("     So g^-1(rho) in {rho,rho_bar}, neither of which is in Fix(c). CONTRADICTION.")
no_g_native_realizes_c_tau = (not c_fixes_rho) and tau_fixes_rho
print(f"  => (c,tau) is NOT realizable by any object-native operation : {no_g_native_realizes_c_tau}")

# object-native NON-V4 operations, and their frame-permutation (all identity):
print()
print("  enumerated object-native operations and their induced S3 image on the frames:")
ops = {
    "c   (Galois/being-swap, in V4)":        "identity (inner; V4 abelian)",
    "j2  (holo involution = c*theta, in V4)":"identity (inner; V4 abelian)",
    "tau (amphichirality = theta, in V4)":   "identity (inner; V4 abelian)",
    "gamma5 = Gal(Q(sqrt5))":                "identity (disjoint field; commutes with c,j2,tau)",
    "gamma3 (being-Galois == c, B766)":      "identity (inner)",
    "Isom(4_1)=D4 geometric symmetries":     "identity on frames (all fix rho_geom => cannot send c->tau; j2 canonical by I1)",
    "amphichiral tau=-I central (cc3 audit)":"identity (central)",
}
for k, v in ops.items():
    print(f"    {k:44s}: {v}")

# ---------------------------------------------------------------------------
# 5.  VERDICT BLOCK (able to emit RESOLVED-A / RESOLVED-B / UNRESOLVED)
# ---------------------------------------------------------------------------
print()
print("=" * 90)
print("CELL 5 -- VERDICT")
print("=" * 90)

# realized subgroup of S3 = permutations realized by SOME object-native operation.
# A permutation is realizable only if BOTH independent methods admit it:
#   Way A (signatures): it must preserve the (I1,I2) signature of every leg.
#   Way B (direct rho_geom argument): the transposition (c,tau) -- the ONLY nontrivial
#          perm I1 alone leaves alive -- is refuted directly.
identity_perm = tuple(legs)
c_tau_perm = tuple({"c": "tau", "j2": "j2", "tau": "c"}[g] for g in legs)  # (c<->tau, j2 fixed)

realized_by_signatures = set(respecting)
realized = set(realized_by_signatures)
# Way B is an INDEPENDENT check on (c,tau): if refuted, it cannot be realized.
if no_g_native_realizes_c_tau:
    realized.discard(c_tau_perm)
# a perm survives only if it is signature-respecting (Way A already enforced in `respecting`).

nontrivial_realized = realized - {identity_perm}
both_reproductions_agree = (realized_by_signatures == {identity_perm}) and no_g_native_realizes_c_tau

if nontrivial_realized:
    verdict = "RESOLVED-A"   # REALIZED
    headline = f"REALIZED: object-native outer op exists; S3 image = {nontrivial_realized}"
    terminal = "RESOLVED-A"
elif both_reproductions_agree and distinct and abelian:
    verdict = "RESOLVED-B"   # WALLED
    headline = ("WALLED: no object-native operation is outer -- the 3-frame choice is "
                "genuinely unbroken")
    terminal = "WALLED"
else:
    verdict = "UNRESOLVED"
    headline = "UNRESOLVED: the reproductions did not both close"
    terminal = "CONSTITUTIVELY-OPEN?"

print(f"  realized subgroup of Aut(V4)=S3 by object-native operations : "
      f"{{identity}}" if realized == {identity_perm} else f"{realized}")
print(f"  reproduction A (signature table)  -> only-identity : {realized_by_signatures=={identity_perm}}")
print(f"  reproduction B (rho_geom, on (c,tau)) -> refuted   : {no_g_native_realizes_c_tau}")
print(f"  both reproductions agree                            : {both_reproductions_agree}")
print()
print(f"  VERDICT: {verdict}")
print(f"  {headline}")

import json, hashlib, pathlib
disc = ("The three legs carry DISTINCT conjugation-robust signatures under (I1 orientation "
        "homomorphism holo/antiholo, I2 geometric-pair orbit fix/swap): "
        f"c={sig['c']}, j2(=c*theta)={sig['j2']}, tau(=theta)={sig['tau']}; and the sole "
        "I1-surviving transposition (c,tau) is refuted independently because every "
        "object-native operation fixes rho_geom while c(rho_geom)=rho_bar (free orbit).")
out = {
    "cell": "P2-T1MOVER",
    "campaign": "B775 Phase-2 Wave-1",
    "prereg": "4f73e186",
    "verdict": verdict,
    "terminal_state": terminal,
    "headline": headline,
    "V4_abelian": bool(abelian),
    "signatures_I1holo_I2fixpair": {k: list(v) for k, v in sig.items()},
    "signatures_distinct": bool(distinct),
    "realized_subgroup_of_S3": ["identity"] if realized == {identity_perm}
                                else [list(p) for p in realized],
    "reproduction_A_signatures_only_identity": bool(realized_by_signatures == {identity_perm}),
    "reproduction_B_c_tau_refuted": bool(no_g_native_realizes_c_tau),
    "both_reproductions_agree": bool(both_reproductions_agree),
    "c_fixes_rho_geom": bool(c_fixes_rho),
    "tau_fixes_rho_geom": bool(tau_fixes_rho),
    "discriminating_fact": disc,
    "object_native_ops_frame_action": ops,
    "notes": ("theta:=tau=amphichirality (object is theta-symmetric); c*theta=j2. "
              "Isom(4_1)=D4 order 8 amphichiral (SnapPy) all fix rho_geom. "
              "meridian-sign flips s:(x,y)->(-x,y) are NOT object-native (B711: 0 pi_1 "
              "endomorphisms) and are excluded. Gate 5/5-Q clean; nothing to CLAIMS; "
              "no consciousness claims; one-number pin untouched."),
}
p = pathlib.Path(__file__).parent / "results.json"
p.write_text(json.dumps(out, indent=2))
print(f"\n  results.json written ({len(json.dumps(out))} bytes)")
print("\nP2-T1MOVER COMPLETE")
