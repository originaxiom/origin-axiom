"""THE HOROCYCLE AND THE HEIGHT, post hoc read-outs (POST HOC, labelled; written after the cells were read once, 84a323125).
No cell.  From the committed census (8de923cea) only; no frame value is computed.
  Q1  the levers L_max - L_2 per sector, reading (S, S~) and generation over G: median and 10th-90th percentiles;
  Q2  in the cells' configuration (S~, S, S): the fraction of G points, and of the 480 base points, at which the six
      levers do not all share one sign (a shift of Im tau moves all six logs the same way at leading order);
  Q3  at the absorption searches' minima: each component's median residual, and the fraction of base points whose
      residuals do not all share one sign.
    python3 -B horocycle_posthoc.py > horocycle_posthoc_out.txt"""
import json, pathlib
import numpy as np

HERE = pathlib.Path(__file__).resolve().parent
NAMES = ("up2", "up1", "down2", "down1", "lep2", "lep1")


def main():
    d = np.load(HERE / "horocycle_census.npz"); idx = json.loads((HERE / "horocycle_census.json").read_text())
    G = d["G"]                                                                 # (40, 10, 13, sector, horocycle, reading, generation)
    with np.errstate(divide="ignore"):
        lg = np.log(G)
    lev = lg[..., 0, :, :] - lg[..., 1, :, :]                                  # (40, 10, 13, sector, reading, generation)
    q = lambda x: "%.3f (%.3f to %.3f)" % (float(np.median(x)), float(np.quantile(x, 0.1)), float(np.quantile(x, 0.9)))
    print("Q1 the levers ln r(L_max) - ln r(L_2) over G: median (10th to 90th percentile)")
    for s, sn in enumerate(("up", "down", "lep")):
        for r, rn in enumerate(("S", "S~")):
            x2, x1 = lev[..., s, r, 0].ravel(), lev[..., s, r, 1].ravel()
            ok = np.isfinite(x2) & np.isfinite(x1)
            print("   %-4s %-2s  second generation %s;  first generation %s" % (sn, rn, q(x2[ok]), q(x1[ok])))
    cfg = {"up": 1, "down": 0, "lep": 0}                                       # (S~, S, S)
    six_lev = np.stack([lev[..., s, cfg[sn], g] for s, sn in enumerate(("up", "down", "lep")) for g in (0, 1)], axis=-1)   # (40, 10, 13, 6)
    fin = np.all(np.isfinite(six_lev), axis=-1)
    mixed = ~(np.all(six_lev > 0, axis=-1) | np.all(six_lev < 0, axis=-1))
    print("Q2 (S~, S, S): the six levers do not all share one sign at %.4f of the G points with finite values" % float(mixed[fin].mean()))
    re_g, im_g = idx["re_G"], idx["im_G"]
    bp = idx["base_points"]
    bm = [bool(mixed[li, re_g.index(re_t), im_g.index(im_t)]) for li, re_t, im_t in bp]
    print("   and at %d of the %d base points" % (sum(bm), len(bm)))
    neg = {NAMES[i]: float((six_lev[..., i][fin] < 0).mean()) for i in range(6)}
    print("   the fraction of G points with a negative lever, per ratio: %s" % {k: round(v, 4) for k, v in neg.items()})
    S = [o for o in idx["searches"] if o.get("residual")]
    R = np.array([o["residual"] for o in S])                                    # L_2 at the minimum minus L_max
    print("Q3 at the searches' minima (%d base points): the median residual (L_2 at the minimum minus L_max) per ratio: %s"
          % (len(S), {NAMES[i]: round(float(np.median(R[:, i])), 4) for i in range(6)}))
    rm = ~(np.all(R > 0, axis=1) | np.all(R < 0, axis=1))
    print("   residuals not all of one sign at %d of %d; flagged among them %d" % (int(rm.sum()), len(S), int(sum(o["flagged"] for o, m in zip(S, rm) if m))))
    print("horocycle posthoc exit 0")


if __name__ == "__main__":
    main()
