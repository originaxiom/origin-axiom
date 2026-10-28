"""P-323's post hoc read-outs (POST HOC, labelled; written after reading p323_cells_run.txt, 77a943950).  No cell, no grade.
From the committed census (762784a71) with the sealed script's own functions (p323_strong_angle.py, imported unchanged):
  Q1  why the power control C0(e) failed: the classes of the frozen-(S, S) centres, and why the unclassed ones fell to U;
  Q2  what the 219 UNDETERMINED combinations of H1 look like (their largest |D(r1)| and its ratio);
  Q3  the 8 HARMONIC combinations of H1b: the same (line, Higgs, horocycle) in the other three readings;
  Q4  the 12 lines where theta_M is HARMONIC: which channels are clamped there (c_s None), per sector;
  Q5  H2's 136 exceptions: by line class and Higgs, with the largest horocycle difference;
  Q6  the six's slope: the verdicts of the Standard Model's reading on the 40 lines of slope 2/5 in scope.
    python3 -B p323_posthoc.py > p323_posthoc_out.txt"""
import sys, json, math, importlib.util, pathlib
from fractions import Fraction as Fr
import numpy as np

HERE = pathlib.Path(__file__).resolve().parent
sp = importlib.util.spec_from_file_location("p323", HERE / "p323_strong_angle.py"); P = importlib.util.module_from_spec(sp)
sys.modules["p323"] = P; sp.loader.exec_module(P)


