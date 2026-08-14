#!/usr/bin/env python3
"""
W2B — THE GENERAL-FAMILY HEARING LANDSCAPE
Derivation Campaign, seat cc3, wave-2 addendum cell W2b.

Reads (read-only, cited): PREREG_DC.md (W2b spec), SYNTHESIS_DB.md section 4
(the sealed question), the repo's banked landscape machinery
  origin-axiom/frontier/B664_metallic_landscape/{FINDINGS.md,landscape_verify.py,
  METALLIC_LANDSCAPE_HANDOFF.md}
and the SU(3)_2 modular-data source it consumes,
  origin-axiom/frontier/B238_su32_levelrank/su32_wrt.py  (su3_data(k), wrt_trace)
plus the cross-adjudication that first computed R^2L^2 = "the silver bundle"
off the metallic slice:
  origin-axiom/frontier/B665_landscape_reconciliation/FINDINGS.md
  seat-work/LANDSCAPE_ADJUDICATION_CC2.md
  seat-work/anatomy/TRACK_H_ADJUDICATION_CC2.md

THE BANKED CONVENTION (hard gate: must reproduce B664's slice values exactly).
B238's su32_wrt.wrt_trace docstring is the ground truth:
    "Z = tr(rho(word)) with R=T, L=S^{-1}T^{-1}S"
and B664's landscape_verify.py builds X = inv(S) @ inv(T) @ S, then evaluates
the metallic word R^{n-2}L as W = T^(n-2) @ X (i.e. word letters map to
matrices in LEFT-TO-RIGHT order: w = c1 c2 ... ck -> M(c1)@M(c2)@...@M(ck),
with c='R' -> T, c='L' -> S^{-1}T^{-1}S), and
    tr_odd(w) = trace(odd.T @ M(w) @ odd)
where `odd` is the (dim, 2) matrix of theta-odd unit vectors (1/sqrt2)(e_a-e_b)
for each of the two SU(3)_2 conjugate-weight pairs (a,b) with (b,a) > (a,b).
This script reuses that convention exactly (verified below against B664's own
numbers, not merely asserted) and generalizes it from the single-L metallic
slice to ALL 745 primitive necklace classes.

THE VALUE RING. All SU(3)_2 modular data at level k=2 (kappa = k+3 = 5) has:
  - T-matrix phases exp(2 pi i * m/15) for integer m (proved below: phase*15
    is always an integer, from the Kac-Peterson formula with kappa=5);
  - S-matrix (Weyl/Kac-Peterson alternating sum over 3! permutations) entries
    that are integer combinations of 15th roots of unity (same denominator-15
    argument applied to the su(3) inner product mod kappa=5).
So R_full = T and L_full = S^{-1} T^{-1} S both live in Q(zeta_15) (degree
phi(15) = 8 over Q); crucially the S-matrix's usual real normalization
constant (dividing by sqrt(sum of column moduli^2)) CANCELS EXACTLY in the
similarity transform S^{-1} T^{-1} S, so the UNNORMALIZED Weyl-sum matrix S0
may be used directly with no loss of exactness (verified: [P,S0-dependent
L_full]=0, see below). Hence every word matrix M(w), and tr_odd(w) itself,
is an EXACT element of the 15th cyclotomic field Q(zeta_15), represented
here as an 8-tuple of exact Fractions in the power basis {1,z,...,z^7}
reduced modulo the 15th cyclotomic polynomial
    Phi_15(x) = x^8 - x^7 + x^5 - x^4 + x^3 - x + 1.
|tr_odd|^2 and reality (Im(tr_odd)=0) are decided by EXACT field arithmetic
(complex conjugation z -> z^14, an exact ring automorphism of this
representation) -- no floating-point epsilon anywhere in a verdict path.
sqrt(5) (needed to express values as B664's a+b*sqrt5 golden forms) embeds
exactly via the classical Gauss sum sqrt5 = z^3 - z^6 - z^9 + z^12 (z_5 :=
zeta_15^3 is a primitive 5th root; sqrt5 = sum_a (a|5) zeta_5^a).

THE CROSS-COLUMNS (trace, disc, amphichirality) reuse the W0a convention
EXACTLY (seat-work/derivation_campaign/w0a_criteria/w0a_criteria.py):
R=[[1,1],[0,1]], L=[[1,0],[1,1]], word matrix = left-to-right product,
canonical class rep = lexicographically minimal rotation ('L'<'R'),
amphichiral iff canonical(swap(reverse(w))) == w. The 745-class enumeration
(primitive, mixed-letter, cyclic necklaces of length 2..12) is regenerated
here independently with the identical algorithm and cross-checked against
the banked w0a_table.json count.

NOTE ON tr_odd AND CYCLIC ROTATION: tr_odd(w) = tr(P . M(w)) where P =
odd@odd^T is the (rank-2) theta-odd projector on the full 6-dim SU(3)_2
carrier space. Proved here by direct exact computation (not assumed):
[P, R_full] = 0 and [P, L_full] = 0 exactly. Consequently tr_odd is a
genuine class function on necklaces (invariant under cyclic rotation of the
word), exactly like the ordinary trace -- so the single canonical
representative per necklace class is unambiguous for tr_odd too, no
representative-choice artifact.

Run: python3 -u w2b_landscape.py
"""
import itertools
import json
import sys
import time
from fractions import Fraction as Fr

