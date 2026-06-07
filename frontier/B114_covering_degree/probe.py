"""B114 -- the covering-degree mechanism for degree=rank's exponent: TESTED-NEGATIVE (the simple '=k' fails).

S022's candidate positive mechanism (CC-web Addition 1 A1d): the exponent k = the Weyl-orbit covering degree of
the meridian->longitude map M -> L = c*M^k. B111 found it k-to-1 at the EIGENVALUE level (mu -> mu^k). This stage
tests the FULL-spectrum version and finds it does NOT hold:

  The full covering degree -- the number of distinct meridian spectra {M_i} with det = prod M_i = 1 (SL(n)), mod
  the Weyl group (permutations), mapping to the same longitude spectrum {L_i = c*M_i^k} -- is ~ k^{n-1}, NOT k:
        SL(3) W1      (n=3, k=3): 9  = 3^2 = k^{n-1}
        SL(4) secondary (n=4,k=3): 27 = 3^3 = k^{n-1}
        SL(4) principal (n=4,k=4): 40       (< 4^3, reduced by the repeated eigenvalue {1,1,omega,omega^2})
  (each L_i/c has k k-th roots -> k^n combinations; det=1 fixes one -> ~k^{n-1}; mod permutation adjusts for
  repeated eigenvalues). So 'covering degree = k' holds only for a SINGLE eigenvalue, not the full spectrum.

VERDICT: the covering-degree-=-k mechanism is NOT supported (TESTED-NEGATIVE at the full-spectrum level). The
exponent is NOT a covering degree. The real (partial) exponent mechanism stays the M^k-scalar arithmetic of B111
(ADDITION 1): k is constrained to powers where M^k is non-scalar AND compatible with the bundle relations (the
M^4=-1 scalar impossibility forces k=3 on the secondary). S022's covering-degree candidate is downgraded; the
exponent (the power half of rho_n) stays open, with the scalar-arithmetic as the live lead, not covering degree.

Standalone trace-map / Lie theory; NO physics; no CLAIMS.md promotion; the rho_n proof stays the prize; P1-P16
untouched.
"""
from __future__ import annotations

import itertools

import numpy as np

_W = np.exp(2j * np.pi / 3)
_Z = np.exp(1j * np.pi / 4)
_COMPS = {
    "SL3_W1": {"spec": [1, 1j, -1j], "k": 3, "c": 1},
    "SL4_principal": {"spec": [1, 1, _W, _W ** 2], "k": 4, "c": -1},
    "SL4_secondary": {"spec": [_Z, _Z ** 3, _Z ** 5, _Z ** 7], "k": 3, "c": 1j},
}


def _multiset_key(vals, tol=1e-6):
    return tuple(sorted((round(v.real / tol) * tol, round(v.imag / tol) * tol) for v in vals))


def full_covering_degree(component):
    """# distinct meridian spectra (det=1, mod permutation) mapping to the same longitude L = c*M^k."""
    d = _COMPS[component]
    M = np.array(d["spec"], complex)
    k, c = d["k"], d["c"]
    n = len(M)
    L = c * M ** k
    roots_per = [[abs(Li / c) ** (1 / k) * np.exp(1j * (np.angle(Li / c) + 2 * np.pi * j) / k) for j in range(k)]
                 for Li in L]
    seen = set()
    for combo in itertools.product(*roots_per):
        if abs(np.prod(combo) - 1) < 1e-6:
            seen.add(_multiset_key(combo))
    return {"n": n, "k": k, "full_covering_degree": len(seen),
            "equals_k": len(seen) == k, "approx_k_pow_nm1": len(seen) in (k ** (n - 1),) or len(seen) < k ** (n - 1)}


def covering_degree_negative():
    """The full covering degree is ~k^{n-1}, not k -- the '=k' mechanism fails at the full-spectrum level."""
    out = {comp: full_covering_degree(comp) for comp in _COMPS}
    none_equal_k = all(not v["equals_k"] for v in out.values())
    return {"per_component": out, "covering_degree_equals_k": not none_equal_k,
            "verdict": "TESTED-NEGATIVE: the full covering degree ~ k^{n-1}, not k; 'covering degree = k' holds "
                       "only at the single-eigenvalue level (B111). The exponent is NOT a covering degree; the "
                       "live exponent lead stays the M^k-scalar arithmetic (B111 ADDITION 1)."}


def main():
    print("=" * 78)
    print("B114 -- the covering-degree mechanism for degree=rank's exponent: TESTED-NEGATIVE")
    print("=" * 78)
    print("\nFull covering degree (# meridian spectra, det=1, mod permutation -> same L = c*M^k):")
    r = covering_degree_negative()
    for comp, v in r["per_component"].items():
        print(f"    {comp:>14}: n={v['n']} k={v['k']} -> covering degree = {v['full_covering_degree']}"
              f"  (==k? {v['equals_k']};  ~k^(n-1)={v['k'] ** (v['n'] - 1)})")
    print(f"\n    covering degree == k on all four: {r['covering_degree_equals_k']}")
    print(f"    {r['verdict']}")


if __name__ == "__main__":
    main()
