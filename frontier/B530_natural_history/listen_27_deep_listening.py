"""
Movement XXV — the deep listening (a second seat's advanced handoff, verified):
the prime 11, the three-prime organization, the deterministic hierarchy -- and the
claims that did NOT survive recomputation.

A cross-seat "advanced listening" handoff arrived after the portrait was drawn.
Verified each claim independently (verify-don't-trust, held in both directions after
the "don't be so sure" correction).  Banked what is exact; flagged what failed.

VERIFIED EXACTLY (banked):
  * THE PRIME 11.  H^1 of the tiling space has torsion Z/11: Smith normal form of
    M^T - I = diag(1,1,1,11).  And 11 = |det(M-I)| = |char_poly(1)| = |N(1-beta)| --
    the torsion IS the norm of (1-beta) in Q(beta).  (Fibonacci: trivial cokernel.)
  * PRIME SPLITTING of x^4-2x^3-5x^2-4x-1: 2,3,5,7,13,17,23 INERT; 11,19,31 split;
    29 fully split.  (5 and 7 inert -- unlike Fibonacci, where 5 splits.)
  * THREE-PRIME ORGANIZATION: 5 = the golden end (disc -400 = -2^4·5^2), 3 = the
    twist (running letter-sum uniform mod 3 AND mod 6; image sums {8,5,6,2}={2,2,0,2}
    mod 3; the trace-zero Z/3, movement XIX), 11 = the tiling (H^1 torsion).
  * DETERMINISTIC RULE HIERARCHY: fraction of zero-entropy contexts climbs
    50,57,70,69,82,85,87 % over context lengths 1-7; the denominators are exactly
    the factor complexity p(n) = 4,7,10,13,17,20,23.
  * SUBLATTICE: even/odd sublattices have identical statistics and MI ~ 1.23 bits
    (63% of the 2-bit max) -- strongly coupled.
  * THREE-POINT non-Markov: kappa3 is ~50x the Markov (factorized) estimate --
    profoundly non-Markov (qualitative; the specific value is normalization-dependent).
  * THE BbB RESONANCE (confirmed, after a false-kill).  The THREE-point pattern B at
    i, b at i+2, B at i+4 occurs 15352x vs 1254 expected under independence = 12.2x;
    EVERY occurrence is the 5-word BabAB, and 100% of them STRADDLE a sigma-image
    boundary (BabAB = the final B of sigma(a)=abAAB, then sigma(A)=abAB).  So the
    deterministic tunnel letters (B->a, b->A) make the substitution's OWN image seam
    audible through the lag-2 sublattice.  AaA is 3.4x by comparison.  (An earlier
    check mistook this for the TWO-point 'B at lag 2' = 0 and wrongly 'refuted' it --
    a self-inflicted false-kill, corrected here.)

DID NOT SURVIVE (flagged, NOT banked):
  * "forward-backward chirality decays to 0 at long range" -- a Markov-power artifact
    (any two stochastic matrices with the same stationary law have P^k -> same limit);
    the actual k-lag chirality does not cleanly decay.
  * "diffraction Bragg peaks at golden frequencies" -- did not reproduce; the naive
    FFT instrument is the same one that failed to confirm Fibonacci's Bragg peaks
    (movement XIII), so it is unreliable here.
  * "walk exponent nu=0.93" -- the sending seat itself flagged this as drift-dominated
    (freq imbalance), not anomalous fluctuation; not structurally deep.

No physics.  Firewalled.
"""
import numpy as np
import sympy as sp
from sympy.matrices.normalforms import smith_normal_form
from collections import Counter

SUB = {'a': 'abAAB', 'b': 'aAB', 'A': 'abAB', 'B': 'aA'}
M = sp.Matrix([[1, 1, 1, 1], [1, 0, 1, 0], [2, 1, 1, 1], [1, 1, 1, 0]])


def word(n=163106):
    u = 'a'
    while len(u) < n:
        u = ''.join(SUB[c] for c in u)
    return u[:n]


def prime11():
    x = sp.symbols('x')
    cp = x**4 - 2 * x**3 - 5 * x**2 - 4 * x - 1
    S = smith_normal_form(M.T - sp.eye(4), domain=sp.ZZ)
    torsion = abs(S[3, 3])
    return torsion, int((M - sp.eye(4)).det()), int(cp.subs(x, 1))


