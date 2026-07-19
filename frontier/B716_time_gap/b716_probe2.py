#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
B716 PROBE 2 — CANONICAL 4d? Is there a canonical 4d spacetime the object
SELECTS, or is 4d-ness external?

FIREWALL: origin-axiom. Structural/mathematical only. No cosmology, no SM
value, no physics assertion beyond structural characterization. Verify-don't-
trust: every claim reproduced/derived in-sandbox where feasible; theorems that
cannot be re-run are cited with the SPECIFIC discriminating input computed here.

THE OBJECT: M = S^3 \\ 4_1 (figure-eight knot complement) = H^3/Gamma, a cusped
hyperbolic 3-manifold; equivalently the once-punctured-torus bundle with Anosov
monodromy sigma = [[2,1],[1,1]].

QUESTION: physical spacetime is 4d. Does the object canonically SELECT a 4d, or
is the 4th dimension always ADDED externally?

Candidate 4d constructions examined:
  (C1) M x R          -- product with a time line.
  (C2) mapping-torus S^1 -- the fibration's S^1.
  (C3) a 4-manifold bounding M (cobordism / canonical 4d filling), tested
       against the object's INTRINSIC data: A-polynomial, trace field, torsion.
  (C4) same-geometry-up-one-dimension in real-hyperbolic H^4: (a) M as a cusp
       cross-section (obstructed), and (b) M as the totally geodesic boundary of
       a hyperbolic 4-manifold W (EXISTS by Slavich 2016, but non-canonical).
  (C5) complex-hyperbolic CH^2/Gamma' (spherical CR uniformization, Falbel /
       Deraux-Falbel) -- the strongest candidate for "the object selects a 4d".

Two-outcome: A = a canonical 4d spacetime selected by the object;
             B = external-only (object is intrinsically 3d; 4d-ness is added).
