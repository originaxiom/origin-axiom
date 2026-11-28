"""The six-move slow rate at mod 125 is 2 sqrt(6 + sqrt 5), a root of x^4 - 48 x^2 + 496 (minimal over Q).
The value is B2015's, read from its run on main (origin/main; the copy of that file beside this script when git is not
at hand).
    python3 -B rate125.py            (the claim)
    python3 -B rate125.py --control  (the polynomial x^4 - 48 x^2 + 495: it must not vanish at the value)"""
import re, sys, subprocess, pathlib
import sympy as sp
HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[1]
r = subprocess.run(["git", "-C", str(ROOT), "ls-tree", "-r", "--name-only", "origin/main", "frontier/"],
                   capture_output=True, text=True)
path = [p for p in r.stdout.split() if p.startswith("frontier/B2015_") and p.endswith("rate_law_run.txt")]
txt = subprocess.run(["git", "-C", str(ROOT), "show", "origin/main:" + path[0]], capture_output=True, text=True).stdout \
    if path else ""
if not txt:
    txt = next(HERE.glob("frontier/B2015_*/verification/rate_law_run.txt")).read_text()
v = float(re.search(r"mod 125 \(M = 5\): [^\n]*?\(double\) ([0-9.]+)", txt).group(1))
x = sp.Symbol("x"); P = x**4 - 48 * x**2 + (495 if "--control" in sys.argv else 496)
print("DECISIVE: value read:", v); print("P(value) = %.3e" % float(P.subs(x, v))); print("P irreducible over Q:", sp.Poly(P, x).is_irreducible)
if abs(float(P.subs(x, v))) < 1e-9 and sp.Poly(P, x).is_irreducible:
    print("DECISIVE: the rate at mod 125 is 2 sqrt(6 + sqrt 5), minimal polynomial x^4 - 48 x^2 + 496")
else:
    sys.exit(1)
