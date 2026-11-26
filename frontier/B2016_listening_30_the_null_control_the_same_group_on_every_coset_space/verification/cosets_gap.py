"""B2016, N0 to N2 (main, 2026-11-26; data-free; FLINT): on each coset space exported by cosets_export.py, the six moves as
words sigma C^2, sigma C, C sigma, C^2 sigma, C sigma C, C^2 sigma C^2 (closed under inversion and under C-conjugation, so W
is symmetric and C-covariant in any action); W's neutral and q = 1 charged sector polynomials exactly (the charged one by CRT
over primes = 1 mod 3 past the 7^d bound); the classification (a) p_neutral(2x)/2^d == (x^2 - 9) x S(x), (b) S divides
p_neutral(2x)/2^d, (c) neither; C's fixed points.
    python3 -B cosets_gap.py > cosets_gap_run.txt"""
import json, pathlib, time, collections, hashlib
import flint
from sympy import nextprime
HERE = pathlib.Path(__file__).resolve().parent
t0 = time.time()
log = lambda s: print(s + "  [%.0f s]" % (time.time() - t0), flush=True)


def comp(*ps):            # functions composed right to left: comp(a, b)(i) = a(b(i))
    def f(i):
        for p in reversed(ps):
            i = p[i]
        return i
    return f


def sector_polys(Cp, Sp):
    n = len(Cp)
    C2 = [Cp[Cp[i]] for i in range(n)]
    words = [comp(Sp, C2), comp(Sp, Cp), comp(Cp, Sp), comp(C2, Sp), comp(Cp, Sp, Cp), comp(C2, Sp, C2)]
    orb, reps, size = {}, [], []
    for v in range(n):
        if v in orb:
            continue
        o = len(reps); reps.append(v); u = v; j = 0
        while u not in orb:
            orb[u] = (o, j); u = Cp[u]; j += 1
        size.append(j)
    d0 = len(reps)
    Q = [[0] * d0 for _ in range(d0)]
    for o, v in enumerate(reps):
        for w in words:
            Q[orb[w(v)][0]][o] += 1
    pn = flint.fmpz_mat(Q).charpoly()
    ch = [o for o in range(d0) if size[o] == 3]; ci = {o: i for i, o in enumerate(ch)}; d1 = len(ch)
    if d1 == 0:
        return pn, flint.fmpz_poly([1]), d0, d1, sum(1 for z in size if z == 1)
    ent = [dict() for _ in range(d1)]
    pw = ((1, 0), (0, 1), (-1, -1))
    for o in ch:
        v = reps[o]; u = v
        for j in range(3):
            ph = pw[(3 - j) % 3]
            for w in words:
                o2, jt = orb[w(u)]
                if o2 in ci and jt == 0:
                    e = ent[ci[o2]].setdefault(ci[o], [0, 0]); e[0] += ph[0]; e[1] += ph[1]
            u = Cp[u]
    bound = 2 * 7 ** d1 + 1; M = 1; res = None; p = int(nextprime(1 << 61))
    while M <= bound:
        while p % 3 != 1:
            p = int(nextprime(p))
        g = 2
        while pow(g, (p - 1) // 3, p) == 1:
            g += 1
        w3 = pow(g, (p - 1) // 3, p)
        rows = [[0] * d1 for _ in range(d1)]
        for r, dct in enumerate(ent):
            for cc, (a, b) in dct.items():
                rows[r][cc] = (a + b * w3) % p
        cp = [int(x) for x in flint.nmod_mat(rows, p).charpoly().coeffs()]
        if res is None:
            res, M = cp, p
        else:
            inv = pow(M, -1, p); res = [r + M * (((x - r) * inv) % p) for r, x in zip(res, cp)]; M *= p
        p = int(nextprime(p))
    S = flint.fmpz_poly([r if r <= M // 2 else r - M for r in res])
    return pn, S, d0, d1, sum(1 for z in size if z == 1)


def halved(f):
    cs = [int(c) for c in f.coeffs()]; d = len(cs) - 1
    return flint.fmpz_poly([c * 2 ** i // 2 ** d for i, c in enumerate(cs)])


X = flint.fmpz_poly([0, 1]); Q9 = flint.fmpz_poly([-9, 0, 1])
raw = (HERE / "coset_actions.json").read_bytes()
log("the exported actions: sha256 %s" % hashlib.sha256(raw).hexdigest())
data = json.loads(raw)
for N in ("27", "81"):
    tally = collections.Counter(); whole = None; a_list = []
    for r in data[N]["classes"]:
        n = r["index"]
        if n > 2000:
            tally["skipped (index > 2000)"] += 1; continue
        pn, S, d0, d1, fx = sector_polys(r["C"], r["S"])
        h = halved(pn)
        cat = "a" if h == Q9 * X * S else ("b" if d1 > 0 and h % S == 0 else "c")
        tally[cat] += 1
        if cat == "a":
            a_list.append((r["order"], n, fx, r["rho_trivial"], r["whole"]))
        if r["whole"]:
            whole = (cat, r["order"], n, fx, r["rho_trivial"])
    log("mod %s: |G| = %d; %d classes of subgroups" % (N, data[N]["order"], len(data[N]["classes"])))
    log("    the whole's stabiliser class: category %s, |H| = %d, index %d, C fixes %d, rho trivial on H: %s" % whole)
    log("    categories: %s" % dict(tally))
    log("    the classes in (a) (|H|, index, C's fixed points, rho trivial on H, conjugate to the whole's stabiliser): %s" % sorted(a_list))
