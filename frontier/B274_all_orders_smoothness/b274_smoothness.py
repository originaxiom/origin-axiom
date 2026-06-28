"""B274 result encoding (pyenv-importable). Heavy computation: b274_smoothness_modp.py (sage-python, exact mod p).
FIREWALLED; nothing to CLAIMS.md.

VERDICT (exact, mod p=99991 & 100003, both agree): rho_prin is a SMOOTH point of the E6 character variety of the
figure-eight, of dimension 6 = rank(E6) -- so the {4,8} E6-irreducible flat connections (B265) exist UNCONDITIONALLY
(all orders), upgrading B273's "to second order".

  route (b), the boundary/cusp closer (cited Heusener-Porti / Menal-Ferrer-Porti criterion + computed hypotheses):
    dim H^1(M,e6)=6, dim H^2(M,e6)=6, meridian holonomy regular (ker(ad e)=6=rank), dim H^1(dM,e6)=12=2*rank,
    restriction injective (half-lives-half-dies, B270 per-block) => smooth point of dim 1/2*12 = 6.
  route (a), independent in-sandbox corroboration: the cubic (3rd-order) obstruction [q3] in H^2 vanishes for all 6
    exponent directions AND a generic combination (q3 a nonzero cochain but a coboundary; invariant under the
    eta-indeterminacy). A nonzero cubic would have REFUTED smoothness; it does not.
"""
EXPONENTS = [1, 4, 5, 7, 8, 11]
PRIMES = [99991, 100003]

CERTS = {"H1M": 6, "H2M": 6, "merid_regular": 6, "H0_boundary": 6, "H1_boundary": 12}
RESULT = {
    99991: {**CERTS, **{f"cubic_exp{m}": True for m in EXPONENTS},
            "cubic_generic": True, "generic_o2_zero": True, "generic_q3_nonzero": True, "cubic_generic_eta_shifted": True},
    100003: {**CERTS, **{f"cubic_exp{m}": True for m in EXPONENTS},
             "cubic_generic": True, "generic_o2_zero": True, "generic_q3_nonzero": True, "cubic_generic_eta_shifted": True},
}


def boundary_criterion_holds():
    """MFP smoothness signature: dim H1(M)=6, H1(dM)=2*rank=12, meridian regular (=rank), for every recorded prime."""
    for p in PRIMES:
        r = RESULT[p]
        if not (r["H1M"] == 6 and r["merid_regular"] == 6 == r["H0_boundary"] and r["H1_boundary"] == 12):
            return False
    return True


def cubic_obstruction_vanishes():
    """3rd-order obstruction = 0 for all directions + generic (non-vacuously, eta-invariant), every prime."""
    for p in PRIMES:
        r = RESULT[p]
        if not all(r[f"cubic_exp{m}"] for m in EXPONENTS):
            return False
        if not (r["cubic_generic"] and r["generic_o2_zero"] and r["generic_q3_nonzero"] and r["cubic_generic_eta_shifted"]):
            return False
    return True


def smooth_point_unconditionally():
    """Both independent routes agree => rho_prin is a smooth point => existence is unconditional (all orders)."""
    return boundary_criterion_holds() and cubic_obstruction_vanishes()


if __name__ == "__main__":
    print("B274 verdict: rho_prin a smooth point of X_E6(4_1) (all orders):", smooth_point_unconditionally())
    print("  boundary/MFP criterion:", boundary_criterion_holds(), "| cubic obstruction vanishes:", cubic_obstruction_vanishes())
    print("  => E6-irreducible flat connections (B265) exist UNCONDITIONALLY. Reproduce: sage-python b274_smoothness_modp.py")
