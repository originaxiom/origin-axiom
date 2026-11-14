"""X-SURVIVAL's S4 on main's frame, pointwise (P-831's test before any average): at each tau, averaged over the 24 points
of order 5, Delta(tau) = sum over sectors f of k_f [ln|det Y_f(W-)| - ln|det Y_f(W+)|] with the seat's weights
(k_up, k_down, k_lep) = (3, 3, 1) (leptons = the down sector at level 5, so k_down + k_lep = 4), and with the declared
moves changed: weights (1, 1, 1); the trace functional -Tr H^2 instead of ln det (H = Im tau Y^dag Y); the frame's
truncated weight instead of the exact. If Delta has one sign at every tau, every measure gives that sign."""
import sys, pathlib, math
import mpmath as mp

FM_DIR = next(q for q in pathlib.Path(__file__).resolve().parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file()) / "frontier" / "B1940_the_area_options_corrected_in_extended_precision" / "verification"
sys.path.insert(0, str(FM_DIR))
import frame_mp as FM
B, te, CR = FM.B, FM.te, FM.CR

def dets(tx, ty, exact=True):
    mp.mp.dps = int(30 + 2 * ty)
    I, QI, QJ, QK, EPS, U, ED, BLOCKS = FM.setup()
    t = mp.mpc(tx, ty); y = mp.im(t); H_ = FM.H
    L = mp.mpf(CR.canon(complex(((tx + 0.5) % 1) - 0.5, ty))["L_2"])
    eta = mp.exp(I * mp.pi * t / 12) * mp.qp(mp.exp(2 * I * mp.pi * t)); t1p = 2 * mp.pi * eta ** 3
    th1 = lambda z: B.th_mp(1, z, t)
    c3 = [te.ev(cc, t) for cc in te.B[1]]; S = c3[0] * QI + c3[1] * QJ + c3[2] * QK
    conj = lambda A: mp.matrix([[mp.conj(A[i, j]) for j in range(A.cols)] for i in range(A.rows)])
    RD = {"S": S, "St": EPS * conj(S) * EPS.T}
    acc = {}
    for a, b in FM.POINTS:
        for sec in ("up", "down"):
            ql, qr = B.SIXY[B.SECTORS[sec][0]], B.SIXY[B.SECTORS[sec][1]]
            x = (ql * a, 2 * ql * b); yy = (qr * a, 2 * qr * b)
            ap, am = x[0] + yy[0], x[0] - yy[0]; bp, bm = (x[1] + yy[1]) / 2, (x[1] - yy[1]) / 2
            e = mp.exp(-2 * I * mp.pi * FM.f2m(x[0])); kap = {"1": -I * e, "i": mp.mpf(-1), "j": -e, "k": I}
            cs = {"1": (ap + H_, bp + H_), "i": (ap + H_, bp), "j": (ap, bp + H_), "k": (ap, bp)}
            ds = {"1": (am + H_, bm + H_), "i": (am + H_, bm), "j": (am, bm + H_), "k": (am, bm)}
            u = {}
            for s in FM.UNITS:
                if FM.is_zero(cs[s]) or FM.is_zero(ds[s]): u[s] = 0; continue
                R = kap[s] * B.thc_mp(FM.f2m(cs[s][0]), FM.f2m(cs[s][1]), 0, t) * B.thc_mp(FM.f2m(ds[s][0]), FM.f2m(ds[s][1]), 0, t) / t1p
                al, be = cs[s][0] - H_, cs[s][1] - H_; z = FM.f2m(al) * t + FM.f2m(be)
                a0 = 2 * I * mp.pi * FM.f2m(al) + mp.diff(th1, z) / th1(z)
                c = FM.F_u(cs[s][0] - H_, cs[s][1] - H_, t, y) + mp.pi * mp.log(y) - 2 * mp.pi * (mp.euler + mp.log(mp.pi))
                if exact: c = c - mp.pi * abs(a0) ** 2 * mp.exp(-2 * L)
                arg = 2 * mp.pi * L + c; u[s] = mp.sqrt(arg) * R if arg > 0 else 0
            Mw = sum((u[s] * ED[s] for s in FM.UNITS), mp.zeros(2, 2))
            for rn, Sr in RD.items():
                Y = mp.matrix([[sum(((Ca.T * EPS * Sr * Cb)[m, n] * Mw[m, n] for m in range(2) for n in range(2)), mp.mpc(0)) for Cb in BLOCKS] for Ca in BLOCKS])
                Hm = y * conj(Y).T * Y
                ld = mp.log(abs(mp.det(Y))) * 2 + 3 * mp.log(y)
                tr2 = mp.re(sum(Hm[i, j] * Hm[j, i] for i in range(3) for j in range(3)))
                for k, v in (("ld", ld), ("tr2", tr2)):
                    acc[(sec, rn, k)] = acc.get((sec, rn, k), 0) + v / len(FM.POINTS)
    return acc

def deltas(acc):
    out = {}
    for name, (ku, kd) in (("weights 3,3,1", (3, 4)), ("weights 1,1,1", (1, 2))):
        out["ln det, " + name] = ku * (acc[("up", "St", "ld")] - acc[("up", "S", "ld")]) + kd * (acc[("down", "S", "ld")] - acc[("down", "St", "ld")])
        out["-Tr H^2, " + name] = -(ku * (acc[("up", "St", "tr2")] - acc[("up", "S", "tr2")]) + kd * (acc[("down", "S", "tr2")] - acc[("down", "St", "tr2")]))
    return out

if __name__ == "__main__":
    import random
    rng = random.Random(1939); pts = []
    for yv in (0.9, 1.2, 1.6, 2.2, 3.0, 4.5, 6.0, 9.0):
        for _ in range(4):
            x = rng.uniform(-0.5, 0.5)
            if x * x + yv * yv >= 1: pts.append((x, yv))
    signs = {}
    for x, yv in pts:
        for exact in (True, False):
            d = deltas(dets(x, yv, exact))
            for k, v in d.items():
                kk = k + (", exact weight" if exact else ", truncated weight")
                signs.setdefault(kk, []).append(float(v))
    for k, v in sorted(signs.items()):
        print("%-45s  positive at %2d of %2d points  min %+.3e  max %+.3e" % (k, sum(x > 0 for x in v), len(v), min(v), max(v)))
