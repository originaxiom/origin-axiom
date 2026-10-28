"""P-323's post hoc read-outs, second part (POST HOC, labelled; written after reading p323_posthoc_out.txt, 0843b961c).  No cell.
p323_posthoc.py's Q2 and Q6 classified the centres without the cells' J cut (it did not recompute J), so its Q2 counted 239
combinations against the cells' 219 UNDETERMINED.  Here J is computed at the centres as the cells compute it (the LU
coupling and tic.ckm_left, the cells' code copied), and:
  Q2'  H1's UNDETERMINED combinations with the J cut: the count is checked against the cells' 219, then their largest
       |D(r1)|, by slope and by Higgs;
  Q6'  the Standard Model's reading on the 40 lines of slope 2/5, with the J cut, both horocycles;
  Q7   the Higgs directions' shape at the centres: the largest component's share |h_max|^2 (a direction near one channel
       makes (u.h) nearly one term, so its phase nearly holomorphic);
  Q8   on the 12 lines where theta_M is HARMONIC: the spread of the four norms c_s at the centres (are they equal in pairs?).
    python3 -B p323_posthoc2.py > p323_posthoc2_out.txt"""
import sys, json, math, importlib.util, pathlib
from fractions import Fraction as Fr
import numpy as np

HERE = pathlib.Path(__file__).resolve().parent
sp = importlib.util.spec_from_file_location("p323", HERE / "p323_strong_angle.py"); P = importlib.util.module_from_spec(sp)
sys.modules["p323"] = P; sp.loader.exec_module(P)


