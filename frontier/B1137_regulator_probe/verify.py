"""STEP 3 (b) -- exact verification + within-1sigma resolution for a candidate PSLQ relation.

A "candidate" is an integer vector c = [c0, c1..cD, c_reg...] (aligned with [1, V, V^2,..,V^D,
<basis keys in order>]) such that c . vec ~ 0 at the search precision. This module:
  1. Rejects any candidate whose V-power coefficients (c1..cD) are ALL zero (a pure regulator/
     constant identity -- uninformative about V; see basis_hygiene_check.py for why these occur).
  1b. ALSO rejects any candidate whose regulator/constant coefficients are ALL zero -- i.e. a bare
     relation between '1' and V alone (e.g. c0 + c1*V = 0). Found empirically (2026-08-22, real
     grid run): because V is represented in the search at its OWN truncated digit budget (a
     terminating decimal), it is ALWAYS trivially rational, so PSLQ trivially "discovers" this at
     essentially every cell for every low-digit target (worst case: delta_CP digits=0 truncates to
     "4.0", PSLQ instantly returns c0=4,c1=-1; m_s/m_d digits=1 truncates to "20", same story) --
     this says nothing whatsoever about the regulators and must not count as a candidate. This is
     the SAME hygiene issue as the V-free regulator identities, mirrored: a relation is only
     evidence about "is V algebraic over the regulator field" if it involves BOTH V and >=1
     regulator/constant.
  2. Re-evaluates the residual at a BOOSTED precision (dps_search + BOOST) using freshly computed
     regulators (not cached low-precision ones) -- a candidate whose residual does not shrink
     in proportion to the extra precision is a numerical artifact, not a relation (STEP 3 "not
     residual alone").
  3. Solves the (degree <= 3) polynomial in V implied by the relation (c0+K_reg) + c1 V + c2 V^2
     + c3 V^3 = 0 for its real roots at high precision, and reports whether the target's measured
     central value lies within its stated 1-sigma of the nearest real root.
"""
from mpmath import mp, mpf, polyroots, workdps

BOOST = 120  # extra digits for the exact-verification re-check, beyond the search dps

def involves_V(coeffs, D):
    return any(c != 0 for c in coeffs[1:1 + D])

def involves_regulator(coeffs, D):
    return any(c != 0 for c in coeffs[1 + D:])

def coefficient_height(coeffs):
    return max(abs(c) for c in coeffs)

def height_aware_ok(residual, dps_search, maxh, n_dim, margin=20):
    """Item (a): coefficient-height-aware threshold (E25). The precision genuinely 'spent'
    resolving a height-H, n-dim relation is ~ n_dim*log10(H); what's left over must still show
    a decisively small residual, not just 'small at face value'."""
    if residual == 0:
        return True, float('inf')
    spent = n_dim * mp.log(max(maxh, 2), 10)
    resid_digits = -mp.log(abs(residual), 10)
    slack = resid_digits - spent
    return bool(slack > margin), float(slack)

def exact_reverify(coeffs, basis_keys, dps_search, get_vec_at_dps, D):
    """Recompute vec (regulators+V-powers) at dps_search+BOOST via get_vec_at_dps(dps) and check
    the SAME integer relation's residual shrinks correspondingly (stability under precision)."""
    dps_hi = dps_search + BOOST
    with workdps(dps_hi + 20):
        vec_hi = get_vec_at_dps(dps_hi, D)
        resid_hi = sum(mpf(coeffs[i]) * vec_hi[i] for i in range(len(coeffs)))
        resid_hi_digits = float('inf') if resid_hi == 0 else float(-mp.log(abs(resid_hi), 10))
    # a genuine relation's residual at the boosted precision should be commensurate with dps_hi
    # (i.e. within a healthy constant of dps_hi digits); an artifact will show a residual stuck
    # near where it was at the ORIGINAL search precision (did not shrink with the extra digits).
    stable = resid_hi_digits > (dps_search + BOOST * 0.5)
    return stable, resid_hi_digits

def solve_for_V_roots(coeffs, D, K_reg, dps):
    """coeffs[0]=c0 (const '1' coeff), coeffs[1..D]=c1..cD (V-power coeffs). Solve
    c_D x^D + ... + c1 x + (c0 + K_reg) = 0 for real roots at working precision `dps`."""
    with workdps(dps + 20):
        poly = [mpf(coeffs[D - i]) for i in range(D)] + [mpf(coeffs[0]) + K_reg]
        # mpmath polyroots wants highest degree first; poly currently [c_D,...,c1, (c0+K_reg)]
        if all(c == 0 for c in poly[:-1]):
            return []
        try:
            roots = polyroots(poly, maxsteps=200, extraprec=400)
        except Exception:
            return []
        real_roots = [r.real for r in roots if abs(r.imag) < mpf(10) ** (-(dps // 2))]
        return real_roots

def within_1sigma(roots, V_central, rel_unc):
    if not roots:
        return False, None, None
    Vc = mpf(V_central)
    sigma_abs = abs(Vc) * mpf(rel_unc) if Vc != 0 else mpf(rel_unc)
    best = min(roots, key=lambda r: abs(r - Vc))
    dev = abs(best - Vc)
    ok = dev <= sigma_abs if sigma_abs > 0 else dev == 0
    return bool(ok), best, (float(dev / sigma_abs) if sigma_abs > 0 else None)
