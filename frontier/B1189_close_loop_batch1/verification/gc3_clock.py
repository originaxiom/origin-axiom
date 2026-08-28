# GC-3 THE CLOCK: adjudicate the three tick candidates + reconcile the arrow contradiction.
# All facts exact (sympy / integer arithmetic); every check is a hard assert.
# Two-sided controls marked [CONTROL+] (recover known positive) / [CONTROL-] (exclude absent target).

import itertools
from sympy import Matrix, eye, symbols, sqrt, simplify, expand, Rational, diff

OUT = []
def say(s):
    OUT.append(s); print(s)

# ---------------------------------------------------------------- Part 1: the tick algebra
R = Matrix([[1, 1], [0, 1]]); L = Matrix([[1, 0], [1, 1]])
RL = R * L
M = Matrix([[1, 1], [1, 0]])
assert RL == Matrix([[2, 1], [1, 1]])
assert M.det() == -1
assert M**2 == RL
say("P1: RL = [[2,1],[1,1]]; M=[[1,1],[1,0]]; det M = -1; M^2 = RL  (B1083 re-derived) OK")

# Exhaustive integer square roots of RL (Cayley-Hamilton: K^2 = tK - dI => tr(K^2)=t^2-2d=3, det=d^2=1)
roots = []
for d in (1, -1):
    for t in range(-20, 21):
        if t == 0 or t * t - 2 * d != 3:
            continue
        K = (RL + d * eye(2)) / t
        if all(x.is_Integer for x in K):
            K = Matrix(2, 2, [int(x) for x in K])
            if K**2 == RL:
                roots.append((t, d, tuple(K)))
# t=0 => K^2 = -dI != RL (RL not scalar). d=+1 => t^2=5 impossible over Z.
brute = [Matrix([[a, b], [c, e]]) for a, b, c, e in itertools.product(range(-4, 5), repeat=4)
         if Matrix([[a, b], [c, e]])**2 == RL]
say(f"P2: integer square roots of RL (Cayley-Hamilton exhaustive): {roots}")
say(f"    brute force |entries|<=4 finds {len(brute)} roots: {[tuple(b) for b in brute]}")
assert len(brute) == 2 and all(b.det() == -1 for b in brute)
assert sorted(tuple(b) for b in brute) == sorted([tuple(M), tuple(-M)])
say("P2: ONLY +/-M, both det -1. [CONTROL-] det=+1 square root of RL: d=+1 forces t^2=5, NO integer"
    " solution -- a det +1 halving of the double tick is EXCLUDED. The Breath (det -1) is FORCED.")

# ---------------------------------------------------------------- Part 2: conductor clock table
def ord_mod(A, m, cap=200000):
    A = [[int(A[0, 0]) % m, int(A[0, 1]) % m], [int(A[1, 0]) % m, int(A[1, 1]) % m]]
    B = [row[:] for row in A]
    for n in range(1, cap + 1):
        if B[0][0] % m == 1 and B[1][1] % m == 1 and B[0][1] % m == 0 and B[1][0] % m == 0:
            return n
        B = [[(B[0][0] * A[0][0] + B[0][1] * A[1][0]) % m, (B[0][0] * A[0][1] + B[0][1] * A[1][1]) % m],
             [(B[1][0] * A[0][0] + B[1][1] * A[1][0]) % m, (B[1][0] * A[0][1] + B[1][1] * A[1][1]) % m]]
    return None

banked_clock = {k + 3: v for k, v in enumerate([1, 10, 12, 8, 12, 36, 60, 20, 12, 28, 24, 60], start=1)}
# banked_clock[kappa] for kappa=4..15 (B585 k=1..12)
expected_ord = {4: 12, 5: 20}  # B656 anomaly rows
rows = []
halving_ok = True
for kap in range(4, 16):
    oRL = ord_mod(RL, 3 * kap)
    oM = ord_mod(M, 3 * kap)
    oU = ord_mod(Matrix([[1, 1], [0, 1]]), 3 * kap)   # [CONTROL-] deliberately-absent candidate
    onaive = ord_mod(RL, kap)                          # B596's failed naive modulus
    clk = banked_clock[kap]
    match = (oRL == clk)
    rows.append((kap, clk, oRL, oM, oU, onaive, match))
    if oM != 2 * oRL:
        halving_ok = False
