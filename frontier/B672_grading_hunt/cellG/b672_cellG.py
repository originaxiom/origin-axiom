#!/usr/bin/env python3
"""B672 / cellG -- THE GRADING HUNT (L108 first search).

QUESTION: does any banked framework object carry an infinite non-periodic
integer grading whose graded traces reproduce the weight-5 doublet streams
banked in B666/cellW33 (comp1 = q^{1/5}(1 + 42q - 108q^2 - 4q^3 - 378q^4 + ...))?

CANDIDATES (two-outcome each: MATCH with >=10 verified coefficients / MISS
with the first differing coefficient):
  C1  the B205 generic-q skein tower: the q-continued-fraction / q-metallic
      mean at the golden specialization ([phi]_q, MGO normal form; plus the
      naive fixed-point deformation z = 1 + q/z; plus the banked q-Chebyshev
      leading stream (1+q^-2)^m).
  C2  the word-length / geodesic filtration: generating series of traces of
      R^a L^b words graded by length (three natural gradings, each verified
      against brute-force matrix enumeration before use).
  C3  Habiro-style reading of the ladder certificate (B662/cellG
      l100_results.json): the 130-frequency support as a q-object
      (scalar-free ratio comparison + the exact 2-adic support census
      against the Rogers-Ramanujan theta classes).
  C4  eta-quotient / theta recognition: exact formal-log linear solver over
      the menus {E1,E5}, {E1,E5,E_{1/5}}, {N1,N2,E1}, {N1,N2,E1,E5} with
      N1,N2 = the Rogers-Ramanujan numerators; positive controls included.

Targets are read from the banked machine-readable JSON
(frontier/B666_leads_campaign/cellW33/cellW33_doublet_streams.json) AND
independently recomputed from the banked Sym^25 coefficient vectors +
Euler products (gate: verbatim agreement on every banked term), then
extended to 100 terms for the comparisons.

Exact arithmetic (int / Fraction) in every decisive step. Bounded run.
"""

import json, os, sys, time
from fractions import Fraction as Fr

T0 = time.time()
_HERE = os.path.dirname(os.path.abspath(__file__))
_REPO = os.path.abspath(os.path.join(_HERE, "..", "..", ".."))
OUT = []


def log(msg=""):
    print(msg)
    OUT.append(msg)


# ---------------------------------------------------------------- series ops
def smul(a, b, N):
    c = [Fr(0)] * (N + 1)
    for i, ai in enumerate(a):
        if ai == 0 or i > N:
            continue
        for j, bj in enumerate(b):
            if i + j > N:
                break
            if bj:
                c[i + j] += ai * bj
    return c


def spow(a, n, N):
    r = [Fr(1)] + [Fr(0)] * N
    base = a[: N + 1] + [Fr(0)] * max(0, N + 1 - len(a))
    while n:
        if n & 1:
            r = smul(r, base, N)
        base = smul(base, base, N)
        n >>= 1
    return r


def sinv(a, N):
    assert a[0] == 1
    inv = [Fr(1)] + [Fr(0)] * N
    for n in range(1, N + 1):
        s = Fr(0)
        for k in range(1, n + 1):
            if k < len(a) and a[k]:
                s += a[k] * inv[n - k]
        inv[n] = -s
    return inv


def slog(a, N):
    """formal log of a series with a[0] == 1."""
    assert a[0] == 1
    l = [Fr(0)] * (N + 1)
    for n in range(1, N + 1):
        s = Fr(0)
        for k in range(1, n):
            if n - k < len(a) and a[n - k]:
                s += k * l[k] * a[n - k]
        an = a[n] if n < len(a) else Fr(0)
        l[n] = an - s / n
    return l


def ssqrt(f, N):
    """sqrt of a series with f[0] == 1."""
    assert f[0] == 1
    s = [Fr(1)] + [Fr(0)] * N
    for n in range(1, N + 1):
        acc = Fr(0)
        for i in range(1, n):
            acc += s[i] * s[n - i]
        fn = f[n] if n < len(f) else Fr(0)
        s[n] = (fn - acc) / 2
    return s


def euler_prod(residues, modulus, N):
    """prod over k>=1, k mod modulus in residues, of (1 - q^k)."""
    r = [Fr(1)] + [Fr(0)] * N
    for k in range(1, N + 1):
        if k % modulus in residues or (0 in residues and k % modulus == 0):
            new = [Fr(0)] * (N + 1)
            for i, ri in enumerate(r):
                if ri:
                    new[i] += ri
                    if i + k <= N:
                        new[i + k] -= ri
            r = new
    return r


