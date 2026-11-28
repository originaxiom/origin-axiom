#!/usr/bin/env python3
"""The web seat's peer check of queue card Q0025 (fam3-v1-high-03): a second computation in other code, by other means.

The card is a bundle. This script checks five of its parts and says which it leaves: the chiral index law for every
odd N and multiplier r, the flip-trace identity and its half-and-half split, the mod-4 mirror dichotomy over odd N up
to 35, the CRT and dilation equivalences at N = 15, and the Leg(5) intertwiner with its two Weil-triplet ratios. It
works in 50-digit floating point (mpmath) and integer arithmetic; it imports nothing of the producer's and reads no
file of theirs.

THE DEFINITIONS USED (the card's definitions field). N odd, inv2 = (N + 1)/2, zeta = exp(2 pi i/N), r a unit mod N.
  G_s = sum_b zeta^(-s inv2 b^2) (the card's G_r = G_{N, -r inv2}; G_{3r} is read in the same notation);
  L = diag(zeta^(r inv2 j^2)); S[a][c] = zeta^(r a c) / G_r; C3 = S^H L^H; (P_flip)[(-j) mod N][j] = 1;
  W+ = sum_{j=0..2} C3^j L C3^-j, W- = W+^H, W6 = W+ + W-; H_q = ker(C3 - omega^q), omega = exp(2 pi i/3);
  M_a = U_a K with U_a|j> = |a j mod N>, a^2 = -1 mod N, K complex conjugation.
  P^1(F_5) ordered l_1..l_6 = (1,0), (0,1), (1,1), (1,2), (1,3), (1,4); Leg(5): M e_j = (s/5) e_i when M l_j = s l_i
  mod 5 (column vectors); K_5 = sum of Leg(5)(g) over the class of [[1,1],[0,1]] in SL(2, F_5) (Leg(5)(-I) = I, so
  this is the card's class in PSL(2, F_5)); P_a = (K_5 - (2 - 2 sqrt 5)) / (4 sqrt 5),
  P_b = ((2 + 2 sqrt 5) - K_5) / (4 sqrt 5);
  v_i(tau) = (F(l_i/5; tau) - F(2 l_i/5; tau)) / sqrt 2 with F(a, b; tau) = wp(a tau + b; tau), the Weierstrass
  function, here computed as -d^2/dz^2 log theta_1(pi z | tau) (its additive constant cancels in v);
  R(tau) = ||P_b Leg(S) v||^2 / ||P_a Leg(S) v||^2 with S = [[0,-1],[1,0]].

THE CONDITION, written before any of this was run. The card holds where this seat checks it if and only if all of:
  D1. For every odd N in 3..99 and every unit r mod N: tr C3 = G_{3r} / conj(G_r), and tr C3 = Jacobi(-3/N) when
      3 does not divide N, = +i sqrt 3 (r/3) when 3 divides N, each within 1e-35.
  D2. For the same pairs, tr(P_flip C3) = 1 within 1e-35; and for odd N in 3..63, every unit r, the eigenvalue counts
      of C3 on the even and odd subspaces of P_flip are integers within 1e-30 and d1 - d2 splits into equal halves.
      (Printed, not judged: the scalar c with S^2 = c P_flip, beside (-1/N); the card's copy masks which symbol.)
  D3. For odd N in 3..35 at r = 1: the sectors q = 1, 2 of W6 have the same dimension and characteristic polynomial
      (coefficients within 1e-30) exactly for N in {5, 13, 17, 25, 29}; an a with a^2 = -1 mod N exists exactly for
      those N; and for each such N some such M_a commutes with W6 and with C3 (U_a conj(X) U_a^T = X, 1e-35).
  D4. With the CRT bijection j -> (j mod 3, j mod 5), rho_{15,1}(L) and rho_{15,1}(S) equal rho_{3,2} (x) rho_{5,2} of
      the same within 1e-35; and with U_2|j> = |2 j mod 15>, U_2 rho_{15,1}(X) U_2^T = rho_{15,4}(X) for X = L, S.
  D5. K_5's eigenvalues are 2 + 2 sqrt 5 and 2 - 2 sqrt 5, three each; P_a, P_b are complementary orthogonal
      projectors of rank 3 commuting with Leg(5); among the assignments L -> T^(+-1) or R^(+-1), S -> S^(+-1)
      (T = [[1,1],[0,1]], R = [[1,0],[1,1]]), at least one makes rho_{5,1} and rho_{5,2} homomorphisms of SL(2, F_5),
      and under every such assignment the character of Leg(5) equals the sum of the characters of rho_{5,2} and
      rho_{5,1} on their P_flip-even subspaces at all 120 elements, within 1e-30; R(exp(2 pi i/3)) = 1/4 and
      R(i) = 7/23 within 1e-30; and R takes the same value at tau, tau + 1 and -1/tau for tau = 0.3 + 1.1 i, within
      1e-25.
  Any one failing is a fault in the card as this seat reads it, or in this seat's reading; the note says which.

NOT CHECKED HERE: the exact cyclotomic proofs as such, the spinor-parity symbol (masked; printed only), the
O_27 x Weil_N and Q_6 x Weil_N freezing and moments, the Siegel ratio, the lattice Weil-theta forms on L_N and L'_15,
their chiral locking and the boundary-to-interior stabilization values, the discriminant-15 rank-2 duality, and the
card's controls.

    python3 relays/chat1_2026-11-28_peer/q0025_check.py            # the check; exits 0, prints the verdict
    python3 relays/chat1_2026-11-28_peer/q0025_check.py --control  # targets made wrong on purpose; exits 1
"""
import math
import sys

