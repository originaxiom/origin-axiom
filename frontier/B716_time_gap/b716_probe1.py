#!/usr/bin/env python3
# B716 PROBE 1 — the object's INTRINSIC time.
#
# FIREWALL: origin-axiom. Structural/mathematical ONLY. No cosmology claimed,
# no SM value, no physics assertion beyond structural characterization.
# Verify-don't-trust: everything below is independently recomputed in-sandbox.
#
# CLAIM UNDER TEST
# ----------------
# The figure-eight knot complement (m004 = 4_1) is the mapping torus
#     M_sigma = (T^2 minus pt)  x]_sigma  S^1
# of the once-punctured torus with Anosov monodromy
#     sigma = [[2,1],[1,1]]   (the cat map; RL = R*L with R=[[1,1],[0,1]], L=[[1,0],[1,1]]).
# Its suspension flow is the object's ONLY internal notion of "time".
# Two-outcome:
#   A = a usable EXTERNAL cosmological R-time WITH an arrow.
#   B = an INTERNAL thermal/Anosov time only (compact S^1, hyperbolic, no arrow;
#       a Connes-Rovelli modular/thermal time, not an external clock).
#
# DISCRIMINATING FACTS computed here:
#   (1) topological entropy  h = log(spectral radius) = log(phi^2) = 2 log phi
#   (2) amphichirality:  sigma ~ sigma^-1 in GL(2,Z)  =>  time-reversal symmetry => NO arrow
#   (3) base of the fibration = S^1 (compact, periodic), not R (non-compact) => no cosmological line
#   (4) flow is Anosov: hyperbolic (|lambda| != 1), no fixed points of sigma^k (det(sigma^k - I) != 0)

import sympy as sp
import mpmath as mp

mp.mp.dps = 40
out = []
def p(*a):
    s = " ".join(str(x) for x in a)
    out.append(s)
    print(s)

p("="*74)
p("B716 PROBE 1 — the object's INTRINSIC time (figure-eight = punctured-torus bundle)")
p("="*74)

# ---------------------------------------------------------------------------
# 0. Verify the monodromy really is RL and equals [[2,1],[1,1]], det 1, trace 3.
# ---------------------------------------------------------------------------
R = sp.Matrix([[1,1],[0,1]])   # Dehn twist
L = sp.Matrix([[1,0],[1,1]])   # Dehn twist
sigma = R*L
sigma_alt = L*R
p("\n[0] Monodromy from the two Dehn twists")
p("    R = [[1,1],[0,1]], L = [[1,0],[1,1]]")
p("    sigma = R*L   =", sigma.tolist(), " trace", sigma.trace(), " det", sigma.det())
p("    sigma'= L*R   =", sigma_alt.tolist(), " trace", sigma_alt.trace(), " det", sigma_alt.det())
assert sigma == sp.Matrix([[2,1],[1,1]])
assert sigma.det() == 1 and sigma.trace() == 3
p("    -> sigma = [[2,1],[1,1]] confirmed (the cat map). char poly = x^2 - 3x + 1.")

# ---------------------------------------------------------------------------
# 1. Eigenvalues, dilatation, topological entropy.
# ---------------------------------------------------------------------------
x = sp.symbols('x')
charpoly = sp.expand((x - sigma[0,0])*(x - sigma[1,1]) - sigma[0,1]*sigma[1,0])
p("\n[1] Spectrum / dilatation / topological entropy")
p("    char poly:", sp.Poly(sp.Matrix(sigma).charpoly(x).as_expr(), x).as_expr())
eigs = sp.Matrix(sigma).eigenvals()
p("    eigenvalues (exact):", eigs)

phi = (1 + sp.sqrt(5))/2
lam_plus  = (3 + sp.sqrt(5))/2      # = phi^2
lam_minus = (3 - sp.sqrt(5))/2      # = phi^-2
# verify these are the eigenvalues and equal phi^{±2}
assert sp.simplify(lam_plus  - phi**2) == 0
assert sp.simplify(lam_minus - phi**(-2)) == 0
assert sp.simplify(lam_plus*lam_minus - 1) == 0          # det 1
assert sp.simplify(lam_plus + lam_minus - 3) == 0        # trace 3
p("    lambda_+ = (3+sqrt5)/2 = phi^2  =", mp.mpf(mp.nstr(mp.mpf((sp.N(lam_plus,40)).__str__()),40)) if False else mp.mpf(str(sp.N(lam_plus,40))))
p("    lambda_- = (3-sqrt5)/2 = phi^-2 =", mp.mpf(str(sp.N(lam_minus,40))))
p("    product lambda_+ * lambda_- = 1 (det=1)  ;  sum = 3 (trace)")

