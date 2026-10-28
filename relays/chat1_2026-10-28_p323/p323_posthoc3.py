"""P-323's post hoc read-outs, third part (POST HOC, labelled; written after this seat's read-only referee of the result note,
which found the note's account of the UNDETERMINED combinations wrong as written and Q2''s fixed-text parenthesis
uncomputed).  No cell.  From the committed census (762784a71) and the sealed script's functions:
  R1  per line, whether the four norms c_s are equal in pairs in some pairing ((1,i)(j,k), (1,j)(i,k) or (1,k)(i,j)),
      to 1e-9 relative, at every centre and in both sectors; and how theta_M's verdict (H4) splits over such lines;
  R2  H1's 219 UNDETERMINED combinations: how many lie on the twelve lines where theta_M is HARMONIC, how many on lines
      with norms equal in pairs (R1), and how many involve F_-10 or F_-6;
  R3  the UNDETERMINED combinations whose largest |D(r1)| exceeds 1e-6: the ratio D(r1)/D(r2) and sigma_D at that centre.
    python3 -B p323_posthoc3.py > p323_posthoc3_out.txt"""
import sys, json, importlib.util, pathlib
from fractions import Fraction as Fr
import numpy as np

HERE = pathlib.Path(__file__).resolve().parent
sp = importlib.util.spec_from_file_location("p323", HERE / "p323_strong_angle.py"); P = importlib.util.module_from_spec(sp)
sys.modules["p323"] = P; sp.loader.exec_module(P)


def main():
    d = np.load(P.OUT_CENSUS); idx = json.loads(P.OUT_INDEX.read_text())
    C = d["C"]; nl = C.shape[0]
    cells = json.loads((HERE / "p323_cells.json").read_text())
    # R1
    pairings = {"(1,i)(j,k)": ((0, 1), (2, 3)), "(1,j)(i,k)": ((0, 2), (1, 3)), "(1,k)(i,j)": ((0, 3), (1, 2))}
    eq = {}
    for li in range(nl):
        c = C[li, :, 0]                                                                # (6 centres, 2 sectors, 4)
        found = None
        for nm, ((a, b), (e, f)) in pairings.items():
            sc = np.nanmax(np.abs(c)) if np.isfinite(c).any() else 1.0
            ok = np.isfinite(c).all() and (np.abs(c[..., a] - c[..., b]) <= 1e-9 * sc).all() and (np.abs(c[..., e] - c[..., f]) <= 1e-9 * sc).all()
            if ok: found = nm; break
        eq[li] = found
    pl = [li for li in range(nl) if eq[li]]
    print("R1 lines whose norms are equal in pairs (to 1e-9 relative, every centre, both sectors): %d of %d" % (len(pl), nl))
    byp = {}
    for li in pl: byp[eq[li]] = byp.get(eq[li], 0) + 1
    print("   by pairing: %s" % byp)
    bys = {}
    for li in pl: bys[idx["lines"][li][0]] = bys.get(idx["lines"][li][0], 0) + 1
    print("   by slope: %s" % dict(sorted(bys.items(), key=lambda x: Fr(x[0]))))
    vM = {tuple(x[0]): x[1] for x in cells["H4"]["listed_other_than_not_harmonic"]}
    split = {}
    for li in range(nl):
        v = vM.get(tuple(idx["lines"][li]), "NOT HARMONIC")
        k = ("pairs" if eq[li] else "no pairs", v); split[k] = split.get(k, 0) + 1
    print("   theta_M's verdict against the pairing: %s" % {"%s / %s" % k: v for k, v in sorted(split.items())})
    # R2
    und = cells["H1"]["listed"]["UNDETERMINED"]                                         # [reading, horocycle, [a, b], higgs]
    twelve = {tuple(x[0]) for x in cells["H4"]["listed_other_than_not_harmonic"] if x[1] == "HARMONIC"}
    on12 = sum(1 for x in und if tuple(x[2]) in twelve)
    on12h = sum(1 for x in und if tuple(x[2]) in twelve and x[3] in ("F_-10", "F_-6"))
    onp = sum(1 for x in und if eq[idx["lines"].index(x[2])])
    onph = sum(1 for x in und if eq[idx["lines"].index(x[2])] and x[3] in ("F_-10", "F_-6"))
    hh = sum(1 for x in und if x[3] in ("F_-10", "F_-6"))
    print("R2 H1's %d UNDETERMINED: on the twelve lines where theta_M is HARMONIC %d (%d of them with F_-10 or F_-6); on lines with norms "
          "equal in pairs %d (%d with F_-10 or F_-6); with F_-10 or F_-6 anywhere %d" % (len(und), on12, on12h, onp, onph, hh))
    # R3: the classes as the cells compute them, with J at the centres (the cells' LU coupling and tic.ckm_left, as posthoc2)
    print("R3 the UNDETERMINED combinations whose largest |D(r1)| over their valid centres exceeds 1e-6 (with the cells' J cut):")
    g = P.frame(); B, tic = g["B"], g["tic"]
    R, Cc, L, H = d["R"], d["C"], d["L"], d["H"]
    Q = P.all_quantities(R, Cc, L, H)
    QP = [P.all_quantities(*P.perturbed((R, Cc, L, H), p), keep=False) for p in range(P.NPERT)]
    sig = {k: np.max([np.abs(P.wrap(qp[k][0] - Q[k][0])) for qp in QP], axis=0) for k in Q if k[0] != "clamp"}
    clamp_ok = {hr: (Q[("clamp", hr)] == Q[("clamp", hr)][:, :, :1]).all(axis=(2, 3, 4)) for hr in range(2)}
    J = {}
    for hr in range(2):
        u0, _ = P.weights(R[:, :, 0], Cc[:, :, 0], L[:, :, 0, hr])
        M0 = np.einsum("...s,sab->...ab", u0, np.array([B.EDUAL[s] for s in P.UNITS]))
        for name in P.PHASE_FREE:
            cu, cd = P.READINGS[name]; Ys = []
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
    n = 0
    for x in und:
        name, hor, ln, hn = x; hr = P.HORS.index(hor); li = idx["lines"].index(ln); hi = P.HIGGS.index(hn)
        th, fs = Q[("Y", name, hr)]
        valid, _ = P.validity(fs, "Y", True, clamp_ok[hr][..., None] * np.ones((1, 1, len(P.HIGGS)), bool))
        valid = valid & (np.abs(J[(name, hr)]) > 1e-9)
        D1, D2, sD, cls, ratio = P.classify(np.moveaxis(th, 2, -1), np.moveaxis(sig[("Y", name, hr)], 2, -1))
        v = valid[li, :, hi]; a = np.abs(D1[li, :, hi])
        j = int(np.argmax(np.where(v, a, -1)))
        if v[j] and a[j] > 1e-6:
            n += 1
            print("   %s %s (%s, %s) %s: |D(r1)| %.2e, ratio %.2f, sigma_D %.1e, class %d" % (name, hor, ln[0], ln[1], hn, a[j], ratio[li, j, hi], sD[li, j, hi], cls[li, j, hi]))
    print("   %d such combinations (the classes: 0 U, 1 N, 2 H, 3 H', 4 Un)" % n)
    print("p323 posthoc3 exit 0")


if __name__ == "__main__":
    main()
