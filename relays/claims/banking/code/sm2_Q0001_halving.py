#!/usr/bin/env python3
"""sm2 (fam1-v1-unset-05): an independent recomputation for card Q0001 (the halving at mod 135 on the orbit of (3,3,3)).
python-flint, sympy (permutation groups) and the standard library. Written from the card's definitions only.

    python3 relays/claims/banking/code/sm2_Q0001_halving.py            # N = 135, the card's level
    python3 relays/claims/banking/code/sm2_Q0001_halving.py --level 27 # my control: the halving holds there, so the
                                                                       # card's claim cannot come out (exit 1)

For level N: the orbit O of (3,3,3) under L, R and their inverses; that C and X preserve O; C's fixed points; the six-move
sum W (L, R, X and their inverses; W symmetric, commuting with C). The neutral sector: W on the C-invariant functions,
basis the indicator of each C-orbit, an integer matrix, its characteristic polynomial computed exactly over Z by flint.
The charged sector q = 1: W on b_o = sum_j w^-j e_(C^j v), with coefficients in Z[w]; its characteristic polynomial S is
computed modulo primes p = 1 mod 3 (w a cube root of 1 mod p) and lifted by the CRT, symmetric residues, with the product
of the primes above 2 * 7^n (every eigenvalue has |lambda| <= 6, so |coefficient k| <= C(n,k) 6^k <= 7^n); S is checked
to be real by lifting the q = 2 sector the same way and finding the same polynomial. Then: deg gcd(p(2x)/2^d, S), the
unpaired part S / gcd and its factors over Q, and whether p(2x)/2^d = (x - 3)(x + 3) x S(x).
At N = 135 it also checks that reduction mod 27 maps O onto the mod-27 orbit (so G_135 maps onto G_27), and at 27 that
rho (L -> -w^2, R -> -w) is well defined on G_27: |<L, R>| on the orbit equals |<L, R>| on the orbit times Z/6.
"""
import sys, time
import flint
from sympy.combinatorics import Permutation, PermutationGroup

N = int(sys.argv[sys.argv.index("--level") + 1]) if "--level" in sys.argv else 135

def moves(N):
    L = lambda v: (v[0], v[2], (v[0] * v[2] - v[1]) % N)
    R = lambda v: (v[2], v[1], (v[1] * v[2] - v[0]) % N)
    X = lambda v: (v[1], (v[1] * v[2] - v[0]) % N, v[2])
    Li = lambda v: (v[0], (v[0] * v[1] - v[2]) % N, v[1])
    Ri = lambda v: ((v[0] * v[1] - v[2]) % N, v[1], v[0])
    Xi = lambda v: ((v[0] * v[2] - v[1]) % N, v[0], v[2])
    return L, R, X, Li, Ri, Xi
C = lambda v: (v[1], v[2], v[0])

def orbit(N):
    L, R, X, Li, Ri, Xi = moves(N)
    s = (3 % N, 3 % N, 3 % N); O = {s}; st = [s]
    while st:
        v = st.pop()
        for m in (L, R, Li, Ri):
            u = m(v)
            if u not in O: O.add(u); st.append(u)
    return sorted(O)

O = orbit(N)
L, R, X, Li, Ri, Xi = moves(N)
SIX = (L, R, X, Li, Ri, Xi)
idx = {v: i for i, v in enumerate(O)}
assert all(Li(L(v)) == v and Ri(R(v)) == v and Xi(X(v)) == v for v in O)          # the inverses are inverses
assert all(C(v) in idx and X(v) in idx for v in O)                                  # C and X preserve the orbit
# the six moves are closed under conjugation by C, so W commutes with C
Ci = lambda v: (v[2], v[0], v[1])
for m in SIX:
    cm = lambda v, m=m: C(m(Ci(v)))
    assert any(all(cm(v) == m2(v) for v in O) for m2 in SIX)
fixed = [v for v in O if C(v) == v]
reps, seen = [], set()
for v in O:
    if v in seen or C(v) == v: continue
    reps.append(v); seen |= {v, C(v), C(C(v))}
n = len(reps); d = n + len(fixed)
print("level %d: orbit %d readings, C's fixed points %s, size-3 C-orbits %d" % (N, len(O), fixed, n))

# ---- neutral sector, exactly over Z
corb = {}
for k, v in enumerate(fixed): corb[v] = k
for k, v in enumerate(reps):
    for u in (v, C(v), C(C(v))): corb[u] = len(fixed) + k
base = fixed + reps
Mn = [[0] * d for _ in range(d)]
for a, b0 in enumerate(base):
    members = [b0] if C(b0) == b0 else [b0, C(b0), C(C(b0))]
    col = {}
    for u in members:
        for m in SIX:
            col[m(u)] = col.get(m(u), 0) + 1
    for b, u in enumerate(base):                       # W u_a is C-invariant: read it at each orbit's base point
        Mn[b][a] = col.get(u, 0)
t0 = time.time()
pn = flint.fmpz_mat(Mn).charpoly()
print("neutral sector: degree %d, characteristic polynomial in %.1f s" % (pn.degree(), time.time() - t0))

# ---- charged sectors q = 1, 2, modulo primes p = 1 mod 3, lifted by the CRT
def charged_entries():
    """for each size-3 orbit a, W b_a's coefficient on b_b as (e0, e1, e2): sum of e_j w^(-j)... read at base points"""
    ent = []
    for a, v in enumerate(reps):
        col = {}
        for j, u in enumerate((v, C(v), C(C(v)))):
            for m in SIX:
                t = m(u); col.setdefault(t, [0, 0, 0])[j] += 1      # e_t gets w^-j from e_(C^j v)
        ent.append(col)
    return ent