def main():
    g = P.frame(); B, tic = g["B"], g["tic"]
    d = np.load(P.OUT_CENSUS); idx = json.loads(P.OUT_INDEX.read_text())
    R, C, L, H = d["R"], d["C"], d["L"], d["H"]
    nl = R.shape[0]; lines = [(Fr(a), Fr(b)) for a, b in idx["lines"]]
    Q = P.all_quantities(R, C, L, H)
    QP = [P.all_quantities(*P.perturbed((R, C, L, H), p), keep=False) for p in range(P.NPERT)]
    sig = {k: np.max([np.abs(P.wrap(qp[k][0] - Q[k][0])) for qp in QP], axis=0) for k in Q if k[0] != "clamp"}
    clamp_ok = {hr: (Q[("clamp", hr)] == Q[("clamp", hr)][:, :, :1]).all(axis=(2, 3, 4)) for hr in range(2)}
    # J at the centres: the cells' code
    J = {}
    for hr in range(2):
        u0, _ = P.weights(R[:, :, 0], C[:, :, 0], L[:, :, 0, hr])
        M0 = np.einsum("...s,sab->...ab", u0, np.array([B.EDUAL[s] for s in P.UNITS]))
        for name, (cu, cd) in P.READINGS.items():
            if name not in P.PHASE_FREE: continue
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
            JJ = np.zeros((nl, 6, len(P.HIGGS)))
            for li in range(nl):
                for ci in range(6):
                    for hi in range(len(P.HIGGS)):
                        JJ[li, ci, hi] = tic.ckm_left(Ys[0][li, ci, hi], Ys[1][li, ci, hi])[3]
            J[(name, hr)] = JJ

    def vc(name, hr):
        th, fs = Q[("Y", name, hr)]
        valid, _ = P.validity(fs, "Y", True, clamp_ok[hr][..., None] * np.ones((1, 1, len(P.HIGGS)), bool))
        valid = valid & (np.abs(J[(name, hr)]) > 1e-9)
        D1, D2, sD, cls, ratio = P.classify(np.moveaxis(th, 2, -1), np.moveaxis(sig[("Y", name, hr)], 2, -1))
        return valid, D1, D2, sD, cls, ratio
    # Q2'
    rows = []; cnt = {}
    for name in P.PHASE_FREE:
        for hr in range(2):
            valid, D1, D2, sD, cls, ratio = vc(name, hr)
            vd = P.verdicts(np.moveaxis(valid, 1, -1), np.moveaxis(cls, 1, -1))
            for v in np.unique(vd): cnt[v] = cnt.get(v, 0) + int((vd == v).sum())
            for li in range(nl):
                for hi in range(len(P.HIGGS)):
                    if vd[li, hi] != "UNDETERMINED": continue
                    v = valid[li, :, hi]; a = np.abs(D1[li, :, hi]); j = int(np.argmax(np.where(v, a, -1)))
                    rows.append((name, hr, lines[li], P.HIGGS[hi], a[j], ratio[li, j, hi]))
    print("Q2' the H1 verdicts recomputed with the J cut: %s (the cells: NOT HARMONIC 10859, HARMONIC 0, UNDETERMINED 219, NOISE-LIMITED 318, NO READING 444)" % cnt)
    A = np.array([r[4] for r in rows])
    print("   the %d UNDETERMINED: largest |D(r1)| below 1e-8 %d, 1e-8 to 1e-6 %d, above 1e-6 %d (there the ratio lies outside [3, 5])"
          % (len(rows), int((A < 1e-8).sum()), int(((A >= 1e-8) & (A <= 1e-6)).sum()), int((A > 1e-6).sum())))
    bs, bh = {}, {}
    for r in rows:
        bs[str(r[2][0])] = bs.get(str(r[2][0]), 0) + 1; bh[r[3]] = bh.get(r[3], 0) + 1
    print("   by slope: %s" % dict(sorted(bs.items(), key=lambda x: Fr(x[0]))))
    print("   by Higgs: %s" % bh)
    # Q6'
    l25 = [i for i, (a, b) in enumerate(lines) if a == Fr(2, 5)]
    for hr in range(2):
        valid, D1, D2, sD, cls, ratio = vc(P.SM, hr)
        vd = P.verdicts(np.moveaxis(valid, 1, -1), np.moveaxis(cls, 1, -1))
        c = {}
        for li in l25:
            for hi in range(len(P.HIGGS)): c[vd[li, hi]] = c.get(vd[li, hi], 0) + 1
        print("Q6' the Standard Model's reading on the 40 slope-2/5 lines, %s, with the J cut: %s" % (P.HORS[hr], c))
    # Q7
    share = (np.abs(H[:, :, 0]) ** 2).max(-1)                                          # (nl, 6, 10)
    print("Q7 the largest component's share |h_max|^2 at the centres, per Higgs: median (min-max)")
    for hi, hn in enumerate(P.HIGGS):
        x = share[:, :, hi]
        print("   %-5s %.6f (%.6f-%.6f)" % (hn, float(np.median(x)), float(x.min()), float(x.max())))
    # Q8
    print("Q8 the norms c_s at the centres on the 12 lines where theta_M is HARMONIC: |c_1 - c_i| and |c_j - c_k| (largest over centres, both sectors), and |c_1 - c_j|")
    hl = [x[0] for x in json.loads((HERE / "p323_cells.json").read_text())["H4"]["listed_other_than_not_harmonic"] if x[1] == "HARMONIC"]
    for ln in hl:
        li = idx["lines"].index(ln); c = C[li, :, 0]                                       # (6, 2, 4)
        print("   (%s, %s): |c_1 - c_i| %.1e, |c_j - c_k| %.1e, |c_1 - c_j| %.1e" % (ln[0], ln[1], float(np.abs(c[..., 0] - c[..., 1]).max()),
              float(np.abs(c[..., 2] - c[..., 3]).max()), float(np.abs(c[..., 0] - c[..., 2]).max())))
    li = lines.index((Fr(2, 5), Fr(1, 2))); c = C[li, :, 0]
    print("   for comparison (2/5, 1/2): |c_1 - c_i| %.1e, |c_j - c_k| %.1e, |c_1 - c_j| %.1e" % (float(np.abs(c[..., 0] - c[..., 1]).max()),
          float(np.abs(c[..., 2] - c[..., 3]).max()), float(np.abs(c[..., 0] - c[..., 2]).max())))
    print("p323 posthoc2 exit 0")


if __name__ == "__main__":
    main()
