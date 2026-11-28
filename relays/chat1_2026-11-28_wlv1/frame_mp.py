"""Frame C's averaged frame F-bar in extended precision (main, 2026-11-14, P-853): every step of B1724's frame with the
exact channel weight (B1932's fiber_grid_t90) redone in mpmath, so that the read-out can be evaluated high in the cusp,
where the double-precision frame loses the first generation and the mixing (F-bar(tau + 1) = F-bar(tau) fails above
Im tau about 11).
- residues: B1906's closed form (B1938 section 1, checked against the contour);
- a0: the constant term of Kronecker's function, 2 pi i alpha + theta1'(z)/theta1(z);
- c_s: B1919's closed form (fast_norm's F_u), in mpmath;
- exact zeros of the zero law by exact rational characteristics, not by a threshold;
- the Higgs triplet's components from the record's q-series (the_exponents' ev), unrounded;
- the coupling, the SVDs and the CKM in mpmath at 30 + 2 Im tau digits.
The canonical end L_2 is the record's (B1927's table, read at x reduced mod 1), as a definitional input."""
import sys, pathlib
from fractions import Fraction as Fr
import mpmath as mp
ROOT = pathlib.Path(__file__).resolve().parent / "main_tree"  # [copy: loader replaced, see MANIFEST.md]
EB = pathlib.Path(__file__).resolve().parent  # [copy: loader replaced, see MANIFEST.md]
_argv = sys.argv; sys.argv = ["x"]  # [copy: loader replaced, see MANIFEST.md]
import fiber_grid_t90 as G90          # the record's frame, for its constants, the end table and the triplet's series
sys.argv = _argv
FG, CR, C = G90.FG, G90.CR, G90.C
B = C._modules()["B"]; te = C._modules()["te"]
H = Fr(1, 2)
POINTS = [(Fr(i, 5), Fr(j, 5)) for i in range(5) for j in range(5) if (i, j) != (0, 0)]
assert [(float(a), float(b)) for a, b in POINTS] == [(float(a), float(b)) for a, b in FG.POINTS]
KEYS = ["up|L_2|St", "up|L_2|S", "down|L_2|S", "down|L_2|St", "ckm|L_2|St|S", "ckm|L_2|S|St"]
UNITS = list(B.UNITS)


def M2(A):
    return mp.matrix([[mp.mpc(complex(A[i][j]).real, complex(A[i][j]).imag) for j in range(2)] for i in range(2)])


def f2m(q):
    return mp.mpf(q.numerator) / q.denominator


def setup():
    I = mp.mpc(0, 1)
    QI = mp.matrix([[I, 0], [0, -I]]); QJ = mp.matrix([[0, 1], [-1, 0]]); QK = QI * QJ; EPS = QJ
    U = {"1": mp.eye(2), "i": QI, "j": QJ, "k": QK}
    ED = {s: M2(B.EDUAL[s]) for s in UNITS}            # exact halves (checked below)
    for s in UNITS:
        for i in range(2):
            for j in range(2):
                assert abs(ED[s][i, j] * 2 - mp.nint(mp.re(ED[s][i, j] * 2)) - I * mp.nint(mp.im(ED[s][i, j] * 2))) < mp.mpf(10) ** -14
                ED[s][i, j] = (mp.nint(mp.re(ED[s][i, j] * 2)) + I * mp.nint(mp.im(ED[s][i, j] * 2))) / 2
    return I, QI, QJ, QK, EPS, U, ED, [QJ, QI, QK]


def F_u(u1, u2, t, y):
    """B1919's closed form (fast_norm.F_u) in mpmath; u1, u2 exact rationals"""
    a = u1 % 1; b = u2 % 1; x = mp.re(t)
    if a != 0:
        first = -mp.pi * (2 * mp.log(2) + mp.log(y) + mp.digamma(f2m(a)) + mp.digamma(1 - f2m(a))); zero_row = 0
    else:
        first = mp.pi * (2 * mp.euler - 2 * mp.log(2) - mp.log(y))
        zero_row = y * mp.pi ** 2 / mp.sin(mp.pi * f2m(b)) ** 2 if b != 0 else mp.inf
    K = int(mp.mp.dps * 2.31 / (2 * mp.pi * y)) + 4
    tot = 0
    for k in range(-K, K + 1):
        m = f2m(a) + k
        if m == 0:
            continue
        w = mp.exp(-2 * mp.pi * abs(m) * y + 2j * mp.pi * (m * x + f2m(u2)))
        tot += (2 * mp.pi / abs(m)) * mp.re(w / (1 - w))
    return first + zero_row + tot


def is_zero(c):
    return (c[0] - H) % 1 == 0 and (c[1] - H) % 1 == 0


