"""The web seat, 2026-11-06: THE DEPARTURE THE LINE CANNOT SEE (PREREGISTRATION.md in this folder, predictions P1-P6).
Data-free: SL(2, Z) arithmetic and hyperbolic geometry only -- no frame value, no theta function, no data file, no
held-out quantity, no theta-bar, no inter-sector value. Lines are written (a/5, b/5); the action is the record's,
(alpha, b) -> (alpha, b) gamma^-1 under tau -> gamma tau (B1733 sec. 1), and the frame identifies +-w.

  A  the golden pair: the lines RL and LR fix up to sign; the knot determinant; RL, LR mod 5           (P1)
  B  level-5 visibility: L^n R (LR)^k against (LR)^(k+1) mod 5, n = 1..12, k = 0..19                   (P2)
  C  the highest apexes of L^n R (LR)^k, n = 5, 6, k = 0..20, by the matrix orbit with S-conjugates
     and by continued fractions; the homoclinic limit n/2 + i(n - 1 + sqrt5)/2                          (P3)
  D  each approximant's own order-5 lines (B1733's rule) at its highest apex, Re tau in [0, 1)          (P4)
  E  the homoclinic history, n = 1..12: the in and out golden lifts, their own pairs at the apex, the
     stabiliser test, and the palindrome's reflection                                                  (P5)
  F  the departure's excess length                                                                     (P6)

    python3 departure_check.py
"""
import mpmath as mp

mp.mp.dps = 60
EPS = mp.mpf(10) ** -40
PHI = (1 + mp.sqrt(5)) / 2
I2 = ((1, 0), (0, 1))
L = ((1, 0), (1, 1))
R = ((1, 1), (0, 1))
T = R
S = ((0, -1), (1, 0))
J0 = ((-1, 0), (0, 1))  # tau -> -conj(tau); on lines (alpha, b) -> (-alpha, b), the frame's mirror covariance (P-336)


def mul(A, B):
    return ((A[0][0] * B[0][0] + A[0][1] * B[1][0], A[0][0] * B[0][1] + A[0][1] * B[1][1]),
            (A[1][0] * B[0][0] + A[1][1] * B[1][0], A[1][0] * B[0][1] + A[1][1] * B[1][1]))


def det(A):
    return A[0][0] * A[1][1] - A[0][1] * A[1][0]


def inv(A):
    (a, b), (c, d) = A
    e = det(A)
    assert e in (1, -1)
    return ((d * e, -b * e), (-c * e, a * e))


def pw(A, n):
    if n < 0:
        A, n = inv(A), -n
    P = I2
    for _ in range(n):
        P = mul(P, A)
    return P


def prod(letters):
    P = I2
    for x in letters:
        P = mul(P, x)
    return P


def conj(g, A):
    return mul(mul(g, A), inv(g))


def tr(A):
    return A[0][0] + A[1][1]


def mod5(A):
    return tuple(tuple(x % 5 for x in row) for row in A)


def neg(A):
    return tuple(tuple(-x for x in row) for row in A)


RL, LR = mul(R, L), mul(L, R)
NONZERO = [(a, b) for a in range(5) for b in range(5) if (a, b) != (0, 0)]


def act(w, G):
    """the row vector w times G, mod 5"""
    return ((w[0] * G[0][0] + w[1] * G[1][0]) % 5, (w[0] * G[0][1] + w[1] * G[1][1]) % 5)


def pm(w):
    return min(w, ((-w[0]) % 5, (-w[1]) % 5))


LINES12 = sorted(set(pm(w) for w in NONZERO))


def own(A, sign=None):
    """order-5 lines w with w A^-1 = +-w (sign None), = +w (sign +1) or = -w (sign -1)"""
    Ai, out = inv(A), set()
    for w in NONZERO:
        u = act(w, Ai)
        if (sign in (None, 1) and u == w) or (sign in (None, -1) and u == ((-w[0]) % 5, (-w[1]) % 5)):
            out.add(pm(w))
    return frozenset(out)


def fl(lines):
    if len(lines) == 12:
        return "all twelve"
    if not lines:
        return "none"
    return "{" + ", ".join("+-(%d/5, %d/5)" % w for w in sorted(lines)) + "}"


def word(n, k):
    return [L] * n + [R] + [L, R] * k


def axis(A):
    (a, b), (c, d) = A
    t = a + d
    assert abs(t) > 2 and c != 0, A
    s = mp.sqrt(mp.mpf(t * t - 4))
    return (mp.mpf(a - d) + s) / (2 * c), (mp.mpf(a - d) - s) / (2 * c)


def apex(A):
    x1, x2 = axis(A)
    return (x1 + x2) / 2, abs(x1 - x2) / 2


