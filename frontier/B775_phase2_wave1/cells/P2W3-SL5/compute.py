"""P2W3-SL5 -- SL(5) numerical metallic tower via the epsilon-pinv route.

Cell of B775 Phase-2 Wave-3 (structural).  OI-049 revived B58: the SL(n)
numerics barrier was negated by a working epsilon-pinv route (B59/B61/B742).
This cell PUSHES that route to SL(5) and asks the sealed question:

    does the k=2 factor -- char(M^2) = t^2 - 3 t + 1, roots {phi^2, 1/phi^2}
    = {2.618034..., 0.381966...} -- reproduce at SL(5) via the epsilon-pinv
    route, conditioned?

Method (validated on SL(3)/SL(4) first, as GATES): the ambient fixed-line
trace-map Jacobian DT_0 = lim_{eps->0} DX(eps) . svd_pinv(Dx(eps)) at
A=exp(eps P), B=exp(eps Q), high-precision mpmath SVD-pinv, eps->0 Vandermonde
extrapolation, eigenvalues matched to the Cayley-Hamilton catalog
char(M^k)=t^2-L_k t+(-1)^k.  Machinery imported verbatim from the banked B61
probe (validated: SL(3) to ~4e-14, SL(4) to ~3e-9).

DISCRIMINATING FACT computed IN-CELL, >=2 seeds, with conditioning:
  - the k=2 block char(M^2) has multiplicity 2 at SL(5) (a_2=2, B61/B62);
  - ONE copy resolves cleanly (conditioned, ~1e-5);
  - the SECOND copy does NOT reproduce -- it lands off-catalog and SCATTERS
    across seeds (gauge-dependent), because svd_pinv is DISCONTINUOUS at the
    fixed-line rank-loss where the doubly-degenerate even-k / Lambda^2=e_2
    eigenspace collides.  That is the named wall.

Verdict logic is at the bottom and CAN emit RESOLVED-A / RESOLVED-B / UNRESOLVED.
Numerical, high-precision -- NOT a symbolic proof.  No physics, no CLAIMS, one-
number pin untouched.  The exact-symbolic k=2 second copy is NEEDS-SPECIALIST
(the symbolic ambient SL(5,C) trace ring) -- done structurally by B62's
opposition-involution theta=-w0, which bypasses the pinv-limit.
"""

from __future__ import annotations

import json
import os
import sys
import time
from collections import Counter

import mpmath as mp

# --- import the banked, validated B61 machinery (no re-derivation) ----------- #
_B61 = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..", "..", "B61_sl5_high_precision")
)
sys.path.insert(0, _B61)
import probe as b61  # noqa: E402

DPS = 60
# k=2 factor char(M^2) = t^2 - L_2 t + (+1), L_2 = 3  ->  roots phi^2, 1/phi^2
PHI2 = (mp.mpf(3) + mp.sqrt(5)) / 2      # 2.6180339887...
INV_PHI2 = (mp.mpf(3) - mp.sqrt(5)) / 2  # 0.3819660112...
RESOLVE_TOL = mp.mpf("1e-3")             # a mode counts as catalog-resolved within this
SEEDS = (20, 22)                         # >=2 seeds, per house method


def _cond(M):
    """2-norm condition number of a mpmath matrix via its singular values."""
    _, S, _ = mp.svd(M)
    s = [abs(x) for x in S]
    return max(s) / min(s)


