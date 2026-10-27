"""Referee (B1786), the committed producer of the grade-setting read-outs (added 2026-10-28 at the web seat's checking pass,
which found kd_analysis.txt, prior_conditional.txt and prior_given_fit.txt without one).  Reads what null_kd.py and
prior_all.py write in this directory (kd_<tag>.npz: every target whose KD-screened chi2_six is within the margin of the
data's 3.0048, with its seat-menu minimum in each of the 26 slope classes at orders 25 and 30; prior_all_<tag>.npz: every
target's prior-chosen class and prior minimum over B1749's and B1755's lines at the same apexes) and prints:
  the class-choosing nulls (kd_analysis.txt), the prior-chosen null with and without the condition that the chosen class
  has lines at orders 25 and 30 (prior_conditional.txt), and the event rate given a prior fit as good as the data's
  (prior_given_fit.txt).
    python3 -B analyse_kd.py [valid fresh160k fresh10M]"""
import sys, pathlib
import numpy as np
from scipy.stats import beta
D = pathlib.Path(__file__).resolve().parent
BAR, RUNNER = 16.75, 103.095
f = np.load(D / "features.npz"); CL = [str(c) for c in f["classes"]]; I25 = CL.index("2/5")
PCL = [str(c) for c in np.load(D / "prior_features.npz")["classes"]]
sys.path.insert(0, str(D))
import null
OBS = float(null.classmin(f["T6"][None, :])[I25, 0])


def r975(h, n): return beta.ppf(0.975, h + 1, n - h) if h < n else 1.0


def line(label, h, n):
    r = r975(h, n)
    return "%-58s hits %5d  frac %.3e  r97.5 %.3e  m*r(41) %.4f  m*r(73) %.4f" % (label, h, h / n, r, 41 * r, 73 * r)


def events(M, chosen=None):
    """per candidate: the class-choosing event (some class <= OBS, every other >= BAR); with `chosen` (a 25/30 class index
    per candidate, -1 if absent) the event on that class only"""
    lo = M <= OBS + 1e-9; srt = np.sort(M, axis=0)
    any_ = lo.any(0); cc = any_ & (srt[1] >= BAR)
    if chosen is None: return any_, cc
    ok = chosen >= 0; c = np.where(ok, chosen, 0)
    own = M[c, np.arange(M.shape[1])]
    others = np.where(np.arange(M.shape[0])[:, None] == c[None, :], np.inf, M).min(0)
    return ok & (own <= OBS + 1e-9) & (others >= BAR)


for tag in (sys.argv[1:] or ["valid", "fresh160k", "fresh10M"]):
    k = np.load(D / ("kd_%s.npz" % tag)); n = int(k["n"]); M = k["classmin"]
    any_, cc = events(M)
    srt = np.sort(M, axis=0)
    print("\n== %s: %d targets" % (tag, n))
    print(line("2/5 class <= obs (sealed conjunct 1)", int((M[I25] <= OBS + 1e-9).sum()), n))
    print(line("ANY class <= obs (class-choosing, specificity only)", int(any_.sum()), n))
    print(line("CLASS-CHOOSING: some class <= obs AND all others >= 16.75", int(cc.sum()), n))
    print(line("  stricter: ... AND all others >= runner-up 103.1", int((any_ & (srt[1] >= RUNNER)).sum()), n))
    o25 = np.delete(M, I25, axis=0).min(0)
    print(line("  2/5 <= obs AND all others >= 16.75", int(((M[I25] <= OBS + 1e-9) & (o25 >= BAR)).sum()), n))
    print(line("  a class OTHER than 2/5 <= obs AND all others >= 16.75", int((cc & ~(M[I25] <= OBS + 1e-9)).sum()), n))
    pa = D / ("prior_all_%s.npz" % tag)
    if not pa.exists(): continue
    p = np.load(pa); seeds = list(p["seeds"]); row = {int(s): i for i, s in enumerate(seeds)}
    pcls = p["cls"]; pchi = p["chi2"]
    to25 = np.array([CL.index(PCL[c]) if PCL[c] in CL else -1 for c in range(len(PCL))])
    present_all = to25[pcls] >= 0
    sel = np.array([row[int(s)] for s in k["cand_seed"]]); idx = k["cand_idx"]
    chosen = to25[pcls[sel, idx]]
    ev = events(M, chosen)
    h = int(ev.sum()); den = int(present_all.sum())
    print(line("PRIOR-CHOSEN, unconditional", h, n))
    print(line("PRIOR-CHOSEN, conditional on the prior class present at 25/30 (n = %d)" % den, h, den))
    # given a prior fit as good as the data's: of the targets with prior minimum <= thr, how many reach the event
    pmin = pchi[sel, idx]
    for thr in (3.5737, 5.3303, 16.750):          # B1749's and B1755's exact prior minima (prior.py), then the bar
        allfit = pchi <= thr
        for lab, mask_all, mask_c in (("any prior class", allfit, pmin <= thr),
                                      ("prior class 2/5", allfit & (pcls == PCL.index("2/5")), (pmin <= thr) & (pcls[sel, idx] == PCL.index("2/5"))),
                                      ("prior class present at 25/30", allfit & present_all, (pmin <= thr) & (chosen >= 0))):
            nt = int(mask_all.sum()); he = int((ev & mask_c).sum())
            print("prior min <= %.3f  %-30s targets %8d  25/30 event follows %5d  (%.3f)" % (thr, lab, nt, he, he / max(nt, 1)))
print("analyse_kd exit 0")
