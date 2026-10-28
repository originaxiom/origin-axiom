"""Referee B1798: a c-choosing class-choosing null.  The lepton factor c entered every test from TWO_INGREDIENTS on after
the web seat's post hoc read of main's rows (gj_posthoc: c scanned from 1/3 to 5, best at 3; its ledger row: "informed
c = 3 in TWO_INGREDIENTS and in every later test that uses it").  Here each random target (and the data) may choose c
continuously in [1/3, 5] (gj_posthoc's range), with the seat's two readings and all 266 lines at B1753's 223 apexes;
B1741's features, sigmas and draws unchanged.  chi2(k) = |Q - t_q|^2 + (a + k - t4)^2/s4^2 + (b - k - t5)^2/s5^2,
k = ln c clipped to [ln 1/3, ln 5] at its unconstrained optimum (exact: the lepton part is convex in k).
Screen: the unconstrained-c ('free') features give a lower bound, KD radius sqrt(obs + 0.5); exact bounded minimum over
every row for the candidates.  Control: k restricted to {0, ln 3} must reproduce the seat menu's hits.
    python3 -B cnull.py ARC SEED_LO SEED_HI [CLO CHI]"""
import os
os.environ.setdefault("OMP_NUM_THREADS", "1"); os.environ.setdefault("OPENBLAS_NUM_THREADS", "1"); os.environ.setdefault("VECLIB_MAXIMUM_THREADS", "1")
import sys, json, math, pathlib
import numpy as np
from scipy.spatial import cKDTree
from scipy.stats import beta
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import direct_null as DN


def main():
    arc, lo, hi = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
    SET = None
    if len(sys.argv) > 4 and sys.argv[4] == "set":
        from fractions import Fraction as Fr
        SET = tuple(math.log(float(Fr(x))) for x in sys.argv[5].split(","))
        clo, chi_ = math.exp(min(SET)), math.exp(max(SET))
    else:
        clo, chi_ = (float(sys.argv[4]), float(sys.argv[5])) if len(sys.argv) > 5 else (1 / 3, 5.0)
    KLO, KHI = math.log(clo), math.log(chi_)
    C, Fseat, rows, lab = DN.build(arc); A = C._A; s6, _ = C.sigmas(); s45 = math.sqrt(s6[4] ** 2 + s6[5] ** 2)
    blocks = []
    for (a, b, l) in C.SEAT:
        Q = np.concatenate([A["U"][:, a] / s6[0:2], A["Dn"][:, b] / s6[2:4]], axis=1)
        blocks.append((Q, A["E"][:, l, 0], A["E"][:, l, 1]))

    def chi2_exact(T, ks=None):
        """T (m x 6) raw log targets -> (m,) min over rows and the two readings; ks None = bounded continuous c"""
        out = np.full(len(T), np.inf)
        tq = T[:, 0:4] / s6[0:4]
        for Q, ea, eb in blocks:
            qq = (Q ** 2).sum(1)[:, None] - 2 * Q @ tq.T + (tq ** 2).sum(1)[None, :]
            u0 = ea[:, None] - T[None, :, 4]; v0 = eb[:, None] - T[None, :, 5]
            if ks is None and SET is not None:
                ks = SET
            if ks is None:
                k = (s6[4] ** 2 * v0 - s6[5] ** 2 * u0) / (s6[4] ** 2 + s6[5] ** 2)
                k = np.clip(k, KLO, KHI)
                lep = (u0 + k) ** 2 / s6[4] ** 2 + (v0 - k) ** 2 / s6[5] ** 2
            else:
                lep = np.minimum.reduce([(u0 + kk) ** 2 / s6[4] ** 2 + (v0 - kk) ** 2 / s6[5] ** 2 for kk in ks])
            out = np.minimum(out, (qq + lep).min(0))
        return out

    T6 = A["T6"][None, :]
    obs_b = float(chi2_exact(T6)[0]); obs_s = float(chi2_exact(T6, ks=(0.0, math.log(3)))[0])
    obs_free = float(C.min_chi2(C.chi2_features("free", False), T6)[0])
    print("data: seat (c in {1,3}) %.9f; bounded c in [%.4f, %.1f] %.9f; free c %.9f" % (obs_s, clo, chi_, obs_b, obs_free), flush=True)
    Xf = np.concatenate([np.concatenate([Q, ((ea + eb) / s45)[:, None]], axis=1) for Q, ea, eb in blocks], axis=0)
    tree = cKDTree(Xf)
    n = hb = hs = cands = 0
    per_seed = {}
    for s in range(lo, hi + 1):
        d6, _ = C.draws(s); T = np.array(d6); n += len(T)
        tf = np.concatenate([T[:, 0:4] / s6[0:4], ((T[:, 4] + T[:, 5]) / s45)[:, None]], axis=1)
        rad = math.sqrt(max(obs_b, obs_s) + 0.5)
        dist, _i = tree.query(tf, k=1, distance_upper_bound=rad)
        cand = np.flatnonzero(np.isfinite(dist)); cands += len(cand)
        if len(cand):
            eb_ = chi2_exact(T[cand]); es_ = chi2_exact(T[cand], ks=(0.0, math.log(3)))
            a1, a2 = int((eb_ <= obs_b + 1e-9).sum()), int((es_ <= obs_s + 1e-9).sum())
        else:
            a1 = a2 = 0
        hb += a1; hs += a2; per_seed[s] = (a1, a2)
    for name, h, o in (("seat control (c in {1,3})", hs, obs_s), (("c-choosing, c in [%.3g, %.3g]" % (clo, chi_)) if SET is None else ("c-choosing, c in set " + sys.argv[5]), hb, obs_b)):
        r = float(beta.ppf(0.975, h + 1, n - h))
        print("%-34s obs %.6f  targets %d  hits %d  frac %.4e  r97.5 %.4e  m*r(39) %.4f  m*r(41) %.4f  break-even m %.1f"
              % (name, o, n, h, h / n, r, 39 * r, 41 * r, 0.01 / r), flush=True)
    print("candidates", cands)
    json.dump({"arc": arc, "seeds": [lo, hi], "c_range": [clo, chi_], "n": n, "obs_bounded": obs_b, "obs_seat": obs_s, "obs_free": obs_free,
               "hits_bounded": hb, "hits_seat": hs, "per_seed": per_seed},
              open(pathlib.Path(__file__).resolve().parent / (("cnull_%s_%d_%d_c%.3g_%.3g.json" % (arc, lo, hi, clo, chi_)) if SET is None else ("cnull_%s_%d_%d_set%d.json" % (arc, lo, hi, len(SET)))), "w"), indent=1)
    print("cnull exit 0")


if __name__ == "__main__":
    main()
