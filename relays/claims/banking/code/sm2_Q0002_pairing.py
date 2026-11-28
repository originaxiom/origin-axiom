#!/usr/bin/env python3
"""sm2 (fam1-v1-unset-05): an independent recomputation for card Q0002 (the four-move sum's pairing law). python-flint and
the standard library. Written from the card's definitions only.

    python3 relays/claims/banking/code/sm2_Q0002_pairing.py                  # the law on every orbit tested
    python3 relays/claims/banking/code/sm2_Q0002_pairing.py --wrong-pairing  # my control: R(x+4) R(x+1) must fail

Orbits: every orbit, under L, R and their inverses, of every leaf mod 7, 11 and 13 (all k, the zero reading left out), and
the orbit of (3,3,3) mod 27, 81 and 135. On each: C and sigma preserve it; T4 = 3(SP + PS) - 2S as matrices (checked as
T4 = S(C + C^2) + (C + C^2)S, the multiset of images at every reading); A = 3P(1 + S)P on the basis of C-orbit sums, its
characteristic polynomial exactly; d1, d2, R, f_S, d3, d4; T4's characteristic polynomial against the predicted
R(x+4) R(x+2) (x-4)^d1 (x+4)^d2 (x+2)^d3 (x-2)^d4: exactly over Z up to 700 readings, and modulo five 62-bit primes above.
"""
import sys
from collections import Counter
import flint

WRONG = "--wrong-pairing" in sys.argv

def maps(N):
    L = lambda v: (v[0], v[2], (v[0] * v[2] - v[1]) % N)
    R = lambda v: (v[2], v[1], (v[1] * v[2] - v[0]) % N)
    Li = lambda v: (v[0], (v[0] * v[1] - v[2]) % N, v[1])
    Ri = lambda v: ((v[0] * v[1] - v[2]) % N, v[1], v[0])
    C = lambda v: (v[1], v[2], v[0])
    sg = lambda v: (v[1], v[0], (v[0] * v[1] - v[2]) % N)
    return L, R, Li, Ri, C, sg

def orbit(N, s):
    L, R, Li, Ri, C, sg = maps(N)
    O = {s}; st = [s]
    while st:
        v = st.pop()
        for m in (L, R, Li, Ri):
            u = m(v)
            if u not in O: O.add(u); st.append(u)
    return sorted(O)

def orbits_of_leaves(N):
    seen, out = set(), []
    for x in range(N):
        for y in range(N):
            for z in range(N):
                v = (x, y, z)
                if v == (0, 0, 0) or v in seen: continue
                O = orbit(N, v); seen |= set(O); out.append((N, (x * x + y * y + z * z - x * y * z) % N, O))
    return out

PRIMES = []
p = (1 << 62) - 1
def isprime(m):
    if m % 2 == 0: return False
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
while len(PRIMES) < 5:
    p -= 2 if p % 2 else 1
    if isprime(p): PRIMES.append(p)

def check(N, k, O):
    L, R, Li, Ri, C, sg = maps(N)
    idx = {v: i for i, v in enumerate(O)}
    n = len(O)
    assert all(sg(sg(v)) == v for v in O)
    if not all(C(v) in idx and sg(v) in idx for v in O):
        return "C or sigma leaves the orbit"
    # T4 = S C^2 + S C + C S + C^2 S, pointwise as multisets of images
    for v in O:
        lhs = Counter([L(v), R(v), Li(v), Ri(v)])
        rhs = Counter([sg(C(C(v))), sg(C(v)), C(sg(v)), C(C(sg(v)))])
        if lhs != rhs: return "T4 is not 3(SP + PS) - 2S"
    # A = 3 P (1 + S) P on C-orbit sums u_o: (1 + S) u_o = u_o + sum of e_sigma(v); 3P e_w = (3/|o(w)|) u_o(w)
    reps, orb_of = [], {}
    for v in O:
        if v in orb_of: continue
        o = sorted({v, C(v), C(C(v))}); r = len(reps); reps.append(o)
        for u in o: orb_of[u] = r
    m = len(reps)
    # P(1 + S) u_o on the u's: P u_o = u_o, and P e_w = u_o(w) / |o(w)|; then times 3, exactly over Q
    Aq = [[flint.fmpq(0)] * m for _ in range(m)]
    for a, o in enumerate(reps):
        Aq[a][a] += 3
        for v in o:
            b = orb_of[sg(v)]
            Aq[b][a] += flint.fmpq(3, len(reps[b]))
    for row in Aq:
        for c in row: assert c.q == 1, "A is not an integer matrix"
    Ai = flint.fmpz_mat([[int(c.p) for c in row] for row in Aq])
    pa = Ai.charpoly()
    x = flint.fmpz_poly([0, 1])
    d1 = d2 = 0; Rp = pa
    while Rp(6) == 0: Rp = Rp // (x - 6); d1 += 1     # the multiplicity of 6
    while Rp(0) == 0: Rp = Rp // x; d2 += 1           # the multiplicity of 0
    fS = sum(1 for v in O if sg(v) == v)
    assert (n + fS) % 2 == 0
    d3 = (n + fS) // 2 - d1 - Rp.degree(); d4 = (n - fS) // 2 - d2 - Rp.degree()
    if d3 < 0 or d4 < 0: return "negative d3 or d4"
    shift = 1 if WRONG else 2
    pred = Rp(x + 4) * Rp(x + shift) * (x - 4) ** d1 * (x + 4) ** d2 * (x + 2) ** d3 * (x - 2) ** d4
    assert pred.degree() == n
    rows = [[0] * n for _ in range(n)]
    for v in O:
        for g in (L, R, Li, Ri):
            rows[idx[g(v)]][idx[v]] += 1
    if n <= 700:
        how = "exact"
        same = flint.fmpz_mat(rows).charpoly() == pred
    else:
        how = "mod %d primes" % len(PRIMES)
        same = all(flint.nmod_mat(rows, q).charpoly() == flint.nmod_poly([int(c) % q for c in pred.coeffs()], q)
                   for q in PRIMES)
    return (same, how, n, d1, d2, Rp.degree(), d3, d4, fS)

cases = []
for N in (7, 11, 13):
    cases += orbits_of_leaves(N)
for N in (27, 81, 135):
    cases.append((N, (27 - 27) % N, orbit(N, (3 % N, 3 % N, 3 % N))))
bad, done, sizes, card_six = [], 0, Counter(), []
for N, k, O in cases:
    r = check(N, k, O)
    if isinstance(r, str) or not r[0]:
        bad.append((N, k, len(O), r if isinstance(r, str) else "the characteristic polynomial differs"))
    done += 1; sizes[N] += 1
    if N >= 27:
        print("level %d, orbit of (3,3,3): n = %d, d1 = %d, d2 = %d, deg R = %d, d3 = %d, d4 = %d, f_S = %d, %s: %s"
              % (N, r[2], r[3], r[4], r[5], r[6], r[7], r[8], r[1], r[0]))
print("orbits tested: %d (by level: %s)" % (done, dict(sizes)))
print("DECISIVE: T4 = 3(SP + PS) - 2S and the characteristic polynomial R(x+4) R(x+%d) (x-4)^d1 (x+4)^d2 (x+2)^d3 "
      "(x-2)^d4 on every orbit tested: %s" % (1 if WRONG else 2, not bad))
print("DECISIVE: orbits where it fails: %d %s" % (len(bad), bad[:5]))
print("RESULT: the card's law %s" % ("holds" if not bad else "does not come out"))
sys.exit(0 if not bad else 1)
