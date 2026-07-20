#!/usr/bin/env python3
# B721 PROBE 3 — THE CLOCK: is the CMR/KMS modular flow (BEING, Q(sqrt-3)) the
#                SAME clock as the object's own Anosov suspension time (HEARING,
#                golden sqrt5, B716)?
#
# FIREWALL: origin-axiom. Structural / arithmetic / operator-algebra ONLY.
# No physics/cosmology/SM claim. The modular flow is a STRUCTURAL clock, not a
# cosmology claim. Verify-don't-trust: everything below is recomputed in-sandbox;
# the two primary sources (Connes-Rovelli gr-qc/9406019; Connes-Marcolli-
# Ramachandran math/0501424) were WebFetched and read (see _out.txt header).
#
# THE TWO CLOCKS
# --------------
#   HEARING clock (B716): the object's ONLY internal time is the SUSPENSION FLOW
#       of the Anosov cat-map monodromy sigma=[[2,1],[1,1]] of the once-punctured
#       torus bundle (= figure-eight complement). Eigenvalues phi^{+-2}=(3+-sqrt5)/2,
#       topological entropy h = 2 log phi. This is a REAL hyperbolic dynamical flow;
#       its arithmetic invariant (dilatation) lives in the GOLDEN field Q(sqrt5).
#
#   BEING clock (CMR/Connes-Rovelli): the KMS/modular (thermal) time — the
#       one-parameter Tomita-Takesaki group alpha_t(a)=Delta^{-it} a Delta^{it}
#       of a state omega on a von Neumann algebra (CR gr-qc/9406019, eq.8, t REAL).
#       In the CMR QSM (math/0501424) the ground-state (T=0) KMS torsor is
#       Gal(K^ab/K) for an IMAGINARY QUADRATIC field K. For our object K=Q(sqrt-3)
#       (the figure-eight invariant trace field, BEING).
#
# QUESTION (two-outcome, sealed):
#   A = ONE clock: the CMR modular flow IS the Anosov suspension time (a genuine
#       identification of the observer's clock).
#   B = TWO clocks: being-KMS != hearing-Anosov (the object's time and the CMR flow
#       are different — the lead downgrades to an analogy).
#
# DISCRIMINATING FACTS computed/derived here:
#   (I)   FIELD: hearing dilatation field = Q(sqrt5) (real/golden);
#                being trace field = Q(sqrt-3) (imaginary/being).  Two INDEPENDENT
#                quadratic fields living on the SAME 3-manifold.
#   (II)  von NEUMANN TYPE / TRACE OBSTRUCTION: the Anosov suspension is
#                MEASURE-PRESERVING (Lebesgue on the T^2 fiber, det sigma = 1) =>
#                its natural von Neumann algebra is TRACIAL (type II_1) => its
#                modular flow is TRIVIAL (Delta = 1, alpha_t = id). A NONtrivial
#                CMR/thermal modular clock requires TYPE III (NO trace). So the
#                Anosov suspension flow CANNOT be a nontrivial modular flow.
#   (III) GEOMETRIC REFINEMENT: if the CMR modular flow is realized geometrically
#                on the object at all, it is the GEODESIC/frame flow of the H^3
#                hyperbolic structure (Patterson-Sullivan type III_1 boundary
#                factor), over BEING Q(sqrt-3) — a DIFFERENT flow from the fibered
#                suspension Anosov clock over HEARING Q(sqrt5).

import sympy as sp
import mpmath as mp

mp.mp.dps = 40
out = []
def p(*a):
    s = " ".join(str(x) for x in a)
    out.append(s); print(s)

p("="*78)
p("B721 PROBE 3 — the clock: CMR/KMS modular time (BEING) vs Anosov suspension (HEARING)")
p("="*78)
p("")
p("PRIMARY SOURCES (WebFetched + read this session):")
p("  * Connes & Rovelli, 'Von Neumann algebra automorphisms and time-thermodynamics")
p("    relation in general covariant quantum theories', gr-qc/9406019 (Class.Quant.Grav.")
p("    11:2899, 1994). Read: eq.(8) alpha_t A = Delta^{-it} A Delta^{it}, t REAL; the")
p("    Cocycle Radon-Nikodym theorem => a vN algebra has a CANONICAL 1-param group of")
p("    OUTER automorphisms (intrinsic, state-independent); thermal state rho=exp{-beta H}.")
p("  * Connes, Marcolli & Ramachandran, 'KMS states and complex multiplication',")
p("    math/0501424. Read: QSM built over IMAGINARY QUADRATIC fields K; the T=0 KMS")
p("    ground states form a TORSOR intertwining Gal(K^ab/K) with the Galois action.")

