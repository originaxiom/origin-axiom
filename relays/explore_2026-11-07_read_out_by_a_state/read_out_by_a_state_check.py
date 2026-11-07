"""The explore seat, 2026-11-07: THE READ-OUT BY A STATE (PREREGISTRATION_READ_OUT_BY_A_STATE.md in this folder).
Data-free: the hyperbolic geometry of the history's geodesic, the separated Laplacian of the flat-fibre bundle over it,
SL(2, Z/5) arithmetic, SnapPy length spectra and volumes. No frame value, no data, no held-out quantity.

  S1  the run classes' heights are half the Markov values lambda_i (two methods)
  S2  the exact separation along the history: l_c(s)^2 H_c = cosh(s - s_c), sampled classes
  S3  the class operator -psi'' + q cosh(2u) psi: ground energy by two discretisations; increasing in q
  S4  the run of 6: the lightest state, its gap, its read-out against the fibre area A, the small-A law
  S5  the closed approximants L^6 R (LR)^k, k = 1..8 (not blind)
  S6  the golden ground
  D   HS6: the cheapest line- (and rung-) invisible departures whose lightest state is unique
  V   HS6v: the leaders under the volume action (SnapPy)
  W   HS7: the hyperbolic systole's multiplicity on closed threads (the winding tower)
    python3 read_out_by_a_state_check.py
"""
import importlib.util
import itertools
import math
import pathlib
import sys

import mpmath as mp
import numpy as np
from scipy.linalg import eigh, eigh_tridiagonal

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))


def load(name):
    sp = importlib.util.spec_from_file_location(name, HERE / (name + ".py"))
    mod = importlib.util.module_from_spec(sp)
    sys.modules[name] = mod
    sp.loader.exec_module(mod)
    return mod


LA = load("least_action_check")
D0 = LA.D0
mp.mp.dps = 50
PHI = (1 + mp.sqrt(5)) / 2
SQ5 = mp.sqrt(5)
HSTAR = (5 + SQ5) / 2
G = 40
AREAS = [1e-4, 1e-3, 1e-2, 1e-1, 1.0, 2 * math.pi, 10.0]


# ---------------------------------------------------------------- S1: heights
def lambdas(runs, g=G):
    """lambda_i = a_i + [0; a_i+1, ...] + [0; a_i-1, ...] on the history [1]*g + runs + [1]*g, golden beyond"""
    h = [1] * g + list(runs) + [1] * g
    n = len(h)
    right, left = [None] * n, [None] * n
    v = 1 / PHI
    for i in range(n - 1, -1, -1):
        right[i] = v
        v = 1 / (h[i] + v)
    v = 1 / PHI
    for i in range(n):
        left[i] = v
        v = 1 / (h[i] + v)
    return [h[i] + right[i] + left[i] for i in range(n)], h, right, left


def closed(runs, k):
    return list(runs) + ([1] if len(runs) % 2 else []) + [1] * (2 * k)


def word_matrix(seq, start):
    M, p = D0.I2, len(seq)
    for j in range(p):
        idx = (start + j) % p
        M = D0.mul(M, D0.pw(D0.L if idx % 2 == 0 else D0.R, seq[idx]))
    return M


def axis_height(seq, i):
    """the axis of the rotation starting at run i, its height over that run's cusp (R-run: infinity; L-run: 0)"""
    M = word_matrix(seq, i)
    t = M[0][0] + M[1][1]
    off = M[1][0] if i % 2 == 1 else M[0][1]
    return mp.sqrt(mp.mpf(t) ** 2 - 4) / (2 * abs(off))


def deepest(runs):
    lam, h, _, _ = lambdas(runs)
    order = sorted(range(len(lam)), key=lambda i: -lam[i])
    return lam, order, lam[order[0]] - lam[order[1]]


# ---------------------------------------------------------------- S3: the class operator
def window(q):
    """w: the harmonic width (2q)^-1/4; U: the half-box, wide enough for the decay, narrow enough for the conditioning"""
    w = (2 * q) ** -0.25
    return w, max(6 * w, 0.5 * math.acosh(1 + 400.0 / q))


