"""
Frontier probe B5 — Wheeler-DeWitt constraint, and a Lambda estimate that
overlaps DEAD work.

  SPECULATIVE FRONTIER WORK. Outputs are *logged observations*, not claims.
  See ../../GOVERNANCE.md sec. 5 and ./README.md.

This probe is recorded mainly to DOCUMENT a dead-adjacent path, so that it is
not silently re-attempted (cf. docs/ARCHIVE.md, dead claims D1 and D2).

Run:  python frontier/B5_wheeler_dewitt/probe.py
"""

import sympy as sp

from origin_axiom.constants import VOL_FIG8


def main():
    print("=" * 72)
    print("Frontier probe B5 -- Wheeler-DeWitt constraint & a dead-adjacent Lambda")
    print("SPECULATIVE: observations only, not claims (GOVERNANCE.md sec. 5)")
    print("=" * 72)

    r = sp.symbols("r")
    sols = sp.solve(r**2 - r - 1, r)
    print("\n[1] The H = 0 (Hamiltonian) constraint reduces to  r^2 - r - 1 = 0.")
    print(f"    solutions: {sols}   (phi and -1/phi)")
    print("    NOTE: r^2 - r - 1 = 0 is the golden-ratio fixed-point equation")
    print("    already present throughout the proven core (it is chi_A up to")
    print("    relabeling). This reproduces known structure; nothing new.")

    lam = 2 * sp.pi**2 / VOL_FIG8
    print(f"\n[2] Lambda = 2*pi^2 / Vol(4_1) = {float(lam):.4f}   (Planck units)")
    print("    This is ~10^120 times the observed cosmological constant.")
    print("    It does NOT resolve the cosmological-constant problem, and it sits")
    print("    squarely adjacent to the DEAD claims D1 (k = 137) and")
    print("    D2 (Lambda = phi^-2N). See docs/ARCHIVE.md.")

    print("\n[verdict]  See README.md. B5 documents a dead-adjacent path so it is")
    print("not silently re-attempted. No claim; O5 remains open.")


if __name__ == "__main__":
    main()
