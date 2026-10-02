#!/usr/bin/env python3
"""B1522 -- the sealed census: on every level M_1 ... M_12 of m004's harmonic family, which vacua V = nu (x) rho_q (q > 0, q != 1)
are fixed by a count-odd map, by two routes that share no code (route F, the fibre model; route R, Reidemeister-Schreier with
its own Smith normal form), compared character by character through the bijection checked in controls.py (C8).

Read-out (PREREGISTRATION section 5):
  per level: |T_n|; the number of characters unfixed at generic or real lam (not E) and at unitary lam (neither E nor A);
  their primes, typed by their splitting in Q(sqrt 5) (split p = +-1 mod 5, inert p = +-2 mod 5, ramified p = 5);
  at split primes, the golden eigenline type of each p-primary component (zero, on the phi-line, on the phibar-line, mixed);
  the banked firing members (levels 1, 3, 4, 5, 6, from B1509/B1511/B1512/B1514's records) and whether each is fixed at its lam.
Usage: python3 census.py   (writes census.json; prints the read-out)"""
import json
import sys
import time
from math import gcd
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
sys.path.insert(0, str(HERE))
import route_fibre as RF  # noqa: E402
import route_rs as RR  # noqa: E402

LEVELS = range(1, 13)


def factor(n):
    out, p = {}, 2
    while p * p <= n:
        while n % p == 0:
            out[p] = out.get(p, 0) + 1
            n //= p
        p += 1
    if n > 1:
        out[n] = out.get(n, 0) + 1
    return out


def prime_type(p):
    if p == 5:
        return "ramified"
    return "split" if p % 5 in (1, 4) else "inert"


def char_order(v, N):
    return N // gcd(N, gcd(v[0], v[1]))


def golden_roots(p, e):
    """the two roots of t^2 - t - 1 mod p^e (p split), by brute force mod p and Hensel lifting"""
    roots = [r for r in range(p) if (r * r - r - 1) % p == 0]
    assert len(roots) == 2
    out = []
    for r in roots:
        x, mod = r, p
        for _ in range(1, e):
            mod *= p
            # Newton: x -> x - f(x)/f'(x) mod p^k
            f = x * x - x - 1
            fp = 2 * x - 1
            x = (x - f * pow(fp, -1, mod)) % mod
        assert (x * x - x - 1) % (p ** e) == 0
        out.append(x)
    return out


def eigen_type(v, N, p):
    """the golden eigenline type of the p-primary component of the character v (row vector, acted on by v -> v M)"""
    e = 0
    while N % (p ** (e + 1)) == 0:
        e += 1
    if e == 0:
        return "absent"
    pe = p ** e
    # the p-primary component of v is v times the CRT idempotent; up to a unit mod p^e it is v mod p^e, and the eigenline
    # condition (w M = lam w) is invariant under units, so v mod p^e is read
    w = (v[0] % pe, v[1] % pe)
    if w == (0, 0):
        return "zero"
    phi, phib = golden_roots(p, e)
    M = RF.M

    def on_line(w, lam):
        wm = ((w[0] * M[0][0] + w[1] * M[1][0]) % pe, (w[0] * M[0][1] + w[1] * M[1][1]) % pe)
        return wm == ((lam * w[0]) % pe, (lam * w[1]) % pe)
    if on_line(w, phi):
        return "phi-line"
    if on_line(w, phib):
        return "phibar-line"
    return "mixed"


def level_census(n):
    t0 = time.time()
    f = RF.flags(n)
    r = RR.census(n)
    lv = r["level"]
    chars, order, N = RF.characters(n)
    # character-by-character comparison through the bijection (controls C8)
    disagreements = []
    for v in chars:
        chi = RR.chi_from_fibre(lv, v, N)
        a, b = f["flags"][v], r["flags"][chi]
        if (a["E"], a["A"]) != (b["E"], b["A"]):
            disagreements.append({"char": list(v), "route F": a, "route R": b})
    generic = [v for v in chars if not f["flags"][v]["E"]]
    unitary = [v for v in chars if not (f["flags"][v]["E"] or f["flags"][v]["A"])]
    primes = factor(order) if order > 1 else {}
    types = {str(p): prime_type(p) for p in primes}

    def describe(vs):
        by_order, by_golden = {}, {}
        for v in vs:
            o = char_order(v, N)
            by_order[o] = by_order.get(o, 0) + 1
            key = tuple((p, eigen_type(v, N, p)) for p in sorted(primes) if prime_type(p) == "split")
            k = ";".join(f"{p}:{t}" for p, t in key) or "no split prime"
            by_golden[k] = by_golden.get(k, 0) + 1
        return {"by order": {str(k): v for k, v in sorted(by_order.items())}, "by golden type at split primes": by_golden}
    return {
        "n": n, "order": order, "invariant factors": sorted(r["invariant_factors"]), "N": N, "primes": {str(p): e for p, e in primes.items()},
        "prime types": types, "group order on characters": f["group_order"],
        "routes agree on every character": not disagreements, "disagreements": disagreements[:10],
        "unfixed at generic lam": len(generic), "unfixed at unitary lam": len(unitary),
        "fraction unfixed at generic lam": round(len(generic) / order, 6),
        "generic unfixed described": describe(generic), "unitary unfixed described": describe(unitary),
        "generic unfixed list": [list(v) for v in generic] if len(generic) <= 40 else None,
        "unitary unfixed list": [list(v) for v in unitary] if len(unitary) <= 40 else None,
        "seconds": round(time.time() - t0, 1),
    }