def fixes(A, x):
    (a, b), (c, d) = A
    return abs((a * x + b) / (c * x + d) - x)


def highest_matrix(letters):
    """the highest lift over the rotations of the word and their S-conjugates; returns (centre, radius, matrix)"""
    W, best = prod(letters), None
    for j in range(len(letters)):
        P = prod(letters[:j])
        Aj = mul(mul(inv(P), W), P)
        for g in (I2, S):
            A = conj(g, Aj)
            c, r = apex(A)
            if best is None or r > best[1] + EPS:
                best = (c, r, A)
    return best


def to_unit(c, A):
    """conjugate by T^-m (tau -> tau - m) so that the centre lies in [0, 1)"""
    m = int(mp.floor(c + EPS))
    return c - m, conj(pw(T, -m), A)


def cf(seq):
    v = mp.mpf(seq[-1])
    for a in reversed(seq[:-1]):
        v = a + 1 / v
    return v


def highest_cf(runs, reps=40):
    """the Lagrange formula over the cyclic run sequence: max_i [a_i; a_i+1, ...] + [0; a_i-1, ...]"""
    p, best = len(runs), None
    for i in range(p):
        xp = cf([runs[(i + j) % p] for j in range(p * reps)])
        y = 1 / cf([runs[(i - 1 - j) % p] for j in range(p * reps)])
        if best is None or xp + y > best[0] + EPS:
            best = (xp + y, (xp - y) / 2)
    return best[0] / 2, best[1] - mp.floor(best[1] + EPS)


def cf_digits(x, n=12):
    out = []
    for _ in range(n):
        a = int(mp.floor(x))
        out.append(a)
        x = 1 / (x - a)
    return out


SL25 = [((a, b), (c, d)) for a in range(5) for b in range(5) for c in range(5) for d in range(5) if (a * d - b * c) % 5 == 1]


def conjugate_mod5(A, B):
    A, B = mod5(A), mod5(B)
    for g in SL25:
        (a, b), (c, d) = g
        gi = ((d % 5, (-b) % 5), ((-c) % 5, a % 5))  # det g = 1 mod 5, so the adjugate is the inverse mod 5
        if mod5(mul(mul(g, A), gi)) == B:
            return True
    return False


