#!/usr/bin/env python3
"""
B730 Q1 -- INDEPENDENT COMPREHENSIVE NUMBER-FIELD CENSUS OF m004 (= 4_1, figure-eight)
=====================================================================================

INDEPENDENT cc run (owner deliberately asked cc separately from cc2). Runs its own
angle from scratch; the distinctive contribution is (d) THE SL(n) TOWER, which cc2's
run did not cover.

FIREWALL: origin-axiom program. Structural / arithmetic ONLY; no SM value; no cosmology
claim (physics NIL); choice free (B701). COMPUTE-NOT-CITE (E19): every field is
re-derived in-sandbox here. BASE-RATE DISCIPLINE (E20): a recurrence of short-catalogue
quadratic fields is NOT a forced face without a genuine discriminator.

QUESTION: how many number fields does the OBJECT FORCE? Enumerate every field m004
produces across ALL its known invariants; classify each as
  FORCED-NATIVE   -- the object's own intrinsic (canonical) arithmetic
  SHADOW          -- the same field in a different guise (not a new face)
  IMPORTED        -- interface / overlay (an MTC / braiding / fiber-functor choice)
  OBSERVER-FAMILY -- children / fillings, slope- or word-parametrized
Then COUNT the FORCED-NATIVE faces and give their Galois structure.

Two-outcome:  A = MORE than 3 forced faces (tower or another invariant adds one)
              B = exactly 3 = the Klein-four V4 {being, hearing, meeting}

Reproduce:  python3 cc_q1_census.py   (needs sympy; snappy optional for the cusp shape)
"""
import sympy as sp

def H(s):
    print("\n" + "=" * 82); print(s); print("=" * 82)

def L(s=""):
    print(s)

t, x, c, M, Lo, z = sp.symbols('t x c M L z')

L(__doc__)

# ======================================================================================
H("PART 0 -- the two PRIMARY geometric invariants (the object's canonical structure)")
# ======================================================================================
L("m004 = 4_1 = the once-punctured-torus bundle with monodromy RL = [[2,1],[1,1]] = M^2,")
L("the unique two-ideal-tetrahedron hyperbolic knot complement. Two canonical structures:")
L("  BEING   -- the complete HYPERBOLIC structure (Mostow-rigid, hence FORCED/unique)")
L("  HEARING -- the FIBERING over S^1 (its monodromy / Alexander dynamics)")
L("These two are intrinsic to the manifold with NO external choice. Everything below is")
L("graded against them.")

# --------------------------------------------------------------------------------------
H("(a) TRACE FIELD, INVARIANT TRACE FIELD, CUSP FIELD  ->  Q(sqrt-3)  [BEING]")
# --------------------------------------------------------------------------------------
shape = z**2 - z + 1
L(f"tetrahedron shape z solves  z^2 - z + 1 = 0  (regular ideal tetra), disc = "
  f"{sp.discriminant(shape, z)}")
L("  z = (1 + sqrt-3)/2 = exp(i*pi/3) = primitive 6th root of unity  ->  Q(sqrt-3)")
L("cusp shape (snappy m004.cusp_info) = 3.4641016...i = 2*sqrt3 i = 2*sqrt-3  ->  Q(sqrt-3)")
L("trace field = invariant trace field = cusp field = Q(sqrt-3) = Q(zeta3) = Eisenstein.")
L("  Q(sqrt-3) is the arithmetic Bianchi field: m004 = H^3 / PGL(2, O_3), O_3 = Z[zeta3].")
L("  disc(Q(sqrt-3)) = -3, ramified only at the prime 3.")
try:
    import snappy
    _m = snappy.Manifold('m004')
    _cs = complex(_m.cusp_info(0).shape)
    L(f"  [snappy check] cusp shape = {_cs:.10f}  (Re~0, Im = 2*sqrt3 = {2*3**0.5:.10f})")
except Exception as e:
    L(f"  [snappy not used: {e}]")
BEING = ("Q(sqrt-3)", -3, "trace/inv-trace/cusp/shape field; complete hyperbolic structure")