def firing_population():
    """the banked chiral configurations' backgrounds: (level, character (a, b) mod N, N, lam, source)"""
    out = [{"level": 1, "char": [0, 0], "N": 1, "lam": "-1", "source": "B1509/B1455/B1520: W1 at q0 = 17 +- 12 sqrt2"}]
    for c in ((0, 2), (2, 2), (2, 0)):
        out.append({"level": 3, "char": list(c), "N": 4, "lam": "-1", "source": "B1511 part A: the projective triplet at q^3 = 17 +- 12 sqrt2"})
    # B1509's W1 pulled back to every level n <= 6: trivial fibre character, lam = (-1)^n (B1511: 'an orbit of size one')
    for n in range(2, 7):
        out.append({"level": n, "char": [0, 0], "N": 1, "lam": "-1" if n % 2 else "1", "source": "B1511: B1509's W1 pulled back"})
    # the projective triplet pulled back to level 6 (Shapiro): T_3's order-2 characters in T_6, lam = (-1)^2 = 1
    chars6, order6, N6 = RF.characters(6)
    pulled = [v for v in chars6 if all(((v[0] * B[0][j] + v[1] * B[1][j]) % N6) == 0 for B in ([[x - (1 if i == j else 0) for j, x in enumerate(row)] for i, row in enumerate(RF.matpow(RF.PHI, 3))],) for j in range(2)) and v != (0, 0)]
    for v in pulled:
        if char_order(v, N6) == 2:
            out.append({"level": 6, "char": list(v), "N": N6, "lam": "1", "source": "B1511: the triplet pulled back to M6 (Shapiro)"})
    # B1511/B1512's case (b) members on M4, M5, M6, read by B1514's loader from the banked run records
    import importlib.util
    spec = importlib.util.spec_from_file_location("b1514_law_lib", ROOT / "frontier/B1514_the_decoupling_law/verification/law_lib.py")
    LL = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(LL)
    for pop in LL.populations():
        for oname, members in pop["orbits"].items():
            for m in members:
                out.append({"level": pop["level"], "char": [int(m[0]), int(m[1])], "N": int(pop["N"]), "lam": pop["lam"],
                            "source": f"case (b): {pop['label']} ({pop['factor']})"})
    return out


def firing_census(levels_data):
    pop = firing_population()
    rows = []
    cache = {}
    for m in pop:
        n = m["level"]
        if n not in cache:
            cache[n] = RF.flags(n)
        f = cache[n]
        N = f["N"]
        # bring the member's character to this level's exponent N
        a, b = m["char"]
        scale = N // m["N"] if m["N"] and N % m["N"] == 0 else None
        assert scale is not None, (m, N)
        v = ((a * scale) % N, (b * scale) % N)
        assert v in f["flags"], (m, v)
        fl = f["flags"][v]
        unitary = m["lam"] in ("1", "-1", "i", "-i")
        fixed = (fl["E"] or fl["A"]) if unitary else fl["E"]
        rows.append({**m, "char at level": list(v), "E": fl["E"], "A": fl["A"], "fixed at its lam": fixed})
    return {"members": len(rows), "fixed": sum(1 for r in rows if r["fixed at its lam"]),
            "unfixed": [r for r in rows if not r["fixed at its lam"]], "rows": rows}


def main():
    out = {"levels": [], "started": time.strftime("%Y-%m-%d %H:%M:%S")}
    for n in LEVELS:
        row = level_census(n)
        out["levels"].append(row)
        print(f"n = {n:2d}  |T| = {row['order']:6d}  unfixed generic {row['unfixed at generic lam']:6d}  unitary "
              f"{row['unfixed at unitary lam']:6d}  routes agree {row['routes agree on every character']}  ({row['seconds']} s)", flush=True)
    out["firing"] = firing_census(out["levels"])
    print(f"firing members: {out['firing']['members']}, fixed {out['firing']['fixed']}, unfixed {len(out['firing']['unfixed'])}")
    out["finished"] = time.strftime("%Y-%m-%d %H:%M:%S")
    (HERE / "census.json").write_text(json.dumps(out, indent=1, ensure_ascii=False) + "\n")


if __name__ == "__main__":
    main()