import mpmath as mp
import sympy as sp

CONTROL = "--control" in sys.argv
mp.mp.dps = 50
T35, T30 = mp.mpf("1e-35"), mp.mpf("1e-30")


def say(text):
    print("DECISIVE: " + text)


def zpow(N):
    return [mp.expjpi(mp.mpf(2 * k) / N) for k in range(N)]


def gauss(N, s, zp):
    inv2 = (N + 1) // 2
    return mp.fsum(zp[(-s * inv2 * b * b) % N] for b in range(N))


def weil(N, r):
    zp = zpow(N)
    inv2 = (N + 1) // 2
    G = gauss(N, r, zp)
    L = mp.diag([zp[(r * inv2 * j * j) % N] for j in range(N)])
    S = mp.matrix(N, N)
    for a in range(N):
        for c in range(N):
            S[a, c] = zp[(r * a * c) % N] / G
    return L, S


def mx(A):
    return max(abs(A[i, j]) for i in range(A.rows) for j in range(A.cols))


def legendre3(r):
    return {1: 1, 2: -1}[r % 3]


# ---------------------------------------------------------------- D1, D2: traces by closed sums
def d1_d2():
    ok1, ok2, worst1, worst2, pairs, parity = True, True, mp.mpf(0), mp.mpf(0), 0, []
    for N in range(3, 100, 2):
        zp = zpow(N)
        inv2 = (N + 1) // 2
        jac = sp.jacobi_symbol(-3 % N, N)
        if CONTROL and N == 7:
            jac = -jac          # wrong on purpose
        for r in range(1, N):
            if math.gcd(r, N) != 1:
                continue
            pairs += 1
            G = gauss(N, r, zp)
            cg = mp.conj(G)
            C = lambda a, b: zp[(-r * (a * b + inv2 * b * b)) % N] / cg   # C3[a][b]
            t1 = mp.fsum(C(a, a) for a in range(N))
            want = mp.mpc(0, mp.sqrt(3)) * legendre3(r) if N % 3 == 0 else mp.mpf(jac)
            e = max(abs(t1 - gauss(N, 3 * r, zp) / cg), abs(t1 - want))
            f1 = mp.fsum(C((-a) % N, a) for a in range(N))
            e2 = abs(f1 - 1)
            worst1, worst2 = max(worst1, e), max(worst2, e2)
            if e > T35:
                ok1 = False
            if e2 > T35:
                ok2 = False
            if N <= 63:
                t2 = mp.fsum(C(a, k) * C(k, a) for a in range(N) for k in range(N))
                f2 = mp.fsum(C((-a) % N, k) * C(k, a) for a in range(N) for k in range(N))
                om = mp.expjpi(mp.mpf(2) / 3)
                halves = []
                for sign in (1, -1):
                    tr = [(N + sign * 1) / mp.mpf(2), (t1 + sign * f1) / 2, (t2 + sign * f2) / 2]
                    d = [(tr[0] + om ** (-q) * tr[1] + om ** (-2 * q) * tr[2]) / 3 for q in range(3)]
                    di = [int(mp.nint(mp.re(x))) for x in d]
                    if max(abs(x - i) for x, i in zip(d, di)) > T30:
                        ok2 = False
                    halves.append(di[1] - di[2])
                if halves[0] != halves[1]:
                    ok2 = False
                if r == 1:
                    c = N / G ** 2
                    parity.append((N, int(mp.nint(mp.re(c))), int(sp.jacobi_symbol(N - 1, N))))
    say("D1 over %d pairs (N odd 3..99, r a unit): tr C3 = G_3r / conj(G_r) = the card's law, max error %s: %s"
        % (pairs, "below 1e-35" if worst1 <= T35 else mp.nstr(worst1, 3), ok1))
    say("D2 tr(P_flip C3) = 1 on all pairs, and d1 - d2 splits half and half on even and odd for N <= 63: %s" % ok2)
    agree = all(c == j for _, c, j in parity)
    print("  S^2 = c P_flip at r = 1: c equals (-1/N) for every odd N <= 63: %s" % agree)
    return ok1 and ok2


