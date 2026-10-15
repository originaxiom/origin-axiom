"""Main's own check of the reviewer's finding 1 (UNSEALED; before any B1653 seal). Period-1 convention and B1642's
series (the exploration's code); the record frame F~ = (f, e^{i pi b} f(u + tau)); B1644's coupling
Y_ab = Res (C_a F~_x)^T eps S (C_b F~_y), BLOCKS (j, i, k). All linear algebra in mpmath at 40 digits."""
import mpmath as mp
mp.mp.dps = 40
I = mp.mpc(0, 1); NS = range(-25, 26)
e = lambda x: mp.exp(I * mp.pi * x)
def thc(a, b, z, T): return mp.fsum(e(T * (n + a) ** 2 + 2 * (n + a) * (z + b)) for n in NS)
def th1(z, t): return -I * mp.fsum((-1) ** k * e(t * (k + mp.mpf(1) / 2) ** 2 + (2 * k + 1) * z) for k in NS)
QI = mp.matrix([[I, 0], [0, -I]]); QJ = mp.matrix([[0, 1], [-1, 0]]); QK = QI * QJ; ONE = mp.eye(2); EPS = QJ
BLOCKS = [QJ, QI, QK]


def Bt(x, y, z, t):
    (ax, bx), (ay, by) = x, y; T = 2 * t; t1 = th1(z, t)
    den = I * e(-t / 2) * e(-z) * t1
    X0, X1 = thc(ax, bx, z, T), thc(ax, bx, z + t, T); Y0, Y1 = thc(ay, by, z, T), thc(ay, by, z + t, T)
    px, py = e(bx), e(by)
    return mp.matrix([[X0 * Y0 / t1, py * X0 * Y1 / den], [px * X1 * Y0 / den, px * py * X1 * Y1 / th1(z + t, t)]])


def ResB(x, y, t, rad=mp.mpf("0.02"), N=96):
    acc = mp.matrix(2, 2)
    for m in range(N):
        z = rad * e(2 * mp.mpf(m) / N); acc += Bt(x, y, z, t) * z
    return acc / N


def Y(S, Rb):
    M = mp.matrix(3, 3)
    for a, Ca in enumerate(BLOCKS):
        for b, Cb in enumerate(BLOCKS):
            K = Ca.T * EPS * S * Cb
            M[a, b] = sum(K[m, n] * Rb[m, n] for m in range(2) for n in range(2))
    return M


def svals(M): return sorted([abs(s) for s in mp.svd_c(M, compute_uv=False)], reverse=True)


def left_null(M):
    U, S, V = mp.svd_c(M)
    return [U[k, 2] for k in range(3)]


import random
random.seed(1653)
rt = lambda: (mp.mpf(random.uniform(-0.5, 0.5)), mp.mpf(random.uniform(-1, 1)))
t = mp.mpc(0.13, 1.07)
for trial in range(3):
    x, y, y2 = rt(), rt(), rt()
    Rb = ResB(x, y, t)
    det = Rb[0, 0] * Rb[1, 1] - Rb[0, 1] * Rb[1, 0]
    nrm = max(abs(Rb[m, n]) for m in range(2) for n in range(2))
    # the four unit residues: R_C = sum (eps C)_mn Res B_mn
    R = {}
    for name, C in (("1", ONE), ("i", QI), ("j", QJ), ("k", QK)):
        K = EPS * C; R[name] = sum(K[m, n] * Rb[m, n] for m in range(2) for n in range(2))
    nullq = R["1"] ** 2 + R["i"] ** 2 + R["j"] ** 2 + R["k"] ** 2
    S = mp.matrix([[mp.mpc(random.gauss(0, 1), random.gauss(0, 1)), mp.mpc(random.gauss(0, 1), random.gauss(0, 1))],
                   [mp.mpc(random.gauss(0, 1), random.gauss(0, 1)), mp.mpc(random.gauss(0, 1), random.gauss(0, 1))]])
    sv = svals(Y(S, Rb))
    # the left null vector depends only on x: compare with another y2
    n1 = left_null(Y(S, Rb)); n2 = left_null(Y(S, ResB(x, y2, t)))
    ov = abs(sum(mp.conj(n1[k]) * n2[k] for k in range(3)))
    print("trial", trial, " |det Res B|/max^2 =", mp.nstr(abs(det) / nrm ** 2, 3),
          " |R1^2 + R.R|/sum|R|^2 =", mp.nstr(abs(nullq) / sum(abs(v) ** 2 for v in R.values()), 3),
          " |R.R|/|R|^2 =", mp.nstr(abs(R['i'] ** 2 + R['j'] ** 2 + R['k'] ** 2) / sum(abs(R[s]) ** 2 for s in 'ijk'), 3),
          " sigma_min/sigma_max =", mp.nstr(sv[2] / sv[0], 3), " left-null overlap (x fixed, y varied) =", mp.nstr(ov, 15))
