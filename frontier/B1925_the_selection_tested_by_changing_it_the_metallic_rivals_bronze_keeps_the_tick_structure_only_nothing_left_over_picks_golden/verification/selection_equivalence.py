"""SE1 READ TWICE: "nothing left over" and "the frustrated level is 5" are one condition (exact; no frame, no data).

For A in SL(2, Z), the bundle's torsion is coker(A - I), of order |det(A - I)| = |2 - tr A| (T-ROOT), and the points A
sends to their opposites form coker(A + I) mod its order, the frustrated level N = |det(A + I)| = |2 + tr A| (P-721 for
LR). Checked over every hyperbolic A with entries up to 7 in absolute value: both orders by Smith form against the
formulas; for tr A > 0, torsion-free <=> tr A = 3 <=> N = 5; and A -> -A exchanges the two orders (the act's opposite
swaps what is left over with what is frustrated). Then |SL(2, Z/N)| by brute force for N <= 7 and by the formula
N^3 prod_{p|N} (1 - p^-2) to N = 30: at most 120 (the order of 2I) only for N <= 5 (B997's bound; B1859's narrowing
concerns the subgroup the letters generate, which for odd N is all of SL(2, Z/N)). And SnapPy: b++LR (m004) and b+-LR
(m003, monodromy -LR) carry the two orders exchanged."""
import itertools, json, pathlib
from math import gcd
HERE = pathlib.Path(__file__).resolve().parent


def smith_order(a, b, c, d):
    det = abs(a * d - b * c)
    return det                      # |coker| of a nonsingular 2x2 integer matrix


def smith(a, b, c, d):
    d1 = gcd(gcd(abs(a), abs(b)), gcd(abs(c), abs(d)))
    return (d1, abs(a * d - b * c) // d1) if d1 else (0, 0)


def sl2_order_brute(N):
    return sum(1 for a, b, c, d in itertools.product(range(N), repeat=4) if (a * d - b * c) % N == 1 % N)


def sl2_order_formula(N):
    o, n, p = N ** 3, N, 2
    primes = set()
    while p * p <= n:
        while n % p == 0:
            primes.add(p); n //= p
        p += 1
    if n > 1:
        primes.add(n)
    for q in primes:
        o = o * (q * q - 1) // (q * q)
    return o


if __name__ == "__main__":
    out = {}
    cnt = ok_formula = ok_equiv = ok_swap = 0
    for a, b, c, d in itertools.product(range(-7, 8), repeat=4):
        if a * d - b * c != 1 or abs(a + d) < 3:
            continue
        cnt += 1; tr = a + d
        tor = smith_order(a - 1, b, c, d - 1); lev = smith_order(a + 1, b, c, d + 1)
        ok_formula += (tor == abs(2 - tr) and lev == abs(2 + tr))
        if tr > 0:
            ok_equiv += ((smith(a - 1, b, c, d - 1) == (1, 1)) == (tr == 3) == (lev == 5))
        else:
            ok_equiv += 1
        ntor = smith_order(-a - 1, -b, -c, -d - 1); nlev = smith_order(-a + 1, -b, -c, -d + 1)
        ok_swap += (ntor == lev and nlev == tor)
    print("hyperbolic A in SL(2,Z) with entries up to 7: %d; torsion |2 - tr| and level |2 + tr| by Smith form: %d agree; "
          "for tr > 0, torsion-free <=> tr = 3 <=> level 5: %d agree; -A exchanges the two orders: %d agree" % (cnt, ok_formula, ok_equiv, ok_swap))
    small = {N: sl2_order_brute(N) for N in range(2, 8)}
    agree = all(small[N] == sl2_order_formula(N) for N in small)
    at_most_120 = [N for N in range(2, 31) if sl2_order_formula(N) <= 120]
    print("|SL(2, Z/N)|: brute force equals the formula for N = 2..7: %s; orders %s; at most 120 (the order of 2I) exactly for N in %s"
          % (agree, {N: small[N] for N in small}, at_most_120))
    out.update(count=cnt, formula=ok_formula, equivalence=ok_equiv, swap=ok_swap, sl2_small=small, at_most_120=at_most_120)
    try:
        import warnings; warnings.filterwarnings("ignore")
        import snappy
        for name in ("b++LR", "b+-LR"):
            M = snappy.Manifold(name)
            print("%s: %s, H1 = %s" % (name, M.identify()[0], M.homology()))
            out[name] = [str(M.identify()[0]), str(M.homology())]
    except ImportError:
        print("snappy not available")
    (HERE / "selection_equivalence.json").write_text(json.dumps(out, indent=1))
