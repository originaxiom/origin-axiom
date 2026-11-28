#!/usr/bin/env python3
"""The web seat's peer check of queue card Q0029 (fam3-v1-high-01): a second computation in other code, by other means.

The card states, among other things: the non-commutative two-counts Weil register on C^N (odd N, multiplier
r = 1), its six-move walk W6 = W+ + W-, the sector dimensions and characteristic polynomials of W6 on the eigenspaces
H_q of the order-3 charge C3, the mod-4 pairing of the sectors q = 1, 2 over the primes 3..23, the chiral index on
N = 3^k, the Markoff-tree Jacobian cubic of the trace walk, the Silver shapes and V(LLRR) = 4 Catalan, the Bronze trace
quartic, and the settling of the excess-volume step ratio on five (H, P) pairs. The card computes in exact cyclotomic
fields and a lex Groebner basis. This script does not: it works in 50- and 80-digit floating point (mpmath), finds the
sector spectra by Gram-Schmidt and Hermitian eigenvalues, finds fixed points and closed orbits by Newton from seeded
random starts, and checks the polynomial identities in sympy. It imports nothing of the producer's and reads no file of
theirs.

THE DEFINITIONS USED (read from the card's definitions field). N odd, inv2 = (N + 1)/2, zeta = exp(2 pi i/N), r = 1.
  L = diag(zeta^(inv2 j^2)); G = sum_b zeta^(-inv2 b^2); S[a][c] = zeta^(a c) / G; R = S L^+ S^+; Cw = L R^+;
  C3 = S^+ L^+; W+ = sum_{j=0..2} Cw^j L Cw^-j; W- = sum_{j=0..2} Cw^j R Cw^-j; W6 = W+ + W-.
  The card masks the bounds of the sums in the copy this seat reads; j = 0..2 is this seat's reading, and the card's own
  closed-form polynomials (C4) test it. H_q = ker(C3 - omega^q), omega = exp(2 pi i/3), d_q = dim H_q,
  P_{N,q}(x) = det(x - W6 on H_q).
  Trace walk on C^3: L(x,y,z) = (x, z, xz - y), R(x,y,z) = (z, y, yz - x), C(x,y,z) = (y, z, x),
  W6tr = sum_{j=0..2} C^j (L + R) C^-j, J = its Jacobian. Chart (u, v) = (x/z, y/z) on x^2 + y^2 + z^2 = xyz:
  F_L(u,v) = (u/(v^2+1), uv/(v^2+1)), shape v^2/(v^2+1); F_R(u,v) = (uv/(u^2+1), v/(u^2+1)), shape 1/(u^2+1).
  A word c_1..c_n acts right to left; its closed orbit z_0..z_{n-1} has shapes w_j, and V = sum_j D(w_j) with
  D(w) = Im Li2(w) + arg(1 - w) log|w|. "Geometric" here means every shape has positive imaginary part.

THE CONDITION, written before any of this was run. The card holds where this seat checks it if and only if all of:
  C1. For N in {3,5,7,9,11,13,15,17,19,23,27}: X Z = zeta Z X, S S^+ = I, L S L = S L^+ S, C3^3 = I, [W+, W-] = 0,
      [W6, C3] = 0 and W- = W+^+, each with max entry residual <= 1e-30.
  C2. Over the primes p in {3,...,23}, the set with d1 = d2 and P_{p,1} = P_{p,2} (coefficients within 1e-30) is exactly
      {5, 13, 17}; the rest, {3, 7, 11, 19, 23}, split.
  C3. For N = 3^k, k = 1..5: tr C3 = +i sqrt 3 within 1e-30, and (d0, d1, d2) = (3^(k-1), 3^(k-1) + 1, 3^(k-1) - 1).
  C4. The card's 18 closed-form sector polynomials at N in {3,5,7,9,15,27}: each sector's dimension is the polynomial's
      degree and its characteristic polynomial matches coefficient by coefficient within 1e-30.
  C5. Symbolically: det(t - J) = (t - 2)(t - 2 - (x+y+z))^2 - 4xyz identically; with D = diag(sqrt x, sqrt y, sqrt z),
      the matrix D^-1 (J - 2) D, or failing that its symmetric part, is the matrix of the card's three-square form; the
      cubic's critical value at t = 2 + (x+y+z)/3 is (4/27)((x+y+z)^3 - 27xyz).
  C6. The Vieta-flip tree from (3,3,3), sorted triples to depth 7 with the root at depth 0, has 65 triples, all on
      a^2 + b^2 + c^2 = abc, and (3,3,3) is the only one where the Jacobian has fewer than 3 distinct eigenvalues.
  C7. LLRR has exactly one geometric shape sequence, it is (1+i, (1+i)/2, i, (1+i)/2) within 1e-40, and
      |V(LLRR) - 4 Catalan| < 1e-36. (Not judged, printed: V(LR) and the chart trace of the geometric fixed point of LR,
      LLRR and LLLRRR, which the card's lambda_+ values imply are 5, 18 and u_max.)
  C8. The quartic u^4 - 114u^3 + 4264u^2 - 58910u + 192359 is irreducible over Q with exactly one real root in (54, 55);
      every root of the card's fac_8 is the z of a fixed point of F_{LLLRRR} found in the chart off the curve
      u^2 + v^2 + 1 = 0 (the blown-up origin); at each such point the chart trace u = lambda + 1/lambda is a root of the
      quartic within 1e-30 (relative); all four roots are attained; the geometric fixed point has u = u_max.
  C9. With V taken on the geometric orbit of H P^k, the ratio (dV_{k-1} - dV_{k-2}) / (dV_k - dV_{k-1}), whose terms are
      V(H P^j) - V(H P^(j-1)) - V(P), is within 1e-7 of lambda_+ at k = 12 for H in {LLLLLLR, LLRRLLR, LLLRRRRLLLR} on
      P = LR (lambda_+ = (5 + sqrt 21)/2), at k = 9 for LLLR on LLRR (9 + 4 sqrt 5), and at k = 8 for LLLLRR on LLLRRR
      ((u_max + sqrt(u_max^2 - 4))/2).
  Any one failing is a fault in the card as this seat reads it, or in this seat's reading; the note says which.

THE FIRST RUN, AND WHAT CHANGED AFTER IT (post hoc in method; the condition above is unchanged). The first run, at
commit b4aff7623 (its output is q0029_out_run1.txt), passed C1 to C6 and stopped at C7: its random Newton search
found no geometric fixed point of LLLRRR. That is the search, not the card: nearly every start falls to the chart's
origin, a super-attracting fixed point, and the geometric orbits of C9's long words are harder still. Two searches were
changed, and nothing that judges:
  - geometric orbits (C7, C9) are now also started from chart points made from two shapes of SnapPy's solution of the
    same bundle (q0029_seeds.py, run once, its output q0029_seeds.json beside this script), then solved by this
    script's own Newton at 80 digits and kept only if every shape has positive imaginary part. C9 now takes the orbit of
    H P^k at k = K - 2, K - 1, K directly, with no continuation in k. SnapPy's volumes are printed beside this seat's,
    not judged.
  - C8's fixed points over the roots of fac_8 are now found in the trace coordinates, with z held at the root and
    Newton in (x, y) from starts on the surface; each is then carried to the chart, (u, v) = (x/z, y/z), and must be a
    chart fixed point off the blown-up origin there, with the chart trace equal to tr(DT) - 1, as C8 asks.

NOT CHECKED HERE: exactness in the cyclotomic fields as such, the invariance of Omega, the outward ray limit, the
factored polynomials cp_336 and cp_3615, the card's b_0 offsets and selection inequalities (printed, not judged), and
its control and float counts.

    python3 relays/chat1_2026-11-28_peer/q0029_check.py            # the check; exits 0, prints the verdict
    python3 relays/chat1_2026-11-28_peer/q0029_check.py --control  # targets made wrong on purpose; exits 1
"""
import json
import pathlib
import random
import sys