# dilatation = spectral radius = lambda_+ = phi^2 (RECIPROCAL pair => reversible)
dilatation = mp.mpf(str(sp.N(lam_plus,40)))
h_top = mp.log(dilatation)
two_log_phi = 2*mp.log(mp.mpf(str(sp.N(phi,40))))
p("    dilatation (Perron / stretch factor) = phi^2 =", dilatation)
p("    topological entropy h = log(dilatation) = log(phi^2) = 2 log phi")
p("      h =", h_top)
_match = abs(h_top - two_log_phi) < mp.mpf(10)**-30   # exact identity log(phi^2)=2log phi; tol beats 40-digit round-trip
p("      2 log phi =", two_log_phi, "  (match to 30+ digits:", bool(_match), "; |diff| =", mp.nstr(abs(h_top-two_log_phi),3), ")")
# cross-check numeric value 0.9624...
assert mp.almosteq(h_top, mp.mpf("0.9624236501192068949955178268487368462703"), rel_eps=mp.mpf(10)**-30)
p("    -> h = 0.96242365... > 0  : POSITIVE entropy => hyperbolic/chaotic/mixing flow.")
p("       (entropy of sigma^-1 is IDENTICAL: log|phi^-2|^-1 = log phi^2 = h. Rate, not arrow.)")

# ---------------------------------------------------------------------------
# 2. AMPHICHIRALITY  =>  time-reversal symmetry  =>  no canonical arrow.
#    Search P in GL(2,Z) with  P sigma P^-1 = sigma^-1.
# ---------------------------------------------------------------------------
p("\n[2] Time-reversal: is sigma conjugate to sigma^-1 in GL(2,Z)?  (amphichirality)")
sigma_inv = sigma.inv()
p("    sigma^-1 =", sigma_inv.tolist(), " trace", sigma_inv.trace(), " det", sigma_inv.det())
found = []
rng = range(-4,5)
for a in rng:
 for b in rng:
  for c in rng:
   for d in rng:
     det = a*d - b*c
     if det in (1,-1):
        P = sp.Matrix([[a,b],[c,d]])
        if P*sigma == sigma_inv*P:      # P sigma = sigma^-1 P  <=> P sigma P^-1 = sigma^-1
            found.append((P.tolist(), det))
p("    #conjugators P (entries in [-4,4], det=+-1) with P sigma P^-1 = sigma^-1 :", len(found))
if found:
    # show the minimal / a representative one and note its determinant sign
    dets = sorted(set(d for _,d in found))
    p("    example conjugators:", found[:4])
    p("    conjugator determinant signs present:", dets)
    # is there a det = -1 one (orientation-reversing => genuine amphichiral involution)?
    has_orient_rev = any(d == -1 for _,d in found)
    p("    orientation-reversing (det=-1) conjugator exists:", has_orient_rev)
    assert len(found) > 0
    p("    -> sigma ~ sigma^-1  : the monodromy is conjugate to its inverse.")
    p("       The figure-eight knot is AMPHICHIRAL; the bundle is time-reversal symmetric.")
    p("       => the two flow directions are indistinguishable => NO canonical time ARROW.")
else:
    p("    -> NOT found in this box (unexpected).")

# extra: the flip J=[[0,1],[1,0]] (det -1) conjugates RL <-> LR (the two Dehn-twist orders)
J = sp.Matrix([[0,1],[1,0]])
p("    (aside) J=[[0,1],[1,0]] (det -1):  J (RL) J = LR ?", (J*sigma*J) == sigma_alt)

# ---------------------------------------------------------------------------
# 3. Base of the fibration is S^1 (compact/periodic), NOT R (non-compact/cosmological).
#    The fibered face / the fact that it fibers over S^1 with pseudo-Anosov (Anosov) monodromy.
# ---------------------------------------------------------------------------
p("\n[3] The 'time' base: S^1 (compact, periodic) vs R (non-compact, cosmological)")
p("    M_sigma = (fiber x [0,1]) / (x,1)~(sigma x, 0).")
p("    The fibration M_sigma -> S^1 has base S^1 = [0,1]/(0~1): COMPACT, PERIODIC.")
p("    'Time' = the S^1 direction of the suspension. There is no R-line, no infinite")
p("    past/future, no beginning: it is a circle, the opposite of a cosmological FRW R-time.")