MIN_LEN = 2
MAX_LEN = 12

# ============================================================================
# PART 0 -- exact Q(zeta_15) field arithmetic
# ============================================================================
# Phi_15(x) = x^8 - x^7 + x^5 - x^4 + x^3 - x + 1  =>  x^8 = x^7-x^5+x^4-x^3+x-1
REDUCE8 = [-1, 1, 0, -1, 1, -1, 0, 1]  # coefficients of 1,z,...,z^7 for z^8


def _mul_by_z_int(v):
    shifted = [0] + list(v[:7])
    carry = v[7]
    return [shifted[i] + carry * REDUCE8[i] for i in range(8)]


REDUCE = {8: REDUCE8}
_cur = REDUCE8
for _k in range(9, 15):
    _cur = _mul_by_z_int(_cur)
    REDUCE[_k] = _cur


def cyc_zero():
    return [Fr(0)] * 8


def monomial(k):
    """Exact vector for zeta_15^k, reduced mod Phi_15."""
    k = k % 15
    if k < 8:
        v = [Fr(0)] * 8
        v[k] = Fr(1)
        return v
    return [Fr(x) for x in REDUCE[k]]


ONE = monomial(0)


def cyc_add(a, b):
    return [a[i] + b[i] for i in range(8)]


def cyc_sub(a, b):
    return [a[i] - b[i] for i in range(8)]


def cyc_scale(a, s):
    return [x * s for x in a]


def cyc_eq(a, b):
    return all(a[i] == b[i] for i in range(8))


def cyc_is_zero(a):
    return all(x == 0 for x in a)


def cyc_mul(a, b):
    raw = [Fr(0)] * 15
    for i in range(8):
        ai = a[i]
        if ai == 0:
            continue
        for j in range(8):
            bj = b[j]
            if bj == 0:
                continue
            raw[i + j] += ai * bj
    result = list(raw[:8])
    for k in range(8, 15):
        ck = raw[k]
        if ck != 0:
            rk = REDUCE[k]
            for i in range(8):
                if rk[i] != 0:
                    result[i] += ck * rk[i]
    return result


CONJ_BASIS = [monomial((-i) % 15) for i in range(8)]


def cyc_conj(a):
    """Complex conjugation z -> z^{-1}, an exact ring automorphism."""
    res = cyc_zero()
    for i in range(8):
        if a[i] != 0:
            res = cyc_add(res, cyc_scale(CONJ_BASIS[i], a[i]))
    return res


# ---- polynomial extended-gcd over Q (for field inversion mod Phi_15) ----
def _poly_trim(p):
    p = list(p)
    while p and p[-1] == 0:
        p.pop()
    return p


def _poly_divmod(a, b):
    a = _poly_trim(a)
    b = _poly_trim(b)
    q = [Fr(0)] * max(1, len(a) - len(b) + 1)
    r = list(a)
    while _poly_trim(r) and len(_poly_trim(r)) >= len(b):
        r = _poly_trim(r)
        deg_r, deg_b = len(r) - 1, len(b) - 1
        coeff = r[-1] / b[-1]
        shift = deg_r - deg_b
        q[shift] += coeff
        for i in range(len(b)):
            r[shift + i] -= coeff * b[i]
        r = _poly_trim(r)
    return _poly_trim(q), r


def _poly_sub(a, b):
    n = max(len(a), len(b))
    a = a + [Fr(0)] * (n - len(a))
    b = b + [Fr(0)] * (n - len(b))
    return _poly_trim([a[i] - b[i] for i in range(n)])


def _poly_mul(a, b):
    a, b = _poly_trim(a), _poly_trim(b)
    if not a or not b:
        return []
    res = [Fr(0)] * (len(a) + len(b) - 1)
    for i, ai in enumerate(a):
        if ai == 0:
            continue
        for j, bj in enumerate(b):
            if bj != 0:
                res[i + j] += ai * bj
    return _poly_trim(res)


