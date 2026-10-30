#!/usr/bin/env python3
"""STEP B, the pre-seal calibration and controls (data-free; aggregate-only; refused unless the refined census's manifest
is committed and pushed).  m0 = 53, the floor of m: the gates here are the loosest the card can apply (gate_bits(53) =
12.37 bits); the card's m at the seal is at least 53.  Runs after p2_driver (it reads p2's output).

1. THE VACUITY CALIBRATION (P-523): null worlds (BL1, as p2_driver draws them) until M of them are in the support (S at the
   nine c); for each, K over the ten and the CKM leg at the scan's best c.  Reported: the fraction with K failing
   (C_ten <= gate_bits) and with the CKM leg failing, with Clopper-Pearson intervals.  VOID only if a failing fraction is
   0 (K or the leg implied by support); a fraction near 1 is the healthy outcome (the fifth review's N5).
2. THE MARKOV CHECK, with power at the gate (N5): unconditioned worlds rarely reach the frame, so the check runs on the
   supported worlds of step 1 weighted by p2's lower end: P0(X >= c) >= p2_lo * P(X >= c | S); it FAILS if, for some c in
   1..16, p2_lo times the Clopper-Pearson lower end of the supported worlds' rate exceeds 2^-c.  X = C_ten, bits_CKM and
   C_six.  M0 unconditioned worlds add the unsupported part (reported).
3. THE PASS SIDE (power, MB12): worlds planted at the frame's own ten at continuous tau (a physical row by its cell's
   measure, tau by dx dy / y^2), the leptons shifted by c = 3, (a) at chi2 = 0 and (b) with Gaussian noise at sigma:
   the fractions in the support (c = 3), with C_ten > gate_bits, with the CKM leg passing, and with all of S, K and the
   CKM leg; per reading.  If no planted world passes, the card says before the seal that the conjunction cannot pass.
4. THE LEG'S SIZE: the six planted from the frame (c = 3), the four drawn from the frame's physical marginal independently:
   the CKM leg's pass rate.
Every K is computed by forked workers sharing the index (tested identical to serial); a checkpoint follows each section.
Prints and writes counts, rates and intervals; never a world or a row's value.
    python3 -I calibration_driver.py <refined dir> <manifest.json> <manifest sha256> <sigma file> <p2.json> <out.json> [M] [M0] [P] [seed] [workers]"""
import json, math, multiprocessing as mp, pathlib, sys, time

GEN = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(GEN))
import numpy as np

import compression as K
import stepb_core as C
import kten
import p2_driver as P2

M_FLOOR = 53
GATE = K.gate_bits(M_FLOOR)


def legs_for(args):
    """K over the ten and the CKM leg (bits and the clause) for one world, by the shared index"""
    t, c_values = args
    ci = P2.CI
    r = kten.K_ten(ci, t, c_values)
    if r["grade"] != "JUDGED":
        return {"K_judged": False, "K": False, "CKM": False, "C_ten": None, "bits": None, "C_six": None, "clause": None, "converged": None}
    clause = None
    if r["bits_CKM"] > GATE:                                    # the clause matters only when the bits clear the gate
        clause = kten.ckm_clause(ci, np.asarray(t, float) - C.c_shift(r["c"]))["clause"]
    return {"K_judged": True, "K": bool(r["C_ten"] > GATE), "CKM": bool(r["bits_CKM"] > GATE and bool(clause)),
            "C_ten": float(r["C_ten"]), "bits": float(r["bits_CKM"]), "C_six": float(r["C_six"]), "clause": clause,
            "converged": bool(r.get("converged"))}


def planted(ci, sig, rng, n, noise):
    rows, xs, ys = ci.sample_prior(rng, n)
    f = ci.interp_many(rows, xs, ys)
    t = f + C.c_shift(3.0)
    if noise:
        t = t + rng.normal(0.0, 1.0, t.shape) * sig
    fin = np.isfinite(t).all(axis=1)
    return t[fin], rows[fin]


def cp_lower(k, n):
    from scipy.stats import beta
    return 0.0 if k == 0 else float(beta.ppf(0.025, k, n - k + 1))