def main():
    d = np.load(P.OUT_CENSUS); idx = json.loads(P.OUT_INDEX.read_text())
    R, C, L, H = d["R"], d["C"], d["L"], d["H"]
    nl = R.shape[0]; lines = [(Fr(a), Fr(b)) for a, b in idx["lines"]]
    Q = P.all_quantities(R, C, L, H)
    QP = [P.all_quantities(*P.perturbed((R, C, L, H), p), keep=False) for p in range(P.NPERT)]
    sig = {k: np.max([np.abs(P.wrap(qp[k][0] - Q[k][0])) for qp in QP], axis=0) for k in Q if k[0] != "clamp"}
    clamp_ok = {hr: (Q[("clamp", hr)] == Q[("clamp", hr)][:, :, :1]).all(axis=(2, 3, 4)) for hr in range(2)}
    hmask = lambda hr: clamp_ok[hr][..., None] * np.ones((1, 1, len(P.HIGGS)), bool)

    def classes(key, phase_free, hr):
        th, fs = Q[key]
        which = "M" if key[0] == "M" else ("H" if key[0] == "H" else "Y")
        cok = clamp_ok[0][..., None] if key[0] == "M" else hmask(hr)
        valid, _ = P.validity(fs, which, phase_free, cok)
        if key[0] == "M": valid = valid[..., 0]
        D1, D2, sD, cls, ratio = P.classify(np.moveaxis(th, 2, -1), np.moveaxis(sig[key], 2, -1))
        return valid, D1, D2, sD, cls, ratio

    # Q1
    print("Q1 the power control: frozen weights, reading (S, S), both horocycles, valid centres (no J cut)")
    tot = {}; why = {"|D(r1)| < 1e-8 but sigma_D > 1e-10": 0, "|D(r1)| >= 1e-8, ratio outside [30, 250]": 0,
                     "ratio in [30, 250] but |D(r2)| < 100 sigma_D": 0}
    sDs, D1s, rs = [], [], []
    for hr in range(2):
        valid, D1, D2, sD, cls, ratio = classes(("Yf", "S,S", hr), False, hr)
        for c, nm in ((1, "N"), (2, "H"), (3, "H'"), (0, "U"), (4, "Un")):
            tot[nm] = tot.get(nm, 0) + int((valid & (cls == c)).sum())
        u = valid & (cls == 0)
        why["|D(r1)| < 1e-8 but sigma_D > 1e-10"] += int((u & (np.abs(D1) < 1e-8) & (sD > 1e-10)).sum())
        why["|D(r1)| >= 1e-8, ratio outside [30, 250]"] += int((u & (np.abs(D1) >= 1e-8) & ~((ratio >= 30) & (ratio <= 250))).sum())
        why["ratio in [30, 250] but |D(r2)| < 100 sigma_D"] += int((u & (ratio >= 30) & (ratio <= 250) & (np.abs(D2) < 100 * sD)).sum())
        sDs.append(sD[valid]); D1s.append(np.abs(D1[valid])); rs.append(ratio[valid & (np.abs(D1) >= 1e-8)])
    sDs, D1s, rs = np.concatenate(sDs), np.concatenate(D1s), np.concatenate(rs)
    print("   classes of the valid centres: %s" % tot)
    print("   why U: %s" % why)
    q = lambda x: ", ".join("%.1e" % v for v in np.quantile(x, [0.1, 0.5, 0.9])) if x.size else "-"
    print("   quantiles 10/50/90%%: sigma_D %s; |D(r1)| %s; ratio where |D(r1)| >= 1e-8: %s" % (q(sDs), q(D1s), q(rs)))
    # Q2
    print("Q2 H1's UNDETERMINED combinations (the two Higgs-phase-free readings): the largest |D(r1)| over their valid centres")
    rows = []
    for name in P.PHASE_FREE:
        for hr in range(2):
            valid, D1, D2, sD, cls, ratio = classes(("Y", name, hr), True, hr)
            vd = P.verdicts(np.moveaxis(valid, 1, -1), np.moveaxis(cls, 1, -1))       # (nl, nH)
            for li in range(nl):
                for hi in range(len(P.HIGGS)):
                    if vd[li, hi] != "UNDETERMINED": continue
                    v = valid[li, :, hi]; a = np.abs(D1[li, :, hi]); j = int(np.argmax(np.where(v, a, -1)))
                    rows.append((name, P.HORS[hr], lines[li], P.HIGGS[hi], a[j], ratio[li, j, hi], sD[li, j, hi]))
    A = np.array([r[4] for r in rows]); Rt = np.array([r[5] for r in rows])
    print("   %d combinations; their largest |D(r1)|: below 1e-8 %d, 1e-8 to 1e-6 %d, above 1e-6 %d (there the ratio lies outside [3, 5])"
          % (len(rows), int((A < 1e-8).sum()), int(((A >= 1e-8) & (A <= 1e-6)).sum()), int((A > 1e-6).sum())))
    cls_count = {}
    for r in rows:
        k = str(r[2][0]); cls_count[k] = cls_count.get(k, 0) + 1
    print("   by slope: %s" % dict(sorted(cls_count.items(), key=lambda x: Fr(x[0]))))
    hc = {}
    for r in rows: hc[r[3]] = hc.get(r[3], 0) + 1
    print("   by Higgs: %s" % hc)
    # Q3
    print("Q3 H1b's HARMONIC combinations, in every reading (the verdicts)")
    harm = json.loads((HERE / "p323_cells.json").read_text())["H1b"]["listed"]["HARMONIC"]
    for name0, hor, ln, hn in harm:
        li = idx["lines"].index(ln); hi = P.HIGGS.index(hn); hr = P.HORS.index(hor); out = []
        for name in P.READINGS:
            valid, D1, D2, sD, cls, ratio = classes(("Y", name, hr), name in P.PHASE_FREE, hr)
            vd = P.verdicts(valid[li, :, hi][None], cls[li, :, hi][None])[0]
            out.append("%s %s" % (name, vd))
        print("   (%s, %s) %s %s: %s" % (ln[0], ln[1], hn, hor, "; ".join(out)))
    # Q4
    print("Q4 the lines where theta_M is HARMONIC: channels clamped (c_s None) at the centre, per sector (units 1, i, j, k)")
    hl = [x[0] for x in json.loads((HERE / "p323_cells.json").read_text())["H4"]["listed_other_than_not_harmonic"] if x[1] == "HARMONIC"]
    for ln in hl:
        li = idx["lines"].index(ln); cm = ~np.isfinite(C[li, 0, 0])
        print("   (%s, %s): up %s, down %s" % (ln[0], ln[1], "".join("x" if c else "." for c in cm[0]), "".join("x" if c else "." for c in cm[1])))
    # Q5
    print("Q5 H2's exceptions by line class and Higgs; the largest horocycle difference among them")
    exc = json.loads((HERE / "p323_cells.json").read_text())["H2"]["exceptions"]
    by = {}
    for ln, hn in exc:
        k = "slope %s" % ln[0]; by.setdefault(k, set()).add(hn)
    for k, v in sorted(by.items(), key=lambda x: Fr(x[0].split()[1])):
        print("   %s: %d pairs; Higgs %s" % (k, sum(1 for ln, hn in exc if "slope %s" % ln[0] == k), sorted(v)))
    th0, th1 = Q[("Y", P.SM, 0)][0][:, :, 0], Q[("Y", P.SM, 1)][0][:, :, 0]
    dif = np.abs(P.wrap(th0 - th1))
    mx = max(float(dif[idx["lines"].index(ln), :, P.HIGGS.index(hn)].max()) for ln, hn in exc) if exc else float("nan")
    print("   the largest |theta_Y(L_max) - theta_Y(L_2)| over the exceptions' centres: %.1e" % mx)
    # Q6
    print("Q6 the Standard Model's reading on the lines of slope 2/5 in scope: verdicts over 10 Higgs x 2 horocycles")
    l25 = [i for i, (a, b) in enumerate(lines) if a == Fr(2, 5)]
    for hr in range(2):
        valid, D1, D2, sD, cls, ratio = classes(("Y", P.SM, hr), True, hr)
        vd = P.verdicts(np.moveaxis(valid, 1, -1), np.moveaxis(cls, 1, -1))
        cnt = {}
        for li in l25:
            for hi in range(len(P.HIGGS)):
                cnt[vd[li, hi]] = cnt.get(vd[li, hi], 0) + 1
        print("   %s (before the J cut): %d lines; %s" % (P.HORS[hr], len(l25), cnt))
    print("p323 posthoc exit 0")


if __name__ == "__main__":
    main()
