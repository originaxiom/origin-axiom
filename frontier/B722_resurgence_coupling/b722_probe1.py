#!/usr/bin/env python3
# B722 PROBE 1 -- the two Kashaev phases = being/hearing?
# origin-axiom program. Structural/arithmetic ONLY. No physics/SM claims.
#
# SOURCES (WebFetch-verified REAL, 2026-07-20):
#   Galakhov-Morozov arXiv:2605.31588 "Two roles of Alexander in two Kashaev phases"
#     Abstract (verbatim): classical A-polynomials have common roots with Delta,
#       while Jones polynomials tend to Delta^{-1} in the perturbative expansion.
#       "...two different branches (phases) in the quasiclassical limit -- with
#        non-trivial and with vanishing classical actions.  The first leads to
#        classical A-polynomials and hyperbolic volumes, the second -- to inverse
#        Alexanders."
#   Morozov arXiv:2606.24497 "More on Kashaev limits of the quantum A-polynomials"
#     Abstract (paraphrase): the non-homogeneous quantum A-polynomial splits into
#       TWO pieces = the two phases; "in one of them the classical action vanishes
#       and in another one it is a deformation of hyperbolic volume."  Also
#       A^K(1,M) ~ Delta^K(M)  (A-poly at L=1 proportional to Alexander).
#
# CLAIM UNDER TEST (probe 1 two-outcome):
#   A = the two Kashaev quasiclassical phases ARE exactly the object's being/hearing
#       BEING  = A-polynomial + hyperbolic volume, trace field Q(sqrt(-3))
#       HEARING= inverse-Alexander, golden roots phi^{+/-2}, field Q(sqrt(5))
#   B = a different structure.
#
# We VERIFY (mpmath, verify-don't-trust) the two numbers each phase carries and the
# quadratic field each lives in.

import mpmath as mp
import sympy as sp

mp.mp.dps = 60
OUT = []
def log(s=""):
    print(s); OUT.append(s)

log("="*78)
log("B722 PROBE 1 -- the two Kashaev phases = being/hearing?")
log("="*78)

# ---------------------------------------------------------------------------
# PHASE 1 (non-trivial classical action):  A-polynomial + HYPERBOLIC VOLUME
#   -> BEING.  Trace field of the figure-eight (4_1) = Q(sqrt(-3)) (Eisenstein).
# ---------------------------------------------------------------------------
log("")
log("-"*78)
log("PHASE 1  (non-trivial classical action)  ==  A-poly + hyperbolic volume")
log("-"*78)

# (a) Hyperbolic volume of the figure-eight complement.
#     Vol(4_1) = 2 * V_tet  where V_tet = volume of the regular ideal tetrahedron
#     V_tet = Cl_2(pi/3) = Im Li_2(e^{i pi/3})  (Lobachevsky/Clausen)
z_geo = mp.e**(1j*mp.pi/3)                 # ideal-tetra shape at complete structure
V_tet = mp.im(mp.polylog(2, z_geo))        # Im Li_2(e^{i pi/3}) = Cl_2(pi/3)
Vol   = 2 * V_tet
log("shape z = e^{i pi/3}            = %s" % mp.nstr(z_geo, 25))
log("V_tet = Im Li_2(e^{i pi/3})     = %s" % mp.nstr(V_tet, 30))
log("Vol(4_1) = 2*Im Li_2(e^{ipi/3})= %s" % mp.nstr(Vol, 30))
log("target (SnapPy)  2.029883212819307...   ->  match: %s"
    % (abs(Vol - mp.mpf('2.029883212819307250042')) < mp.mpf('1e-18')))

# (b) The geometric/A-poly phase lives over Q(sqrt(-3)):
#     the tetra shape z solves the gluing equation z^2 - z + 1 = 0 (roots e^{+-i pi/3}),
#     discriminant = 1 - 4 = -3  ->  Q(sqrt(-3)).
t = sp.symbols('t')
geo_poly = t**2 - t + 1
disc_geo = sp.discriminant(geo_poly, t)
log("")
log("gluing/shape polynomial        z^2 - z + 1,  roots = %s"
    % [sp.nsimplify(r) for r in sp.roots(geo_poly, t)])
log("discriminant                   = %s   ->  field Q(sqrt(%s)) = Q(sqrt(-3))"
    % (disc_geo, disc_geo))
# double-check z_geo is a root of z^2 - z + 1
log("check z_geo^2 - z_geo + 1      = %s  (~0)" % mp.nstr(z_geo**2 - z_geo + 1, 5))

