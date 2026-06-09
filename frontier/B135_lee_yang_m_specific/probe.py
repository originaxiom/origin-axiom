"""B135 -- the Lee-Yang bridge is m=1-specific (not a metallic family); the match is at modular-data level.

Phase D of the approved program (the Lee-Yang physics push), done honestly + firewalled. B132/S8 + S030 established
that at level k=3 the sigma_3 Galois conjugate of the SU(2)_3 even part (Fibonacci) gives the Yang-Lee / M(2,5) data
(d_tau = -1/phi). Phase D asks: is there a metallic FAMILY of Lee-Yang realizations across m, and at what level does
the m=1 match actually hold? Re-derived in-sandbox (verify-don't-trust).

ONE-LINE RESULT. The Lee-Yang bridge is m=1-SPECIFIC: only the golden mean lambda_1 = phi < 2 is a quantum dimension
(2cos(pi/(k+2)) < 2 forces m=1); for m>=2, lambda_m > 2, so there is NO metallic family of Lee-Yang CFTs. The metallic
*family* is the family of distinct aperiodic SPECTRAL objects (K010, trace field Q(sqrt(m^2+4))), NOT a family of
Lee-Yang minimal models. The single golden bridge (m=1 -> M(2,5)) is real at MODULAR-DATA level (fusion rule + quantum
dimension + S-matrix Galois conjugate + central charge), stronger than fusion-rule-only -- but it is emergent
non-equilibrium physics (the Lee-Yang edge), firewalled from fundamental physics.

MATH + emergent-physics tier (POSTULATED). Nothing to CLAIMS.md; P1-P16, B85, S031, the merged B124-B134 untouched.

  ============================================================================================================
  RESULTS:
    D1  m-specificity: lambda_m = (m + sqrt(m^2+4))/2 < 2 ONLY for m=1 (golden = 2cos(pi/5)). m>=2: lambda_m > 2,
        not a 2cos(pi/(k+2)) quantum dimension -> no Lee-Yang/minimal-model realization. So NO metallic family of
        Lee-Yang CFTs; the bridge is the single golden case. (Re-confirms B127/M-3 in the Lee-Yang framing.)
    D2  the m=1 match at MODULAR-DATA level: the sigma_3 Galois conjugate (zeta5 -> zeta5^3) of the Fibonacci MTC
        (1, tau; tau^2 = 1+tau; d_tau = phi) is the Yang-Lee MTC (d_tau = -1/phi); the rank-2 S-matrix
        S = (1/sqrt(1+d^2))[[1,d],[d,-1]] Galois-conjugates Fib -> Yang-Lee; central charges Fibonacci (G2)_1
        c = +14/5 -> Yang-Lee M(2,5) c = -22/5 (c_eff = c - 24 h_min = 2/5). Standard data (R3 audit: Jeffrey 1992,
        Dong-Lin-Ng 2015, Lawrence-Zagier 1999); the framework supplies the fusion rule + the golden dimension.
    D3  HONEST CALIBRATION of S030: the match is at the level of {fusion rule, quantum dimension, S-matrix Galois
        conjugate, central charge} -- NOT a full RCFT identification (no torus partition-function / full character
        match; the framework's object is the hyperbolic, non-unitary complex-CS quantization, related to M(2,5) via
        the quantum dimension/fusion, not a proven RCFT equality). So S030 stays TESTED-POSITIVE but scoped to
        modular-data level, m=1-specific, emergent.
"""
from __future__ import annotations

import numpy as np

PHI = (1 + np.sqrt(5)) / 2


def m_specificity(mmax=6):
    rows = {}
    for m in range(1, mmax + 1):
        lam = (m + np.sqrt(m * m + 4)) / 2
        rows[m] = {"lambda": round(float(lam), 4), "is_quantum_dim": bool(lam < 2)}
    return {"rows": rows, "only_m1_is_quantum_dim": all(rows[m]["is_quantum_dim"] == (m == 1) for m in rows),
            "note": "lambda_m<2 iff m=1 -> Lee-Yang/minimal-model realization is m=1-specific; no metallic CFT family."}


def fibonacci_vs_yang_lee():
    out = {}
    for name, sig in (("fibonacci", 1), ("yang_lee", 3)):
        d = np.sin(sig * 2 * np.pi / 5) / np.sin(sig * np.pi / 5)
        D = 1 + d * d
        S = np.array([[1, d], [d, -1]]) / np.sqrt(D)
        out[name] = {"d_tau": round(float(d), 4), "S": np.round(S, 4).tolist(),
                     "S4_is_identity": bool(np.allclose((S @ S) @ (S @ S), np.eye(2), atol=1e-9))}
    out["galois_phi_to_minus_inv_phi"] = bool(abs(out["fibonacci"]["d_tau"] - PHI) < 1e-3 and
                                              abs(out["yang_lee"]["d_tau"] + 1 / PHI) < 1e-3)
    out["central_charges"] = {"fibonacci_G2_1": "+14/5", "yang_lee_M(2,5)": "-22/5", "c_eff_M25": "2/5"}
    out["match_level"] = "fusion rule + quantum dimension + S-matrix Galois conjugate + central charge (modular-data); " \
                         "NOT a full RCFT identification (no torus partition-function match). m=1-specific, emergent."
    return out


def main():
    print("=" * 96)
    print("B135 -- the Lee-Yang bridge is m=1-specific; the m=1 match is at modular-data level")
    print("=" * 96)
    ms = m_specificity()
    print("\n[D1 m-specificity (lambda_m<2 iff m=1 -> no metallic Lee-Yang family)]")
    for m, r in ms["rows"].items():
        print(f"    m={m}: lambda={r['lambda']:.4f}  quantum_dim={r['is_quantum_dim']}")
    print("    only_m1:", ms["only_m1_is_quantum_dim"])
    fy = fibonacci_vs_yang_lee()
    print("\n[D2 Fibonacci -> Yang-Lee (sigma_3 Galois conjugate, MTC level)]")
    print("    d_tau: Fibonacci", fy["fibonacci"]["d_tau"], "-> Yang-Lee", fy["yang_lee"]["d_tau"],
          "(phi -> -1/phi:", fy["galois_phi_to_minus_inv_phi"], ")")
    print("    central charges:", fy["central_charges"])
    print("\n[D3 honest calibration]", fy["match_level"])
    print("\nThe Lee-Yang edge is the m=1 (golden) realization; the metallic family is SPECTRAL (K010), not CFT.")


if __name__ == "__main__":
    main()
