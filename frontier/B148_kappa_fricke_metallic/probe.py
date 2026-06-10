"""B148 -- the kappa/Fricke-Vogt identity, the metallic monodromy as the SL(2,Z) MCG action, and the invariant data
a class-S comparison needs. INDEPENDENT re-derivation (verify-don't-trust on a cross-session handoff): every claim
below is re-proved symbolically here (sympy), not inherited.

  FIREWALL (state first, do not lose). A scale-free conserved invariant -- kappa = tr[A,B], a pure number / element
  of C/pi^2 Z under the Chern-Simons reading -- has no beta-function, no RG flow, no anomaly, and CANNOT become a
  dimensionful energy density without an externally supplied scale. Every established case where a dimensionless/
  topological quantity touches a dimensionful observable (theta in the QCD vacuum, the CS level, quantized Hall
  conductance, anomaly coefficients) sets a QUANTIZED/dimensionless RATIO; the SCALE is always supplied independently
  (Lambda_QCD^4, e^2/h, hbar/level). So EVERYTHING here is mathematics about the tower's SYMMETRY -- NOT a bridge to
  vacuum energy or the Standard Model. The physics aspiration is POSTULATED and quarantined; nothing promotes to
  ../../CLAIMS.md. (The decisive primary-source confirmation of the firewall is an OPEN reading task -- see FINDINGS
  section 4.B; the dimensional argument above is strong but is formally an absence, not a cited no-go theorem.)

What is RE-DERIVED here (all exact, symbolic):
  S1  the Fricke commutator identity tr(ABA^-1 B^-1) = x^2+y^2+z^2-xyz-2 =: kappa   (from generic SL(2,C) A,B);
      kappa = 4*I_FV + 2 under the HALF-trace convention (x=2X); both trace maps preserve their own invariant.
  S2  tr(R^m L^m) = m^2+2 (symbolic m); the Dehn twists tau_a, tau_b preserve kappa (=> the SL(2,Z) MCG action);
      the kappa=-2 slice is the Markov surface; (3,3,3) [Markov root] and (0,0,0) [Q8 point] BOTH lie on kappa=-2.
  S3  R^m L^m is hyperbolic (|tr|=m^2+2>2); its top eigenvalue is (metallic mean)^2; the boundary fixed slopes are
      the roots of t^2+mt-1=0; the eigenvalue/trace field is Q(sqrt(m^2+4)) REDUCED (m=1,4 share Q(sqrt5)).

Run under plain pyenv (pure sympy; no SnapPy/Sage/cypari needed). MATH tier; firewalled.
"""
from __future__ import annotations

import sympy as sp


# ---------------------------------------------------------------------------------------------------------------------
# S1 -- the kappa / Fricke-Vogt identity, pinned exactly
# ---------------------------------------------------------------------------------------------------------------------

def kappa_poly(x, y, z):
    """Full-trace (commutator) cubic kappa = tr[A,B]."""
    return x**2 + y**2 + z**2 - x*y*z - 2


def fricke_vogt(X, Y, Z):
    """Half-trace (Fricke-Vogt) invariant I conserved by the Fibonacci trace map."""
    return X**2 + Y**2 + Z**2 - 2*X*Y*Z - 1


def verify_fricke_commutator():
    """tr(ABA^-1 B^-1) = x^2+y^2+z^2-xyz-2, from generic SL(2,C) matrices with det enforced = 1."""
    a, b, c, e, f, g = sp.symbols("a b c e f g")
    d = (1 + b*c) / a                       # det A = 1
    h = (1 + f*g) / e                       # det B = 1
    A = sp.Matrix([[a, b], [c, d]])
    B = sp.Matrix([[e, f], [g, h]])
    Ai = sp.Matrix([[d, -b], [-c, a]])      # inverse (det 1)
    Bi = sp.Matrix([[h, -f], [-g, e]])
    tr_comm = sp.simplify((A * B * Ai * Bi).trace())
    x = sp.simplify(A.trace())
    y = sp.simplify(B.trace())
    z = sp.simplify((A * B).trace())
    diff = sp.simplify(tr_comm - kappa_poly(x, y, z))
    return diff == 0


def verify_kappa_4I_plus_2():
    """kappa(2X,2Y,2Z) = 4*I_FV(X,Y,Z) + 2 exactly (the half-trace convention x=2X)."""
    X, Y, Z = sp.symbols("X Y Z")
    diff = sp.expand(kappa_poly(2*X, 2*Y, 2*Z) - (4 * fricke_vogt(X, Y, Z) + 2))
    return diff == 0