# ---------------------------------------------------------------- D3: the mirror dichotomy
def sectors(N, W6, C3):
    om = mp.expjpi(mp.mpf(2) / 3)
    I = mp.eye(N)
    C2 = C3 * C3
    out = []
    for q in range(3):
        Pq = (I + om ** (-q) * C3 + om ** (-2 * q) * C2) / 3
        basis = []
        for c in range(N):
            v = Pq[:, c]
            for _ in range(2):
                for b in basis:
                    v = v - (b.H * v)[0, 0] * b
            nv = mp.norm(v)
            if nv > mp.mpf("1e-20"):
                basis.append(v / nv)
        d = len(basis)
        if d == 0:
            out.append((0, [mp.mpf(1)]))
            continue
        B = mp.matrix(N, d)
        for i, b in enumerate(basis):
            for k in range(N):
                B[k, i] = b[k]
        M = B.H * W6 * B
        M = (M + M.H) / 2
        coef = [mp.mpc(1)]
        for lam in mp.eigh(M, eigvals_only=True):
            coef = [a - lam * b for a, b in zip(coef + [0], [0] + coef)]
        out.append((d, coef))
    return out


def d3():
    iso, roots_exist, commute = [], [], True
    for N in range(3, 36, 2):
        L, S = weil(N, 1)
        C3 = S.H * L.H
        Wp = mp.matrix(N, N)
        P = mp.eye(N)
        for _ in range(3):
            Wp += P * L * P.H
            P = P * C3
        W6 = Wp + Wp.H
        sec = sectors(N, W6, C3)
        (d1, c1), (d2, c2) = sec[1], sec[2]
        if d1 == d2 and max(abs(a - b) for a, b in zip(c1, c2)) <= T30:
            iso.append(N)
        aa = [a for a in range(N) if (a * a + 1) % N == 0]
        if aa:
            roots_exist.append(N)
            good = False
            for a in aa:
                U = mp.matrix(N, N)
                for j in range(N):
                    U[(a * j) % N, j] = 1
                cw = mp.matrix([[mp.conj(W6[i, j]) for j in range(N)] for i in range(N)])
                cc = mp.matrix([[mp.conj(C3[i, j]) for j in range(N)] for i in range(N)])
                if mx(U * cw * U.T - W6) <= T35 and mx(U * cc * U.T - C3) <= T35:
                    good = True
            commute = commute and good
        print("  N = %d: dims %s" % (N, [s[0] for s in sec]))
    want = [5, 13, 17, 25, 29] if not CONTROL else [5, 13, 17, 29]     # wrong on purpose in the control
    split = [N for N in range(3, 36, 2) if N not in iso]
    ok = iso == want and roots_exist == want and commute
    say("D3 iso-spectral N: %s; N with a^2 = -1: %s; split: %s; M_a commutes where it exists: %s; as the card says: %s"
        % (iso, roots_exist, split, commute, ok))
    return ok


# ---------------------------------------------------------------- D4: CRT and dilation at 15
def kron(A, B):
    n, m = A.rows, B.rows
    K = mp.matrix(n * m, n * m)
    for i in range(n):
        for j in range(n):
            for k in range(m):
                for l in range(m):
                    K[i * m + k, j * m + l] = A[i, j] * B[k, l]
    return K