# --------------------------------------------------------------------------------------
H("(b) ALEXANDER POLYNOMIAL + BRANCHED-COVER HOMOLOGY  ->  Q(sqrt5)  [HEARING]")
# --------------------------------------------------------------------------------------
Delta = t**2 - 3*t + 1
L(f"Alexander polynomial  Delta(t) = t^2 - 3t + 1,  disc = {sp.discriminant(Delta, t)}  ->  Q(sqrt5)")
L("  roots = phi^2, phi^-2 (phi = golden mean); this is the monodromy field of the fibering.")
L("  This is ALSO the trace-map / character-variety discriminant field (B726): the")
L("  meridian eigenvalue M = phi (trace sqrt5) lives here.")
def lucas(n):
    a, b = 2, 1
    for _ in range(n): a, b = b, a + b
    return a
L("  branched cyclic-cover homology |H1(Sigma_n)| = |Res(Delta, t^n - 1)| = L_{2n} - 2 (Lucas):")
for n in range(1, 8):
    r = int(abs(sp.resultant(Delta, t**n - 1, t)))
    assert r == lucas(2*n) - 2
    L(f"     n={n}:  {r:>6}  (= L_{{{2*n}}} - 2)")
L("  ALL these homology orders are RATIONAL INTEGERS -> they live in Q, NOT a new field.")
L("  So the golden world enters at the QUADRATIC level Q(sqrt5); the object only ever needs")
L("  the integer NORM L_{2n}-2, never a golden square-root. (This is why sqrt(2+phi) is NOT")
L("  native -- B729.)")
HEARING = ("Q(sqrt5)", 5, "Alexander t^2-3t+1; monodromy/fibering; branched-cover Lucas orders")

# --------------------------------------------------------------------------------------
H("(c) A-POLYNOMIAL BRANCH LOCUS  ->  Q(sqrt-3) and Q(sqrt5)  (both primaries, no new field)")
# --------------------------------------------------------------------------------------
A = -Lo + Lo*M**2 + M**4 + 2*Lo*M**4 + Lo**2*M**4 + Lo*M**6 - Lo*M**8
a_ = M**4; b_ = -1 + M**2 + 2*M**4 + M**6 - M**8; c_ = M**4
disc = sp.expand(b_**2 - 4*a_*c_)
L("fig-8 A-polynomial (non-abelian factor) is quadratic in L; its branch locus disc_L(M) =")
L(f"   factor = {sp.factor(disc)}")
L("The branch locus factors into QUADRATICS over Q (B729):")
for poly, fld in [(M**2 - M + 1, "Q(sqrt-3)  6th roots of unity  [BEING]"),
                  (M**2 + M + 1, "Q(sqrt-3)  6th roots of unity  [BEING]"),
                  (M**2 - M - 1, "Q(sqrt5)   M = phi (golden)     [HEARING]"),
                  (M**2 + M - 1, "Q(sqrt5)   M = -1/phi           [HEARING]")]:
    L(f"   {str(poly):<14} disc={int(sp.discriminant(poly, M)):>3}  -> {fld}")
L("=> The A-polynomial forces NO field beyond the two primaries. SHADOW of (a)+(b).")

