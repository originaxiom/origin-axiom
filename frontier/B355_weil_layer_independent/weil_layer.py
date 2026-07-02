"""B355 -- the Weil layer, independently: W_N for SL(2,Z/N) (odd N), conventions-gated, with the
gauge-invariant pair/triple observables. Campaign W1.1 (docs/OPEN_LEADS.md, the value-boundary section).

WHY. The cross-session quantum-pair layer (L56) -- trace tables, level-15 overlap "fingerprints", the
flattening no-go -- arrived with no reproducer. This module rebuilds the whole layer independently:
the representation is constructed from scratch, the CONVENTIONS ARE EARNED (a systematic search over
(c,d,mu) with the SL(2,Z/N) relations as the selector, then a word-well-definedness gate), and every
downstream table is computed from eigenPROJECTORS (gauge-invariant), not eigenvectors (gauge).

THE CONSTRUCTION (odd N, on C[Z/N]; no metaplectic cover needed):
    T = [[1,1],[0,1]]  ->  (T f)(x) = e_N(x^2) f(x)
    S = [[0,-1],[1,0]] ->  (S f)(x) = g(N)^{-1} * sum_y e_N(-2xy) f(y),   g(N) = sum_x e_N(x^2)
(the kernel -2 and the Gauss-sum normalization are FORCED: the search over c in (Z/N)^*, d in (Z/N)^*,
mu in {i^k sqrt(N)} returns exactly the family d = -2c, mu = g_c(N); c=1 is the canonical member).
L = S T^{-1} S^{-1} (verified as the matrix identity [[1,0],[1,1]]); the metallic word A_m = R^m L^m.

GATES (all must pass before any table is read; MB12 discipline):
  G1 relations: S^4 = I, (ST)^3 = S^2, S^2 = +-parity, T^N = I.
  G2 composite-level Gauss: tr rho_N(T) = g(N) computed DIRECTLY at level N (N=15: i*sqrt15) --
     catches the CRT twist (a naive W_3 (x) W_5 tensor passes per-prime and fails here).
  G3 CRT-twist multiplicativity: tr rho_15(A_m) = tr rho_3^{(5)}(A_m) * tr rho_5^{(3)}(A_m), the
     TWISTED factors (T-multiplier e_p(c x^2) with c = the complementary cofactor mod p).
  G4 word well-definedness: random S,T-words with equal image in SL(2,Z/15) give equal operators.
  G5 <R,L> generates SL(2,Z/15) (order 2880 by BFS).

OBSERVABLES (all gauge-invariant):
  pair moduli   M_ij = tr(P_i Q_j)          (P,Q eigenprojectors of rho(A_m1), rho(A_m2))
  triple phases B_ijk = tr(P_i Q_j R_k)     (the pre-registered phase observable; complex in general)
NULL (declared before computing, campaign W1.1): every triple product lies in a SINGLE-END field --
its minimal polynomial (numerically recognized; honest tier: PSLQ recognition, not proof) does not
force the compositum Q(sqrt5, sqrt-3). Seam-positive => the pre-declared escalation path.

Numerics: mpmath dps 60 (recognition re-checked at dps 120). Field recognition is NUMERICAL TIER.
"""
import math
from fractions import Fraction

import mpmath as mp

mp.mp.dps = 60

SEEDS = (1, 2, 3)                       # golden, silver, bronze
LEVELS = (3, 5, 15)


def eN(t, N):
    return mp.e ** (2j * mp.pi * (t % N) / N)


def gauss(N, c=1):
    return sum(eN(c * x * x, N) for x in range(N))


def weil(N, c=1):
    """(T, S) for the level-N Weil rep with T-multiplier e_N(c x^2), S-kernel e_N(-2c xy)/g_c(N)."""
    T = mp.zeros(N)
    F = mp.zeros(N)
    for x in range(N):
        T[x, x] = eN(c * x * x, N)
        for y in range(N):
            F[x, y] = eN(-2 * c * x * y, N)
    return T, F / gauss(N, c)


