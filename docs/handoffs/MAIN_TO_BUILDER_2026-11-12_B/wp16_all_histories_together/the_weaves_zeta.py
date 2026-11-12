#!/usr/bin/env python3
"""WP-1.6, a first exact object for "all histories together": the generating function of every history, its product over
threads, and the law of its rates.

STATEMENTS (each proved below in the docstring of its part, then checked)
  Z1  In SL(2, Z): L = S U and R = -S U^-1, with S of order 4 (S^2 = -1) and U of order 3.  So a positive word in L and R
      is, up to the central sign, an alternating word S U^e1 S U^e2 ... with every e = +-1: a REDUCED word of the free
      product Z/2 * Z/3 = PSL(2, Z).  Positive words are the words in which no letter cancels another.
  Z2  (Amitsur's identity, 1980; a formal identity for any two square matrices)  For a representation rho,
          det(1 - u (rho(L) + rho(R)))  =  PRODUCT over Lyndon words w in L, R of  det(1 - u^|w| rho(w)).
      The Lyndon words are the two letters and one word for each primitive cyclic word that holds both letters: the
      threads.  So the sum over all histories is a product over threads, with one factor for each of the two letters.
  Z3  In the defining representation: det(1 - u(L + R)) = (1 - u)(1 - 3u), a thread's factor is 1 - tr(w) u^|w| + u^2|w|,
      and so   PRODUCT over threads (1 - tr(w) u^|w| + u^2|w|) = (1 - 3u) / (1 - u)^3.
  Z4  THE RATES.  rho unitary and irreducible, A = (rho(L) + rho(R)) / 2, P1 the projection on the vectors U fixes.
      - even (the sign -1 acts as +1): A = rho(S) (3 P1 - 1) / 2, and rho(S) is a Hermitian involution.  On each plane
        where S and P1 are in general position, at angle t, the two eigenvalues of A multiply to 1/2 and add to
        (3/2) cos 2t: a complex pair of modulus EXACTLY 1/sqrt 2 when |3 cos 2t| <= 2 sqrt 2, a real pair otherwise.
        3 P1 S P1 is the adjacency operator of the three-valent graph of the level (vertices: cosets of U; edges: S).
        So the rate is 1/sqrt 2 exactly when that graph's eigenvalues obey Ramanujan's bound 2 sqrt 2 in the sector;
        the other eigenvalues of A are +-1/2 (and +-1 on a vector both fix, which only a character has).
      - odd (the sign acts as -1): A = (sqrt 3 / 2) (i rho(S)) (Pw - Pw'), with i rho(S) a Hermitian involution and
        Pw, Pw' the projections on U's two other eigenspaces.  So the rate is at most sqrt 3 / 2, and when U fixes no
        vector the product of the two involutions is unitary: EVERY eigenvalue of A has modulus sqrt 3 / 2.
WHAT IS COMPUTED: Z1 on every positive word to length 10; Z2 to order 10 for (L, R) and for two planted pairs of integer
3 by 3 matrices; Z3 to order 14; Z4 on every sector of levels 2 to 13 from rates_by_sector.json, with the three-valent
graph of each level built here and its spectrum computed.
HOW IT COULD FAIL: the planted pair for Z2 with one Lyndon word left out; a planted graph (the same with one edge moved)
for the comparison of the graph's spectrum with the sectors' rates.
Exact integers for Z1 to Z3; double precision for the graphs' spectra.  No measured number.  0 of 19."""
import itertools, json, math, pathlib
import numpy as np

HERE = pathlib.Path(__file__).resolve().parent
CHECKS = []


def check(name, ok, detail=""):
    CHECKS.append({"check": name, "holds": bool(ok), "detail": str(detail)[:400]})
    print("%s  %s%s" % ("ok  " if ok else "FAIL", name, ("  [%s]" % str(detail)[:300]) if detail else ""), flush=True)


def mm(A, B): return tuple(tuple(sum(A[i][k] * B[k][j] for k in range(len(B))) for j in range(len(B[0]))) for i in range(len(A)))
def neg(A): return tuple(tuple(-x for x in r) for r in A)
def eye(n): return tuple(tuple(int(i == j) for j in range(n)) for i in range(n))
L, R = ((1, 1), (0, 1)), ((1, 0), (1, 1))
S, U = ((0, -1), (1, 0)), ((0, 1), (-1, -1))
Ui = mm(U, U)