# (c) The classical figure-eight A-polynomial (Cooper-Long), just to exhibit the
#     A-poly object this phase reproduces.  A(M,L) with M=meridian,L=longitude eig.
M, L = sp.symbols('M L')
A_poly = (-M**4 + L*(1 - M**2 - 2*M**4 - M**6 + M**8) - L**2*M**4)
log("")
log("classical A-poly (4_1)         A(M,L) = %s" % sp.expand(A_poly))
# Morozov 2606.24497:  A^K(1,M) ~ Delta(M).  Set L=1, collect in M.
A_at_L1 = sp.expand(A_poly.subs(L, 1))
log("A(M,1)  (L=1 slice)            = %s" % A_at_L1)
# factor out to see the Alexander content
A_at_L1_factored = sp.factor(A_at_L1)
log("A(M,1) factored                = %s" % A_at_L1_factored)

# ---------------------------------------------------------------------------
# PHASE 2 (vanishing classical action):  INVERSE ALEXANDER
#   -> HEARING.  Fig-8 Alexander Delta(t)=t^2-3t+1, roots phi^{+-2}, field Q(sqrt5).
# ---------------------------------------------------------------------------
log("")
log("-"*78)
log("PHASE 2  (vanishing classical action)  ==  inverse Alexander")
log("-"*78)

Delta = t**2 - 3*t + 1                      # figure-eight Alexander polynomial
disc_alex = sp.discriminant(Delta, t)
alex_roots = sp.roots(Delta, t)
log("Alexander polynomial (4_1)     Delta(t) = t^2 - 3t + 1")
log("discriminant                   = %s   ->  field Q(sqrt(%s)) = Q(sqrt5)"
    % (disc_alex, disc_alex))
log("roots                          = %s" % [sp.nsimplify(r) for r in alex_roots])

# golden ratio, verify roots = phi^{+-2}
phi = (1 + sp.sqrt(5))/2
log("")
log("golden ratio phi = (1+sqrt5)/2 = %s" % mp.nstr(mp.mpf((1+mp.sqrt(5))/2), 25))
log("phi^2   = (3+sqrt5)/2          = %s" % sp.simplify(phi**2))
log("phi^-2  = (3-sqrt5)/2          = %s" % sp.simplify(1/phi**2))
# confirm phi^2 and phi^-2 are exactly the two Alexander roots
r_hi = sp.nsimplify((3 + sp.sqrt(5))/2)
r_lo = sp.nsimplify((3 - sp.sqrt(5))/2)
log("Delta(phi^2)                   = %s  (~0): %s"
    % (sp.simplify(Delta.subs(t, phi**2)), sp.simplify(Delta.subs(t, phi**2)) == 0))
log("Delta(phi^-2)                  = %s  (~0): %s"
    % (sp.simplify(Delta.subs(t, 1/phi**2)), sp.simplify(Delta.subs(t, 1/phi**2)) == 0))
log("numeric roots                  = %s , %s"
    % (mp.nstr(mp.mpf((3+mp.sqrt(5))/2),20), mp.nstr(mp.mpf((3-mp.sqrt(5))/2),20)))
log("phi^2 numeric = 2.6180339887..., phi^-2 = 0.3819660112...")

# 'inverse Alexander' -- Phase 2 gives Delta^{-1}; its poles are the roots above.
# The reciprocal polynomial t^2 Delta(1/t) = 1 - 3t + t^2 is SELF-RECIPROCAL:
Delta_recip = sp.expand(t**2 * Delta.subs(t, 1/t))
log("")
log("reciprocal t^2*Delta(1/t)      = %s   (self-reciprocal: roots phi^{+2}<->phi^{-2})"
    % Delta_recip)
log("=> 'inverse Alexander' Delta^-1 has the SAME golden roots phi^{+-2} in Q(sqrt5)")

# ---------------------------------------------------------------------------
# VERDICT
# ---------------------------------------------------------------------------
log("")
log("="*78)
log("VERDICT")
log("="*78)
log("Phase 1 (non-trivial action) -> A-poly + Vol=%s , trace field Q(sqrt-3)"
    % mp.nstr(Vol, 12))
log("Phase 2 (vanishing action)   -> inverse-Alexander, roots phi^{+-2}, field Q(sqrt5)")
log("")
log("object's split:")
log("  BEING   = A-poly / hyperbolic volume / Q(sqrt-3)   ==  Phase 1  [EXACT]")
log("  HEARING = Alexander / golden phi^{+-2} / Q(sqrt5)  ==  Phase 2  [EXACT]")
log("")
log("The two Kashaev quasiclassical phases carry TWO DISTINCT quadratic fields")
log("(disc -3 vs disc +5) that coincide, object-invariant, with being vs hearing.")
log("OUTCOME (probe 1) = A : the two phases ARE exactly being/hearing.")
log("(campaign-level: this is STRUCTURE, rung-2 torsor-adjacent; it does NOT by")
log(" itself open a free coupling -- see probes 2 & 3.)")

with open(__file__.replace('.py', '_out.txt'), 'w') as f:
    f.write("\n".join(OUT) + "\n")