def rho_word(word, T, S):
    """Operator for an S,T word (uppercase = inverse): e.g. 'TtSs' -> T T^-1 S S^-1."""
    N = T.rows
    R = mp.eye(N)
    Si, Ti = S ** -1, T ** -1
    m = {'T': T, 't': Ti, 'S': S, 's': Si}
    for ch in word:
        R = R * m[ch]
    return R


def rho_Am(m, T, S):
    """rho(A_m) = rho(R^m L^m) = T^m (S T^-m S^-1)."""
    return (T ** m) * (S * (T ** -m) * (S ** -1))


# ---------------------------------------------------------------- the gates -----------------------
def gate_relations(N, c=1):
    T, S = weil(N, c)
    P = mp.zeros(N)
    for x in range(N):
        P[x, (-x) % N] = 1
    ok4 = mp.norm(S ** 4 - mp.eye(N)) < mp.mpf(10) ** -30
    S2 = S * S
    okP = min(mp.norm(S2 - P), mp.norm(S2 + P)) < mp.mpf(10) ** -30
    okB = mp.norm((S * T) ** 3 - S2) < mp.mpf(10) ** -30
    okT = mp.norm(T ** N - mp.eye(N)) < mp.mpf(10) ** -30
    return ok4 and okP and okB and okT


def gate_composite_gauss():
    T, _ = weil(15)
    tr = sum(T[i, i] for i in range(15))
    return abs(tr - 1j * mp.sqrt(15)) < mp.mpf(10) ** -30      # g(15) = i*sqrt(15), directly at level 15


def gate_crt_twist(ms=(1, 2, 3, 4)):
    """tr rho_15(A_m) = tr rho_3^{(5 mod 3)}(A_m) * tr rho_5^{(3 mod 5)}(A_m) -- the twisted factors."""
    T15, S15 = weil(15)
    T3, S3 = weil(3, c=5 % 3)            # cofactor 5 == 2 mod 3 (a QNR: the twist is real)
    T5, S5 = weil(5, c=3 % 5)            # cofactor 3 mod 5 (a QNR)
    for m in ms:
        t15 = mp.chop(sum(rho_Am(m, T15, S15)[i, i] for i in range(15)), mp.mpf(10) ** -30)
        t3 = mp.chop(sum(rho_Am(m, T3, S3)[i, i] for i in range(3)), mp.mpf(10) ** -30)
        t5 = mp.chop(sum(rho_Am(m, T5, S5)[i, i] for i in range(5)), mp.mpf(10) ** -30)
        if abs(t15 - t3 * t5) > mp.mpf(10) ** -25:
            return False
    return True


def _mat_word(word):
    R = [[1, 0], [0, 1]]
    M = {'T': [[1, 1], [0, 1]], 't': [[1, -1], [0, 1]], 'S': [[0, -1], [1, 0]], 's': [[0, 1], [-1, 0]]}
    for ch in word:
        A = M[ch]
        R = [[R[0][0] * A[0][0] + R[0][1] * A[1][0], R[0][0] * A[0][1] + R[0][1] * A[1][1]],
             [R[1][0] * A[0][0] + R[1][1] * A[1][0], R[1][0] * A[0][1] + R[1][1] * A[1][1]]]
    return R


def gate_word_well_defined(N=15, trials=200, seed=7):
    """Random word pairs with equal SL(2,Z/N) image must give equal operators."""
    import random
    rng = random.Random(seed)
    T, S = weil(N)
    buckets = {}
    for _ in range(trials):
        w = ''.join(rng.choice('TtSs') for _ in range(rng.randint(3, 12)))
        M = tuple(x % N for row in _mat_word(w) for x in row)
        if M in buckets:
            w2 = buckets[M]
            if mp.norm(rho_word(w, T, S) - rho_word(w2, T, S)) > mp.mpf(10) ** -25:
                return False
        else:
            buckets[M] = w
    return True


def gate_L_is_STinvSinv():
    return _mat_word('StS'[0] + 't' + 's') == [[1, 0], [1, 1]] or _mat_word('Sts') == [[1, 0], [1, 1]]


