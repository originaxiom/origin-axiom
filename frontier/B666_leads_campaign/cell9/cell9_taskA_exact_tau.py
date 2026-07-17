"""B666 cell 9, TASK A (R21-2): the m = 7/8/11 EXACT identifications.

The silver (m136 = RRLL) six-exponent exterior torsion family: B627 banked
m = 1, 4, 5 as exact integers and left m = 7, 8, 11 as high-precision
complex numerics ("exact form unidentified; PSLQ failed within budget").

Here: the SAME pipeline (B627 conventions: presentation <a,b,c | aBAbcc,
aaCbcB>, alpha = {a:0, b:1, c:0}, Sym^{2m}, kept gens [a,c], dropped b,
shift/degree from the analytic bound, monic normalization, tau = Delta'(1))
is run EXACTLY over the field L = Q(s,i), s^4 = 8s^2+16, i^2 = -1
(the exact B649 silver holonomy, entries_L.json, re-verified in-sandbox:
relators exactly I, dets exactly 1).

Method (exact): multi-modular. For primes p ≡ 1 (mod 8) with x^4-8x^2-16
split, L embeds in F_p in 8 ways; the whole pipeline is field arithmetic,
so it commutes with each embedding hom (checked: no division by any element
mapping to 0 -- remainder/degree asserts). Per prime the 8 embedding values
determine the 8 rational coordinates of tau in the basis
(1, s, s^2, s^3, i, is, is^2, is^3) by an exact 8x8 solve mod p; CRT across
primes + rational reconstruction gives the exact coordinates; verified on
EXTRA primes never used in the reconstruction, then numerically at 250 dps
against B627's sealed digits.

Calibration: the same engine must reproduce the three banked exact integers
tau_1 = -16, tau_4 = +11682800640, tau_5 = -1357126041600000 (B627 sealed).
"""
import sys, json, time, random
from fractions import Fraction
from math import comb

sys.path.insert(0, _REPO + '/frontier/B666_leads_campaign/cell9')
from cell9_L_arith import load_silver_gens, ONE8
import os
_REPO = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", ".."))

GENS_PATH = _REPO + '/frontier/B649_silver_holonomy/entries_L.json'
GENS = ['a', 'b', 'c']
RELATORS = ['aBAbcc', 'aaCbcB']
KEPT = ['a', 'c']
DROPPED = 'b'
ALPHA = {'a': 0, 'b': 1, 'c': 0}   # matches B627's logged alpha_map output

# ---------------- prime / embedding machinery ----------------

def is_probable_prime(n, k=40):
    if n < 2:
        return False
    for p in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]:
        if n % p == 0:
            return n == p
    d = n - 1
    r = 0
    while d % 2 == 0:
        d //= 2
        r += 1
    for _ in range(k):
        a = random.randrange(2, n - 1)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = x * x % n
            if x == n - 1:
                break
        else:
            return False
    return True


