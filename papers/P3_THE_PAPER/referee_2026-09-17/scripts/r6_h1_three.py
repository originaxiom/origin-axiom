"""Is THREE reachable by the tower mechanism at all?

Verified in round 3: on Y2..Y5 every non-split locus has h1(chi^2) = 1, and that is exactly why
B1374/B1375 get ONE net generation per background.  Each firing sector contributes one interior
class against none.  To get THREE generations by the same mechanism you need a locus with
h1(chi^2) = 3.

This scans for one: every cover of m004 up to degree 8, plus the named members of the object's
commensurability class, over the full character group of order dividing N, and records the
distribution of h1(chi^2) at the non-split loci.

Own characters, own Fox calculus, own ranks over a prime field with Nth roots of unity.
SnapPy supplies presentations only.
"""
import snappy, warnings, itertools, sys
from collections import Counter
warnings.filterwarnings("ignore")


def expsums(word, gens):
    e = {g: 0 for g in gens}
    for ch in word:
        e[ch.lower()] += 1 if ch.islower() else -1
    return [e[g] for g in gens]


def fox_row(word, gens, chi, p):
    P, D = 1, {g: 0 for g in gens}
    for ch in word:
        g = ch.lower()
        if ch.islower():
            D[g] = (D[g] + P) % p
            P = (P * chi[g]) % p
        else:
            P = (P * pow(chi[g], p - 2, p)) % p
            D[g] = (D[g] - P) % p
    return [D[g] for g in gens]


def rank_fp(M, p):
    M = [r[:] for r in M]
    if not M or not M[0]:
        return 0
    n, m = len(M), len(M[0])
    r = 0
    for c in range(m):
        piv = next((i for i in range(r, n) if M[i][c] % p), None)
        if piv is None:
            continue
        M[r], M[piv] = M[piv], M[r]
        iv = pow(M[r][c], p - 2, p)
        M[r] = [(x * iv) % p for x in M[r]]
        for i in range(n):
            if i != r and M[i][c] % p:
                f = M[i][c]
                M[i] = [(M[i][j] - f * M[r][j]) % p for j in range(m)]
        r += 1
        if r == n:
            break
    return r


def root_of_unity(N, p):
    assert (p - 1) % N == 0
    for g in range(2, p):
        z = pow(g, (p - 1) // N, p)
        if all(pow(z, N // q, p) != 1 for q in prime_divisors(N)):
            return z
    raise RuntimeError


def prime_divisors(n):
    out, d = set(), 2
    while d * d <= n:
        while n % d == 0:
            out.add(d); n //= d
        d += 1
    if n > 1:
        out.add(n)
    return out


def h1_profile(G, N, p, cap=400000):
    gens = list(G.generators())
    rels = list(G.relators())
    g = len(gens)
    if not rels or g == 0:
        return None
    if N ** g > cap:
        return "skipped(too many characters)"
    R = [expsums(r, gens) for r in rels]
    z = root_of_unity(N, p)
    chars = [t for t in itertools.product(range(N), repeat=g)
             if all(sum(R[i][j] * t[j] for j in range(g)) % N == 0 for i in range(len(R)))]
    h1 = {}
    for t in chars:
        chi = {gens[j]: pow(z, t[j], p) for j in range(g)}
        J = [fox_row(r, gens, chi, p) for r in rels]
        h1[t] = (g - rank_fp(J, p)) - (0 if all(x % N == 0 for x in t) else 1)
    prof = Counter()
    for t in chars:
        t2 = tuple((2 * x) % N for x in t)
        v = h1.get(t2, 0)
        if v:
            prof[v] += 1
    return prof, len(chars)


def scan(names, N, p, label):
    print(f"\n=== {label}   (characters of order | {N}, field F_{p}) ===")
    print("   manifold            gens  characters   h1(chi^2) distribution at the loci")
    worst = Counter()
    for nm, G in names:
        try:
            res = h1_profile(G, N, p)
        except Exception as e:
            print(f"   {nm:18s}  -- {type(e).__name__}")
            continue
        if res is None or isinstance(res, str):
            print(f"   {nm:18s}  {res}")
            continue
        prof, nchars = res
        worst.update(prof)
        flag = "   <<< h1 >= 2 HERE" if any(k >= 2 for k in prof) else ""
        print(f"   {nm:18s}  {len(G.generators()):>3}  {nchars:>9}   {dict(sorted(prof.items()))}{flag}")
    print(f"   --- pooled h1(chi^2) distribution: {dict(sorted(worst.items()))}")
    return worst


if __name__ == "__main__":
    N, p = 60, 421
    M = snappy.Manifold('m004')

    covers = []
    for d in range(2, 9):
        for i, c in enumerate(M.covers(d)):
            covers.append((f"cover d={d} #{i}", snappy.Manifold(c).fundamental_group()))
    print(f"covers of m004 to degree 8: {len(covers)}")
    w1 = scan(covers, N, p, "every cover of m004 to degree 8")

    fam = ['m003', 'm202', 'm203', 'm206', 'm207', 'm208', 'm410', 'm412',
           's955', 's956', 's957', 's958', 's959', 's960', 's961',
           't12833', 't12835', 't12839', 'v2873']
    w2 = scan([(nm, snappy.Manifold(nm).fundamental_group()) for nm in fam], N, p,
              "named members of the object's commensurability class / family")

    tot = w1 + w2
    print("\n" + "=" * 66)
    print("POOLED over everything scanned:", dict(sorted(tot.items())))
    print("loci with h1(chi^2) = 3 (what THREE generations would need):", tot.get(3, 0))
    print("loci with h1(chi^2) >= 2:", sum(v for k, v in tot.items() if k >= 2))
