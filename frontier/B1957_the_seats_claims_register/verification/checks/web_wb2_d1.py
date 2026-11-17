"""B1957: the web seat's W-B2, stages 3 and 4 (frame D1 with only the Szego zero moved), rebuilt by main on its own
frame functions (B1656's bilinear and theta functions; B1945's frame C).  Data-free; no mixing is formed.
The seat's placement, from its note: M_alt(h)(u) = v_x(u) v_y(u)^T / theta_1(u + h, tau), with
v_x(u) = (theta[x](u, 2 tau), -i theta[x + (1/2, 0)](u, 2 tau)), x = (q a, 2 q b), and h = c q_H w, w = a tau + b.
 D1  U0: frame C's bilinear (main's bil_mp) is v_x v_y^T / theta_1 at h = 0.
 D2  E, by hand and by number: shifting a theta's argument by -h is a change of characteristic times one factor
     exp(2 pi i eps (u + beta - delta) - i pi eps^2 2 tau), eps = c q_H a/2, delta = c q_H b, the same for both
     components.  So the residue at the pole u = -h is frame C's residue at the charges q' = q - c q_H/2 times one
     scalar, for every c; and off the pole M_alt(h)(u - h) is frame C's bilinear at q' times a scalar of modulus
     const * exp(k Im u), k = -2 pi c q_H a.
 D3  the residue-level coupling's ratio sigma_2/sigma_1 under tau -> tau + 1, tau -> -1/tau, w -> w + 1, w -> w + tau,
     for c = +-2 and c = +-1 (the point transported; with and without reduction mod 1).
 D4  the flat unitary metric exp(4 pi Im h Im z/Im tau) times |M_alt(h)(z - h)|^2 is |frame C's bilinear at q'|^2
     times a constant, at every z: so with that metric the norms are frame C's at q', and with a flat norm over a
     cell they depend on where the cell is cut and are not periodic in the Higgs's point.
 D5  R: the reading S at h against the reading S~ at -h.
 D6  B1947's twisted triplet (main's own S_comps, both of its conventions) on the corrected placement at c = +2: the
     change of sigma_2/sigma_1 under tau -> tau + 1 with the point transported."""
import sys, pathlib, functools, math
from fractions import Fraction as Fr
import numpy as np
print = functools.partial(print, flush=True)
sys.path.insert(0, str(next(q for q in pathlib.Path(__file__).resolve().parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file()) / "frontier/B1957_the_seats_claims_register/verification/checks"))
import wb2_stage3_on_main as W
FM, B, te, mp = W.FM, W.B, W.te, W.mp; mp.mp.dps = 34; I = mp.mpc(0, 1); f2m = FM.f2m
SEC = {"up": (1, -4, 3), "down": (1, 2, -3), "lepton": (-3, 6, -3)}
_, QI, QJ, QK, EPS, U, ED, BLOCKS = FM.setup()


def vvec(x, u, t): return mp.matrix([B.thc_mp(x[0], x[1], u, 2 * t), -I * B.thc_mp(x[0] + mp.mpf(1) / 2, x[1], u, 2 * t)])
def chars(q, a, b): return (f2m(q * a), f2m(2 * q * b))
def malt(x, y, h, u, t): return vvec(x, u, t) * vvec(y, u, t).T / B.th_mp(1, u + h, t)
def t1p(t): return 2 * mp.pi * (mp.exp(I * mp.pi * t / 12) * mp.qp(mp.exp(2 * I * mp.pi * t))) ** 3
def readings(t):
    c3 = [te.ev(cc, t) for cc in te.B[1]]; S = c3[0] * QI + c3[1] * QJ + c3[2] * QK; conj = lambda A: mp.matrix([[mp.conj(A[i, j]) for j in range(2)] for i in range(2)]); return {"S": S, "St": EPS * conj(S) * EPS.T}
def couple(Sr, M): return np.array([[complex(sum(((Ca.T * EPS * Sr * Cb)[m, n] * M[m, n] for m in range(2) for n in range(2)), mp.mpc(0))) for Cb in BLOCKS] for Ca in BLOCKS])
def r21(Y): s = np.linalg.svd(Y, compute_uv=False); return s[1] / s[0]
def d1(t, a, b, sec, c, rd="S"):
    """the residue-level coupling of frame D1 at the pole u = -h"""
    ql, qr, qh = SEC[sec]; h = c * qh * (f2m(a) * t + f2m(b)); return couple(readings(t)[rd], vvec(chars(ql, a, b), -h, t) * vvec(chars(qr, a, b), -h, t).T / t1p(t))


