"""B1945: frame C's coupling split into its pieces at one point (B1940's frame, unchanged), and B1659's determinant law
det Y = 4 det S det M tr(eps S M^T) checked on it (main, 2026-11-15; data-free)."""
import sys, pathlib
ROOT = pathlib.Path(__file__).resolve().parent / "main_tree"  # [copy: loader replaced, see MANIFEST.md]
pass  # [copy: loader replaced, see MANIFEST.md]
import frame_mp as FM
mp = FM.mp; B = FM.B; te = FM.te; H = FM.H; f2m = FM.f2m
def parts(tx, ty, a, b, sec):
    mp.mp.dps = int(30 + 2 * ty)
    I, QI, QJ, QK, EPS, U, ED, BLOCKS = FM.setup()
    t = mp.mpc(mp.mpf(tx), mp.mpf(ty)); y = mp.im(t)
    xr = ((float(tx) + 0.5) % 1.0) - 0.5; L = mp.mpf(FM.CR.canon(complex(xr, float(ty)))["L_2"])
    eta = mp.exp(I * mp.pi * t / 12) * mp.qp(mp.exp(2 * I * mp.pi * t)); t1p = 2 * mp.pi * eta ** 3
    th1 = lambda z: B.th_mp(1, z, t)
    c3 = [te.ev(cc, t) for cc in te.B[1]]; S = c3[0] * QI + c3[1] * QJ + c3[2] * QK
    conj = lambda A: mp.matrix([[mp.conj(A[i, j]) for j in range(A.cols)] for i in range(A.rows)])
    RD = {"S": S, "St": EPS * conj(S) * EPS.T}
    ql, qr = B.SIXY[B.SECTORS[sec][0]], B.SIXY[B.SECTORS[sec][1]]
    x = (ql * a, 2 * ql * b); yy = (qr * a, 2 * qr * b)
    ap, am = x[0] + yy[0], x[0] - yy[0]; bp, bm = (x[1] + yy[1]) / 2, (x[1] - yy[1]) / 2
    e = mp.exp(-2 * I * mp.pi * f2m(x[0])); kap = {"1": -I * e, "i": mp.mpf(-1), "j": -e, "k": I}
    cs = {"1": (ap + H, bp + H), "i": (ap + H, bp), "j": (ap, bp + H), "k": (ap, bp)}
    ds = {"1": (am + H, bm + H), "i": (am + H, bm), "j": (am, bm + H), "k": (am, bm)}
    u = {}
    for s in FM.UNITS:
        if FM.is_zero(cs[s]) or FM.is_zero(ds[s]): u[s] = 0; continue
        R = kap[s] * B.thc_mp(f2m(cs[s][0]), f2m(cs[s][1]), 0, t) * B.thc_mp(f2m(ds[s][0]), f2m(ds[s][1]), 0, t) / t1p
        al, be = cs[s][0] - H, cs[s][1] - H; z = f2m(al) * t + f2m(be)
        a0 = 2 * I * mp.pi * f2m(al) + mp.diff(th1, z) / th1(z)
        c = FM.F_u(cs[s][0] - H, cs[s][1] - H, t, y) + mp.pi * mp.log(y) - 2 * mp.pi * (mp.euler + mp.log(mp.pi))
        c = c - mp.pi * abs(a0) ** 2 * mp.exp(-2 * L); arg = 2 * mp.pi * L + c
        u[s] = mp.sqrt(arg) * R if arg > 0 else 0
    Mw = sum((u[s] * ED[s] for s in FM.UNITS), mp.zeros(2, 2))
    Ys = {}
    for rn, Sr in RD.items():
        Ys[rn] = mp.matrix([[sum(((Ca.T * EPS * Sr * Cb)[m, n] * Mw[m, n] for m in range(2) for n in range(2)), mp.mpc(0)) for Cb in BLOCKS] for Ca in BLOCKS])
    return RD, Mw, Ys, u, cs, ds
if __name__ == "__main__":
    from fractions import Fraction as Fr
    EPS = mp.matrix([[0, 1], [-1, 0]]); worst = 0; n = 0
    for (tx, ty) in (("0.13", 1.7), ("-0.31", 2.9), ("0.4", 6.0)):
        for (a, b) in ((Fr(1, 5), Fr(2, 5)), (Fr(2, 5), Fr(1, 5)), (Fr(0), Fr(3, 5)), (Fr(4, 5), Fr(4, 5))):
            for sec in ("up", "down"):
                RD, Mw, Ys, u, cs, ds = parts(tx, ty, a, b, sec)
                for rn in ("S", "St"):
                    S = RD[rn]; pair = sum(((EPS * S * Mw.T)[i, i] for i in range(2)), mp.mpc(0))
                    worst = max(worst, abs(mp.det(Ys[rn]) - 4 * mp.det(S) * mp.det(Mw) * pair) / abs(mp.det(Ys[rn]))); n += 1
    print("B1659's law det Y = 4 det S det M tr(eps S M^T) on frame C: worst relative residual %.1e over %d cases" % (worst, n))
