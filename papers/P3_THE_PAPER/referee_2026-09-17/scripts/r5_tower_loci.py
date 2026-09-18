"""Referee verification of the MECHANISM behind B1374/B1375's 'one generation, never three'.

B1374: on t12839 = Y4, the non-split loci are 64 characters, and 'h1(chi^2) = 1 on all 64 loci
(chi of order 15 with chi(lam) = 1, or 30 with chi(lam) = -1; chi(mu) = 1 always, mu null-homologous)'.
B1375: 'all h1 = 1' on Y4, Y5, Y6, and each firing sector has (a0,a1,t0,r1) = (0,1,1,0) / (0,2,1,2).

That is the whole reason the count is ONE and never THREE: each firing sector contributes
n(V) - n(V*) = 1 - 0, and there is exactly one interior class because h1 = 1.  If any locus
carried h1 = 3 the mechanism would give three.

Computed here from scratch: SnapPy for the cover's presentation only; characters, Fox calculus,
ranks and h1 are this script's own, over three prime fields with 60th roots of unity.
"""
import snappy, warnings, itertools
warnings.filterwarnings("ignore")

def expsums(word, gens):
    e = {g: 0 for g in gens}
    for ch in word:
        g = ch.lower()
        e[g] += 1 if ch.islower() else -1
    return [e[g] for g in gens]

def fox_row(word, gens, chi, p):
    """Fox derivatives of `word` w.r.t. each generator, under the 1-dim character chi, over F_p."""
    P = 1
    D = {g: 0 for g in gens}
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
    M = [row[:] for row in M]
    if not M: return 0
    n, m = len(M), len(M[0]); r = 0
    for c in range(m):
        piv = next((i for i in range(r, n) if M[i][c] % p), None)
        if piv is None: continue
        M[r], M[piv] = M[piv], M[r]
        iv = pow(M[r][c], p - 2, p)
        M[r] = [(x * iv) % p for x in M[r]]
        for i in range(n):
            if i != r and M[i][c] % p:
                f = M[i][c]
                M[i] = [(M[i][j] - f * M[r][j]) % p for j in range(m)]
        r += 1
        if r == n: break
    return r

def primitive_root_of_unity(N, p):
    for g in range(2, p):
        z = pow(g, (p - 1) // N, p)
        if all(pow(z, N // q, p) != 1 for q in set(f for f in range(2, N + 1)
                                                  if N % f == 0 and all(f % d for d in range(2, f)))):
            return z
    raise RuntimeError

def analyse(level, N, primes, verbose=True):
    M = snappy.Manifold('m004')
    cov = M.covers(level, cover_type='cyclic')[0]
    G = cov.fundamental_group()
    gens = [g for g in G.generators()]
    rels = list(G.relators())
    mu, lam = G.peripheral_curves()[0]
    R = [expsums(r, gens) for r in rels]
    g = len(gens)
    print(f"\n=== Y{level}  ({cov.homology()}), {g} generators, {len(rels)} relators, N = {N} ===")
    print(f"    meridian  {mu}  expsums {expsums(mu, gens)}"
          f"   -> null-homologous: {all(e == 0 for e in expsums(mu, gens))}")
    print(f"    longitude {lam} expsums {expsums(lam, gens)}")

    # characters chi: t in (Z/N)^g with R t = 0 mod N
    chars = [t for t in itertools.product(range(N), repeat=g)
             if all(sum(R[i][j] * t[j] for j in range(g)) % N == 0 for i in range(len(R)))]
    print(f"    characters of order dividing {N}: {len(chars)}")

    results = {}
    for p in primes:
        z = primitive_root_of_unity(N, p)
        h1 = {}
        for t in chars:
            chi = {gens[j]: pow(z, t[j], p) for j in range(g)}
            J = [fox_row(r, gens, chi, p) for r in rels]
            trivial = all(x % N == 0 for x in t)
            h1[t] = (g - rank_fp(J, p)) - (0 if trivial else 1)
        results[p] = h1
    # agreement across primes
    agree = all(results[primes[0]] == results[q] for q in primes[1:])
    print(f"    h1 agrees across {primes}: {agree}")
    h1 = results[primes[0]]
    print(f"    h1(trivial character) = {h1[tuple([0]*g)]}   (must equal b1 = 1)")

    # loci: chi with h1(chi^2) != 0
    loci = []
    for t in chars:
        t2 = tuple((2 * x) % N for x in t)
        if h1.get(t2, 0) != 0:
            loci.append((t, h1[t2]))
    print(f"    NON-SPLIT LOCI (h1(chi^2) != 0): {len(loci)}")
    from collections import Counter
    print(f"    h1(chi^2) values at the loci: {dict(Counter(v for _, v in loci))}")
    def order(t):
        o = 1
        while any((o * x) % N for x in t): o += 1
        return o
    print(f"    orders of the locus characters: {dict(Counter(order(t) for t, _ in loci))}")
    zl = primitive_root_of_unity(N, primes[0])
    lam_e = expsums(lam, gens); mu_e = expsums(mu, gens)
    chilam = Counter()
    for t, _ in loci:
        e = sum(lam_e[j] * t[j] for j in range(g)) % N
        chilam[("+1" if e == 0 else ("-1" if 2 * e % N == 0 else "other"))] += 1
    print(f"    chi(longitude) at the loci: {dict(chilam)}")
    print(f"    chi(meridian) = 1 at every locus: "
          f"{all(sum(mu_e[j]*t[j] for j in range(len(gens))) % N == 0 for t, _ in loci)}")
    return loci, h1

if __name__ == "__main__":
    analyse(4, 60, [421, 541, 601])
    analyse(2, 60, [421, 541, 601])
    analyse(3, 12, [13, 37, 61])