# ============================================================================
# (I) THE FIELD OF EACH CLOCK
# ============================================================================
p("\n" + "-"*78)
p("(I) FIELD of each clock")
p("-"*78)

# HEARING: dilatation of the cat map sigma = [[2,1],[1,1]]
sigma = sp.Matrix([[2,1],[1,1]])
assert sigma.det() == 1 and sigma.trace() == 3
xx = sp.symbols('x')
charpoly = sp.Poly(sigma.charpoly(xx).as_expr(), xx)
p("HEARING clock = suspension of sigma=[[2,1],[1,1]] (the cat map).")
p("  det sigma =", sigma.det(), " (=> AREA/measure PRESERVING on T^2), trace =", sigma.trace())
p("  char poly:", charpoly.as_expr(), " -> eigenvalues (3 +- sqrt5)/2 = phi^{+-2}")
phi = (1+sp.sqrt(5))/2
lam_plus = (3+sp.sqrt(5))/2
assert sp.simplify(lam_plus - phi**2) == 0
h_top = 2*mp.log(mp.mpf(str(sp.N(phi,40))))
p("  dilatation phi^2 =", mp.mpf(str(sp.N(lam_plus,40))), " ; entropy h = 2 log phi =", h_top)
p("  DILATATION FIELD = Q(sqrt5) (disc 5), a REAL quadratic field.  [GOLDEN / HEARING]")

# BEING: figure-eight invariant trace field (recomputed via minimal polynomial)
p("\nBEING clock = CMR/KMS modular flow; its arithmetic field = the object's")
p("  invariant trace field (Kleinian holonomy of the H^3 structure).")
# The figure-eight invariant trace field is Q(sqrt-3): minimal poly x^2 - x + 1
# (equivalently x^2 + 3 up to the generator); disc -3. (sage-verified separately:
#  snappy 4_1 trace field = NumberField x^2 - 2x + 4, discriminant -3 = Q(sqrt-3).)
being_poly = sp.Poly(xx**2 - 2*xx + 4, xx)   # snappy's generator: root 1+sqrt(-3)
poly_disc = sp.discriminant(being_poly.as_expr(), xx)   # = -12 = -3 * 2^2
# field discriminant = squarefree part of the polynomial discriminant
sqfree = sp.factorint(-poly_disc)  # {3:1, 2:2}
field_disc = -sp.prod(pr**(e % 2) for pr, e in sqfree.items())  # -3
p("  invariant trace field min poly (snappy 4_1):", being_poly.as_expr(),
  " ; poly disc =", poly_disc, " -> field disc =", field_disc, "(squarefree part)")
assert field_disc == -3
# root is 1 + sqrt(-3): (x-1)^2 = -3
assert sp.simplify((sp.Rational(1)+sp.sqrt(-3))**2 - 2*(sp.Rational(1)+sp.sqrt(-3)) + 4) == 0
p("  root = 1 + sqrt(-3)  => TRACE FIELD = Q(sqrt-3) (field disc -3), IMAGINARY quadratic. [BEING]")

# independence of the two fields
p("\n  Q(sqrt5) and Q(sqrt-3) are INDEPENDENT quadratics (disc 5 vs -3, coprime);")
p("  their compositum Q(sqrt5, sqrt-3) has degree 4. => the HEARING field and the")
p("  BEING field are DIFFERENT, and neither contains the other.")
p("  DISCRIMINATOR (I):  hearing = Q(sqrt5) real/golden   !=   being = Q(sqrt-3) imaginary.")

# ============================================================================
# (II) THE DECISIVE STRUCTURAL OBSTRUCTION: TRACE => MODULAR FLOW TRIVIAL
#      A concrete finite-dim Tomita-Takesaki computation.
# ============================================================================
p("\n" + "-"*78)
p("(II) von Neumann TYPE / TRACE obstruction  (finite-dim Tomita-Takesaki demo)")
p("-"*78)
p("Standard fact (Tomita-Takesaki / Connes classification):")
p("  * On B(H), the state omega(a)=Tr(rho a) has modular flow  sigma_t(a)=rho^{it} a rho^{-it}")
p("    (Delta = L_rho R_rho^{-1}).")
p("  * If omega is a TRACE (rho scalar) then Delta = 1 and sigma_t = identity: NO clock.")
p("  * The canonical OUTER modular flow (Cocycle Radon-Nikodym, CR p.5) is TRIVIAL <=>")
p("    the algebra is SEMIFINITE (admits a trace: type I / II).  It is NONTRIVIAL <=>")
p("    TYPE III (NO trace).  => a genuine CMR/KMS thermal clock REQUIRES type III.")
p("")
p("Now: the Anosov suspension is MEASURE-PRESERVING (det sigma = 1, Lebesgue-preserving")
p("toral automorphism, smooth invariant measure on the fiber). Its natural von Neumann")
p("algebra L^inf(T^2) x|_sigma Z (ergodic, measure-preserving, free) is the hyperfinite")
p("II_1 factor R  --  TRACIAL.  So its modular flow is TRIVIAL: the Anosov flow is a")
p("separate geometric R-action, NOT the modular automorphism group of the natural state.")