import mpmath as mp
import sympy as sp

CONTROL = "--control" in sys.argv
TOL = mp.mpf("1e-30")
OUT = []


def say(tag, text):
    line = ("DECISIVE: " if tag else "") + text
    OUT.append(line)
    print(line)


# ---------------------------------------------------------------- the Weil register, numerically at 50 digits
def weil(N):
    mp.mp.dps = 50
    zp = [mp.expjpi(mp.mpf(2 * k) / N) for k in range(N)]
    inv2 = (N + 1) // 2
    I = mp.eye(N)
    L = mp.diag([zp[(inv2 * j * j) % N] for j in range(N)])
    G = mp.fsum(zp[(-inv2 * b * b) % N] for b in range(N))
    S = mp.matrix(N, N)
    for a in range(N):
        for c in range(N):
            S[a, c] = zp[(a * c) % N] / G
    R = S * L.H * S.H
    Cw = L * R.H
    C3 = S.H * L.H
    Wp, Wm, P = mp.matrix(N, N), mp.matrix(N, N), mp.eye(N)
    for _ in range(3):
        Wp += P * L * P.H
        Wm += P * R * P.H
        P = P * Cw
    W6 = Wp + Wm
    X = mp.matrix(N, N)
    for j in range(N):
        X[j, (j + 1) % N] = 1
    Z = mp.diag([zp[j % N] for j in range(N)])
    res = {
        "XZ": X * Z - zp[1] * Z * X, "SS": S * S.H - I, "LSL": L * S * L - S * L.H * S,
        "C3^3": C3 * C3 * C3 - I, "[W+,W-]": Wp * Wm - Wm * Wp, "[W6,C3]": W6 * C3 - C3 * W6, "W-=W+^+": Wm - Wp.H}
    res = {k: max(abs(v[i, j]) for i in range(N) for j in range(N)) for k, v in res.items()}
    return W6, C3, res


