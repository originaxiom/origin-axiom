"""B1855 (P-737; data-free): the explore seat's settlement of the charge law, checked with main's own code (B1853's
functions, re-stated here): (1) its counterexamples for lcm(S) >= 12 -- the premise E = +-I mod every N in S exactly, and
the excess length (k = 20, 80 digits) below the single run lcm(S) + 1's; its S = {5} control above; (2) Lemma A,
excess = 2 log Q(E), Q = v^T E v / v^T v with v = (phi, 1) in GENESIS's letters, on 3000 R1 defects; (3) an independent brute force over
GAPPED defects (two or three non-golden runs at any positions up to 40, lengths 2..12 / 2..8) under the charge premise
at 5, by Lemma A: if the proof holds, nothing is below the run of 6. A corroboration, not the proof."""
import itertools, random
import mpmath as mp
mp.mp.dps = 80
def mul(A, B): return ((A[0][0]*B[0][0]+A[0][1]*B[1][0], A[0][0]*B[0][1]+A[0][1]*B[1][1]), (A[1][0]*B[0][0]+A[1][1]*B[1][0], A[1][0]*B[0][1]+A[1][1]*B[1][1]))
def inv(A): return ((A[1][1], -A[0][1]), (-A[1][0], A[0][0]))
def pw(A, n):
    X = ((1, 0), (0, 1))
    for _ in range(n): X = mul(X, A)
    return X
def mod(A, n): return tuple(tuple(x % n for x in r) for r in A)
L, R, I = ((1, 1), (0, 1)), ((1, 0), (1, 1)), ((1, 0), (0, 1)); LR = mul(L, R)
def D(runs):
    M = I
    for i, r in enumerate(runs): M = mul(M, pw(L if i % 2 == 0 else R, r))
    return M
def E(runs): return mul(D(runs), inv(D([1] * len(runs))))
def pmI(A, n): return mod(A, n) in (mod(I, n), mod(((-1, 0), (0, -1)), n))
def excess(runs, k=20):
    m = len(runs); X = R if m % 2 else I
    W = mul(mul(D(runs), X), pw(LR, k)); G = mul(mul(D([1] * m), X), pw(LR, k))
    t = lambda A: abs(mp.mpf(A[0][0] + A[1][1]))          # a geodesic's length uses |tr|
    return 2 * mp.acosh(t(W) / 2) - 2 * mp.acosh(t(G) / 2)
def lemmaA(Em):
    phi = mp.phi
    # with GENESIS's L, R the leading eigenvector of LR = [[2,1],[1,1]] is v = (phi, 1) (the web seat's modules take the
    # transposed letters, hence its v = (1, phi)); Q = v^T E v / v^T v
    return 2 * mp.log(abs(Em[0][0] * phi ** 2 + (Em[0][1] + Em[1][0]) * phi + Em[1][1]) / (1 + phi ** 2))
def placed(pairs):
    m = max(p for p, _ in pairs); runs = [1] * m
    for p, r in pairs: runs[p - 1] = r
    return runs
from math import lcm
out = []
cases = [((3, 4), [(1, 2), (2, 1), (3, 1), (4, 3), (5, 1), (6, 1), (7, 2)]),
         ((3, 5), [(1, 3), (6, 2), (11, 3)]),
         ((4, 5), [(1, 2), (17, 2), (64, 4), (69, 2)]),
         ((2, 3, 5), [(1, 5), (33, 2), (129, 2)]),
         ((3, 4, 5), [(1, 2), (17, 2), (19, 4), (129, 2)]),
         ((2, 3, 4, 5), [(1, 2), (17, 2), (19, 4), (129, 2)]),
         ((5,), [(1, 2), (21, 5)])]
for S, pairs in cases:
    runs = placed(pairs); Em = E(runs)
    prem = all(pmI(Em, n) for n in S)
    ex = excess(runs); exA = lemmaA(Em); single = excess([lcm(*S) + 1])
    verdict = ("COUNTEREXAMPLE" if prem and ex < single else "not below") if S != (5,) else ("the control: above, as the proof says" if ex > single else "BELOW: the proof fails")
    out.append("S = %-13s %-38s premise %s; excess %.4f (Lemma A %.4f) vs single run (%d) %.4f -> %s"
               % (S, pairs, prem, float(ex), float(exA), lcm(*S) + 1, float(single), verdict))
# Lemma A on a sample of R1
def R1():
    for m in range(1, 9):
        top = 6 if m <= 6 else 3
        for r in itertools.product(range(1, top + 1), repeat=m):
            if r[0] >= 2 and r[-1] >= 2: yield r
rng = random.Random(20261107); sample = rng.sample(list(R1()), 3000)
worst = max(abs(excess(r) - lemmaA(E(r))) for r in sample)
out.append("Lemma A on 3000 R1 defects (k = 20 excess against 2 log Q): max difference %.1e" % float(worst))
# the brute force over gapped defects under the charge premise at 5 (Lemma A, exact E)
best = (mp.inf, None); n2 = n3 = 0
single6 = excess([6])
for p2 in range(2, 41):
    for a, b in itertools.product(range(2, 13), repeat=2):
        runs = placed([(1, a), (p2, b)]); Em = E(runs)
        if pmI(Em, 5):
            n2 += 1; v = lemmaA(Em)
            if v < best[0]: best = (v, (a, p2, b))
for p2, p3 in itertools.combinations(range(2, 31), 2):
    for a, b, c in itertools.product(range(2, 9), repeat=3):
        runs = placed([(1, a), (p2, b), (p3, c)]); Em = E(runs)
        if pmI(Em, 5):
            n3 += 1; v = lemmaA(Em)
            if v < best[0]: best = (v, (a, p2, b, p3, c))
out.append("gapped defects under charge at 5: %d two-run and %d three-run premise-satisfying; least excess %.4f at %s against the run of 6's %.4f -> %s"
           % (n2, n3, float(best[0]), best[1], float(single6), "none below (corroborates the proof)" if best[0] > single6 else "BELOW: the proof fails"))
print("\n".join(out))