say("P3: kappa | banked clock | ord(RL mod 3k) | ord(M mod 3k) | ord(unipotent mod 3k) | ord(RL mod k) | clock==ord")
for r in rows:
    say("    " + str(r))
assert all(r[2] == r[1] for r in rows if r[0] >= 6), "conductor law kappa=6..15 must reproduce"
assert rows[0][2] == 12 and rows[1][2] == 20, "anomaly rows must be 12, 20"
assert halving_ok, "Breath halving ord(M)=2*ord(RL) must hold at every conductor"
say("P3: kappa=6..15 EXACT 10/10 [CONTROL+ banked table recovered]; kappa=4: clock 1 vs ord 12,"
    " kappa=5: clock 10 vs ord 20 (the banked anomaly rows, reproduced).")
say("P3: ord(M mod 3k) = 2*ord(RL mod 3k) at ALL 12 conductors -- the Breath Z/2 halving is exact"
    " at every modulus: conductor clock = (single-tick clock)/Breath.")
mismU = sum(1 for r in rows if r[4] != r[1])
mismN = sum(1 for r in rows if r[5] != r[1])
say(f"P3 [CONTROL-]: unipotent [[1,1],[0,1]] mismatches banked clock on {mismU}/12 rows;"
    f" naive modulus ord(RL mod kappa) mismatches on {mismN}/12 rows (B596's negative recovered).")
assert mismU >= 10 and mismN >= 6

# det character: det(M^j) = (-1)^j -- the Breath IS the det character of the tick clock
assert all((M**j).det() == (-1) ** j for j in range(1, 9))
say("P4: det(M^j) = (-1)^j for j=1..8 -- the Breath Z/2 = the det character of <M>; kernel = <M^2>=<RL>.")

# ---------------------------------------------------------------- Part 3: memo-49 substitution clock = same GL(2,Z) class as RL
Cmp = Matrix([[0, -1], [1, 3]])  # memo 49 fiber-substitution abelianization, charpoly x^2-3x+1
assert Cmp.charpoly().as_expr() == RL.charpoly().as_expr()
conj = []
for a, b, c, e in itertools.product(range(-5, 6), repeat=4):
    P = Matrix([[a, b], [c, e]])
    if abs(P.det()) == 1 and P * Cmp == RL * P:
        conj.append(P)
assert conj, "conjugator must exist (class number 1 of Q(sqrt5))"
P0 = conj[0]
assert P0 * Cmp * P0.inv() == RL
say(f"P5: memo-49 clock [[0,-1],[1,3]] IS GL(2,Z)-conjugate to RL: P = {tuple(P0)}, det P = {P0.det()};"
    f" ({len(conj)} conjugators with |entries|<=5). Same clock, different basis.")
# [CONTROL-]: same charpoly, genuinely non-conjugate pair -- instrument must return NONE
U1 = Matrix([[1, 1], [0, 1]]); U2 = Matrix([[1, 2], [0, 1]])
conj_ctrl = [1 for a, b, c, e in itertools.product(range(-5, 6), repeat=4)
             if abs(Matrix([[a, b], [c, e]]).det()) == 1
             and Matrix([[a, b], [c, e]]) * U1 == U2 * Matrix([[a, b], [c, e]])]
assert not conj_ctrl
say("P5 [CONTROL-]: same instrument on [[1,1],[0,1]] vs [[1,2],[0,1]] (same charpoly (x-1)^2,"
    " known non-conjugate in GL(2,Z)): 0 conjugators found -- the instrument can exclude.")

# ---------------------------------------------------------------- Part 4: depth-3 is a DEPTH not an ORDER; it becomes order 3 exactly at the ramified prime 3
N = Matrix([[0, 1, 0], [0, 0, 1], [0, 0, 0]]); J = eye(3) + N
assert N**3 == Matrix.zeros(3) and N**2 != Matrix.zeros(3)
# char 0: J^n = I + nN + C(n,2)N^2, entry (1,2) = n != 0 => infinite order
assert all((J**n) != eye(3) for n in range(1, 50))
Jn = J**7
assert Jn[0, 1] == 7 and Jn[0, 2] == 21
# mod 3: (I+N)^3 = I + 3N + 3N^2 + N^3 == I
J3 = (J**3).applyfunc(lambda x: x % 3)
assert J3 == eye(3)
assert (J**1).applyfunc(lambda x: x % 3) != eye(3) and (J**2).applyfunc(lambda x: x % 3) != eye(3)
say("P6: a nilpotency-3 unipotent (J = I+N, N^3=0) has INFINITE order in char 0 (J^n[0,1]=n)"
    " but order EXACTLY 3 mod 3. The meridian's 'order 3' is a DEPTH grading; it is a finite"
    " order-3 clock only at the ramified prime 3 -- the same 3 that makes the conductor 3*kappa.")