def verify_trace_maps_preserve_invariants():
    """Full-trace map F(x,y,z)=(xy-z,x,y) preserves kappa; half-trace map T(X,Y,Z)=(2XY-Z,X,Y) preserves I_FV."""
    x, y, z = sp.symbols("x y z")
    F = (x*y - z, x, y)
    full_ok = sp.expand(kappa_poly(*F) - kappa_poly(x, y, z)) == 0
    X, Y, Z = sp.symbols("X Y Z")
    T = (2*X*Y - Z, X, Y)
    half_ok = sp.expand(fricke_vogt(*T) - fricke_vogt(X, Y, Z)) == 0
    return full_ok, half_ok


# ---------------------------------------------------------------------------------------------------------------------
# S2 -- the metallic monodromies ARE the SL(2,Z) mapping-class action
# ---------------------------------------------------------------------------------------------------------------------

def verify_metallic_trace_symbolic():
    """tr(R^m L^m) = m^2+2 and det = 1, symbolic in m (using R^m=[[1,0],[m,1]], L^m=[[1,m],[0,1]])."""
    m = sp.symbols("m")
    Rm = sp.Matrix([[1, 0], [m, 1]])
    Lm = sp.Matrix([[1, m], [0, 1]])
    W = Rm * Lm
    return sp.expand(W.trace() - (m**2 + 2)) == 0, sp.expand(W.det() - 1) == 0


def verify_dehn_twists_preserve_kappa():
    """The mapping-class Dehn twists tau_a:(x,y,z)->(x,z,xz-y), tau_b:(x,y,z)->(z,y,yz-x) preserve kappa."""
    x, y, z = sp.symbols("x y z")
    ta = (x, z, x*z - y)
    tb = (z, y, y*z - x)
    a_ok = sp.expand(kappa_poly(*ta) - kappa_poly(x, y, z)) == 0
    b_ok = sp.expand(kappa_poly(*tb) - kappa_poly(x, y, z)) == 0
    return a_ok, b_ok


def verify_markov_slice_and_two_states():
    """On kappa=-2, (x,y,z)=(3p,3q,3r) gives exactly the Markov equation p^2+q^2+r^2=3pqr. Both (3,3,3) and (0,0,0)
    lie on kappa=-2 (a 2-dim surface containing the Markov tree AND the Q8 point -- not a single point)."""
    p, q, r = sp.symbols("p q r")
    on_edge = sp.expand(kappa_poly(3*p, 3*q, 3*r) + 2)           # = 9(p^2+q^2+r^2) - 27pqr
    markov_ok = sp.expand(on_edge / 9 - (p**2 + q**2 + r**2 - 3*p*q*r)) == 0
    k_markov_root = int(kappa_poly(3, 3, 3))                      # -2
    k_q8_point = int(kappa_poly(0, 0, 0))                         # -2
    return markov_ok, k_markov_root, k_q8_point


# ---------------------------------------------------------------------------------------------------------------------
# S3 -- invariant data of the metallic monodromies (what a class-S comparison must reproduce)
# ---------------------------------------------------------------------------------------------------------------------

def verify_eigenvalue_is_metallic_squared():
    """The top eigenvalue of R^m L^m equals (metallic mean)^2, lambda_m = (m+sqrt(m^2+4))/2."""
    m = sp.symbols("m", positive=True)
    lam_plus = ((m**2 + 2) + m * sp.sqrt(m**2 + 4)) / 2          # larger root of lam^2-(m^2+2)lam+1=0
    metallic_sq = ((m + sp.sqrt(m**2 + 4)) / 2)**2
    return sp.simplify(lam_plus - metallic_sq) == 0


def verify_fixed_slopes():
    """The boundary fixed slopes of R^m L^m on RP^1 are the roots of t^2 + m t - 1 = 0 (Mobius fixed points
    c t^2 + (d-a) t - b = 0 for W=[[a,b],[c,d]])."""
    m = sp.symbols("m", positive=True)
    t = sp.symbols("t")
    W = sp.Matrix([[1, m], [m, m**2 + 1]])                       # = R^m L^m
    a, b, c, d = W[0, 0], W[0, 1], W[1, 0], W[1, 1]
    fixed = c * t**2 + (d - a) * t - b                           # = m t^2 + m^2 t - m
    monic = sp.expand(fixed / m)
    return sp.expand(monic - (t**2 + m*t - 1)) == 0


