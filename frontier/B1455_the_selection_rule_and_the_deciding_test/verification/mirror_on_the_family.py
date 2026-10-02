#!/usr/bin/env python3
"""B1455, Route 1 -- what the figure-eight's symmetries do to Ballas' family rho_q, by characters, exactly.

    python3 mirror_on_the_family.py        # prints the tables, writes mirror_on_the_family.json; exit 1 on a failed control

Sealed design (PREREGISTRATION.md, commit 12ed66bd): C0 controls, C1 the eight candidate maps, C2 the test.
Exact rational arithmetic (fractions) at q = 2, 3, 5/2, 7/3, 1/5; symbolic in q on short words (sympy).
The group: <m, n | m n M N m N M n m N>, capitals inverses.  rho_q(m), rho_q(n): Ballas, arXiv:1403.3314v3, p. 17, t = q/2.
"""
import itertools, json, os, sys
from fractions import Fraction as F

REL = "mnMNmNMnmN"
LONG = "nMNmmNMn"            # Ballas p. 17: l = n m^-1 n^-1 m^2 n^-1 m^-1 n
QS = [F(2), F(3), F(5, 2), F(7, 3), F(1, 5)]


def mul(A, B): return [[sum(A[i][k] * B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]
def ident(n): return [[F(int(i == j)) for j in range(n)] for i in range(n)]
def tr(A): return sum(A[i][i] for i in range(len(A)))
def transpose(A): return [list(r) for r in zip(*A)]


def inverse(A):
    n = len(A); M = [list(A[i]) + [F(int(i == j)) for j in range(n)] for i in range(n)]
    for c in range(n):
        p = next(r for r in range(c, n) if M[r][c] != 0); M[c], M[p] = M[p], M[c]
        M[c] = [v / M[c][c] for v in M[c]]
        for r in range(n):
            if r != c and M[r][c] != 0: M[r] = [a - M[r][c] * b for a, b in zip(M[r], M[c])]
    return [row[n:] for row in M]


def ballas(q):
    t = F(q) / 2
    m = [[F(1), F(0), F(1), t - 1], [F(0), F(1), F(1), t], [F(0), F(0), F(1), t + F(1, 2)], [F(0), F(0), F(0), F(1)]]
    n = [[F(1), F(0), F(0), F(0)], [2 + 1 / t, F(1), F(0), F(0)], [F(2), F(1), F(1), F(0)], [F(1), F(1), F(0), F(1)]]
    return {"m": m, "n": n, "M": inverse(m), "N": inverse(n)}


def dual(g):
    """the contragredient: x -> rho(x)^{-T}"""
    return {"m": transpose(g["M"]), "n": transpose(g["N"]), "M": transpose(g["m"]), "N": transpose(g["n"])}


def word(w, g):
    A = ident(len(g["m"]))
    for c in w: A = mul(A, g[c])
    return A


SWAP = str.maketrans("mnMN", "MNmn")
def inv_word(w): return w[::-1].translate(SWAP)

# the eight candidate maps: images of m and n
CANDS = {"id": ("m", "n"), "m,N": ("m", "N"), "M,n": ("M", "n"), "iota": ("M", "N"),
         "swap": ("n", "m"), "n,M": ("n", "M"), "N,m": ("N", "m"), "N,M": ("N", "M")}


def apply(sig, w):
    a, b = CANDS[sig]
    img = {"m": a, "n": b, "M": inv_word(a), "N": inv_word(b)}
    return "".join(img[c] for c in w)


def pulled(sig, g):
    """rho o sigma, as a table on the four letters"""
    return {c: word(apply(sig, c), g) for c in "mnMN"}


def positive_words(maxlen):
    for L in range(1, maxlen + 1):
        for w in itertools.product("mn", repeat=L): yield "".join(w)


WORDS = list(positive_words(10))


def chars(g):
    """traces of all positive words to length 10, by extending products"""
    out = {}; level = {"": ident(4)}
    for L in range(1, 11):
        nxt = {}
        for w, A in level.items():
            for c in "mn":
                B = mul(A, g[c]); nxt[w + c] = B; out[w + c] = tr(B)
        level = nxt
    return out


def same(c1, c2): return all(c1[w] == c2[w] for w in WORDS)


def targets(q):
    g, h = ballas(q), ballas(1 / F(q))
    return {"rho_q": g, "rho_q*": dual(g), "rho_1/q": h, "rho_1/q*": dual(h)}


def geo():
    """the SL(2,C) holonomy with m = [[1,1],[0,1]], n = [[1,0],[z,1]], exactly, as pairs (a, b) = a + b*w, w = e^{2 pi i/3}"""
    class E:                                              # the Eisenstein field Q(w), w^2 = -1 - w
        def __init__(s, a, b=0): s.a, s.b = F(a), F(b)
        def __add__(s, o): return E(s.a + o.a, s.b + o.b)
        def __sub__(s, o): return E(s.a - o.a, s.b - o.b)
        def __mul__(s, o): return E(s.a * o.a - s.b * o.b, s.a * o.b + s.b * o.a - s.b * o.b)
        def __eq__(s, o): return (s.a, s.b) == (o.a, o.b)
        def conj(s): return E(s.a - s.b, -s.b)            # w -> w^2 = -1 - w
        def tup(s): return (str(s.a), str(s.b))
    def mm(A, B): return [[A[i][0] * B[0][j] + A[i][1] * B[1][j] for j in range(2)] for i in range(2)]
    one, zero = E(1), E(0)
    out = None
    for z in (E(0, 1), E(-1, -1), E(1, 1), E(0, -1)):      # w, w^2, -w^2, -w
        g = {"m": [[one, one], [zero, one]], "M": [[one, E(-1)], [zero, one]],
             "n": [[one, zero], [z, one]], "N": [[one, zero], [zero - z, one]]}
        R = [[one, zero], [zero, one]]
        for c in REL: R = mm(R, g[c])
        if R == [[one, zero], [zero, one]]: out = (g, mm, E); break
    assert out is not None, "no parabolic representation found among the four candidates"
    return out


def zero_sum_words(maxlen=6):
    for L in range(2, maxlen + 1):
        for w in itertools.product("mnMN", repeat=L):
            w = "".join(w)
            if any(w[i] == w[i + 1].swapcase() for i in range(L - 1)): continue
            if sum(1 if c.islower() else -1 for c in w) == 0: yield w


def main():
    res = {}; ok = True
    # ---- C0: the instrument separates the four targets off q = 1 and not at q = 1
    c0 = {}
    for q in QS:
        T = targets(q); ch = {k: chars(v) for k, v in T.items()}
        c0[str(q)] = {a + " ~ " + b: same(ch[a], ch[b]) for a, b in itertools.combinations(T, 2)}
        R = word(REL, T["rho_q"]); assert R == ident(4), "relator at q = %s" % q
    T1 = targets(F(1)); ch1 = {k: chars(v) for k, v in T1.items()}
    c0["1"] = {a + " ~ " + b: same(ch1[a], ch1[b]) for a, b in itertools.combinations(T1, 2)}
    res["C0"] = c0
    control = all(not c0[str(q)]["rho_q ~ rho_1/q"] and not c0[str(q)]["rho_q ~ rho_q*"] for q in QS) and all(c0["1"].values())
    print("C0 controls: rho_q is not rho_1/q and not rho_q* off q = 1, and all four agree at q = 1:", control)
    print("   rho_q* ~ rho_1/q at each q:", {str(q): c0[str(q)]["rho_q* ~ rho_1/q"] for q in QS})
    ok &= control
    # ---- C1: automorphisms, orientation, meridian and longitude
    g2, mm2, E = geo()
    def w2(w):
        A = [[E(1), E(0)], [E(0), E(1)]]
        for c in w: A = mm2(A, g2[c])
        return A
    zw = list(zero_sum_words(6))
    c1 = {}
    for sig in CANDS:
        auto = all(word(apply(sig, REL), ballas(q)) == ident(4) for q in QS[:3])
        row = {"automorphism": auto}
        if auto:
            t_plain = all((lambda A, B: A[0][0] + A[1][1] == B[0][0] + B[1][1])(w2(apply(sig, w)), w2(w)) for w in zw)
            t_conj = all((lambda A, B: (A[0][0] + A[1][1]) == (B[0][0] + B[1][1]).conj())(w2(apply(sig, w)), w2(w)) for w in zw)
            row["orientation"] = "preserved" if t_plain and not t_conj else "reversed" if t_conj and not t_plain else "undecided(%s,%s)" % (t_plain, t_conj)
            # the longitude: trace of rho_q(sigma(l)) against the traces of l and of l^-1
            lg = {}
            for q in QS:
                g = ballas(q); tl, tli = tr(word(LONG, g)), tr(word(inv_word(LONG), g)); ts = tr(word(apply(sig, LONG), g))
                lg[str(q)] = "l" if ts == tl and ts != tli else "l^-1" if ts == tli and ts != tl else "?"
            row["longitude_goes_to"] = sorted(set(lg.values()))
        c1[sig] = row
    res["C1"] = c1; res["zero_sum_words_used"] = len(zw)
    print("C1:")
    for k, v in c1.items(): print("   %-5s %s" % (k, v))
    # ---- C2: the test
    c2 = {}
    for sig, row in c1.items():
        if not row["automorphism"]: continue
        hit = {}
        for q in QS:
            T = targets(q); cs = chars(pulled(sig, T["rho_q"]))
            hit[str(q)] = [k for k, v in T.items() if same(cs, chars(v))]
        c2[sig] = hit
    res["C2"] = c2
    print("C2: rho_q o sigma is conjugate to")
    for k, v in c2.items(): print("   %-5s %s" % (k, {q: h for q, h in v.items()}))
    # the count-odd mirrors: Theta_sigma(rho_q) = (rho_q o sigma)^*  fixes rho_q  iff  rho_q o sigma ~ rho_q*
    theta_fix = {sig: all("rho_q*" in v[str(q)] for q in QS) for sig, v in c2.items()}
    bare_fix = {sig: all("rho_q" in v[str(q)] for q in QS) for sig, v in c2.items()}
    swaps_q = {sig: all("rho_1/q" in v[str(q)] for q in QS) for sig, v in c2.items()}
    res["Theta_sigma_fixes_every_vacuum"] = theta_fix; res["bare_sigma_fixes_every_vacuum"] = bare_fix; res["bare_sigma_sends_q_to_1/q"] = swaps_q
    print("Theta_sigma fixes every rho_q:", [s for s, v in theta_fix.items() if v])
    print("bare sigma fixes every rho_q :", [s for s, v in bare_fix.items() if v])
    print("bare sigma sends q to 1/q    :", [s for s, v in swaps_q.items() if v])
    none = [s for s, v in c2.items() if any(not h for h in v.values())]
    res["outside_the_family"] = none
    print("sigma taking the family outside the four targets (outcome C):", none)
    # ---- symbolic in q on short words
    try:
        import sympy as sp
        q = sp.symbols("q", positive=True)
        def B(qq):
            t = qq / 2
            m = sp.Matrix([[1, 0, 1, t - 1], [0, 1, 1, t], [0, 0, 1, t + sp.Rational(1, 2)], [0, 0, 0, 1]])
            n = sp.Matrix([[1, 0, 0, 0], [2 + 1 / t, 1, 0, 0], [2, 1, 1, 0], [1, 1, 0, 1]])
            return {"m": m, "n": n, "M": m.inv(), "N": n.inv()}
        def W(w, g):
            A = sp.eye(4)
            for c in w: A = A * g[c]
            return A
        g, h = B(q), B(1 / q)
        dg = {c: g[c.swapcase()].T for c in "mnMN"}
        sym = {"longitude trace": str(sp.factor(sp.simplify(W(LONG, g).trace()))),
               "longitude inverse trace": str(sp.factor(sp.simplify(W(inv_word(LONG), g).trace())))}
        short = [w for w in WORDS if len(w) <= 4]
        sym["rho_q* ~ rho_1/q on words to length 4"] = all(sp.simplify(W(w, dg).trace() - W(w, h).trace()) == 0 for w in short)
        sym["rho_q o iota ~ rho_q* on words to length 4"] = all(sp.simplify(W(apply("iota", w), g).trace() - W(w, dg).trace()) == 0 for w in short)
        res["symbolic"] = sym
        print("symbolic:", sym)
    except Exception as exc:                               # the exact rational run above is the result; this is a second look
        res["symbolic"] = "not run: %r" % (exc,)
    json.dump(res, open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "mirror_on_the_family.json"), "w"), indent=1)
    print("VERDICT mirror-on-the-family: %s" % ("controls PASS" if ok else "controls FAIL"))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
