"""W177 post hoc 1 (labelled; after the output 603b22a21 was read): N3's 80 failing points (Im tau 24, the 2/11 lines,
s = 1, 2) recomputed with the committed script's own functions at 120 digits, to see whether the remainder after
c-infinity and the leading correction falls under the rule's bound once the working precision resolves it."""
import contextlib, io, json, sys
from fractions import Fraction as Fr
from pathlib import Path
D = Path(sys.argv[1]).resolve()
sys.path.insert(0, str(D)); sys.dont_write_bytecode = True
with contextlib.redirect_stdout(io.StringIO()):
    import the_twisted_norms_closed as W177
mp = W177.mp
rows = json.loads((D / "the_twisted_norms_closed.json").read_text())["N3 the first correction"]["rows"]
fails = [r for r in rows if not r[-1]]
mp.mp.dps = 120
out, worst = [], mp.mpf(0)
for r in fails:
    a, b = (Fr(v) for v in r[0].split(","))
    sign, s, x, y = r[1], r[2], Fr(r[3]), r[4]
    tau = mp.mpc(mp.mpf(x.numerator) / x.denominator, y)
    w = mp.mpf(a.numerator) / a.denominator * tau + mp.mpf(b.numerator) / b.denominator
    c, cinf, lead, lp, lm = W177.c_series(s, sign * 3 * w, tau, parts=True)
    rem = abs(c - cinf - lead)
    bound = 10 * max(mp.exp(-4 * mp.pi * y * lp) / lp, mp.exp(-4 * mp.pi * y * lm) / lm)
    worst = max(worst, rem / bound)
    out.append([r[0], sign, s, r[3], y, mp.nstr(rem, 6), mp.nstr(bound, 6), mp.nstr(rem / bound, 6), bool(rem <= bound)])
print(json.dumps({"points": len(out), "all within": all(o[-1] for o in out), "worst remainder/bound": mp.nstr(worst, 6),
                  "rows": out[:6]}, indent=1))
