"""B1957: main's own two-loop running of the Standard Model with full 3 x 3 Yukawa matrices, transcribed by main from the
primary source: Luo and Xiao, "Two-loop renormalization group equations in the Standard Model", Phys. Rev. Lett. 90 (2003)
011601, arXiv:hep-ph/0207271, equations (3) to (10), read in the paper's PDF.
Their conventions: -L = e-bar F_L phi^dagger l + d-bar F_D phi^dagger q + u-bar H phi^(dagger c) q + h.c. + (lambda/2)(phi^dagger phi)^2;
beta_x = mu dx/dmu = beta1/(16 pi^2) + beta2/(16 pi^2)^2; each Yukawa beta function is the matrix times the right-hand side
(the polynomial stands on the RIGHT of the matrix and acts on the doublet index); g1 in SU(5) normalisation.
The gauge two-loop terms are the standard ones (their matrix of coefficients, with the Yukawa traces of Buttazzo et al.,
arXiv:1307.3536, equations (96) to (98)).  No measured number is used."""
import numpy as np
from scipy.integrate import solve_ivp
K = 1 / (16 * np.pi ** 2); NG = 3
BIJ = np.array([[199 / 50, 27 / 10, 44 / 5], [9 / 10, 35 / 6, 12], [11 / 10, 9 / 2, -26]]); B1 = np.array([41 / 10, -19 / 6, -7])
CU, CD, CE = np.array([17 / 10, 3 / 2, 2]), np.array([1 / 2, 3 / 2, 2]), np.array([3 / 2, 1 / 2, 0])


def pack(g, H, FD, FL, lam):
    return np.concatenate([np.asarray(g, float), np.asarray(H, complex).ravel().view(float), np.asarray(FD, complex).ravel().view(float), np.asarray(FL, complex).ravel().view(float), [float(lam)]])


def unpack(v):
    g = v[:3]; H = v[3:21].view(complex).reshape(3, 3); FD = v[21:39].view(complex).reshape(3, 3); FL = v[39:57].view(complex).reshape(3, 3)
    return g, H, FD, FL, v[57]


def rhs(t, v, loops=2, mixed_swapped=False):
    g, H, FD, FL, lam = unpack(v); a, b, c = g * g; g2 = g * g
    U, Dn, E = H.conj().T @ H, FD.conj().T @ FD, FL.conj().T @ FL; I = np.eye(3)
    tr = lambda M: np.trace(M).real
    Y2 = tr(3 * U + 3 * Dn + E); HS = tr(3 * U @ U + 3 * Dn @ Dn + E @ E)
    Y4 = (17 / 20 * a + 9 / 4 * b + 8 * c) * tr(U) + (1 / 4 * a + 9 / 4 * b + 8 * c) * tr(Dn) + 3 / 4 * (a + b) * tr(E)
    chi4 = 9 / 4 * tr(3 * U @ U + 3 * Dn @ Dn + E @ E - (U @ Dn + Dn @ U) / 3)
    Ru = 3 / 2 * (U - Dn) + (Y2 - (17 / 20 * a + 9 / 4 * b + 8 * c)) * I
    Rd = 3 / 2 * (Dn - U) + (Y2 - (1 / 4 * a + 9 / 4 * b + 8 * c)) * I
    Rl = 3 / 2 * E + (Y2 - 9 / 4 * (a + b)) * I
    dg = K * B1 * g ** 3
    dlam = K * (12 * lam ** 2 - (9 / 5 * a + 9 * b) * lam + (27 / 100 * a * a + 9 / 10 * a * b + 9 / 4 * b * b) + 4 * Y2 * lam - 4 * HS)
    if loops >= 2:
        mixu = (U @ Dn + Dn @ U / 4) if not mixed_swapped else (Dn @ U + U @ Dn / 4)
        mixd = (Dn @ U + U @ Dn / 4) if not mixed_swapped else (U @ Dn + Dn @ U / 4)
        Ru2 = (3 / 2 * U @ U - mixu + 11 / 4 * Dn @ Dn + Y2 * (5 / 4 * Dn - 9 / 4 * U) + (-chi4 + 3 / 2 * lam ** 2 + 5 / 2 * Y4) * I - 6 * lam * U
               + (223 / 80 * a + 135 / 16 * b + 16 * c) * U - (43 / 80 * a - 9 / 16 * b + 16 * c) * Dn
               + ((9 / 200 + 29 / 45 * NG) * a * a - 9 / 20 * a * b + 19 / 15 * a * c - (35 / 4 - NG) * b * b + 9 * b * c - (404 / 3 - 80 / 9 * NG) * c * c) * I)
        Rd2 = (3 / 2 * Dn @ Dn - mixd + 11 / 4 * U @ U + Y2 * (5 / 4 * U - 9 / 4 * Dn) + (-chi4 + 3 / 2 * lam ** 2 + 5 / 2 * Y4) * I - 6 * lam * Dn
               + (187 / 80 * a + 135 / 16 * b + 16 * c) * Dn - (79 / 80 * a - 9 / 16 * b + 16 * c) * U
               + (-(29 / 200 + 1 / 45 * NG) * a * a - 27 / 20 * a * b + 31 / 15 * a * c - (35 / 4 - NG) * b * b + 9 * b * c - (404 / 3 - 80 / 9 * NG) * c * c) * I)
        Rl2 = (3 / 2 * E @ E - 9 / 4 * Y2 * E + (-chi4 + 3 / 2 * lam ** 2 + 5 / 2 * Y4) * I - 6 * lam * E + (387 / 80 * a + 135 / 16 * b) * E
               + ((51 / 200 + 11 / 5 * NG) * a * a + 27 / 20 * a * b - (35 / 4 - NG) * b * b) * I)
        Ru = Ru + K * Ru2; Rd = Rd + K * Rd2; Rl = Rl + K * Rl2
        dg = dg + K * K * g ** 3 * (BIJ @ g2 - CU * tr(U) - CD * tr(Dn) - CE * tr(E))
        l2 = (-78 * lam ** 3 + (54 * b + 54 / 5 * a) * lam ** 2 - ((313 / 8 - 10 * NG) * b * b - 117 / 20 * a * b - (687 / 200 + 2 * NG) * a * a) * lam
              + (497 / 8 - 8 * NG) * b ** 3 - (97 / 40 + 8 / 5 * NG) * b * b * a - (717 / 200 + 8 / 5 * NG) * b * a * a - (531 / 1000 + 24 / 25 * NG) * a ** 3
              - 64 * c * tr(U @ U + Dn @ Dn) - 8 / 5 * a * tr(2 * U @ U - Dn @ Dn + 3 * E @ E) - 3 / 2 * b * b * Y2
              + a * ((63 / 5 * b - 171 / 50 * a) * tr(U) + (27 / 5 * b + 9 / 10 * a) * tr(Dn) + (33 / 5 * b - 9 / 2 * a) * tr(E))
              + 10 * lam * Y4 - 24 * lam ** 2 * Y2 - lam * HS - 42 * lam * tr(U @ Dn) + 20 * tr(3 * U @ U @ U + 3 * Dn @ Dn @ Dn + E @ E @ E) - 12 * tr(U @ (U + Dn) @ Dn))
        dlam = dlam + K * K * l2
    return pack(dg, K * H @ Ru, K * FD @ Rd, K * FL @ Rl, dlam)


