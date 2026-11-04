"""B1836 § 3: by exact arithmetic from the channel-exponent law (LAW_MAP), the within-sector channel-class gaps on every
reduced slope with N <= 60; among slopes in (0, 1/2] whose line carries B1728's lepton-down identity (N | 4 or 5), the
ones whose three gaps are not all equal. No held-out quantity enters."""
from fractions import Fraction as F
from math import gcd
def nn(x):
    x = x - (x.numerator // x.denominator); return min(x, 1 - x)
def gaps(al):
    out = {}
    for s, (ql, qr) in {"up": (1, -4), "down": (1, 2), "lep": (-3, 6)}.items():
        e = {(a, b): nn(ql * al + F(a, 2)) ** 2 + nn(qr * al + F(b, 2)) ** 2 - F(1, 8) for a in (0, 1) for b in (0, 1)}
        out[s] = abs(min(e[0, 0], e[1, 1]) - min(e[0, 1], e[1, 0]))
    return out
sl = [F(p, N) for N in range(1, 61) for p in range(1, N) if gcd(p, N) == 1]
print("reduced slopes N<=60:", len(sl), "; up gap != down gap:", sum(1 for a in sl if gaps(a)["up"] != gaps(a)["down"]))
print("1/5:", {k: str(v) for k, v in gaps(F(1, 5)).items()}, " 2/5:", {k: str(v) for k, v in gaps(F(2, 5)).items()})
half = [a for a in sl if a <= F(1, 2) and (4 % a.denominator == 0 or 5 % a.denominator == 0)]
print("N|4 or N|5 in (0,1/2]:", [str(a) for a in half], "; gaps not all equal:", [str(a) for a in half if len(set(gaps(a).values())) > 1])
