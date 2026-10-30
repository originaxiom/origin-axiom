#!/usr/bin/env python3
"""STEP B, X2's p2 (data-free; aggregate-only; runs only after the refined census's manifest is committed and pushed: the
guard refuses otherwise).

p2 = the fraction of null worlds that the support search puts in the support: continuous tau (cells.CellIndex: the census
interpolated cell by cell, J signed; Bernstein enclosures and branch-and-bound), every line, direction, radius, reading and
the nine values of c (the null re-makes the data's choice of c), chi2_ten < 23.209 with sigma from the sigma-only file.
The null worlds (BL1, the card's section 2): the six from B1741's box (stepb_core.null_six); the four from the frame's own
unconditional CKM marginal over its PHYSICAL choices -- a row by its cell's measure, tau in the cell by dx dy / y^2, the
interpolated four, plus the kernel's Gaussian noise at sigma -- drawn independently of the six.  A world with a non-finite
entry (an exactly zero modulus at a node-only cell) is not of our kind: dropped and counted (the fifth review's N4).
The graded upper end counts the UNDECIDED worlds as possible hits (the fifth review's N2): p2_up = CP upper of
(hits + undecided) / N.  Read-out: p2 at chi2_nine < 21.67.
Worlds are drawn in the parent (one seed, reproducible whatever the scheduling) and searched by forked workers sharing the
index (tested identical to serial); a checkpoint is written after every batch.  The INDICES of the supported worlds in the
drawn sequence (never their values) are recorded, so the calibration regenerates them from the seed without searching
again.  The nine-quantity read-out runs on the first N9 worlds.
Prints and writes counts, rates, Clopper-Pearson intervals, timings; never a world or a row's value.
    python3 -I p2_driver.py <refined dir> <manifest.json> <manifest sha256> <sigma file> <out.json> [N] [seed] [batch] [workers]"""
import json, math, multiprocessing as mp, pathlib, sys, time

GEN = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(GEN))
import numpy as np

import stepb_core as C
from assemble import Choices
from cells import CellIndex
from census_io import load_compact
from guard import require_pushed_manifest

N_CFG = 991
N_CHOICES_MAX = 266 * 12 * 2 * 8              # A's Kraft count: the address code covers at most these choices
CI = None                                     # the shared index (set before forking)


def cp(k, n):
    from scipy.stats import beta
    lo = 0.0 if k == 0 else float(beta.ppf(0.025, k, n - k + 1))
    hi = 1.0 if k >= n else float(beta.ppf(0.975, k + 1, n - k))
    return lo, hi


def build(refined, manifest, expected, sigma_file):
    g = require_pushed_manifest(manifest, expected)
    sig = np.array(json.loads(pathlib.Path(sigma_file).read_text())["sigma_natural_log"], float)
    assert sig.shape == (10,) and (sig >= 0.0999).all()
    t0 = time.time()
    cen, info = load_compact(refined, g["per_file"], n_cfg_expected=g["files"] * N_CFG)
    pts = sorted({(round(float(a), 4), round(float(b), 4)) for a, b in cen.tau})
    ch = Choices(cen, cen.F, pts)
    if ch.R.shape[0] > N_CHOICES_MAX:
        raise SystemExit("refused: %d choices exceed the address code's %d (Kraft)" % (ch.R.shape[0], N_CHOICES_MAX))
    ci = CellIndex(cen.F, cen.J, pts, ch, sig)
    for s in ("nine", "six", "ckm3"):
        ci.trees(s)
    for n in (4, 16, 32, 64):
        ci.gauss_table(n)
    ci.measure_totals()
    return ci, sig, {"manifest_commit": g["manifest_commit"], "load_s": round(time.time() - t0, 1), "rows": int(len(cen.F)),
                     "rows_defined": int(len(ci.rows)), "rows_interpolated": int(ci.ok.sum()), "choices": int(ch.R.shape[0]),
                     "choices_physical": int(ci.physical_choice.sum()), "error_configs": len(info["errors"]),
                     "a0_F-2_max_log10": info["worst_a0_Fm2_log10"]}


def null_worlds(ci, sig, rng, n):
    """(worlds (m, 10), dropped): n draws, the non-finite ones dropped"""
    six = C.null_six(rng, n)
    rows, xs, ys = ci.sample_prior(rng, n)
    four = ci.interp_many(rows, xs, ys)[:, 6:10] + rng.normal(0.0, 1.0, (n, 4)) * sig[6:10]
    W = np.concatenate([six, four], axis=1)
    fin = np.isfinite(W).all(axis=1)
    return W[fin], int((~fin).sum())


