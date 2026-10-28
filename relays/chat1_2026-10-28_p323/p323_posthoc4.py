"""P-323's post hoc read-outs, fourth part (POST HOC, labelled; written after this seat's read-only referee of the result
note, whose recounts gave numbers the note's corrections would cite; each is computed here, from the committed census
(762784a71) and the sealed script's functions, before the note cites it).  No cell.
  S1  C0(f)'s 360 checks (60 calibration points x 3 Higgs x 2 horocycles): the noise estimate max(sigma at the two points)
      over the T-step's deviation, its minimum and median, and how often the 1e-12 floor exceeds 10 sigma (C0(f)'s own
      counts recomputed first);
  S2  C0(e) with the noise estimate divided by 1, 20, 100 and 1000: the frozen-(S, S) combinations classed HARMONIC, out of
      those with a reading (at 1 the cells' 189 of 5 603 must come back);
  S3  frozen (S, S): the valid centres binned by |D(r2)| / sigma_D, with their count, D(r1)/D(r2) at the 10th, 50th and 90th
      percentiles, and their classes;
  S4  the twelve lines where theta_M is HARMONIC: over every stencil point (6 centres x 13 points x 2 sectors), the signed
      range of c_1 - c_j, and the pairing's precision, max |c_1 - c_i| and max |c_j - c_k|;
  S5  the rule's D wraps the total phase difference.  Per quantity: the valid centres with a stencil point whose per-factor
      wrapped differences sum past pi in absolute value, the largest such sum, how many valid centres change class when D is
      computed from the per-factor sums, and how many verdicts change;
  S6  H2's exceptions by slope and Higgs (from p323_cells.json);
  S7  H1's 219 UNDETERMINED on the lines whose norms are equal in pairs (p323_posthoc3.py's R1), split by theta_M's verdict.
    python3 -B p323_posthoc4.py > p323_posthoc4_out.txt"""
import sys, json, importlib.util, pathlib
from fractions import Fraction as Fr
import numpy as np

HERE = pathlib.Path(__file__).resolve().parent
sp = importlib.util.spec_from_file_location("p323", HERE / "p323_strong_angle.py"); P = importlib.util.module_from_spec(sp)
sys.modules["p323"] = P; sp.loader.exec_module(P)
KEYS = {"Y": ("hh", "Sig", "uh"), "H": ("uh",), "M": ("Sig",)}
CLS = ("U", "N", "H", "H'", "Un")


def classify_d(d, sig):
    """P.classify with the twelve stencil differences d (..., 12) given, instead of wrap(th[..., 1:] - th[..., :1])"""
    D1, D2 = d[..., :6].mean(-1), d[..., 6:].mean(-1)
    sD = sig.max(-1)
    with np.errstate(divide="ignore", invalid="ignore"):
        ratio = D1 / D2
    Un = sD > 1e-9
    N = ~Un & (np.abs(D1) > 1e-6) & (ratio >= 3) & (ratio <= 5)
    H = ~Un & ~N & (np.abs(D1) < 1e-8) & (sD <= 1e-10)
    Hp = ~Un & ~N & ~H & (ratio >= 30) & (ratio <= 250) & (np.abs(D2) >= 100 * sD)
    return D1, D2, sD, np.where(Un, 4, np.where(N, 1, np.where(H, 2, np.where(Hp, 3, 0)))), ratio


def per_factor_d(fs, which):
    """the sum over the quantity's factors of each factor's wrapped difference from the centre; point axis moved last"""
    tot = 0
    for f in fs:
        for k in KEYS[which]:
            ph = np.angle(f[k][0]); tot = tot + P.wrap(ph[:, :, 1:] - ph[:, :, :1])
    return np.moveaxis(tot, 2, -1)