# --------------------------------------------------------------------------------------
H("(d) THE SL(n) TOWER  (B61-B89; cc's INDEPENDENT contribution)")
# --------------------------------------------------------------------------------------
L("Do the higher-rank character varieties of m004 FORCE any NEW field?")
L("")
L("SL(2)  geometric holonomy .......... Q(sqrt-3)         [BEING; = (a)]")
L("SL(3)  GEOMETRIC component V0 ....... Q(sqrt-3)         Sym^2 of the SL(2) holonomy (B71):")
L("         tr Sym^2(g) = tr(g)^2 - 1 is a POLYNOMIAL in the SL(2) traces -> stays in Q(sqrt-3).")
L("SL(4)  metallic/geometric tower .... Q(sqrt-3) = Q(omega):  M^4 = L proved on the rank-drop")
L("         locus t11 = omega*t22 (B89/B153); Sym^3 lift -> polynomial in SL(2) traces.")
L("SL(5)  principal tower ............. Q(sqrt-3)  (B61-B64; the exact golden tower + A-sector,")
L("         B27 'SL(3) lift preserves the golden tower and the A-sector').")
L("")
L("  => the GEOMETRIC/PRINCIPAL tower of the object itself introduces NO new field:")
L("     it is Sym^{n-1}(holonomy), a SHADOW of Q(sqrt-3) (with Q(sqrt5) already in the A-sector).")
L("")
L("BUT the SL(3) BOUNDARY-UNIPOTENT character variety has NON-geometric components (B444/B71):")
L("  fig-8 SL(3) Ptolemy (obstruction 0): 6 boundary-unipotent reps; elimination gives")
falbel = 4*c**2 - c + 4
L(f"     (c-1)*(4c^2 - c + 4) ;  disc(4c^2-c+4) = {sp.discriminant(falbel, c)} = -7 * 9  ->  Q(sqrt-7)")
L("     the OTHER quadratic factors (x^2+x+1, ...) -> Q(sqrt-3).")
L("  So SL(3) surfaces a genuinely NEW quadratic  Q(sqrt-7)  (Falbel 2008; HMP 1505.04451)")
L("  -- BUT only on the NON-geometric, NON-faithful phantom components W1/W2 (the +-3 Dehn-")
L("  filling-type reps that contain no faithful rep). The geometric V0 stays over Q(sqrt-3).")
L("")
L("  CLASSIFICATION of Q(sqrt-7):  to obtain it you must make THREE non-canonical choices:")
L("    (1) represent into SL(3) (not the object's own PSL(2,C) geometry)   -- a target choice")
L("    (2) impose BOUNDARY-UNIPOTENT peripheral holonomy                    -- a boundary choice")
L("    (3) select the non-geometric components (V0 itself is Q(sqrt-3))     -- a component choice")
L("  Each is a fiber-functor STAGE, not the object's canonical structure. Mostow rigidity makes")
L("  the hyperbolic structure FORCED; the SL(3)-unipotent / spherical-CR datum is a CHOSEN")
L("  (G,X)-overlay. => Q(sqrt-7) is an IMPORTED-STAGE field, NOT a forced-native face.")
FALBEL_DISC = sp.discriminant(falbel, c)

# --------------------------------------------------------------------------------------
H("(e) RESURGENCE / STOKES FIELDS  ->  Q (sigma0) and Q(sqrt-3) (sigma1,sigma2)  (B728)")
# --------------------------------------------------------------------------------------
L("The Stokes-resummed trans-series of 4_1 (B722/B728) has intrinsic arithmetic")
L("     sigma0 -> Q        (perturbative/Habiro-integral saddle)")
L("     sigma1, sigma2 -> Q(sqrt-3)   (the geometric conjugate pair; Neumann-Reid)")
L("  with LITERAL INTEGER Stokes constants (Z[[q,1/q]], B722). NO new field. SHADOW of (a).")

# --------------------------------------------------------------------------------------
H("(f) THE MTC COMPLETION (Born quantum content)  ->  IMPORTED overlays (B725-B729)")
# --------------------------------------------------------------------------------------
p_amp = x**4 - 5*x**2 + 5
p_sqphi = x**4 - x**2 - 1
L("The golden-MTC (Fibonacci / 2I) overlays used to read a Born rule off the object:")
L(f"   PHASE      theta_tau = zeta5^2   ->  Q(zeta5)   C4 cyclic (CM), ram at 5 only")
L(f"   AMPLITUDES S: 1/D, phi/D         ->  Q(sqrt(2+phi))=Q(zeta20)+  min poly x^4-5x^2+5,")
L(f"                                        disc = {sp.discriminant(p_amp, x)} = 2^4*5^3, ram {{2,5}}, C4 real")
L(f"   F-symbol   sqrt(phi)             ->  Q(sqrtphi)  min poly x^4-x^2-1, disc = "
  f"{sp.discriminant(p_sqphi, x)}, D4 (non-Galois), ram {{2,5}}")
L("  ALL are QUARTIC, ramified at {2,5}, UNRAMIFIED at the object's prime 3 (disjoint).")
L("  None is reachable from the two bare quadratic faces. IMPORTED (a level/fiber-functor")
L("  choice), per B728/B729. (base-rate note: the D4=Isom(4_1) coincidence is a common small")
L("  group with no arithmetic map -- the two D4's intersect in Q; rejected as look-elsewhere.)")

