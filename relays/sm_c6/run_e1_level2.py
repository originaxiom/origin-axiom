#!/usr/bin/env python3
"""SM-C6 E1, the owed level 2 of the word step (card relays/cards/SM_C6_E1_the-based-count.md, step 1; its run left
level 2 out at N = 221 and 198, page relays/SM_C6_E1_THE_BASED_COUNT.md).  Same definitions as run_e1.py (B1438's
slopes, the based count), one change of method, disclosed: the slopes are computed in F_p for two primes p = 1 mod N,
through the ring map Z[zeta_N][1/d] -> F_p, zeta_N -> a primitive N-th root mod p, in place of exact Q(zeta_N).
Equal slopes stay equal under the map; a false equality needs p to divide a non-zero difference, so a pair of slopes is
called equal only when it is equal mod both primes.
Built-in check: at level 1 every slope mod p must equal B1438's exact slope reduced mod p, and the level-1 results must
reproduce relays/sm_c6/e1_results.json.  Plant P1 as in run_e1.py (alpha's slope replaced by beta's).
    python3 run_e1_level2.py MAIN_CHECKOUT [out.json]"""
import sys, io, json, time, contextlib, pathlib, itertools
from collections import Counter
from fractions import Fraction as Fr
HERE = pathlib.Path(__file__).resolve().parent
MAIN = pathlib.Path(sys.argv[1]).resolve()
sys.path.insert(0, str(MAIN / "frontier" / "B1438_the_slope_law" / "verification"))
with contextlib.redirect_stdout(io.StringIO()):
    import slope_law as SL
ac, ic = SL.ac, SL.ic
PAIRS = [("LLRLRR", "LLRRLR"), ("LLLRLRR", "LLLRRLR"), ("LLRLRRR", "LLRRRLR")]


def is_prime(n):
    if n < 2: return False
    for q in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        if n % q == 0: return n == q
    d, s = n - 1, 0
    while d % 2 == 0: d //= 2; s += 1
    for a in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        x = pow(a, d, n)
        if x in (1, n - 1): continue
        for _ in range(s - 1):
            x = x * x % n
            if x == n - 1: break
        else: return False
    return True


def primes_1_mod(N, start, count):
    out, m = [], start // N + 1
    while len(out) < count:
        p = m * N + 1
        if is_prime(p): out.append(p)
        m += 1
    return out