def main():
    g = P.frame(); B, tic = g["B"], g["tic"]
    d = np.load(P.OUT_CENSUS); idx = json.loads(P.OUT_INDEX.read_text())
    cells = json.loads((HERE / "p323_cells.json").read_text())
    R, C, L, H = d["R"], d["C"], d["L"], d["H"]
    nl, nh = R.shape[0], len(P.HIGGS)
    Q = P.all_quantities(R, C, L, H)
    QP = [P.all_quantities(*P.perturbed((R, C, L, H), p), keep=False) for p in range(P.NPERT)]
    sig = {k: np.max([np.abs(P.wrap(qp[k][0] - Q[k][0])) for qp in QP], axis=0) for k in Q if k[0] != "clamp"}
    clamp_ok = {hr: (Q[("clamp", hr)] == Q[("clamp", hr)][:, :, :1]).all(axis=(2, 3, 4)) for hr in range(2)}

    # S1: C0(f), as the cells compute it
    cR, cC, cL, cH = d["calR"], d["calC"], d["calL"], d["calH"]
    tl = idx["ten"]

    def theta_points(Rp, Cp, Lp, Hp, hr):
        u, _ = P.weights(Rp, Cp, Lp[..., hr]); return P.theta_of(P.factors(u, Hp, 1, 0), "Y")
    devs, sigs = [], []
    for hr in range(2):
        thc = theta_points(cR, cC, cL, cH, hr)
        thb = Q[("Y", P.SM, hr)][0][tl][:, :, 0]
        sc = np.max([np.abs(P.wrap(theta_points(*P.perturbed((cR, cC, cL, cH), p), hr) - thc)) for p in range(P.NPERT)], axis=0)
        sb = sig[("Y", P.SM, hr)][tl][:, :, 0]
        for hn in P.CAL_HIGGS:
            hi = P.HIGGS.index(hn)
            devs.append(np.abs(P.wrap(thc[:, :, hi] - thb[:, :, hi] - P.T_SHIFT)).ravel())
            sigs.append(np.maximum(sc[:, :, hi], sb[:, :, hi]).ravel())
    dev, s = np.concatenate(devs), np.concatenate(sigs)
    tol = 10 * s + 1e-12
    print("S1 C0(f) recomputed: %d checks, %d failing, worst deviation %.2e, worst deviation/tolerance %.4f (the cells: 360, 0, 2.6e-12, 0.0045)"
          % (dev.size, int((dev > tol).sum()), dev.max(), (dev / tol).max()))
    with np.errstate(divide="ignore"):
        rs = s / dev
    print("   sigma / deviation: minimum %.1f, median %.0f (%d checks with deviation exactly 0); checks where 1e-12 > 10 sigma: %d"
          % (rs.min(), float(np.median(rs)), int((dev == 0).sum()), int((1e-12 > 10 * s).sum())))

    # J at the centres: the cells' code, all four readings
    J = {}
    for hr in range(2):
        u0, _ = P.weights(R[:, :, 0], C[:, :, 0], L[:, :, 0, hr])
        M0 = np.einsum("...s,sab->...ab", u0, np.array([B.EDUAL[s_] for s_ in P.UNITS]))
        for name, (cu, cd) in P.READINGS.items():
            Ys = []
            for sec, cj in ((0, cu), (1, cd)):
                hv = np.conj(H[:, :, 0]) if cj else H[:, :, 0]
                S = hv[..., 0, None, None] * B.QI + hv[..., 1, None, None] * B.QJ + hv[..., 2, None, None] * B.QK
                Mx = M0[:, :, sec][:, :, None]
                Y = np.zeros(S.shape[:-2] + (3, 3), complex)
                for a_, Ca in enumerate(B.BLOCKS):
                    for b_, Cb in enumerate(B.BLOCKS):
                        Y[..., a_, b_] = np.einsum("...ij,...ij->...", Ca.T @ B.EPS @ S @ Cb, np.broadcast_to(Mx, S.shape))
                Ys.append(Y)
            JJ = np.zeros((nl, 6, nh))
            for li in range(nl):
                for ci in range(6):
                    for hi in range(nh):
                        JJ[li, ci, hi] = tic.ckm_left(Ys[0][li, ci, hi], Ys[1][li, ci, hi])[3]
            J[(name, hr)] = JJ

    def vc(key, hr, phase_free, jcut, scale=1.0):
        """the cells' vc(): validity (with the J cut where the cells apply it), the rule's classes, and the per-factor sums"""
        th, fs = Q[key]
        which = "M" if key[0] == "M" else ("H" if key[0] == "H" else "Y")
        cok = clamp_ok[0][..., None] if key[0] == "M" else clamp_ok[hr][..., None] * np.ones((1, 1, nh), bool)
        valid, _ = P.validity(fs, which, phase_free, cok)
        pf = per_factor_d(fs, which)
        if key[0] == "M":
            valid = valid[..., 0]; pf = pf[:, :, 0]
        if jcut is not None:
            valid = valid & (np.abs(jcut) > 1e-9)
        sg = np.moveaxis(sig[key], 2, -1) / scale
        D1, D2, sD, cls, ratio = P.classify(np.moveaxis(th, 2, -1), sg)
        cls_pf = classify_d(pf, sg)[3]
        return valid, D1, D2, sD, cls, ratio, pf, cls_pf

    def verd(valid, cls, key):
        if key[0] == "M":
            return P.verdicts(valid, cls)
        return P.verdicts(np.moveaxis(valid, 1, -1), np.moveaxis(cls, 1, -1))

    # S2
    print("S2 C0(e), frozen (S, S), the noise estimate divided by k:")
    for k in (1, 20, 100, 1000):
        nH = nwr = 0
        for hr in range(2):
            valid, D1, D2, sD, cls, ratio, pf, cls_pf = vc(("Yf", "S,S", hr), hr, False, None, scale=k)
            vd = verd(valid, cls, ("Yf",))
            nH += int((vd == "HARMONIC").sum()); nwr += int(np.isin(vd, ["HARMONIC", "UNDETERMINED", "NOT HARMONIC"]).sum())
        print("   k = %-5d HARMONIC %d of %d with a reading (%.1f%%)" % (k, nH, nwr, 100.0 * nH / nwr if nwr else float("nan")))

    # S3
    rr, xx, cc = [], [], []
    for hr in range(2):
        valid, D1, D2, sD, cls, ratio, pf, cls_pf = vc(("Yf", "S,S", hr), hr, False, None)
        m = valid & np.isfinite(ratio) & (np.abs(D2) > 0) & (sD > 0)
        rr.append(ratio[m]); xx.append(np.abs(D2[m]) / sD[m]); cc.append(cls[m])
    rr, xx, cc = np.concatenate(rr), np.concatenate(xx), np.concatenate(cc)
    print("S3 frozen (S, S), valid centres by |D(r2)| / sigma_D: count; D(r1)/D(r2) at the 10th, 50th, 90th percentiles; classes")
    for lo, hi in ((0, 1e-3), (1e-3, 1e-2), (1e-2, 1e-1), (1e-1, 1), (1, 10), (10, 100), (100, np.inf)):
        m = (xx >= lo) & (xx < hi)
        if m.any():
            q = np.quantile(rr[m], [0.1, 0.5, 0.9])
            print("   [%g, %g): %6d; %.2f %.2f %.2f; %s" % (lo, hi, int(m.sum()), q[0], q[1], q[2],
                  {CLS[c]: int((cc[m] == c).sum()) for c in range(5) if (cc[m] == c).any()}))

    # S4
    twelve = [x[0] for x in cells["H4"]["listed_other_than_not_harmonic"] if x[1] == "HARMONIC"]
    print("S4 the twelve lines where theta_M is HARMONIC, over all 6 x 13 stencil points and both sectors:")
    fam = {}
    for ln in twelve:
        c = C[idx["lines"].index(ln)]                                                    # (6, 13, 2, 4)
        d1j = c[..., 0] - c[..., 2]; p1 = np.abs(c[..., 0] - c[..., 1]).max(); p2 = np.abs(c[..., 2] - c[..., 3]).max()
        print("   (%s, %s): c_1 - c_j from %+.2f to %+.2f; max |c_1 - c_i| %.1e, max |c_j - c_k| %.1e" % (ln[0], ln[1], d1j.min(), d1j.max(), p1, p2))
        f = fam.setdefault(ln[0], [np.inf, -np.inf, 0.0])
        f[0] = min(f[0], float(d1j.min())); f[1] = max(f[1], float(d1j.max())); f[2] = max(f[2], float(p1), float(p2))
    for a, (lo, hi, pr) in fam.items():
        print("   family slope %s: c_1 - c_j from %+.2f to %+.2f (sign fixed: %s); pairing precision at most %.1e" % (a, lo, hi, (lo > 0) or (hi < 0), pr))

    # S5
    print("S5 the D-wrap, per quantity: valid centres; those with a point whose per-factor sum exceeds pi; the largest |sum|; class changes; verdict changes")
    spec = [(("Y", n, hr), hr, n in P.PHASE_FREE, J[(n, hr)]) for n in P.READINGS for hr in range(2)]
    spec += [(("Yf", P.SM, hr), hr, True, J[(P.SM, hr)]) for hr in range(2)]
    spec += [(("Yf", "S,S", hr), hr, False, None) for hr in range(2)]
    spec += [(("H", hr), hr, True, J[(P.SM, hr)]) for hr in range(2)]
    spec += [(("M",), 0, True, None)]
    for key, hr, pfree, jc in spec:
        valid, D1, D2, sD, cls, ratio, pf, cls_pf = vc(key, hr, pfree, jc)
        big = (np.abs(pf) > np.pi).any(-1) & valid
        mx = float(np.abs(pf)[valid].max()) if valid.any() else 0.0
        chg = int((valid & (cls != cls_pf)).sum())
        v0, v1 = verd(valid, cls, key), verd(valid, cls_pf, key)
        nN = int((valid & (cls_pf == 1)).sum()) if key == ("Yf", "S,S", hr) else None
        print("   %-26s valid %6d; past pi %5d (%.1f%%); largest %.2f rad; class changes %3d; verdict changes %d%s"
              % (str(key), int(valid.sum()), int(big.sum()), 100.0 * big.sum() / max(valid.sum(), 1), mx, chg, int((v0 != v1).sum()),
                 ("; N with per-factor sums (C0(d)): %d" % nN) if nN is not None else ""))

    # S6
    exc = cells["H2"]["exceptions"]
    bys = {}
    for ln, hn in exc:
        bys.setdefault(ln[0], {}); bys[ln[0]][hn] = bys[ln[0]].get(hn, 0) + 1
    print("S6 H2's %d exceptions by slope, then Higgs (pairs passing %d of %d; 95%% needs %d):" % (len(exc), cells["H2"]["pairs_passing"], cells["H2"]["pairs_checked"],
          int(np.ceil(0.95 * cells["H2"]["pairs_checked"] - 1e-9))))
    for a in sorted(bys, key=Fr):
        print("   %s: %s" % (a, dict(sorted(bys[a].items()))))

    # S7
    pairings = (((0, 1), (2, 3)), ((0, 2), (1, 3)), ((0, 3), (1, 2)))
    eq = []
    for li in range(nl):
        c = C[li, :, 0]; ok = False
        if np.isfinite(c).all():
            sc = np.abs(c).max()
            ok = any((np.abs(c[..., a] - c[..., b]) <= 1e-9 * sc).all() and (np.abs(c[..., e] - c[..., f]) <= 1e-9 * sc).all()
                     for (a, b), (e, f) in pairings)
        eq.append(ok)
    vM = {tuple(x[0]): x[1] for x in cells["H4"]["listed_other_than_not_harmonic"]}
    und = cells["H1"]["listed"]["UNDETERMINED"]
    sp7 = {}
    for x in und:
        li = idx["lines"].index(x[2])
        k = ("pairs" if eq[li] else "no pairs", vM.get(tuple(x[2]), "NOT HARMONIC"))
        sp7[k] = sp7.get(k, 0) + 1
    print("S7 H1's %d UNDETERMINED by (norms equal in pairs on the line, theta_M's verdict on the line): %s; lines with pairs: %d"
          % (len(und), {"%s / %s" % k: v for k, v in sorted(sp7.items())}, sum(eq)))
    print("p323 posthoc4 exit 0")


if __name__ == "__main__":
    main()
