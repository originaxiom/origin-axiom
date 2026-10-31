#!/usr/bin/env python3
"""STEP B, the pass side on B1741's box (S284; data-free; aggregate-only; refused unless the refined census's manifest is
committed and pushed).  The calibration's dress rehearsal (calibration_driver, S283) planted its worlds from the frame's
whole prior: all twenty planted worlds of its pass side, and the ten each of the leg's size and anarchy, had six outside
B1741's box, where K is undefined (L_raw = +inf: UNJUDGED, and legs_for then returns the CKM leg as failing), so those
three sections were void (none of their worlds was judged).  The target lies in the box by the box's construction, so the
pass side that bears on it is the frame's worlds whose six lie in the box.  This computes:
0. THE FRAME'S MASS IN THE BOX: of the worlds calibration_driver.planted() draws (a physical row by its cell's measure, tau
   by dx dy / y^2, c = 3), the fraction whose six lie in the box (Clopper-Pearson), from every batch drawn below.
1. THE PASS SIDE ON THE BOX: (a) chi2 = 0 and (b) Gaussian noise at sigma (a world kept when its noisy six lie in the box):
   S (c = 3), K judged, K (C_ten > gate_bits), the CKM leg, all three; the quantiles of C_ten, C_six and bits_CKM.
2. THE LEG'S SIZE ON THE BOX: the six as in 1(a), the four from the frame's physical marginal (p2's null four).
3. ANARCHY ON THE BOX: the six as in 1(a), the four from a Haar-random unitary (as calibration_driver's section 6).
Worlds are drawn in batches until P lie in the box for each section, or N_max are drawn.  Serial (no fork, S283); a
checkpoint after every K.  Prints and writes counts, rates, intervals and quantiles; never a world or a row's value.
    python3 -I calibration_inbox.py <refined dir> <manifest.json> <manifest sha256> <sigma file> <out.json> [P] [seed] [N_max]"""
import json, math, pathlib, sys, time

GEN = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(GEN))
import numpy as np

import compression as K
import stepb_core as C
import p2_driver as P2
import calibration_driver as CAL

BATCH = 20000


def in_box_mask(T):
    return np.array([K.in_box(t[:6]) for t in T], bool)


def planted_in_box(ci, sig, rng, n, noise, nmax, tally):
    """n planted worlds (fewer if nmax are drawn first) whose six lie in the box; tally counts every drawn world"""
    keep_t, keep_r, got = [], [], 0
    while got < n and tally["drawn"] < nmax:
        T, rows = CAL.planted(ci, sig, rng, BATCH, noise)
        m = in_box_mask(T)
        tally["drawn"] += BATCH; tally["in_box"] += int(m.sum())            # non-finite worlds count as drawn, outside
        keep_t.append(T[m]); keep_r.append(rows[m]); got += int(m.sum())
    if not keep_t:
        return np.zeros((0, 10)), np.zeros(0, np.int64)
    return np.concatenate(keep_t)[:n], np.concatenate(keep_r)[:n]


def quant(v):
    v = [x for x in v if x is not None]
    return [float(x) for x in np.quantile(v, [.1, .5, .9])] if v else None


def summary(S, rr):
    judged = [r for r in rr if r["K_judged"]]
    allp = [bool(s) and r["K"] and r["CKM"] for s, r in zip(S, rr)]
    return {"n": len(rr), "S": int(np.sum(S)), "K_judged": len(judged), "not_converged": sum(r["converged"] is False for r in judged),
            "K": sum(r["K"] for r in rr), "K_cp95": P2.cp(sum(r["K"] for r in rr), len(rr)) if rr else None,
            "CKM": sum(r["CKM"] for r in rr), "CKM_cp95": P2.cp(sum(r["CKM"] for r in rr), len(rr)) if rr else None,
            "all_three": int(sum(allp)), "C_ten_q10_50_90": quant([r["C_ten"] for r in judged]),
            "C_six_q10_50_90": quant([r["C_six"] for r in judged]), "bits_CKM_q10_50_90": quant([r["bits"] for r in judged])}