def sectors(N, W6, C3):
    """(d_q, char poly coefficients high to low) for q = 0, 1, 2"""
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
            for r in range(N):
                B[r, i] = b[r]
        M = B.H * W6 * B
        M = (M + M.H) / 2
        ev = mp.eigh(M, eigvals_only=True)
        coef = [mp.mpc(1)]
        for lam in ev:
            coef = [a - lam * b for a, b in zip(coef + [0], [0] + coef)]
        out.append((d, coef))
    return out


def coeffs(expr):
    x = sp.Symbol("x")
    p = sp.Poly(sp.expand(expr), x)
    return [mp.mpf(str(sp.N(c, 60))) for c in p.all_coeffs()]


def closeco(a, b):
    return len(a) == len(b) and max(abs(u - v) for u, v in zip(a, b)) <= TOL


def targets():
    x = sp.Symbol("x")
    s5, s21 = sp.sqrt(5), sp.sqrt(21)
    T = {
        3: [x, x**2 - 9, sp.Integer(1)],
        5: [x + 2 * s5, (x - (3 - s5) / 2) * (x + (3 + 3 * s5) / 2), (x - (3 - s5) / 2) * (x + (3 + 3 * s5) / 2)],
        7: [x**2 * (x + 4), x**2 - 2 * x + (-9 + s21) / 2, x**2 - 2 * x + (-9 - s21) / 2],
        9: [x * (x - 4) * (x - 6), (x**2 - x - 3) * (x**2 - 3 * x - 9), (x - 1) * (x - 3)],
        15: [x**3 * (x - s5 + 1) * (x + s5 + 3),
             (x - (3 + s5) / 2) * (x - (3 - 3 * s5) / 2) * (x**2 - (21 - 3 * s5) / 2)
             * (x**2 + (1 - s5) * x - (3 + 3 * s5) / 2),
             (x + s5) * (x - (1 - s5) / 2) * (x**2 - ((3 + 3 * s5) / 2) * x - (3 - 3 * s5) / 2)],
        27: [x**5 * (x**4 - 24 * x**2 - 16 * x + 48),
             x**2 * (x**8 - 30 * x**6 - 10 * x**5 + 300 * x**4 + 126 * x**3 - 1179 * x**2 - 324 * x + 1620),
             x**8 - 27 * x**6 + 14 * x**5 + 174 * x**4 - 180 * x**3 - 171 * x**2 + 270 * x - 81]}
    if CONTROL:   # wrong on purpose: P_{7,1} given the sign of P_{7,2}'s root
        T[7][1] = x**2 - 2 * x + (-9 - s21) / 2
    return T


def weil_checks():
    mp.mp.dps = 50
    Ns = [3, 5, 7, 9, 11, 13, 15, 17, 19, 23, 27]
    T = targets()
    worst, sec = mp.mpf(0), {}
    for N in Ns:
        W6, C3, res = weil(N)
        worst = max([worst] + list(res.values()))
        sec[N] = sectors(N, W6, C3)
        print("  N = %d: dims %s, max residual %s" % (N, [s[0] for s in sec[N]], mp.nstr(max(res.values()), 3)))
    c1 = worst <= TOL
    say(True, "C1 Weil relations and commutators hold for N in %s with max residual <= 1e-30: %s" % (Ns, c1))
    primes = [3, 5, 7, 11, 13, 17, 19, 23]
    paired = [p for p in primes if sec[p][1][0] == sec[p][2][0] and closeco(sec[p][1][1], sec[p][2][1])]
    split = [p for p in primes if p not in paired]
    c2 = paired == [5, 13, 17] and split == [3, 7, 11, 19, 23]
    say(True, "C2 primes with paired sectors q = 1, 2: %s; split: %s; as the card says: %s" % (paired, split, c2))
    ok4, bad4 = True, []
    for N, polys in T.items():
        for q in range(3):
            want = coeffs(polys[q])
            d, got = sec[N][q]
            good = d == len(want) - 1 and closeco([mp.re(g) for g in got], want) and \
                max([abs(mp.im(g)) for g in got]) <= TOL
            if not good:
                ok4 = False
                bad4.append((N, q))
    say(True, "C4 the 18 closed-form sector polynomials match in degree and coefficients within 1e-30: %s%s"
        % (ok4, "" if ok4 else " (failing (N, q): %s)" % bad4))
    return c1 and c2 and ok4


