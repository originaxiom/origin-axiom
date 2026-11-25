"""B1980 part A (main, 2026-11-25; exact; data-free): the act M = [[2,1],[1,1]] on the level-30 curve X(30): its order mod 30,
the powers with a fixed point off the cusps, the cusps, and the act's orbits and fixed cusps.
    python3 -B act_level30.py > act_level30_run.txt"""
from math import gcd
N = 30
def mul(A, B): return ((A[0] * B[0] + A[1] * B[2]) % N, (A[0] * B[1] + A[1] * B[3]) % N, (A[2] * B[0] + A[3] * B[2]) % N, (A[2] * B[1] + A[3] * B[3]) % N)
I = (1, 0, 0, 1); mI = (N - 1, 0, 0, N - 1); M = (2, 1, 1, 1)
P, pw = I, {}
for k in range(1, 121):
    P = mul(P, M); pw[k] = P
first_pm = min(k for k in pw if pw[k] in (I, mI)); first_id = min(k for k in pw if pw[k] == I)
print("A0: M^k = +-I (mod 30) first at k = %d; M^k = I first at k = %d" % (first_pm, first_id))
ell = [k for k in range(1, first_pm) if (pw[k][0] + pw[k][3]) % N in (0, 1, N - 1)]
par = [k for k in range(1, first_pm) if (pw[k][0] + pw[k][3]) % N in (2, N - 2)]
print("A1: powers 1 <= k < %d with an elliptic element in M^k Gamma(30) (trace 0, +-1 mod 30): %s" % (first_pm, ell))
print("    traces of M^k mod 30, k = 1..%d: %s" % (first_pm, [(pw[k][0] + pw[k][3]) % N for k in range(1, first_pm + 1)]))
print("    powers whose trace is +-2 mod 30 (a parabolic element possible): %s" % par)
def order(v): return N // gcd(gcd(v[0], v[1]), N)
cusps = set()
for a in range(N):
    for c in range(N):
        if order((a, c)) == N: cusps.add(min((a, c), ((-a) % N, (-c) % N)))
print("A2: cusps of X(30) (vectors of order 30 up to sign): %d" % len(cusps))
def act(Mk, v):
    w = ((Mk[0] * v[0] + Mk[1] * v[1]) % N, (Mk[2] * v[0] + Mk[3] * v[1]) % N); return min(w, ((-w[0]) % N, (-w[1]) % N))
seen, sizes = set(), []
for v in sorted(cusps):
    if v in seen: continue
    o = [v]; w = act(M, v)
    while w != v: o.append(w); w = act(M, w)
    seen |= set(o); sizes.append(len(o))
print("    the act's orbits on the cusps: %d orbits, sizes %s" % (len(sizes), sorted(set(sizes))))
fixed = {k: [v for v in sorted(cusps) if act(pw[k], v) == v] for k in range(1, first_pm)}
print("    cusps fixed by M: %d; powers k < %d fixing some cusp: %s" % (len(fixed[1]), first_pm, [(k, len(fixed[k])) for k in range(1, first_pm) if fixed[k]]))
k0 = min([k for k in fixed if fixed[k]], default=None)
if k0: print("    the cusps fixed by M^%d: %s" % (k0, fixed[k0]))
print("SUMMARY A: no interior fixed point for k < %d: %s; M fixes no cusp: %s" % (first_pm, not ell, not fixed[1]))
