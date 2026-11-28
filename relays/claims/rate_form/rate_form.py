"""The six-move slow rate r at the five levels run (B2015's R1, read from its committed output) against polynomials in
c = cos(pi/M) of degree 1 to 3 with rational coefficients.  An exact form is accepted at a residual below 1e-10.
    python3 -B rate_form.py            (the claim)
    python3 -B rate_form.py --control  (r replaced by 1 + 2c: a fit must be found, and the NEGATIVE line must not print)"""
import re, sys, pathlib
import numpy as np
ROOT = pathlib.Path(__file__).resolve().parent
txt = next(ROOT.glob("frontier/B2015_*/verification/rate_law_run.txt")).read_text()
pts = [(int(M), float(v)) for M, v in re.findall(r"\(M = (\d+)\): [^\n]*?\(double\) ([0-9.]+)", txt)]
M = np.array([m for m, _ in pts]); c = np.cos(np.pi / M)
r = 1 + 2 * c if "--control" in sys.argv else np.array([v for _, v in pts])
print("levels' M:", list(M)); print("r:", list(r))
best = None
for deg in (1, 2, 3):
    V = np.vander(c, deg + 1); coef, *_ = np.linalg.lstsq(V, r, rcond=None); res = float(np.abs(V @ coef - r).max())
    print("DECISIVE: degree %d: largest residual %.3e" % (deg, res))
    if res < 1e-10 and best is None:
        best = (deg, coef)
if best:
    print("fit found: degree %d, coefficients %s" % (best[0], np.round(best[1], 12)))
    sys.exit(1)
else:
    print("DECISIVE: NEGATIVE: the six-move slow rate is not a polynomial in cos(pi/M) of degree <= 3; the rate is not a function of "
          "cos(pi/M) alone")
