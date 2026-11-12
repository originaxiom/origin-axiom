#!/usr/bin/env python3
"""WP-1.6 and WP-1.5 together: a thread's factor in the product over threads, in the record's triplet.

The triplet's two moves are monomial matrices (B1866's lock gives them: a permutation of the three parities with 24th
roots of unity).  So a thread's matrix T(w) is monomial too, its permutation is the thread's act on the three parities
(the three classes of harvest row 917), and its factor det(1 - x T(w)), x = u^|w|, is read off:
  a 3-cycle (odd trace):            1 - det T(w) x^3,  and det T(w) = (-1)^|w| exp(i pi (#L - #R) / 4);
  a transposition (an involution):  (1 - a x)(1 - b x^2);
  the identity:                     (1 - a x)(1 - b x)(1 - c x).
COMPUTED, exactly: every primitive cyclic word with both letters to length 14, its class, its factor's type, and for the
odd-trace ones the formula for the determinant.  And the product over all of them with the two letters' factors, against
1 - sqrt2 u + u^2 + sqrt2 u^3, to order 14: Amitsur's identity in this module.  Arithmetic is in the ring of 24th roots
of unity, Z[z] modulo z^8 - z^4 + 1, with integer vectors of length 8.
HOW IT COULD FAIL: the planted case drops the threads of length 2 from the product."""
import itertools, json, pathlib, collections
HERE = pathlib.Path(__file__).resolve().parent
XL, XR = ((0, 2, 1), (21, 3, 3)), ((1, 0, 2), (21, 21, 3))                    # column j goes to row p[j] with the phase z^e[j]
ID = ((0, 1, 2), (0, 0, 0)); ORDER = 14
def mul(A, B): return (tuple(A[0][B[0][j]] for j in range(3)), tuple((B[1][j] + A[1][B[0][j]]) % 24 for j in range(3)))
def word(w):
    M = ID
    for ch in w: M = mul(M, XL if ch == "L" else XR)
    return M
def lyndon(n):
    return ["".join(w) for w in itertools.product("LR", repeat=n) if all("".join(w) < "".join(w[i:] + w[:i]) for i in range(1, n))]
def trace2(w):
    a, b, c, d = 1, 0, 0, 1
    for ch in w: a, b, c, d = (a, a + b, c, c + d) if ch == "L" else (a + b, b, c + d, d)
    return a + d
# ---- the ring: a vector v of length 8 is sum v[i] z^i; z^8 = z^4 - 1
def times_z(v): return [-v[7], v[0], v[1], v[2], v[3] + v[7], v[4], v[5], v[6]]
def times_zk(v, k):
    for _ in range(k % 24): v = times_z(v)
    return v
ZERO = [0] * 8; ONE = [1] + [0] * 7
assert times_zk(ONE, 24) == ONE and times_zk(ONE, 12) == [-1] + [0] * 7, "z is not a primitive 24th root of unity here"
def times_factor(P, a, m):
    """P(u) (1 - z^a u^m), truncated at ORDER"""
    out = [list(c) for c in P]
    for k in range(m, ORDER + 1):
        t = times_zk(P[k - m], a); out[k] = [x - y for x, y in zip(out[k], t)]
    return out
def cycles(M):
    p, e = M; seen, out = set(), []
    for j in range(3):
        if j in seen: continue
        k, ph, c = j, 0, 0
        while k not in seen: seen.add(k); ph += e[k]; c += 1; k = p[k]
        out.append((c, ph % 24))
    return out
CHECKS = []
def check(name, ok, detail=""):
    CHECKS.append({"check": name, "holds": bool(ok), "detail": str(detail)[:300]}); print("%s  %s%s" % ("ok  " if ok else "FAIL", name, ("  [%s]" % str(detail)[:260]) if detail else ""), flush=True)
P = [list(ONE)] + [list(ZERO) for _ in range(ORDER)]; Pp = [list(c) for c in P]
kinds = collections.Counter(); okdet, classes_ok, n_threads = True, True, 0
for n in range(1, ORDER + 1):
    for w in lyndon(n):
        M = word(w); cy = cycles(M)
        for c, ph in cy:
            P = times_factor(P, ph, n * c)
            if n != 2: Pp = times_factor(Pp, ph, n * c)
        if n == 1: continue
        n_threads += 1; kind = {1: "a 3-cycle", 2: "a transposition", 3: "the identity"}[len(cy)]; kinds[kind] += 1
        classes_ok &= ((trace2(w) % 2 == 1) == (kind == "a 3-cycle"))
        if kind == "a 3-cycle": okdet &= (cy[0][1] == (12 * n + 3 * (w.count("L") - w.count("R"))) % 24)
sqrt2 = [a + b for a, b in zip(times_zk(ONE, 3), times_zk(ONE, 21))]             # z^3 + z^-3 = 2 cos 45 degrees
sq = ZERO
for i, c in enumerate(sqrt2):
    if c: sq = [x + c * y for x, y in zip(sq, times_zk(sqrt2, i))]
check("z^3 + z^-3 squares to 2 in the ring, so it is sqrt 2", sq == [2] + [0] * 7, sqrt2)
target = [list(ONE), [-x for x in sqrt2], list(ONE), list(sqrt2)] + [list(ZERO) for _ in range(ORDER - 3)]
check("the threads to length %d by their act on the three parities, a 3-cycle exactly at odd trace" % ORDER, classes_ok, "%d threads: %s" % (n_threads, dict(kinds)))
check("for every odd-trace thread the factor is 1 - det T(w) u^(3|w|), with det T(w) = (-1)^|w| exp(i pi (#L - #R) / 4)", okdet, "%d odd-trace threads" % kinds["a 3-cycle"])
check("the product over the two letters and every thread is 1 - sqrt2 u + u^2 + sqrt2 u^3, to order %d, exactly" % ORDER, P == target, "the first five coefficients: %s" % P[:5])
check("planted: with the threads of length 2 left out the product is another series", Pp != target)
json.dump({"threads": n_threads, "kinds": dict(kinds), "checks": CHECKS, "failing": [c["check"] for c in CHECKS if not c["holds"]]}, open(HERE / "the_triplets_thread_factors.json", "w"), indent=1)
print("\n%d checks, %d failing" % (len(CHECKS), sum(1 for c in CHECKS if not c["holds"])))