def index_checks():
    mp.mp.dps = 50
    ok, dims = True, []
    om = mp.expjpi(mp.mpf(2) / 3)
    for k in range(1, 6):
        N = 3 ** k
        zp = [mp.expjpi(mp.mpf(2 * m) / N) for m in range(N)]
        inv2 = (N + 1) // 2
        G = mp.fsum(zp[(-inv2 * b * b) % N] for b in range(N))
        cg = mp.conj(G)
        t1 = mp.fsum(zp[(-(1 + inv2) * a * a) % N] for a in range(N)) / cg
        t2 = mp.fsum(zp[(-(2 * a * b + inv2 * (a * a + b * b))) % N] for a in range(N) for b in range(N)) / cg ** 2
        ds = [(N + om ** (-q) * t1 + om ** (-2 * q) * t2) / 3 for q in range(3)]
        di = [int(mp.nint(mp.re(d))) for d in ds]
        intok = max(abs(d - i) for d, i in zip(ds, di)) <= TOL
        want = [3 ** (k - 1), 3 ** (k - 1) + 1, 3 ** (k - 1) - 1]
        good = abs(t1 - mp.mpc(0, mp.sqrt(3))) <= TOL and intok and di == want
        ok = ok and good
        dims.append(di)
    say(True, "C3 on N = 3^k, k = 1..5: tr C3 = +i sqrt 3 and dims (3^(k-1), 3^(k-1)+1, 3^(k-1)-1): %s; dims %s"
        % (ok, dims))
    return ok


# ---------------------------------------------------------------- the trace walk's Jacobian, symbolically
def jacobian_checks():
    x, y, z, t = sp.symbols("x y z t", positive=True)

    def Lm(v):
        return (v[0], v[2], v[0] * v[2] - v[1])

    def Rm(v):
        return (v[2], v[1], v[1] * v[2] - v[0])

    def C(v, j):
        for _ in range(j % 3):
            v = (v[1], v[2], v[0])
        return v

    v0 = (x, y, z)
    W = [0, 0, 0]
    for j in range(3):
        u = C(v0, -j)
        a, b = C(Lm(u), j), C(Rm(u), j)
        W = [W[i] + a[i] + b[i] for i in range(3)]
    J = sp.Matrix(W).jacobian([x, y, z])
    s = x + y + z
    cub = (t - 2) * (t - 2 - s) ** 2 - 4 * x * y * z
    ok_det = sp.expand((t * sp.eye(3) - J).det() - cub) == 0
    D = sp.diag(sp.sqrt(x), sp.sqrt(y), sp.sqrt(z))
    M = D.inv() * (J - 2 * sp.eye(3)) * D
    A = sp.Matrix([[y + z, sp.sqrt(x * y), sp.sqrt(x * z)], [sp.sqrt(x * y), x + z, sp.sqrt(y * z)],
                   [sp.sqrt(x * z), sp.sqrt(y * z), x + y]])
    m_eq = sp.simplify(M - A) == sp.zeros(3, 3)
    sym_eq = sp.simplify((M + M.T) / 2 - A) == sp.zeros(3, 3)
    t0 = 2 + s / 3
    ok_peak = sp.expand(cub.subs(t, t0) - sp.Rational(4, 27) * (s ** 3 - 27 * x * y * z)) == 0 and \
        sp.expand(sp.diff(cub, t).subs(t, t0)) == 0
    c5 = ok_det and (m_eq or sym_eq) and ok_peak
    say(True, "C5 det(t - J) is the card's cubic: %s; D^-1 (J - 2) D is the three-square matrix: %s (its symmetric "
              "part: %s); critical value (4/27)(s^3 - 27xyz): %s" % (ok_det, m_eq, sym_eq, ok_peak))
    # the tree
    level, seen, depth = {(3, 3, 3)}, {(3, 3, 3)}, 0
    while depth < 7:
        new = set()
        for (a, b, c) in level:
            for tr in ((b * c - a, b, c), (a, a * c - b, c), (a, b, a * b - c)):
                st = tuple(sorted(tr))
                if st not in seen:
                    seen.add(st)
                    new.add(st)
        level, depth = new, depth + 1
    onS = all(a * a + b * b + c * c == a * b * c for (a, b, c) in seen)
    degen = []
    for (a, b, c) in sorted(seen):
        g = sp.Poly(cub.subs({x: a, y: b, z: c}), t)
        if sp.discriminant(g) == 0:
            degen.append([a, b, c])
    want = 64 if CONTROL else 65     # wrong on purpose in the control
    c6 = len(seen) == want and onS and degen == [[3, 3, 3]]
    say(True, "C6 tree to depth 7: %d sorted triples, all on the surface: %s; degenerate: %s; as the card says: %s"
        % (len(seen), onS, degen, c6))
    return c5 and c6