def d4():
    L15, S15 = weil(15, 1)
    L3, S3 = weil(3, 2)
    L5, S5 = weil(5, 2)
    Pi = mp.matrix(15, 15)
    for j in range(15):
        Pi[(j % 3) * 5 + (j % 5), j] = 1
    e_crt = max(mx(Pi * L15 * Pi.T - kron(L3, L5)), mx(Pi * S15 * Pi.T - kron(S3, S5)))
    L4, S4 = weil(15, 4)
    U = mp.matrix(15, 15)
    for j in range(15):
        U[(2 * j) % 15, j] = 1
    e_dil = max(mx(U * L15 * U.T - L4), mx(U * S15 * U.T - S4))
    ok = e_crt <= T35 and e_dil <= T35
    say("D4 rho_15,1 = rho_3,2 (x) rho_5,2 under CRT and U_2 rho_15,1 U_2^T = rho_15,4, within 1e-35: %s" % ok)
    return ok


# ---------------------------------------------------------------- D5: Leg(5) and the Weil-triplet ratios
LINES = [(1, 0), (0, 1), (1, 1), (1, 2), (1, 3), (1, 4)]
SQ5 = {1: 1, 4: 1, 2: -1, 3: -1}


def leg(g):
    a, b, c, d = g
    M = mp.matrix(6, 6)
    for j, (x, y) in enumerate(LINES):
        X, Y = (a * x + b * y) % 5, (c * x + d * y) % 5
        for i, (u, v) in enumerate(LINES):
            for s in range(1, 5):
                if (s * u - X) % 5 == 0 and (s * v - Y) % 5 == 0:
                    M[i, j] = SQ5[s]
    return M


def mul(g, h):
    a, b, c, d = g
    e, f, g2, h2 = h
    return ((a * e + b * g2) % 5, (a * f + b * h2) % 5, (c * e + d * g2) % 5, (c * f + d * h2) % 5)


def inv(g):
    a, b, c, d = g
    return (d % 5, (-b) % 5, (-c) % 5, a % 5)


def group():
    return [(a, b, c, d) for a in range(5) for b in range(5) for c in range(5) for d in range(5)
            if (a * d - b * c) % 5 == 1]


def bfs(gens):
    """images of all of SL(2, F_5) under the assignment gens = {matrix tuple: image}; None if not a homomorphism"""
    one = (1, 0, 0, 1)
    some = next(iter(gens.values()))
    img = {one: mp.eye(some.rows)}
    frontier = [one]
    while frontier:
        new = []
        for g in frontier:
            for x, X in gens.items():
                h = mul(g, x)
                Hm = img[g] * X
                if h in img:
                    if mx(img[h] - Hm) > T30:
                        return None
                else:
                    img[h] = Hm
                    new.append(h)
        frontier = new
    return img if len(img) == 120 else None


def wp_shift(z, tau):
    q = mp.expjpi(tau)
    w = mp.pi * z
    t0, t1, t2 = (mp.jtheta(1, w, q, derivative=k) for k in range(3))
    return -mp.pi ** 2 * (t2 / t0 - (t1 / t0) ** 2)


def ratio(tau, Pa, Pb, LS):
    v = mp.matrix(6, 1)
    for i, (x, y) in enumerate(LINES):
        z1 = mp.mpf(x) / 5 * tau + mp.mpf(y) / 5
        z2 = 2 * z1
        v[i] = (wp_shift(z1, tau) - wp_shift(z2, tau)) / mp.sqrt(2)
    phi = LS * v
    nb = mp.fsum(abs(x) ** 2 for x in Pb * phi)
    na = mp.fsum(abs(x) ** 2 for x in Pa * phi)
    return nb / na