def _squarefree(n):
    sf = 1
    for prime, exp in sp.factorint(n).items():
        if exp % 2 == 1:
            sf *= prime
    return sf


def metallic_trace_fields(mmax=6):
    """Reduced eigenvalue/trace field Q(sqrt(m^2+4)): square-free part of the discriminant tr^2-4 = m^2(m^2+4)."""
    out = []
    for m in range(1, mmax + 1):
        disc_unreduced = m * m * (m * m + 4)                     # tr^2 - 4 = (m^2+2)^2 - 4
        sf = _squarefree(m * m + 4)                              # field is Q(sqrt(squarefree(m^2+4)))
        hyperbolic = (m * m + 2) > 2
        out.append({"m": m, "trace": m*m + 2, "hyperbolic": hyperbolic,
                    "disc_unreduced": disc_unreduced, "field_radicand": sf})
    return out


# ---------------------------------------------------------------------------------------------------------------------

def run_all():
    r = {}
    r["S1_fricke_commutator"] = verify_fricke_commutator()
    r["S1_kappa_eq_4I_plus_2"] = verify_kappa_4I_plus_2()
    r["S1_full_trace_map_preserves_kappa"], r["S1_half_trace_map_preserves_I"] = verify_trace_maps_preserve_invariants()
    r["S2_trace_m2plus2"], r["S2_det_one"] = verify_metallic_trace_symbolic()
    r["S2_tau_a_preserves_kappa"], r["S2_tau_b_preserves_kappa"] = verify_dehn_twists_preserve_kappa()
    markov_ok, k333, k000 = verify_markov_slice_and_two_states()
    r["S2_markov_slice"] = markov_ok
    r["S2_markov_root_on_edge"] = (k333 == -2)
    r["S2_q8_point_on_edge"] = (k000 == -2)
    r["S2_two_distinct_states_share_edge"] = (k333 == -2 and k000 == -2)
    r["S3_eigenvalue_metallic_squared"] = verify_eigenvalue_is_metallic_squared()
    r["S3_fixed_slopes"] = verify_fixed_slopes()
    fields = metallic_trace_fields()
    r["S3_all_hyperbolic"] = all(row["hyperbolic"] for row in fields)
    r["S3_fields_reduced_m1_m4_share_5"] = (fields[0]["field_radicand"] == 5 and fields[3]["field_radicand"] == 5)
    return r, fields


def main():
    print("=" * 100)
    print("B148 -- kappa/Fricke-Vogt identity + metallic monodromy = SL(2,Z) MCG action (INDEPENDENT re-derivation)")
    print("=" * 100)
    print("\nFIREWALL: everything below is MATH about the tower's symmetry. kappa is scale-free; it CANNOT source a")
    print("physical energy density without an externally supplied scale. Nothing here is a physics-magnitude result.\n")

    r, fields = run_all()
    width = max(len(k) for k in r)
    for k, v in r.items():
        print(f"  {k:<{width}} : {'OK' if v else 'FAIL'}")

    print("\n[metallic monodromy invariant data -- what a class-S comparison must reproduce]")
    print("   m | tr=m^2+2 | hyperbolic | disc(tr^2-4)=m^2(m^2+4) | reduced field")
    for row in fields:
        print(f"   {row['m']} | {row['trace']:>7} | {str(row['hyperbolic']):>10} | {row['disc_unreduced']:>22} | "
              f"Q(sqrt{row['field_radicand']})")

    all_ok = all(r.values())
    print("\n" + ("ALL CHECKS PASS." if all_ok else "SOME CHECKS FAILED."))
    print("\nBANKED (verified): S1 kappa=4I+2 (half-trace convention) + Fricke identity; S2 metallic monodromies = the")
    print("SL(2,Z) mapping-class action (Dehn twists preserve kappa), kappa=-2 = the Markov surface, the Markov root")
    print("(3,3,3) and the Q8 point (0,0,0) are two distinct orbits on that surface; S3 hyperbolic, eigenvalue =")
    print("(metallic mean)^2, fixed slopes = roots of t^2+mt-1, reduced field Q(sqrt(m^2+4)) (m=1,4 share Q(sqrt5)).")
    print("OPEN (reading/proof, NOT sandbox): the class-S coincidence question (the one mathematically-tractable")
    print("direction) and the firewall confirmation (the decisive physics-boundary check). See FINDINGS sections 4.A/4.B.")
    return all_ok


if __name__ == "__main__":
    import sys
    sys.exit(0 if main() else 1)
