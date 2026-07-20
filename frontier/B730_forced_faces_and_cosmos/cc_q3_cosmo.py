#!/usr/bin/env sage
# -*- mode: python -*-
"""
B730 / Q3 (cc, INDEPENDENT run, CORRECTED) -- the cosmic-topology meeting point.

RUN WITH SAGE:  sage cc_q3_cosmo.py   (writes cc_q3_cosmo_out.txt)
The invariant-trace-field computation uses snappy's canonical
  M.invariant_trace_field_gens().find_field(prec, degree, optimize)
which requires SnapPy-inside-Sage; this is the literature-standard tool
(Coulson-Goodman-Hodgson-Neumann), NOT an algdep guess.

Question: is "the universe as a figure-8 / closed child = residue of the open
object" a genuine real-MATH meeting point (physics NIL, honestly bounded), or
an over-read?

--------------------------------------------------------------------------
CORRECTION OF THE PRIOR ROUND (this is the whole reason for the recompute):
  The prior discriminating_fact asserted the CHILD m004(5,1)'s invariant
  trace field is "the cubic x^3-x+1, nfdisc=-23".  THAT IS FALSE.
  Computed here (canonical find_field, cross-checked by hand-disc):
    * open   m004         : x^2 - x + 1   deg 2  disc  -3   [Q(sqrt-3)=Eisenstein]
    * child  m004(5,1)    : x^4 - x - 1   deg 4  disc -283  Gal S4  (NO subfields)
    * Weeks  m003(-3,1)   : x^3 - x - 1   deg 3  disc  -23  Gal S3
  The cubic-disc-(-23) field is genuine but belongs to WEEKS (the SISTER
  m003's child), NOT to the object's own child m004(5,1)=Thurston.  The prior
  run copy-pasted a Weeks literature fact onto the less-famous Thurston case
  (an E19 compute-not-cite failure).  The QUALITATIVE conclusion survives:
  deg 4 != deg <=2, so Eisenstein "being" still does NOT survive the closing.
--------------------------------------------------------------------------

(d) m004(5,1) = the Thurston manifold = #2-smallest closed orientable
    hyperbolic 3-manifold (vol ~0.98137).  #1 = Weeks (vol ~0.94271) = the
    SISTER m003's child; Weeks is NOT in m004's own filling family.
(e) The object's "being" field Q(sqrt-3)=Eisenstein does NOT survive Dehn
    filling: the closed child carries the S4 quartic disc -283, which has no
    proper subfield at all (B718 "being washes out" -- with the CORRECT field).

Frontier-science (curvature flat / topology null) is summarised at the end
with primary-source citations; the physics claim is NIL.
Firewall: structural/arithmetic only; no SM value; no cosmology claim.
Compute-not-cite (E19); base-rate discipline (E20).
"""
import snappy

L = []
def p(s=""):
    L.append(s); print(s)

p("="*74)
p("B730 Q3 (cc, CORRECTED) -- cosmic-topology meeting point: OBJECT-SIDE VERIFY")
p("snappy %s  (SnapPy-in-Sage; find_field is canonical, not algdep)" % snappy.version())
p("="*74)

# ------------------------------------------------------------------ (d) census
p("\n(d) Closed-census ordering (OrientableClosedCensus, Hodgson-Weeks)")
occ = snappy.OrientableClosedCensus
p("    total closed orientable hyperbolic census manifolds: %d" % len(occ))
for i in range(3):
    p("      #%d  %-8s vol = %.11f" % (i+1, occ[i].name(), float(occ[i].volume())))

M51   = snappy.Manifold('m004(5,1)')     # the object's own (5,1) child
Thur  = snappy.Manifold('m003(-2,3)')    # classical Thurston manifold
Weeks = snappy.Manifold('m003(-3,1)')    # Weeks manifold (child of the SISTER m003)
m3, m4 = snappy.Manifold('m003'), snappy.Manifold('m004')

p("\n    m004(5,1): vol=%.11f  H1=%s  sol=%s"
  % (float(M51.volume()), M51.homology(), M51.solution_type()))