# ------------------------------------------------------------------------------------------------------------ Z1
check("Z1: S^2 = -1, U^3 = 1, L = S U, R = -S U^-1, in integers",
      mm(S, S) == neg(eye(2)) and mm(U, mm(U, U)) == eye(2) and mm(S, U) == L and neg(mm(S, Ui)) == R)
bad = 0; n_words = 0
for n in range(1, 11):
    for w in itertools.product("LR", repeat=n):
        n_words += 1
        direct = eye(2); alt = eye(2); sign = 1
        for ch in w:
            direct = mm(direct, L if ch == "L" else R)
            alt = mm(mm(alt, S), U if ch == "L" else Ui); sign *= (1 if ch == "L" else -1)
        if direct != (alt if sign == 1 else neg(alt)): bad += 1
check("Z1: every positive word to length 10 is, up to the central sign, the alternating word S U^e S U^e ... (e = +1 for L, -1 for R); the sign is (-1)^(number of R)", bad == 0, "%d words" % n_words)

# --------------------------------------------------------------------------------- polynomials in u with integer coefficients
ORDER = 14
def pmul(a, b, order=ORDER):
    c = [0] * (order + 1)
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b):
                if i + j > order: break
                c[i + j] += x * y
    return c
def det(Mx):
    n = len(Mx)
    if n == 1: return Mx[0][0]
    if n == 2: return Mx[0][0] * Mx[1][1] - Mx[0][1] * Mx[1][0]
    return sum((-1) ** j * Mx[0][j] * det(tuple(tuple(r[k] for k in range(n) if k != j) for r in Mx[1:])) for j in range(n))
def charpoly_in(Mx, power, order=ORDER):
    """det(1 - x M) with x = u^power, as a polynomial in u: the coefficients are the signed sums of principal minors"""
    n = len(Mx); out = [0] * (order + 1); out[0] = 1
    for k in range(1, n + 1):
        if k * power > order: break
        e = sum(det(tuple(tuple(Mx[i][j] for j in idx) for i in idx)) for idx in itertools.combinations(range(n), k))
        out[k * power] += (-1) ** k * e
    return out
def lyndon(n):
    """the Lyndon words of length n on the letters A < B"""
    out = []
    for w in itertools.product("AB", repeat=n):
        s = "".join(w)
        if all(s < s[i:] + s[:i] for i in range(1, n)): out.append(s)
    return out
def amitsur(A, B, order, drop=None):
    lhs = charpoly_in(tuple(tuple(A[i][j] + B[i][j] for j in range(len(A))) for i in range(len(A))), 1, order)
    rhs = [1] + [0] * order; words = 0
    for n in range(1, order + 1):
        for w in lyndon(n):
            if w == drop: continue
            Mx = eye(len(A))
            for ch in w: Mx = mm(Mx, A if ch == "A" else B)
            rhs = pmul(rhs, charpoly_in(Mx, n, order), order); words += 1
    return lhs[:order + 1] == rhs[:order + 1], words, lhs[:6]

# ------------------------------------------------------------------------------------------------------------ Z2
ok, words, head = amitsur(L, R, 10)
check("Z2: Amitsur's identity for (L, R) to order 10: det(1 - u(L + R)) is the product over Lyndon words of det(1 - u^|w| w)", ok, "%d Lyndon words; the left side begins %s" % (words, head))
X = ((2, -1, 0), (1, 3, 1), (0, 1, -2)); Y = ((1, 0, 4), (-2, 1, 1), (3, 0, 1))
ok3, words3, _ = amitsur(X, Y, 8)
check("Z2: the same for a pair of integer 3 by 3 matrices that have nothing to do with the moves, to order 8", ok3, "%d Lyndon words" % words3)
okp, _, _ = amitsur(X, Y, 8, drop="AAB")
check("planted: with one Lyndon word left out of the product the identity fails", not okp)