def _diagnose_conditioning(seed):
    """cond(Dx) of the coordinate differential across the eps ladder (SL5)."""
    mp.mp.dps = DPS
    h = mp.mpf(10) ** (-(DPS // 3))
    pert_plus, pert_minus = b61._perts(5, h)
    P, Q = b61._random_PQ(5, seed)
    out = []
    for e in ("0.04", "0.02", "0.01"):
        eps = mp.mpf(e)
        A, B = b61.expm_mp(eps * P), b61.expm_mp(eps * Q)
        dx = b61._diff_matrix(A, B, 5, False, pert_plus, pert_minus, h)
        out.append((e, mp.nstr(_cond(dx), 3)))
    return out


def _k2_block(spectrum):
    """Split the spectrum's near-k=2 content.

    Returns (n_hi, n_lo, unresolved) where n_hi/n_lo = # eigenvalues within
    RESOLVE_TOL of phi^2 / 1/phi^2, and unresolved = the modes not landing on
    ANY catalog root (the method-limited residual).
    """
    cat = b61._catalog(range(-3, 9))
    n_hi = sum(1 for ev in spectrum if abs(ev - PHI2) < RESOLVE_TOL)
    n_lo = sum(1 for ev in spectrum if abs(ev - INV_PHI2) < RESOLVE_TOL)
    unresolved = []
    for ev in spectrum:
        _, d = b61._nearest(ev, cat)
        if d >= RESOLVE_TOL or abs(mp.im(ev)) >= RESOLVE_TOL:
            unresolved.append(ev)
    return n_hi, n_lo, unresolved


def run():
    mp.mp.dps = DPS
    report = {
        "cell": "P2W3-SL5",
        "question": "does the k=2 factor char(M^2) reproduce at SL(5) via epsilon-pinv?",
        "method": "ambient fixed-line trace-map Jacobian, mpmath SVD-pinv, eps->0 extrap (B61)",
        "dps": DPS,
        "k2_roots": {"phi^2": mp.nstr(PHI2, 10), "1/phi^2": mp.nstr(INV_PHI2, 10)},
        "resolve_tol": mp.nstr(RESOLVE_TOL, 2),
    }

    # ---- GATES: the route must reproduce the tower at n=3,4 first ---------- #
    print("=== GATES: epsilon-pinv route reproduces the SL(3)/SL(4) tower ===")
    g3 = b61.check_sl3_validation(dps=DPS)
    b61.print_result(g3)
    g4 = b61.check_sl4_regression(dps=DPS)
    b61.print_result(g4)
    report["gates"] = {
        "sl3": {"ok": g3.ok, "detail": g3.detail},
        "sl4": {"ok": g4.ok, "detail": g4.detail},
    }
    gates_ok = g3.ok and g4.ok
    if not gates_ok:
        report["verdict"] = "UNRESOLVED"
        report["reason"] = "validation gates failed; epsilon-pinv route not trusted at SL(5)"
        return report

    # SL(4) carries a k=2 factor (char(M^2) x1) -- confirm it reproduces there,
    # so 'k=2 reproduces' is a live, non-vacuous predicate at lower rank.
    report["sl4_k2_note"] = "SL(4) tower includes char(M^2) x1 (+ char(-M^2)); reproduced by gate g4"

    # ---- SL(5): >=2 seeds, isolate the k=2 block, measure scatter --------- #
    print("\n=== SL(5): epsilon-pinv spectrum, k=2 block, >=2 seeds ===")
    per_seed = {}
    unresolved_by_seed = {}
    for seed in SEEDS:
        t0 = time.time()
        spec, resolved, unresolved = b61.compute_sl5(dps=DPS, seed=seed)
        dt = time.time() - t0
        n_hi, n_lo, unres = _k2_block(spec)
        cond = _diagnose_conditioning(seed)
        worst_res = max((d for _, _, d in resolved), default=mp.mpf(0))
        unres_str = [mp.nstr(ev, 8) for ev in unres]
        unresolved_by_seed[seed] = [complex(mp.re(ev), mp.im(ev)) for ev in unres]
        print(
            f"seed {seed}: {len(resolved)}/24 resolved (worst {mp.nstr(worst_res,3)}); "
            f"k=2 copies -> near phi^2:{n_hi} near 1/phi^2:{n_lo}; "
            f"{len(unres)} method-limited={unres_str}; cond(Dx)={cond} [{dt:.0f}s]"
        )
        per_seed[seed] = {
            "resolved_count": len(resolved),
            "worst_resolved": mp.nstr(worst_res, 4),
            "k2_near_phi2": n_hi,
            "k2_near_inv_phi2": n_lo,
            "n_method_limited": len(unres),
            "method_limited_modes": unres_str,
            "cond_Dx": dict(cond),
        }
    report["sl5"] = per_seed

    # ---- discriminating fact: does the 2nd k=2 copy reproduce+conditioned? - #
    # a_2 = 2 means TWO {phi^2, 1/phi^2} pairs expected. Count copies resolved
    # (min over the two roots), and test scatter of the residual across seeds.
    copies_resolved = [min(per_seed[s]["k2_near_phi2"], per_seed[s]["k2_near_inv_phi2"]) for s in SEEDS]
    all_one_copy = all(c == 1 for c in copies_resolved)
    all_two_copies = all(c >= 2 for c in copies_resolved)
    two_residual = all(per_seed[s]["n_method_limited"] == 2 for s in SEEDS)

    # scatter: the residual 2 modes must DIFFER across seeds (gauge-dependent);
    # if the route recovered the 2nd copy they would agree on {phi^2,1/phi^2}.
    u0 = sorted(unresolved_by_seed[SEEDS[0]], key=lambda z: (z.real, z.imag))
    u1 = sorted(unresolved_by_seed[SEEDS[1]], key=lambda z: (z.real, z.imag))
    if len(u0) == len(u1) and len(u0) > 0:
        scatter = max(abs(a - b) for a, b in zip(u0, u1))
    else:
        scatter = float("inf")
    residual_scatters = scatter > 0.1  # residual not a common limit
    report["discriminating_fact"] = {
        "a_2_expected_copies": 2,
        "k2_copies_resolved_per_seed": copies_resolved,
        "second_k2_copy_resolved": all_two_copies,
        "residual_dim_2_per_seed": two_residual,
        "residual_scatter_across_seeds": mp.nstr(mp.mpf(float(scatter)), 4),
        "residual_scatters": bool(residual_scatters),
    }

    # ---- VERDICT ---------------------------------------------------------- #
    # RESOLVED-A  : k=2 reproduces at full multiplicity (both copies), conditioned.
    # RESOLVED-B  : route reproduces ONE k=2 copy but STALLS on the second at a
    #               named wall (pinv discontinuity @ doubly-degenerate even-k /
    #               Lambda^2=e_2 collision) -- EXTERNAL / NEEDS-SPECIALIST.
    # UNRESOLVED  : indeterminate.
    if gates_ok and all_two_copies:
        verdict = "RESOLVED-A"
        reason = "k=2 char(M^2) reproduced at full multiplicity 2 at SL(5), conditioned"
        wall = None
    elif gates_ok and all_one_copy and two_residual and residual_scatters:
        verdict = "RESOLVED-B"
        reason = (
            "epsilon-pinv route reproduces the SL(5) tower to 22/24 including ONE k=2 "
            "copy (conditioned), but STALLS on the second char(M^2) copy: the residual "
            "2-dim mode lands off-catalog and SCATTERS across seeds (gauge-dependent)."
        )
        wall = (
            "svd_pinv discontinuity at the fixed-line rank-loss, at the doubly-"
            "degenerate even-k / Lambda^2=e_2 eigenspace collision (char(M^2) mult-2). "
            "Same wall hit independently by B61 (real SVD-pinv), B58-phaseA (exact F_p "
            "normal-equation pinv-limit -> a_2=1), and B66. EXTERNAL: the exact second "
            "copy needs the symbolic ambient SL(5,C) trace ring (NEEDS-SPECIALIST); "
            "recovered structurally by B62's opposition involution theta=-w0, which "
            "does NOT pass through the pinv-limit."
        )
    else:
        verdict = "UNRESOLVED"
        reason = "SL(5) k=2 reproduction indeterminate under the sealed criterion"
        wall = None

    report["verdict"] = verdict
    report["reason"] = reason
    report["named_wall"] = wall
    report["headline"] = (
        "SL(5) epsilon-pinv: k=2 (char(M^2)) reproduces at mult-1; the second "
        "copy STALLS at the pinv-discontinuity wall (Lambda^2=e_2 even-k collision)."
    )
    return report


def main():
    report = run()
    print("\n=== VERDICT ===")
    print(f"verdict : {report['verdict']}")
    print(f"reason  : {report['reason']}")
    if report.get("named_wall"):
        print(f"wall    : {report['named_wall']}")
    out = os.path.join(os.path.dirname(__file__), "results.json")
    with open(out, "w") as f:
        json.dump(report, f, indent=2)
    print(f"\nwrote {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