def _poly_ext_gcd(a, b):
    old_r, r = _poly_trim(a), _poly_trim(b)
    old_s, s = [Fr(1)], [Fr(0)]
    while _poly_trim(r):
        q, rem = _poly_divmod(old_r, r)
        old_r, r = r, rem
        old_s, s = s, _poly_sub(old_s, _poly_mul(q, s))
    return _poly_trim(old_r), _poly_trim(old_s)


PHI15 = [Fr(1), Fr(-1), Fr(0), Fr(1), Fr(-1), Fr(1), Fr(0), Fr(-1), Fr(1)]


def cyc_inv(a):
    a = _poly_trim(a)
    if not a:
        raise ZeroDivisionError("cyc_inv of zero")
    g, x = _poly_ext_gcd(a, PHI15)
    assert len(g) == 1, f"Phi_15 irreducibility violated?! gcd degree {len(g)-1}"
    c = g[0]
    x = [xi / c for xi in x]
    _, r = _poly_divmod(x, PHI15)
    r = r + [Fr(0)] * (8 - len(r))
    return r[:8]


def cyc_eval(v, zc):
    return sum(v[i] * (zc ** i) for i in range(8))


import cmath
ZC64 = cmath.exp(2j * cmath.pi / 15)


def numeric(v):
    return cyc_eval(v, ZC64)


# sqrt5 via the classical Gauss sum: zeta_5 = zeta_15^3; sqrt5 = z5-z5^2-z5^3+z5^4
SQRT5 = cyc_add(cyc_sub(monomial(3), monomial(6)), cyc_sub(monomial(12), monomial(9)))
assert abs(numeric(SQRT5) - 5 ** 0.5) < 1e-9
PHI_GOLD = cyc_scale(cyc_add(ONE, SQRT5), Fr(1, 2))          # (1+sqrt5)/2
assert abs(numeric(PHI_GOLD) - (1 + 5 ** 0.5) / 2) < 1e-9
INV_PHI2 = cyc_scale(cyc_sub(cyc_scale(ONE, Fr(3)), SQRT5), Fr(1, 2))  # (3-sqrt5)/2 = 1/phi^2
PHI2 = cyc_scale(cyc_add(cyc_scale(ONE, Fr(3)), SQRT5), Fr(1, 2))      # (3+sqrt5)/2 = phi^2
FOUR = cyc_scale(ONE, Fr(4))
ZEROV = cyc_zero()

KNOWN_ABS2 = [
    ("0", ZEROV, 0.0),
    ("1", ONE, 1.0),
    ("(3-sqrt5)/2 = 1/phi^2", INV_PHI2, (3 - 5 ** 0.5) / 2),
    ("1 [loud]", ONE, 1.0),
    ("(3+sqrt5)/2 = phi^2", PHI2, (3 + 5 ** 0.5) / 2),
    ("4", FOUR, 4.0),
]


def closed_form_label(abs2):
    for label, val, _ in KNOWN_ABS2:
        if cyc_eq(abs2, val):
            return label
    # generic Q(sqrt5) fit: abs2 = p*1 + q*sqrt5 ?
    # solve using coordinates 0 and 3 (ONE has support only at 0; SQRT5 has
    # nonzero coordinate at index 3), then verify all 8 coordinates.
    # ONE = (1,0,0,0,0,0,0,0); SQRT5 = (s0,s1,...,s7)
    s = SQRT5
    if s[3] != 0:
        # abs2[3] = q*s[3]  (ONE contributes 0 at index3)
        q = abs2[3] / s[3]
        p = abs2[0] - q * s[0]
        cand = cyc_add(cyc_scale(ONE, p), cyc_scale(s, q))
        if cyc_eq(cand, abs2):
            sign = '+' if q >= 0 else '-'
            return f"{p} {sign} {abs(q)}*sqrt5"
    return None


