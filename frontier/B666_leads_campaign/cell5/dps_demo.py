"""Cell 5 (R21-11): the mechanism, isolated — no pytest, no test-file edits.

theta_chain_blockscalar_residual() and hyperelliptic_certificate() compute at
RUNTIME under the ambient global mp.mp.dps. geometric_theta sets dps=100 at
import; the b353 locks need it. Any later global assignment (the full suite's
post-collection value is 40, from test_cc2_r5_adopted.py line 282) starves them.
"""
import pathlib
import sys

import mpmath as mp

REPO = pathlib.Path(_REPO + "")
sys.path.insert(0, str(REPO / "frontier" / "B353_geometric_theta_identification"))
from geometric_theta import EXPONENTS, SIGN, theta_chain_blockscalar_residual, hyperelliptic_certificate  # noqa: E402  (sets dps=100 at import)
import os
_REPO = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", ".."))

for dps in (100, 40, 30):
    mp.mp.dps = dps
    rA = theta_chain_blockscalar_residual()
    verdictA = "PASS" if rA < mp.mpf(10) ** -60 else "FAIL"
    worst = mp.mpf(0)
    for m in EXPONENTS:
        _lam, resid = hyperelliptic_certificate(m)
        worst = max(worst, resid)
    verdictC = "PASS" if worst < mp.mpf(10) ** -40 else "FAIL"
    print(f"dps={dps:3d}: blockscalar residual = {mp.nstr(rA, 6):>12s} (<1e-60? {verdictA}) | "
          f"worst hyperelliptic resid = {mp.nstr(worst, 6):>12s} (<1e-40? {verdictC})")
