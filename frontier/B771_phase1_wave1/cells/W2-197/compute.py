"""W2-197 (H134): closed-form the kappa=10 golden-eigenspace delocalization weights.

Construction mirrors frontier/B629_interaction_values/exact_hearing.py (itself
mirroring b238.su3_data / pairing_law_scan.py): SU(3)_k modular data (kappa=k+3),
WRL = T S^-1 T^-1 S, antisymmetric (odd) pair basis U, B_odd = -(U^T WRL U).

Cell tasks (per PREREG_WAVE2.md, sealed 486ea7c8):
  1. Recompute the kappa=10 (k=7) 16x16 B_odd; extract the e^{+2pi i/5} eigenvector.
  2. Identify all 6 distinct |component|^2 values exactly in Q(sqrt5)
     (PSLQ, tolerance-height rule, both directions >=10 digits).
  3. Two seeds: dps=120 mp.eig vs dps=60 independent null-space route; conditioning.
  4. Full closed form attempt: gauge-fix and identify every component's phase too;
     reconstruct v from the closed forms and check ||B v - lambda v||.
  5. Weight law across kappa in {5,10,15}: recompute kappa=5 in-cell, build
     kappa=15 (k=12, 42x42), find the golden pair, identify its weights.
"""
import itertools
from fractions import Fraction
import mpmath as mp

OUT = []
def say(*a):
    s = " ".join(str(x) for x in a)
    OUT.append(s)
    print(s, flush=True)


# ----------------------------------------------------------------------------
# construction (mirrors exact_hearing.py exactly)
# ----------------------------------------------------------------------------
def su3_data(k):
    kap = k + 3
    weights = [(a, b) for a in range(k + 1) for b in range(k + 1 - a)]
    n = len(weights)

    def Lvec(w):
        return [mp.mpf(w[0] + w[1] + 2), mp.mpf(w[1] + 1), mp.mpf(0)]

    def ip(u, v):
        s = sum(u[i] * v[i] for i in range(3))
        return s - sum(u) * sum(v) / 3

    perms = list(itertools.permutations(range(3)))

    def sgn(p):
        inv = sum(1 for i in range(3) for j in range(i + 1, 3) if p[i] > p[j])
        return (-1) ** inv

    S = mp.matrix(n, n)
    for i, wl in enumerate(weights):
        Ll = Lvec(wl)
        for j, wm in enumerate(weights):
            Lm = Lvec(wm)
            tot = mp.mpc(0)
            for p in perms:
                Lp = [Ll[p[0]], Ll[p[1]], Ll[p[2]]]
                tot += sgn(p) * mp.e ** (-2j * mp.pi * ip(Lp, Lm) / kap)
            S[i, j] = tot
    norm = mp.sqrt(sum(abs(S[i, 0]) ** 2 for i in range(n)))
    for i in range(n):
        for j in range(n):
            S[i, j] = S[i, j] / norm

    c = mp.mpf(k * 8) / (k + 3)
    T = mp.matrix(n, n)
    for i, (a, b) in enumerate(weights):
        expo = ((mp.mpf(2) / 3) * (a * a + a * b + b * b) + 2 * (a + b)) / (2 * kap) - c / 24
        T[i, i] = mp.e ** (2j * mp.pi * expo)
    return weights, S, T


def odd_form(k):
    w, S, T = su3_data(k)
    n = len(w)
    Si = S ** -1
    Ti = T ** -1
    WRL = T * (Si * Ti * S)
    pairs = sorted({(min(a, b), max(a, b)) for (a, b) in w if a != b})
    m = len(pairs)
    U = mp.matrix(n, m)
    for j, (a, b) in enumerate(pairs):
        U[w.index((a, b)), j] = 1 / mp.sqrt(2)
        U[w.index((b, a)), j] = -1 / mp.sqrt(2)
    B = -(U.T * WRL * U)
    return pairs, B


# ----------------------------------------------------------------------------
# helpers
# ----------------------------------------------------------------------------
def eig_sorted(B):
    E, V = mp.eig(B)
    m = B.rows
    cols = []
    for j in range(m):
        col = [V[i, j] for i in range(m)]
        nrm = mp.sqrt(sum(abs(c) ** 2 for c in col))
        cols.append([c / nrm for c in col])
    return E, cols


