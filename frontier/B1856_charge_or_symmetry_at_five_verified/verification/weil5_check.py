"""B1856 (P-738; data-free): the explore seat's level-5 Weil-representation test, re-derived with main's own code.
The Weil representation of SL(2, F5) on C^5 (B355's quantized cat map): rho(T) = diag e(3 x^2/5), rho(S) = the DFT
(sign chosen so that rho is projectively consistent -- both signs tried, the consistent one kept). B355's letters are
R = T, L = S T^-1 S^-1, i.e. GENESIS's R and L swapped (its LR is GENESIS's RL, conjugate to LR). Checks:
HQ0 projective closure on all 120 elements (no clash: two words for one element give proportional matrices);
HQ1 the elements acting as a scalar on each parity sector (even dim 3, odd dim 2) are exactly +-I;
HQ2 the projective commutant of rho(LR) is +-<LR> (order 10);
HQ3 rho(LR)'s eigenvalue ratios within each sector are primitive 5th roots; with the even sector normalised to contain
    eigenvalue 1, its trace is 1 - phi and the odd sector's 2 cos 36 = phi;
HQ4 the line-invisible departure (2,1,1,1,2) has E = +-(LR)^a mod 5 with a != 0 (GENESIS letters; its image under the
    swap is the seat's), non-scalar on both sectors; the run of 6 has E = I mod 5."""
import itertools, cmath, math
import numpy as np
P = 5; w = lambda x: cmath.exp(2j * math.pi * x / P)
def mmod(A): return tuple(tuple(int(x) % P for x in r) for r in A)
def mmul(A, B): return mmod(((A[0][0]*B[0][0]+A[0][1]*B[1][0], A[0][0]*B[0][1]+A[0][1]*B[1][1]), (A[1][0]*B[0][0]+A[1][1]*B[1][0], A[1][0]*B[0][1]+A[1][1]*B[1][1])))
T = ((1, 1), (0, 1)); S = ((0, -1 % P), (1, 0)); I = ((1, 0), (0, 1))
RT = np.diag([w(3 * x * x) for x in range(P)])
def build(sign):
    RS = np.array([[w(sign * x * y) for y in range(P)] for x in range(P)]) / math.sqrt(P)
    rep = {mmod(I): np.eye(P, dtype=complex)}; frontier = [mmod(I)]; clashes = 0; repeats = 0
    gens = [(mmod(T), RT), (mmod(S), RS)]
    while frontier:
        nxt = []
        for g in frontier:
            for h, Rh in gens:
                k = mmul(g, h); M = rep[g] @ Rh
                if k in rep:
                    repeats += 1
                    A = rep[k]; c = np.vdot(A.ravel(), M.ravel()) / np.vdot(A.ravel(), A.ravel())
                    if np.abs(M - c * A).max() > 1e-9: clashes += 1
                else:
                    rep[k] = M; nxt.append(k)
        frontier = nxt
    return rep, clashes, repeats
for sign in (-1, 1):
    rep, clashes, repeats = build(sign)
    if clashes == 0: break