def theta_num(c, N):
    """sum_{m in Z} (-1)^m q^{m(5m+c)/2}  (c = 1 -> N1, c = 3 -> N2)."""
    s = [Fr(0)] * (N + 1)
    m = 0
    while True:
        hit = False
        for mm in ([0] if m == 0 else [m, -m]):
            e = mm * (5 * mm + c) // 2
            if 0 <= e <= N:
                s[e] += Fr((-1) ** (mm % 2))
                hit = True
        if not hit and m * (5 * m - abs(c)) // 2 > N:
            break
        m += 1
    return s


def ints(s, upto=None):
    out = []
    for x in s[: (upto if upto else len(s))]:
        out.append(int(x) if x.denominator == 1 else x)
    return out


def first_mismatch_ratio(cand, targ, nmax):
    """scalar-free: first n >= 1 with cand[n]/cand[0] != targ[n]/targ[0].
    Returns (n, cand_ratio, targ_ratio) or None if agree through nmax."""
    assert cand[0] != 0 and targ[0] != 0
    for n in range(1, nmax + 1):
        cr = Fr(cand[n], 1) / cand[0] if isinstance(cand[n], int) else cand[n] / cand[0]
        tr = Fr(targ[n], 1) / targ[0] if isinstance(targ[n], int) else targ[n] / targ[0]
        if cr != tr:
            return (n, cr, tr)
    return None


# ---------------------------------------------------------------- S0: targets
log("== S0: the targets -- banked streams loaded + independently recomputed ==")
N = 100  # comparison horizon

with open(os.path.join(_REPO, "frontier", "B666_leads_campaign", "cellW33",
                       "cellW33_doublet_streams.json")) as fh:
    W33 = json.load(fh)

banked = {k: [int(x) for x in v] for k, v in W33["doublet_streams_integer"].items()}
banked_row1 = [int(x) for x in W33["sextet_rows"]["row1 (F1^5+2F2^5)"]]

# independent recomputation from the banked Sym^25 coefficient vectors:
#   comp = q^{alpha} * E1^{-15} * sum_i c_i N1^{25-j_i} N2^{j_i} q^{(j_i-r)/5}
# with alpha = r/5 the leading fractional power, j_i the F2-exponents.
NH = N + 8
E1 = euler_prod({1, 2, 3, 4, 0}, 5, NH)          # (q;q)
N1 = theta_num(1, NH)
N2 = theta_num(3, NH)
E1i15 = sinv(spow(E1, 15, NH), NH)

coeffvecs = {
    "2hat'.comp1": [(1, 1), (6, 28), (11, -456), (16, 247), (21, 26)],
    "2hat'.comp2": [(4, 26), (9, -247), (14, -456), (19, -28), (24, 1)],
    "2hat.comp1": [(2, 1), (7, -22), (12, 119), (17, 22), (22, 1)],
    "2hat.comp2": [(3, 1), (8, -22), (13, 119), (18, 22), (23, 1)],
}
targets = {}
for name, vec in coeffvecs.items():
    r = vec[0][0] % 5  # leading fractional power numerator
    acc = [Fr(0)] * (NH + 1)
    for j, c in vec:
        term = smul(spow(N1, 25 - j, NH), spow(N2, j, NH), NH)
        shift = (j - r) // 5
        for i, t in enumerate(term):
            if i + shift <= NH and t:
                acc[i + shift] += c * t
    stream = smul(acc, E1i15, NH)
    targets[name] = ints(stream, N + 1)
    nb = len(banked[name])
    ok = targets[name][:nb] == banked[name]
    log("  %-14s recomputed; gate vs banked (%d terms): %s; extended to %d terms"
        % (name, nb, ok, N + 1))
    assert ok, "recomputation disagrees with the banked stream"

# row1 sextet (weight 1) for the C4 side-test: (F1^5 + 2 F2^5)
A5 = smul(spow(N1, 5, NH), sinv(spow(E1, 3, NH), NH), NH)     # F1^5 = N1^5/E1^3
B5 = smul(spow(N2, 5, NH), sinv(spow(E1, 3, NH), NH), NH)     # F2^5/q = N2^5/E1^3
row1 = [A5[i] + 2 * (B5[i - 1] if i >= 1 else 0) for i in range(NH + 1)]
ok = ints(row1, len(banked_row1)) == banked_row1
log("  row1 sextet   recomputed; gate vs banked (%d terms): %s" % (len(banked_row1), ok))
assert ok
row1 = ints(row1, N + 1)

log("  target heads: 2hat'.comp1 = q^(1/5)*%s..." % targets["2hat'.comp1"][:6])

# ------------------------------------------------------- C1: B205 q-tower
log("")
log("== C1: the B205 generic-q skein tower (q-metallic mean, golden specialization) ==")

# C1a  naive fixed-point deformation of z -> 1 + 1/z:  z = 1 + q/z
#      => z^2 - z - q = 0 => z = (1 + sqrt(1+4q))/2  (signed Catalan stream)
f = [Fr(1), Fr(4)] + [Fr(0)] * (N - 1)
c1a = [x / 2 for x in ssqrt(f, N)]
c1a[0] += Fr(1, 2)
log("  C1a  z = 1+q/z fixed point: stream %s..." % ints(c1a, 8))
assert all(x.denominator == 1 for x in c1a), "C1a not integral"