def main(refined, manifest, expected, sigma_file, out, P="10", seed="20261102", N_max="4000000"):
    Pn, seed, nmax = int(P), int(seed), int(N_max)
    P2.CI, sig, meta = P2.build(refined, manifest, expected, sigma_file, spaces=("nine", "six", "ckm3"), gauss=(4, 16, 32, 64))
    ci = P2.CI
    rng = np.random.default_rng(seed); tally = {"drawn": 0, "in_box": 0}; t0 = time.time()
    rep = dict(meta, gate_bits_m53=CAL.GATE, P=Pn, seed=seed, N_max=nmax, box="B1741: per sector ln r2 in [-3, -1] ln 10, ln r1 in [-6, -2.5] ln 10, r1 < r2")
    ck = pathlib.Path(out).with_suffix(".checkpoint.json")

    def save():
        rep["frame_mass_in_box"] = {"drawn": tally["drawn"], "in_box": tally["in_box"],
                                    "fraction": tally["in_box"] / tally["drawn"] if tally["drawn"] else None,
                                    "cp95": P2.cp(tally["in_box"], tally["drawn"]) if tally["drawn"] else None}
        rep["seconds"] = round(time.time() - t0, 1)
        ck.write_text(json.dumps(rep, indent=1, default=float) + "\n")

    def legs(label, T, S):
        rr = []
        for t in T:
            rr.append(CAL.legs_for((t, C.C_OURS)))
            rep[label] = dict(summary(S[:len(rr)], rr), complete=len(rr) == len(T)); save()
        rep[label] = dict(summary(S, rr), complete=True) if len(T) else {"n": 0, "complete": True}; save()
        print(label, {k: v for k, v in rep[label].items()}, "%.0f s" % (time.time() - t0), flush=True)
        return rr

    sup = lambda T: ci.support_batch(T, C.C_OURS)["in_support"] if len(T) else np.zeros(0, bool)
    # 1. the pass side on the box: chi2 = 0, then noise at sigma
    T1, _ = planted_in_box(ci, sig, rng, Pn, False, nmax, tally)
    legs("pass_side_in_box_chi2_0", T1, sup(T1))
    Tn, _ = planted_in_box(ci, sig, rng, Pn, True, nmax, tally)
    legs("pass_side_in_box_noise_sigma", Tn, sup(Tn))
    # 2. the leg's size on the box: the four from the frame's physical marginal
    T2, _ = planted_in_box(ci, sig, rng, Pn, False, nmax, tally)
    if len(T2):
        W, _ = P2.null_worlds(ci, sig, rng, len(T2)); T2[:len(W), 6:10] = W[:, 6:10]; T2 = T2[:len(W)]
    legs("leg_size_in_box", T2, sup(T2))
    # 3. anarchy on the box: the four from a Haar-random unitary
    T3, _ = planted_in_box(ci, sig, rng, Pn, False, nmax, tally)
    four = []
    for z in (rng.normal(size=(len(T3), 3, 3)) + 1j * rng.normal(size=(len(T3), 3, 3))) / math.sqrt(2):
        q, r = np.linalg.qr(z); U = q * (np.diag(r) / np.abs(np.diag(r)))[None, :]
        J = float(np.imag(U[0, 1] * U[1, 2] * np.conj(U[0, 2]) * np.conj(U[1, 1])))
        four.append(np.log([abs(U[0, 1]), abs(U[1, 2]), abs(U[0, 2]), abs(J) + 1e-300]))
    if len(T3):
        T3[:, 6:10] = np.array(four)
    legs("anarchy_in_box", T3, sup(T3))
    rep["complete"] = True; save()
    pathlib.Path(out).write_text(json.dumps(rep, indent=1, default=float) + "\n", encoding="utf-8")
    print(json.dumps(rep, indent=1, default=float))


if __name__ == "__main__":
    if len(sys.argv) < 6: sys.exit(__doc__)
    main(*sys.argv[1:])
