"""The web seat's disclosure check (exploration tier, labelled). At B1825's least-chi2_ten address -- line (3/8, 3/8),
tau = 0.093359375 + 2.742578125i, direction DR, radius L_2, readings S~ for up and down (B1825's run.json key
[(3/8, 3/8), "0", "1", "6"]) -- the corner ratio |V_ub|/|V_td| and |V_ud| with a singlet component a0 I added to the
Higgs's internal orientation (S = a0 I + h.Q, before the reading, as S289's singlet_higgs_scan2.py does), at the natural
magnitude a0 = c sqrt(h.h) over main's twelve phases c = exp(2 pi i k/12), in five families:
  odd (up -a0, down +a0: main's opposite-sign family, FRAMING_LEDGER section D), even (both +a0), up only, down only,
  and a quarter turn between the sectors (up i a0, down a0).
A Higgs with det S = a0^2 + h.h = 0 in either sector is null (B1659's J4) and is reported, not ranked.
No measured value is read by this script, but its address was chosen with the ten (B1825's least chi2_ten), so any
comparison of its output with nature is post hoc there. Data-free in what it computes.

Usage: python3 singlet_at_the_address.py <main checkout>   (main at 0f3e71a24)
"""
import cmath
import contextlib
import io
import math
import pathlib
import sys
from fractions import Fraction as Fr

import numpy as np

sys.dont_write_bytecode = True
ROOT = pathlib.Path(sys.argv[1]).resolve()
sys.path.insert(0, str(ROOT / "frontier" / "B1821_the_frames_mirror_symmetry_in_re_tau" / "verification"))
with contextlib.redirect_stdout(io.StringIO()):
    import cm_zero_line as Z
    B = Z.mods()["B"]
CHARGES = {sn: (ql, qr) for sn, ql, qr in Z.SECTORS}
tau = complex(0.093359375, 2.742578125); line = (Fr(3, 8), Fr(3, 8))
with contextlib.redirect_stdout(io.StringIO()):
    L = Z.radii(tau)[1]
    h = np.array(Z.direction("DR", tau))
    M = {}
    for sn in ("up", "down"):
        ql, qr = CHARGES[sn]
        w = B.line_w(line[0], line[1], tau); x, y = B.sector_twists(w, tau, ql, qr)
        R = B.residues(x, y, tau); c = B.cA(x, y, tau, R)
        u = {k: (math.sqrt(2 * math.pi * L + c[k]) * R[k] if c[k] is not None and 2 * math.pi * L + c[k] > 0 else 0) for k in B.UNITS}
        M[sn] = B.weighted_M(u)
hh = complex(h @ h); nat = cmath.sqrt(hh); hn2 = float(sum(abs(v) ** 2 for v in h))


def S_of(a0):
    return a0 * np.eye(2) + h[0] * B.QI + h[1] * B.QJ + h[2] * B.QK


def U_of(sn, a0):
    S = B.EPS @ S_of(a0).conj() @ B.EPS.T                  # the reading S~ (up and down at this address)
    u_, s, _ = np.linalg.svd(B.coupling(S, M[sn])); o = np.argsort(s)
    return u_[:, o]


def corner(au, ad):
    V = np.abs(U_of("up", au).conj().T @ U_of("down", ad))
    return V[0, 2] / V[2, 0], V[0, 0]


def null(a0):
    return abs(np.linalg.det(S_of(a0))) < 1e-9 * hn2


print("B1825's address: L_2 = %.6f, |h.h| / |h|^2 = %.3e" % (L, abs(hh) / hn2))
r0, v0 = corner(0, 0)
print("no singlet: |V_ub|/|V_td| = %.3f, |V_ud| = %.4f" % (r0, v0))
PH = [cmath.exp(2j * math.pi * k / 12) for k in range(12)]
FAM = {"odd (up -a0, down +a0)": lambda a: (-a, a), "even (both +a0)": lambda a: (a, a),
       "up only": lambda a: (a, 0), "down only": lambda a: (0, a), "quarter turn (up i a0, down a0)": lambda a: (1j * a, a)}
for name, f in FAM.items():
    rows = []
    for k, c in enumerate(PH):
        au, ad = f(c * nat)
        if null(au) or null(ad):
            rows.append((k, None, None)); continue
        rows.append((k,) + corner(au, ad))
    live = [r for r in rows if r[1] is not None]
    print("%-32s non-null phases %2d: |V_ub|/|V_td| %.3f-%.3f, below 1 at %2d; |V_ud| %.3f-%.3f; null at k = %s"
          % (name, len(live), min(r[1] for r in live), max(r[1] for r in live), sum(r[1] < 1 for r in live),
             min(r[2] for r in live), max(r[2] for r in live), [r[0] for r in rows if r[1] is None]))
print("per phase k (c = exp(2 pi i k/12)), |V_ub|/|V_td|:")
for name, f in FAM.items():
    out = []
    for k, c in enumerate(PH):
        au, ad = f(c * nat)
        out.append("  null" if (null(au) or null(ad)) else "%6.3f" % corner(au, ad)[0])
    print("  %-32s %s" % (name, " ".join(out)))