def run(v0, t1, loops=2, mixed_swapped=False, rtol=1e-13):
    r = solve_ivp(rhs, (0.0, float(t1)), v0, method="DOP853", rtol=rtol, atol=1e-15, args=(loops, mixed_swapped)); return r.y[:, -1]


def observables(v):
    g, H, FD, FL, lam = unpack(v)
    su = np.linalg.svd(H, compute_uv=False); sd = np.linalg.svd(FD, compute_uv=False); sl = np.linalg.svd(FL, compute_uv=False)
    _, Vu = np.linalg.eigh(H.conj().T @ H); _, Vd = np.linalg.eigh(FD.conj().T @ FD)                 # eigenvectors on the doublet index
    V = np.abs(Vu.conj().T @ Vd)
    theta = np.angle(np.linalg.det(H) * np.linalg.det(FD))
    return np.concatenate([su, sd, sl, V.ravel()]), theta


if __name__ == "__main__":
    rng = np.random.default_rng(20261117)
    # V1: the top alone, against Buttazzo et al. (their lambda is half of Luo and Xiao's)
    from scipy.optimize import brentq
    H0 = np.zeros((3, 3), complex); H0[2, 2] = 0.9; v0 = pack([0.5, 0.6, 1.0], H0, np.zeros((3, 3)), np.zeros((3, 3)), 0.2)
    tc = brentq(lambda t: run(v0, t)[57], 1.0, 30.0, xtol=1e-14, rtol=1e-14)
    print("V1: the top alone from (1/2, 3/5, 1, 9/10) with lambda = 1/10 in the other normalisation: the quartic crosses zero at t = %.12f (Buttazzo et al.'s equations on main: 7.578626559316; agy-002: 7.578626559317)" % tc)
    # V2: the third generation, diagonal, against Buttazzo et al. equations (96) to (103)
    import pathlib as _pl, sys as _sys; _sys.path.insert(0, str(_pl.Path(__file__).resolve().parent))          # the sibling below is found in isolated mode too (the web seat's section 9, 2026-11-18)
    import sm_rge3
    g = np.array([0.47, 0.63, 1.08]); yt, yb, yl, lam = 0.91, 0.37, 0.23, 0.13
    v = pack(g, np.diag([0, 0, yt]), np.diag([0, 0, yb]), np.diag([0, 0, yl]), 2 * lam); d = rhs(0, v); dg, dH, dD, dL, dl = unpack(d)
    mine = np.array([dg[0], dg[1], dg[2], dH[2, 2].real, dD[2, 2].real, dL[2, 2].real, dl / 2]); ref = np.array(sm_rge3.beta3(g[0], g[1], g[2], yt, yb, yl, lam))
    print("V2: third generation, diagonal: Luo and Xiao against Buttazzo et al., seven beta functions, largest relative difference %.1e" % np.abs(mine / ref - 1).max())
    # V3, V4: generic complex matrices: basis independence, and the determinant's phase
    Yu = 0.3 * (rng.normal(size=(3, 3)) + 1j * rng.normal(size=(3, 3))); Yd = 0.2 * (rng.normal(size=(3, 3)) + 1j * rng.normal(size=(3, 3))); Yl = 0.1 * (rng.normal(size=(3, 3)) + 1j * rng.normal(size=(3, 3)))
    T1 = -6.0                                                    # six e-folds down: the couplings stay perturbative
    v0 = pack([0.5, 0.6, 1.0], Yu, Yd, Yl, 0.3); o0, th0 = observables(v0); o1, th1 = observables(run(v0, T1))
    def haar():
        q, r = np.linalg.qr(rng.normal(size=(3, 3)) + 1j * rng.normal(size=(3, 3))); return q * (np.diag(r) / np.abs(np.diag(r)))
    worst = 0.0
    for _ in range(6):
        UQ, Uu, Ud, UL, Ue = (haar() for _ in range(5))
        w0 = pack([0.5, 0.6, 1.0], Uu @ Yu @ UQ.conj().T, Ud @ Yd @ UQ.conj().T, Ue @ Yl @ UL.conj().T, 0.3); o2, th2 = observables(run(w0, T1))
        worst = max(worst, np.abs(o2 / o1 - 1).max())
    print("V3: generic complex matrices run over six e-folds: singular values and |V| unchanged by six random changes of basis in U(3)^5: %.1e" % worst)
    print("V4: arg det(Y_u Y_d) along that run: %.15f before, %.15f after: it moves by %.1e, while the singular values move by up to %.2f in ratio" % (th0, th1, abs(th1 - th0), np.abs(o1[:9] / o0[:9] - 1).max()))
    # V5: the order of the mixed two-loop products, on a rank-one top and bottom whose directions differ by an angle
    yt, yb = 0.9, 0.6; th = 0.35; e_t = np.array([0, 0, 1.0]); e_b = np.array([0, np.sin(th), np.cos(th)])
    Hu = yt * np.outer(e_t, e_t).astype(complex); Fd = yb * np.outer(e_b, e_b).astype(complex)
    def angle(v):
        g, H, FD, FL, lam = unpack(v)
        tu = np.linalg.eigh(H.conj().T @ H)[1][:, -1]; td = np.linalg.eigh(FD.conj().T @ FD)[1][:, -1]
        return np.arccos(min(1.0, abs(np.vdot(tu, td))))
    def dlnsin(swapped, loops):
        v = pack([0.0, 0.0, 0.0], Hu, Fd, np.zeros((3, 3)), 0.0); e = 1e-3
        f = lambda s: np.log(np.sin(angle(v + s * rhs(0, v, loops, swapped))))
        return (f(e) - f(-e)) / (2 * e)
    one = dlnsin(False, 1) / K; c0 = (dlnsin(False, 2) - dlnsin(False, 1)) / (K * K); c1 = (dlnsin(True, 2) - dlnsin(True, 1)) / (K * K)
    u = (yt ** 2 + yb ** 2) * np.cos(th) ** 2
    print("V5: rank-one top and bottom at angle 0.35, gauge and quartic off: d ln(sin theta)/dt at one loop is %+.6f /(16 pi^2), and +(3/2)(yt^2 + yb^2) cos^2 = %+.6f (the angle grows toward high scales)" % (one, 1.5 * u))
    def small(yt_, yb_, sw, th_=0.02):
        global yt, yb, th, Hu, Fd
        e_b_ = np.array([0, np.sin(th_), np.cos(th_)]); Hu_ = yt_ * np.outer(e_t, e_t).astype(complex); Fd_ = yb_ * np.outer(e_b_, e_b_).astype(complex)
        def d(loops):
            v = pack([0.0, 0.0, 0.0], Hu_, Fd_, np.zeros((3, 3)), 0.0); e = 1e-3
            f = lambda s: np.log(np.sin(angle(v + s * rhs(0, v, loops, sw))))
            return (f(e) - f(-e)) / (2 * e)
        return (d(2) - d(1)) / (K * K)
    for sw, lab in ((False, "as printed by Luo and Xiao"), (True, "the two mixed products exchanged")):
        a_, b_, c_ = small(1.0, 1e-3, sw), small(1e-3, 1.0, sw), small(1.0, 1.0, sw)
        print("    at a small angle, %s: the two-loop part is %.4f yt^4 %.4f yb^4 %.4f yt^2 yb^2 (-13/2, -13/2 and -11/2 as printed; 7 is the exchanged order)" % (lab, a_, b_, c_ - a_ - b_))
    print("    its two-loop part in units of 1/(16 pi^2)^2: %.6f with the products as printed by Luo and Xiao; %.6f with the two mixed products exchanged; the difference %.6f, and (3/2) yt^2 yb^2 cos^2(theta) = %.6f" % (c0, c1, c1 - c0, 1.5 * yt ** 2 * yb ** 2 * np.cos(th) ** 2))