# ---------------------------------------------------------------- closed orbits in the chart, at 80 digits
def run(word, u, v):
    J = [[mp.mpf(1), mp.mpf(0)], [mp.mpf(0), mp.mpf(1)]]
    ws = []
    for c in reversed(word):
        if c == "L":
            a = v * v + 1
            w, nu, nv = v * v / a, u / a, u * v / a
            Jc = [[1 / a, -2 * u * v / a ** 2], [v / a, u * (1 - v * v) / a ** 2]]
        else:
            b = u * u + 1
            w, nu, nv = 1 / b, u * v / b, v / b
            Jc = [[v * (1 - u * u) / b ** 2, u / b], [-2 * u * v / b ** 2, 1 / b]]
        J = [[Jc[0][0] * J[0][0] + Jc[0][1] * J[1][0], Jc[0][0] * J[0][1] + Jc[0][1] * J[1][1]],
             [Jc[1][0] * J[0][0] + Jc[1][1] * J[1][0], Jc[1][0] * J[0][1] + Jc[1][1] * J[1][1]]]
        ws.append(w)
        u, v = nu, nv
    return u, v, ws, J


def newton(word, u, v, its=120, fast=False):
    """Newton for F_word(z) = z; fast=True works in Python complex (the search), else in mpmath (the polish)"""
    one = 1 if fast else mp.mpf(1)
    tol = 1e-11 if fast else mp.mpf(10) ** (-(mp.mp.dps - 20))
    extra = 0
    for _ in range(its):
        try:
            fu, fv, _, J = (run_c if fast else run)(word, u, v)
        except (ZeroDivisionError, OverflowError):
            return None
        gu, gv = fu - u, fv - v
        if abs(gu) + abs(gv) < tol:
            extra += 1
            if fast or extra > 2:
                return u, v
        a, b, c, d = J[0][0] - one, J[0][1], J[1][0], J[1][1] - one
        det = a * d - b * c
        if det == 0:
            return None
        du, dv = (-gu * d + gv * b) / det, (gu * c - gv * a) / det
        size = abs(du) + abs(dv)
        cap = (1 + abs(u) + abs(v)) / 2
        if size > cap:
            du, dv = du * cap / size, dv * cap / size
        u, v = u + du, v + dv
        if abs(u) > 1e6 or abs(v) > 1e6:
            return None
    return None


def run_c(word, u, v):
    """run() in Python complex, for the search only"""
    J = [[1, 0], [0, 1]]
    for c in reversed(word):
        if c == "L":
            a = v * v + 1
            nu, nv = u / a, u * v / a
            Jc = [[1 / a, -2 * u * v / a ** 2], [v / a, u * (1 - v * v) / a ** 2]]
        else:
            b = u * u + 1
            nu, nv = u * v / b, v / b
            Jc = [[v * (1 - u * u) / b ** 2, u / b], [-2 * u * v / b ** 2, 1 / b]]
        J = [[Jc[0][0] * J[0][0] + Jc[0][1] * J[1][0], Jc[0][0] * J[0][1] + Jc[0][1] * J[1][1]],
             [Jc[1][0] * J[0][0] + Jc[1][1] * J[1][0], Jc[1][0] * J[0][1] + Jc[1][1] * J[1][1]]]
        u, v = nu, nv
    return u, v, None, J