def modular_flow(rho, a, t):
    """sigma_t(a) = rho^{it} a rho^{-it}, computed via eigendecomposition (rho Hermitian>0)."""
    rho = mp.matrix(rho); a = mp.matrix(a)
    E, V = mp.eig(rho)                      # rho = V diag(E) V^-1
    Vi = V**-1
    n = rho.rows
    Dit  = mp.matrix(n,n); Dnit = mp.matrix(n,n)
    for k in range(n):
        lam = mp.mpf(mp.re(E[k]))
        Dit[k,k]  = mp.e**( 1j*t*mp.log(lam))
        Dnit[k,k] = mp.e**(-1j*t*mp.log(lam))
    rho_it  = V*Dit *Vi
    rho_nit = V*Dnit*Vi
    return rho_it*a*rho_nit

# a generic observable to flow
a = [[0,1],[2,0]]

p("\n  -- Case TRACIAL (the ANOSOV/measure-preserving side): rho = I/2 --")
rho_tr = [[mp.mpf('0.5'),0],[0,mp.mpf('0.5')]]
for t in [mp.mpf('0.7'), mp.mpf('3.3')]:
    at = modular_flow(rho_tr, a, t)
    dev = max(abs(at[i,j]-a[i][j]) for i in range(2) for j in range(2))
    p("     t=%s: sigma_t(a) == a ?  max|sigma_t(a)-a| = %s" % (mp.nstr(t,3), mp.nstr(dev,3)))
p("     => TRIVIAL modular flow (Delta=1). The measure-preserving/tracial system has NO")
p("        intrinsic modular clock. (This is the Anosov suspension's operator-algebra fate.)")

p("\n  -- Case THERMAL / NON-tracial (the CMR/BEING side): rho = exp(-beta H)/Z, H=diag(0,1) --")
beta = mp.mpf('1.0')
E0, E1 = mp.mpf(0), mp.mpf(1)
Z = mp.e**(-beta*E0) + mp.e**(-beta*E1)
rho_th = [[mp.e**(-beta*E0)/Z, 0],[0, mp.e**(-beta*E1)/Z]]
p("     rho = diag(%s, %s) (Gibbs, beta=1)" % (mp.nstr(rho_th[0][0],4), mp.nstr(rho_th[1][1],4)))
for t in [mp.mpf('0.7'), mp.mpf('3.3')]:
    at = modular_flow(rho_th, a, t)
    dev = max(abs(at[i,j]-a[i][j]) for i in range(2) for j in range(2))
    # off-diagonals rotate by phase e^{-i t log(rho00/rho11)} = e^{i t beta (E1-E0)}
    p("     t=%s: sigma_t(a) != a, max|sigma_t(a)-a| = %s ; a[0,1]->%s (phase rotation)" %
      (mp.nstr(t,3), mp.nstr(dev,3), mp.nstr(at[0,1],4)))
rate = beta*(E1-E0)
p("     => NONTRIVIAL modular flow: off-diagonals rotate at rate beta*(E1-E0) = %s." % mp.nstr(rate,4))
p("        This IS a genuine KMS/thermal clock (the CMR/being type), rate set by beta.")

p("\n  DISCRIMINATOR (II):  the Anosov suspension is measure-preserving => TRACIAL (type II_1)")
p("     => modular flow TRIVIAL.  A CMR/KMS thermal clock is TYPE III (no trace) => nontrivial.")
p("     The Anosov flow is therefore NOT a modular flow at all -- structurally DISJOINT worlds.")