out = ["HQ0: rho projective on %d of 120 elements (%d repeated arrivals, %d clashes; DFT sign %+d)" % (len(rep), repeats, clashes, sign)]
assert len(rep) == 120 and clashes == 0
par = np.zeros((P, P)); 
for x in range(P): par[(-x) % P, x] = 1
ev = np.array([[1, 0, 0, 0, 0], [0, 1, 0, 0, 1], [0, 0, 1, 1, 0]], dtype=float); ev[1:] /= math.sqrt(2)
od = np.array([[0, 1, 0, 0, -1], [0, 0, 1, -1, 0]], dtype=float) / math.sqrt(2)
def block(M, B): return B @ M @ B.T
def scalar(M): c = np.trace(M) / M.shape[0]; return np.abs(M - c * np.eye(M.shape[0])).max() < 1e-9
inv_sectors = [g for g, M in rep.items() if scalar(block(M, ev)) and scalar(block(M, od))]
whole = [g for g, M in rep.items() if scalar(M)]
out.append("HQ1: scalar on C^5: %s; scalar on each sector: %s" % (whole, sorted(inv_sectors)))
assert set(inv_sectors) == {mmod(I), mmod(((-1, 0), (0, -1)))} and whole == [mmod(I)]
# B355's letters: R = T, L = S T^-1 S^-1
Tinv = ((1, -1 % P), (0, 1)); Sinv = ((0, 1), (-1 % P, 0))
Lb = mmul(mmul(S, Tinv), Sinv); Rb = mmod(T); LRb = mmul(Lb, Rb)
M = rep[LRb]
comm = [g for g, A in rep.items() if (lambda X: (lambda c: np.abs(X - c * M).max() < 1e-9)(np.vdot(M.ravel(), X.ravel()) / np.vdot(M.ravel(), M.ravel())))(A @ M @ np.linalg.inv(A))]
gen = set(); X = mmod(I)
for _ in range(10): gen.add(X); X = mmul(X, LRb)
out.append("HQ2: projective commutant of rho(LR): %d elements, = +-<LR>: %s" % (len(comm), set(comm) == gen | {mmul(g, ((P - 1, 0), (0, P - 1))) for g in gen}))
assert set(comm) == gen and len(comm) == 10
e_ev = np.linalg.eigvals(block(M, ev)); e_od = np.linalg.eigvals(block(M, od))
ref = e_ev[np.argmin([abs(cmath.phase(z / e_ev[0])) for z in e_ev])]
# normalise so that the even sector contains eigenvalue 1 at the angle-0 member of {0, .4, .6}
cands = []
for z0 in e_ev:
    a_ev = sorted(round((cmath.phase(z / z0) / (2 * math.pi)) % 1, 6) for z in e_ev)
    a_od = sorted(round(((cmath.phase(z / z0) / (2 * math.pi)) + 0.5) % 1 - 0.5, 6) for z in e_od)
    cands.append((a_ev, a_od, z0))
pick = [c for c in cands if c[0] == [0.0, 0.4, 0.6]]
assert pick, cands
a_ev, a_od, z0 = pick[0]
phi = (1 + math.sqrt(5)) / 2
tr_ev = sum(cmath.exp(2j * math.pi * a) for a in a_ev); tr_od = sum(cmath.exp(2j * math.pi * a) for a in a_od)
out.append("HQ3: rho(LR) eigenvalue angles, even sector %s, odd sector %s (turns); traces %.12f%+.1ei and %.12f%+.1ei; 1 - phi = %.12f, phi = %.12f"
           % (a_ev, a_od, tr_ev.real, tr_ev.imag, tr_od.real, tr_od.imag, 1 - phi, phi))
assert abs(tr_ev - (1 - phi)) < 1e-9 and abs(tr_od - phi) < 1e-9
# HQ4 in GENESIS letters
L, R = ((1, 1), (0, 1)), ((1, 0), (1, 1))
def zmul(A, B): return ((A[0][0]*B[0][0]+A[0][1]*B[1][0], A[0][0]*B[0][1]+A[0][1]*B[1][1]), (A[1][0]*B[0][0]+A[1][1]*B[1][0], A[1][0]*B[0][1]+A[1][1]*B[1][1]))
def zpow(A, n):
    X = ((1, 0), (0, 1))
    for _ in range(n): X = zmul(X, A)
    return X
def Dm(runs):
    X = ((1, 0), (0, 1))
    for i, r in enumerate(runs): X = zmul(X, zpow(L if i % 2 == 0 else R, r))
    return X
def zinv(A): return ((A[1][1], -A[0][1]), (-A[1][0], A[0][0]))
def Em(runs): return mmod(zmul(Dm(runs), zinv(Dm([1] * len(runs)))))
LRg = mmod(zmul(L, R)); pw = {}; X = mmod(I)
for a in range(10): pw[X] = a; X = mmul(X, LRg)
E6 = Em((6,)); E2 = Em((2, 1, 1, 1, 2))
a2 = pw.get(E2)
# map GENESIS letters to B355's (swap L <-> R): conjugation by the matrix J = [[0,1],[1,0]] composed with transpose -- here
# test non-scalarity directly on rho of the element itself and of its swap image
swap = lambda A: ((A[1][1], A[1][0]), (A[0][1], A[0][0]))
E2b = mmod(swap(E2))
ns = lambda g: not scalar(block(rep[g], ev)) and not scalar(block(rep[g], od))
out.append("HQ4: E(6) = %s (= I: %s); E(2,1,1,1,2) = %s = (LR)^%s in GENESIS letters; its swap image %s non-scalar on both sectors: %s"
           % (E6, E6 == mmod(I), E2, a2, E2b, ns(E2b)))
assert E6 == mmod(I) and a2 not in (None, 0, 5) and ns(E2b)
print("\n".join(out))
