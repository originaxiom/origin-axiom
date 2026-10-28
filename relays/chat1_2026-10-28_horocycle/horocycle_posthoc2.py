"""THE HOROCYCLE AND THE HEIGHT, post hoc read-outs, second part (POST HOC, labelled; written after the read-only referee of
the result note, to compute the numbers its corrections need before the note cites them).  No cell.  From the committed
census (8de923cea) and cells (84a323125) only; no frame value is computed.
  Q4  the lever of ln(m1/m2) (L_max minus L_2) per sector and reading over G: median and 10th-90th percentiles;
  Q5  on G, in (S~, S, S) and per horocycle: for steps of +0.1 in Im tau, the fraction at which all six logs fall; for steps
      of +0.1 in Re tau, the fraction at which the six move with mixed signs, and the fraction at which down's ln(m2/m3) and
      ln(m1/m3) move in opposite directions;
  Q6  the searches' found distances: the least, and the least among unflagged searches;
  Q7  the searches that ran six iterations: how many were still improving at the last one (by more than the stop
      tolerance 1e-5), and the largest last improvement;
  Q8  the refinements: per horocycle, how many ended on a bound of the rule's box (Re tau 0 or 1, Im tau 1.5 or 3.6), the
      least chi2_six among those, and the Im tau range of all refined minima.
    python3 -B horocycle_posthoc2.py > horocycle_posthoc2_out.txt"""
import json, pathlib
import numpy as np

HERE = pathlib.Path(__file__).resolve().parent


def main():
    d = np.load(HERE / "horocycle_census.npz"); idx = json.loads((HERE / "horocycle_census.json").read_text())
    cells = json.loads((HERE / "horocycle_cells.json").read_text())
    G = d["G"]
    with np.errstate(divide="ignore"):
        lg = np.log(G)                                                         # (40, 10, 13, sector, horocycle, reading, generation)
    q = lambda x: "%.3f (%.3f to %.3f)" % (float(np.median(x)), float(np.quantile(x, 0.1)), float(np.quantile(x, 0.9)))
    print("Q4 the lever of ln(m1/m2), L_max minus L_2, over G: median (10th to 90th percentile)")
    for s, sn in enumerate(("up", "down", "lep")):
        for r, rn in enumerate(("S", "S~")):
            x = ((lg[..., s, 0, r, 1] - lg[..., s, 0, r, 0]) - (lg[..., s, 1, r, 1] - lg[..., s, 1, r, 0])).ravel()
            print("   %-4s %-2s %s" % (sn, rn, q(x[np.isfinite(x)])))
    cfg = (1, 0, 0)                                                            # (S~, S, S): up S~, down S, lep S
    six = lambda h: np.stack([lg[..., s, h, cfg[s], g] for s in range(3) for g in (0, 1)], axis=-1)   # (40, 10, 13, 6)
    print("Q5 steps on G in (S~, S, S)")
    for h, hn in enumerate(("L_max", "L_2")):
        v = six(h)
        dim = v[:, :, 1:] - v[:, :, :-1]                                       # +0.1 in Im tau
        dre = v[:, 1:, :] - v[:, :-1, :]                                       # +0.1 in Re tau
        fin_i = np.all(np.isfinite(dim), axis=-1); fin_r = np.all(np.isfinite(dre), axis=-1)
        all_fall = np.all(dim < 0, axis=-1)[fin_i]
        mixed_r = (~(np.all(dre > 0, axis=-1) | np.all(dre < 0, axis=-1)))[fin_r]
        opp_r = (np.sign(dre[..., 2]) != np.sign(dre[..., 3]))[fin_r]
        print("   %s: Im tau steps %d, all six logs fall at %.4f; Re tau steps %d, mixed signs at %.4f, down's two ratios opposite at %.4f"
              % (hn, int(fin_i.sum()), float(all_fall.mean()), int(fin_r.sum()), float(mixed_r.mean()), float(opp_r.mean())))
    S = [o for o in idx["searches"] if "A" in o]
    A = np.array([o["A"] for o in S]); fl = np.array([o["flagged"] for o in S])
    print("Q6 found distances: least %.4f over all %d searches; least among the %d unflagged %.4f; unflagged below 0.15: %d"
          % (float(A.min()), len(S), int((~fl).sum()), float(A[~fl].min()), int(((~fl) & (A < 0.15)).sum())))
    six_it = [o for o in S if o["iterations"] >= 6]
    last = [o["path"][-2][2] - o["path"][-1][2] if len(o["path"]) >= 2 else 0.0 for o in six_it]
    print("Q7 searches with six iterations: %d; still improving by more than 1e-5 at the last: %d; largest last improvement %.2e"
          % (len(six_it), sum(x > 1e-5 for x in last), max(last) if last else 0.0))
    nm = cells["readout_nelder_mead"]
    for hn in ("L_max", "L_2"):
        xs = [o for o in nm if o["horocycle"] == hn]
        onb = [o for o in xs if min(abs(o["x"][0] - 0.0), abs(o["x"][0] - 1.0)) < 1e-9 or min(abs(o["x"][1] - 1.5), abs(o["x"][1] - 3.6)) < 1e-9]
        im = [o["x"][1] for o in xs]
        print("Q8 %s refinements: %d of %d end on a bound of the box; least chi2_six among them %s; refined Im tau %.3f to %.3f; on an Im bound %d"
              % (hn, len(onb), len(xs), ("%.2f" % min(o["chi2"] for o in onb)) if onb else "-", min(im), max(im),
                 sum(1 for o in xs if min(abs(o["x"][1] - 1.5), abs(o["x"][1] - 3.6)) < 1e-9)))
    print("horocycle posthoc2 exit 0")


if __name__ == "__main__":
    main()
