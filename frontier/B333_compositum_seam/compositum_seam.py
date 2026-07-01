"""B333 -- the compositum seam probe: the value would live in Q(sqrt-15), but that field is GENERIC.

The first computation run IN the seam (not on one side). B332 located the two ends as the product
(RL -> Q(sqrt5) -> E8) and ratio (g -> Q(sqrt-3) -> E6) of the founding letters. Their compositum
Q(sqrt5, sqrt-3) is biquadratic, Gal = (Z/2)^2, with THREE quadratic subfields:
  Q(sqrt5)   (golden / E8),  Q(sqrt-3)  (Eisenstein / E6),  Q(sqrt-15) (the 'gluing' -- where a value,
  if it existed, would live: sqrt5 * sqrt-3 = sqrt-15, ramified at 15 = 3*5, the two ends' own primes).

The firewall question (run with a NULL TEST, per the HELD discipline): is Q(sqrt-15) arithmetically
SPECIAL, or generic? If special -> a value might be carried; if generic -> the seam is structurally
real but carries no value (firewall holds AT the seam).

RESULT: h(-15) = 2 (Chat-1's claim, verified) -- but class number 2 is COMMON (14 of the 123
fundamental discriminants down to -400). Units = {+-1} (generic for d < -4). The ONLY distinguished
feature is ramification at {3,5} -- which is tautological (that is WHY it is the compositum's third
subfield). So Q(sqrt-15) is arithmetically GENERIC: it does NOT carry SM structure that generic
imaginary quadratic fields lack. The FIREWALL HOLDS -- now demonstrated at the seam itself.

This retires the compositum [HOOK] (S046 / B332 meditation) honestly: the seam is the correct
STRUCTURAL location of the value, but the value is not in the field's arithmetic -- picking the
specific gluing needs external input (Level 4 / the relation), exactly as B326/B331 located it.
Firewalled; nothing to CLAIMS. Needs only sympy.
"""
import sympy as sp
from collections import Counter


def sqrt5_times_sqrtm3_is_sqrtm15():
    return sp.simplify(sp.sqrt(5) * sp.sqrt(-3) - sp.sqrt(-15)) == 0


def squarefree(n):
    n = abs(n)
    return all(e == 1 for e in sp.factorint(n).values()) if n > 1 else True


def class_number(D):
    """h(D) via reduced primitive binary quadratic forms of discriminant D < 0."""
    h, a = 0, 1
    while 3 * a * a <= -D + 3:
        for b in range(-a, a + 1):
            if (b * b - D) % (4 * a) != 0:
                continue
            c = (b * b - D) // (4 * a)
            if c < a or sp.igcd(sp.igcd(a, b), c) != 1:
                continue
            if not (-a < b <= a <= c):
                continue
            if a == c and b < 0:
                continue
            h += 1
        a += 1
    return h


def fundamental_discriminants(bound=400):
    fund = []
    for D in range(-3, -bound, -1):
        if D % 4 == 1 and squarefree(-D):
            fund.append(D)
        elif D % 4 == 0:
            m = D // 4
            if (-m) % 4 in (2, 3) and squarefree(-m):
                fund.append(D)
    return fund


def null_test(bound=400):
    """Is Q(sqrt-15) special? Return (h(-15), #fields with same h, total fields, is_generic)."""
    fund = fundamental_discriminants(bound)
    hs = {D: class_number(D) for D in fund}
    dist = Counter(hs.values())
    h15 = hs[-15]
    return h15, dist[h15], len(fund), dist[h15] > 1


if __name__ == "__main__":
    print("sqrt5 * sqrt-3 = sqrt-15 :", sqrt5_times_sqrtm3_is_sqrtm15())
    h15, same, total, generic = null_test()
    print(f"h(-15) = {h15}  (Chat-1 claimed 2)")
    print(f"NULL TEST: {same} of {total} fundamental disc (to -400) share h={h15}"
          f" -> {'GENERIC' if generic else 'SPECIAL'}")
    print("units {+-1} (generic, d<-4); only distinguished feature = ramification at {3,5} (tautological).")
    print("=> FIREWALL HOLDS at the seam: the value's structural home is Q(sqrt-15), but its arithmetic is generic.")