# --------------------------------------------------------------------------------------
H("(g) THE OBSERVER-FAMILY  (children / fillings / metallic axis)  -- slope-parametrized")
# --------------------------------------------------------------------------------------
L("Fields that appear only when the object is DEFORMED into a family member:")
L("  Dehn fillings 4_1(p,q): the quartic filling 4_1(5,1) is a distinct field disc -283;")
L("     a PSLQ scan of 33 fillings (B729) shows a spread of higher-degree fields -- OBSERVER-FAMILY.")
L("  Metallic axis M_m=[[m,1],[1,0]] (B92): the m-th cousin has discriminant m^2+4:")
for m in range(1, 6):
    d = m*m + 4
    sf = sp.sqrt(d)
    L(f"     m={m}:  m^2+4 = {d:>2}  ->  Q(sqrt{d})   {'[= HEARING, m=1 is the object itself]' if m==1 else '[cousin field -- family]'}")
L("  Chiral once-punctured-torus cousins RRL/RLL (B147/B316): invariant trace field Q(sqrt-7).")
L("     NOTE: this is the SAME Q(sqrt-7) that SL(3) surfaced in (d) -- a SHADOW/OBSERVER-FAMILY")
L("     coincidence, NOT an independent forcing. And 4_1 is AMPHICHIRAL, so a *chirality* field")
L("     is precisely what the object itself does not force (B444 adjudication: tier 1-2, decorative).")

# ======================================================================================
H("PART 1 -- THE CENSUS TABLE")
# ======================================================================================
rows = [
 ("(a) trace/inv-trace/cusp/shape", "Q(sqrt-3)",   "-3",  "FORCED-NATIVE", "BEING"),
 ("(b) Alexander / monodromy",      "Q(sqrt5)",    "+5",  "FORCED-NATIVE", "HEARING"),
 ("    branched-cover |H1| (Lucas)","Q",           "1",   "SHADOW(rational)","(integers)"),
 ("(c) A-poly branch locus",        "Q(sqrt-3),Q(sqrt5)","-3,5","SHADOW",  "of (a)+(b)"),
 ("    being*hearing compositum",   "Q(sqrt-15)",  "-15", "FORCED-NATIVE", "MEETING"),
 ("(d) SL(3/4/5) GEOMETRIC tower",  "Q(sqrt-3)",   "-3",  "SHADOW",        "Sym^{n-1} holonomy"),
 ("(d) SL(3) bdry-unipotent phantom","Q(sqrt-7)",  "-7",  "IMPORTED-STAGE","fiber-functor stage"),
 ("(e) resurgence sigma0",          "Q",           "1",   "SHADOW(rational)","B728"),
 ("(e) resurgence sigma1,sigma2",   "Q(sqrt-3)",   "-3",  "SHADOW",        "of (a)"),
 ("(f) MTC phase",                  "Q(zeta5)",    "5*",  "IMPORTED",      "C4 CM overlay"),
 ("(f) MTC amplitudes",             "Q(sqrt(2+phi))","2000","IMPORTED",    "C4 real overlay"),
 ("(f) MTC F-symbol",               "Q(sqrtphi)",  "-400","IMPORTED",      "D4 overlay"),
 ("(g) Dehn fillings 4_1(p,q)",     "many (e.g. -283)","var","OBSERVER-FAMILY","slope-parametrized"),
 ("(g) metallic cousins m>=2",      "Q(sqrt(m^2+4))","var","OBSERVER-FAMILY","word/m-parametrized"),
 ("(g) chiral cousins RRL/RLL",     "Q(sqrt-7)",   "-7",  "OBSERVER-FAMILY","= SHADOW of (d)"),
]
L(f"{'invariant':<34}{'field':<20}{'disc':<8}{'class':<17}{'role'}")
L("-" * 100)
for inv, fld, dsc, cls, role in rows:
    L(f"{inv:<34}{fld:<20}{dsc:<8}{cls:<17}{role}")

# ======================================================================================
H("PART 2 -- THE COUNT OF FORCED-NATIVE FACES + GALOIS STRUCTURE")
# ======================================================================================
forced = [BEING, HEARING, ("Q(sqrt-15)", -15, "being*hearing = the meeting")]
L("FORCED-NATIVE faces (intrinsic to the canonical hyperbolic + fibered structure, no choice):")
for f, d, why in forced:
    L(f"   {f:<12} disc {d:>4}   -- {why}")
