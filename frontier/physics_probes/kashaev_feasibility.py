"""Feasibility probe for S027 (quantum modularity of the metallic Kashaev invariants) -- the figure-eight Kashaev
invariant is a CHEAP finite sum whose asymptotic recovers the hyperbolic volume (the SL(2)/4_1 complex-CS partition
function). This grounds the HEAVY fork S027: the computation is in-house feasible; the open part is the quantum-
MODULAR cocycle (Zagier-Garoufalidis) and the metallic-family extension.

Phase 3 of the physics-bridge sweep (heavy forks, mapped + feasibility). FIREWALLED; 1D / low-dim topology, NOT
fundamental physics; nothing to CLAIMS.md; the physics chapter stays CLOSED; P1-P16 untouched. The continuous
metallic family-in-m is DEAD as a moduli family (Gate 1, V32-34); this fork targets the arithmetic / modular cocycle
of the INDIVIDUAL invariants, not a moduli family.
"""
from __future__ import annotations

import numpy as np

VOL_FIG8 = 2.029883212819307     # vol(4_1) = 2.0298832... (the figure-eight hyperbolic volume)


def kashaev_fig8(N):
    """The Kashaev invariant <4_1>_N = sum_{k=0}^{N-1} |(q)_k|^2, q = exp(2 pi i / N), (q)_k = prod (1-q^j).
    A cheap finite sum (the colored-Jones at the root of unity / the complex-CS partition function)."""
    q = np.exp(2j * np.pi / N)
    total, poch = 0.0, 1.0 + 0j
    for k in range(N):
        total += abs(poch) ** 2
        poch *= (1 - q ** (k + 1))
    return total


def volume_conjecture(Ns=(50, 100, 200, 400, 800)):
    """The volume conjecture: (2 pi / N) log <4_1>_N -> vol(4_1). The asymptotic converges (slowly, from above) to
    the hyperbolic volume -- the feasibility witness that the Kashaev / complex-CS computation is in-house."""
    rows = []
    for N in Ns:
        J = kashaev_fig8(N)
        growth = (2 * np.pi / N) * np.log(J)
        rows.append({"N": N, "growth": round(float(growth), 5), "vol": VOL_FIG8,
                     "err": round(abs(growth - VOL_FIG8), 4)})
    # the trend is monotone-decreasing toward the volume (log-slow convergence)
    errs = [r["err"] for r in rows]
    return {"rows": rows, "monotone_toward_vol": bool(all(errs[i] > errs[i + 1] for i in range(len(errs) - 1))),
            "feasible": bool(errs[-1] < errs[0]),
            "note": "the Kashaev sum is a cheap finite computation; (2pi/N)log J_N -> vol(4_1) (slow, from above). "
                    "The complex-CS partition function of 4_1 is in-house. OPEN (S027): the quantum-modular cocycle "
                    "(Zagier-Garoufalidis) + the metallic-family extension (the arithmetic, not a moduli family -- "
                    "the continuous family-in-m is DEAD, Gate 1)."}


def main():
    print("=" * 78)
    print("Kashaev feasibility (S027) -- the figure-eight Kashaev invariant -> volume conjecture")
    print("=" * 78)
    vc = volume_conjecture()
    for r in vc["rows"]:
        print(f"    N={r['N']:>4}: (2pi/N)log<4_1>_N = {r['growth']:.5f}  (vol={r['vol']:.5f}, err {r['err']:.4f})")
    print(f"\n  monotone toward vol: {vc['monotone_toward_vol']}; feasible (err shrinks): {vc['feasible']}")
    print(f"  {vc['note']}")


if __name__ == "__main__":
    main()