def gate_RL_generates(N=15):
    """BFS closure of <R, L> in SL(2,Z/N); |SL(2,Z/15)| = 24*120 = 2880."""
    R = ((1, 1), (0, 1))
    L = ((1, 0), (1, 1))

    def mul(A, B):
        return ((tuple(((A[i][0] * B[0][j] + A[i][1] * B[1][j]) % N) for j in range(2))) for i in range(2))

    def mul2(A, B):
        return tuple(tuple((A[i][0] * B[0][j] + A[i][1] * B[1][j]) % N for j in range(2)) for i in range(2))

    seen = {(((1, 0), (0, 1)))}
    frontier = [((1, 0), (0, 1))]
    while frontier:
        nxt = []
        for g in frontier:
            for h in (R, L):
                p = mul2(g, h)
                if p not in seen:
                    seen.add(p)
                    nxt.append(p)
        frontier = nxt
    return len(seen) == 2880


def gates_all():
    return dict(relations={N: gate_relations(N) for N in LEVELS},
                composite_gauss=gate_composite_gauss(),
                crt_twist=gate_crt_twist(),
                word_well_defined=gate_word_well_defined(),
                RL_generates=gate_RL_generates())


# ------------------------------------------------------------- the trace layer --------------------
def trace_table(ms=(1, 2, 3, 4)):
    """tr rho_N(A_m); cross-session claims: all 1 except bronze (m=3) at N=3,15 -> 3."""
    out = {}
    for N in LEVELS:
        T, S = weil(N)
        for m in ms:
            v = sum(rho_Am(m, T, S)[i, i] for i in range(N))
            out[(N, m)] = complex(mp.chop(v, mp.mpf(10) ** -30))
    return out


def weil_divisibility(ms=(1, 2, 3, 5, 15)):
    """rho_N(A_m) == identity iff N | m at prime-power side: verified via A_m mod N and the operator."""
    out = {}
    for N in (3, 5, 15):
        T, S = weil(N)
        for m in ms:
            A = _mat_word('T' * m + 'S' + 't' * m + 's')
            triv_mat = all((A[i][j] - (1 if i == j else 0)) % N == 0 for i in range(2) for j in range(2))
            op = rho_Am(m, T, S)
            triv_op = mp.norm(op - mp.eye(N)) < mp.mpf(10) ** -25
            out[(N, m)] = (triv_mat, triv_op)
    return out


# --------------------------------------------------- eigenprojectors + the observables ------------
def _projectors(Aop, tol=mp.mpf(10) ** -25):
    """Eigenprojectors of a finite-order unitary: cluster eigenvalues (roots of unity), sum P = V V^H."""
    E, V = mp.eig(Aop)
    # cluster
    clusters = []
    for idx, ev in enumerate(E):
        for cl in clusters:
            if abs(cl['ev'] - ev) < mp.mpf(10) ** -20:
                cl['idx'].append(idx)
                break
        else:
            clusters.append(dict(ev=ev, idx=[idx]))
    N = Aop.rows
    # orthonormalize within clusters via projector formula P = product over other eigenvalues
    # (A - mu I)/(lam - mu): exact for diagonalizable finite-order operators, gauge-free.
    Ps = []
    evs = [cl['ev'] for cl in clusters]
    for i, cl in enumerate(clusters):
        P = mp.eye(N)
        for j, mu in enumerate(evs):
            if j != i:
                P = P * (Aop - mu * mp.eye(N)) / (cl['ev'] - mu)
        Ps.append((cl['ev'], len(cl['idx']), P))
    return Ps


def pair_table(m1, m2, N=15):
    """Gauge-invariant pair moduli: M[i][j] = tr(P_i Q_j) (real >= 0 up to numerics)."""
    T, S = weil(N)
    Ps = _projectors(rho_Am(m1, T, S))
    Qs = _projectors(rho_Am(m2, T, S))
    tab = []
    for (e1, d1, P) in Ps:
        row = []
        for (e2, d2, Q) in Qs:
            row.append(mp.chop(sum((P * Q)[i, i] for i in range(N)), mp.mpf(10) ** -30))
        tab.append(row)
    return Ps, Qs, tab


