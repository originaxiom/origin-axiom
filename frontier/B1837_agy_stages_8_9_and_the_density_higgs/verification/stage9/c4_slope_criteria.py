"""S303 check c4 (value-free; exact arithmetic): the agy lane's 'Spectral Faithfulness' (Theorem 67, cited by Theorem 71's
R5) against three exponent families on every slope in (0, 1/2] whose line carries B1728's lepton-down identity (N | 4 or 5):
 (i)  main's channel-class gaps (LAW_MAP channel-exponent law; B1836 slope_gaps_exact.py);
 (ii) B1788 section 4's m2/m3 exponents on 5 alpha in Z: e_up = 1/2 - ||3 alpha||, e_down = e_lep = 1/5;
 (iii) the web seat's steepness map e_up - e_down = (||4 alpha|| - ||8 alpha||)/2 (B1836, re-derived from B1788).
'Faithful' (the lane's definition): the self-transpose orbit (up) and the pair orbit (down, lepton) have different exponents.
Also the mod-5 orbit structure of the charges. Within-sector exponents only; no cross-sector exponent is computed."""
from fractions import Fraction as F
from math import gcd


def nn(x):
    x = x - (x.numerator // x.denominator); return min(x, 1 - x)


CH = {"up": (1, -4), "down": (1, 2), "lep": (-3, 6)}


def class_gaps(al):
    out = {}
    for s, (ql, qr) in CH.items():
        e = {(a, b): nn(ql * al + F(a, 2)) ** 2 + nn(qr * al + F(b, 2)) ** 2 - F(1, 8) for a in (0, 1) for b in (0, 1)}
        out[s] = abs(min(e[0, 0], e[1, 1]) - min(e[0, 1], e[1, 0]))
    return out


print("mod-5 charges:", {s: (ql % 5, qr % 5) for s, (ql, qr) in CH.items()}, "(up self-transpose; down, lepton a transpose pair)")
slopes = sorted({F(p, N) for N in range(1, 61) for p in range(1, N) if gcd(p, N) == 1 and F(p, N) <= F(1, 2)
                 and (4 % N == 0 or 5 % N == 0)})
print("identity slopes in (0, 1/2]:", [str(a) for a in slopes])
for al in slopes:
    g = class_gaps(al)
    f1 = g["up"] != g["down"]
    row = "  %-4s (i) class gaps up %s down %s lep %s -> faithful %s" % (al, g["up"], g["down"], g["lep"], f1)
    if (5 * al).denominator == 1:
        eu, ed = F(1, 2) - nn(3 * al), F(1, 5)
        st = (nn(4 * al) - nn(8 * al)) / 2
        row += " | (ii) e_up %s e_down %s -> faithful %s, up steeper %s | (iii) e_up - e_down %s (agrees with (ii): %s)" % (
            eu, ed, eu != ed, eu > ed, st, st == eu - ed)
    print(row)
