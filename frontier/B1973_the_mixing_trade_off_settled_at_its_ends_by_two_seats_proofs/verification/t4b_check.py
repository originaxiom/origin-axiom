"""B1973: main's own check of A2-P879's T4(b) on frame C's code (2026-11-24): with the Theorem-90 channel weights removed, the residue
matrix M_res = sum_s R_s ED[s] (R_s = kap_s theta[c_s] theta[d_s] / (2 pi eta^3), exactly as B1945's parts builds it) is rank one in
the up and down sectors, with one shared left singular vector.  Then the weighted M_w (frame C's own) for comparison: s_L =
sqrt(1 - |<l_u|l_d>|^2) of the dominant left singular vectors."""
import sys, pathlib
ROOT = next((q for q in [*pathlib.Path(__file__).resolve().parents, pathlib.Path.cwd()] if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file()))
sys.path.insert(0, str(next((ROOT / "frontier").glob("B1945_*")) / "verification"))
import determinant_law as DL
from fractions import Fraction as Fr
mp = DL.mp; FM = DL.FM; B = DL.B; H = DL.H; f2m = DL.f2m
def mres(tx, ty, a, b, sec, weighted):
    mp.mp.dps = 40
    I, QI, QJ, QK, EPS, U, ED, BLOCKS = FM.setup()
    t = mp.mpc(mp.mpf(tx), mp.mpf(ty))
    eta = mp.exp(I * mp.pi * t / 12) * mp.qp(mp.exp(2 * I * mp.pi * t)); t1p = 2 * mp.pi * eta ** 3
    ql, qr = B.SIXY[B.SECTORS[sec][0]], B.SIXY[B.SECTORS[sec][1]]
    x = (ql * a, 2 * ql * b); yy = (qr * a, 2 * qr * b)
    ap, am = x[0] + yy[0], x[0] - yy[0]; bp, bm = (x[1] + yy[1]) / 2, (x[1] - yy[1]) / 2
    e = mp.exp(-2 * I * mp.pi * f2m(x[0])); kap = {"1": -I * e, "i": mp.mpf(-1), "j": -e, "k": I}
    cs = {"1": (ap + H, bp + H), "i": (ap + H, bp), "j": (ap, bp + H), "k": (ap, bp)}
    ds = {"1": (am + H, bm + H), "i": (am + H, bm), "j": (am, bm + H), "k": (am, bm)}
    if weighted: return DL.parts(tx, ty, a, b, sec)[1]
    M = mp.zeros(2, 2)
    for s in FM.UNITS:
        if FM.is_zero(cs[s]) or FM.is_zero(ds[s]): continue
        R = kap[s] * B.thc_mp(f2m(cs[s][0]), f2m(cs[s][1]), 0, t) * B.thc_mp(f2m(ds[s][0]), f2m(ds[s][1]), 0, t) / t1p
        M += R * ED[s]
    return M
def left(M):
    U_, S_, V_ = mp.svd_c(M); k = 0 if S_[0] >= S_[1] else 1
    return [U_[0, k], U_[1, k]], (min(S_[0], S_[1]) / max(S_[0], S_[1]))
pts = [(Fr(i, 5), Fr(j, 5)) for i in range(5) for j in range(5) if (i, j) != (0, 0)] + [(Fr(1, 7), Fr(3, 7)), (Fr(2, 7), Fr(1, 7)), (Fr(1, 3), Fr(1, 3)), (Fr(1, 4), Fr(3, 4)), (Fr(1, 6), Fr(1, 6)), (Fr(3, 8), Fr(1, 8))]
for weighted in (False, True):
    worst_rank = 0; worst_sL = 0; n = 0
    for (a, b) in pts:
        for ty in (2.0, 6.0):
            lu, ru = left(mres("0.13", ty, a, b, "up", weighted)); ld, rd = left(mres("0.13", ty, a, b, "down", weighted))
            ov = abs(mp.conj(lu[0]) * ld[0] + mp.conj(lu[1]) * ld[1]); sL = mp.sqrt(max(0, 1 - ov ** 2))
            if not weighted: worst_rank = max(worst_rank, ru, rd)
            worst_sL = max(worst_sL, sL); n += 1
    print("%s: %d cases; %s max s_L = %s" % ("weighted M_w (frame C)" if weighted else "unweighted residues", n,
          ("max mu2/mu1 = %s;" % mp.nstr(worst_rank, 3)) if not weighted else "", mp.nstr(worst_sL, 6)))