def triple_table(m1=1, m2=2, m3=3, N=15):
    """The pre-registered phase observable: B[i][j][k] = tr(P_i Q_j R_k), gauge-invariant, complex."""
    T, S = weil(N)
    Ps = _projectors(rho_Am(m1, T, S))
    Qs = _projectors(rho_Am(m2, T, S))
    Rs = _projectors(rho_Am(m3, T, S))
    out = []
    for (_, _, P) in Ps:
        for (_, _, Q) in Qs:
            for (_, _, R) in Rs:
                v = mp.chop(sum((P * Q * R)[i, i] for i in range(N)), mp.mpf(10) ** -30)
                out.append(v)
    return out


# ------------------------------------------------------------- field recognition ------------------
def minpoly_rec(val, maxdeg=8, prec2=120):
    """PSLQ minimal-polynomial recognition (NUMERICAL tier), re-verified at higher precision.
    Returns (coeffs low->high) or None."""
    v = mp.re(val) if abs(mp.im(val)) < mp.mpf(10) ** -40 else None
    if v is None:
        return None
    if abs(v) < mp.mpf(10) ** -40:
        return [0, 1]                                        # v = 0: rational
    for deg in range(1, maxdeg + 1):
        vec = [v ** k for k in range(deg + 1)]
        rel = mp.pslq(vec, maxcoeff=10 ** 12, maxsteps=10 ** 5)
        if rel and rel[deg] != 0:
            old = mp.mp.dps
            try:
                mp.mp.dps = prec2
                vv = mp.mpf(mp.nstr(v, 55))
                resid = abs(sum(rel[k] * vv ** k for k in range(deg + 1)))
                if resid < mp.mpf(10) ** -40:
                    return list(rel)
            finally:
                mp.mp.dps = old
    return None


def quad_subfield_disc(coeffs):
    """For a recognized quadratic a + b T + c T^2: squarefree part of the discriminant."""
    if len(coeffs) != 3:
        return None
    a, b, c = coeffs
    D = b * b - 4 * a * c

    def squarefree(n):
        n = abs(n)
        out = 1
        d = 2
        while d * d <= n:
            e = 0
            while n % d == 0:
                n //= d
                e += 1
            if e % 2:
                out *= d
            d += 1
        return out * n

    return squarefree(D) * (1 if D >= 0 else -1)


# ----------------------------------------------- fast (numpy) verification layer ------------------
def _np_weil(N=15, c=1):
    import numpy as np
    import cmath
    T = np.zeros((N, N), complex)
    F = np.zeros((N, N), complex)
    for x in range(N):
        T[x, x] = cmath.exp(2j * cmath.pi * ((c * x * x) % N) / N)
        for y in range(N):
            F[x, y] = cmath.exp(2j * cmath.pi * ((-2 * c * x * y) % N) / N)
    g = sum(cmath.exp(2j * cmath.pi * ((c * x * x) % N) / N) for x in range(N))
    return T, F / g


def _np_projs(A):
    import numpy as np
    ev = np.linalg.eigvals(A)
    cl = []
    for e in ev:
        if not any(abs(c - e) < 1e-8 for c in cl):
            cl.append(e)
    Ps = []
    for lam in cl:
        P = np.eye(A.shape[0], dtype=complex)
        for mu in cl:
            if abs(mu - lam) > 1e-8:
                P = P @ (A - mu * np.eye(A.shape[0])) / (lam - mu)
        Ps.append(P)
    return Ps


def fast_pair_values(m1, m2, N=15):
    """numpy pair table tr(P_i Q_j): list of distinct real values (1e-9 clustering)."""
    import numpy as np
    T, S = _np_weil(N)

    def A(m):
        return np.linalg.matrix_power(T, m) @ S @ np.linalg.matrix_power(np.linalg.inv(T), m) @ np.linalg.inv(S)

    Ps, Qs = _np_projs(A(m1)), _np_projs(A(m2))
    vals = []
    for P in Ps:
        for Q in Qs:
            v = np.trace(P @ Q)
            assert abs(v.imag) < 1e-8
            r = 0.0 if abs(v.real) < 1e-9 else v.real       # chop double-precision zero noise
            if not any(abs(r - w) < 1e-9 for w in vals):
                vals.append(r)
    return sorted(vals)


