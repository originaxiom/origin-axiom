#!/usr/bin/env python3
"""e18 (data-free; P-139, input to main's P-327; follows e17): the record's contents' cusp coefficients at EVERY cusp of
the fit's lines, not only at infinity.  On a twisted line the potential is invariant only under the line's stabilizer, so
it has many cusps p/r, and it can run to any of them.  Labelled exploration; committed before its run, output committed
before it was read.

At the cusp p/r (gcd(p, r) = 1) the shrinking cycle is the lattice vector k(-p, r), so a characteristic (p1, p2)
contributes, at that cusp, through x = -p p1 + r p2 (mod 1) in place of e17's p1 (at infinity, (p, r) = (-1, 0) gives
x = p1).  The contents and their characteristics are B1686's, as in e17, with B1728's twist q(alpha, b) on the line
(alpha, b) in the S_c convention (B1728's (q alpha, 2 q b) in the theta functions' convention, whose second entry is read
mod 2):
  the Higgs's three copies: p + 3(alpha, b), p in {(1/2,0), (0,1/2), (1/2,1/2)}, weight 2 each;
  the matter: 45 Weyl fermions in rho_Q, each -2 x the comb, whose characteristics (a/2, b/2) with weight -1/2 and
  (a/4, b/4) with weight 1/4 are shifted by q(alpha, b);
  gauge 48 and graviton 9 (neutral: the same at every cusp).
Checks: (C1) at (p, r) = (-1, 0) every line reproduces e17's totals; (C2) without a line the comb's coefficient is
-31/512 at every cusp (rho_Q's shrinking holonomy has eigenvalues +-i at every primitive cycle).
The cusps: every primitive (p, r) with 0 <= r <= 40 and -40 <= p <= 40, one of each sign pair.
    python3 -B e18_every_cusp_of_the_fit_lines.py      # writes e18_every_cusp_of_the_fit_lines_out.txt and .json"""
import json, math, pathlib
from fractions import Fraction as Fr

HERE = pathlib.Path(__file__).resolve().parent


def B6(x):
    return x ** 6 - 3 * x ** 5 + 2.5 * x ** 4 - 0.5 * x ** 2 + 1 / 42


def kappa(x):
    return 84 * B6(float(x % 1))


FIELDS = [("Q", 1, 6), ("u^c", -4, 3), ("d^c", 2, 3), ("L", -3, 2), ("e^c", 6, 1)]
PAR = [(Fr(1, 2), Fr(0)), (Fr(0), Fr(1, 2)), (Fr(1, 2), Fr(1, 2))]
COMB = [((Fr(a, 2), Fr(b, 2)), -0.5) for a in range(2) for b in range(2)] + [((Fr(a, 4), Fr(b, 4)), 0.25) for a in range(4) for b in range(4)]
GAUGE, GRAV = 48.0, 9.0


def x_at(ch, p, r):
    return (-p * ch[0] + r * ch[1]) % 1


def comb_at(shift, p, r):
    return sum(w * kappa(x_at((c[0] + shift[0], c[1] + shift[1]), p, r)) for c, w in COMB)


def contents(line, p, r):
    al, b = line
    mt = sum(-2 * 3 * n * comb_at((q * al, q * b), p, r) for _, q, n in FIELDS)
    h = sum(2 * kappa(x_at((pp[0] + 3 * al, pp[1] + 3 * b), p, r)) for pp in PAR)
    return {"(d) matter alone": mt, "(a) matter + Higgs": mt + h, "(b) + gauge": mt + h + GAUGE, "(c) + graviton": mt + h + GAUGE + GRAV}


CUSPS = []
for r in range(0, 41):
    for p in range(-40, 41):
        if math.gcd(p, r) != 1:
            continue
        if r == 0 and p != -1:
            continue
        CUSPS.append((p, r))
out, res = [], {}
c2 = sorted({round(comb_at((Fr(0), Fr(0)), p, r), 12) for p, r in CUSPS})
out.append(f"C2 the comb without a line, over {len(CUSPS)} cusps: distinct values {c2} (-31/512 = {-31/512:.12f})")
FIT = [(Fr(2, 5), Fr(k, 10)) for k in range(10)]
for line in FIT + [(Fr(1, 2), Fr(1, 2)), (Fr(0), Fr(1, 2)), (Fr(3, 10), Fr(1, 10))]:
    inf = contents(line, -1, 0)
    rows = [(p, r, contents(line, p, r)) for p, r in CUSPS]
    rec = {"line": [str(line[0]), str(line[1])], "at infinity": inf}
    for key in ("(d) matter alone", "(a) matter + Higgs", "(b) + gauge"):
        vals = [(c[key], p, r) for p, r, c in rows]
        mx = max(vals); mn = min(vals)
        npos = sum(1 for v, _, _ in vals if v > 0)
        rec[key] = {"max": mx[0], "max at p/r": f"{mx[1]}/{mx[2]}", "min": mn[0], "min at p/r": f"{mn[1]}/{mn[2]}", "cusps positive": npos}
    res[f"({line[0]}, {line[1]})"] = rec
    a = rec["(a) matter + Higgs"]; d = rec["(d) matter alone"]
    out.append(f"line ({line[0]}, {line[1]}): at infinity (a) {inf['(a) matter + Higgs']:.4f}, (d) {inf['(d) matter alone']:.4f}; "
               f"(a) over all cusps: max {a['max']:.4f} at {a['max at p/r']}, min {a['min']:.4f} at {a['min at p/r']}, positive at {a['cusps positive']} of {len(CUSPS)}; "
               f"(d): max {d['max']:.4f} at {d['max at p/r']}, positive at {d['cusps positive']}; "
               f"(b) positive at {rec['(b) + gauge']['cusps positive']}")
(HERE / "e18_every_cusp_of_the_fit_lines_out.txt").write_text("\n".join(out) + "\n")
(HERE / "e18_every_cusp_of_the_fit_lines.json").write_text(json.dumps(res, indent=1))
print("written")