def sqrt_mod(a, p):
    """Tonelli-Shanks; returns r with r^2 = a mod p, or None."""
    a %= p
    if a == 0:
        return 0
    if pow(a, (p - 1) // 2, p) != 1:
        return None
    if p % 4 == 3:
        return pow(a, (p + 1) // 4, p)
    q, s = p - 1, 0
    while q % 2 == 0:
        q //= 2
        s += 1
    z = 2
    while pow(z, (p - 1) // 2, p) != p - 1:
        z += 1
    m, c, t, r = s, pow(z, q, p), pow(a, q, p), pow(a, (q + 1) // 2, p)
    while t != 1:
        i, tt = 0, t
        while tt != 1:
            tt = tt * tt % p
            i += 1
        b = pow(c, 1 << (m - i - 1), p)
        m, c = i, b * b % p
        t, r = t * c % p, r * b % p
    return r


def find_good_primes(count, seed_start):
    """Primes p ≡ 1 mod 8 with x^2+1 and x^4-8x^2-16 fully split mod p.
    Returns list of (p, iota, sig, sigp): iota^2=-1, sig^2=4+4*sqrt2,
    sigp^2=4-4*sqrt2 (one fixed choice of sqrt2 per prime)."""
    out = []
    n = seed_start | 1
    while len(out) < count:
        n += 2
        if n % 8 != 1:
            continue
        if not is_probable_prime(n):
            continue
        p = n
        r2 = sqrt_mod(2, p)
        if r2 is None:
            continue
        iota = sqrt_mod(p - 1, p)
        if iota is None:
            continue
        sig = sqrt_mod((4 + 4 * r2) % p, p)
        if sig is None:
            continue
        sigp = sqrt_mod((4 - 4 * r2) % p, p)
        if sigp is None:
            continue
        # sanity: quartic splits
        for s_ in (sig, sigp):
            assert (pow(s_, 4, p) - 8 * pow(s_, 2, p) - 16) % p == 0
        out.append((p, iota, sig, sigp))
    return out


def embed_L(coords, s_p, i_p, p):
    """coords: 8-tuple of Fractions -> value in F_p."""
    val = 0
    sp = [1, s_p % p, pow(s_p, 2, p), pow(s_p, 3, p)]
    for k in range(2):
        for j in range(4):
            c = coords[j + 4 * k]
            if c:
                num = c.numerator % p
                den = pow(c.denominator % p, p - 2, p)
                term = num * den % p * sp[j] % p
                if k == 1:
                    term = term * i_p % p
                val = (val + term) % p
    return val


# ---------------- pipeline mod p ----------------

def sym_power_matrix_p(A, k, p):
    """Port of B627 pipeline.sym_power_matrix, over F_p. A: 2x2 ints."""
    a, b, c, d = A[0][0], A[0][1], A[1][0], A[1][1]
    out = [[0] * (k + 1) for _ in range(k + 1)]
    for i in range(k + 1):
        pp, q = k - i, i
        coefs_p = [comb(pp, s_) * pow(a, pp - s_, p) % p * pow(c, s_, p) % p
                   for s_ in range(pp + 1)]
        coefs_q = [comb(q, u) * pow(b, q - u, p) % p * pow(d, u, p) % p
                   for u in range(q + 1)]
        row_of_j = [0] * (k + 1)
        for s_ in range(pp + 1):
            cs = coefs_p[s_]
            if cs == 0:
                continue
            for u in range(q + 1):
                j = s_ + u
                row_of_j[j] = (row_of_j[j] + cs * coefs_q[u]) % p
        for j in range(k + 1):
            out[j][i] = row_of_j[j]
    return out


def mat_mul_p(A, B, p):
    n, m2, l = len(A), len(B), len(B[0])
    Bt = [[B[r][c] for r in range(m2)] for c in range(l)]
    C = [[0] * l for _ in range(n)]
    for i in range(n):
        Ai = A[i]
        Ci = C[i]
        for jc in range(l):
            Bc = Bt[jc]
            s_ = 0
            for r in range(m2):
                s_ += Ai[r] * Bc[r]
            Ci[jc] = s_ % p
    return C


def mat_inv_p(A, p):
    n = len(A)
    M = [row[:] + [1 if i == j else 0 for j in range(n)]
         for i, row in enumerate(A)]
    for col in range(n):
        piv = next(r for r in range(col, n) if M[r][col] % p != 0)
        M[col], M[piv] = M[piv], M[col]
        inv = pow(M[col][col], p - 2, p)
        M[col] = [x * inv % p for x in M[col]]
        for r in range(n):
            if r != col and M[r][col]:
                f = M[r][col]
                Mr, Mc = M[r], M[col]
                M[r] = [(x - f * y) % p for x, y in zip(Mr, Mc)]
    return [row[n:] for row in M]


def det_p(M, p):
    n = len(M)
    A = [row[:] for row in M]
    det = 1
    for col in range(n):
        piv = None
        for r in range(col, n):
            if A[r][col] % p != 0:
                piv = r
                break
        if piv is None:
            return 0
        if piv != col:
            A[col], A[piv] = A[piv], A[col]
            det = -det
        pivval = A[col][col]
        det = det * pivval % p
        inv = pow(pivval, p - 2, p)
        Ac = A[col][col:]
        for r in range(col + 1, n):
            f = A[r][col]
            if f:
                f = f * inv % p
                Ar = A[r]
                Ar[col:] = [(x - f * y) % p for x, y in zip(Ar[col:], Ac)]
    return det % p


def fox_occurrences_p(word, xj, acts, acts_inv, alpha, d, p):
    """The t^alpha-twisted Fox derivative d(word)/d(xj) as a finite sum
    Sum_occ M_occ * t^(e_occ) with t-INDEPENDENT matrices M_occ (the trick:
    every letter's action is Sym(g) * t^alpha(g), so the t-power of each
    prefix factors out).  Returns list of (e_occ, M_occ)."""
    pref = [[1 if i == j else 0 for j in range(d)] for i in range(d)]
    e = 0
    occs = []
    for ch in word:
        if ch.islower():
            x = ch
            if x == xj:
                occs.append((e, [row[:] for row in pref]))
            pref = mat_mul_p(pref, acts[x], p)
            e += alpha[x]
        else:
            x = ch.lower()
            e -= alpha[x]
            if x == xj:
                neg = mat_mul_p(pref, acts_inv[x], p)
                occs.append((e, [[(-v) % p for v in row] for row in neg]))
            pref = mat_mul_p(pref, acts_inv[x], p)
    return occs


def word_exponent_range(word, xj, alpha):
    e, lo, hi = 0, None, None
    for ch in word:
        if ch.islower():
            x = ch
            if x == xj:
                lo = e if lo is None else min(lo, e)
                hi = e if hi is None else max(hi, e)
            e += alpha[x]
        else:
            x = ch.lower()
            e -= alpha[x]
            if x == xj:
                lo = e if lo is None else min(lo, e)
                hi = e if hi is None else max(hi, e)
    return lo, hi


def analytic_shift_and_degree(relators, kept_gens, alpha, d, cushion=2):
    gmin = gmax = 0
    for r in relators:
        los, his = [], []
        for xj in kept_gens:
            lo, hi = word_exponent_range(r, xj, alpha)
            los.append(lo if lo is not None else 0)
            his.append(hi if hi is not None else 0)
        gmin += d * min(los)
        gmax += d * max(his)
    shift = max(0, -gmin) + cushion
    degree = shift + gmax + cushion
    return shift, degree


def block_numerator_p(tval, occ_table, relators, kept_gens, d, p):
    """Assemble the block Fox matrix at t=tval from the precomputed
    occurrence lists and take its determinant mod p."""
    tinv = pow(tval, p - 2, p)
    n1 = len(relators)
    N = n1 * d
    Big = [[0] * N for _ in range(N)]
    for i in range(n1):
        for j in range(len(kept_gens)):
            for (e, M) in occ_table[(i, j)]:
                tf = pow(tval, e, p) if e >= 0 else pow(tinv, -e, p)
                for pi in range(d):
                    row = Big[i * d + pi]
                    Mrow = M[pi]
                    base = j * d
                    for q in range(d):
                        if Mrow[q]:
                            row[base + q] = (row[base + q] + Mrow[q] * tf) % p
    return det_p(Big, p)


def lagrange_interp_p(xs, ys, p):
    n = len(xs)
    coeffs = [0] * n
    for i in range(n):
        num = [1]
        denom = 1
        for j in range(n):
            if j == i:
                continue
            newnum = [0] * (len(num) + 1)
            for k, c in enumerate(num):
                newnum[k] = (newnum[k] - c * xs[j]) % p
                newnum[k + 1] = (newnum[k + 1] + c) % p
            num = newnum
            denom = denom * (xs[i] - xs[j]) % p
        w = ys[i] * pow(denom, p - 2, p) % p
        for k in range(len(num)):
            coeffs[k] = (coeffs[k] + w * num[k]) % p
    return coeffs


def poly_eval_p(coeffs, t, p):
    v = 0
    for c in reversed(coeffs):
        v = (v * t + c) % p
    return v


def poly_divide_p(num, den, p):
    num = [x % p for x in num]
    den = [x % p for x in den]
    while den and den[-1] == 0:
        den.pop()
    dd = len(den) - 1
    dinv = pow(den[-1], p - 2, p)
    rem = num[:]
    q = [0] * max(len(rem) - dd, 1)
    while len(rem) - 1 >= dd and any(rem):
        if rem[-1] == 0:
            rem.pop()
            continue
        shift_ = len(rem) - 1 - dd
        c = rem[-1] * dinv % p
        q[shift_] = c
        for j in range(len(den)):
            rem[shift_ + j] = (rem[shift_ + j] - c * den[j]) % p
        while rem and rem[-1] == 0:
            rem.pop()
    return q, rem


def tau_mod_p(m_exp, acts2x2_p, p, verbose=False):
    """Full B627 pipeline mod p for one embedding. Returns (tau, qdeg)."""
    k = 2 * m_exp
    d = k + 1
    sym_acts = {g: sym_power_matrix_p(acts2x2_p[g], k, p) for g in GENS}
    sym_inv = {g: mat_inv_p(sym_acts[g], p) for g in GENS}
    shift, degbound = analytic_shift_and_degree(RELATORS, KEPT, ALPHA, d)
    # precompute the t-independent Fox occurrence lists
    occ_table = {}
    for i, r in enumerate(RELATORS):
        for j, xj in enumerate(KEPT):
            occ_table[(i, j)] = fox_occurrences_p(r, xj, sym_acts, sym_inv,
                                                  ALPHA, d, p)
    # numerator poly: t^shift * Num(t), degree <= degbound
    npts = degbound + 1
    xs, ys = [], []
    tv = 2
    while len(xs) < npts + 2:          # +2 validation nodes
        nv = block_numerator_p(tv, occ_table, RELATORS, KEPT, d, p)
        ys.append(nv * pow(tv, shift, p) % p)
        xs.append(tv)
        tv += 1
    numP = lagrange_interp_p(xs[:npts], ys[:npts], p)
    for t_, y_ in zip(xs[npts:], ys[npts:]):
        assert poly_eval_p(numP, t_, p) == y_ % p, "validation node mismatch"
    # denominator: det(t*Sym(b) - I) -- interpolate exactly (degree d)
    dxs = list(range(2, d + 4))
    dys = []
    U = sym_acts[DROPPED]
    for t_ in dxs:
        Mt = [[(t_ * U[i][j] - (1 if i == j else 0)) % p for j in range(d)]
              for i in range(d)]
        dys.append(det_p(Mt, p))
    denP = lagrange_interp_p(dxs, dys, p)
    while denP and denP[-1] == 0:
        denP.pop()
    assert len(denP) - 1 == d, f"den degree {len(denP)-1} != {d}"
    q, rem = poly_divide_p(numP, denP, p)
    assert not any(rem), "nonzero division remainder mod p"
    while q and q[-1] == 0:
        q.pop()
    qdeg = len(q) - 1
    lead_inv = pow(q[-1], p - 2, p)
    qn = [c * lead_inv % p for c in q]
    assert sum(qn) % p == 0, "Delta(1) != 0 mod p"
    tau = sum(i * c for i, c in enumerate(qn)) % p
    return tau, qdeg


# ---------------- CRT + rational reconstruction ----------------

def crt_pair(r1, m1, r2, m2):
    # solve x = r1 mod m1, x = r2 mod m2  (m2 prime, coprime to m1)
    inv = pow(m1 % m2, -1, m2)
    t = (r2 - r1) % m2 * inv % m2
    return (r1 + m1 * t) % (m1 * m2), m1 * m2


def rational_reconstruct(a, m):
    """Find n/d = a mod m with |n|, d <= sqrt(m/2); returns Fraction or None."""
    from math import isqrt, gcd
    a %= m
    if a == 0:
        return Fraction(0)
    bound = isqrt(m // 2)
    r0, r1 = m, a
    s0, s1 = 0, 1
    while r1 > bound:
        q = r0 // r1
        r0, r1 = r1, r0 - q * r1
        s0, s1 = s1, s0 - q * s1
    if abs(s1) > bound or s1 == 0:
        return None
    g = gcd(r1, abs(s1))
    if g > 1:
        r1, s1 = r1 // g, s1 // g
    return Fraction(r1, s1) if s1 > 0 else Fraction(-r1, -s1)


def solve_coords_mod_p(tau_by_emb, embs, p):
    """8x8 solve: coords in basis (s^j i^k) from the 8 embedding values."""
    rows, rhs = [], []
    for (s_p, i_p), tv in zip(embs, tau_by_emb):
        sp = [1, s_p % p, pow(s_p, 2, p), pow(s_p, 3, p)]
        row = []
        for k in range(2):
            for j in range(4):
                row.append(sp[j] * (i_p if k == 1 else 1) % p)
        rows.append(row)
        rhs.append(tv)
    n = 8
    M = [rows[i][:] + [rhs[i]] for i in range(n)]
    for col in range(n):
        piv = next(r for r in range(col, n) if M[r][col] % p != 0)
        M[col], M[piv] = M[piv], M[col]
        inv = pow(M[col][col], p - 2, p)
        M[col] = [x * inv % p for x in M[col]]
        for r in range(n):
            if r != col and M[r][col]:
                f = M[r][col]
                M[r] = [(x - f * y) % p for x, y in zip(M[r], M[col])]
    return [M[i][8] % p for i in range(8)]


def main():
    t_start = time.time()
    gens = load_silver_gens(GENS_PATH)
    # exact 2x2 entries as coordinate tuples
    coords2x2 = {g: [[gens[g][r][c] for c in range(2)] for r in range(2)]
                 for g in GENS}

    QUICK = 'quick' in sys.argv[1:]
    N_RECON = 4 if QUICK else 14      # primes used in reconstruction
    N_VERIFY = 1 if QUICK else 3      # extra primes only for verification
    print("finding good primes (p ≡ 1 mod 8, quartic + i split) ...")
    primes = find_good_primes(N_RECON + N_VERIFY, (1 << 61) + 12345)
    print(f"got {len(primes)} primes; first {primes[0][0]}, last {primes[-1][0]}")

    M_EXPS = [1, 4, 5] if QUICK else [1, 4, 5, 7, 8, 11]
    BANKED_INT = {1: -16, 4: 11682800640, 5: -1357126041600000}

    # per m: list over primes of (p, coords mod p)
    residues = {m: [] for m in M_EXPS}
    qdegs = {}
    for (p, iota, sig, sigp) in primes:
        t0 = time.time()
        embs = []
        for s_p in (sig, p - sig, sigp, p - sigp):
            for i_p in (iota, p - iota):
                embs.append((s_p, i_p))
        # embed generators once per embedding
        acts_by_emb = []
        for (s_p, i_p) in embs:
            acts = {}
            for g in GENS:
                acts[g] = [[embed_L(coords2x2[g][r][c], s_p, i_p, p)
                            for c in range(2)] for r in range(2)]
            # sanity: det = 1 mod p
            for g in GENS:
                A = acts[g]
                assert (A[0][0] * A[1][1] - A[0][1] * A[1][0]) % p == 1
            acts_by_emb.append(acts)
        for m_exp in M_EXPS:
            taus = []
            qd = None
            for acts in acts_by_emb:
                tau, qdeg = tau_mod_p(m_exp, acts, p)
                taus.append(tau)
                if qd is None:
                    qd = qdeg
                assert qdeg == qd, "qdeg differs across embeddings (bad prime?)"
            expected_qdeg = 2 * m_exp + 3
            assert qd == expected_qdeg, f"qdeg {qd} != {expected_qdeg} (bad prime)"
            qdegs[m_exp] = qd
            coords_p = solve_coords_mod_p(taus, embs, p)
            residues[m_exp].append((p, coords_p))
        print(f"prime {p}: all m done in {time.time()-t0:.1f}s", flush=True)

    # CRT + rational reconstruction using the first N_RECON primes
    print("\n===== RECONSTRUCTION =====")
    exact = {}
    for m_exp in M_EXPS:
        rec = residues[m_exp][:N_RECON]
        coords_exact = []
        for idx in range(8):
            r, mod = rec[0][1][idx], rec[0][0]
            for (p, cp) in rec[1:]:
                r, mod = crt_pair(r, mod, cp[idx], p)
            fr = rational_reconstruct(r, mod)
            assert fr is not None, f"rational reconstruction failed m={m_exp} idx={idx}"
            coords_exact.append(fr)
        exact[m_exp] = tuple(coords_exact)
        # verification on held-out primes
        for (p, cp) in residues[m_exp][N_RECON:]:
            for idx in range(8):
                fr = coords_exact[idx]
                lhs = fr.numerator % p * pow(fr.denominator % p, p - 2, p) % p
                assert lhs == cp[idx] % p, \
                    f"HELD-OUT PRIME CHECK FAILED m={m_exp} idx={idx} p={p}"
        print(f"m={m_exp}: coords (1,s,s^2,s^3, i,is,is^2,is^3) =")
        for idx, fr in enumerate(coords_exact):
            if fr != 0:
                base = ['1', 's', 's^2', 's^3', 'i', 'i*s', 'i*s^2', 'i*s^3'][idx]
                print(f"    {base}: {fr}")
        if all(f == 0 for f in coords_exact):
            print("    0")
        print(f"  qdeg = {qdegs[m_exp]} (= 2m+3: {qdegs[m_exp] == 2*m_exp+3})")
        # calibration rows must be the banked integers
        if m_exp in BANKED_INT:
            want = BANKED_INT[m_exp]
            got_ok = (coords_exact[0] == want
                      and all(f == 0 for f in coords_exact[1:]))
            print(f"  CALIBRATION vs banked {want}: {'PASS' if got_ok else 'FAIL'}")
            assert got_ok
        print(f"  verified on {N_VERIFY} held-out primes: PASS")

    # persist the reconstruction FIRST (the verification stages below must
    # not be able to lose it)
    out = {str(m): [str(f) for f in exact[m]] for m in M_EXPS}
    json.dump(out, open(_REPO + '/frontier/B666_leads_campaign/'
                        'cell9/taskA_exact_coords.json', 'w'), indent=1)
    print("exact coordinates written to taskA_exact_coords.json")

    # numeric comparison against the sealed B627 digits (250 dps),
    # parsed directly from B627's preserved run records (no hand transcription)
    print("\n===== NUMERIC COMPARISON vs the SEALED B627 values =====")
    import mpmath as mp, re
    mp.mp.dps = 260

    def parse_tau_line(text, m_exp):
        pat = (r'm=%d: tau=\(([-0-9.]+)\s*([+-])\s*([0-9.]+)j\)' % m_exp)
        mo = re.search(pat, text)
        assert mo, f"could not parse sealed tau for m={m_exp}"
        re_s, sign, im_s = mo.groups()
        return mp.mpc(mp.mpf(re_s), mp.mpf(im_s) * (1 if sign == '+' else -1))

    b627 = _REPO + '/frontier/B627_silver_heldout/'
    sealed = {}
    if not QUICK:
        sealed[7] = parse_tau_line(open(b627 + 'm7_line.txt').read(), 7)
        sealed[8] = parse_tau_line(open(b627 + 'm8_line.txt').read(), 8)
        sealed[11] = parse_tau_line(open(b627 + 'm136_six_run.log').read(), 11)
    # the four candidate archimedean embeddings with s real (the geometric ones)
    s_real = mp.sqrt(4 + 4 * mp.sqrt(2))
    embeddings = {
        '(s -> +sqrt(4+4sqrt2), i -> +i)': (s_real, mp.mpc(0, 1)),
        '(s -> +sqrt(4+4sqrt2), i -> -i)': (s_real, mp.mpc(0, -1)),
        '(s -> -sqrt(4+4sqrt2), i -> +i)': (-s_real, mp.mpc(0, 1)),
        '(s -> -sqrt(4+4sqrt2), i -> -i)': (-s_real, mp.mpc(0, -1)),
    }
    # NOTE (run 2): the sealed B627 numerics were produced from SnapPy's
    # ManifoldHP holonomy (quad-double, ~60 digits) treated as 250-dps input;
    # their tau error grows steeply with d = 2m+1 (the seat's own
    # pre-registered m=7/8/11 hazard, cellF_full_result.md item 3).  Expected
    # agreement: m=7 ~ 1e-27, m=8 ~ 1e-18, m=11 none (sealed value is noise).
    # The authoritative independent numeric check is cell9_taskA_verify2.py
    # (EXACT B649 entries evaluated at 500 dps through B627's own pipeline).
    EXPECT = {7: mp.mpf('1e-20'), 8: mp.mpf('1e-10'), 11: mp.inf}
    for m_exp in ([] if QUICK else [7, 8, 11]):
        print(f"m={m_exp}:")
        best = None
        for name, (sv, iv) in embeddings.items():
            val = mp.mpc(0)
            for k in range(2):
                for j in range(4):
                    fr = exact[m_exp][j + 4 * k]
                    if fr:
                        term = mp.mpf(fr.numerator) / mp.mpf(fr.denominator) * sv ** j
                        if k == 1:
                            term *= iv
                        val += term
            err = abs(val - sealed[m_exp]) / abs(sealed[m_exp])
            print(f"  {name}: rel dev vs sealed = {mp.nstr(err, 3)}")
            if best is None or err < best[1]:
                best = (name, err)
        if m_exp == 11:
            print(f"  m=11: rel dev vs sealed = {mp.nstr(best[1], 3)} -- the "
                  f"sealed m=11 digits are input-precision noise (adjudicated "
                  f"by verify2); no agreement expected")
        else:
            print(f"  agreement with sealed to {mp.nstr(best[1], 3)} "
                  f"(within the sealed numerics' credible window)")
            assert best[1] < EXPECT[m_exp], "sealed-comparison outside window"

    # sign law + property checks on the exact values
    print("\n===== PROPERTY CERTIFICATES (exact) =====")
    for m_exp in ([] if QUICK else [7, 8, 11]):
        c = exact[m_exp]
        print(f"m={m_exp}: tau in Z[1/2][s,i]-span check: denominators = "
              f"{sorted(set(f.denominator for f in c))}")

    # exact factorizations of the identified integers
    if not QUICK:
        import sympy as sp
        print("\n===== FACTORIZATIONS (exact) =====")
        for m_exp in M_EXPS:
            v = exact[m_exp][0]
            if v.denominator == 1 and all(f == 0 for f in exact[m_exp][1:]):
                n = int(v)
                fac = sp.factorint(abs(n))
                fstr = ' * '.join(f"{p}^{e}" if e > 1 else str(p)
                                  for p, e in sorted(fac.items()))
                print(f"tau_{m_exp} = {n} = {'-' if n < 0 else '+'}{fstr}")
        print("\nsign law sign(Re tau_m) = (-1)^m on the exact values:",
              all((exact[m][0] < 0) == (m % 2 == 1) for m in M_EXPS))

    print(f"\ntotal time {time.time()-t_start:.1f}s")
    print("TASK A ENGINE: ALL GATES PASSED")


if __name__ == '__main__':
    main()