# ---------------------------------------------------------------- Part 5: the arrow reconciliation (B766 T7=T3 vs B1083)
phi = (1 + sqrt(5)) / 2
assert simplify((1 - phi) ** 2 - phi ** (-2)) == 0
say("P7: (1-phi)^2 = phi^(-2) exact -- gamma5 (the sqrt5 Galois branch) inverts the tick eigenvalue:"
    " B766's T7 'time direction' flip is a SPECTRAL RELABELING (which root is called forward).")
Minv = M.inv()
assert Minv == Matrix([[0, 1], [1, -1]]) and any(x < 0 for x in Minv)
say(f"P8: M^-1 = {tuple(Minv)} has a NEGATIVE entry -- the inverse tick is NOT realized by any"
    " positive substitution; no Galois action changes this (M^-1 is Galois-fixed, defined over Z).")

def sigma(w):  # a -> ab, b -> a
    return "".join("ab" if ch == "a" else "a" for ch in w)
imgs = set()
for n in range(1, 11):
    for bits in itertools.product("ab", repeat=n):
        imgs.add(sigma("".join(bits)))
assert "bb" not in imgs and not any(w.endswith("bb") or "bb" in w for w in imgs if len(w) <= 4 and "bb" in w)
assert not any("bb" == w for w in imgs)
assert "aaa" in imgs  # sigma(bbb) = aaa
hasbb = any("bb" in w for w in imgs)
say(f"P9: image of sigma over all words length<=10: 'bb' has NO preimage (any 'bb' substring: {hasbb});"
    " 'aaa' = sigma('bbb') HAS one. B1083's arrow (monoid non-surjectivity) re-verified.")

# ---------------------------------------------------------------- Part 6: B293 Goldman Casimir + the beat is anti-symplectic
x, y, z = symbols("x y z")
def pb(f, g):  # Goldman bracket on trace coordinates
    bxy = 2 * z - x * y; byz = 2 * x - y * z; bzx = 2 * y - x * z
    return expand(
        (diff(f, x) * diff(g, y) - diff(f, y) * diff(g, x)) * bxy
        + (diff(f, y) * diff(g, z) - diff(f, z) * diff(g, y)) * byz
        + (diff(f, z) * diff(g, x) - diff(f, x) * diff(g, z)) * bzx)
kappa = x**2 + y**2 + z**2 - x * y * z - 2
assert pb(kappa, x) == 0 and pb(kappa, y) == 0 and pb(kappa, z) == 0
ctrl = x**2 + y**2 + z**2
assert pb(ctrl, x) != 0
say("P10: {kappa, x}={kappa, y}={kappa, z}=0 exact (kappa = x^2+y^2+z^2-xyz-2 IS the Casimir,"
    " B293 recovered) [CONTROL+]; deliberately-wrong x^2+y^2+z^2 has {.,x} != 0 [CONTROL-].")

Beat = Matrix([[1, 0], [0, -1]])   # memo 31: beta(mu)=mu, beta(lambda)=lambda^-1 on H1(cusp)
Om = Matrix([[0, 1], [-1, 0]])     # <mu,lambda> = 1
assert Beat.T * Om * Beat == -Om and Beat.det() == -1 and Beat**2 == eye(2)
say("P11: the beat diag(1,-1) on H1(cusp) is ANTI-symplectic (B^T Om B = -Om, det -1, order 2)"
    " -- the SAME det=-1 Z/2 as the Breath tick M at the fiber face: one orientation-reversing"
    " bit at both peripheral faces; B293's conjugate pair (mu,lambda) is what it reverses.")

say("ALL ASSERTS GREEN")