if __name__ == "__main__":
    t = mp.mpc("0.13", "1.7"); PTS = [(Fr(2, 5), Fr(4, 5)), (Fr(1, 5), Fr(2, 5)), (Fr(0), Fr(1, 5)), (Fr(3, 5), Fr(1, 5))]
    # D1
    w = 0
    for k in range(6):
        u = mp.mpc(0.11 + 0.07 * k, 0.05 - 0.09 * k); x, y = chars(1, *PTS[0]), chars(-4, *PTS[0]); Bm = B.bil_mp(x, y, u, t); Fm = malt(x, y, 0, u, t)
        w = max(w, max(abs(Bm[i][j] - Fm[i, j]) / abs(Bm[i][j]) for i in range(2) for j in range(2)))
    print("D1 (U0): main's bilinear against v_x v_y^T / theta_1 at six points u: largest relative difference %s" % mp.nstr(w, 3))
    # D2
    wE = wk = 0; ks = []
    for sec, (ql, qr, qh) in SEC.items():
        for (a, b) in PTS:
            for c in (2, -2, 1, -1):
                Yd = d1(t, a, b, sec, c); Yc = W.coupling("0.13", 1.7, a, b, ql - Fr(c * qh, 2), qr - Fr(c * qh, 2), True)["S"]; wE = max(wE, W.upto(Yd, Yc))
            c = 2; h = c * qh * (f2m(a) * t + f2m(b)); x, y = chars(ql, a, b), chars(qr, a, b); xp, yp = chars(ql - Fr(c * qh, 2), a, b), chars(qr - Fr(c * qh, 2), a, b); lg = []
            for u in (mp.mpc("0.21", "0.13"), mp.mpc("-0.17", "0.31"), mp.mpc("0.05", "-0.22")):
                Md = malt(x, y, h, u - h, t); Mc = B.bil_mp(xp, yp, u, t); r = [Md[i, j] / Mc[i][j] for i in range(2) for j in range(2)]; wk = max(wk, max(abs(z / r[0] - 1) for z in r)); lg.append((mp.im(u), mp.log(abs(r[0]))))
            k = (lg[1][1] - lg[0][1]) / (lg[1][0] - lg[0][0]); k2 = (lg[2][1] - lg[0][1]) / (lg[2][0] - lg[0][0]); pred = -2 * mp.pi * c * qh * f2m(a); ks.append((sec, str(a), float(k), float(pred), float(abs(k - pred) + abs(k2 - pred))))
    print("D2 (E): the residue-level coupling of D1 against frame C at q' = q - c q_H/2, up to one scalar: 3 sectors, 4 points, c = 2, -2, 1, -1: largest relative difference %.1e" % wE)
    print("D2 (off the pole, c = +2): M_alt(h)(u - h) is frame C's bilinear at q' times one scalar on all four entries (to %s); the scalar's modulus is exp(k Im u) with k = -2 pi c q_H a: largest |k - prediction| %.1e; k for up at the mark %.3f (the seat: about -15)" % (mp.nstr(wk, 3), max(x[4] for x in ks), next(x[2] for x in ks if x[0] == "up" and x[1] == "2/5")))
    # D3
    red = lambda v: v - math.floor(v)
    for c in (2, -2, 1, -1):
        out = {"T": [], "T reduced": [], "S": [], "S reduced": [], "w + 1": [], "w + tau": []}
        for sec in SEC:
            for (a, b) in PTS:
                r0 = r21(d1(t, a, b, sec, c)); bb = b - a
                out["T"].append(abs(r21(d1(t + 1, a, bb, sec, c)) / r0 - 1)); out["T reduced"].append(abs(r21(d1(t + 1, a, red(bb), sec, c)) / r0 - 1))
                out["S"].append(abs(r21(d1(-1 / t, -b, a, sec, c)) / r0 - 1)); out["S reduced"].append(abs(r21(d1(-1 / t, red(-b), a, sec, c)) / r0 - 1))
                out["w + 1"].append(abs(r21(d1(t, a, b + 1, sec, c)) / r0 - 1)); out["w + tau"].append(abs(r21(d1(t, a + 1, b, sec, c)) / r0 - 1))
        print("D3 c = %+d: sigma_2/sigma_1 moves by at most: %s" % (c, "; ".join("%s %.1e" % (k, max(v)) for k, v in out.items())))
    # D4
    wm = 0
    for sec, (ql, qr, qh) in SEC.items():
        a, b = PTS[0]; c = 2; h = c * qh * (f2m(a) * t + f2m(b)); x, y = chars(ql, a, b), chars(qr, a, b); xp, yp = chars(ql - Fr(c * qh, 2), a, b), chars(qr - Fr(c * qh, 2), a, b); vals = []
        for z in (mp.mpc("0.21", "0.13"), mp.mpc("-0.17", "0.31"), mp.mpc("0.05", "-0.22"), mp.mpc("0.4", "0.6"), mp.mpc("0.4", "0.6") + t):
            Md = malt(x, y, h, z - h, t); Mc = B.bil_mp(xp, yp, z, t); g = mp.exp(4 * mp.pi * mp.im(h) * mp.im(z) / mp.im(t)); vals.append(g * abs(Md[0, 0]) ** 2 / abs(Mc[0][0]) ** 2)
        wm = max(wm, max(abs(v / vals[0] - 1) for v in vals)); flat = abs(malt(x, y, h, mp.mpc("0.4", "0.6") + t - h, t)[0, 0]) ** 2 / abs(malt(x, y, h, mp.mpc("0.4", "0.6") - h, t)[0, 0]) ** 2; cflat = abs(B.bil_mp(xp, yp, mp.mpc("0.4", "0.6") + t, t)[0][0]) ** 2 / abs(B.bil_mp(xp, yp, mp.mpc("0.4", "0.6"), t)[0][0]) ** 2
        print("D4 %s, c = +2, the mark: with the metric exp(4 pi Im h Im z/Im tau), |D1|^2/|frame C at q'|^2 is one constant at five points, one of them a lattice translate (to %s); without it, |D1|^2 changes under z -> z + tau by a factor %s where frame C's changes by %s" % (sec, mp.nstr(max(abs(v / vals[0] - 1) for v in vals), 3), mp.nstr(flat, 6), mp.nstr(cflat, 6)))
    # D5
    wr = min(W.upto(d1(t, a, b, sec, 2, "S"), d1(t, a, b, sec, -2, "St")) for sec in SEC for (a, b) in PTS); wr2 = min(abs(r21(d1(t, a, b, sec, 2, "S")) / r21(d1(t, a, b, sec, -2, "St")) - 1) for sec in SEC for (a, b) in PTS)
    print("D5 (R): reading S at h against reading S~ at -h: least distance up to a scalar %.3f; least relative difference of sigma_2/sigma_1 %.1e" % (wr, wr2))

    sys.path.insert(0, str(next((W.ROOT / "frontier").glob("B1947_*")) / "verification")); import d1_coupling as DC
    for v2, name in ((False, "the card's twist (q_H a, 2 q_H b)"), (True, "the amended twist (q_H a, q_H b)")):
        DC.V2 = v2; ch = []
        for sec, (ql, qr, qh) in SEC.items():
            for (a, b) in PTS:
                def y(tt, aa, bb):
                    c3 = DC.S_comps(tt, qh, aa, bb); S = c3[0] * QI + c3[1] * QJ + c3[2] * QK; h = 2 * qh * (f2m(aa) * tt + f2m(bb)); return couple(S, vvec(chars(ql, aa, bb), -h, tt) * vvec(chars(qr, aa, bb), -h, tt).T / t1p(tt))
                ch.append(abs(math.log(r21(y(t + 1, a, b - a)) / r21(y(t, a, b)))))
        nz = [x for x in ch if x > 1e-9]
        print("D6 %s on the corrected placement: |d ln sigma_2/sigma_1| under tau -> tau + 1 over 3 sectors and 4 points: %d of %d change, by %.2f to %.2f (the point with a = 0 does not change: %s)" % (name, len(nz), len(ch), min(nz), max(nz), all(x < 1e-9 for x, (sec_, pt) in zip(ch, [(s_, p_) for s_ in SEC for p_ in PTS]) if pt[0] == 0)))