ent = charged_entries()
# W b_a has the q-th character, so its coefficient on b_b is its coefficient at e_(base b); on fixed points it vanishes
for a, col in enumerate(ent):
    for f in fixed:
        if f in col:
            e = col[f]; assert e[0] == e[1] == e[2], "W b_a is not in the charged sector"
def is_prime(m):
    if m < 2: return False
    for p in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        if m % p == 0: return m == p
    dd, s = m - 1, 0
    while dd % 2 == 0: dd //= 2; s += 1
    for a in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        x = pow(a, dd, m)
        if x in (1, m - 1): continue
        for _ in range(s - 1):
            x = x * x % m
            if x == m - 1: break
        else: return False
    return True
bound = 2 * 7 ** n
primes, M, p = [], 1, (1 << 62) - 1
while M <= bound:
    p -= 1
    if p % 3 == 1 and is_prime(p):
        primes.append(p); M *= p
def cube_root(p):
    g = 2
    while True:
        w = pow(g, (p - 1) // 3, p)
        if w != 1: return w
        g += 1
def sector(q):
    res = []
    for p in primes:
        w = cube_root(p)
        if q == 2: w = w * w % p
        wi = [1, pow(w, p - 2, p), pow(w, 2 * (p - 2), p)]           # w^0, w^-1, w^-2
        A = [[0] * n for _ in range(n)]
        for a, col in enumerate(ent):
            for b, v in enumerate(reps):
                e = col.get(v)
                if e: A[b][a] = (e[0] * wi[0] + e[1] * wi[1] + e[2] * wi[2]) % p
        res.append(flint.nmod_mat(A, p).charpoly())
    coeffs = []
    for k in range(n + 1):
        x, Mk = 0, 1
        for p, c in zip(primes, res):                                 # CRT, incremental
            ck = int(c[k]); t = ((ck - x) * pow(Mk, -1, p)) % p
            x += Mk * t; Mk *= p
        if x > Mk // 2: x -= Mk
        coeffs.append(x)
    return flint.fmpz_poly(coeffs)
t0 = time.time()
S = sector(1)
S2 = sector(2)
print("charged sector: degree %d, %d primes of 62 bits, both sectors in %.1f s; q = 1 and q = 2 the same (S real): %s"
      % (S.degree(), len(primes), time.time() - t0, S == S2))

# ---- the comparison over Q
X1 = flint.fmpq_poly([0, 1])
pq = flint.fmpq_poly([int(c) for c in pn.coeffs()])
p2 = pq(2 * X1) / flint.fmpq(2) ** d                                  # p_neutral(2x) / 2^d, monic
Sq = flint.fmpq_poly([int(c) for c in S.coeffs()])
g = p2.gcd(Sq)
un = Sq / g if g.degree() > 0 else Sq
form = p2 == flint.fmpq_poly([0, -9, 0, 1]) * Sq                       # (x - 3)(x + 3) x S(x)
fac = flint.fmpz_poly([int(c * un.denom()) for c in un.coeffs()]).factor() if un.degree() > 0 else (1, [])
print("unpaired part: degree %d, factors over Q (degree, multiplicity): %s"
      % (un.degree(), [(f.degree(), e) for f, e in fac[1]]))
for f, e in fac[1]:
    print("   %s   (multiplicity %d)" % (f, e))
print("DECISIVE: level %d: charged roots %d, paired %d, unpaired %d" % (N, S.degree(), g.degree(), un.degree()))
print("DECISIVE: level %d: p_neutral(2x)/2^d = (x - 3)(x + 3) x S(x): %s" % (N, form))
ok = True
if N == 135:
    O27 = set(orbit(27))
    red = {(a % 27, b % 27, c % 27) for a, b, c in O}
    onto = red == O27
    print("DECISIVE: level 135 reduces onto the level-27 orbit: %s; C's fixed points at 135: %d" % (onto, len(fixed)))
    ok = onto and len(fixed) == 3 and S.degree() == 959 and un.degree() == 10 and not form
if N in (27, 135):
    O27 = orbit(27); i27 = {v: i for i, v in enumerate(O27)}
    L27, R27 = moves(27)[0], moves(27)[1]
    pL = [i27[L27(v)] for v in O27]; pR = [i27[R27(v)] for v in O27]
    G = PermutationGroup([Permutation(pL), Permutation(pR)])
    k = len(O27)
    eL = pL + [k + (j + 1) % 6 for j in range(6)]                     # rho(L) = -w^2 = zeta_6
    eR = pR + [k + (j + 5) % 6 for j in range(6)]                     # rho(R) = -w = zeta_6^5
    H = PermutationGroup([Permutation(eL), Permutation(eR)])
    print("DECISIVE: rho well defined on G_27: |G_27| = %d, with Z/6 attached %d: %s" % (G.order(), H.order(),
                                                                                         G.order() == H.order()))
    fL = pL + [k + (j + 1) % 6 for j in range(6)]                     # a wrong character, L -> zeta_6, R -> zeta_6
    fR = pR + [k + (j + 1) % 6 for j in range(6)]
    F2 = PermutationGroup([Permutation(fL), Permutation(fR)])
    print("rho's check can fail: with the wrong character L, R -> zeta_6 the order is %d (%s)"
          % (F2.order(), "larger" if F2.order() > G.order() else "the same"))
    if N == 27:
        ok = False                                                    # the card's claim is about 135
        print("CONTROL: at 27 the halving holds (unpaired %d, form %s), so the card's claim at 135 is not shown here"
              % (un.degree(), form))
print("RESULT: %s" % ("the card's claim holds" if ok else "the card's claim does not come out"))
sys.exit(0 if ok else 1)
