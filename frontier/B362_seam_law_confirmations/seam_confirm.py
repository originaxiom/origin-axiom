"""B362 -- the pre-registered confirmations: (2,7) BRIGHT, (1,5) DARK, (4,5) DARK. Exact."""
from fractions import Fraction as Fr
import json, os, sys
_here = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_here, "..", "B360_seam_selection_rule"))
sys.path.insert(0, os.path.join(_here, "..", "B358_seam_certification"))
from seam_predict import theta_gens, word_power, powers, pair_readout
from cyclo_engine import mmul

def main():
    WR, WL = theta_gens()
    seeds = {}
    for m in (1, 2, 4, 5, 7):
        Wm = mmul(word_power(WR, m), word_power(WL, m))
        seeds[m] = powers(Wm)
        print(f"seed {m}: order {len(seeds[m])}", flush=True)
    results = {}
    for (a, b) in ((2, 7), (1, 5), (4, 5)):
        t = pair_readout(seeds[a], seeds[b])
        seam = {k: v for k, v in t.items() if v[3] != 0}
        svals = sorted({str(v[3]) for v in seam.values()})
        results[f"{a},{b}"] = dict(nonzero=len(t), seam=len(seam), svals=svals)
        print(f"pair ({a},{b}): nonzero {len(t)} | seam {len(seam)} | s {svals}", flush=True)
    json.dump(results, open(os.path.join(_here, "seam_confirm.json"), "w"))
    print("saved", flush=True)


def load_banked():
    return json.load(open(os.path.join(_here, "seam_confirm.json")))


if __name__ == "__main__":
    main()