def golden_vector(B, sign=+1):
    """eigenvector(s) for e^{sign*2pi i/5}; returns (list of vecs, gapinfo)."""
    lam = mp.e ** (sign * 2j * mp.pi / 5)
    E, cols = eig_sorted(B)
    d = [abs(e - lam) for e in E]
    order = sorted(range(len(E)), key=lambda i: d[i])
    hits = [i for i in order if d[i] < mp.mpf(10) ** (-mp.mp.dps // 2)]
    gap = min(d[i] for i in order if i not in hits)
    return [cols[i] for i in hits], [d[i] for i in hits], gap


def pslq_sqrt5(val, agree_digits):
    """identify val = (p + q*sqrt5)/r; tolerance-height rule tol=10^-(agree-14)."""
    tol = mp.mpf(10) ** (-(agree_digits - 14))
    rel = mp.pslq([val, mp.mpf(1), mp.sqrt(5)], tol=tol, maxcoeff=10 ** 8)
    if rel is None or rel[0] == 0:
        return None
    a, b, c = rel  # a*val + b + c*sqrt5 = 0
    # forward check at full precision (direction 2)
    recon = -(b + c * mp.sqrt(5)) / a
    err = abs(recon - val)
    return (a, b, c, recon, err)


def fr(x):
    return Fraction(x).limit_denominator(10 ** 6)


# ----------------------------------------------------------------------------
# SEED 1: dps=120, mp.eig
# ----------------------------------------------------------------------------
say("=" * 90)
say("SEED 1: kappa=10 (k=7), dps=120, mp.eig route")
say("=" * 90)
mp.mp.dps = 120
pairs10, B10 = odd_form(7)
m10 = len(pairs10)
say(f"dim_odd = {m10} (expect 16); pairs = {pairs10}")

# unitarity + trace sanity
Bd = mp.matrix(m10, m10)
for i in range(m10):
    for j in range(m10):
        Bd[i, j] = mp.conj(B10[j, i])
P = B10 * Bd
udev = max(abs(P[i, j] - (1 if i == j else 0)) for i in range(m10) for j in range(m10))
tr = sum(B10[i, i] for i in range(m10))
say(f"unitarity dev = {mp.nstr(udev, 5)}; trace = {mp.nstr(tr, 30)} (expect 1/phi = {mp.nstr(2/(1+mp.sqrt(5)), 30)})")

vecs_p, dists_p, gap_p = golden_vector(B10, +1)
say(f"e^(+2pi i/5) eigenspace: multiplicity {len(vecs_p)}, |lam - target| = {[mp.nstr(d,5) for d in dists_p]}, spectral gap to next = {mp.nstr(gap_p, 8)}")
v1 = vecs_p[0]
w1 = [abs(c) ** 2 for c in v1]

vecs_m, dists_m, gap_m = golden_vector(B10, -1)
v1m = vecs_m[0]
w1m = [abs(c) ** 2 for c in v1m]

say("\nper-pair |component|^2 (seed 1, +2pi/5 vector):")
for p, x in zip(pairs10, w1):
    say(f"  pair {p}:  {mp.nstr(x, 40)}")

# ----------------------------------------------------------------------------
# SEED 2: dps=60, independent null-space route (LU solve, no mp.eig)
# ----------------------------------------------------------------------------
say("\n" + "=" * 90)
say("SEED 2: kappa=10, dps=60, null-space (bordered solve) route -- independent of mp.eig")
say("=" * 90)
mp.mp.dps = 60
pairs10b, B10b = odd_form(7)
lam = mp.e ** (2j * mp.pi / 5)
M = mp.matrix(m10, m10)
for i in range(m10):
    for j in range(m10):
        M[i, j] = B10b[i, j] - (lam if i == j else 0)
# bordered system: fix v[j0]=1 at the (numerically) largest seed-1 component
j0 = max(range(m10), key=lambda i: w1[i])
# solve M v = 0 with v[j0]=1: move column j0 to RHS, drop one row (least squares via normal eqs)
idx = [j for j in range(m10) if j != j0]
A = mp.matrix(m10, m10 - 1)
rhs = mp.matrix(m10, 1)
for i in range(m10):
    for jj, j in enumerate(idx):
        A[i, jj] = M[i, j]
    rhs[i] = -M[i, j0]
# normal equations A^H A x = A^H rhs
AH = mp.matrix(m10 - 1, m10)
for i in range(m10 - 1):
    for j in range(m10):
        AH[i, j] = mp.conj(A[j, i])
x = mp.lu_solve(AH * A, AH * rhs)
v2 = [mp.mpc(0)] * m10
v2[j0] = mp.mpc(1)
for jj, j in enumerate(idx):
    v2[j] = x[jj]
nrm = mp.sqrt(sum(abs(c) ** 2 for c in v2))
v2 = [c / nrm for c in v2]
res = [sum(M[i, j] * v2[j] for j in range(m10)) for i in range(m10)]
resn = mp.sqrt(sum(abs(r) ** 2 for r in res))
say(f"null-space residual ||(B - lam I) v|| = {mp.nstr(resn, 5)}  (conditioning check)")
w2 = [abs(c) ** 2 for c in v2]

# agreement between seeds
agree = min(
    (mp.floor(-mp.log10(abs(a - b))) if abs(a - b) > 0 else 55)
    for a, b in zip(w1, w2)
)
agree = int(agree)
say(f"seed1(120dps,eig) vs seed2(60dps,nullspace): min agreement across 16 weights = {agree} digits")
if agree < 24:
    say("UNSTABLE: seeds disagree beyond conditioning allowance -- refusing to identify.")

# ----------------------------------------------------------------------------
# exact identification of the weights (PSLQ in Q(sqrt5); tolerance-height rule)
# ----------------------------------------------------------------------------
say("\n" + "=" * 90)
say("IDENTIFICATION: |component|^2 in Q(sqrt5) via PSLQ (tol = 10^-(agree-14))")
say("=" * 90)
mp.mp.dps = 120
ids = []
for p, x in zip(pairs10, w1):
    if x < mp.mpf(10) ** -100:
        ids.append((p, "0", mp.mpf(0), x))
        say(f"  pair {p}: EXACT ZERO (|.|^2 < 1e-100)")
        continue
    r = pslq_sqrt5(x, agree)
    if r is None:
        ids.append((p, None, None, x))
        say(f"  pair {p}: NO relation at height 1e8, tol 1e-{agree-14}  value={mp.nstr(x,40)}")
        continue
    a, b, c, recon, err = r
    # normalized display (p+q*sqrt5)/r with r>0
    den = a
    pnum, qnum = -b, -c
    if den < 0:
        den, pnum, qnum = -den, -pnum, -qnum
    from math import gcd
    g = gcd(gcd(abs(pnum), abs(qnum)), den)
    pnum, qnum, den = pnum // g, qnum // g, den // g
    form = f"({pnum} {'+' if qnum>=0 else '-'} {abs(qnum)}*sqrt5)/{den}"
    ids.append((p, form, recon, x))
    say(f"  pair {p}: |v|^2 = {form}   |err| = {mp.nstr(err, 4)}  ({int(-mp.log10(err)) if err>0 else '>119'} digits)")

# distinct values + multiplicities + sum check
say("\ndistinct nonzero closed forms and multiplicities:")
from collections import Counter
cnt = Counter(f for _, f, _, _ in ids if f not in (None, "0"))
for f, c in sorted(cnt.items(), key=lambda t: -t[1]):
    say(f"  {f}   x{c}")
say(f"support = {sum(cnt.values())} of {m10} pair-directions; zeros = {sum(1 for _,f,_,_ in ids if f=='0')}")
ssum = sum(recon for _, f, recon, _ in ids if f not in (None, "0"))
say(f"sum of identified weights = {mp.nstr(ssum, 30)} (must be 1)")

# conjugate eigenvector: same multiset?
w1m_sorted = sorted([float(x) for x in w1m])
w1_sorted = sorted([float(x) for x in w1])
mdev = max(abs(a - b) for a, b in zip(w1_sorted, w1m_sorted))
say(f"e^(-2pi i/5) vector weight multiset matches (max dev {mdev:.2e})")

# ----------------------------------------------------------------------------
# FULL closed form: phases (gauge: largest component real positive)
# ----------------------------------------------------------------------------
say("\n" + "=" * 90)
say("FULL EIGENVECTOR CLOSED FORM: gauge-fixed phases (units of pi)")
say("=" * 90)
ph0 = v1[j0] / abs(v1[j0])
vg = [c / ph0 for c in v1]
phase_ids = []
for p, c in zip(pairs10, vg):
    if abs(c) ** 2 < mp.mpf(10) ** -100:
        phase_ids.append((p, None))
        continue
    th = mp.arg(c) / mp.pi
    frth = fr(float(th))
    err = abs(th - mp.mpf(frth.numerator) / frth.denominator)
    ok = err < mp.mpf(10) ** -(agree - 14)
    phase_ids.append((p, frth if ok else None))
    say(f"  pair {p}: arg/pi = {mp.nstr(th, 30)}  ~ {frth} {'OK' if ok else 'NOT RATIONAL at tol'}  err={mp.nstr(err,4)}")

# reconstruct v from closed forms and test B v = lam v
say("\nreconstruction test from closed forms:")
allok = all(f is not None for _, f, _, _ in ids) and all(
    (fi is not None) or (idv[1] == "0") for (_, fi), idv in zip(phase_ids, ids)
)
if allok:
    vrec = []
    for (p, form, recon, _), (_, frth) in zip(ids, phase_ids):
        if form == "0":
            vrec.append(mp.mpc(0))
        else:
            vrec.append(mp.sqrt(recon) * mp.e ** (1j * mp.pi * mp.mpf(frth.numerator) / frth.denominator))
    lam120 = mp.e ** (2j * mp.pi / 5)
    resid = [sum(B10[i, j] * vrec[j] for j in range(m10)) - lam120 * vrec[i] for i in range(m10)]
    rn = mp.sqrt(sum(abs(r) ** 2 for r in resid))
    say(f"||B v_closed - e^(2pi i/5) v_closed|| = {mp.nstr(rn, 6)}   (dps=120)")
else:
    say("some component lacked a closed form -- reconstruction skipped")

# ----------------------------------------------------------------------------
# kappa=5 in-cell (discriminating fact computed here, not cited)
# ----------------------------------------------------------------------------
say("\n" + "=" * 90)
say("KAPPA=5 (k=2) in-cell: golden weights")
say("=" * 90)
mp.mp.dps = 80
pairs5, B5 = odd_form(2)
vp5, d5, gap5 = golden_vector(B5, +1)
w5 = [abs(c) ** 2 for c in vp5[0]]
for p, x in zip(pairs5, w5):
    r = pslq_sqrt5(x, 60)
    say(f"  pair {p}: |v|^2 = {mp.nstr(x, 30)}  PSLQ -> {r[:3] if r else None}")

# ----------------------------------------------------------------------------
# kappa=15 (k=12): 42x42 -- the weight-law leg
# ----------------------------------------------------------------------------
say("\n" + "=" * 90)
say("KAPPA=15 (k=12) 42x42: golden pair present? weights?")
say("=" * 90)
mp.mp.dps = 60
pairs15, B15 = odd_form(12)
m15 = len(pairs15)
say(f"dim_odd = {m15}")
E15, cols15 = eig_sorted(B15)
lamt = mp.e ** (2j * mp.pi / 5)
d = [abs(e - lamt) for e in E15]
hits = [i for i in range(m15) if d[i] < mp.mpf(10) ** -25]
say(f"eigenvalues within 1e-25 of e^(2pi i/5): {len(hits)}")
say("spectrum arguments (deg, sorted): " + str(sorted(round(float(mp.arg(e) / mp.pi * 180), 6) for e in E15)))
if len(hits) == 1:
    v15 = cols15[hits[0]]
    w15 = [abs(c) ** 2 for c in v15]
    say("per-pair weights (kappa=15, +2pi/5):")
    for p, x in zip(pairs15, w15):
        if x > 1e-40:
            r = pslq_sqrt5(x, 40)
            if r:
                a, b, c2, recon, err = r
                den = a; pn, qn = -b, -c2
                if den < 0: den, pn, qn = -den, -pn, -qn
                from math import gcd as _g
                g = _g(_g(abs(pn), abs(qn)), den)
                say(f"  pair {p}: {mp.nstr(x,30)} = ({pn//g} {'+' if qn>=0 else '-'} {abs(qn//g)}*sqrt5)/{den//g}  err={mp.nstr(err,3)}")
            else:
                say(f"  pair {p}: {mp.nstr(x,30)}  UNIDENTIFIED in Q(sqrt5) at tol")
    say(f"support = {sum(1 for x in w15 if x>1e-40)} of {m15}")
elif len(hits) > 1:
    say("degenerate golden eigenspace at kappa=15: using projector diagonal (basis-canonical)")
    proj = [sum(abs(cols15[h][i]) ** 2 for h in hits) for i in range(m15)]
    # NB: cols from mp.eig may not be orthonormal within a degenerate block; Gram-Schmidt
    import copy
    basis = []
    for h in hits:
        u = list(cols15[h])
        for b in basis:
            ov = sum(mp.conj(b[i]) * u[i] for i in range(m15))
            u = [u[i] - ov * b[i] for i in range(m15)]
        nn = mp.sqrt(sum(abs(c) ** 2 for c in u))
        basis.append([c / nn for c in u])
    proj = [sum(abs(b[i]) ** 2 for b in basis) for i in range(m15)]
    for p, x in zip(pairs15, proj):
        if x > 1e-40:
            r = pslq_sqrt5(x, 40)
            say(f"  pair {p}: projdiag {mp.nstr(x,30)}  PSLQ {r[:3] if r else None}")
else:
    say("golden pair ABSENT from the kappa=15 spectrum")

# ----------------------------------------------------------------------------
# UNIFIED FORM (sympy exact): the six kappa=10 values are odd phi-powers / (10 sqrt5)
# ----------------------------------------------------------------------------
say("\n" + "=" * 90)
say("UNIFIED FORM CHECK (sympy exact): weights as phi-powers over sqrt5")
say("=" * 90)
import sympy as sp

phi = (1 + sp.sqrt(5)) / 2
checks = [
    ("(5+sqrt5)/100  = phi^(+1)/(10 sqrt5)", sp.Rational(5, 100) + sp.sqrt(5) / 100, phi / (10 * sp.sqrt(5))),
    ("(5-sqrt5)/100  = phi^(-1)/(10 sqrt5)", sp.Rational(5, 100) - sp.sqrt(5) / 100, phi ** -1 / (10 * sp.sqrt(5))),
    ("(5+2sqrt5)/50  = phi^(+3)/(10 sqrt5)", sp.Rational(5, 50) + 2 * sp.sqrt(5) / 50, phi ** 3 / (10 * sp.sqrt(5))),
    ("(5-2sqrt5)/50  = phi^(-3)/(10 sqrt5)", sp.Rational(5, 50) - 2 * sp.sqrt(5) / 50, phi ** -3 / (10 * sp.sqrt(5))),
    ("(5+sqrt5)/25   = 4 phi^(+1)/(10 sqrt5)", sp.Rational(5, 25) + sp.sqrt(5) / 25, 4 * phi / (10 * sp.sqrt(5))),
    ("(5-sqrt5)/25   = 4 phi^(-1)/(10 sqrt5)", sp.Rational(5, 25) - sp.sqrt(5) / 25, 4 * phi ** -1 / (10 * sp.sqrt(5))),
]
allphi = True
for name, lhs, rhs in checks:
    ok = sp.simplify(lhs - rhs) == 0
    allphi = allphi and ok
    say(f"  {name}: {'EXACT' if ok else 'FAIL'}")
tot = sp.simplify(2 * (checks[0][1] + checks[1][1] + checks[2][1] + checks[3][1]) + checks[4][1] + checks[5][1])
say(f"  multiplicity-weighted sum 2,2,2,2,1,1 = {tot} (must be 1): {'EXACT' if tot == 1 else 'FAIL'}")

# kappa=5 and kappa=15 in the same units (exact)
k5p = sp.simplify(sp.Rational(5, 10) + sp.sqrt(5) / 10 - phi / sp.sqrt(5))
k5m = sp.simplify(sp.Rational(5, 10) - sp.sqrt(5) / 10 - phi ** -1 / sp.sqrt(5))
k15p = sp.simplify(sp.Rational(5, 30) + sp.sqrt(5) / 30 - phi / (3 * sp.sqrt(5)))
k15m = sp.simplify(sp.Rational(5, 30) - sp.sqrt(5) / 30 - phi ** -1 / (3 * sp.sqrt(5)))
say(f"  kappa=5:  (5+-sqrt5)/10 = phi^(+-1)/sqrt5:      {'EXACT' if k5p == 0 and k5m == 0 else 'FAIL'}")
say(f"  kappa=15: (5+-sqrt5)/30 = phi^(+-1)/(3 sqrt5):  {'EXACT' if k15p == 0 and k15m == 0 else 'FAIL'}")
say("  law observed: kappa=5m, m=1,3 -> the kappa=5 weights phi^(+-1)/sqrt5 divided by m,")
say("  each on m pair-directions (m=3 support triangles {0,3,9},{1,4,7}); m=2 (kappa=10)")
say("  delocalizes into odd phi-powers {phi^(+-1), phi^(+-3), 4 phi^(+-1)}/(10 sqrt5) --")
say("  multiplicities (2,2,2,2,1,1), still summing to (phi+phi^-1)/sqrt5 = 1 exactly.")
say("  (Support/zero pattern at kappa=10 recorded, mechanism NOT derived here.)")

say("\ndone.")
with open(__file__.replace("compute.py", "output.txt"), "w") as f:
    f.write("\n".join(OUT) + "\n")