# ------------------------------------------------------------------------------------------------------------ Z3
lhs = charpoly_in(tuple(tuple(L[i][j] + R[i][j] for j in range(2)) for i in range(2)), 1)
check("Z3: det(1 - u(L + R)) = (1 - u)(1 - 3u)", lhs[:3] == [1, -4, 3] and not any(lhs[3:]))
prod = [1] + [0] * ORDER; threads = 0; traces = {}
for n in range(2, ORDER + 1):
    for w in lyndon(n):
        Mx = eye(2)
        for ch in w: Mx = mm(Mx, L if ch == "A" else R)
        t = Mx[0][0] + Mx[1][1]; f = [0] * (ORDER + 1); f[0] = 1; f[n] -= t
        if 2 * n <= ORDER: f[2 * n] += 1
        prod = pmul(prod, f); threads += 1; traces.setdefault(n, []).append(t)
target = pmul([1, -3] + [0] * (ORDER - 1), [math.comb(k + 2, 2) for k in range(ORDER + 1)])        # (1 - 3u) / (1 - u)^3
check("Z3: the product over threads of (1 - tr(w) u^|w| + u^2|w|) is (1 - 3u) / (1 - u)^3, to order %d" % ORDER, prod == target, "%d threads to length %d; of length 2, 3, 4: traces %s" % (threads, ORDER, [sorted(traces[n]) for n in (2, 3, 4)]))

# ------------------------------------------------------------------------------------------------------------ Z4
def level_graph(N, move_edge=False):
    """the three-valent graph of level N: vertices are the cosets g<U> of PSL(2, Z/N); g<U> is joined to g U^k S <U>, k = 0, 1, 2"""
    red = lambda g: tuple(tuple(x % N for x in r) for r in g)
    canon = lambda g: min(red(g), red(neg(g)))
    one = canon(eye(2)); G = {one}; fr = [one]
    while fr:
        nxt = []
        for g in fr:
            for h in (L, R):
                x = canon(mm(g, h))
                if x not in G: G.add(x); nxt.append(x)
        fr = nxt
    coset = lambda g: min(canon(g), canon(mm(g, U)), canon(mm(g, Ui)))
    V = sorted({coset(g) for g in G}); ix = {v: i for i, v in enumerate(V)}
    Adj = np.zeros((len(V), len(V)))
    for v in V:
        for k in range(3):
            g = v
            for _ in range(k): g = mm(g, U)
            Adj[ix[v], ix[coset(mm(g, S))]] += 1
    if move_edge and len(V) > 3:
        a, b = np.argwhere(Adj > 0)[0]; Adj[a, b] -= 1; Adj[b, a] -= 1; c = (b + 1) % len(V); Adj[a, c] += 1; Adj[c, a] += 1
    return len(G), Adj

rates = json.loads((HERE / "rates_by_sector.json").read_text(encoding="utf-8"))["levels"]
r2, bound = 1 / math.sqrt(2), 2 * math.sqrt(2)
table = {}; all_even_fit = True; all_ramanujan = True
for N in range(2, 14):
    order, Adj = level_graph(N)
    assert np.allclose(Adj, Adj.T) and np.allclose(Adj.sum(1), 3), "the graph is not three-valent and symmetric"
    ev = np.sort(np.linalg.eigvalsh(Adj))[::-1]
    nontriv = [x for x in ev if abs(abs(x) - 3) > 1e-8]
    lam = max((abs(x) for x in nontriv), default=0.0)
    bip = bool(abs(ev[-1] + 3) < 1e-8)
    # what the graph's spectrum predicts for the even sectors: 1/sqrt2 inside the bound, the larger root outside it, and 1/2
    pred = set()
    for x in nontriv:
        pred.add(round(r2, 6) if abs(x) <= bound + 1e-9 else round((abs(x) + math.sqrt(x * x - 8)) / 4, 6))
    even = [s for s in rates[str(N)]["sectors"] if s["sign on -1"] == 1 and s["dimension"] > 1 or (s["sign on -1"] == 1 and s["level"] not in (1, 2))]
    got = {round(s["rate, moves L and R"], 6) for s in rates[str(N)]["sectors"] if s["sign on -1"] == 1 and abs(s["rate, moves L and R"] - 1) > 1e-6}
    fit = got <= (pred | {0.5})
    all_even_fit &= fit; all_ramanujan &= (lam <= bound + 1e-9)
    table[N] = {"order of PSL": order, "vertices": Adj.shape[0], "largest eigenvalue in modulus below 3": round(lam, 6), "within 2 sqrt 2": bool(lam <= bound + 1e-9), "two-coloured (an eigenvalue -3)": bip,
                "rates of the even sectors": sorted(got), "predicted from the graph": sorted(pred | {0.5})}
    print("   level %2d: %4d vertices; largest eigenvalue below 3 in modulus %.6f (2 sqrt 2 = %.6f): %s; two-coloured: %-5s; even sectors' rates %s" % (N, Adj.shape[0], lam, bound, "within" if lam <= bound + 1e-9 else "OUTSIDE", bip, sorted(got)), flush=True)