def D(w):
    return mp.im(mp.polylog(2, w)) + mp.arg(1 - w) * mp.log(abs(w))


def fixed_points(word, starts, seed):
    """search in double precision from seeded random starts, then polish each hit in mpmath"""
    rng = random.Random(seed)
    pts = []
    for _ in range(starts):
        u0 = complex(rng.uniform(-2.5, 2.5), rng.uniform(-2.5, 2.5))
        v0 = complex(rng.uniform(-2.5, 2.5), rng.uniform(-2.5, 2.5))
        r = newton(word, u0, v0, its=200, fast=True)
        if r is None:
            continue
        r = newton(word, mp.mpc(r[0]), mp.mpc(r[1]), its=40)
        if r is None:
            continue
        u, v = r
        if abs(u) < 1e-20 or abs(v) < 1e-20:
            continue
        if all(abs(u - a) + abs(v - b) > mp.mpf("1e-25") for a, b in pts):
            pts.append((u, v))
    return pts


def geometric(word, pts):
    seqs = []
    for u, v in pts:
        _, _, ws, J = run(word, u, v)
        if all(mp.im(w) > 0 for w in ws):
            key = tuple(mp.nstr(w, 30) for w in ws)
            if key not in [k for k, _ in seqs]:
                seqs.append((key, (u, v, ws, J[0][0] + J[1][1])))
    return seqs


SEEDS = None


def seeds():
    """the starting points q0029_seeds.py wrote beside this script (SnapPy's shapes); see that script"""
    global SEEDS
    if SEEDS is None:
        SEEDS = json.loads(pathlib.Path(__file__).with_name("q0029_seeds.json").read_text(encoding="utf-8"))["words"]
    return SEEDS


def rots(s):
    return [s, 1 / (1 - s), 1 - 1 / s]


def seeded(word):
    """the geometric orbit of a word by this seat's Newton, started at chart points made from two seed shapes"""
    S = [mp.mpc(*x.split()) for x in seeds()[word]["shapes"]]
    n = len(S)
    c0, c1 = word[-1], word[-2]
    pairs = [(1 % n, 2 % n)] + [(a, (a + 1) % n) for a in range(n)]
    for a, b in pairs:
        for w0 in rots(S[a]):
            for w1 in rots(S[b]):
                for s0 in (1, -1):
                    for s1 in (1, -1):
                        if c0 == "R":
                            u0 = s0 * mp.sqrt((1 - w0) / w0)
                            v0 = s1 * (mp.sqrt((1 - w1) / w1) / (u0 * w0) if c1 == "R" else mp.sqrt(w1 / (1 - w1)) / w0)
                        else:
                            v0 = s0 * mp.sqrt(w0 / (1 - w0))
                            u0 = s1 * (mp.sqrt((1 - w1) / w1) / (1 - w0) if c1 == "R"
                                       else mp.sqrt(w1 / (1 - w1)) / (v0 * (1 - w0)))
                        r = newton(word, u0, v0, its=60)
                        if r is not None:
                            g = geometric(word, [r])
                            if g:
                                return g
    return []


def merge(a, b):
    keys = [k for k, _ in a]
    return a + [(k, x) for k, x in b if k not in keys]


def T3(p, fixed_z=True):
    """T_1^3 o T_2^3 on C^3 and its Jacobian (T_2 applied first)"""
    x, y, z = p
    J = mp.eye(3)
    for _ in range(3):
        J = mp.matrix([[1, 0, 0], [0, 0, 1], [z, -1, x]]) * J
        x, y, z = x, z, x * z - y
    for _ in range(3):
        J = mp.matrix([[0, 0, 1], [0, 1, 0], [-1, z, y]]) * J
        x, y, z = z, y, y * z - x
    return (x, y, z), J


