"""B1812, Review 73 (2026-10-30; main's check of its reader's finding, own code: integer matrices, no sympy, nothing reused
from e_n_monodromy.py).  DHIZ-I (2.4): branes X_1..X_n in order have monodromy K = K_{X_n} ... K_{X_1},
K_[p,q] = [[1+pq, -p^2], [q^2, 1-pq]], A = [1,0], B = [1,-1], C = [1,1].  For every contiguous sub-collection of E_10's
configuration A^9 B C C: its monodromy's trace and its Kodaira match -- conjugate (by search) to the fibre's standard
monodromy, with the brane number equal to the fibre's Euler number -- and so whether it can collapse to a point.
    python3 review73_subcollections.py      # writes review73_subcollections.json beside itself"""
import itertools, json, pathlib, sys
def mul(X, Y): return [[X[0][0]*Y[0][0]+X[0][1]*Y[1][0], X[0][0]*Y[0][1]+X[0][1]*Y[1][1]], [X[1][0]*Y[0][0]+X[1][1]*Y[1][0], X[1][0]*Y[0][1]+X[1][1]*Y[1][1]]]
def K(p, q): return [[1+p*q, -p*p], [q*q, 1-p*q]]
BR = {"A": K(1, 0), "B": K(1, -1), "C": K(1, 1)}
def mono(word):
    M = [[1, 0], [0, 1]]
    for x in word: M = mul(BR[x], M)          # K_{X_n} ... K_{X_1}: each later brane multiplies on the left
    return M
def inv(g): return [[g[1][1], -g[0][1]], [-g[1][0], g[0][0]]]
def conj(X, Y, r=12):
    for a, b, c in itertools.product(range(-r, r+1), repeat=3):
        if a == 0 or (1 + b*c) % a: continue
        g = [[a, b], [c, (1 + b*c)//a]]
        if mul(mul(g, X), inv(g)) == Y: return g
    return None
T = [[1, 1], [0, 1]]; S = [[0, -1], [1, 0]]; I = [[1, 0], [0, 1]]
def neg(M): return [[-x for x in r] for r in M]
def pw(M, n):
    P = I
    for _ in range(abs(n)): P = mul(P, M if n > 0 else inv(M))
    return P
ST = mul(S, T)
# Kodaira fibres: (name, algebra, Euler number, a standard monodromy) -- Kodaira's table up to conjugacy and orientation
FIB = [("I_%d" % n, "su(%d)" % n, n, pw(T, n)) for n in range(1, 10)] + [("I_%d" % n, "su(%d)" % n, n, pw(T, -n)) for n in range(1, 10)]
FIB += [("I_%d*" % n, "so(%d)" % (2*n+8), n+6, neg(pw(T, n))) for n in range(0, 6)] + [("I_%d*" % n, "so(%d)" % (2*n+8), n+6, neg(pw(T, -n))) for n in range(0, 6)]
ST2 = mul(ST, ST)
for name, alg, e, F in (("II", "-", 2, ST), ("III", "su(2)", 3, S), ("IV", "su(3)", 4, ST2),
                        ("IV*", "e6", 8, inv(ST2)), ("III*", "e7", 9, inv(S)), ("II*", "e8", 10, inv(ST))):
    FIB += [(name, alg, e, F), (name, alg, e, inv(F))]     # both orientations; the brane number (Euler number) separates X from X*
word = "A" * 9 + "BCC"
rows = []
for i in range(len(word)):
    for j in range(i + 1, len(word) + 1):
        w = word[i:j]; M = mono(w); t = M[0][0] + M[1][1]; n = len(w)
        hit = None
        for name, alg, e, F in FIB:
            if e == n and (F[0][0] + F[1][1]) == t and conj(M, F) is not None: hit = (name, alg); break
        rows.append({"sub": "A^%dB%s" % (w.count("A"), "C" * w.count("C")) if "B" in w else ("A^%d" % w.count("A") if set(w) == {"A"} else w),
                     "word": w, "branes": n, "trace": t, "collapsible_as": hit})
seen = {}
for r in rows: seen.setdefault(r["word"], r)
out = sorted(seen.values(), key=lambda r: (r["branes"], r["word"]))
for r in out: print("%-14s branes %2d  trace %3d  %s" % (r["word"], r["branes"], r["trace"], r["collapsible_as"] or "not a Kodaira fibre"))
key = {w: seen[w]["collapsible_as"] for w in ("AAAAA", "AAAAABC", "AAAAABCC", "AAABCC", "AABCC", "AAA", "AA")}
print(json.dumps(key))
pathlib.Path(__file__).with_suffix(".json").write_text(json.dumps({"sub_collections": out, "chain": {w: key[w] for w in key}}, indent=1), encoding="utf-8")
# the nested chain su(5) < so(10) < e6 as nested contiguous sub-collections of A^9BCC
assert key["AAAAA"] == ("I_5", "su(5)") and key["AAAAABC"] == ("I_1*", "so(10)") and key["AAAAABCC"] == ("IV*", "e6")
assert key["AAABCC"] is None and key["AABCC"] is None          # E_4 and E_3: hyperbolic, not collapsible (B1812's computation)
assert key["AAA"] == ("I_3", "su(3)") and key["AA"] == ("I_2", "su(2)")
print("CHECKS PASS")