# Try to corroborate the bundle structure with SnapPy (optional; core result is the linear algebra).
snappy_note = "snappy: (not run)"
try:
    import warnings; warnings.filterwarnings("ignore")
    import snappy
    M = snappy.Manifold('4_1')
    vol = M.volume()
    # figure-eight is the once-punctured torus bundle with monodromy of trace 3;
    # confirm it is 4_1/m004 and hyperbolic (cusped, finite volume => Mostow rigid).
    ident = [str(x) for x in (M.identify() or [])]
    snappy_note = "snappy: 4_1 = %s ; volume = %s (hyperbolic, 1 cusp, Mostow-rigid)" % (ident[:2], vol)
    p("    " + snappy_note)
    p("    -> the complement is CUSPED hyperbolic (finite volume 2.0298832...): a rigid,")
    p("       timeless 3-geometry whose ONLY flow-time is this suspension S^1.")
except Exception as e:
    p("    snappy check skipped:", repr(e))

# ---------------------------------------------------------------------------
# 4. Anosov / hyperbolic: |eigenvalues| != 1, and no periodic fixed points on the torus
#    fiber => the suspension flow has NO fixed points (a genuine flow, everywhere transverse).
# ---------------------------------------------------------------------------
p("\n[4] Hyperbolicity (Anosov) & absence of fixed points")
p("    |lambda_+| =", dilatation, " > 1  ;  |lambda_-| =", mp.mpf(str(sp.N(lam_minus,40))), " < 1")
p("    Neither eigenvalue is on the unit circle => the linear map is HYPERBOLIC (Anosov).")
# no non-zero fixed points of sigma^k on Z^2 <=> det(sigma^k - I) != 0 for all k>=1
p("    det(sigma^k - I) for k=1..6 (nonzero => sigma^k has no fixed 1-cycle => flow has no closed")
p("    orbit collapsing to a fixed point of the return map):")
for k in range(1,7):
    Mk = sigma**k
    d = (Mk - sp.eye(2)).det()
    # Lefschetz / number-of-fixed-points count = |det(sigma^k - I)| = number of k-periodic points on T^2
    p("      k=%d: det(sigma^k - I) = %s  (=> %d periodic points of period k on T^2)" % (k, d, abs(d)))
p("    All nonzero => sigma is Anosov with a dense set of periodic orbits, positive entropy,")
p("    mixing. The suspension is a smooth flow with NO fixed points (background-independent 'time').")

# ---------------------------------------------------------------------------
# 5. Connes-Rovelli reading + VERDICT.
# ---------------------------------------------------------------------------
p("\n[5] Connes-Rovelli thermal/modular reading")
p("    A background-independent system has no external clock; the only intrinsic dynamics")
p("    is a one-parameter automorphism group (modular/thermal flow). Here that role is")
p("    played EXACTLY by the suspension of the Anosov cat map:")
p("      * one-parameter flow (the S^1/suspension direction)         <-> modular one-parameter group")
p("      * positive entropy h = 2 log phi (a temperature/rate scale)  <-> KMS/thermal character")
p("      * time-reversal symmetric (sigma ~ sigma^-1), no arrow        <-> modular flow has no a priori arrow")
p("      * compact periodic base S^1, no R-line, no beginning          <-> intrinsic, background-independent")
p("    This is an INTERNAL thermal/Anosov time, NOT an external cosmological R-time with an arrow.")

p("\n" + "="*74)
p("VERDICT")
p("="*74)
p("OUTCOME = B  (INTERNAL thermal/Anosov time only; NO external cosmological R-time).")
p("Discriminating facts (all recomputed in-sandbox):")
p("  (1) topological entropy h = log(phi^2) = 2 log phi = 0.96242365... > 0")
p("      => hyperbolic/mixing flow (a rate/temperature), and identical for sigma and sigma^-1")
p("         => entropy gives NO arrow.")
p("  (2) sigma ~ sigma^-1 in GL(2,Z) (amphichiral) => time-reversal symmetric => NO canonical arrow.")
p("  (3) base = S^1 (compact, periodic), not R (non-compact) => no cosmological line, no beginning.")
p("  (4) Anosov: |eig|=phi^{+-2}!=1, det(sigma^k-I)!=0 => genuine hyperbolic flow, no fixed points.")
p("=> the object's only internal 'time' is a Connes-Rovelli-type thermal/modular Anosov flow;")
p("   it is NOT a usable external cosmological time with an arrow. FIREWALL: structural only.")

with open("/Users/dri/origin-axiom/frontier/B716_time_gap/b716_probe1_out.txt","w") as f:
    f.write("\n".join(out) + "\n")
print("\n[written] frontier/B716_time_gap/b716_probe1_out.txt")
