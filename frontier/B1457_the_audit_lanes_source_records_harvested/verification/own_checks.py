#!/usr/bin/env python3
"""B1457 -- the load-bearing algebra of the audit lane's source records, re-derived on main.

    python3 own_checks.py      # prints, writes own_checks.json; exit 1 if a check fails

  K1  R41's table: for the complete flag 0 < F1 < F2 < F3 < V of a rank-four module, xi_k = 4 P_k - k Id, and a source
      direction S in the defining five (the four and a determinant line): the pairings tr(xi_k S), k = 1, 2, 3.
      A scalar on the four pairs to zero; U = diag(3,-1,-1,-1,0) to (12, 8, 4); -U to its negative; E00 - E44 to (3, 2, 1).
      And the general statement behind it: tr(xi_k S) = 0 for every k exactly when S is scalar on the four along the flag.
  K2  R57's guard: the abelianisation q: F2 -> Z^2 is natural (q o f = f_ab o q for the golden substitution and for the
      swap), identifies ab with ba, and kills the commutator, which is non-trivial in F2.  A natural quotient that
      forgets order exists; no-selector does not forbid it.
  K3  R54's longitude traces on Ballas' family: 3q + q^-3 on the four, 3/q + q^3 on its dual, 3(q^2 + q^-2) on the
      exterior square; each is the other's value at 1/q where it should be.
  K4  the two-ended count is not available to a one-ended state: every word state has one cusp and b1 = 1 (the first
      24 by SnapPy), while m202 has two cusps -- the object on which the audit lane's sourced three is stated.
"""
import itertools, json, os, sys
from fractions import Fraction as F
out = {}; ok = True

# K1
def pairings(S):
    res = []
    for k in (1, 2, 3):
        xi = [(4 if i < k else 0) - k for i in range(4)]            # diagonal of 4 P_k - k Id in the adapted frame
        res.append(sum(xi[i] * S[i] for i in range(4)))
    return tuple(res)
table = {"T = diag(1,1,1,1,-4)": pairings([1, 1, 1, 1]), "U = diag(3,-1,-1,-1,0)": pairings([3, -1, -1, -1]),
         "-U": pairings([-3, 1, 1, 1]), "E00 - E44": pairings([1, 0, 0, 0])}
out["K1 table"] = {k: list(v) for k, v in table.items()}
k1 = table == {"T = diag(1,1,1,1,-4)": (0, 0, 0), "U = diag(3,-1,-1,-1,0)": (12, 8, 4), "-U": (-12, -8, -4), "E00 - E44": (3, 2, 1)}
# all three pairings vanish iff the diagonal is constant: the 3 x 4 system has rank 3 with kernel the scalars
rows = [[(4 if i < k else 0) - k for i in range(4)] for k in (1, 2, 3)]
def rank(M):
    M = [[F(x) for x in r] for r in M]; r = 0
    for c in range(len(M[0])):
        p = next((i for i in range(r, len(M)) if M[i][c] != 0), None)
        if p is None: continue
        M[r], M[p] = M[p], M[r]
        for i in range(len(M)):
            if i != r and M[i][c] != 0:
                f = M[i][c] / M[r][c]; M[i] = [a - f * b for a, b in zip(M[i], M[r])]
        r += 1
    return r
k1 &= rank(rows) == 3 and all(sum(r) == 0 for r in rows)
out["K1 kernel is the scalars"] = rank(rows) == 3 and all(sum(r) == 0 for r in rows)
ok &= k1; print("K1 R41's pairings:", "PASS" if k1 else "FAIL", out["K1 table"])

# K2
def red(w):
    o = []
    for c in w:
        if o and o[-1] == c.swapcase(): o.pop()
        else: o.append(c)
    return "".join(o)
def inv(w): return w[::-1].swapcase()
def hom(img):
    full = dict(img); full.update({k.swapcase(): inv(v) for k, v in img.items()})
    return lambda w: red("".join(full[c] for c in w))
def q(w): return (sum(1 if c == "a" else -1 if c == "A" else 0 for c in w), sum(1 if c == "b" else -1 if c == "B" else 0 for c in w))
gold, swap = hom({"a": "ab", "b": "a"}), hom({"a": "b", "b": "a"})
gold_ab = lambda v: (v[0] + v[1], v[0]); swap_ab = lambda v: (v[1], v[0])
words = ["".join(w) for L in range(1, 7) for w in itertools.product("abAB", repeat=L) if red("".join(w)) == "".join(w)]
nat = all(q(gold(w)) == gold_ab(q(w)) and q(swap(w)) == swap_ab(q(w)) for w in words)
comm = red("abAB")
k2 = nat and q("ab") == q("ba") and comm != "" and q(comm) == (0, 0) and "ab" != "ba"
out["K2"] = dict(words=len(words), natural=nat, q_ab=q("ab"), q_ba=q("ba"), commutator=comm, its_image=q(comm))
ok &= k2; print("K2 the natural quotient that forgets order:", "PASS" if k2 else "FAIL", out["K2"])

# K3
try:
    import sympy as sp
    x = sp.symbols("q", positive=True); t = x / 2
    m = sp.Matrix([[1, 0, 1, t - 1], [0, 1, 1, t], [0, 0, 1, t + sp.Rational(1, 2)], [0, 0, 0, 1]])
    n = sp.Matrix([[1, 0, 0, 0], [2 + 1 / t, 1, 0, 0], [2, 1, 1, 0], [1, 1, 0, 1]])
    g = {"m": m, "n": n, "M": m.inv(), "N": n.inv()}
    Lg = sp.eye(4)
    for c in "nMNmmNMn": Lg = Lg * g[c]
    T4 = sp.simplify(Lg.trace()); T4d = sp.simplify(Lg.inv().trace())
    T6 = sp.simplify((T4 ** 2 - (Lg * Lg).trace()) / 2)
    k3 = sp.simplify(T4 - (3 * x + x ** -3)) == 0 and sp.simplify(T4d - (3 / x + x ** 3)) == 0 and sp.simplify(T6 - 3 * (x ** 2 + x ** -2)) == 0 \
        and sp.simplify(T4d - T4.subs(x, 1 / x)) == 0
    out["K3"] = dict(T4=str(sp.factor(T4)), T4_dual=str(sp.factor(T4d)), T6=str(sp.factor(T6)))
except Exception as exc:
    k3 = False; out["K3"] = "not run: %r" % (exc,)
ok &= k3; print("K3 the longitude traces:", "PASS" if k3 else "FAIL", out["K3"])

# K4
try:
    import snappy, warnings
    warnings.filterwarnings("ignore")
    names = ["m004", "m003", "m009", "m010", "m369", "s639", "m207"]
    cusps = {nm: (snappy.Manifold(nm).num_cusps(), snappy.Manifold(nm).homology().betti_number()) for nm in names}
    two = {nm: (snappy.Manifold(nm).num_cusps(), snappy.Manifold(nm).homology().betti_number()) for nm in ("m202", "s959")}
    k4 = all(v == (1, 1) for v in cusps.values()) and all(v[0] == 2 for v in two.values())
    out["K4"] = dict(one_ended=cusps, two_ended=two)
except Exception as exc:
    k4 = False; out["K4"] = "not run: %r" % (exc,)
ok &= k4; print("K4 ends:", "PASS" if k4 else "FAIL", out["K4"])
json.dump(out, open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "own_checks.json"), "w"), indent=1, default=str)
print("VERDICT audit-own-checks: %s" % ("PASS" if ok else "FAIL")); sys.exit(0 if ok else 1)