def xyz_fixed(zi, starts, rng):
    """fixed points of T_1^3 T_2^3 on x^2 + y^2 + z^2 = xyz with z = zi: Newton in (x, y) on the first two components,
    from starts put on the surface; kept when the third component and the surface hold too"""
    found = []
    for _ in range(starts):
        x = mp.exp(mp.mpc(rng.uniform(-2, 2), rng.uniform(0, 6.283185307179586)))
        y = (x * zi + rng.choice((1, -1)) * mp.sqrt((x * zi) ** 2 - 4 * (x * x + zi * zi))) / 2
        for _ in range(80):
            (X, Y, Z), J = T3((x, y, zi))
            g1, g2 = X - x, Y - y
            if abs(g1) + abs(g2) < mp.mpf(10) ** (-(mp.mp.dps - 25)) * (1 + abs(x) + abs(y)):
                break
            a, b, c, d = J[0, 0] - 1, J[0, 1], J[1, 0], J[1, 1] - 1
            det = a * d - b * c
            if det == 0:
                break
            dx, dy = (-g1 * d + g2 * b) / det, (g1 * c - g2 * a) / det
            size = abs(dx) + abs(dy)
            cap = (1 + abs(x) + abs(y)) / 2
            if size > cap:
                dx, dy = dx * cap / size, dy * cap / size
            x, y = x + dx, y + dy
            if abs(x) > 1e5 or abs(y) > 1e5:
                break
        (X, Y, Z), J = T3((x, y, zi))
        tol = mp.mpf("1e-40")
        if abs(X - x) + abs(Y - y) + abs(Z - zi) < tol and abs(x * x + y * y + zi * zi - x * y * zi) < tol:
            if all(abs(x - a) + abs(y - b) > mp.mpf("1e-20") for a, b, _ in found):
                found.append((x, y, J[0, 0] + J[1, 1] + J[2, 2] - 1))
        if found:
            break
    return found


def volume_checks():
    mp.mp.dps = 80
    G = mp.catalan
    out = {}
    for P, seed in (("LR", 1), ("LLRR", 2), ("LLLRRR", 3)):
        g = merge(geometric(P, fixed_points(P, 400, 20261128 + seed)), seeded(P))
        out[P] = g
        if not g:
            say(True, "C7 no geometric fixed point found for %s" % P)
            return False, False, None, out
        for key, (u, v, ws, tr) in g:
            print("  %s geometric: V = %s (SnapPy %s), chart trace %s"
                  % (P, mp.nstr(mp.fsum(D(w) for w in ws), 20), seeds()[P]["volume"][:22], mp.nstr(tr, 20)))
    say(False, "V(LR) and the chart trace at its geometric fixed point: %s, %s" % (
        mp.nstr(mp.fsum(D(w) for w in out["LR"][0][1][2]), 15), mp.nstr(mp.re(out["LR"][0][1][3]), 15)))
    say(False, "chart trace at LLRR's geometric fixed point: %s" % mp.nstr(mp.re(out["LLRR"][0][1][3]), 15))
    sil = out["LLRR"]
    want = [mp.mpc(1, 1), mp.mpc(0.5, 0.5), mp.mpc(0, 1), mp.mpc(0.5, 0.5)]
    c7 = len(sil) == 1 and max(abs(a - b) for a, b in zip(sil[0][1][2], want)) < mp.mpf("1e-40") and \
        abs(mp.fsum(D(w) for w in sil[0][1][2]) - 4 * G) < mp.mpf("1e-36")
    say(True, "C7 LLRR has %d geometric shape sequence(s); it is (1+i, (1+i)/2, i, (1+i)/2) and V = 4 Catalan: %s"
        % (len(sil), c7))
    # the Bronze quartic
    u = sp.Symbol("u")
    quart = [1, -114, 4264, -58910, 192359 + (1 if CONTROL else 0)]   # wrong on purpose in the control
    qpoly = sp.Poly(quart, u)
    irr = qpoly.is_irreducible
    real = [r for r in sp.Poly(quart, u).real_roots() if 54 < r < 55]
    nreal = len(real)
    qroots = mp.polyroots([mp.mpf(c) for c in quart], maxsteps=200, extraprec=200)
    umax = [r for r in qroots if abs(mp.im(r)) < 1e-40 and 54 < mp.re(r) < 55]
    fac8 = [1, -1, 6, -5, 21, 15, 7, -3, 3]
    zr = mp.polyroots(fac8, maxsteps=200, extraprec=200)
    rng = random.Random(20261131)
    rows = []
    for zi in zr:
        for x, y, tr3 in xyz_fixed(zi, 600, rng):
            a, b = x / zi, y / zi           # the chart point
            fa, fb, ws, J = run("LLLRRR", a, b)
            chart_ok = abs(fa - a) + abs(fb - b) < mp.mpf("1e-35") and abs(a * a + b * b + 1) > mp.mpf("1e-20")
            tr = J[0][0] + J[1][1]
            rows.append((zi, tr, chart_ok and abs(tr - tr3) < mp.mpf("1e-30")))
    scale = lambda x: mp.fsum(abs(c) * abs(x) ** (4 - i) for i, c in enumerate(quart))
    zhit = [any(abs(zz - r) < mp.mpf("1e-30") and ok for zz, _, ok in rows) for r in zr]
    trroot = all(abs(mp.polyval([mp.mpf(c) for c in quart], tr)) / scale(tr) < TOL for _, tr, _ in rows)
    hit = [any(abs(tr - r) < mp.mpf("1e-25") for _, tr, _ in rows) for r in qroots]
    geo = [x[1][3] for x in out["LLLRRR"]]
    geo_ok = len(umax) == 1 and len(geo) == 1 and abs(geo[0] - umax[0]) < mp.mpf("1e-25")
    c8 = bool(irr) and nreal == 1 and all(zhit) and trroot and all(hit) and geo_ok
    print("  LLLRRR: chart traces at the fixed points over fac_8's roots: %s"
          % [mp.nstr(tr, 10) for _, tr, _ in rows])
    say(True, "C8 quartic irreducible: %s; one real root in (54, 55): %s; fac_8 roots reached as fixed points: "
              "%d of 8; their traces are quartic roots: %s; roots attained: %d of 4; geometric trace is u_max: %s; "
              "C8 holds: %s"
        % (bool(irr), nreal == 1, sum(zhit), trroot, sum(hit), geo_ok, c8))
    if umax:
        say(False, "u_max = %s" % mp.nstr(mp.re(umax[0]), 20))
    return c7, c8, (mp.re(umax[0]) if umax else None), out


