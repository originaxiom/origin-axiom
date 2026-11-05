"""S301 verifier B, check T41 (value-free; main's code and first principles).

Theorem 41 (agy, c5c9236df) claims a 'data-free' selection of the slope alpha = 2/5 by three conditions:
  C1  R_1^{up}(alpha tau) == 0   (coded: 5 p = 0 mod N)
  C2  down-lepton congruence (1, 2) = (6, -3) mod N   (coded: N | 5)
  C3  Delta E_up(alpha) != Delta E_down(alpha)   (variant: Delta E_up > Delta E_down)
with Delta E_s the WITHIN-sector gap of main's channel-exponent law (LAW_MAP, B1832 S300).

FIREWALL: only within-sector gaps are computed or printed.  The inter-sector exponent (dominant down minus dominant up),
which Theorem 41's part 3 states, is never computed here; absolute per-sector exponents are never printed (only
rule-vs-numeric deviations, as main's c2 does).

Checks:
 (a) exact within-sector gaps on 1/5 and 2/5 (= LAW_MAP);
 (b) over ALL reduced slopes p/N in (0, 1/2], N <= 60: how many pass C3 alone, the '>' variant alone, C1, C2, and
     the conjunction; whether C1 and C2 are the same condition;
 (c) R_1^{up} on the line through 0 on main's residues: its true zero set (B1832 section 1.2: R_1 <-> X +- Y in the
     lattice) against the lane's 'C1 <=> 3 alpha not in Z and 5 alpha in Z';
 (d) the gap rule validated numerically on main's residues at seven further slopes (within-sector only).
"""
import math, pathlib, sys
from fractions import Fraction as F
import numpy as np

ROOT = pathlib.Path(__file__).resolve().parents[5]
sys.path.insert(0, str(ROOT / "frontier/B1691_the_exponents_at_the_two_fixed_points/verification/correction"))
import b1656_funcs as B  # main's frame functions (B1656 verbatim)

SECT = [("up", 1, -4), ("down", 1, 2), ("lepton", -3, 6)]
assert (B.SIXY["Q"], B.SIXY["u"]) == (1, -4) and (B.SIXY["Q"], B.SIXY["d"]) == (1, 2) and (B.SIXY["L"], B.SIXY["e"]) == (-3, 6)


