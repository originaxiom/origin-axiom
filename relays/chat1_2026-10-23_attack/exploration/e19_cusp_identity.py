#!/usr/bin/env python3
"""e19 (data-free; follows e17 and e18): the identity behind e18, checked on every line.  At the cusp p/r the line
(alpha, b) acts exactly as a line with first entry alpha' = -p alpha + r b (mod 1) acts at infinity, because the comb's
characteristics spread evenly over Z/4 and Z/2 at every cusp and the Higgs copies' parity parts are always {0, 1/2, 1/2}.
  I1  for all 266 of B1713's lines and the 1 960 cusps of e18: |contents(line, p, r) - totals(alpha')|, largest;
  I2  every line has a cusp with alpha' = 0 (the line invisible there), where B1686's untwisted totals apply;
  I3  the alpha' classes met by order-5 and order-10 lines, with the sign of matter + Higgs at each;
  I4  the lowest matter + Higgs over alpha' in (1/840)Z and over a fine real grid (the gauge fields add +48).
Uses e17's and e18's own functions (imported from their committed files).  Labelled exploration; committed before its
run, output committed before it was read.
    python3 -B e19_cusp_identity.py      # writes e19_cusp_identity_out.txt"""
import importlib.util, io, contextlib, math, pathlib, sys
from fractions import Fraction as Fr

HERE = pathlib.Path(__file__).resolve().parent


def _load(name):
    spec = importlib.util.spec_from_file_location(name, HERE / f"{name}.py"); mod = importlib.util.module_from_spec(spec)
    src = (HERE / f"{name}.py").read_text()
    # run only the definitions: cut each script before its first output-producing block
    cut = {"e17_cusp_coefficients_on_lines": "# K1\n", "e18_every_cusp_of_the_fit_lines": "CUSPS = []\n"}[name]
    code = src.split(cut)[0]
    exec(compile(code, str(HERE / f"{name}.py"), "exec"), mod.__dict__)
    return mod


e17 = _load("e17_cusp_coefficients_on_lines")
e18 = _load("e18_every_cusp_of_the_fit_lines")
src17 = (HERE / "e17_cusp_coefficients_on_lines.py").read_text()
exec(compile(src17.split("rows = []")[0].split("# the 266 lines")[1], "e17-lines", "exec"), e17.__dict__)   # _lines, LINES

CUSPS = []
for r in range(0, 41):
    for p in range(-40, 41):
        if math.gcd(p, r) != 1:
            continue
        if r == 0 and p != -1:
            continue
        CUSPS.append((p, r))
out = []
worst, worst_at = 0.0, None
has_zero = 0
classes = {5: {}, 10: {}}
KEY = "(a) matter + Higgs"
for N, a, b in e17.LINES:
    zero = False
    for p, r in CUSPS:
        ap = (-p * a + r * b) % 1
        c = e18.contents((a, b), p, r)
        t = e17.totals(ap)
        d = max(abs(c[k] - t[k]) for k in c)
        if d > worst:
            worst, worst_at = d, (str(a), str(b), p, r)
        if ap == 0:
            zero = True
        if N in classes:
            classes[N][ap] = t[KEY]
    has_zero += zero
out.append(f"I1 largest |contents at p/r - totals(alpha')| over {len(e17.LINES)} lines x {len(CUSPS)} cusps: {worst:.3e} (at {worst_at})")
out.append(f"I2 lines with a cusp where alpha' = 0: {has_zero} of {len(e17.LINES)}; there matter alone {e17.totals(0)['(d) matter alone']:.3f}, "
           f"matter + Higgs {e17.totals(0)[KEY]:.3f}, + gauge {e17.totals(0)['(b) + gauge']:.3f}, + graviton {e17.totals(0)['(c) + graviton']:.3f}")
for N in (5, 10):
    cl = sorted(classes[N].items(), key=lambda kv: kv[0])
    pos = [str(k) for k, v in cl if v > 0]; neg = [str(k) for k, v in cl if v < 0]
    out.append(f"I3 order-{N} lines meet alpha' classes {[str(k) for k, _ in cl]}; matter + Higgs positive at {pos}, negative at {neg}")
lo = min((e17.totals(Fr(k, 840))[KEY], k) for k in range(840))
lo_real = min(e17.totals(x / 20000)[KEY] for x in range(20000))
out.append(f"I4 lowest matter + Higgs over alpha' in (1/840)Z: {lo[0]:.4f} at {Fr(lo[1], 840)}; over a 1/20000 grid: {lo_real:.4f}; the gauge fields add +48")
(HERE / "e19_cusp_identity_out.txt").write_text("\n".join(out) + "\n")
print("written")