def ratio_checks(umax, geo):
    mp.mp.dps = 80
    VP = {P: mp.fsum(D(w) for w in geo[P][0][1][2]) for P in geo}
    cases = [("LLLLLLR", "LR", 12, (5 + mp.sqrt(21)) / 2), ("LLRRLLR", "LR", 12, (5 + mp.sqrt(21)) / 2),
             ("LLLRRRRLLLR", "LR", 12, (5 + mp.sqrt(21)) / 2), ("LLLR", "LLRR", 9, 9 + 4 * mp.sqrt(5)),
             ("LLLLRR", "LLLRRR", 8, (umax + mp.sqrt(umax ** 2 - 4)) / 2)]
    ok = True
    for H, P, K, lam in cases:
        vols = {}
        for k in (K - 2, K - 1, K):
            g = seeded(H + P * k)
            if len(g) != 1:
                break
            vols[k] = mp.fsum(D(w) for w in g[0][1][2])
            print("  V(%s (%s)^%d) = %s (SnapPy %s)" % (H, P, k, mp.nstr(vols[k], 25),
                                                     seeds()[H + P * k]["volume"][:27]))
        if len(vols) != 3:
            ok = False
            say(True, "C9 %s on %s: no geometric orbit found at some k" % (H, P))
            continue
        b0 = {"LLLLLLR": 1, "LLRRLLR": 2, "LLLRRRRLLLR": 2, "LLLR": 0, "LLLLRR": 0}[H]
        say(False, "  %s on %s at k = %d: V(W_k) > (k + b_0) V(P) - 1/2: %s; |V(W_k) - (k + b_0) V(P)| > 1e-6: %s"
            % (H, P, K, vols[K] > (K + b0) * VP[P] - mp.mpf(1) / 2, abs(vols[K] - (K + b0) * VP[P]) > mp.mpf("1e-6")))
        d1 = vols[K - 1] - vols[K - 2] - VP[P]
        d2 = vols[K] - vols[K - 1] - VP[P]
        rat = d1 / d2
        good = abs(rat - lam) < mp.mpf("1e-7")
        ok = ok and good
        say(True, "C9 %s on %s at k = %d: ratio %s, lambda_+ %s, within 1e-7: %s"
            % (H, P, K, mp.nstr(rat, 12), mp.nstr(lam, 12), good))
    return ok


def main():
    if CONTROL:
        a = weil_checks()
        b = jacobian_checks()
        c7, c8, _, _ = volume_checks()
        caught = not (a and b and c8)
        print("CONTROL: the checks %s the targets made wrong on purpose" % ("caught" if caught else "MISSED"))
        return 1 if caught else 0
    a = weil_checks()
    b = index_checks()
    c = jacobian_checks()
    c7, c8, umax, geo = volume_checks()
    d = ratio_checks(umax, geo) if umax is not None else False
    verdict = a and b and c and c7 and c8 and d
    say(True, "VERDICT: the card holds where this seat checks it (C1-C9): %s" % verdict)
    return 0


if __name__ == "__main__":
    sys.exit(main())