def dz(x):
    x = x - (x.numerator // x.denominator)
    return min(x, 1 - x)


def rule(alpha, ql, qr):
    ax, ay = ql * alpha, qr * alpha
    e = {(a, b): dz(ax + F(a, 2)) ** 2 + dz(ay + F(b, 2)) ** 2 - F(1, 8) for a in (0, 1) for b in (0, 1)}
    jk = min(e[(0, 0)], e[(1, 1)]); one_i = min(e[(0, 1)], e[(1, 0)])
    return {"1": one_i, "i": one_i, "j": jk, "k": jk}


def gap(alpha, ql, qr):
    r = rule(alpha, ql, qr)
    return abs(r["j"] - r["1"])          # within-sector only


print("(a) within-sector gaps (rule, exact):")
for al in (F(1, 5), F(2, 5)):
    print("   alpha=%s  up %s  down %s  lepton %s" % (al, *[gap(al, ql, qr) for _, ql, qr in SECT]))

print("\n(b) all reduced slopes p/N in (0, 1/2], 2 <= N <= 60:")
slopes = [F(p, N) for N in range(2, 61) for p in range(1, N // 2 + 1) if math.gcd(p, N) == 1]
c3 = [a for a in slopes if gap(a, 1, -4) != gap(a, 1, 2)]
c3gt = [a for a in slopes if gap(a, 1, -4) > gap(a, 1, 2)]
c3lt = [a for a in slopes if gap(a, 1, -4) < gap(a, 1, 2)]
alldeg = [a for a in slopes if gap(a, 1, -4) == gap(a, 1, 2) == gap(a, -3, 6)]
c1 = [a for a in slopes if (5 * a.numerator) % a.denominator == 0]
c2 = [a for a in slopes if (6 - 1) % a.denominator == 0 and (-3 - 2) % a.denominator == 0]
both = [a for a in slopes if a in c1 and a in c2]
sel = [a for a in both if a in c3]
print("   slopes scanned:", len(slopes))
print("   C3 (up gap != down gap) alone passes:", len(c3), " ; '>' variant alone:", len(c3gt), " ; '<':", len(c3lt))
print("   all three sectors' gaps equal (fully degenerate):", len(alldeg), [str(a) for a in alldeg[:12]], "...")
print("   C1 (5p = 0 mod N) passes:", [str(a) for a in c1], " ; C2 (N | 5) passes:", [str(a) for a in c2])
print("   C1 and C2 are the same set:", c1 == c2, " ; C1 & C2 & C3:", [str(a) for a in sel])
print("   C3 among the N = 5 slopes:", {str(a): gap(a, 1, -4) != gap(a, 1, 2) for a in both})
# down vs lepton gap equality is the transposition (C2) on N | 5 and fails elsewhere
dl_eq = [a for a in slopes if gap(a, 1, 2) == gap(a, -3, 6)]
print("   down gap == lepton gap on", len(dl_eq), "slopes; N | 5 among them:", all(a in dl_eq for a in c2))
small = [a for a in slopes if a.denominator <= 12]
print("   C3 on every slope with N <= 12 (True = passes):", {str(a): gap(a, 1, -4) != gap(a, 1, 2) for a in small})

print("\n(c) R_1^{up} on the line through 0 (p2 = 0), main's residues, |R_1| / max_s |R_s| at two tau:")
for al in (F(1, 5), F(2, 5), F(1, 3), F(1, 4), F(1, 6), F(2, 7), F(3, 8), F(1, 10), F(3, 10), F(1, 15), F(2, 15)):
    vals = []
    for t in (complex(0.13, 1.7), complex(0.41, 2.3)):
        w = B.line_w(float(al), 0.0, t)
        x, y = B.sector_twists(w, t, 1, -4)
        R = B.residues(x, y, t)
        m = max(abs(v) for v in R.values())
        vals.append(abs(R["1"]) / m)
    lane_c1 = (5 * al.numerator) % al.denominator == 0 and (3 * al.numerator) % al.denominator != 0
    theory = (5 * al.numerator) % al.denominator == 0 or (3 * al.numerator) % al.denominator == 0
    print("   alpha=%-5s |R_1|/max = %.1e, %.1e   vanishes: %-5s  lattice rule (5a or 3a in Z): %-5s  lane's C1: %s"
          % (al, vals[0], vals[1], max(vals) < 1e-9, theory, lane_c1))

print("\n(d) the gap rule on main's residues at further slopes (generic offset p2 = 0.137; Im tau = 12, 16; two Re tau);")
print("    printed: per sector, max |numeric relative exponent - rule relative exponent| over the four channels (within-sector)")
worst = 0.0
for al in (F(1, 3), F(1, 4), F(2, 7), F(3, 8), F(1, 6), F(3, 7), F(1, 7)):
    line = []
    for sn, ql, qr in SECT:
        r = rule(al, ql, qr); rdom = min(r.values())
        for xre in (0.13, 0.41):
            Rs = []
            for y in (12.0, 16.0):
                t = complex(xre, y); w = B.line_w(float(al), 0.137, t); x, yy = B.sector_twists(w, t, ql, qr)
                Rs.append(B.residues(x, yy, t))
            num = {s: -(math.log(abs(Rs[1][s])) - math.log(abs(Rs[0][s]))) / (2 * math.pi * 4.0) for s in B.UNITS}
            ndom = min(num.values())
            dev = max(abs((num[s] - ndom) - float(r[s] - rdom)) for s in B.UNITS)
            worst = max(worst, dev)
        line.append("%s gap rule %s dev %.1e" % (sn, gap(al, ql, qr), dev))
    print("   alpha=%-4s " % al + " | ".join(line))
print("   worst within-sector deviation:", "%.1e" % worst)

print("\n(e) 'structural non-degeneracy' applied to each sector pair, and uniformly (all three gaps distinct):")
pairs = {"up!=down": lambda a: gap(a, 1, -4) != gap(a, 1, 2), "up!=lepton": lambda a: gap(a, 1, -4) != gap(a, -3, 6),
         "down!=lepton": lambda a: gap(a, 1, 2) != gap(a, -3, 6)}
for nm, fn in pairs.items():
    print("   %-13s on N | 5: %s ; over all %d slopes: %d pass" % (nm, [str(a) for a in c2 if fn(a)], len(slopes), sum(1 for a in slopes if fn(a))))
alld = lambda a: all(fn(a) for fn in pairs.values())
print("   all three distinct on N | 5:", [str(a) for a in c2 if alld(a)], "; over all slopes:", sum(1 for a in slopes if alld(a)))

print("\n(f) the slopes whose down and lepton within-sector gaps coincide, and the minimal genericity 'not all three equal':")
print("   down gap == lepton gap:", [str(a) for a in dl_eq])
print("   ... and not all three equal:", [str(a) for a in dl_eq if a not in alldeg])
print("   B1728's lepton-down identity on the line through 0 (order N | 4 or N | 5):",
      [str(a) for a in slopes if a.denominator in (2, 4, 5)], "-> not all three equal among them:",
      [str(a) for a in slopes if a.denominator in (2, 4, 5) and a not in alldeg])