def d5():
    T, R, S = (1, 1, 0, 1), (1, 0, 1, 1), (0, 4, 1, 0)
    G = group()
    cls = {mul(mul(h, T), inv(h)) for h in G}
    K5 = mp.matrix(6, 6)
    for g in cls:
        K5 += leg(g)
    ev = sorted(mp.eig(K5)[0], key=lambda x: mp.re(x))
    s5 = mp.sqrt(5)
    ok_ev = len(cls) == 12 and all(abs(ev[i] - (2 - 2 * s5)) < T30 for i in range(3)) and \
        all(abs(ev[i] - (2 + 2 * s5)) < T30 for i in range(3, 6))
    I6 = mp.eye(6)
    Pa = (K5 - (2 - 2 * s5) * I6) / (4 * s5)
    Pb = ((2 + 2 * s5) * I6 - K5) / (4 * s5)
    LT, LSm = leg(T), leg(S)
    ok_pr = mx(Pa * Pa - Pa) < T30 and mx(Pb * Pb - Pb) < T30 and mx(Pa + Pb - I6) < T30 and \
        mx(Pa - Pa.H) < T30 and abs(sum(Pa[i, i] for i in range(6)) - 3) < T30 and \
        mx(Pa * LT - LT * Pa) < T30 and mx(Pa * LSm - LSm * Pa) < T30
    reps = {}
    for r in (1, 2):
        Lw, Sw = weil(5, r)
        reps[r] = (Lw, Sw)
    P5 = mp.matrix(5, 5)
    for j in range(5):
        P5[(-j) % 5, j] = 1
    even = (mp.eye(5) + P5) / 2
    Tinv, Rinv, Sinv = inv(T), inv(R), inv(S)
    good, assignments = True, []
    for lname, lt in (("T", T), ("T^-1", Tinv), ("R", R), ("R^-1", Rinv)):
        for sname, st in (("S", S), ("S^-1", Sinv)):
            imgs = {}
            for r in (1, 2):
                Lw, Sw = reps[r]
                imgs[r] = bfs({lt: Lw, st: Sw})
            if imgs[1] is None or imgs[2] is None:
                continue
            assignments.append(lname + ", " + sname)
            for g in G:
                lhs = sum(leg(g)[i, i] for i in range(6))
                rhs = mp.fsum((even * imgs[r][g])[i, i] for r in (1, 2) for i in range(5))
                if abs(lhs - rhs) > T30:
                    good = False
    ok_ch = bool(assignments) and good
    want_w, want_i = (mp.mpf(1) / 4, mp.mpf(7) / 23) if not CONTROL else (mp.mpf(1) / 5, mp.mpf(7) / 23)
    rw = ratio(mp.expjpi(mp.mpf(2) / 3), Pa, Pb, LSm)
    ri = ratio(mp.mpc(0, 1), Pa, Pb, LSm)
    t0 = mp.mpc("0.3", "1.1")
    r0, r1, r2 = ratio(t0, Pa, Pb, LSm), ratio(t0 + 1, Pa, Pb, LSm), ratio(-1 / t0, Pa, Pb, LSm)
    ok_r = abs(rw - want_w) < T30 and abs(ri - want_i) < T30
    ok_inv = abs(r0 - r1) < mp.mpf("1e-25") and abs(r0 - r2) < mp.mpf("1e-25")
    print("  R(exp(2 pi i/3)) = %s, R(i) = %s, R at 0.3 + 1.1i, +1, -1/tau: %s %s %s"
          % (mp.nstr(rw, 20), mp.nstr(ri, 20), mp.nstr(r0, 15), mp.nstr(r1, 15), mp.nstr(r2, 15)))
    say("D5 K_5 class of 12 with eigenvalues 2 -+ 2 sqrt 5 three each: %s; P_a, P_b projectors commuting with "
        "Leg(5): %s" % (ok_ev, ok_pr))
    say("D5 homomorphic assignments %s; Leg(5) character = even rho_5,2 + even rho_5,1 at all 120 elements: %s"
        % (assignments, ok_ch))
    say("D5 R(omega_+) = 1/4 and R(i) = 7/23 within 1e-30: %s; R invariant under tau + 1 and -1/tau: %s"
        % (ok_r, ok_inv))
    return ok_ev and ok_pr and ok_ch and ok_r and ok_inv


def main():
    a = d1_d2()
    b = d3()
    c = d4()
    d = d5()
    verdict = a and b and c and d
    if CONTROL:
        print("CONTROL: the checks %s the targets made wrong on purpose" % ("caught" if not verdict else "MISSED"))
        return 1 if not verdict else 0
    say("VERDICT: the card holds where this seat checks it (D1-D5): %s" % verdict)
    return 0


if __name__ == "__main__":
    sys.exit(main())