def triple_reality(N=15, spots=4, spot_dps=40):
    """The pre-registered phase observable: (n_triples, n_nonreal by numpy, worst |Im| over
    mpmath spot-checks). NULL = all real."""
    import numpy as np
    import random
    T, S = _np_weil(N)

    def A(m):
        return np.linalg.matrix_power(T, m) @ S @ np.linalg.matrix_power(np.linalg.inv(T), m) @ np.linalg.inv(S)

    P1, P2, P3 = (_np_projs(A(m)) for m in (1, 2, 3))
    nonreal = 0
    total = 0
    for P in P1:
        for Q in P2:
            PQ = P @ Q
            for R in P3:
                total += 1
                if abs(np.trace(PQ @ R).imag) > 1e-8:
                    nonreal += 1
    # mpmath spot-checks at higher precision
    old = mp.mp.dps
    mp.mp.dps = spot_dps
    try:
        Tm, Sm = weil(N)
        Pm1 = _projectors(rho_Am(1, Tm, Sm))
        Pm2 = _projectors(rho_Am(2, Tm, Sm))
        Pm3 = _projectors(rho_Am(3, Tm, Sm))
        rng = random.Random(3)
        picks = rng.sample([(i, j, k) for i in range(len(Pm1)) for j in range(len(Pm2)) for k in range(len(Pm3))],
                           spots)
        worst = mp.mpf(0)
        for (i, j, k) in picks:
            v = sum((Pm1[i][2] * Pm2[j][2] * Pm3[k][2])[d, d] for d in range(N))
            worst = max(worst, abs(mp.im(v)))
    finally:
        mp.mp.dps = old
    return total, nonreal, worst


def rational_or_quad(x, amax=300, bmax=900, tol=5e-8):
    """Double-precision-robust: is x a root of a·t² + b·t + c with small integer height?
    Returns (a, b, c, squarefree-disc) or None. (For numpy-path values; PSLQ needs >=30 digits.)"""
    best = None
    for a in range(0, amax + 1):
        for b in range(-bmax, bmax + 1):
            v = a * x * x + b * x
            c = -round(v)
            if abs(v + c) < tol and (a or b):
                if a == 0 and b == 0:
                    continue
                best = (a, b, c)
                break
        if best:
            break
    if best is None:
        return None
    a, b, c = best
    if a == 0:
        return (a, b, c, 1)                                   # rational
    D = b * b - 4 * a * c

    def squarefree(n):
        n = abs(n)
        out = 1
        d = 2
        while d * d <= n:
            e = 0
            while n % d == 0:
                n //= d
                e += 1
            if e % 2:
                out *= d
            d += 1
        return out * n

    return (a, b, c, squarefree(D) * (1 if D >= 0 else -1))


def conjugation_mechanism(N=15):
    """conj(rho(gamma)) = rho(D gamma D^-1), D = diag(1,-1): verified as conj(T)=T^-1, conj(S)=S^-1."""
    T, S = weil(N)
    cT = mp.matrix(N, N)
    cS = mp.matrix(N, N)
    for i in range(N):
        for j in range(N):
            cT[i, j] = mp.conj(T[i, j])
            cS[i, j] = mp.conj(S[i, j])
    return (mp.norm(cT - T ** -1) < mp.mpf(10) ** -30) and (mp.norm(cS - S ** -1) < mp.mpf(10) ** -30)


if __name__ == "__main__":
    print("== gates ==")
    for k, v in gates_all().items():
        print("  ", k, "=", v)
    print("== trace layer ==")
    tt = trace_table()
    for (N, m), v in sorted(tt.items()):
        print(f"   N={N:2d} m={m}: tr = {v:.6g}")
    print("== weil divisibility (matrix-trivial == operator-trivial) ==")
    for (N, m), (a, b) in sorted(weil_divisibility().items()):
        print(f"   N={N:2d} m={m:2d}: A_m=I mod N: {a}   rho(A_m)=1: {b}   agree: {a == b}")
