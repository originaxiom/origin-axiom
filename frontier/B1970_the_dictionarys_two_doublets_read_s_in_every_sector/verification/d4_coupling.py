"""Review 86 mend (main, 2026-11-24): B1970's D4 tested conj(c_k), which is antiholomorphic whenever c_k is holomorphic
(a check that cannot fail).  The real check: frame C's UNNORMALISED coupling (the theta residues, before the channel weights,
which are real norms) under the reading S and under the conjugate reading S~ = eps conj(S) eps^T, by central finite
differences: |d Y / d conj(tau)| / |d Y / d tau| for every nonzero entry, up and down sectors, three points, two tau."""
import sys, pathlib
ROOT = next((q for q in [*pathlib.Path(__file__).resolve().parents, pathlib.Path.cwd()] if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file()))
sys.path.insert(0, str(next((ROOT / "frontier").glob("B1945_*")) / "verification"))
import determinant_law as DL
from fractions import Fraction as Fr
mp = DL.mp; FM = DL.FM; B = DL.B; H = DL.H; f2m = DL.f2m; te = FM.te
def Y_unnorm(t, a, b, sec, reading):
    I, QI, QJ, QK, EPS, U, ED, BLOCKS = FM.setup()
    eta = mp.exp(I * mp.pi * t / 12) * mp.qp(mp.exp(2 * I * mp.pi * t)); t1p = 2 * mp.pi * eta ** 3
    c3 = [te.ev(cc, t) for cc in te.B[1]]; S = c3[0] * QI + c3[1] * QJ + c3[2] * QK
    conj = lambda A: mp.matrix([[mp.conj(A[i, j]) for j in range(A.cols)] for i in range(A.rows)])
    Sr = S if reading == "S" else EPS * conj(S) * EPS.T
    ql, qr = B.SIXY[B.SECTORS[sec][0]], B.SIXY[B.SECTORS[sec][1]]
    x = (ql * a, 2 * ql * b); yy = (qr * a, 2 * qr * b)
    ap, am = x[0] + yy[0], x[0] - yy[0]; bp, bm = (x[1] + yy[1]) / 2, (x[1] - yy[1]) / 2
    e = mp.exp(-2 * I * mp.pi * f2m(x[0])); kap = {"1": -I * e, "i": mp.mpf(-1), "j": -e, "k": I}
    cs = {"1": (ap + H, bp + H), "i": (ap + H, bp), "j": (ap, bp + H), "k": (ap, bp)}
    ds = {"1": (am + H, bm + H), "i": (am + H, bm), "j": (am, bm + H), "k": (am, bm)}
    M = mp.zeros(2, 2)
    for s in FM.UNITS:
        if FM.is_zero(cs[s]) or FM.is_zero(ds[s]): continue
        M += kap[s] * B.thc_mp(f2m(cs[s][0]), f2m(cs[s][1]), 0, t) * B.thc_mp(f2m(ds[s][0]), f2m(ds[s][1]), 0, t) / t1p * ED[s]
    return mp.matrix([[sum(((Ca.T * EPS * Sr * Cb)[m, n] * M[m, n] for m in range(2) for n in range(2)), mp.mpc(0)) for Cb in BLOCKS] for Ca in BLOCKS])
mp.mp.dps = 40; h = mp.mpf(10) ** -12
for reading in ("S", "St"):
    worst = 0; best = mp.inf
    for (tx, ty) in ((0.13, 1.4), (-0.31, 2.2)):
        t = mp.mpc(tx, ty)
        for (a, b) in ((Fr(2, 5), Fr(4, 5)), (Fr(1, 5), Fr(2, 5)), (Fr(1, 2), Fr(1, 3))):
            for sec in ("up", "down"):
                Yx1, Yx0 = Y_unnorm(t + h, a, b, sec, reading), Y_unnorm(t - h, a, b, sec, reading)
                Yy1, Yy0 = Y_unnorm(t + 1j * h, a, b, sec, reading), Y_unnorm(t - 1j * h, a, b, sec, reading)
                for i in range(3):
                    for j in range(3):
                        dx = (Yx1[i, j] - Yx0[i, j]) / (2 * h); dy = (Yy1[i, j] - Yy0[i, j]) / (2 * h)
                        dbar = (dx + 1j * dy) / 2; dhol = (dx - 1j * dy) / 2
                        if abs(dhol) + abs(dbar) < mp.mpf(10) ** -20: continue
                        r = abs(dbar) / abs(dhol); worst = max(worst, r); best = min(best, r)
    print("reading %-2s: |dY/d conj tau| / |dY/d tau| over every nonzero entry: from %s to %s" % (reading, mp.nstr(best, 3), mp.nstr(worst, 3)), flush=True)
