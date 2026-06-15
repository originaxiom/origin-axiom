"""B153 -- the rank-stratified degeneration of degree=rank (figure-eight SL(n) bundle).

RESULT (campaign synthesis; see FINDINGS.md): the figure-eight degree=rank relation
L=(-1)^{n-1} M^n is realized on a genuine character-variety COMPONENT at n=3, degenerates to a
measure-zero SLICE at n=4, and is ABSENT (reducible principal holonomy) at n=5.

This probe reproduces the DETERMINISTIC, fast facts via the validated toolkit (sln_toolkit.py):
  - n=4 {1,1,w,w^2}: L=-M^4 exact, irreducible, A-free tangent 19 => SLICE (B89 + round-2);
  - n=5 {1,1,1,-1,-1} semisimple: A^2=I => B=tAt^-1 is an involution (B^2=I) for ANY t
    => <A,B> dihedral => every SL(5) rep reducible (a proof; the semisimplicity-gap fill).
The n=3 spectrum-rigid component (L=+M^3) and the n=5 non-semisimple absence are NUMERICAL /
Sage results documented in FINDINGS.md (n=4 slice is additionally confirmed EXACTLY over Q(w);
n=3 has 2 components dims 3,5 over Q(i) -- both via Sage).

Run:  python frontier/B153_degree_rank_degeneration/probe.py
Standalone low-dim topology / invariant theory; nothing to CLAIMS.md.
"""
from __future__ import annotations
import os, sys
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sln_toolkit as tk


def check_n4_slice():
    """B89 n=4: L=-M^4, irreducible, A-free tangent 19 (slice)."""
    w = np.exp(2j * np.pi / 3)
    t12, t21, t22, s = 1.3 + 0.2j, 0.7 - 0.1j, 0.9 + 0.4j, 0.5 + 0.3j
    D = np.diag([w, w ** 2]); T = np.array([[w * t22, t12], [t21, t22]]); P = -D @ T
    R = np.array([[t12 * t21 * (w + 1) - t22 ** 2, s],
                  [s * t21 / t12, t22 ** 2 + w * (t22 ** 2 - t12 * t21)]])
    t = np.block([[P, np.eye(2)], [R, T]]); A = np.diag([1, 1, w, w ** 2]).astype(complex)
    (n, res), _ = tk.relation_exponent(A, t)
    tr = tk.tangent_report(A, t)
    irr = tk.is_irreducible(A, tk.Bfrom(A, t))
    ok = (n == 4 and res < 1e-9 and irr and tr["tangent_dim"] == 19 and tr["trA_moves_in_SL"])
    print(f"n=4 {{1,1,w,w2}}: L=-M^4 (res {res:.1e}), irreducible={irr}, "
          f"tangent={tr['tangent_dim']}, spectrum_moves={tr['trA_moves_in_SL']}  -> SLICE  [{'OK' if ok else 'FAIL'}]")
    return ok


def check_n5_semisimple_dihedral():
    """n=5 semisimple {1,1,1,-1,-1}: A^2=I => B=tAt^-1 involution => dihedral => reducible."""
    A = np.diag([1, 1, 1, -1, -1]).astype(complex)
    a2I = np.allclose(A @ A, np.eye(5))
    rng = np.random.default_rng(0)
    t = rng.standard_normal((5, 5)) + 1j * rng.standard_normal((5, 5))
    B = tk.Bfrom(A, t)                       # = A^-2 t A t^-1 = t A t^-1 since A^2=I
    binv = np.allclose(B @ B, np.eye(5))     # B is an involution for ANY t
    ok = a2I and binv
    print(f"n=5 {{1,1,1,-1,-1}} semisimple: A^2=I={a2I}, B^2=I={binv} (B=tAt^-1 involution) "
          f"=> <A,B> dihedral => reducible  [{'OK' if ok else 'FAIL'}]")
    return ok


def main():
    print("B153 -- rank-stratified degeneration of degree=rank (figure-eight)\n")
    ok = []
    ok.append(check_n4_slice())
    ok.append(check_n5_semisimple_dihedral())
    print("\nDegeneration (campaign synthesis):")
    print("  n=3 {1,i,-i}    : L=+M^3 on a spectrum-RIGID component   (EXACT over F_p (3 primes): geometric")
    print("                     (dim-5) comp tangent 11/rigid/irred;   reducible slice tangent 10; Falbel [lit.])")
    print("  n=4 {1,1,w,w2}  : L=-M^4 on a SLICE only                  (exact over Q(w): tangent 29/kernel 19)")
    print("  n=5 {1,1,1,-1,-1}: NOT realized on irreducibles           (ss reducible PROVEN; non-ss irreducibles")
    print("                     EXIST but degree=rank fails on them    -- corrected 2026-06-15, see n5_nonss_irreducible.py)")
    print("\nselftest:", "PASS" if all(ok) else "FAIL")
    tk._selftest()
    return 0 if all(ok) else 1


if __name__ == "__main__":
    sys.exit(main())