def ground_fd(q, N=20000):
    w, U = window(q)

    def fd(n):
        u = np.linspace(-U, U, n)
        hh = u[1] - u[0]
        d = 2 / hh ** 2 + q * np.cosh(2 * u)
        e = -np.ones(n - 1) / hh ** 2
        val, vec = eigh_tridiagonal(d, e, select="i", select_range=(0, 0))
        return val[0], u, vec[:, 0]

    E1, _, _ = fd(N)
    E2, u, psi = fd(2 * N - 1)
    psi = psi * np.sign(psi[len(psi) // 2])
    return E2 + (E2 - E1) / 3, u, psi


def ground_dvr(q, n=801):
    w, U = window(q)
    u = np.linspace(-U, U, n)
    hh = u[1] - u[0]
    i = np.arange(n)
    D = i[:, None] - i[None, :]
    Dn = np.where(D == 0, 1, D)
    T = np.where(D == 0, np.pi ** 2 / 3, 2.0 * (-1.0) ** np.abs(D) / Dn ** 2) / hh ** 2
    return eigh(T + np.diag(q * np.cosh(2 * u)), eigvals_only=True, subset_by_index=[0, 0])[0]


def readout(q):
    E, u, psi = ground_fd(q)
    P = psi ** 2
    P /= np.trapezoid(P, u)
    return dict(E=E, h_ratio=float(np.trapezoid(P / np.cosh(2 * u), u)),
                h_lin=float(np.trapezoid(psi / np.cosh(2 * u), u) / np.trapezoid(psi, u)),
                u2=float(np.trapezoid(P * u * u, u)), cosh=float(np.trapezoid(P * np.cosh(2 * u), u)),
                odd=float(np.trapezoid(P * np.tanh(2 * u), u)), w=window(q)[0], u=u, P=P)


def qof(A, H):
    return 4 * math.pi ** 2 / (A * float(H))


# ---------------------------------------------------------------- D: departures
def mod5(M):
    return tuple(tuple(x % 5 for x in row) for row in M)


def mul5(A, B):
    return (((A[0][0] * B[0][0] + A[0][1] * B[1][0]) % 5, (A[0][0] * B[0][1] + A[0][1] * B[1][1]) % 5),
            ((A[1][0] * B[0][0] + A[1][1] * B[1][0]) % 5, (A[1][0] * B[0][1] + A[1][1] * B[1][1]) % 5))


POW5 = {(lt, r): mod5(D0.pw(D0.L if lt == 0 else D0.R, r)) for lt in (0, 1) for r in range(1, 8)}
NEGI5 = ((4, 0), (0, 4))
I5 = ((1, 0), (0, 1))
PAIR = LA.PAIR


def mat5(runs):
    M = I5
    for i, r in enumerate(runs):
        M = mul5(M, POW5[(i % 2, r)])
    return M


def inv5(M):
    return ((M[1][1], (-M[0][1]) % 5), ((-M[1][0]) % 5, M[0][0]))


def E5(runs):
    return mul5(mat5(runs), inv5(mat5([1] * len(runs))))


def line_inv(E):
    Ei = inv5(E)
    return all(D0.pm(D0.act(w, Ei)) == w for w in PAIR)


def rung_inv(E):
    return E in (I5, NEGI5)


def Q_exact(runs):
    E = D0.mul(LA.mat(runs), D0.inv(LA.mat([1] * len(runs))))
    return (E[0][0] + (E[0][1] + E[1][0]) * PHI + E[1][1] * PHI ** 2) / (2 + PHI)


def B_bound(runs):
    prod = mp.mpf(1)
    for r in runs:
        prod *= 1 + (r - 1) / PHI ** 2
    return 1 + PHI ** 2 / SQ5 * (prod - 1)


def single_excess(r):
    return 2 * mp.log((r - 1 + SQ5) / SQ5)


def build(rs, gaps):
    runs = [rs[0]]
    for g, r in zip(gaps, rs[1:]):
        runs += [1] * g + [r]
    return tuple(runs)


if __name__ == "__main__":
    print("THE READ-OUT BY A STATE -- data-free check (the explore seat, 2026-11-07)")
    six = (6,)

    # ------------------------------------------------------------ S1
    print("\nS1. heights = half the Markov values (two methods)")
    worst = mp.mpf(0)
    for runs in ((6,), (2, 1, 1, 1, 2), (2, 3), (3, 1, 2), (2, 2, 1, 4)):
        lam, h, _, _ = lambdas(runs)
        seq = closed(runs, 30)
        for j in range(len(seq) if len(seq) < 12 else 12):
            idx = G + j
            if idx >= len(lam):
                break
            d = abs(lam[idx] / 2 - axis_height(seq, j))
            worst = max(worst, d)
    print("  max |lambda_i/2 - axis height of the rotation at run i| (k = 30, 5 departures, first 12 runs): %s" % mp.nstr(worst, 3))
    lam6, order6, gap6 = deepest(six)
    print("  run of 6: deepest at history index %d (the 6 sits at %d); lambda/2 = %s; (5 + sqrt5)/2 = %s; diff %s" % (
        order6[0], G, mp.nstr(lam6[order6[0]] / 2, 20), mp.nstr(HSTAR, 20), mp.nstr(abs(lam6[order6[0]] / 2 - HSTAR), 3)))
    print("  HS1a (two methods agree to 1e-20): %s" % (worst < mp.mpf(10) ** -20))

    # ------------------------------------------------------------ S2
    print("\nS2. the exact separation along the run-of-6 history (lift with the 6's cusp at infinity)")
    lam, h, right, left = lambdas(six)
    xi = float(h[G] + right[G])
    eta = float(-left[G])
    c0, rho = (xi + eta) / 2, (xi - eta) / 2
    s = np.linspace(-10, 10, 40001)
    tau = c0 + rho * np.tanh(s) + 1j * rho / np.cosh(s)
    classes = []
    for m in range(0, 26):
        for n in range(-200, 201):
            if (m, n) == (0, 0) or math.gcd(m, abs(n)) != 1 or (m == 0 and n != 1):
                continue
            Hc = rho if m == 0 else (xi - eta) / (2 * abs(m * xi - n) * abs(m * eta - n))
            classes.append((Hc, m, n))
    classes.sort(reverse=True)
    resid, grid_dev = 0.0, 0.0
    for Hc, m, n in classes[:40]:
        l2 = np.abs(m * tau - n) ** 2 / tau.imag
        if m == 0:
            sc = 0.0
        else:
            r_ = n / m
            a_, b_ = (c0 - r_) ** 2 + rho ** 2, 2 * rho * (c0 - r_)
            sc = -math.atanh(b_ / a_)   # a cosh s + b sinh s is least at s = -atanh(b/a)
        grid_dev = max(grid_dev, abs(s[int(np.argmin(l2))] - sc))
        mask = np.abs(s - sc) < 8
        r = np.max(np.abs(l2[mask] * Hc / np.cosh(s[mask] - sc) - 1))
        resid = max(resid, r)
    print("  classes sampled: %d (m <= 25, |n| <= 200, primitive); cosh law on the 40 deepest: max relative residual %.2e" % (len(classes), resid))
    print("  the analytic s_c against the grid's argmin (step 5e-4): max deviation %.1e" % grid_dev)
    runH = sorted({round(float(x / 2), 12) for x in lam}, reverse=True)
    top = [(round(Hc, 6), m, n) for Hc, m, n in classes[:8]]
    print("  the 8 deepest sampled classes (H_c, m, n): %s" % top)
    print("  the deepest run-class heights lambda_i/2: %s" % runH[:6])
    big = [(Hc, m, n) for Hc, m, n in classes if Hc > 1]
    unmatched = [(Hc, m, n) for Hc, m, n in big if min(abs(Hc - x) for x in runH) > 1e-9]
    print("  sampled classes with H_c > 1: %d; not a run class: %d %s" % (len(big), len(unmatched), unmatched[:5]))
    print("  HS1b (cosh law < 1e-9; max H_c = max lambda/2; H_c > 1 only run classes): %s, %s, %s" % (
        resid < 1e-9, abs(classes[0][0] - runH[0]) < 1e-9, not unmatched))

    # ------------------------------------------------------------ S3
    print("\nS3. the class operator -psi'' + q cosh(2u) psi")
    qs = np.logspace(-1, 5, 25)
    Es, agree = [], 0.0
    for q in qs:
        E = ground_fd(q)[0]
        Es.append(E)
        agree = max(agree, abs(E - ground_dvr(q)) / abs(E))
    mono = all(b > a for a, b in zip(Es, Es[1:]))
    hf = []
    for q in (1.0, 10.0, 100.0):
        dq = 1e-3 * q
        num = (ground_fd(q + dq)[0] - ground_fd(q - dq)[0]) / (2 * dq)
        hf.append((q, num, readout(q)["cosh"]))
    print("  q in [0.1, 1e5] (25 points): FD-Richardson vs sinc-DVR max relative difference %.2e; strictly increasing: %s" % (agree, mono))
    print("  Hellmann-Feynman dE/dq vs <cosh 2u>: %s" % ["q=%g: %.8f vs %.8f" % t for t in hf])
    print("  HS2 (agree < 1e-7 and increasing): %s" % (agree < 1e-7 and mono))

    # ------------------------------------------------------------ S4
    print("\nS4. the run of 6: the lightest state and its read-out")
    H1 = float(lam6[order6[0]] / 2)
    H2 = float(lam6[order6[1]] / 2)
    H3 = float(lam6[order6[2]] / 2)
    print("  deepest H* = %.15f (unique: gap in lambda %s); runner-up H2 = %.12f at index %d, third %.12f at index %d" % (
        H1, mp.nstr(gap6, 6), H2, order6[1], H3, order6[2]))
    print("  the runner-up pair is a mirror pair (equal heights at indices symmetric about the 6): %s" % (
        abs(H2 - H3) < 1e-30 and order6[1] + order6[2] == 2 * G))
    law = math.sqrt(H1 / (8 * math.pi ** 2))
    print("  small-A law constant sqrt(H*/(8 pi^2)) = %.6f" % law)
    print("  %-10s %-12s %-12s %-10s %-10s %-12s %-12s %-12s" % ("A", "q*", "E0(q*)", "E0 gap", "<Im>/H*", "lin/H*", "(1-<>)/sqrtA", "<tanh 2u>"))
    for A in AREAS:
        q1, q2 = qof(A, H1), qof(A, H2)
        r = readout(q1)
        e2 = ground_fd(q2)[0]
        print("  %-10g %-12.6g %-12.8g %-10.6g %-10.6f %-12.6f %-12.6f %.1e" % (
            A, q1, r["E"], e2 - r["E"], r["h_ratio"], r["h_lin"], (1 - r["h_ratio"]) / math.sqrt(A), r["odd"]))
    r4 = readout(qof(1e-4, H1))
    print("  HS3 (unique deepest at the 6, H* = sqrt5 phi to 1e-40, mirror runner-up): %s" % (
        order6[0] == G and abs(lam6[order6[0]] / 2 - HSTAR) < mp.mpf(10) ** -40 and abs(H2 - H3) < 1e-30))
    print("  HS4 (law within 2%% at A = 1e-4; <Re> exactly the apex's: odd moment ~ 0): %s (ratio %.4f)" % (
        abs((1 - r4["h_ratio"]) / 1e-2 / law - 1) < 0.02, (1 - r4["h_ratio"]) / 1e-2 / law))

    # ------------------------------------------------------------ S5
    print("\nS5. closed approximants L^6 R (LR)^k: not blind")
    print("  %-3s %-18s %-10s %-14s %-12s %-12s" % ("k", "H_k (6-class)", "deepest?", "next H", "<Im>/H_k A=1", "window/period"))
    ok5 = True
    for k in range(1, 9):
        seq = closed(six, k)
        hs = [axis_height(seq, i) for i in range(len(seq))]
        Hk = hs[0]
        others = sorted((float(x) for x in hs[1:]), reverse=True)
        deepest_ok = all(Hk > x for x in hs[1:])
        r = readout(qof(1.0, Hk))
        W = word_matrix(seq, 0)
        ell = 2 * mp.acosh(mp.mpf(W[0][0] + W[1][1]) / 2)
        frac = 8 * r["w"] / float(ell)
        ok5 &= deepest_ok
        print("  %-3d %-18.14f %-10s %-14.10f %-12.8f %-12.6f" % (k, float(Hk), deepest_ok, others[0], r["h_ratio"], frac))
    print("  H_inf = %.14f; HS5 (the 6-class deepest at every k; H_k -> H*): %s" % (float(HSTAR), ok5))

    # ------------------------------------------------------------ S6
    print("\nS6. the golden ground")
    lamg, _, _, _ = lambdas(())
    dev = max(abs(x - SQ5) for x in lamg)
    gseq = [1, 1]
    print("  every lambda_i = sqrt5 on the golden history: max deviation %s" % mp.nstr(dev, 3))
    print("  closed golden bundle: the two run classes' heights %s, %s (two-fold degenerate)" % (
        mp.nstr(axis_height(gseq, 0), 15), mp.nstr(axis_height(gseq, 1), 15)))
    print("  the golden pair of lines is fixed by the tick LR (the wells one tick apart read the same (tau, line)): %s" % (
        all(D0.pm(D0.act(w, D0.inv(D0.LR))) == w for w in PAIR)))
    print("  the golden pair under the mirror (alpha, b) -> (-alpha, b): %s -> %s" % (
        sorted(PAIR), sorted(D0.pm(((-w[0]) % 5, w[1])) for w in PAIR)))

    # ------------------------------------------------------------ D
    print("\nD. HS6 -- the cheapest invisible departures whose lightest state is unique")
    X6 = 2 * mp.log(Q_exact(six))
    XMAX = X6 + mp.mpf("0.01")
    rmax = 1 + int(mp.floor((mp.e ** (XMAX / 2) - 1) * SQ5))
    Kmax = 0
    while 2 * mp.log(1 + PHI ** 2 / SQ5 * ((1 + 1 / PHI ** 2) ** (Kmax + 1) - 1)) <= XMAX:
        Kmax += 1
    print("  excess(6) by Lemma A = %s (the single-run formula: %s); range: excess <= %s" % (
        mp.nstr(X6, 15), mp.nstr(single_excess(6), 15), mp.nstr(XMAX, 8)))
    print("  Lemma C range: at most %d non-1 runs, each <= %d; gaps 0..%d" % (Kmax, rmax, G))
    found = {"line": [], "rung": []}
    nall, ninv, bad_B = 0, 0, 0
    patterns = []
    for K in range(1, Kmax + 1):
        for rs in itertools.product(range(2, rmax + 1), repeat=K):
            if 2 * mp.log(B_bound(rs)) > XMAX:
                continue
            patterns.append(rs)
            for gaps in itertools.product(range(G + 1), repeat=K - 1):
                runs = build(rs, gaps)
                nall += 1
                E = E5(runs)
                li, ri = line_inv(E), rung_inv(E)
                if not (li or ri):
                    continue
                ninv += 1
                Q = Q_exact(runs)
                if Q < B_bound(runs) - mp.mpf(10) ** -30:
                    bad_B += 1
                X = 2 * mp.log(Q)
                if X > XMAX:
                    continue
                lam, order, gap = deepest(runs)
                rec = (X, runs, gap > mp.mpf(10) ** -30, order[0] - G, float(lam[order[0]] / 2), gap)
                if li:
                    found["line"].append(rec)
                if ri:
                    found["rung"].append(rec)
    print("  departures enumerated: %d; invisible (line or rung): %d; Lemma C violations: %d; patterns within range: %d" % (
        nall, ninv, bad_B, len(patterns)))
    winners = {}
    for reading in ("rung", "line"):
        L_ = sorted(found[reading], key=lambda t: t[0])
        print("  %s-invisible within range: %d; the 12 cheapest:" % (reading, len(L_)))
        for X, runs, uq, pos, Hd, gap in L_[:12]:
            print("    %-30s excess %s  unique lightest: %-5s deepest run #%d (H %.6f, lambda gap %s)" % (
                runs if len(runs) < 14 else str(runs[:6]) + "...(%d runs)" % len(runs), mp.nstr(X, 12), uq, pos, Hd, mp.nstr(gap, 3)))
        uniq = [t for t in L_ if t[2]]
        winners[reading] = uniq[0] if uniq else None
        if uniq:
            X, runs, _, pos, Hd, gap = uniq[0]
            nxt = uniq[1] if len(uniq) > 1 else None
            print("  %s reading: the cheapest with a unique lightest state: %s, excess %s, depth H %.12f; next %s %s" % (
                reading, runs, mp.nstr(X, 15), Hd, nxt[1] if nxt else None, mp.nstr(nxt[0], 12) if nxt else ""))
            lims = [(sum(single_excess(r) for r in rs), rs) for rs in patterns
                    if len(rs) > 1 and not (len(rs) == 2 and rs[0] == rs[1])]   # (r, 1^g, r) is always a palindrome
            under = [(mp.nstr(v, 8), rs) for v, rs in lims if v < X - mp.mpf(10) ** -12]
            print("    patterns whose large-gap limit lies below it (unresolved by the gap range): %s" % (under[:10] if under else "none"))
    for reading in ("rung", "line"):
        w = winners[reading]
        if w:
            print("  cross-check (the web seat's k-approximant excess) for %s's winner %s: k=20 %s, k=30 %s, Lemma A %s" % (
                reading, w[1] if len(w[1]) < 14 else "(%d runs)" % len(w[1]), mp.nstr(LA.excess(w[1], 20), 12),
                mp.nstr(LA.excess(w[1], 30), 12), mp.nstr(w[0], 12)))
    print("  HS6 (line reading: the cheapest unique-lightest departure is (6)): %s" % (
        winners["line"] is not None and winners["line"][1] == six))
    print("  rung reading: the cheapest unique-lightest departure is (6): %s" % (
        winners["rung"] is not None and winners["rung"][1] == six))

    # ------------------------------------------------------------ V
    print("\nV. HS6v -- the volume action for the leaders (SnapPy closed approximants)")
    try:
        import snappy
        VOL4 = float(snappy.ManifoldHP("m004").volume())

        def letters(runs, k):
            st = "".join(("L" if i % 2 == 0 else "R") * r for i, r in enumerate(runs))
            return st + ("R" if len(runs) % 2 else "") + "LR" * k

        def dV(runs, k):
            M = snappy.Manifold("b++" + letters(runs, k))
            return float(M.volume()) - (k + (len(runs) + 1) // 2) * VOL4, M.solution_type()

        line_u = [t for t in sorted(found["line"], key=lambda t: t[0]) if t[2]][:6]
        cands = [six, (2, 1, 1, 1, 2)] + [t[1] for t in line_u if t[1] not in (six, (2, 1, 1, 1, 2))]
        for runs in cands:
            a, sa = dV(runs, 10)
            b, sb = dV(runs, 12)
            print("  %-30s dV(k=10) %.10f  dV(k=12) %.10f  %s" % (
                runs if len(runs) < 14 else "(%d runs) %s..." % (len(runs), runs[:5]), a, b,
                "ok" if sa == sb == "all tetrahedra positively oriented" else (sa, sb)))
    except Exception as exc:  # reported, not fatal
        print("  V failed: %r" % (exc,))

    # ------------------------------------------------------------ W
    print("\nW. HS7 -- the hyperbolic systole on closed threads (the winding tower)")
    try:
        import snappy
        wl = [six, (2, 1, 1, 1, 2)]
        if winners["line"] and winners["line"][1] not in wl and len(winners["line"][1]) < 14:
            wl.append(winners["line"][1])
        for runs in wl:
            for k in (1, 2):
                word = "".join(("L" if i % 2 == 0 else "R") * r for i, r in enumerate(runs)) + ("R" if len(runs) % 2 else "") + "LR" * k
                try:
                    M = snappy.Manifold("b++" + word)
                    spec = M.length_spectrum(2.5)
                    rows = [(float(x.length.real()), int(x.multiplicity)) for x in spec[:4]]
                    print("  b++%-26s systole %.10f mult %d; next %s" % (word, rows[0][0], rows[0][1], rows[1:3]))
                except Exception as exc:
                    print("  b++%-26s length spectrum failed: %r" % (word, exc))
    except Exception as exc:
        print("  W failed: %r" % (exc,))
    print("\nread_out_by_a_state_check exit 0")