def prim_root_of_unity(N, p):
    """an element of exact order N in F_p*"""
    fac = [q for q in range(2, N + 1) if N % q == 0 and all(q % r for r in range(2, q))]
    for g in range(2, p):
        z = pow(g, (p - 1) // N, p)
        if z != 1 and all(pow(z, N // q, p) != 1 for q in fac): return z
    raise ValueError


def slopes_mod(eps, word, k, p):
    """B1438's exact_slopes, line by line, in F_p"""
    ng, rels, mu, lam, tau, A, tors = ac.level(eps, word, k); N = max(1, ac.torsion_exponent(A))
    Phi = ic.Phi_of(eps, word, k); z = prim_root_of_unity(N, p)
    ex = lambda w: (sum((g == 1) - (g == -1) for g in w), sum((g == 2) - (g == -2) for g in w))
    px, py = ex(Phi[1]), ex(Phi[2]); out = {}
    inv = lambda a: pow(a % p, p - 2, p)
    for i, j in itertools.product(range(N), repeat=2):
        if (i, j) == (0, 0) or (px[0] * i + px[1] * j - i) % N or (py[0] * i + py[1] * j - j) % N: continue
        val = {1: pow(z, i, p), 2: pow(z, j, p), -1: pow(z, (-i) % N, p), -2: pow(z, (-j) % N, p)}
        u = {1: 0, 2: inv(val[1] - 1)} if i % N else {1: inv(1 - val[2]), 2: 0}
        def ev(w):
            tot, pre = 0, 1
            for g in w:
                if g > 0: tot = (tot + pre * u[g]) % p; pre = pre * val[g] % p
                else: pre = pre * val[g] % p; tot = (tot - pre * u[-g]) % p
            return tot
        assert ev((1, 2, -1, -2)) == 1, "the longitude normalisation"
        g = 1 if i % N else 2
        s = (u[g] - ev(Phi[g])) * inv(val[g] - 1) % p
        g2 = 3 - g
        if val[g2] != 1: assert (u[g2] - ev(Phi[g2])) * inv(val[g2] - 1) % p == s, "one slope for both generators"
        out[(i, j, 0)] = s
    return N, z, out


def reduce_exact(el, z, p):
    """B1438's exact slope (rational coefficients in powers of zeta) reduced mod p at zeta -> z"""
    tot = 0
    for e, q in enumerate(el.c):
        q = Fr(q); tot = (tot + q.numerator * pow(q.denominator, p - 2, p) * pow(z, e, p)) % p
    return tot


def keyed(slopes_by_prime):
    chars = list(slopes_by_prime[0].keys())
    return {c: tuple(s[c] for s in slopes_by_prime) for c in chars}


def based(K, N, swap_plant=False):
    """the based count {(l, alpha): (n, n*)} as run_e1.based, with slopes compared by their key mod both primes"""
    chars = list(K)
    out = {}
    for l in chars:
        for a in chars:
            if a == l: continue
            b = tuple((x - y) % N for x, y in zip(a, l)); bi = tuple((-x) % N for x in b)
            sa = K[b] if swap_plant else K[a]
            out[(l, a)] = (int(sa == K[l]), int(K[bi] == K[l]))
    return out


def census(B):
    c = Counter(B.values()); return {"%d%d" % k: v for k, v in sorted(c.items())}


def main():
    out_path = pathlib.Path(sys.argv[2]) if len(sys.argv) > 2 else HERE / "e1_level2_results.json"
    e1 = json.load(open(HERE / "e1_results.json"))
    exact1 = {(p_["word"], p_["sign"], p_["level"]): p_ for p_ in e1["pairs"]}
    res = {"method": "slopes in F_p for two primes p = 1 mod N; equal only if equal mod both", "check_level1": [],
           "pairs": [], "plants": {}}
    p1_changed = p1_n = 0
    for k in (1, 2):
        for (w, r) in PAIRS:
            for eps in (1, -1):
                t0 = time.time()
                Nw = max(1, ac.torsion_exponent(ac.level(eps, w, k)[5]))
                primes = primes_1_mod(Nw, 2 ** 31, 2)
                Sw = [slopes_mod(eps, w, k, p)[2] for p in primes]
                Sr = [slopes_mod(eps, r, k, p)[2] for p in primes]
                Nr = max(1, ac.torsion_exponent(ac.level(eps, r, k)[5]))
                assert Nr == Nw
                Kw, Kr = keyed(Sw), keyed(Sr)
                # one prime against the other: the partition into slope classes must be the same
                parts = []
                for S in (Sw, Sr):
                    cl0 = Counter(S[0].values()); cl1 = Counter(S[1].values())
                    parts.append(sorted(cl0.values()) == sorted(cl1.values()))
                Bw, Br = based(Kw, Nw), based(Kr, Nr)
                same_chars = set(Kw) == set(Kr)
                row = {"word": w, "reverse": r, "sign": eps, "level": k, "N": Nw, "primes": primes,
                       "characters": len(Kw), "slope_classes": len(set(Kw.values())),
                       "two_primes_agree_on_classes": all(parts), "same_coordinate_characters": same_chars,
                       "labelled_same": same_chars and Bw == Br, "census_w": census(Bw), "census_r": census(Br)}
                row["census_same"] = row["census_w"] == row["census_r"]
                if k == 1:
                    # exact check: every slope mod p equals B1438's exact slope reduced mod p
                    with contextlib.redirect_stdout(io.StringIO()):
                        N_, F_, S_ex = SL.exact_slopes(eps, w, k)
                    bad = 0
                    for p in primes:
                        Nm, z, Sm = slopes_mod(eps, w, k, p)
                        bad += sum(reduce_exact(S_ex[c], z, p) != Sm[c] for c in Sm)
                    ex = exact1.get((w, eps, 1))
                    row["exact_slopes_mismatch_mod_p"] = bad
                    row["reproduces_e1"] = (ex is not None and ex["labelled_same"] == row["labelled_same"]
                                            and ex["census_w"] == row["census_w"] and ex["census_r"] == row["census_r"])
                    res["check_level1"].append({k_: row[k_] for k_ in ("word", "sign", "exact_slopes_mismatch_mod_p",
                                                                     "reproduces_e1")})
                # plant P1 (alpha's slope replaced by beta's) must change the census
                cp = census(based(Kw, Nw, swap_plant=True)); p1_n += 1; p1_changed += cp != row["census_w"]
                row["seconds"] = round(time.time() - t0, 1)
                res["pairs"].append(row)
                print(k, w, r, eps, "N", Nw, "chars", len(Kw), "classes", row["slope_classes"], "labelled_same",
                      row["labelled_same"], "census_same", row["census_same"], row["seconds"], "s", flush=True)
    res["plants"]["P1 census changed"] = [p1_changed, p1_n]
    L2 = [x for x in res["pairs"] if x["level"] == 2]
    res["summary"] = {
        "level1_exact_check": all(c["exact_slopes_mismatch_mod_p"] == 0 and c["reproduces_e1"] for c in res["check_level1"]),
        "level2_tests": len(L2), "level2_labelled_differs": sum(not x["labelled_same"] for x in L2),
        "level2_census_same": sum(x["census_same"] for x in L2),
        "two_primes_agree": all(x["two_primes_agree_on_classes"] for x in res["pairs"]),
        "outcome_level2": ("1" if all(x["census_same"] for x in L2) and any(not x["labelled_same"] for x in L2)
                           else "2" if not all(x["census_same"] for x in L2) else "3")}
    json.dump(res, open(out_path, "w"), indent=1)
    print(json.dumps(res["summary"], indent=1)); print(json.dumps(res["plants"]))


if __name__ == "__main__":
    main()