check("Z4, even: at every level from 2 to 13 the three-valent graph obeys Ramanujan's bound", all_ramanujan, {N: t["largest eigenvalue in modulus below 3"] for N, t in table.items()})
check("Z4, even: and every even sector's rate is one the graph's spectrum predicts: 1/sqrt 2, or 1/2", all_even_fit)
check("Z4: the graph is two-coloured exactly at the even levels, where the sector that never cancels lives (the parity of the number of moves)", all(table[N]["two-coloured (an eigenvalue -3)"] == (N % 2 == 0) for N in table))
odd = [dict(s, N=int(N)) for N, v in rates.items() for s in v["sectors"] if s["sign on -1"] == -1 and s["level"] == int(N)]
top = max(s["rate, moves L and R"] for s in odd)
check("Z4, odd: no odd sector cancels slower than sqrt 3 / 2", top <= math.sqrt(3) / 2 + 1e-7, "the slowest: %.9f; %d odd sectors" % (top, len(odd)))
at = sorted((s["N"], s["dimension"]) for s in odd if abs(s["rate, moves L and R"] - math.sqrt(3) / 2) < 1e-7)
check("Z4, odd: thirteen sectors cancel at exactly sqrt 3 / 2: the two-dimensional ones of levels 3, 4, 5, 6, 8, 10 and four characters of level 12", len(at) == 13 and {d for _, d in at} == {1, 2}, at)
free = [s for s in odd if s["vectors U fixes"] == 0]
check("Z4, odd: in every odd sector where U fixes no vector the rate is sqrt 3 / 2 (the theorem), and those sectors are exactly the thirteen",
      all(abs(s["rate, moves L and R"] - math.sqrt(3) / 2) < 1e-7 for s in free) and sorted((s["N"], s["dimension"]) for s in free) == at, "%d odd sectors where U fixes no vector" % len(free))
evens = [dict(s, N=int(N)) for N, v in rates.items() for s in v["sectors"] if s["sign on -1"] == 1 and s["level"] == int(N) and s["dimension"] > 1]
check("Z4, even: every even sector of dimension above 1 has a vector that U fixes (so each is seen by the level's graph) but for those at rate 1/2",
      all(s["vectors U fixes"] > 0 or abs(s["rate, moves L and R"] - 0.5) < 1e-6 for s in evens), "%d even sectors; %d with no vector U fixes, all at rate 1/2: %s" % (len(evens), sum(1 for s in evens if s["vectors U fixes"] == 0), all(abs(s["rate, moves L and R"] - 0.5) < 1e-6 for s in evens if s["vectors U fixes"] == 0)))
# planted: a graph with one edge moved must not predict the sectors' rates at a level where the true one does
_, bad_graph = level_graph(7, move_edge=True)
evb = np.linalg.eigvalsh(bad_graph); lamb = max(abs(x) for x in evb if abs(abs(x) - 3) > 1e-8)
check("planted: with one edge of the level-7 graph moved, its largest eigenvalue below 3 is no longer the true graph's", abs(lamb - table[7]["largest eigenvalue in modulus below 3"]) > 1e-6, "%.6f against %.6f" % (lamb, table[7]["largest eigenvalue in modulus below 3"]))
res = {"checks": CHECKS, "failing": [c["check"] for c in CHECKS if not c["holds"]], "levels": {str(k): v for k, v in table.items()}, "odd sectors at sqrt 3 / 2": at,
       "threads to length %d" % ORDER: threads}
(HERE / "the_weaves_zeta.json").write_text(json.dumps(res, indent=1) + "\n", encoding="utf-8")
print("\n%d checks, %d failing" % (len(CHECKS), len(res["failing"])))
