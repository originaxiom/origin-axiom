"""B361 -- the H-min vs H-loc discriminator: pairs (1,7) and (3,7), theta lift, exact.
Pre-registered: BRIGHT => H-loc (any 5-elliptic & 3-nontrivial seed selects); DARK => H-min
(the A_2 residue class specifically). m=7: disc(A_7) = 7^4+4*49 = 2597 = 2 mod 5 (QNR: 5-elliptic),
nontrivial mod 3 -- the same local profile as silver."""
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
    for m in (1, 3, 7):
        Wm = mmul(word_power(WR, m), word_power(WL, m))
        seeds[m] = powers(Wm)
        print(f"seed {m}: operator order {len(seeds[m])}", flush=True)

    results = {}
    for (a, b) in ((1, 7), (3, 7)):
        t = pair_readout(seeds[a], seeds[b])
        seam = {k: v for k, v in t.items() if v[3] != 0}
        svals = sorted({str(v[3]) for v in seam.values()})
        results[f"{a},{b}"] = dict(nonzero=len(t), seam=len(seam), svals=svals,
                                   sample={str(k): [str(x) for x in v] for k, v in list(seam.items())[:4]})
        print(f"pair ({a},{b}): nonzero {len(t)} | seam-bearing {len(seam)} | s-values {svals}", flush=True)
    json.dump(results, open(os.path.join(_here, "seam_disc.json"), "w"))
    print("saved", flush=True)


def load_banked():
    return json.load(open(os.path.join(_here, "seam_disc.json")))


if __name__ == "__main__":
    main()