def fbar(tx, ty, L2=None, dps=None):
    """F-bar at tau = tx + i ty (tx, ty exact or float); L2 the end (default: the record's table at x mod 1)"""
    ty_f = float(ty); mp.mp.dps = dps or int(30 + 2 * ty_f)
    I, QI, QJ, QK, EPS, U, ED, BLOCKS = setup()
    t = mp.mpc(mp.mpf(tx), mp.mpf(ty)); y = mp.im(t)
    if L2 is None:
        xr = ((float(tx) + 0.5) % 1.0) - 0.5
        L2 = CR.canon(complex(xr, ty_f))["L_2"]
    L = mp.mpf(L2)
    eta = mp.exp(I * mp.pi * t / 12) * mp.qp(mp.exp(2 * I * mp.pi * t)); t1p = 2 * mp.pi * eta ** 3
    th1 = lambda z: B.th_mp(1, z, t)
    c3 = [te.ev(cc, t) for cc in te.B[1]]
    S = c3[0] * QI + c3[1] * QJ + c3[2] * QK
    conj = lambda A: mp.matrix([[mp.conj(A[i, j]) for j in range(A.cols)] for i in range(A.rows)])
    RD = {"S": S, "St": EPS * conj(S) * EPS.T}
    acc = {k: None for k in KEYS}
    for a, b in POINTS:
        Y = {}
        for sec in ("up", "down"):
            ql, qr = B.SIXY[B.SECTORS[sec][0]], B.SIXY[B.SECTORS[sec][1]]
            x = (ql * a, 2 * ql * b); yy = (qr * a, 2 * qr * b)                 # twist_of(q w, t), exact
            ap, am = x[0] + yy[0], x[0] - yy[0]; bp, bm = (x[1] + yy[1]) / 2, (x[1] - yy[1]) / 2
            e = mp.exp(-2 * I * mp.pi * f2m(x[0]))
            kap = {"1": -I * e, "i": mp.mpf(-1), "j": -e, "k": I}
            cs = {"1": (ap + H, bp + H), "i": (ap + H, bp), "j": (ap, bp + H), "k": (ap, bp)}
            ds = {"1": (am + H, bm + H), "i": (am + H, bm), "j": (am, bm + H), "k": (am, bm)}
            u = {}
            for s in UNITS:
                if is_zero(cs[s]) or is_zero(ds[s]):
                    u[s] = 0; continue
                R = kap[s] * B.thc_mp(f2m(cs[s][0]), f2m(cs[s][1]), 0, t) * B.thc_mp(f2m(ds[s][0]), f2m(ds[s][1]), 0, t) / t1p
                al, be = cs[s][0] - H, cs[s][1] - H; z = f2m(al) * t + f2m(be)
                a0 = 2 * I * mp.pi * f2m(al) + mp.diff(th1, z) / th1(z)
                c = F_u(cs[s][0] - H, cs[s][1] - H, t, y) + mp.pi * mp.log(y) - 2 * mp.pi * (mp.euler + mp.log(mp.pi))
                c = c - mp.pi * abs(a0) ** 2 * mp.exp(-2 * L)                       # Theorem 90's form (cA_t90)
                arg = 2 * mp.pi * L + c
                u[s] = mp.sqrt(arg) * R if arg > 0 else 0
            Mw = sum((u[s] * ED[s] for s in UNITS), mp.zeros(2, 2))
            for rn, Sr in RD.items():
                Y[(sec, rn)] = mp.matrix([[sum(((Ca.T * EPS * Sr * Cb)[m, n] * Mw[m, n] for m in range(2) for n in range(2)), mp.mpc(0))
                                           for Cb in BLOCKS] for Ca in BLOCKS])
        out = {}; Us = {}
        for (sec, rn), Ym in Y.items():
            Uu, Sv, Vv = mp.svd_c(Ym)
            order = sorted(range(3), key=lambda i: -Sv[i])
            sv = [Sv[i] for i in order]
            out["%s|L_2|%s" % (sec, rn)] = [sv[1] / sv[0], sv[2] / sv[0]]
            Us[(sec, rn)] = mp.matrix([[Uu[r, order[2 - c]] for c in range(3)] for r in range(3)])   # columns ascending
        for ru, rd in (("St", "S"), ("S", "St")):
            Vm = conj(Us[("up", ru)]).T * Us[("down", rd)]
            out["ckm|L_2|%s|%s" % (ru, rd)] = [abs(Vm[0, 1]), abs(Vm[1, 2]), abs(Vm[0, 2])]
        for k in KEYS:
            acc[k] = out[k] if acc[k] is None else [p + q for p, q in zip(acc[k], out[k])]
    return {k: [v / len(POINTS) for v in acc[k]] for k in KEYS}


def flat(f):
    return [x for k in KEYS for x in f[k]]