if __name__ == "__main__":
    print("THE DEPARTURE THE LINE CANNOT SEE -- data-free check (the web seat, 2026-11-06)")

    print("\nA. THE GOLDEN PAIR (P1)")
    for name, M in (("RL", RL), ("LR", LR)):
        U = neg(M)
        unip = mod5(U) != mod5(I2)
        N2 = mod5(pw(((U[0][0] - 1, U[0][1]), (U[1][0], U[1][1] - 1)), 2))
        print("  %s = %s, tr %d, det(M - I) %d, det(M + I) %d; lines fixed: +w %s; -w %s; -M unipotent mod 5 "
              "(-M != I, (-M - I)^2 = 0): %s" % (name, M, tr(M), det(((M[0][0] - 1, M[0][1]), (M[1][0], M[1][1] - 1))),
                                                 det(((M[0][0] + 1, M[0][1]), (M[1][0], M[1][1] + 1))),
                                                 fl(own(M, 1)), fl(own(M, -1)), unip and N2 == ((0, 0), (0, 0))))
    print("  the figure-eight's determinant |Delta(-1)|, Delta(t) = t^2 - 3t + 1: %d" % abs(1 + 3 + 1))
    print("  RL's pair against LR's: LR = L (RL) L^-1, and own(LR) = own(RL) L^-1: %s" % (
        own(LR) == frozenset(pm(act(w, inv(L))) for w in own(RL))))

    print("\nB. LEVEL-5 VISIBILITY (P2): L^n R (LR)^k against (LR)^(k+1) mod 5, k = 0..19")
    for n in range(1, 13):
        eq = [k for k in range(20) if mod5(prod(word(n, k))) == mod5(pw(LR, k + 1))]
        cj = [k for k in range(20) if conjugate_mod5(prod(word(n, k)), pw(LR, k + 1))]
        print("  n = %2d (n mod 5 = %d): equal mod 5 at %s; conjugate in SL(2, F5) at %s" % (
            n, n % 5, "every k" if len(eq) == 20 else (eq or "no k"), "every k" if len(cj) == 20 else (cj or "no k")))
    print("  the word with T^5 inserted after its first L: L^5 L R (LR)^k = L^6 R (LR)^k; and L^5 = I mod 5: %s" % (
        mod5(pw(L, 5)) == mod5(I2)))

    print("\nC. HIGHEST APEXES (P3): matrix orbit with S-conjugates | continued fractions | homoclinic limit")
    lim = {}
    for n in (5, 6):
        lim[n] = (mp.mpf(n) / 2 - mp.floor(mp.mpf(n) / 2), (n - 1 + mp.sqrt(5)) / 2)
        print("  n = %d: homoclinic limit Re %s, Im (n - 1 + sqrt5)/2 = %s" % (n, mp.nstr(lim[n][0], 6), mp.nstr(lim[n][1], 15)))
        worst = 0
        for k in range(21):
            c, r, A = highest_matrix(word(n, k))
            cu, Au = to_unit(c, A)
            ri, cr = highest_cf([n] + [1] * (2 * k + 1))
            worst = max(worst, abs(r - ri), abs(cu - cr))
            if k <= 5 or k % 5 == 0:
                print("    k = %2d: Im %s | %s, Re %s | %s; Im - limit %s" % (
                    k, mp.nstr(r, 15), mp.nstr(ri, 15), mp.nstr(cu, 15), mp.nstr(cr, 15), mp.nstr(r - lim[n][1], 5)))
        print("    the two methods differ by at most %s (Im and Re, k = 0..20)" % mp.nstr(worst, 3))

    print("\nD. EACH APPROXIMANT'S OWN ORDER-5 LINES AT ITS HIGHEST APEX (P4; B1733's rule, Re tau in [0, 1))")
    for n in (5, 6):
        seen = {}
        for k in range(21):
            c, r, A = highest_matrix(word(n, k))
            cu, Au = to_unit(c, A)
            o = own(Au)
            seen.setdefault(o, []).append(k)
            print("  n = %d, k = %2d: tr %d (mod 5: %d), Re %s, own order-5 lines %s" % (
                n, k, tr(Au), tr(Au) % 5, mp.nstr(cu, 6), fl(o)))
        print("  n = %d summary: %s" % (n, "; ".join("%s at k = %s" % (fl(o), ks) for o, ks in seen.items())))

    print("\nE. THE HOMOCLINIC HISTORY ...1,1,n,1,1... (P5): x- = -1/phi, x+ = n + 1/phi")
    gold = own(RL)
    for n in range(1, 13):
        xm, xp = -1 / PHI, n + 1 / PHI
        dig_p, dig_m = cf_digits(xp), cf_digits(-xm)
        Gin, Gout = RL, conj(pw(T, n), LR)
        fx = max(fixes(Gin, xm), fixes(Gout, xp))
        c0, rad = (xm + xp) / 2, (xp - xm) / 2
        m = int(mp.floor(c0 + EPS))
        c = c0 - m
        gin, gout = conj(pw(T, -m), Gin), conj(pw(T, -m), Gout)
        pin, pout = own(gin), own(gout)
        two_c = int(mp.nint(2 * c))
        r = mul(pw(T, two_c), J0)  # the reflection about Re tau = c in the apex marking
        refl_in = frozenset(pm(act(w, inv(r))) for w in pin)
        refl_out = frozenset(pm(act(w, inv(r))) for w in pout)
        rg = conj(r, gin)
        swaps = rg in (gout, inv(gout), neg(gout), neg(inv(gout)))
        stab = all(pm(act(w, inv(pw(T, n - 1)))) == w for w in gold)
        print("  n = %2d: cf(x+) %s, cf(-x-) %s, lifts fix the ends to %s; apex %s + %si; in %s, out %s, equal %s; "
              "T^(n-1) in the line's stabiliser %s; reflection maps in -> out %s, out -> in %s, r Gin r^-1 = Gout^+-1 %s, "
              "fixes the in pair %s" % (
                  n, dig_p[:6], dig_m[:6], mp.nstr(fx, 3), mp.nstr(c, 3), mp.nstr(rad, 15), fl(pin), fl(pout),
                  pin == pout, stab, refl_in == pout, refl_out == pin, swaps, refl_in == pin))

    print("\nF. THE DEPARTURE'S EXCESS LENGTH (P6): l(L^n R (LR)^k) - l((LR)^(k+1)) against 2 log((n - 1 + sqrt5)/sqrt5)")
    for n in (5, 6):
        target = 2 * mp.log((n - 1 + mp.sqrt(5)) / mp.sqrt(5))
        for k in (0, 5, 10, 20, 30):
            d = 2 * mp.acosh(mp.mpf(tr(prod(word(n, k)))) / 2) - 2 * mp.acosh(mp.mpf(tr(pw(LR, k + 1))) / 2)
            print("  n = %d, k = %2d: %s; target %s; difference %s" % (n, k, mp.nstr(d, 15), mp.nstr(target, 15),
                                                                       mp.nstr(d - target, 3)))
    print("\ndeparture_check exit 0")