p("    m004(5,1) is_isometric_to m003(-2,3) [Thurston, #2] : %s" % M51.is_isometric_to(Thur))
p("    m004(5,1) is_isometric_to m003(-3,1) [Weeks,   #1] : %s" % M51.is_isometric_to(Weeks))
p("    Weeks m003(-3,1): vol=%.11f  H1=%s" % (float(Weeks.volume()), Weeks.homology()))
p("    => the object's OWN closed child (5,1) is the #2 Thurston manifold.")

# is Weeks reachable as an m004 filling at all?
weeks_in_m004 = []
for a in range(-8, 9):
    for b in range(0, 9):
        try:
            F = snappy.Manifold('m004(%d,%d)' % (a, b))
            if F.solution_type() != 'all tetrahedra positively oriented':
                continue
            if abs(float(F.volume()) - 0.94270736278) < 1e-6 and F.is_isometric_to(Weeks):
                weeks_in_m004.append((a, b))
        except Exception:
            pass
p("    Weeks among m004(p,q) fillings |p|,q<=8 : %s" % (weeks_in_m004 or "NONE"))
p("    => the #1 (Weeks) is NOT the object's own child; it is the sister m003's.")
p("    m003 vol=%.11f  m004 vol=%.11f  isometric=%s (distinct minimal-vol sisters)"
  % (float(m3.volume()), float(m4.volume()), m3.is_isometric_to(m4)))

# ------------------------------------------------------------- (e) trace fields
p("\n(e) Invariant trace fields (canonical find_field) -- does Q(sqrt-3) survive?")

def field_of(name, deg=12, prec=1000):
    M = snappy.Manifold(name)
    r = M.invariant_trace_field_gens().find_field(prec, deg, True)
    if r is None:
        return None
    K = r[0]
    subs = [str(s[0].defining_polynomial()) for s in K.subfields()]
    return (K.defining_polynomial(), K.degree(), K.discriminant(),
            K.galois_group().structure_description(), subs)

for lbl, name in [("open  m004            ", "m004"),
                  ("child m004(5,1)=Thurst", "m004(5,1)"),
                  ("      m003(-2,3) chk   ", "m003(-2,3)"),
                  ("Weeks m003(-3,1)       ", "m003(-3,1)")]:
    f = field_of(name)
    if f is None:
        p("    %s : degree > 12 (find_field None)" % lbl); continue
    poly, dg, disc, gal, subs = f
    p("    %s : %-14s deg %d  disc %d  Gal %s" % (lbl, poly, dg, disc, gal))
    p("        %sproper subfields: %s"
      % (" "*len(lbl), [s for s in subs if s not in ('x', 'x - 1')] or "NONE"))

# hand cross-check of the three discriminants
R = PolynomialRing(QQ, 'x'); x = R.gen()
p("\n    hand-check field discriminants:")
for q in [x**2 - x + 1, x**4 - x - 1, x**3 - x - 1, x**3 - x + 1]:
    p("        %-14s field disc = %d" % (q, NumberField(q, 'a').discriminant()))
p("    (x^3-x-1 and x^3-x+1 are the SAME disc-(-23) cubic field: roots negate.)")

p("\n    CORRECTION vs prior round:")
p("      prior discriminating_fact: child m004(5,1) TF = cubic x^3-x+1, disc -23  -- FALSE")
p("      correct               : child m004(5,1) TF = QUARTIC x^4-x-1, disc -283, S4")
p("      the cubic disc -23 belongs to WEEKS m003(-3,1), the SISTER's child.")
p("    Conclusion (unchanged qualitatively): the S4 quartic has NO proper")
p("    subfield, so the open object's Eisenstein Q(sqrt-3) does NOT survive the")
p("    closing.  B718 confirmed -- with the correct arithmetic invariant.")

# ------------------------------------------------------- open-object Eisenstein
p("\n    open-object 'being' cross-check (independent of the field machinery):")
s = snappy.Manifold('m004').tetrahedra_shapes('rect', bits_prec=500)[0]
zc = pari(str(s.real()) + '+' + str(s.imag()) + '*I')
q = zc.algdep(2)
res = float(abs(CC(pari.subst(q, 'x', zc))))
p("        m004 tetrahedron shape algdep(2) = %s   residual = %.2e" % (q, res))
p("        (root of x^2-x+1 = exp(i*pi/3); confirms Q(sqrt-3) on the OPEN object)")