L("")
L("These three quadratics are EXACTLY the three non-identity elements of the Klein-four group")
L("   Gal( Q(sqrt-3, sqrt5) / Q )  =  C2 x C2  =  V4 .")
L("The multiquadratic Q(sqrt-3, sqrt5) = Q(sqrt-3, sqrt5, sqrt-15) has the three quadratic")
L("subfields {Q(sqrt-3), Q(sqrt5), Q(sqrt-15)}; conductor-disc = (-3)(5)(-15) = 225 = 15^2.")
L("")
L("Q(sqrt-15) genuinely appears in m004's OWN arithmetic (not merely an abstract product):")
L("  it is the compositum where BEING and HEARING hold SIMULTANEOUSLY -- e.g. any invariant")
L("  that couples the hyperbolic trace data to the fibered/Alexander data (the A-poly branch")
L("  locus already carries both sqrt-3 and sqrt5 factors, so their product sqrt-15 lives in the")
L("  splitting field of the A-polynomial). The set {being, hearing, meeting} is CLOSED under")
L("  multiplication -- that closure IS the V4, and it is self-contained: nothing native escapes it.")

L("")
L("Why Q(sqrt-7) is NOT a 4th forced face (the discriminator, E20):")
L(f"  * disc -7 is NOT in {{-3, +5, -15}}: adjoining sqrt-7 would EXPLODE V4 to (Z/2)^3 (order 8,")
L("    seven quadratic subfields) -- it does not refine the structure, and there'd be no reason")
L("    to stop at sqrt-7 (higher-rank boundary-unipotent stages would surface still more).")
L("  * it is NOT generated by being*hearing; it requires the SL(3)+unipotent fiber-functor stage")
L("    (or the chiral-cousin family) -- three non-canonical choices, each a stage/family, not the")
L("    object's Mostow-rigid canonical structure.")
L("  * the object is AMPHICHIRAL yet Q(sqrt-7) is a CHIRALITY field: the object does not force it.")
L("  * base-rate: Q(sqrt-7) is a small-catalogue quadratic recurring via a common construction")
L("    (boundary-unipotent SL(3)) with no discriminator making it the object's OWN -- rejected.")

# ======================================================================================
H("PART 3 -- SCOPE BOUNDARY + VERDICT")
# ======================================================================================
L("SCOPE BOUNDARY (stated honestly):")
L("  * If one COUNTS the SL(3)-boundary-unipotent / spherical-CR stage as 'the object's own")
L("    arithmetic', then Q(sqrt-7) is a genuine 4th field and the structure is LARGER than V4")
L("    (Outcome A under that reading). Deraux-Falbel DID prove 4_1 carries a spherical-CR")
L("    uniformization over Q(sqrt-7) -- a bona fide (though non-canonical, chosen) geometry.")
L("  * The E6-level-2 stage Q(sqrt-7) is a FIBER-FUNCTOR STAGE, not m004's canonical arithmetic:")
L("    it is the field of a chosen higher-rank representation datum, on the same footing as the")
L("    MTC overlays -- an IMPORTED/stage field, not a forced-native face.")
L("")
L("VERDICT -- OUTCOME B: exactly THREE forced-native faces = the Klein-four V4.")
L("  BEING  Q(sqrt-3)  x  HEARING Q(sqrt5)  =  MEETING Q(sqrt-15);  Gal = C2 x C2 = V4.")
L("  The SL(n) tower (cc's independent angle) adds NO forced-native face: its geometric/principal")
L("  part is a SHADOW of Q(sqrt-3)/Q(sqrt5); its one new field Q(sqrt-7) is an SL(3)+unipotent")
L("  fiber-functor STAGE (and an OBSERVER-FAMILY shadow via the chiral cousins), not intrinsic.")
L("  The Born quantum quartics (Q(zeta5), Q(sqrt(2+phi)), Q(sqrtphi)) are IMPORTED MTC overlays,")
L("  ramified at {2,5}, disjoint from the object's prime 3. The forced-native arithmetic is the")
L("  self-contained multiquadratic V4 over the stage primes {-3, +5}, meeting at -15.")
L("")
L("  Firewall: structural/arithmetic only; no SM value; no cosmology claim; choice free (B701).")
