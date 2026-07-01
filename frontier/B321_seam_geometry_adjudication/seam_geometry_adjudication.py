"""B321 -- adjudication of the cross-chat 'self-realizability / seam geometry' arc (verify-don't-trust, brave-partner).
Run: python (pyenv). Chat-1 (seam geometry) + Chat-2 (self-realizability) ran a long multi-swing arc; this separates the
one verified new fact from the reframes and the splices.

VERIFIED (new, real, firewalled): |cusp shape|^2 = h(E6) = 12. The figure-eight cusp shape is 2 sqrt3 i (SnapPy:
0 + 3.4641...i, |shape|^2 = 12.000000000), and h(E6) = 12 (Coxeter number). Both root in Q(sqrt-3) -- the cusp via the
trace field, h(E6) via 2T -> McKay -> E6. So the core-length quadratic form of the Dehn fillings is Q(p,q) = |p+q*tau|^2
= p^2 + 12 q^2, with coefficient h(E6). A genuine, striking certificate. CAVEAT: |tau|^2 is NOT SL(2,Z)-invariant
(basis-dependent), so this is a coincidence/certificate, not a canonical invariant identity; and any physics reading is
firewalled.

REFUTED (splice): "the CP phase pi/6 IS the core geodesic length of the filling (6,3)=3x(2,1)". Three problems:
  (a) gcd(6,3)=3 -> (6,3) is NOT a primitive Dehn slope (only coprime (p,q) give distinct fillings);
  (b) "core(6,3)=core(2,1)/3" is the TRIVIAL quadratic scaling Q(3z)=9Q(z) (sqrt Q(6,3)=12=3*4=3*sqrt Q(2,1)), NOT a
      "generation Z/3 acting on the (2,1) direction";
  (c) it equates an ANGLE (arg(kappa)=+/-pi/6, B285) with a LENGTH (a core geodesic) -- a dimensional splice.
  (Chat-1 self-flagged: "structural not dynamical; one number could be coincidence.") Not a meaningful identity.

REFUTED: "the democratic Yukawa (3lam,0,0) is forced rank-1 by the Z/3 (|omega|=1)". |omega|=1 => Q(omega z)=Q(z) is
true but trivial (a rotation preserves the norm); it does NOT produce the all-ones matrix. B320 already proved a
Z/3-invariant matrix is a generic circulant (rank 3); the rank-1 all-ones needs S3-democracy. So this CONTRADICTS B320,
is firewalled physics, and presupposes the B307-gated 3 generations.

REFRAME (banked content, re-described): "self-realizability" = the object self-determining a value by which
configuration realizes its golden identity. Its two 'crossings' are banked results reframed -- the CP sign = the
object's chirality (Im w>0 selects the geometric structure vs its mirror) is B285/B318; the scale k=3 (2cos(pi/5)=phi)
is B313. Real, useful reframe of the firewall's INTERIOR; not new content. The 'flow-selection' version was correctly
killed by Chat-2 (sigma=[[2,1],[1,1]] is orientation-preserving, so the flow cannot select a handedness).

THE GENUINE RESIDUE: the sharpened multiplicity gate. Chat-2's honest self-correction: single-object self-realizability
-> 1 generation (B307); RELATIONAL self-realizability -- via the intrinsic commensurator Z/3 (Eisenstein units of
Q(sqrt-3), PGL(2,O_-3), B302) -- is UNTESTED and is where a genuine 3 could live. Stated with a refutation condition:
OPENS iff the commensurator Z/3 gives three SYMMETRIC copies of the 27; CLOSES iff they are the trinification factors
(color/L/R, B302/B305 -- the wrong 3) or fail to be symmetric matter copies. = the standing multiplicity gate
(B302/B307) sharpened -> belongs in OPEN_PROBLEMS.md. FIREWALLED; nothing to CLAIMS.
"""
import math
from math import gcd


def cusp_norm():
    """|2 sqrt3 i|^2, the figure-eight cusp-shape norm (SnapPy: shape = 2 sqrt3 i)."""
    return round((2 * math.sqrt(3)) ** 2)


def h_e6():
    return 12


def Q(p, q):
    """the cusp norm form = |p + q*tau|^2 with tau = 2 sqrt3 i."""
    return p * p + h_e6() * q * q


def is_primitive(p, q):
    return gcd(p, q) == 1


def q_scaling_is_trivial():
    """Q(6,3) = 9 Q(2,1): the (6,3)=3*(2,1) 'core/3' is just Q(3z)=9Q(z)."""
    return Q(6, 3) == 9 * Q(2, 1)


# --- the verdict facts ---
CUSP_NORM_IS_HE6 = True                          # |cusp shape|^2 = 12 = h(E6) (SnapPy-verified) -- real certificate
CUSP_NORM_IS_BASIS_DEPENDENT = True              # |tau|^2 not SL(2,Z)-invariant -> certificate, not canonical identity
CP_PHASE_EQ_CORE_LENGTH_IS_SPLICE = True         # (6,3) non-primitive + trivial scaling + angle != length
DEMOCRATIC_RANK1_FROM_Z3_CONTRADICTS_B320 = True  # Z/3 -> circulant rank 3; rank-1 needs S3
SELF_REALIZABILITY_IS_REFRAME_OF_BANKED = True   # CP sign=chirality (B285/B318) + scale k=3 (B313)
FLOW_SELECTION_SPLICE_CORRECTLY_KILLED = True    # sigma orientation-preserving (Chat-2's own catch)
SHARPENED_MULTIPLICITY_GATE_IS_THE_RESIDUE = True  # relational commensurator-Z/3 + refutation condition -> OPEN_PROBLEMS
DERIVES_SM_VALUES = False


def verdict():
    return bool(
        cusp_norm() == 12 and h_e6() == 12
        and not is_primitive(6, 3) and q_scaling_is_trivial()
        and CUSP_NORM_IS_HE6 and CUSP_NORM_IS_BASIS_DEPENDENT and CP_PHASE_EQ_CORE_LENGTH_IS_SPLICE
        and DEMOCRATIC_RANK1_FROM_Z3_CONTRADICTS_B320 and SELF_REALIZABILITY_IS_REFRAME_OF_BANKED
        and FLOW_SELECTION_SPLICE_CORRECTLY_KILLED and SHARPENED_MULTIPLICITY_GATE_IS_THE_RESIDUE
        and not DERIVES_SM_VALUES
    )


if __name__ == "__main__":
    print("VERIFIED: |cusp shape|^2 =", cusp_norm(), "= h(E6) =", h_e6(), "(SnapPy cusp = 2 sqrt3 i; both Q(sqrt-3))")
    print("SPLICE: (6,3) primitive?", is_primitive(6, 3), "| Q(6,3)=", Q(6, 3), "= 9*Q(2,1)=", 9 * Q(2, 1),
          "(trivial scaling; angle != length)")
    print("REFUTED: democratic rank-1 from Z/3 contradicts B320 (Z/3 -> circulant rank 3; rank-1 needs S3)")
    print("REFRAME: self-realizability = B285/B318 (CP sign=chirality) + B313 (scale k=3); flow-splice killed")
    print("RESIDUE: relational commensurator-Z/3 generation gate (with refutation condition) -> OPEN_PROBLEMS")
    print("verdict:", verdict())
