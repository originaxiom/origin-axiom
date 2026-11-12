#!/usr/bin/env python3
"""Harvest row 917 on main's own code: the parity trichotomy and Theorem S.

THE STATEMENTS (the SM seat's page on the weave's laws)
  THE TRICHOTOMY.  A state's monodromy phi acts on the three non-zero parities of the two records through phi mod 2,
  an element of GL(2, F_2) = S_3, and its class is fixed by the trace: a 3-cycle at odd trace; an involution at even
  trace with phi not the identity mod 2; the identity otherwise.  At tick n the class is that of (phi mod 2)^n.
  THEOREM S.  At its own tick no state has its three parities both separate and carried into one another by a
  symmetry: they are separate only when phi is the identity mod 2, and then the state's symmetries act on them through
  a group of order at most 2.  At every third tick of an odd-trace state they are both.

WHAT IS COMPUTED HERE, exactly, with integer matrices
  1. the trichotomy on every integer matrix of determinant +-1 with entries from -4 to 4;
  2. the census of main's own list of states to length 12 (B1434's enumerator), both signs: how many of each class,
     by word length; and the classes at ticks 1 to 6 of the states to length 6;
  3. for each state that is the identity mod 2: the image mod 2 of its normaliser in GL(2, Z), that is of every g with
     g phi = phi g or g phi = phi^-1 g.  The centraliser is read from the ring Z[I, E] of integer matrices commuting
     with phi (E = (phi - d)/gcd), whose units are found by solving the norm equation; an inverting element is looked
     for in the integer solutions of g phi = phi^-1 g.  The orbits of that image on the three parities are counted.
The seat's committed output is read as data, to be compared with, at its commit.

HOW IT COULD FAIL: the planted cases at the end: a word that is a cube ((LR)^3 is the identity mod 2 and its
centraliser holds a 3-cycle); a matrix whose class is not its trace's."""
import collections, itertools, json, math, pathlib, subprocess, sys
import sympy
from sympy.matrices.normalforms import smith_normal_decomp

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(ROOT / "frontier" / "B1434_the_architecture_census" / "verification"))
import architecture_census as ac

L, R = ((1, 1), (0, 1)), ((1, 0), (1, 1))
I2 = ((1, 0), (0, 1))
def mul(x, y): return tuple(tuple(sum(x[i][k] * y[k][j] for k in range(2)) for j in range(2)) for i in range(2))
def word(w):
    m = I2
    for ch in w: m = mul(m, L if ch == "L" else R)
    return m
def mod2(m): return tuple(tuple(v % 2 for v in r) for r in m)
def order2(m):
    """the order of m mod 2 in GL(2, F_2)"""
    p, n = mod2(m), 1
    while p != I2: p = mod2(mul(p, m)); n += 1
    return n
KIND = {3: "a 3-cycle", 2: "an involution", 1: "the identity"}
CHECKS = []
def check(name, ok, detail=""):
    CHECKS.append({"check": name, "holds": bool(ok), "detail": str(detail)[:300]}); print("%s  %s%s" % ("ok  " if ok else "FAIL", name, ("  [%s]" % str(detail)[:230]) if detail else ""))

# ------------------------------------------------------------------------------------------------- 1. the trichotomy
B = 4
mats = [((a, b), (c, d)) for a, b, c, d in itertools.product(range(-B, B + 1), repeat=4) if a * d - b * c in (1, -1)]
bad = [m for m in mats if (order2(m) == 3) != ((m[0][0] + m[1][1]) % 2 == 1) or (order2(m) == 1) != (mod2(m) == I2)]
check("1: on every integer matrix of determinant +-1 with entries from -%d to %d the class mod 2 is a 3-cycle exactly at odd trace" % (B, B), not bad, "%d matrices" % len(mats))

# --------------------------------------------------------------------------------------------------- 2. the census
states = [(eps, w) for w in ac.states(12) for eps in "+-"]
kinds = collections.Counter(); by_len = collections.defaultdict(collections.Counter)
for eps, w in states:
    k = KIND[order2(word(w))]; kinds[k] += 1; by_len[len(w)][k] += 1