def main(refined, manifest, expected, sigma_file, p2_file, out, M="100", M0="200", P="100", seed="20261101", workers="8"):
    M, M0, Pn, seed, workers = int(M), int(M0), int(P), int(seed), int(workers)
    P2.CI, sig, meta = P2.build(refined, manifest, expected, sigma_file)
    ci = P2.CI
    p2 = json.loads(pathlib.Path(p2_file).read_text()); p2_lo = float(p2["p2_cp95"][0])
    rng = np.random.default_rng(seed); rep = dict(meta, gate_bits_m53=GATE, p2_lo=p2_lo); t0 = time.time()
    ck = pathlib.Path(out).with_suffix(".checkpoint.json")
    save = lambda: ck.write_text(json.dumps(rep, indent=1, default=float) + "\n")
    ctx = mp.get_context("fork")
    with ctx.Pool(workers) as pool:
        # 1. the vacuity calibration
        sup, drawn = [], 0
        while len(sup) < M and drawn < 5_000_000:
            W, _ = P2.null_worlds(ci, sig, rng, 20000); drawn += 20000
            ins = ci.support_batch(W, C.C_SCAN)["in_support"]
            sup.extend(W[ins][: M - len(sup)])
        res = pool.map(legs_for, [(t, C.C_SCAN) for t in sup])
        judged = [r for r in res if r["K_judged"]]
        kf = sum(not r["K"] for r in judged); cf = sum(not r["CKM"] for r in judged)
        rep["vacuity"] = {"null_worlds_drawn": drawn, "supported": len(sup), "K_judged": len(judged),
                          "not_converged": sum(r["converged"] is False for r in judged),
                          "K_failing": kf, "K_failing_cp95": P2.cp(kf, len(judged)) if judged else None,
                          "CKM_failing": cf, "CKM_failing_cp95": P2.cp(cf, len(judged)) if judged else None,
                          "void": bool(judged) and (kf == 0 or cf == 0),
                          "void_rule": "void only if a failing fraction is 0 (K or the leg implied by support)"}
        save(); print("vacuity", rep["vacuity"], "%.0f s" % (time.time() - t0), flush=True)
        # 2. the Markov check on the supported worlds, weighted by p2's lower end
        mk = {}; ok = True
        for name, key in (("C_ten", "C_ten"), ("bits_CKM", "bits"), ("C_six", "C_six")):
            vals = np.array([r[key] for r in judged], float); n = len(vals); rows_ = {}
            for c in range(1, 17):
                k = int((vals >= c).sum()); low = p2_lo * cp_lower(k, n)
                good = low <= 2.0 ** (-c) + 1e-15; ok &= good
                rows_[c] = {"k_supported": k, "lower_P0": low, "bound": 2.0 ** (-c), "ok": good}
            mk[name] = rows_
        W0, _ = P2.null_worlds(ci, sig, rng, M0)
        res0 = pool.map(legs_for, [(t, C.C_SCAN) for t in W0])
        Cs = np.array([r["C_ten"] for r in res0 if r["K_judged"]], float)
        rep["markov"] = {"by_quantity": mk, "all_ok": ok, "unconditioned_worlds": M0, "unconditioned_judged": int(len(Cs)),
                         "unconditioned_C_ten_ge_1": int((Cs >= 1).sum())}
        save(); print("markov", ok, "%.0f s" % (time.time() - t0), flush=True)
        # 3. the pass side, and 4. the leg's size
        for label, noise in (("planted_chi2_0", False), ("planted_noise_sigma", True)):
            T, rows = planted(ci, sig, rng, Pn, noise)
            S = ci.support_batch(T, C.C_OURS)["in_support"]
            rr = pool.map(legs_for, [(t, C.C_OURS) for t in T])
            allp = [bool(s) and r["K"] and r["CKM"] for s, r in zip(S, rr)]
            by = {}
            for k_ in range(8):
                sel = [i for i in range(len(T)) if int(ci.ch.keys[ci.choice[rows[i]]][3]) == k_]
                by[k_] = {"n": len(sel), "S": int(sum(S[i] for i in sel)), "all": int(sum(allp[i] for i in sel))}
            rep[label] = {"n": int(len(T)), "S": int(S.sum()), "K": int(sum(r["K"] for r in rr)), "CKM": int(sum(r["CKM"] for r in rr)),
                          "K_judged": int(sum(r["K_judged"] for r in rr)), "all_three": int(sum(allp)),
                          "C_ten_quantiles": [float(x) for x in np.quantile([r["C_ten"] for r in rr if r["K_judged"]] or [np.nan], [.1, .5, .9])],
                          "by_reading": by}
            save(); print(label, {k: v for k, v in rep[label].items() if k != "by_reading"}, "%.0f s" % (time.time() - t0), flush=True)
        T, rows = planted(ci, sig, rng, Pn, False)
        W, _ = P2.null_worlds(ci, sig, rng, len(T)); T[:len(W), 6:10] = W[:, 6:10]; T = T[:len(W)]
        rr = pool.map(legs_for, [(t, C.C_OURS) for t in T])
        npass = int(sum(r["CKM"] for r in rr))
        rep["leg_size"] = {"n": int(len(T)), "CKM_passing": npass, "cp95": P2.cp(npass, len(T))}
    rep["seconds"] = round(time.time() - t0, 1); rep["complete"] = True
    pathlib.Path(out).write_text(json.dumps(rep, indent=1, default=float) + "\n", encoding="utf-8")
    print(json.dumps({k: v for k, v in rep.items() if k not in ("planted_chi2_0", "planted_noise_sigma", "markov")}, indent=1, default=float))


if __name__ == "__main__":
    if len(sys.argv) < 7: sys.exit(__doc__)
    main(*sys.argv[1:])