"""

import sys
import numpy as np

LOG = []
def out(s=""):
    print(s)
    LOG.append(str(s))

out("="*74)
out("B716 PROBE 2 — CANONICAL 4d, OR EXTERNAL 4th DIMENSION?")
out("="*74)

# ---------------------------------------------------------------------------
# STEP 0 — pin the object down in-sandbox (snappy): what IS its intrinsic data?
# ---------------------------------------------------------------------------
out("\n[STEP 0] The object's intrinsic 3-dimensional data (snappy, in-sandbox)")
out("-"*74)
try:
    import snappy
    M = snappy.Manifold('4_1')
    VOL = float(M.volume())          # snappy Number -> float for formatting
    ncusps = int(M.num_cusps())
    out(f"  manifold            : {M}")
    out(f"  hyperbolic volume   : {VOL:.10f}   (>0 => genuinely hyperbolic, not flat)")
    out(f"  num cusps           : {ncusps}")
    # cusp cross-section topology
    try:
        topo = [c.topology for c in M.cusp_info()]
    except Exception:
        topo = ['torus cusp']
    out(f"  cusp topology       : {topo}  (a 2-torus T^2)")
    # trace field, computed in-sandbox.  snappy's trace_field_gens().find_field()
    # needs Sage; under the pyenv interpreter it raises SageNotAvailable, so we
    # do NOT merely cite -- we take the trace-field minimal polynomial and CLOSE
    # the identification of the field by an in-sandbox discriminant computation.
    # (Independently reproduced under sage-python: M.trace_field_gens().find_field()
    #  returns the number field with defining polynomial x^2 - 2x + 4, z = 1+sqrt(3)i.)
    import sympy as sp
    xx = sp.symbols('x')
    tf_ok = False
    try:
        F = M.trace_field_gens().find_field(100, 10)   # (prec, deg) -- Sage only
        if F is not None:
            minpoly = str(F[0])
            out(f"  trace field (snappy): defining poly {minpoly}")
            tf_ok = True
    except Exception as e:
        out(f"  trace field         : minpoly x^2-2x+4 (sage-python reproduced; "
            f"pyenv snappy: {type(e).__name__})")
    # in-sandbox identification: disc(x^2-2x+4) = -12 = -3*2^2 => field = Q(sqrt(-3)).
    tf_poly = xx**2 - 2*xx + 4
    disc = sp.discriminant(tf_poly, xx)
    sqfree = sp.sqrtdenest(sp.sqrt(disc))            # sqrt(-12) = 2*sqrt(-3)
    out(f"  disc(x^2-2x+4)      : {disc} = -3*2^2  =>  Q(sqrt({disc}))=Q(sqrt(-3))")
    # cross-check via the other standard minpoly x^2-x+1 (primitive 6th root/omega)
    roots = sp.solve(xx**2 - xx + 1, xx)
    out(f"  Q(sqrt(-3)) check   : roots of x^2-x+1 = {roots}  (Eisenstein/omega);"
        f" sqrt(disc)={sqfree}")
    out("  fibered             : YES (once-punctured-torus bundle); monodromy")
    out("                        sigma = [[2,1],[1,1]] (Anosov, |tr|=3>2).")
    # confirm sigma is Anosov: |trace| > 2, real eigenvalues (golden-ratio^2)
    import numpy as _np
    sigma = _np.array([[2,1],[1,1]], dtype=float)
    ev = sorted(float(z.real) for z in _np.linalg.eigvals(sigma))
    out(f"  monodromy eigenvalues: [{ev[0]:.6f}, {ev[1]:.6f}] = [phi^-2, phi^2]"
        f"  (real, |lambda|!=1 => Anosov)")
    SNAPPY_OK = True
except Exception as e:
    out(f"  [snappy unavailable: {e}] using known values.")
    SNAPPY_OK = False
    VOL = 2.0298832128193072  # 2 * Catalan-type; fig-8 volume = 2.02988...

out("""
  => The object is presented in EXACTLY 3 real dimensions:
     - as H^3/Gamma (3d hyperbolic), or
     - as (T^2\\pt) x_sigma S^1  (fiber 2d + base S^1 = 3d).
     The A-polynomial (a plane curve in (C*)^2), the trace field Q(sqrt(-3)),
     and the Reidemeister torsion (a scalar/function) are all invariants of a
     3-MANIFOLD. None of them has a '4th slot'.""")

# ---------------------------------------------------------------------------
# STEP 1 — (C1) M x R : does any object datum pick the R?
# ---------------------------------------------------------------------------
out("\n[STEP 1] (C1)  M x R  — the static-cylinder 'spacetime'")
out("-"*74)
out("""  M x R is a 4-manifold, but the R factor is pure product: it carries NO
  metric scale, NO orientation preference, NO marked point — nothing is
  supplied by M. The SAME construction works for ANY 3-manifold, so it cannot
  be 'selected' by THIS object: M does not distinguish its own R from any
  other's. R is a free external choice (a chosen clock), not object data.
  DISCRIMINATOR: the map {3-manifolds} -> {M x R} is a functor with no M-input
  to the fiber R; the fiber is constant. => 4th dimension is ADDED, not read.""")

# ---------------------------------------------------------------------------
# STEP 2 — (C2) the fibration S^1 is ALREADY the 3rd dimension
# ---------------------------------------------------------------------------
out("\n[STEP 2] (C2)  the mapping-torus S^1 — already spent as the 3rd dimension")
out("-"*74)
out("""  M = (T^2\\pt) x_sigma S^1.  The S^1 base of the fibration is the manifold's
  OWN third dimension (fiber 2d + base 1d = 3d). It is not free to be re-used
  as a 4th dimension. One CAN form M x S^1 (a closed 4-manifold) or the
  mapping torus of a self-map of M, but that new S^1/interval is again an
  EXTERNAL factor with no data from M, and M x S^1 is closed (bounds nothing
  canonically; it is not a 'filling' of M). => no 4th dimension authored here.""")

# ---------------------------------------------------------------------------
# STEP 3 — (C3) a 4-manifold BOUNDING M: existence vs. canonicity
#   Oriented bordism Omega_3^SO = 0 (Rokhlin/Thom): EXISTENCE guaranteed.
#   But the SET of fillings is INFINITE — we EXHIBIT non-uniqueness via the
#   signature (connect-sum with CP^2 changes signature by +1), computed here.
# ---------------------------------------------------------------------------
out("\n[STEP 3] (C3)  a 4-manifold bounding M — EXISTENCE is free, CANONICITY fails")
out("-"*74)
out("""  THEOREM (Thom 1954; Rokhlin 1951): Omega_3^SO = 0, the oriented bordism
  group in dimension 3 is trivial. So EVERY closed oriented 3-manifold bounds a
  compact oriented 4-manifold. (M here is cusped/open; cap the cusp with a solid
  torus -- e.g. the trivial Dehn filling giving a closed 3-mfd -- which also
  bounds.) EXISTENCE of a 4d filling is therefore never the obstruction.

  The obstruction is UNIQUENESS. We show the set of fillings is infinite and has
  no canonical/minimal member, using the signature, computed in-sandbox:""")

# The signature is additive under connect sum and boundary-connect sum:
#   sigma(W # X) = sigma(W) + sigma(X),  and  d(W # X) = dW.
# CP^2 is closed oriented with signature +1. So W, W#CP^2, W#2CP^2, ... all
# bound the SAME M, with signatures s, s+1, s+2, ... -> infinitely many
# distinct fillings, no minimal-by-canonical-invariant choice.
def signature_of_form(Q):
    """signature = (#positive eigenvalues) - (#negative eigenvalues)."""
    w = np.linalg.eigvalsh(np.array(Q, dtype=float))
    pos = int(np.sum(w > 1e-9))
    neg = int(np.sum(w < -1e-9))
    return pos - neg

# intersection form of CP^2 is (+1); of CP^2-bar is (-1); of S^2xS^2 is [[0,1],[1,0]] (sig 0).
sig_CP2   = signature_of_form([[1.0]])
sig_CP2b  = signature_of_form([[-1.0]])
sig_S2S2  = signature_of_form([[0,1],[1,0]])
out(f"  sig(CP^2)     = {sig_CP2:+d}")
out(f"  sig(CP^2-bar) = {sig_CP2b:+d}")
out(f"  sig(S^2xS^2)  = {sig_S2S2:+d}")
out(f"""
  Given ANY filling W with boundary M and signature s:
     W, W#CP^2, W#2CP^2, ...  all have boundary M and signatures s, s+1, s+2,...
     W#CP^2-bar, ...          give s-1, s-2, ...
     W#S^2xS^2, ...           add rank 2 to b_2 with no signature change.
  => a countably infinite family of PAIRWISE NON-DIFFEOMORPHIC 4-manifolds, all
     bounding the SAME M. No signature-minimal, no b_2-minimal canonical pick
     that M's intrinsic data forces.

  Do the object's named invariants pick one? Checked:
   - A-polynomial A(L,M): a curve in (C*)^2 (the SL(2,C) character-variety
     boundary). A curve is a 2-real-dim object; it produces no 4-manifold, and
     is a diffeo/topology invariant of M, not of any filling.
   - trace field Q(sqrt(-3)): a number field; selects the arithmetic of Gamma,
     not a 4-manifold. (It DOES pick a natural symmetric space -- but that is
     H^3, 3-dimensional; see STEP 4.)
   - Reidemeister/adjoint torsion: a scalar (or a function on the character
     variety); no 4-manifold output.
  => none of the intrinsic data has a canonical 4-manifold as its value.""")

# ---------------------------------------------------------------------------
# STEP 4 — (C4) same geometry one dimension up: real-hyperbolic H^4/Gamma'.
#   TWO distinct realizations, tested separately:
#   (a) M as a CUSP cross-section of H^4/Gamma'  -> OBSTRUCTED (cusps are FLAT).
#   (b) M as the TOTALLY GEODESIC BOUNDARY of a hyperbolic 4-manifold W
#       -> EXISTS (Slavich 2016), but NON-CANONICAL, a filling, and Riemannian.
# ---------------------------------------------------------------------------
out("\n[STEP 4] (C4)  real-hyperbolic H^4 one dimension up — two sub-cases")
out("-"*74)
out(f"""  (a) M as a CUSP cross-section of a finite-volume H^4/Gamma'  -- OBSTRUCTED.
  THEOREM (horoball quotient + Bieberbach): cusp cross-sections of finite-volume
  hyperbolic n-manifolds are CLOSED FLAT (Euclidean) (n-1)-manifolds; for n=4,
  closed flat 3-manifolds. Discriminating computation: M is HYPERBOLIC with
  volume = {VOL:.6f} > 0 (NOT flat: a flat 3-manifold has sectional curvature 0)
  and NON-COMPACT (it has its own cusp), while cusp cross-sections are CLOSED.
  Two independent obstructions => M is NOT the cusp of any hyperbolic 4-manifold.

  (b) M as the TOTALLY GEODESIC BOUNDARY of a hyperbolic 4-manifold W -- EXISTS.
  [CORRECTED, prior round had wrongly dismissed this sub-case unchecked.]
  THEOREM (Slavich, 'The complement of the figure-eight knot geometrically
  bounds', Proc. AMS / arXiv:1511.08684, Thm 1.1): the figure-eight complement M
  GEOMETRICALLY BOUNDS -- it is isometric to the totally geodesic boundary of a
  complete, finite-volume real-hyperbolic 4-manifold W (the FIRST hyperbolic knot
  complement shown to do so; W has smallest volume among the known such fillings).
  So a genuine 'same-geometry, one dimension up' 4d filling DOES exist -- with M's
  own hyperbolic metric on the boundary, no enhancement.

  Why (b) still does NOT deliver 'a canonical 4d spacetime the object selects':
   - NON-CANONICAL: Slavich's W is ONE explicit construction (an existence
     result -- 'the first example'), not a unique or minimal-by-object-invariant
     filling. Geometric-bounding manifolds are highly non-unique in general (pass
     to covers, or vary the internal gluing) -- M's A-polynomial / trace field /
     torsion single out no particular W. No uniqueness is claimed or available.
   - FILLING, not becoming: M is the 3-dim boundary of W; the 4th dimension is
     the interior added OVER M, not a direction M itself extends in.
   - RIEMANNIAN, not Lorentzian: W carries the H^4 metric, signature (4,0), a
     negatively-curved Riemannian 4-manifold -- never a Lorentzian (3,1) spacetime.
  => (C4b) gives a real, object-metric 4d filling, but a NON-canonical, Riemannian
     one -- existence, not selection; a bounding, not an authored spacetime.""")

# ---------------------------------------------------------------------------
# STEP 5 — (C5) complex-hyperbolic CH^2/Gamma' (spherical CR): the strongest
#   candidate for "the object selects a 4d". Exists (Falbel; Deraux-Falbel 2015)
#   but requires a PU(2,1) enhancement, is non-unique, and is RIEMANNIAN.
# ---------------------------------------------------------------------------
out("\n[STEP 5] (C5)  complex-hyperbolic CH^2/Gamma' (spherical CR) — the")
out("               strongest A-candidate; it still fails 'canonical spacetime'")
out("-"*74)
out("""  This is the one genuine 4-real-dimensional object the fig-8 is known to
  bound-at-infinity. FACT (Falbel 2008; Deraux-Falbel, 'Complex hyperbolic
  geometry of the figure eight knot', Geom.Topol. 19 (2015) 237-293,
  arXiv:1303.7096, Thm 1.1): there is a discrete Gamma < PU(2,1) whose domain of
  discontinuity Omega in dCH^2=S^3 is non-empty, Gamma acts freely on Omega, and
  Omega/Gamma is homeomorphic to M -- a spherical CR uniformization of M. The 4d
  interior (CH^2 cup Omega)/Gamma is complex-hyperbolic with ideal boundary M. It
  is read off boundary-unipotent PU(2,1) characters (the same Falbel components
  reproduced in B71).

  Why it still does NOT deliver 'a canonical 4d spacetime the object selects'
  -- and note carefully what is and is NOT true about uniqueness:

   (ii) [CORRECTED] It is NOT non-canonical by component-counting -- the opposite.
        Deraux-Falbel Thm 1.1 proves the spherical CR uniformization is UNIQUE
        *provided the peripheral (cusp) holonomy is unipotent* -- and unipotent
        cusp holonomy is exactly M's own intrinsic complete-structure parabolic
        type. Of the three boundary-unipotent representations, rho_1 (the totally-
        real / Sym^2 'geometric' one = B71's V0) does NOT uniformize (its limit
        set is the whole sphere, empty domain of discontinuity); rho_2, rho_3 do,
        but their images Gamma_2, Gamma_3 are CONJUGATE in PU(2,1) (related by M's
        own amphichiral orientation-reversing symmetry) -- ONE filling under two
        markings, not two fillings. [The prior round wrongly cited '3 components'
        to argue non-uniqueness; the cited theorem in fact proves uniqueness in
        this natural class.] Genuine non-uniqueness appears ONLY if one DROPS
        unipotency: Deraux (arXiv:1410.1198) builds a 1-parameter family of
        pairwise non-conjugate uniformizations with TWIST-PARABOLIC (non-
        unipotent) cusp holonomy -- but that abandons the very cusp type that
        mirrors M's complete structure. So uniqueness, if anything, is the
        A-leaning datapoint here; the case for B rests on (i),(iii),(iv):

   (i)  ENHANCEMENT + NON-FAITHFUL: the uniformization needs a chosen rho:
        pi_1(M) -> PU(2,1) that is NOT in the bare 3-manifold's intrinsic data
        (topology / trace field Q(sqrt-3) / A-poly / torsion). Worse, this rho is
        NOT FAITHFUL: Deraux-Falbel note every elliptic element of Gamma has an
        isolated fixed point in CH^2, i.e. Gamma CONTAINS TORSION; but pi_1(M) is
        torsion-free (M is an aspherical hyperbolic manifold), so rho_2 cannot be
        injective. Contrast the INTRINSIC geometric holonomy pi_1(M) -> SL(2,C),
        which IS discrete and faithful and lands in Isom(H^3) -- 3-dimensional.
        The 4d structure comes from a chosen NON-faithful rep, not from carrying
        pi_1(M) up one dimension.
   (ii')ORBIFOLD, not a manifold copy of M one dimension up: because Gamma has
        torsion (elliptic elements with interior fixed points), the 4d filling
        (CH^2 cup Omega)/Gamma is an ORBIFOLD with cone singularities -- only its
        ideal boundary Omega/Gamma is the manifold M. So this is not 'M itself,
        one real dimension up', the way H^3/Gamma faithfully IS pi_1(M).
   (iii)RIEMANNIAN, not a spacetime: CH^2 is a negatively-curved RIEMANNIAN
        4-manifold (signature (4,0)), not Lorentzian (3,1). It supplies a 4d
        FILLING, not TIME. (Whether a Lorentzian continuation exists is Probe 3;
        B710 already found the object's thimbles inverted from FRW.)
   (iv) FILLING, not the object BECOMING 4d: M remains the 3d ideal boundary; the
        4th dimension is interior added over it, entered only through the chosen
        non-faithful enhancement.

  => The best candidate is UNIQUE in the natural cusp class, yet it is an
     ENHANCEMENT-DEPENDENT, NON-FAITHFUL, ORBIFOLD, RIEMANNIAN filling. It is
     'a 4d the object can bound', not 'a Lorentzian 4d spacetime the object
     authors'. Uniqueness of the boundary-CR structure does not make the 4d
     interior a spacetime the object selects to BE.""")

# ---------------------------------------------------------------------------
# STEP 6 — the sharpest objection: SL(2,C) IS Spin(3,1), the 4d Lorentz group.
#   Isn't 4d Lorentzian structure already intrinsic in the holonomy? No: the
#   holonomy acts on the SINGLE 3d hyperboloid H^3 inside R^{3,1}; the 4th
#   (radial/timelike) direction is a fixed linear ambient factor, not a
#   manifold direction Gamma moves in. Verified below.
# ---------------------------------------------------------------------------
out("\n[STEP 6]  sharpest objection: SL(2,C) = Spin(3,1) is the 4d Lorentz group")
out("-"*74)
out("""  A physicist objects: the object's holonomy Gamma < SL(2,C), and
  SL(2,C) = Spin(3,1) is the double cover of the 4d Lorentz group SO^+(3,1).
  Isn't a Lorentzian 4d structure therefore already intrinsic?

  No -- and the reason is exactly the 3d/4d gap. SL(2,C) acts as the FULL
  isometry group of H^3, realized as the upper sheet {x.x = -1, x0>0} of the
  hyperboloid inside Minkowski R^{3,1}. Gamma moves points WITHIN that one
  3-dimensional sheet (fixed 'radius'); it does not translate in the 4th
  (radial/timelike) direction. Check: the vector rep of Spin(3,1) preserves the
  Minkowski form, and each sheet {x.x = -1} is a 3-manifold; the quotient
  H^3/Gamma is 3d. The 4th coordinate is a FIXED ambient linear slot, identical
  for every 3-manifold whose holonomy lands in SL(2,C) -- it is not authored by
  THIS object any more than R was in (C1).""")
# demonstrate: a Lorentz boost (in SL(2,C)) preserves the mass shell x.x=-1
# and keeps the point ON the single 3d sheet (does not create a 4th orbit dim).
eta = np.diag([-1.0, 1.0, 1.0, 1.0])          # Minkowski metric (- + + +)
# a boost in the x-direction, rapidity r
r = 0.7
B = np.array([[np.cosh(r), np.sinh(r), 0, 0],
              [np.sinh(r), np.cosh(r), 0, 0],
              [0, 0, 1, 0],
              [0, 0, 0, 1]])
x0 = np.array([1.0, 0.0, 0.0, 0.0])            # a point on the sheet: x.x = -1
x1 = B @ x0
q0 = x0 @ eta @ x0
q1 = x1 @ eta @ x1
out(f"\n  point on H^3 sheet   : x.x = {q0:+.6f}   (=-1, on the 3d hyperboloid)")
out(f"  after a Lorentz boost: x.x = {q1:+.6f}   (STILL -1: stays on the SAME sheet)")
out("""  => the Lorentz group acts transitively on ONE 3d sheet; no 4th manifold
     dimension is generated. 'Spin(3,1)' names the isometries of a 3d space,
     not a 4d spacetime the object is built on. (The linear (1/2,1/2)-rep IS
     Minkowski 4-space, but that is a representation module, not a quotient the
     object lives in.) The 4th dimension remains ADDED, not authored.""")

# ---------------------------------------------------------------------------
# VERDICT
# ---------------------------------------------------------------------------
out("\n" + "="*74)
out("VERDICT")
out("="*74)
out("""
  OUTCOME B  — EXTERNAL-ONLY.  The object is intrinsically 3-dimensional; a 4th
  dimension is always ADDED, never uniquely AUTHORED.

  Scorecard of candidate 4d constructions:
    (C1) M x R                 : R is a free external clock; no M-datum picks it.
    (C2) fibration S^1         : already spent as M's own 3rd dimension.
    (C3) 4-manifold bounding M : EXISTS (Omega_3^SO = 0) but INFINITELY non-
                                 unique (signature +/- via #CP^2, computed);
                                 A-poly / trace field / torsion select NO
                                 canonical filling.
    (C4a) H^4 cusp             : OBSTRUCTED (cusps of H^4 are FLAT 3-manifolds;
                                 M is hyperbolic, vol>0, and non-compact).
    (C4b) H^4 geodesic bdry    : EXISTS -- M geometrically bounds a hyperbolic
                                 4-manifold W (Slavich 2016), with M's own metric
                                 -- but NON-canonical (one construction, no
                                 uniqueness) and RIEMANNIAN (4,0), a filling.
    (C5) complex-hyperbolic    : the strongest -- a spherical CR uniformization
         CH^2 (spherical CR)      UNIQUE given unipotent cusps (Deraux-Falbel Thm
                                 1.1), yet the 4d interior is a NON-FAITHFUL
                                 (Gamma has torsion; pi_1(M) is torsion-free),
                                 ORBIFOLD, RIEMANNIAN filling -- not a spacetime.

  DISCRIMINATING FACT:
    NO object-intrinsic invariant is 4-manifold-valued: the A-polynomial is a
    plane curve, the trace field Q(sqrt-3) is a number field (disc(x^2-2x+4)=-12,
    computed here), the Reidemeister torsion is a scalar/function -- all three are
    invariants of a 3-MANIFOLD with no 4th slot. Consequently every 4d over M is
    EITHER external / non-canonical -- M x R (constant fiber); a bounding
    4-manifold (Omega_3^SO=0) that is INFINITELY non-unique, W, W#CP^2, W#2CP^2,
    ... with signatures s, s+1, s+2, ... (computed here); Slavich's hyperbolic
    geodesic-boundary filling W (exists, but one non-unique construction) --
    OR obstructed (M is not an H^4 cusp: cusps are FLAT, M is hyperbolic
    vol=%.6f>0 and non-compact) -- OR, in the one case that IS canonical (the
    unipotent spherical CR structure, UNIQUE by Deraux-Falbel), the 4d interior
    is only a RIEMANNIAN (signature (4,0)) ORBIFOLD reached through a NON-FAITHFUL
    PU(2,1) rep (Gamma carries torsion absent from the torsion-free pi_1(M)),
    never a Lorentzian spacetime and never pi_1(M) realized one dimension up.
    The faithful, intrinsic holonomy pi_1(M)->SL(2,C) lands in 3-dim H^3.
    => 4d-ness is EXTERNAL; the object is timeless 3d being.

  Consistent with the frontier's expected endpoint: 4d-ness (like chirality
  B713 and values B685/B706) is the OBSERVER-COUPLING's, not the object's.
  Structural only; Gate 5 stands; nothing to CLAIMS.""" % VOL)

# write log
with open(__file__.replace('.py', '_out.txt'), 'w') as f:
    f.write("\n".join(LOG) + "\n")
out("\n[written] " + __file__.replace('.py', '_out.txt'))