check("2: main's list has 758 states to length 12, both signs", len(states) == 758, len(states))
check("2: the class is a 3-cycle exactly at odd trace on every state", all((order2(word(w)) == 3) == (sum(word(w)[i][i] for i in range(2)) % 2 == 1) for eps, w in states))
ticks = {eps + w: [order2(mul_pow) for mul_pow in itertools.accumulate([word(w)] * 6, mul)] for eps, w in states if len(w) <= 6}
check("2: at tick n the class is that of the n-th power: an odd-trace state is the identity mod 2 at ticks 3 and 6 and a 3-cycle at 1, 2, 4, 5",
      all(v == [3, 3, 1, 3, 3, 1] for k, v in ticks.items() if order2(word(k[1:])) == 3), "%d states to length 6" % len(ticks))

# ---------------------------------------------------------------- 3. the normaliser of a state that is the identity mod 2
def centraliser_units(phi):
    """the units x + y E of the ring of integer matrices commuting with phi, with 0 <= y <= gcd; phi itself is among them"""
    (a, b), (c, d) = phi
    g = math.gcd(math.gcd(abs(b), abs(c)), abs(a - d))
    E = (((a - d) // g, b // g), (c // g, 0))
    t, n = (a - d) // g, (b * c) // (g * g)             # det(x + yE) = x^2 + x y t - y^2 n
    out = []
    for y in range(0, g + 1):
        for s in (1, -1):
            D = y * y * t * t + 4 * (y * y * n + s)
            if D < 0: continue
            r = math.isqrt(D)
            if r * r != D: continue
            for num in (-y * t + r, -y * t - r):
                if num % 2 == 0:
                    x = num // 2
                    m = ((x + y * E[0][0], y * E[0][1]), (y * E[1][0], x))
                    assert mul(m, phi) == mul(phi, m) and m[0][0] * m[1][1] - m[0][1] * m[1][0] in (1, -1)
                    out.append(m)
    return out

def inverting(phi, bound=40):
    """an integer g of determinant +-1 with g phi = phi^-1 g, with small coefficients in a basis of the solutions; or None"""
    (a, b), (c, d) = phi
    inv = ((d, -b), (-c, a))
    # unknowns p, q, r, s of g = ((p, q), (r, s)); the four equations of g phi - inv g = 0
    rows = []
    for i in range(2):
        for j in range(2):
            coef = [0, 0, 0, 0]
            for k in range(2):
                coef[2 * i + k] += phi[k][j]            # (g phi)_{ij} = sum_k g_{ik} phi_{kj}
                coef[2 * k + j] -= inv[i][k]            # (inv g)_{ij} = sum_k inv_{ik} g_{kj}
            rows.append(coef)
    A = sympy.Matrix(rows)
    S, U, V = smith_normal_decomp(A, sympy.ZZ)          # S = U A V; the kernel is spanned by the columns of V over the zero diagonal
    ker = [[int(V[i, j]) for i in range(4)] for j in range(4) if j >= min(S.shape) or S[j, j] == 0]
    assert len(ker) == 2 and all(all(sum(rows[e][k] * v[k] for k in range(4)) == 0 for e in range(4)) for v in ker)
    v1, v2 = ker
    for x in range(0, bound + 1):
        for y in range(-bound, bound + 1):
            if x == 0 and y <= 0: continue
            p, q, r, s = (x * v1[k] + y * v2[k] for k in range(4))
            if p * s - q * r in (1, -1):
                g = ((p, q), (r, s))
                assert mul(g, phi) == mul(inv, g)
                return g
    return None

def image_mod2(phi):
    gens = {mod2(u) for u in centraliser_units(phi)}
    g = inverting(phi)
    if g is not None:
        gens.add(mod2(g))
    G = {I2}; frontier = [I2]
    while frontier:
        nxt = []
        for h in frontier:
            for k in gens:
                x = mod2(mul(h, k))
                if x not in G: G.add(x); nxt.append(x)
        frontier = nxt
    return G, g is not None

PAR = [(1, 0), (0, 1), (1, 1)]
def orbits(G):
    seen, out = set(), []
    for v in PAR:
        if v in seen: continue
        orb = {tuple((m[i][0] * v[0] + m[i][1] * v[1]) % 2 for i in range(2)) for m in G}
        seen |= orb; out.append(len(orb))
    return "+".join(str(x) for x in sorted(out))

ident = [(eps, w) for eps, w in states if order2(word(w)) == 1]
pattern = collections.Counter(); sizes = collections.Counter(); with_inv = 0
for eps, w in ident:
    G, has_inv = image_mod2(word(w))
    pattern[orbits(G)] += 1; sizes[len(G)] += 1; with_inv += has_inv
check("3: 164 states are the identity mod 2", len(ident) == 164, len(ident))
check("3: on each of them the normaliser acts on the three parities through a group of order at most 2", set(sizes) <= {1, 2}, dict(sizes))
check("3: so never one orbit of three", "3" not in pattern, dict(pattern))

# ------------------------------------------------------------------------------- the seat's output, at its commit, as data
raw = subprocess.run(["git", "show", "cecf33c11:docs/dossiers/the_weave_2026-10-07/the_weaves_laws.json"], capture_output=True, text=True, cwd=str(ROOT)).stdout
seat = json.loads(raw)
s1 = seat["(1) the parity trichotomy, along the wave"]; s3 = seat["(3) no state has its three parities separate and alike at its own tick"]
mine_kind = {"a 3-cycle mod 2: one orbit": kinds["a 3-cycle"], "an involution mod 2: a line and a pair": kinds["an involution"], "identity mod 2: three lines": kinds["the identity"]}
check("the seat's count of states and of each class are main's", s1["states of GENESIS to length 12 (both signs)"] == len(states) and s1["by kind"] == mine_kind, mine_kind)
names = {"a 3-cycle": "a 3-cycle mod 2: one orbit", "an involution": "an involution mod 2: a line and a pair", "the identity": "identity mod 2: three lines"}
mine_len = {str(n): {names[k]: v for k, v in sorted(c.items())} for n, c in sorted(by_len.items())}
check("the seat's table by word length is main's", {k: dict(sorted(v.items())) for k, v in s1["by word length"].items()} == {k: dict(sorted(v.items())) for k, v in mine_len.items()})
check("the seat's ticks of the states to length 6 are main's", {x["state"]: x["orders at ticks 1-6"] for x in s1["the states to length 6"]} == ticks, "%d states" % len(ticks))
check("the seat's orbits of the symmetries on the 164 are main's", s3["orbits of their isometries on the three parities"] == dict(pattern), dict(pattern))

# --------------------------------------------------------------------------------------------------------- planted
cube = word("LRLRLR")
Gc, _ = image_mod2(cube)
check("planted: the cube of LR is the identity mod 2 and its centraliser holds a 3-cycle, so a word that is a power would break the theorem",
      order2(cube) == 1 and len(Gc) >= 3, "the image has %d elements" % len(Gc))
check("planted: the matrix ((1, 1), (1, 0)) has odd trace and is a 3-cycle; ((1, 2), (0, 1)) has even trace and is the identity", order2(((1, 1), (1, 0))) == 3 and order2(((1, 2), (0, 1))) == 1)
res = {"checks": CHECKS, "failing": [c["check"] for c in CHECKS if not c["holds"]], "states": len(states), "by kind": dict(kinds), "by word length": mine_len,
       "the identity mod 2": len(ident), "orbits of the normaliser on the three parities": dict(pattern), "sizes of its image": {str(k): v for k, v in sizes.items()},
       "states with an inverting element found": with_inv, "matrices of part 1": len(mats)}
(HERE / "row917_the_trichotomy_and_theorem_s.json").write_text(json.dumps(res, indent=1) + "\n", encoding="utf-8")
print("\n%d checks, %d failing" % (len(CHECKS), len(res["failing"])))
