"""Diagnostic: raw reflection-term values for RRL (base 12) across kappa,
plus fit against sqrt(3) (the possibly-ambient A2 content) vs sqrt(12)
(=2 sqrt(3), same test) to understand contamination, and compare against
identity/rotation ('other') terms as a control.
"""
import sys
sys.path.insert(0, "/private/tmp/claude-501/-Users-dri-origin-axiom/06195d53-d92a-477a-b1cb-cccccca43ae9/scratchpad/cellA")
from scan import weil_ops, rho_weil, WEYL, REFL, fit_sqrt

for kap in [3, 4, 6, 7, 8, 9, 10, 11, 12, 16, 20, 24]:
    T, S, perms, n = weil_ops(kap)
    M = rho_weil("RRL", T, S)
    print(f"--- kap={kap} n={n} ---")
    for (pm, wi), (P, sg) in perms.items():
        v = complex(__import__("numpy").trace(M @ P))
        tag = "REFL" if wi in REFL else ("id " if wi == 0 else "rot")
        f3 = fit_sqrt(v.real, 3) or fit_sqrt(v.imag, 3)
        print(f"  {tag} pm={pm:+d} wi={wi} sign={sg:+d}  v={v:.6f}  "
              f"sqrt3fit={f3}")