# C1b  the MGO q-golden ratio [phi]_q = (q^2+q-1+sqrt(q^4+2q^3-q^2+2q+1))/(2q)
#      gates: (i) q=1 value = phi (checked exactly: numerator = 1+sqrt5),
#             (ii) integer coefficients (MGO integrality),
#             (iii) series starts 1 + q^2 - q^3 + ...
disc = [Fr(1), Fr(2), Fr(-1), Fr(2), Fr(1)] + [Fr(0)] * (N - 3)
sq = ssqrt(disc, N + 1)
num = [Fr(0)] * (N + 2)
num[0] = Fr(-1); num[1] = Fr(1); num[2] = Fr(1)
for i, x in enumerate(sq):
    num[i] += x
assert num[0] == 0, "MGO numerator must vanish at q^0"
c1b = [num[i + 1] / 2 for i in range(N + 1)]
gate_int = all(x.denominator == 1 for x in c1b)
gate_val_q1 = (sum(disc[:5], Fr(0)) == 5)  # disc(1) = 5 => sqrt -> sqrt5 => phi
log("  C1b  MGO [phi]_q: stream %s...; integer-coeff gate: %s; disc(1)=5 gate: %s"
    % (ints(c1b, 9), gate_int, gate_val_q1))
assert gate_int and gate_val_q1

# C1c  the banked q-Chebyshev leading stream (1+q^-2)^m: finite (m+1 terms) per m
log("  C1c  q-Chebyshev leading coeff (1+q^-2)^m: FINITE (m+1 terms) for every m")

mm_table = []
for cname, cs in (("C1a", c1a), ("C1b", c1b)):
    for tname, ts in targets.items():
        r = first_mismatch_ratio(cs, [Fr(x) for x in ts], min(N, len(ts) - 1))
        assert r is not None
        mm_table.append((cname, tname, r[0], r[1], r[2]))
        log("    %s vs %-14s: first mismatch at n=%d (cand ratio %s vs target %s)"
            % (cname, tname, r[0], r[1], r[2]))
log("  C1 VERDICT: MISS (every sub-candidate; first mismatches n = %s; C1c finite vs infinite target)"
    % sorted(set(x[2] for x in mm_table)))

# ------------------------------------------------- C2: word-length filtration
log("")
log("== C2: the word-length / geodesic filtration (traces of R^a L^b words) ==")
R = ((1, 1), (0, 1))
L = ((1, 0), (1, 1))


def mmul(X, Y):
    return ((X[0][0] * Y[0][0] + X[0][1] * Y[1][0], X[0][0] * Y[0][1] + X[0][1] * Y[1][1]),
            (X[1][0] * Y[0][0] + X[1][1] * Y[1][0], X[1][0] * Y[0][1] + X[1][1] * Y[1][1]))


def mpow(X, n):
    Rr = ((1, 0), (0, 1))
    while n:
        if n & 1:
            Rr = mmul(Rr, X)
        X = mmul(X, X)
        n >>= 1
    return Rr


def tr(X):
    return X[0][0] + X[1][1]


# gate: tr(R^a L^b) = 2 + ab, exact, a,b <= 8
gate = all(tr(mmul(mpow(R, a), mpow(L, b))) == 2 + a * b
           for a in range(1, 9) for b in range(1, 9))
log("  gate tr(R^a L^b) = 2 + ab (a,b <= 8, exact matrices): %s" % gate)
assert gate
# gate: sum over all 2^n words of length n of tr = tr((R+L)^n), n <= 10
S = ((2, 1), (1, 2))
gate2 = True
for n in range(1, 11):
    tot = 0
    for w in range(2 ** n):
        M = ((1, 0), (0, 1))
        for b in range(n):
            M = mmul(M, R if (w >> b) & 1 else L)
        tot += tr(M)
    if tot != tr(mpow(S, n)):
        gate2 = False
log("  gate sum_{|w|=n} tr(w) = tr((R+L)^n) = 3^n + 1 (n <= 10, brute force): %s" % gate2)
assert gate2