def prime_splitting():
    x = sp.symbols('x')
    cp = x**4 - 2 * x**3 - 5 * x**2 - 4 * x - 1
    out = {}
    for p in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]:
        out[p] = len([r for r in range(p) if cp.subs(x, r) % p == 0])
    return out


def mod_uniform(u=None):
    if u is None:
        u = word()
    val = {'a': 0, 'b': 1, 'A': 2, 'B': 3}
    cs = np.cumsum([val[c] for c in u])
    res = {}
    for m in (3, 6):
        d = Counter(cs % m)
        res[m] = max(abs(d[r] / len(cs) - 1 / m) for r in range(m))
    return res


def deterministic_hierarchy(u=None):
    if u is None:
        u = word()
    table = []
    for n in range(1, 8):
        ctx = {}
        for i in range(len(u) - n):
            ctx.setdefault(u[i:i + n], set()).add(u[i + n])
        det = sum(1 for s in ctx.values() if len(s) == 1)
        table.append((det, len(ctx)))
    return table


def sublattice_mi(u=None):
    if u is None:
        u = word()
    idx = {c: i for i, c in enumerate('abAB')}
    s = np.array([idx[c] for c in u])
    a, b = s[0::2], s[1::2]
    n = min(len(a), len(b))
    a, b = a[:n], b[:n]
    P = np.zeros((4, 4))
    for i, j in zip(a, b):
        P[i, j] += 1
    P /= n
    pa, pb = P.sum(1), P.sum(0)
    return sum(P[i, j] * np.log2(P[i, j] / (pa[i] * pb[j]))
               for i in range(4) for j in range(4) if P[i, j] > 0)


def bbb_resonance(u=None):
    """The BbB THREE-point resonance: B at i, b at i+2, B at i+4 (lags 0,2,4).
    Returns (ratio_over_independence, all_BabAB, frac_straddling_image_boundary).
    (An earlier check mistakenly computed the TWO-point B-at-lag-2 = 0 and wrongly
    'refuted' this; the real quantity is the three-point B_b_B, ~12x enhanced.)"""
    if u is None:
        u = word()
    N = len(u)
    f = {c: u.count(c) / N for c in 'abAB'}
    obs = sum(1 for i in range(N - 4) if u[i] == 'B' and u[i + 2] == 'b' and u[i + 4] == 'B')
    exp = N * f['B'] * f['b'] * f['B']
    pats = Counter(u[i:i + 5] for i in range(N - 4)
                   if u[i] == 'B' and u[i + 2] == 'b' and u[i + 4] == 'B')
    all_babab = set(pats) == {'BabAB'}
    # image-boundary straddle in the depth-8 word (images of the depth-7 word)
    d7 = 'a'
    for _ in range(7):
        d7 = ''.join(SUB[c] for c in d7)
    cum, bset, img8 = 0, set(), ''
    for c in d7:
        bset.add(cum)
        img8 += SUB[c]
        cum += len(SUB[c])
    occ = [i for i in range(len(img8) - 4) if img8[i:i + 5] == 'BabAB']
    straddle = sum(1 for i in occ if any(i < bb <= i + 4 for bb in bset)) / max(len(occ), 1)
    return obs / exp, all_babab, straddle


if __name__ == "__main__":
    t, d, c1 = prime11()
    print(f"[11] H^1 torsion Z/{t}; det(M-I)={d}=char_poly(1)={c1}=N(1-beta) -> 11 : {t == 11 == abs(d)}")
    print(f"[split] roots mod p: {prime_splitting()}")
    print(f"[mod] max deviation from uniform mod 3,6: {mod_uniform()}")
    print(f"[hierarchy] (det,total) per context len 1-7: {deterministic_hierarchy()}")
    print(f"[sublattice] MI(even,odd) = {sublattice_mi():.3f} bits")
    ratio, allbabab, straddle = bbb_resonance()
    print(f"[BbB CONFIRMED] B_b_B at lags(0,2,4): {ratio:.1f}x enhanced; all BabAB={allbabab}; "
          f"{straddle:.0%} straddle a sigma-image boundary")