def _work(args):
    W, which = args
    if which == "ten":
        r = CI.support_batch(W, C.C_SCAN)
    else:
        r = CI.support_batch(W, C.C_SCAN, T=C.THRESHOLD_NINE, comps=tuple(range(9)))
    return int(r["in_support"].sum()), int(r["undecided"]), np.nonzero(r["in_support"])[0].tolist()


def worlds_by_index(ci, sig, seed, batch, N, indices):
    """regenerate the drawn sequence (the same seed and batches as main) and return the worlds at the given indices (the
    sequence after the non-finite drop), without searching"""
    want = sorted(set(int(i) for i in indices)); out = {}; rng = np.random.default_rng(seed); done = pos = 0
    while done < N and len(out) < len(want):
        b = min(batch, N - done)
        W, _ = null_worlds(ci, sig, rng, b)
        for i in want:
            if pos <= i < pos + len(W):
                out[i] = W[i - pos]
        pos += len(W); done += b
    return np.array([out[i] for i in want if i in out])


def main(refined, manifest, expected, sigma_file, out, N="1000000", seed="20261031", batch="20000", workers="8", N9="100000"):
    global CI
    N, seed, batch, workers, N9 = int(N), int(seed), int(batch), int(workers), int(N9)
    CI, sig, meta = build(refined, manifest, expected, sigma_file)
    rng = np.random.default_rng(seed)
    hits10 = hits9 = und10 = und9 = done = dropped = pos = done9 = 0; t0 = time.time(); supported = []
    ctx = mp.get_context("fork")
    with ctx.Pool(workers) as P:
        while done < N:
            b = min(batch, N - done)
            W, dr = null_worlds(CI, sig, rng, b); dropped += dr
            step = max(1, len(W) // workers + 1)
            starts = list(range(0, len(W), step))
            for st, (h, u, idx) in zip(starts, P.map(_work, [(W[a:a + step], "ten") for a in starts])):
                hits10 += h; und10 += u; supported.extend(pos + st + i for i in idx)
            if done9 < N9:
                for h, u, _ in P.map(_work, [(W[a:a + step], "nine") for a in starts]):
                    hits9 += h; und9 += u
                done9 += len(W)
            done += b; pos += len(W)
            ck = dict(meta, N_done=done, dropped_nonfinite=dropped, in_support_ten=hits10, undecided_ten=und10,
                      in_support_nine=hits9, undecided_nine=und9, N9_done=done9, seconds=round(time.time() - t0, 1), complete=False,
                      seed=seed, batch=batch, supported_indices=supported[:5000])
            pathlib.Path(out).with_suffix(".checkpoint.json").write_text(json.dumps(ck, indent=1) + "\n")
            print("worlds %d (dropped %d)  in support (ten) %d  (nine) %d  undecided %d/%d  %.0f s" % (
                done, dropped, hits10, hits9, und10, und9, time.time() - t0), flush=True)
    n = N - dropped
    rep = dict(meta, N_drawn=N, N=n, dropped_nonfinite=dropped, seed=seed, batch=batch, in_support_ten=hits10, undecided_ten=und10,
               p2=hits10 / n, p2_cp95=(cp(hits10, n)[0], cp(hits10 + und10, n)[1]),
               readout_N9=done9, readout_in_support_nine=hits9, readout_undecided_nine=und9, readout_p2_nine=hits9 / max(1, done9),
               readout_p2_nine_cp95=(cp(hits9, max(1, done9))[0], cp(hits9 + und9, max(1, done9))[1]), seconds=round(time.time() - t0, 1), complete=True,
               supported_indices=supported[:5000],
               definition="p2 = P_null(S): continuous tau, the nine c, chi2_ten < 23.209; null = B1741's box x the frame's "
                          "physical CKM marginal (BL1); the upper end counts undecided worlds as hits")
    pathlib.Path(out).write_text(json.dumps(rep, indent=1) + "\n", encoding="utf-8")
    print(json.dumps(rep, indent=1))


if __name__ == "__main__":
    if len(sys.argv) < 6: sys.exit(__doc__)
    main(*sys.argv[1:])