# ============================================================================
# PART 1 -- SU(3)_2 modular data (Kac-Peterson), EXACT, k=2
# ============================================================================
def build_su3_2_exact():
    weights = [(a, b) for a in range(3) for b in range(3 - a)]
    n = len(weights)

    def Lvec(w):
        return (w[0] + w[1] + 2, w[1] + 1, 0)

    def ip_exact(u, v):
        dot = u[0] * v[0] + u[1] * v[1] + u[2] * v[2]
        su, sv = sum(u), sum(v)
        return Fr(dot) - Fr(su * sv, 3)

    perms = list(itertools.permutations(range(3)))

    def sgn(p):
        s = 1
        for i in range(3):
            for j in range(i + 1, 3):
                if p[i] > p[j]:
                    s = -s
        return s

    # S0: unnormalized Weyl/Kac-Peterson sum (normalization cancels in
    # S^{-1} T^{-1} S, proved via the [P,L_full]=0 check below, so we skip it)
    S0 = [[None] * n for _ in range(n)]
    for i, wl in enumerate(weights):
        Ll = Lvec(wl)
        for j, wm in enumerate(weights):
            Lm = Lvec(wm)
            acc = cyc_zero()
            for p in perms:
                Llp = tuple(Ll[p[t]] for t in range(3))
                val = ip_exact(Llp, Lm)
                phase = val / 5  # kappa = 5
                frac15 = phase * 15
                assert frac15.denominator == 1, "denominator-15 claim violated"
                expo = (-int(frac15)) % 15
                acc = cyc_add(acc, cyc_scale(monomial(expo), sgn(p)))
            S0[i][j] = acc

    Texp = []
    for (a, b) in weights:
        val = a * a + a * b + b * b + 3 * a + 3 * b - 2
        Texp.append(val % 15)
    T = [[ONE if i == j else ZEROV for j in range(n)] for i in range(n)]
    for i in range(n):
        T[i][i] = monomial(Texp[i])
    Tinv = [[ONE if i == j else ZEROV for j in range(n)] for i in range(n)]
    for i in range(n):
        Tinv[i][i] = monomial((-Texp[i]) % 15)

    return weights, S0, T, Tinv, Texp


def mat_mul(A, B):
    m, k, p = len(A), len(A[0]), len(B[0])
    C = [[cyc_zero() for _ in range(p)] for _ in range(m)]
    for i in range(m):
        Ai = A[i]
        for t in range(k):
            at = Ai[t]
            if cyc_is_zero(at):
                continue
            Bt = B[t]
            for j in range(p):
                if not cyc_is_zero(Bt[j]):
                    C[i][j] = cyc_add(C[i][j], cyc_mul(at, Bt[j]))
    return C


def mat_inv(A):
    m = len(A)
    M = [list(A[i]) + [ONE if j == i else ZEROV for j in range(m)] for i in range(m)]
    for col in range(m):
        piv = next((r for r in range(col, m) if not cyc_is_zero(M[r][col])), None)
        assert piv is not None, "singular matrix"
        M[col], M[piv] = M[piv], M[col]
        invp = cyc_inv(M[col][col])
        M[col] = [cyc_mul(x, invp) for x in M[col]]
        for r in range(m):
            if r != col and not cyc_is_zero(M[r][col]):
                factor = M[r][col]
                M[r] = [cyc_sub(M[r][j], cyc_mul(factor, M[col][j])) for j in range(2 * m)]
    return [row[m:] for row in M]


# ============================================================================
# PART 2 -- W0a-convention integer arithmetic (trace/disc/amphichiral)
# reused verbatim in spirit from
# seat-work/derivation_campaign/w0a_criteria/w0a_criteria.py
# ============================================================================
RMAT = ((1, 1), (0, 1))
LMAT = ((1, 0), (1, 1))
IDENTITY = ((1, 0), (0, 1))
SWAP_TABLE = str.maketrans('RL', 'LR')


def matmul2(A, B):
    return (
        (A[0][0] * B[0][0] + A[0][1] * B[1][0], A[0][0] * B[0][1] + A[0][1] * B[1][1]),
        (A[1][0] * B[0][0] + A[1][1] * B[1][0], A[1][0] * B[0][1] + A[1][1] * B[1][1]),
    )


def word_matrix2(word):
    M = IDENTITY
    for ch in word:
        M = matmul2(M, RMAT if ch == 'R' else LMAT)
    return M


def canonical(word):
    n = len(word)
    return min(word[i:] + word[:i] for i in range(n))