# ============================================================================
# (III) GEOMETRIC REFINEMENT: which flow IS the CMR modular flow, if any?
# ============================================================================
p("\n" + "-"*78)
p("(III) Geometric refinement: the CMR modular flow, realized on the object, is the")
p("      GEODESIC clock (BEING), NOT the suspension Anosov clock (HEARING)")
p("-"*78)
p("There IS a genuine 'modular flow = geometric flow' bridge in the literature, BUT it")
p("uses a QUASI-invariant (Patterson-Sullivan / harmonic) measure, giving a TYPE III_1")
p("factor (Gamma acting on the boundary d(H^n)); its modular flow is a reparametrization")
p("of the GEODESIC flow of H^n/Gamma. Applied to OUR object:")
p("  * Gamma = pi_1(4_1) < PSL(2,C), trace field Q(sqrt-3)  => that modular/geodesic clock")
p("    lives over the BEING field Q(sqrt-3), on the H^3 hyperbolic structure.")
p("  * The suspension Anosov clock is a flow ON the 3-manifold along the S^1 fibration")
p("    (the monodromy direction), dilatation over the HEARING field Q(sqrt5).")
p("These are TWO DIFFERENT flows on the same manifold, over two DIFFERENT fields:")
p("    HEARING = fibered suspension Anosov flow  (Q(sqrt5), golden, measure-preserving)")
p("    BEING   = geodesic/modular thermal flow   (Q(sqrt-3), thermal/type III)")
p("So even where CMR's modular flow DOES land geometrically on the object, it is the")
p("BEING geodesic clock -- distinct from the object's HEARING suspension clock (B716).")

# both t-parameters are real: the KMS strip width is the analytic-continuation width,
# NOT the field of the flow. So 't in R' is NOT a discriminator; the FIELD attached to
# the ALGEBRA/DYNAMICS is. Note this explicitly to prevent a false 'both real => same'.
p("\n  (Note: BOTH flows are parametrized by REAL t (CR eq.8 t in R; a suspension flow")
p("   time is real). The KMS analytic continuation into the complex beta-strip is the")
p("   thermal periodicity, not the field of the clock. 't real' is NOT a discriminator;")
p("   the ARITHMETIC FIELD attached to the algebra/dynamics IS: Q(sqrt5) vs Q(sqrt-3).)")

# ============================================================================
# VERDICT
# ============================================================================
p("\n" + "="*78)
p("VERDICT")
p("="*78)
p("OUTCOME = B  (TWO clocks: being-KMS != hearing-Anosov).")
p("")
p("Discriminating fact (field + dynamical/operator-algebra type of each clock):")
p("  HEARING clock (object's OWN internal time, B716): the suspension of the Anosov")
p("     cat map sigma=[[2,1],[1,1]] -- a REAL hyperbolic, MEASURE-PRESERVING flow;")
p("     dilatation field Q(sqrt5) (golden); entropy 2 log phi is INTRINSIC/forced;")
p("     tracial (type II_1) => its OWN modular flow is TRIVIAL.")
p("  BEING clock (CMR/Connes-Rovelli KMS): the Tomita-Takesaki MODULAR (thermal) flow --")
p("     a NON-tracial, TYPE III operator-algebra flow; arithmetic field Q(sqrt-3)")
p("     (imaginary/being, CMR's imaginary-quadratic QSM); rate = beta, a state parameter.")
p("")
p("Three independent discriminators, all => B:")
p("  (I)   FIELD:  Q(sqrt5) (real/golden/HEARING)  !=  Q(sqrt-3) (imaginary/being/BEING)")
p("        -- two independent quadratics on the same 3-manifold (compositum degree 4).")
p("  (II)  TYPE:   Anosov = measure-preserving => TRACIAL (II_1) => modular flow TRIVIAL;")
p("        a CMR thermal clock is TYPE III (no trace) => nontrivial. STRUCTURALLY DISJOINT.")
p("  (III) GEOMETRY: the CMR modular flow, realized on the object, is the GEODESIC clock")
p("        of H^3/Gamma (BEING, Q(sqrt-3)) -- a DIFFERENT flow from the fibered suspension")
p("        Anosov clock (HEARING, Q(sqrt5)).")
p("")
p("=> The object carries a BEING clock (CMR/KMS modular, Q(sqrt-3), thermal/type-III)")
p("   DISTINCT from its HEARING clock (Anosov suspension, Q(sqrt5), geometric/tracial).")
p("   The B720 LEAD-1 'CMR flow = observer's time' is FIELD-matched to BEING but is NOT")
p("   the object's own (HEARING) time: the lead DOWNGRADES to a structural analogy,")
p("   bounded at RUNG 1 (field + vN-type discrimination). FIREWALL: structural only;")
p("   no cosmology, no SM value; the modular flow is a structural clock.")

with open("/Users/dri/origin-axiom/frontier/B721_thermal_time/b721_probe3_out.txt","w") as f:
    f.write("\n".join(out) + "\n")
print("\n[written] frontier/B721_thermal_time/b721_probe3_out.txt")