# C2a: G(x) = sum_{a,b>=1} tr(R^a L^b) x^{a+b}; coeff_n = 2(n-1) + (n-1)n(n+1)/6
c2a = [Fr(0), Fr(0)] + [Fr(2 * (n - 1) + (n - 1) * n * (n + 1) // 6) for n in range(2, N + 1)]
# C2b: coeff_n = 3^n + 1
c2b = [Fr(2)] + [Fr(3 ** n + 1) for n in range(1, N + 1)]
# C2c: golden geodesic tr((RL)^n) = Lucas L_{2n}
RL = mmul(R, L)
c2c = [Fr(2)] + [Fr(tr(mpow(RL, n))) for n in range(1, N + 1)]
log("  C2a stream (n>=2): %s..." % ints(c2a[2:], 6))
log("  C2b stream (n>=1): %s..." % ints(c2b[1:], 6))
log("  C2c stream (n>=1): %s..." % ints(c2c[1:], 6))

for cname, cs, off in (("C2a", c2a[2:], 2), ("C2b", c2b[1:], 1), ("C2c", c2c[1:], 1)):
    for tname, ts in targets.items():
        r = first_mismatch_ratio(cs, [Fr(x) for x in ts], min(len(cs) - 1, len(ts) - 1))
        assert r is not None
        log("    %s vs %-14s: first mismatch at n=%d (cand ratio %s vs target %s)"
            % (cname, tname, r[0], r[1], r[2]))
log("  (structural: all three C2 streams are positive and monotone from n>=2;")
log("   every target stream changes sign by n=2 -- no scalar/offset can rescue)")
log("  C2 VERDICT: MISS (first mismatch n=1 in every pairing)")

# ------------------------------------- C3: the ladder certificate as q-object
log("")
log("== C3: the ladder certificate's 130-frequency support as a q-object ==")
with open(os.path.join(_REPO, "frontier", "B662_successor_campaign", "cellG",
                       "l100_results.json")) as fh:
    L100 = json.load(fh)
sup = L100["support"]
log("  loaded support: %d frequencies (banked n_support = %d)" % (len(sup), L100["n_support"]))
assert len(sup) == 130

entries = []  # (q as Fraction, (A, B)) with coeff = A + B*sqrt5
for k, v in sup.items():
    qv = Fr(k)
    A = Fr(v.get("coeff_sqrt1", "0"))
    B = Fr(v.get("coeff_sqrt5", "0"))
    entries.append((qv, A, B))
entries.sort(key=lambda t: t[0])

# Habiro-style reading: Zhat(x) = sum_q N_q x^{q*D/2} with D = lcm of denominators
from math import gcd
Dl = 1
for qv, _, _ in entries:
    Dl = Dl * qv.denominator // gcd(Dl, qv.denominator)
log("  common denominator of the support frequencies: D = %d" % Dl)
log("  => Zhat(x) = sum N_q x^(q*%d) : a FINITE polynomial, %d terms, coefficients in Q(sqrt5)"
    % (Dl, len(entries)))

# scalar-free ratio comparison against each target (align leading nonzero terms,
# successive-exponent coefficient ratios; ratios computed exactly in Q(sqrt5))
def qsqrt5_div(a, b):
    """(a0+a1*s5)/(b0+b1*s5) exactly, as a pair."""
    a0, a1 = a
    b0, b1 = b
    den = b0 * b0 - 5 * b1 * b1
    assert den != 0
    return ((a0 * b0 - 5 * a1 * b1) / den, (a1 * b0 - a0 * b1) / den)

lead = entries[0]
log("  leading support term: q = %s, coeff = %s + %s*sqrt5" % (lead[0], lead[1], lead[2]))
for tname, ts in targets.items():
    hit = None
    for n in range(1, min(len(entries), len(ts)) ):
        cr = qsqrt5_div((entries[n][1], entries[n][2]), (lead[1], lead[2]))
        trat = (Fr(ts[n], ts[0]), Fr(0))
        if cr != trat:
            hit = (n, cr, trat)
            break
    assert hit is not None
    log("    Zhat vs %-14s: first ratio mismatch at term n=%d (cand %s+%s*sqrt5 vs target %s)"
        % (tname, hit[0], hit[1][0], hit[1][1], hit[2][0]))

# the exact 2-adic census: the RR theta classes need order-80 characters
# F1-theta exponents (10m+1)^2/40 == {1/40, 41/40} mod 2  (order 80)
# F2-theta exponents (10m+3)^2/40 == {9/40, 49/40} mod 2  (order 80)
cls1 = set()
cls2 = set()
for m in range(-40, 41):
    cls1.add(Fr((10 * m + 1) ** 2, 40) % 2)
    cls2.add(Fr((10 * m + 3) ** 2, 40) % 2)
log("  RR theta classes mod 2: F1 -> %s, F2 -> %s (both = order-80 characters)"
    % (sorted(cls1), sorted(cls2)))
max_ord = max(2 * qv.denominator // gcd(2, qv.numerator) if qv != 0 else 1
              for qv, _, _ in entries)
v2max = max((qv.denominator & -qv.denominator).bit_length() - 1 for qv, _, _ in entries)
overlap1 = [(qv) for qv, _, _ in entries if (qv % 2) in cls1]
overlap2 = [(qv) for qv, _, _ in entries if (qv % 2) in cls2]
log("  support census: max character order = %d; max v2(denominator) = %d (theta needs v2 = 3, i.e. denominator 40)"
    % (max_ord, v2max))
log("  support frequencies lying in an RR theta class: F1-classes %d, F2-classes %d"
    % (len(overlap1), len(overlap2)))
assert v2max <= 2 and not overlap1 and not overlap2
log("  => EXACT NO-GO for the C3->RR bridge: every RR theta character has order 80;")
log("     the banked period P = 175560 has 2-part 8, so order-80 characters cannot")
log("     occur in the support -- and indeed 0 of the 130 frequencies hit an RR class")
log("  C3 VERDICT: MISS (finite 130-term object; first ratio mismatch at term n=1")
log("     for every target; the RR theta classes are provably absent from the support)")

# ------------------------------------------- C4: eta-quotient / RR recognition
log("")
log("== C4: eta-quotient / theta recognition of the target streams ==")

# 4a: exact obstruction for the pure {eta(tau), eta(5tau)} menu at weight 5:
#     leading exponent (a+5b)/24 must lie in r/5 + Z (r = 1,2,3,4) with a+b = 10
#     => 5(a+5b) == 24 r mod 120; LHS == 0 mod 5, RHS == 4r != 0 mod 5. Impossible.
bad = []
for r in (1, 2, 3, 4):
    for a in range(-200, 211):
        b = 10 - a
        if (Fr(a + 5 * b, 24) - Fr(r, 5)) % 1 == 0:
            bad.append((r, a, b))
log("  C4a  eta(tau)^a eta(5tau)^b, a+b=10, exponent == r/5 mod 1: solutions found = %d"
    % len(bad))
log("       (mod-5 proof: 5(a+5b) == 0, 24r == 4r != 0 mod 5 -- structurally impossible)")
assert not bad

# 4b/4c: the exact formal-log linear solver.
#   candidate menus of log-series; solve the first k coefficient equations
#   exactly (Gaussian elimination over Q), verify the remaining ones to N.
E5 = [Fr(0)] * (N + 1)
tmp = euler_prod({0}, 5, N)   # (q^5;q^5)
E5 = tmp
logE1 = slog(E1[: N + 1], N)
logE5 = slog(E5, N)
logN1 = slog(N1[: N + 1], N)
logN2 = slog(N2[: N + 1], N)

# the E_{1/5} reduction: log(q^{1/5};q^{1/5}) has nonzero coefficients at
# genuinely fractional exponents k/5 (k not divisible by 5); an integer-exponent
# target forces its coefficient to zero.  Witness the first few exactly:
frac_witness = []
for k in (1, 2, 3, 4, 6):
    # coefficient of x^{k/5} in log prod (1 - x^{j/5}) = -sum_{d | k} (1/d) over... :
    s = Fr(0)
    for d in range(1, k + 1):
        if k % d == 0:
            s -= Fr(1, k // d)
    frac_witness.append((Fr(k, 5), s))
log("  C4b  E_{1/5} reduction: log E_{1/5} fractional-exponent coefficients %s"
    % [(str(e), str(c)) for e, c in frac_witness[:3]])
assert all(c != 0 for _, c in frac_witness)
log("       all nonzero => any integer-exponent target forces the E_{1/5} exponent = 0;")
log("       the {E1, E5, E_{1/5}} menu reduces exactly to {E1, E5}")


def solve_menu(menu_logs, target_log, N, names):
    """exact: find rational x with sum x_i menu_i = target_log; return
    (solution, None) on full verification or (solution_or_None, first_fail)."""
    k = len(menu_logs)
    # pick k rows with a nonsingular system: use first coefficients 1..N
    rows, rhs, used = [], [], []
    import itertools
    n = 1
    while len(rows) < k and n <= N:
        cand = [ml[n] for ml in menu_logs]
        # rank check by trial elimination
        test = [r[:] for r in rows] + [cand[:]]
        tr_rhs = rhs[:] + [target_log[n]]
        # gaussian elim to check independence
        m = [row[:] + [rv] for row, rv in zip(test, tr_rhs)]
        rank = 0
        for col in range(k):
            piv = None
            for i in range(rank, len(m)):
                if m[i][col] != 0:
                    piv = i
                    break
            if piv is None:
                continue
            m[rank], m[piv] = m[piv], m[rank]
            for i in range(len(m)):
                if i != rank and m[i][col] != 0:
                    f = m[i][col] / m[rank][col]
                    m[i] = [a - f * b for a, b in zip(m[i], m[rank])]
            rank += 1
        if rank == len(test):
            rows.append(cand)
            rhs.append(target_log[n])
            used.append(n)
        n += 1
    if len(rows) < k:
        return None, ("underdetermined", None)
    # solve exactly
    m = [row[:] + [rv] for row, rv in zip(rows, rhs)]
    for col in range(k):
        piv = next(i for i in range(col, k) if m[i][col] != 0)
        m[col], m[piv] = m[piv], m[col]
        pv = m[col][col]
        m[col] = [a / pv for a in m[col]]
        for i in range(k):
            if i != col and m[i][col] != 0:
                f = m[i][col]
                m[i] = [a - f * b for a, b in zip(m[i], m[col])]
    x = [m[i][k] for i in range(k)]
    # verify every coefficient 1..N
    for n in range(1, N + 1):
        lhs = sum(x[i] * menu_logs[i][n] for i in range(k))
        if lhs != target_log[n]:
            return x, (n, lhs, target_log[n])
    return x, None


# positive controls: the solver must recognize known quotients exactly
ctrl = smul(spow(E1, 2, N), spow(E5, 3, N), N)
x, fail = solve_menu([logE1, logE5], slog(ctrl, N), N, ["E1", "E5"])
log("  control 1: E1^2 E5^3 recognized over {E1,E5}: x = %s, verified to n=%d: %s"
    % ([str(v) for v in x], N, fail is None))
assert x == [Fr(2), Fr(3)] and fail is None
ctrl2 = smul(spow(N1, 3, N), sinv(spow(E1, 2, N), N), N)
x, fail = solve_menu([logN1, logN2, logE1], slog(ctrl2, N), N, ["N1", "N2", "E1"])
log("  control 2: N1^3 E1^-2 recognized over {N1,N2,E1}: x = %s, verified: %s"
    % ([str(v) for v in x], fail is None))
assert x == [Fr(3), Fr(0), Fr(-2)] and fail is None

menus = [
    ("{E1,E5}", [logE1, logE5], ["E1", "E5"]),
    ("{N1,N2,E1}", [logN1, logN2, logE1], ["N1", "N2", "E1"]),
    ("{N1,N2,E1,E5}", [logN1, logN2, logE1, logE5], ["N1", "N2", "E1", "E5"]),
]
all_targets = dict(targets)
all_targets["row1 sextet"] = row1
miss4 = []
match4 = []
for tname, ts in all_targets.items():
    lead_c = ts[0]
    norm = [Fr(x, lead_c) for x in ts[: N + 1]]
    tlog = slog(norm, N)
    for mname, mlogs, names in menus:
        x, fail = solve_menu(mlogs, tlog, N, names)
        if fail is None:
            log("    !! %s over %s: MATCH x = %s -- ALL %d coefficients verified (S5 verifies further)"
                % (tname, mname, [str(v) for v in x], N))
            match4.append((tname, mname, [str(v) for v in x]))
        else:
            if isinstance(fail[0], int):
                n_fail = fail[0]
                log("    %-14s over %-13s: exact solve from first coeffs -> x = %s;"
                    % (tname, mname, [str(v) for v in x]))
                log("      %-12s FAILS at n=%d (lhs %s vs target %s) -- NOT a monomial in this menu"
                    % ("", n_fail, fail[1], fail[2]))
                miss4.append((tname, mname, n_fail))
            else:
                log("    %-14s over %-13s: system underdetermined -- degenerate, MISS" % (tname, mname))
                miss4.append((tname, mname, -1))
log("  C4 status: %d MATCH(es) fired, %d monomial rejections recorded"
    % (len(match4), len(miss4)))

# --------------------------- S5: THE MATCH -- independent verification to 300
log("")
log("== S5: the 2hat MATCH verified at product level to 300 terms + the 2hat' ansatz ==")
NV = 300
NVH = NV + 8
E1v = euler_prod({1, 2, 3, 4, 0}, 5, NVH)
N1v = theta_num(1, NVH)
N2v = theta_num(3, NVH)
E1v24 = spow(E1v, 24, NVH)


def sym25_numerator(name, NN):
    """the banked Sym^25 numerator A(q) = sum_j c_j N1^{25-j} N2^j q^{(j-r)/5}."""
    vec = coeffvecs[name]
    r = vec[0][0] % 5
    acc = [Fr(0)] * (NN + 1)
    for j, c in vec:
        term = smul(spow(N1v, 25 - j, NN), spow(N2v, j, NN), NN)
        shift = (j - r) // 5
        for i, t in enumerate(term):
            if i + shift <= NN and t:
                acc[i + shift] += c * t
    return acc


# claimed identities (from the solver, re-verified WITHOUT logs or inversion):
#   2hat.comp1 = q^{2/5} N1 (q;q)^9   <=>  A(2hat.comp1)  = N1 (q;q)^24
#   2hat.comp2 = q^{3/5} N2 (q;q)^9   <=>  A(2hat.comp2)  = N2 (q;q)^24
for name, th, tag in (("2hat.comp1", N1v, "N1"), ("2hat.comp2", N2v, "N2")):
    acc = sym25_numerator(name, NVH)
    rhs = smul(th, E1v24, NVH)
    ok = acc[: NV + 1] == rhs[: NV + 1]
    log("  %s: Sym^25 numerator == %s * (q;q)^24 to %d terms: %s" % (name, tag, NV + 1, ok))
    assert ok
log("  => THE IDENTITY (exact, 301 coefficients each, product level):")
log("       Y^(5)_2hat.comp1 = q^{2/5} N1(q) (q;q)^9  = F1 * eta^{48/5}")
log("       Y^(5)_2hat.comp2 = q^{3/5} N2(q) (q;q)^9  = F2 * eta^{48/5}")
log("     with N1 = (q;q) G(q), N2 = (q;q) H(q) = THE ROGERS-RAMANUJAN NUMERATORS.")
log("     Corollary: comp2/comp1 = q^{1/5} N2/N1 = R(q), the Rogers-Ramanujan")
log("     continued fraction.  The whole 2hat doublet = the F-doublet times the")
log("     scalar eta^{48/5} (weight 24/5 + 1/5 = 5, consistent).")

# the derived 2hat' ansatz, forced by the same weight counting:
#   2hat' = eta^{24/5} * P13(F1,F2), deg 13 (weight 12/5 + 13/5 = 5);
#   fractional-power bookkeeping forces the F2-degree i == 0 mod 5 (comp1)
#   and i == 3 mod 5 (comp2), so three unknowns per component:
#   A(comp1') = (q;q)^12 (d0 N1^13 + d5 q N1^8 N2^5 + d10 q^2 N1^3 N2^10)
#   A(comp2') = (q;q)^12 (d3 N1^10 N2^3 + d8 q N1^5 N2^8 + d13 q^2 N2^13)
E1v12 = spow(E1v, 12, NVH)


def solve_linear_exact(basis, target, NN):
    """exact: x with sum x_i basis_i = target, solved from the first independent
    rows, verified on ALL coefficients 0..NN.  Returns (x, None) or (x, fail_n)."""
    k = len(basis)
    rows, rhs2 = [], []
    n = 0
    while len(rows) < k and n <= NN:
        cand = [b[n] for b in basis]
        test = [r_[:] for r_ in rows] + [cand[:]]
        m = [row[:] for row in test]
        rank = 0
        for col in range(k):
            piv = next((i for i in range(rank, len(m)) if m[i][col] != 0), None)
            if piv is None:
                continue
            m[rank], m[piv] = m[piv], m[rank]
            for i2 in range(len(m)):
                if i2 != rank and m[i2][col] != 0:
                    f2 = m[i2][col] / m[rank][col]
                    m[i2] = [a - f2 * b for a, b in zip(m[i2], m[rank])]
            rank += 1
        if rank == len(test):
            rows.append(cand)
            rhs2.append(target[n])
        n += 1
    if len(rows) < k:
        return None, "underdetermined"
    m = [row[:] + [rv] for row, rv in zip(rows, rhs2)]
    for col in range(k):
        piv = next(i for i in range(col, k) if m[i][col] != 0)
        m[col], m[piv] = m[piv], m[col]
        pv = m[col][col]
        m[col] = [a / pv for a in m[col]]
        for i2 in range(k):
            if i2 != col and m[i2][col] != 0:
                f2 = m[i2][col]
                m[i2] = [a - f2 * b for a, b in zip(m[i2], m[col])]
    x = [m[i2][k] for i2 in range(k)]
    for n in range(NN + 1):
        lhs = sum(x[i2] * basis[i2][n] for i2 in range(k))
        if lhs != target[n]:
            return x, n
    return x, None


def p13_basis(triples):
    out = []
    for shift, a13, b13 in triples:
        term = smul(spow(N1v, a13, NVH), spow(N2v, b13, NVH), NVH)
        term = smul(term, E1v12, NVH)
        out.append([Fr(0)] * shift + term[: NVH + 1 - shift])
    return out


p13_hits = {}
for name, triples, labels in (
        ("2hat'.comp1", [(0, 13, 0), (1, 8, 5), (2, 3, 10)],
         ["F1^13", "F1^8 F2^5", "F1^3 F2^10"]),
        ("2hat'.comp2", [(0, 10, 3), (1, 5, 8), (2, 0, 13)],
         ["F1^10 F2^3", "F1^5 F2^8", "F2^13"])):
    acc = sym25_numerator(name, NVH)
    x, failn = solve_linear_exact(p13_basis(triples), acc, NV)
    if failn is None:
        log("  %s = eta^{24/5} * (%s): MATCH, %d coefficients verified"
            % (name, " + ".join("%s %s" % (c, l) for c, l in zip(x, labels)), NV + 1))
        p13_hits[name] = [str(v) for v in x]
    else:
        log("  %s eta^{24/5}*P13 ansatz: x = %s; FAILS at n=%s -- MISS for this ansatz"
            % (name, None if x is None else [str(v) for v in x], failn))
p13_hit = len(p13_hits) == 2

# ---------------------------------------------------------------- the verdict
log("")
log("== OVERALL VERDICT (two-outcome, per candidate) ==")
log("  C1 B205 q-tower (q-metallic golden)         : MISS (first mismatch n=1 in all 8 pairings;")
log("       MGO [phi]_q and the Catalan deformation both integral but wrong from the")
log("       second coefficient; the banked q-Chebyshev stream is finite)")
log("  C2 word-length/geodesic filtration          : MISS (first mismatch n=1 in all 12 pairings;")
log("       positive monotone traces vs sign-changing targets -- structurally excluded)")
log("  C3 ladder certificate as Habiro q-object    : MISS (finite 130-term support; first ratio")
log("       mismatch at term 1; RR theta classes = order-80 characters, provably absent")
log("       since the banked period's 2-part is 8; 0/130 support frequencies hit an RR class)")
log("  C4 eta-quotient / RR recognition            : *** MATCH *** for the FULL 2hat doublet:")
log("       Y^(5)_2hat = eta^{48/5} * (F1, F2) = q^{2/5}(q;q)^9 * (N1, q^{1/5} N2),")
log("       N1, N2 = the Rogers-Ramanujan numerators; verified 100 (log-solver) +")
log("       301 (independent product identity) coefficients per component.")
if p13_hit:
    log("       AND the 2hat' doublet = eta^{24/5} * P13(F1,F2) (coefficients above),")
    log("       301 coefficients verified per component -- BOTH doublets are eta-power")
    log("       times F-polynomials; the recognition leg is complete.")
else:
    log("       The 2hat' doublet resists the single natural eta^{24/5}*P13 ansatz")
    log("       (failure index above) -- its recognition stays open.")
log("       The pure {eta(tau),eta(5tau)} menu stays excluded (mod-5 obstruction).")
log("")
log("  THE ANSWER TO L108's QUESTION, two-sided:")
log("  (i)  RECOGNITION LEG -- FOUND: the weight-5 doublet streams ARE Rogers-")
log("       Ramanujan objects.  The 2hat doublet is literally (N1, N2) times the")
log("       grading-free scalar q^{r/5}(q;q)^9: the banked target factors through")
log("       the RR numerators exactly (301 coefficients, product level), and")
log("       comp2/comp1 IS the Rogers-Ramanujan continued fraction R(q).")
log("  (ii) GENERATION LEG -- STILL MISSING: no banked tower object (B205 q-tower,")
log("       word-length filtration, ladder support) generates these streams; the")
log("       ladder route to N1/N2 is exactly excluded at character order 80 vs the")
log("       banked period 2-part cap 8.  The missing ingredient sharpens to: a")
log("       framework object whose graded trace produces the RR numerators N1, N2")
log("       (equivalently (q;q)G(q), (q;q)H(q)) -- the Andrews-Gordon/Lee-Yang door.")
log("")
log("  total runtime %.1fs" % (time.time() - T0))

with open(os.path.join(_HERE, "cellG_output.txt"), "w") as fh:
    fh.write("\n".join(OUT) + "\n")

# machine-readable verdict table
verdict_json = {
    "C1": {"verdict": "MISS", "first_mismatch": 1,
           "subcandidates": ["z=1+q/z Catalan", "MGO [phi]_q", "q-Chebyshev (finite)"]},
    "C2": {"verdict": "MISS", "first_mismatch": 1,
           "subcandidates": ["sum tr(R^aL^b) x^{a+b}", "tr((R+L)^n)=3^n+1", "tr((RL)^n)=Lucas"]},
    "C3": {"verdict": "MISS", "first_ratio_mismatch_term": 1,
           "structural": "RR theta classes are order-80 characters; period 2-part = 8; 0/130 support hits"},
    "C4": {"verdict": "MATCH",
           "identity": {"2hat.comp1": "q^{2/5} N1 (q;q)^9 = F1 eta^{48/5}",
                        "2hat.comp2": "q^{3/5} N2 (q;q)^9 = F2 eta^{48/5}"},
           "coefficients_verified": 301,
           "p13_2hatprime": p13_hits if p13_hit else "MISS (ansatz failed)",
           "eta_menu_pure": "mod-5 exponent obstruction (0 solutions, a+b=10 exhaustive)",
           "solver_rejections": [{"target": t, "menu": m, "fail_n": n} for t, m, n in miss4],
           "solver_matches": [{"target": t, "menu": m, "x": x} for t, m, x in match4]},
    "overall": ("RECOGNITION LEG FOUND: the 2hat doublet = eta^{48/5} (F1, F2) = the "
                "Rogers-Ramanujan numerators times q^{r/5}(q;q)^9; GENERATION LEG still "
                "missing (C1-C3 dead, exact miss table)"),
}
with open(os.path.join(_HERE, "cellG_verdict_table.json"), "w") as fh:
    json.dump(verdict_json, fh, indent=1)
print("wrote cellG_output.txt + cellG_verdict_table.json")