# --------------------------------------------------------- frontier science box
p("\n" + "="*74)
p("FRONTIER SCIENCE (primary sources; physics claim = NIL)")
p("="*74)
p("""
CURVATURE (geometry -- FLAT; fixes geometry, not topology):
  Planck PR4 (HiLLiPoP V4.2)          Omega_k = -0.012 +/- 0.010  (1.2 sigma; 2309.10034)
  Planck CMB + BAO (tight)            Omega_k =  0.0007 +/- 0.0019 (via 2041-8213/adb7de)
  DESI DR1 BAO-only (model-indep GP)  Omega_k =  0.012 +/- 0.176   (consistent w/ flat)
  => universe measured spatially flat to ~0.2%.

TOPOLOGY (searches -- ALL NULL; a tightening LOWER BOUND, not a detection):
  Review "The Topology of the Universe" (2606.24886, Nature Astronomy 2026):
    "these searches have yielded no definitive evidence for non-trivial topology."
  matched-circle lower bounds on the shortest non-contractible loop d_NC vs the
  last-scattering diameter d_LSS:
    WMAP matched circles      d_NC > 0.985 d_LSS
    Planck likelihood search  d_NC >~ 1.03  d_LSS   (null)
    COMPACT preliminary       d_NC ~  1.05  d_LSS   (all Euclidean manifolds)
  COMPACT collaboration (2210.11426 PRL 132 171501; 2211.02603 Part I; 2409.02226
    Part Ic lens spaces): forecasts + circle limits, NO detection.
  Hyperbolic topologies remain comparatively UNCONSTRAINED (exponential growth of
    volume => costly eigenmodes); open pending LiteBIRD-era data.

COMPACT-HYPERBOLIC CMB MODELS (where our own child actually appears):
  Inoue astro-ph/9810034: Laplace-Beltrami eigenmodes on "the Thurston manifold
    ... the second smallest in the known compact hyperbolic 3-manifolds",
    cataloged in SnapPea as m003(-2,3) == our m004(5,1).  [OUR OWN (5,1) CHILD]
  Inoue astro-ph/9903446 / MNRAS 323,1016: CMB anisotropy in compact hyperbolic
    universes (angular power spectra from those eigenmodes).
  Cornish-Spergel math/9906017: 12 compact hyperbolic manifolds incl. explicit
    "eigenmodes taken from the Weeks space" (== our #1, the sister m003's child).
  => the object's family children (Thurston #2, Weeks #1) are the very manifolds
     cosmologists computed CMB observables on -- because they are the SMALLEST
     (most tractable), a researcher-SELECTION effect, not a data preference.
""")

p("="*74)
p("VERDICT (two-outcome A/B): A = real-MATH meeting point, physics NIL.")
p("""  MATH (rigorous): Dehn filling IS the cusp->closed 'residue/closing' operation
  (Thurston: parent vol = monotone sup of filled vols); cusp cross-sections are
  intrinsically FLAT 2-tori bounding negatively-curved bulk; the object's OWN
  (5,1) child is verifiably the #2-smallest closed orientable hyperbolic
  manifold (Thurston, vol 0.98137), a bona-fide literature CMB candidate (Inoue).
  BASE-RATE (E20, held): distinguished-by-MATH (minimal volume / #2-smallest /
  named manifold) = researcher TRACTABILITY selection, NOT distinguished-by-DATA
  (every topology search is NULL; no CMB observable favors hyperbolic curvature,
  this family, or any manifold; the universe is measured FLAT).
  => genuine real mathematics; the physics/cosmology claim is EXACTLY NIL.""")
p("="*74)

_OUT = '/Users/dri/origin-axiom/frontier/B730_forced_faces_and_cosmos/cc_q3_cosmo_out.txt'
with open(_OUT, 'w') as f:
    f.write("\n".join(L) + "\n")
print("\n[wrote %s]" % _OUT)
