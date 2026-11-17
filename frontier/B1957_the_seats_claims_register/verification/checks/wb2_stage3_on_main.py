"""B1957: the web seat's W-B2, stage 3, the statements that concern frame C at shifted charges, recomputed on main's
frame code (B1945's determinant_law.parts, copied here with the charges passed in and the norm weights optional).
Data-free.  The seat's identity E says frame D1 (the Higgs's twist in its own Szego factor) equals, at residue level,
frame C at q' = q - c q_H / 2; main checked E by a hand reduction (harvest row 1842).  Given E, the seat's further
statements are statements about frame C at shifted charges, and are tested here:
 S1  c = -2: the charges (-q_R, -q_L); the coupling there is frame C's transposed, sector by sector.
 S2  so the singular values are frame C's, and the mixing is frame C's read with right vectors in place of left.
 S3  c = +2: up (-2, -7), down (4, 5), leptons (0, 9); the leptons copy the down rows transposed at the 24 points of
     order 5, and not at a point of order 7.
 S4  c = +2 is a new coupling: how far its sigma_2/sigma_1 is from frame C's."""
import sys, pathlib, functools
from fractions import Fraction as Fr
import numpy as np
print = functools.partial(print, flush=True)
ROOT = next(q for q in pathlib.Path(__file__).resolve().parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
sys.path.insert(0, str(ROOT / "frontier/B1945_the_frames_cusp_exponents/verification")); import determinant_law as DL
FM = DL.FM; mp = DL.mp; B = FM.B; te = FM.te; H = FM.H; f2m = FM.f2m


def coupling(tx, ty, a, b, ql, qr, residue=True, as_mp=False):
    """frame C's 3 x 3 coupling for both Higgs readings at charges (ql, qr); with residue=True the norm weights are 1;
    with as_mp=True the matrices are returned in extended precision (for use high in the cusp)"""
    mp.mp.dps = int(30 + 2 * ty); I, QI, QJ, QK, EPS, U, ED, BLOCKS = FM.setup()
    t = mp.mpc(mp.mpf(tx), mp.mpf(ty)); y = mp.im(t); xr = ((float(tx) + 0.5) % 1.0) - 0.5; L = mp.mpf(FM.CR.canon(complex(xr, float(ty)))["L_2"])
    eta = mp.exp(I * mp.pi * t / 12) * mp.qp(mp.exp(2 * I * mp.pi * t)); t1p = 2 * mp.pi * eta ** 3; th1 = lambda z: B.th_mp(1, z, t)
    c3 = [te.ev(cc, t) for cc in te.B[1]]; S = c3[0] * QI + c3[1] * QJ + c3[2] * QK
    conj = lambda A: mp.matrix([[mp.conj(A[i, j]) for j in range(A.cols)] for i in range(A.rows)]); RD = {"S": S, "St": EPS * conj(S) * EPS.T}
    x = (ql * a, 2 * ql * b); yy = (qr * a, 2 * qr * b); ap, am = x[0] + yy[0], x[0] - yy[0]; bp, bm = (x[1] + yy[1]) / 2, (x[1] - yy[1]) / 2
    e = mp.exp(-2 * I * mp.pi * f2m(x[0])); kap = {"1": -I * e, "i": mp.mpf(-1), "j": -e, "k": I}
    cs = {"1": (ap + H, bp + H), "i": (ap + H, bp), "j": (ap, bp + H), "k": (ap, bp)}; ds = {"1": (am + H, bm + H), "i": (am + H, bm), "j": (am, bm + H), "k": (am, bm)}; u = {}
    for s in FM.UNITS:
        if FM.is_zero(cs[s]) or FM.is_zero(ds[s]): u[s] = 0; continue
        R = kap[s] * B.thc_mp(f2m(cs[s][0]), f2m(cs[s][1]), 0, t) * B.thc_mp(f2m(ds[s][0]), f2m(ds[s][1]), 0, t) / t1p
        if residue: u[s] = R; continue
        al, be = cs[s][0] - H, cs[s][1] - H; z = f2m(al) * t + f2m(be); a0 = 2 * I * mp.pi * f2m(al) + mp.diff(th1, z) / th1(z)
        c = FM.F_u(cs[s][0] - H, cs[s][1] - H, t, y) + mp.pi * mp.log(y) - 2 * mp.pi * (mp.euler + mp.log(mp.pi)) - mp.pi * abs(a0) ** 2 * mp.exp(-2 * L); arg = 2 * mp.pi * L + c
        u[s] = mp.sqrt(arg) * R if arg > 0 else 0
    Mw = sum((u[s] * ED[s] for s in FM.UNITS), mp.zeros(2, 2)); out = {}
    for rn, Sr in RD.items():
        Y = mp.matrix([[sum(((Ca.T * EPS * Sr * Cb)[m, n] * Mw[m, n] for m in range(2) for n in range(2)), mp.mpc(0)) for Cb in BLOCKS] for Ca in BLOCKS])
        out[rn] = Y if as_mp else np.array([[complex(Y[i, j]) for j in range(3)] for i in range(3)])
    return out


def upto(A, Bm):
    """the distance of A from a scalar multiple of Bm, relative"""
    c = np.vdot(Bm, A) / np.vdot(Bm, Bm); return float(np.abs(A - c * Bm).max() / np.abs(A).max())


sv = lambda M: (lambda s: s / s[0])(np.linalg.svd(M, compute_uv=False))
SIX = {"up": (1, -4), "down": (1, 2), "lepton": (-3, 6)}; QH = {"up": 3, "down": -3, "lepton": -3}
PTS = [(Fr(i, 5), Fr(j, 5)) for i in range(5) for j in range(5) if (i, j) != (0, 0)]

if __name__ == "__main__":
    tx, ty = "0.13", 1.7; MARK, TWIN = (Fr(2, 5), Fr(4, 5)), (Fr(1, 5), Fr(2, 5))
    for res, lab in ((True, "residue level"), (False, "with the norms")):
        w1 = w2 = 0.0
        for sec, (ql, qr) in SIX.items():
            for pt in (MARK, TWIN):
                Y0 = coupling(tx, ty, *pt, ql, qr, res); Y1 = coupling(tx, ty, *pt, -qr, -ql, res)
                for rd in ("S", "St"):
                    w1 = max(w1, upto(Y1[rd], Y0[rd].T)); w2 = max(w2, np.abs(sv(Y1[rd]) - sv(Y0[rd])).max())
        print("S1 (%s): frame C at (-q_R, -q_L) against the transpose of frame C at (q_L, q_R), three sectors, two points, both readings: up to a scalar %.1e; singular-value ratios %.1e" % (lab, w1, w2))
    worst = 0.0
    for pt in (MARK, TWIN):
        Yu, Yd = coupling(tx, ty, *pt, *SIX["up"]), coupling(tx, ty, *pt, *SIX["down"])
        for ru, rdn in (("St", "S"), ("S", "St"), ("S", "S"), ("St", "St")):
            L = lambda M: np.linalg.svd(M)[0][:, ::-1]; Rv = lambda M: np.linalg.svd(M)[2].conj().T[:, ::-1]
            Vl = np.abs(L(Yu[ru]).conj().T @ L(Yd[rdn])); Vr = np.abs(Rv(Yu[ru]).conj().T @ Rv(Yd[rdn])); worst = max(worst, np.abs(Vl[1:, 1:] - Vr[1:, 1:]).max())
    print("S2: the mixing read with right singular vectors in place of left (which is the c = -2 frame's), residue level: the massive 2 x 2 block of |V| differs from frame C's by up to %.2f (the seat: up to 0.84)" % worst)
    plus = {s: (q[0] - QH[s], q[1] - QH[s]) for s, q in SIX.items()}
    print("S3: the c = +2 charges q - q_H: %s (the seat: up (-2, -7), down (4, 5), leptons (0, 9))" % plus)
    w5 = max(max(upto(coupling(tx, ty, *pt, *plus["lepton"])[rd], coupling(tx, ty, *pt, *plus["down"])[rd].T) for rd in ("S", "St")) for pt in PTS)
    w5s = max(max(np.abs(sv(coupling(tx, ty, *pt, *plus["lepton"])[rd]) - sv(coupling(tx, ty, *pt, *plus["down"])[rd])).max() for rd in ("S", "St")) for pt in (MARK, TWIN, (Fr(0), Fr(1, 5)), (Fr(3, 5), Fr(1, 5))))
    p7 = (Fr(1, 7), Fr(3, 7)); w7 = max(np.abs(sv(coupling(tx, ty, *p7, *plus["lepton"])[rd]) - sv(coupling(tx, ty, *p7, *plus["down"])[rd])).max() for rd in ("S", "St"))
    print("    at the 24 points of order 5 the lepton coupling against the transpose of the down coupling, up to a scalar: %.1e (singular-value ratios at four points: %.1e); at (1/7, 3/7) the singular-value ratios differ by %.2f" % (w5, w5s, w7))
    d = 0.0
    for sec in SIX:
        for pt in (MARK, TWIN):
            a_, b_ = coupling(tx, ty, *pt, *plus[sec]), coupling(tx, ty, *pt, *SIX[sec])
            d = max(d, max(abs(sv(a_[rd])[1] / sv(b_[rd])[1] - 1) for rd in ("S", "St")))
    print("S4: c = +2 against frame C, residue level, three sectors at the mark and the twin: sigma_2/sigma_1 differs by up to %.2f in ratio (the seat: up to 2.4)" % d)
