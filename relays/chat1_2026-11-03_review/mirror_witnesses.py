"""The web seat's check for its review of main's S286-S290 (data-free; no measured value read).

P-555's mirror rule (S288: "closed for the CKM"; DESIGN_NOTE: "cannot lift it"). The rule moves the down sector to the
mirror address A* = (-conj tau, (alpha, -b)), keeping direction, radius and reading. Here, with main's own probe
(B1827's mirror_rule_probe.sector_U, unchanged), at three witness addresses found by a seeded search in the review:
the frame's corner ratio |V_ub|/|V_td| and |V_ud|, with and without the rule, and the six's ratios, which the rule keeps.
Both readings are S~ (equal readings); the radius is L_max; the direction is DR.

Usage: python3 mirror_witnesses.py <main checkout>   (main at e1e3c6c2f)
"""
import contextlib
import io
import pathlib
import sys
from fractions import Fraction as F

import numpy as np

sys.dont_write_bytecode = True
ROOT = pathlib.Path(sys.argv[1]).resolve()
sys.path.insert(0, str(ROOT / "frontier" / "B1827_the_framing_ledger" / "verification" / "scans"))
with contextlib.redirect_stdout(io.StringIO()):
    import mirror_rule_probe as P
Z = P.Z

WITNESSES = [
    ((F(3, 5), F(0)), complex(0.11592687814754127, 3.4107846907123225)),
    ((F(10, 11), F(9, 11)), complex(0.07590429990567782, 3.632748057635097)),
    ((F(2, 5), F(0)), complex(0.4927638787201879, 3.142598707760312)),
]

print("direction DR, radius L_max, readings S~ (up) and S~ (down)")
for line, tau in WITNESSES:
    with contextlib.redirect_stdout(io.StringIO()):
        L = Z.radii(tau)[0]
        Uu, su = P.sector_U(tau, line, "DR", L, 1, "up")
        Ud, sd = P.sector_U(tau, line, "DR", L, 1, "down")
        Um, sm = P.sector_U(complex(-tau.real, tau.imag), (line[0], -line[1]), "DR", L, 1, "down")
    print("line (%s, %s), tau %.6f%+.6fi, L_max %.6f" % (line[0], line[1], tau.real, tau.imag, L))
    for name, V in (("frame ", Uu.conj().T @ Ud), ("mirror", Uu.conj().T @ Um)):
        A = np.abs(V)
        print("   %s |V_ub|/|V_td| %7.3f  |V_ud| %.4f  |V_us| %.4f  |V_cb| %.4f" % (name, A[0, 2] / A[2, 0], A[0, 0], A[0, 1], A[1, 2]))
    print("   up m2/m3 %.3e m1/m3 %.3e | down m2/m3 %.3e m1/m3 %.3e | mirror-down kept to %.1e (relative)"
          % (su[1] / su[2], su[0] / su[2], sd[1] / sd[2], sd[0] / sd[2], float(np.max(np.abs(sm / sm[2] - sd / sd[2])))))
    hier = all(s[1] / s[2] < 0.1 and 1e-12 < s[0] / s[2] < 0.01 for s in (su, sd))
    steeper = su[1] / su[2] < sd[1] / sd[2] / 2 and su[0] / su[2] < sd[0] / sd[2]
    print("   main's filters (mirror_rule_structure2): both hierarchical %s; up steeper than down %s" % (hier, steeper))