def minimal_period(word):
    n = len(word)
    for d in range(1, n + 1):
        if n % d == 0 and word[:d] * (n // d) == word:
            return d
    return n


def is_prime_exact(n):
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0:
        return False
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True


def factorize(n):
    factors = {}
    m, d = n, 2
    while d * d <= m:
        while m % d == 0:
            factors[d] = factors.get(d, 0) + 1
            m //= d
        d += 1
    if m > 1:
        factors[m] = factors.get(m, 0) + 1
    return factors


def enumerate_necklaces(n):
    seen = set()
    for tup in itertools.product('RL', repeat=n):
        seen.add(canonical(''.join(tup)))
    return seen


# ============================================================================
# MAIN
# ============================================================================
def main():
    t_start = time.time()
    print("[W2b] THE GENERAL-FAMILY HEARING LANDSCAPE -- start", flush=True)

    # ---- PART 1: build SU(3)_2 exact modular data, R_full/L_full, theta-odd P
    print("[W2b] building SU(3)_2 exact modular data (Q(zeta_15))...", flush=True)
    weights, S0, T, Tinv, Texp = build_su3_2_exact()
    n6 = len(weights)
    print(f"[W2b]   weights: {weights}  T-exponents mod 15: {Texp}", flush=True)

    t0 = time.time()
    S0inv = mat_inv(S0)
    prod = mat_mul(S0, S0inv)
    assert all(cyc_eq(prod[i][j], ONE if i == j else ZEROV) for i in range(n6) for j in range(n6)), \
        "S0 * S0^{-1} != I exactly -- GATE FAILURE"
    print(f"[W2b]   S0^-1 built and verified exact in {time.time()-t0:.3f}s", flush=True)

    R_full = T
    L_full = mat_mul(mat_mul(S0inv, Tinv), S0)
    print(f"[W2b]   R_full = T, L_full = S0^-1 T^-1 S0 built ({time.time()-t0:.3f}s total)", flush=True)

    # cross-check against the banked numeric B238 build (independent gate)
    try:
        import importlib.util, os
        import numpy as np
        ROOT = "[seat-machine-path]"
        spec = importlib.util.spec_from_file_location(
            "b238", os.path.join(ROOT, "frontier", "B238_su32_levelrank", "su32_wrt.py"))
        b238 = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(b238)
        weights_num, S_num, T_num, c_num = b238.su3_data(2)
        assert weights == weights_num, "weight ordering mismatch vs banked B238 su3_data(2)"
        L_full_num = np.linalg.inv(S_num) @ np.linalg.inv(T_num) @ S_num
        L_full_eval = np.array([[complex(numeric(L_full[i][j])) for j in range(n6)] for i in range(n6)])
        max_err = float(np.max(np.abs(L_full_eval - L_full_num)))
        print(f"[W2b]   cross-check vs banked B238 numeric build: "
              f"max|L_full_exact - L_full_numeric| = {max_err:.3e}", flush=True)
        assert max_err < 1e-8, "exact build disagrees with banked B238 numeric build -- HARD GATE FAILURE"
    except Exception as e:
        print(f"[W2b]   WARNING: could not cross-check against banked B238 numeric build: {e}", flush=True)
        raise

    # theta-odd conjugate pairs (identical index logic to landscape_verify.py)
    prs = [(i, weights.index((wt[1], wt[0]))) for i, wt in enumerate(weights) if (wt[1], wt[0]) > wt]
    assert prs == [(1, 3), (2, 5)], f"unexpected theta-odd pairs: {prs}"
    print(f"[W2b]   theta-odd conjugate pairs: {prs}", flush=True)

    def tr_odd_exact(M):
        acc = cyc_zero()
        for (a, b) in prs:
            acc = cyc_add(acc, M[a][a])
            acc = cyc_add(acc, M[b][b])
            acc = cyc_sub(acc, M[a][b])
            acc = cyc_sub(acc, M[b][a])
        return cyc_scale(acc, Fr(1, 2))

    def word_matrix_exact(word):
        M = None
        for ch in word:
            letter = R_full if ch == 'R' else L_full
            M = letter if M is None else mat_mul(M, letter)
        return M

    # PROVE tr_odd is a class function (rotation invariance), not merely assume:
    half = Fr(1, 2)
    P = [[cyc_zero() for _ in range(n6)] for _ in range(n6)]
    for (a, b) in prs:
        P[a][a] = cyc_add(P[a][a], cyc_scale(ONE, half))
        P[b][b] = cyc_add(P[b][b], cyc_scale(ONE, half))
        P[a][b] = cyc_sub(P[a][b], cyc_scale(ONE, half))
        P[b][a] = cyc_sub(P[b][a], cyc_scale(ONE, half))
    comm_L = all(cyc_eq(mat_mul(P, L_full)[i][j], mat_mul(L_full, P)[i][j]) for i in range(n6) for j in range(n6))
    comm_R = all(cyc_eq(mat_mul(P, R_full)[i][j], mat_mul(R_full, P)[i][j]) for i in range(n6) for j in range(n6))
    print(f"[W2b]   [P,R_full]=0 exactly: {comm_R};  [P,L_full]=0 exactly: {comm_L}  "
          f"=> tr_odd is EXACTLY cyclic-rotation-invariant (class function on necklaces)", flush=True)
    assert comm_L and comm_R, "theta-odd projector does not commute with generators -- tr_odd would NOT be a class function; representative choice would matter -- STOP"

    # ---- PART 2: regenerate the 745-class enumeration ----
    print("[W2b] enumerating primitive cyclic R/L necklaces, length 2..12...", flush=True)
    hyperbolic_words = []
    counts_per_length = {}
    for L in range(MIN_LEN, MAX_LEN + 1):
        necklaces = enumerate_necklaces(L)
        cnt = 0
        for w in sorted(necklaces):
            if len(set(w)) == 1:
                continue  # parabolic (all-R / all-L)
            if minimal_period(w) != L:
                continue  # not primitive
            hyperbolic_words.append(w)
            cnt += 1
        counts_per_length[L] = cnt
        print(f"[W2b]   length {L:2d}: {cnt} primitive hyperbolic classes", flush=True)

    total = len(hyperbolic_words)
    print(f"[W2b] TOTAL primitive hyperbolic necklace classes: {total}", flush=True)
    assert total == 745, f"HARD GATE FAILURE: expected 745 classes, got {total}"
    print("[W2b] enumeration count GATE: PASSED (745)", flush=True)

    # cross-check against banked w0a_table.json if present
    try:
        with open("w0a_table.json") as f:
            w0a = json.load(f)
        w0a_words = set(c["word"] for c in w0a["hyperbolic_classes"])
        my_words = set(hyperbolic_words)
        print(f"[W2b] cross-check vs banked w0a_table.json: identical word-set: {w0a_words == my_words}", flush=True)
        assert w0a_words == my_words, "enumeration mismatch vs banked W0a table"
    except FileNotFoundError:
        print("[W2b] (banked w0a_table.json not found; skipping cross-check)", flush=True)

    # ---- PART 3: per-class computation ----
    print("[W2b] computing per-class SU(3)_2 tr_odd (exact) + W0a cross-columns for all 745 classes...", flush=True)
    rows = []
    t_sweep = time.time()
    for idx, w in enumerate(hyperbolic_words):
        L = len(w)
        # W0a cross-columns (exact integer arithmetic)
        M2 = word_matrix2(w)
        tr = M2[0][0] + M2[1][1]
        disc = tr * tr - 4
        assert disc > 0
        fac = factorize(disc)
        prime_conductor = is_prime_exact(disc)
        det_AminusI = 2 - tr
        unit_det = (abs(det_AminusI) == 1)
        rev = w[::-1]
        swapped = w.translate(SWAP_TABLE)
        canon_revswap = canonical(rev.translate(SWAP_TABLE))
        amphichiral = (canon_revswap == w)

        # SU(3)_2 exact tr_odd
        M6 = word_matrix_exact(w)
        tro = tr_odd_exact(M6)
        abs2 = cyc_mul(tro, cyc_conj(tro))
        is_real = cyc_eq(tro, cyc_conj(tro))
        tro_num = numeric(tro)
        abs2_num = numeric(abs2).real

        rows.append({
            "word": w,
            "length": L,
            "trace": tr,
            "disc": disc,
            "disc_factorization": {str(p): e for p, e in sorted(fac.items())},
            "prime_conductor": prime_conductor,
            "det_A_minus_I": det_AminusI,
            "unit_det": unit_det,
            "amphichiral": amphichiral,
            "tr_odd_zeta15_coeffs": [[c.numerator, c.denominator] for c in tro],
            "tr_odd_numeric_re": tro_num.real,
            "tr_odd_numeric_im": tro_num.imag,
            "abs_tr_odd_sq_zeta15_coeffs": [[c.numerator, c.denominator] for c in abs2],
            "abs_tr_odd_sq_numeric": abs2_num,
            "abs_tr_odd_sq_closed_form": closed_form_label(abs2),
            "im_tr_odd_is_zero_exact": is_real,
        })
        if (idx + 1) % 100 == 0:
            print(f"[W2b]   {idx+1}/{total} classes done ({time.time()-t_sweep:.1f}s elapsed)", flush=True)

    print(f"[W2b] full sweep done in {time.time()-t_sweep:.1f}s", flush=True)

    # ============================================================================
    # GATES
    # ============================================================================
    print("\n[W2b] === HARD GATE (a): metallic slice n=3..14 (R^{n-2}L) ===", flush=True)
    by_word = {r["word"]: r for r in rows}
    # words R^{n-2}L are not necessarily their own canonical rep, but tr_odd is
    # a class function (proved above), so evaluating any representative
    # (including directly, bypassing the table) is valid and matches the table
    # via the canonical rep of the same necklace.
    gate_a_ok = True
    metallic_report = []
    for nn in range(3, 15):
        w = 'R' * (nn - 2) + 'L'
        M6 = word_matrix_exact(w)
        tro = tr_odd_exact(M6)
        abs2 = cyc_mul(tro, cyc_conj(tro))
        is_real = cyc_eq(tro, cyc_conj(tro))
        label = closed_form_label(abs2)
        three_valued = cyc_eq(abs2, ZEROV) or cyc_eq(abs2, ONE) or cyc_eq(abs2, INV_PHI2)
        gate_a_ok = gate_a_ok and three_valued
        metallic_report.append((nn, w, numeric(tro), label, three_valued, is_real))
        print(f"[W2b]   n={nn:2d} {w:12s} tr_odd~{numeric(tro):+.6f}  "
              f"|tr_odd|^2={label}  in{{0,1,1/phi^2}}:{three_valued}  real_exact:{is_real}", flush=True)
    print(f"[W2b] GATE (a) [metallic slice reproduces B664 three-value closed form]: "
          f"{'PASSED' if gate_a_ok else 'FAILED'}", flush=True)
    assert gate_a_ok, "GATE (a) FAILED -- metallic slice does not reproduce B664's {0,1/phi,1} pattern"

    print("\n[W2b] === HARD GATE (b): silver R^2L^2 = RRLL ===", flush=True)
    M6 = word_matrix_exact("RRLL")
    tro_silver = tr_odd_exact(M6)
    silver_real = cyc_eq(tro_silver, cyc_conj(tro_silver))
    silver_is_one = cyc_eq(tro_silver, ONE)
    print(f"[W2b]   tr_odd(RRLL) = {numeric(tro_silver):+.10f}  == 1 exactly: {silver_is_one}  "
          f"real exactly: {silver_real}", flush=True)
    print("[W2b]   banked citation: seat-work/LANDSCAPE_ADJUDICATION_CC2.md line 18 and "
          "origin-axiom/frontier/B665_landscape_reconciliation/FINDINGS.md "
          "('RRLL and RRRLLL have tr_odd = 1.0 exactly REAL')", flush=True)
    gate_b_ok = silver_is_one and silver_real
    print(f"[W2b] GATE (b) [silver R^2L^2 reproduces banked tr_odd=1, real]: "
          f"{'PASSED' if gate_b_ok else 'FAILED'}", flush=True)
    assert gate_b_ok, "GATE (b) FAILED -- silver R^2L^2 does not reproduce banked tr_odd=1"

    # ============================================================================
    # THE SEALED QUESTION
    # ============================================================================
    print("\n[W2b] === THE SEALED QUESTION ===", flush=True)

    # (i) deaf: tr_odd == 0 exactly
    deaf_rows = [r for r in rows if all(c[0] == 0 for c in r["tr_odd_zeta15_coeffs"])]
    print(f"[W2b] (i) DEAF (tr_odd == 0 exactly): {len(deaf_rows)} classes", flush=True)
    print(f"[W2b]     words: {sorted(r['word'] for r in deaf_rows)}", flush=True)

    # distinct exact |tr_odd|^2 values across the whole family (dedupe by exact equality)
    distinct_abs2 = []  # list of (repr_vector, [rows])
    for r in rows:
        v = [Fr(a, b) for a, b in r["abs_tr_odd_sq_zeta15_coeffs"]]
        placed = False
        for entry in distinct_abs2:
            if cyc_eq(entry["vec"], v):
                entry["rows"].append(r)
                placed = True
                break
        if not placed:
            distinct_abs2.append({"vec": v, "rows": [r]})

    for entry in distinct_abs2:
        entry["numeric"] = numeric(entry["vec"]).real
        entry["label"] = closed_form_label(entry["vec"])
    distinct_abs2.sort(key=lambda e: e["numeric"])

    print(f"\n[W2b] DISTINCT |tr_odd|^2 values family-wide: {len(distinct_abs2)}", flush=True)
    for entry in distinct_abs2:
        print(f"[W2b]     |tr_odd|^2 = {entry['numeric']:.10f}  "
              f"(closed form: {entry['label']})  count={len(entry['rows'])}", flush=True)

    nonzero_entries = [e for e in distinct_abs2 if e["numeric"] > 1e-12]
    min_entry = min(nonzero_entries, key=lambda e: e["numeric"])
    # safety margin check against near-ties
    sorted_nz = sorted(nonzero_entries, key=lambda e: e["numeric"])
    if len(sorted_nz) > 1:
        gap = sorted_nz[1]["numeric"] - sorted_nz[0]["numeric"]
        print(f"[W2b]   (safety) gap between smallest and second-smallest nonzero |tr_odd|^2: {gap:.3e}", flush=True)
        assert gap > 1e-6, "near-tie at the minimum -- exact dedup may be masking a distinct close value"

    min_val = min_entry["numeric"]
    min_label = min_entry["label"]
    class_ii = min_entry["rows"]  # (ii) minimal nonzero |tr_odd|
    print(f"\n[W2b] (ii) MINIMAL NONZERO |tr_odd|^2 = {min_val:.10f}  (closed form: {min_label})", flush=True)
    print(f"[W2b]     attained by {len(class_ii)} classes: {sorted(r['word'] for r in class_ii)}", flush=True)

    class_iii = [r for r in class_ii if r["im_tr_odd_is_zero_exact"]]
    print(f"\n[W2b] (iii) MINIMAL NONZERO |tr_odd| AND Im(tr_odd)=0 EXACTLY: "
          f"{len(class_iii)} classes", flush=True)
    print(f"[W2b]     words: {sorted(r['word'] for r in class_iii)}", flush=True)

    rl_in_iii = any(r["word"] in ("RL", "LR") for r in class_iii)
    rl_unique = (len(class_iii) == 1) and rl_in_iii
    print(f"\n[W2b] IS RL THE UNIQUE CLASS IN (iii)?  {'YES' if rl_unique else 'NO'}", flush=True)
    if not rl_unique:
        print("[W2b] !!!! SEALED-QUESTION VERDICT: RL IS NOT UNIQUE (or is absent) !!!!", flush=True)
        print(f"[W2b] !!!! full (iii) list: {sorted(r['word'] for r in class_iii)}", flush=True)
        for r in class_iii:
            print(f"[W2b]      {r['word']:12s} trace={r['trace']:4d} disc={r['disc']:5d} "
                  f"amphichiral={r['amphichiral']} unit_det={r['unit_det']} "
                  f"prime_conductor={r['prime_conductor']}", flush=True)

    # cross-columns for (ii) and (iii) explicitly (task item 4)
    print("\n[W2b] CROSS-COLUMNS for (ii) [minimal nonzero |tr_odd|]:", flush=True)
    for r in sorted(class_ii, key=lambda r: (r["length"], r["word"])):
        print(f"[W2b]   {r['word']:12s} len={r['length']:2d} trace={r['trace']:4d} disc={r['disc']:5d} "
              f"amphichiral={r['amphichiral']} unit_det={r['unit_det']} prime_conductor={r['prime_conductor']} "
              f"Im=0:{r['im_tr_odd_is_zero_exact']}", flush=True)

    total_time = time.time() - t_start
    print(f"\n[W2b] TOTAL RUNTIME: {total_time:.1f}s", flush=True)

    # ============================================================================
    # WRITE DELIVERABLES
    # ============================================================================
    out_dir = "w2b_landscape"

    output = {
        "meta": {
            "cell": "W2b",
            "campaign": "derivation_campaign",
            "seat": "cc3",
            "word_length_range": [MIN_LEN, MAX_LEN],
            "total_classes": total,
            "value_ring": "Q(zeta_15), the 15th cyclotomic field, degree 8 over Q; "
                           "coefficients given exactly in the power basis {1,z,...,z^7}, "
                           "z=exp(2 pi i/15), reduced mod Phi_15(x)=x^8-x^7+x^5-x^4+x^3-x+1",
            "convention": "R=T, L=S^{-1}T^{-1}S (banked B238/B664 convention, verified against "
                           "the banked numeric build); word w1w2...wk -> M(w1)@M(w2)@...@M(wk); "
                           "tr_odd(w) = trace(odd^T @ M(w) @ odd) over the SU(3)_2 theta-odd "
                           "2-dim conjugate-pair subspace; proved here to be a class function "
                           "(cyclic-rotation invariant, since [P,R_full]=[P,L_full]=0 exactly).",
            "gate_a_metallic_slice_passed": gate_a_ok,
            "gate_b_silver_R2L2_passed": gate_b_ok,
        },
        "classes": rows,
        "distinct_abs_tr_odd_sq_values": [
            {"numeric": e["numeric"], "closed_form": e["label"], "count": len(e["rows"]),
             "words": sorted(r["word"] for r in e["rows"])}
            for e in distinct_abs2
        ],
        "sealed_question": {
            "deaf_count": len(deaf_rows),
            "deaf_words": sorted(r["word"] for r in deaf_rows),
            "minimal_nonzero_abs_tr_odd_sq": min_val,
            "minimal_nonzero_closed_form": min_label,
            "class_ii_words": sorted(r["word"] for r in class_ii),
            "class_iii_words": sorted(r["word"] for r in class_iii),
            "rl_is_unique_in_iii": rl_unique,
        },
    }

    table_path = f"{out_dir}/w2b_table.json"
    with open(table_path, "w") as f:
        json.dump(output, f, indent=1)
    print(f"[W2b] wrote {table_path}", flush=True)

    print("[W2b] EXIT_MARKER_W2B_DONE", flush=True)


if __name__ == "__main__":
    main()
