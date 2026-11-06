"""The web seat, 2026-11-06: THE LEADING RUNG-INVISIBLE SADDLE UNDER THE PRINCIPLE'S ACTION (PREREGISTRATION_CLUSTERS.md).
Data-free: lengths of closed threads (least_action_check.py's space and excess; the post hoc's rung class). No coupling,
scale ratio or held-out quantity.

    python3 cluster_check.py
"""
import importlib.util
import pathlib
import sys

import mpmath as mp

HERE = pathlib.Path(__file__).resolve().parent
sp = importlib.util.spec_from_file_location("least_action_posthoc_rung", HERE / "least_action_posthoc_rung.py")
RG = importlib.util.module_from_spec(sp)
sys.modules["least_action_posthoc_rung"] = RG
sp.loader.exec_module(RG)
LA = RG.LA
mp.mp.dps = 50
G = 2 * mp.log((1 + mp.sqrt(5)) / 2)


def D(runs, ex):
    return (sum(runs) - len(runs)) * G - ex


if __name__ == "__main__":
    print("THE LEADING RUNG-INVISIBLE SADDLE UNDER THE PRINCIPLE'S ACTION -- data-free check (the web seat, 2026-11-06)")
    rung = []
    for runs in LA.space():
        if RG.klass(RG.E_of(runs)) == 0:
            ex = LA.excess(runs)
            rung.append((runs, ex, D(runs, ex)))
    print("  rung-invisible defects in the range: %d" % len(rung))
    byA = sorted(rung, key=lambda t: t[1])
    byB = sorted(rung, key=lambda t: t[2])
    rank6 = [t[0] for t in byB].index((6,)) + 1
    print("  (A) excess at fixed runs: cheapest %s (excess %s)" % (byA[0][0], mp.nstr(byA[0][1], 10)))
    print("  (B) loss at fixed moves: the run of 6 ranks %d of %d (D = %s); the ten cheapest:" % (
        rank6, len(rung), mp.nstr(D((6,), LA.excess((6,))), 10)))
    for runs, ex, d in byB[:10]:
        print("      %-28s D = %s, excess %s" % (str(runs), mp.nstr(d, 8), mp.nstr(ex, 8)))
    per_run = [t for t in rung if all(r in (1, 6) for r in t[0])]
    print("  per-run conservation (every run in {1, 6}): %d defects; cheapest under (A) %s, under (B) %s" % (
        len(per_run), min(per_run, key=lambda t: t[1])[0], min(per_run, key=lambda t: t[2])[0]))
    print("cluster_check exit 0")
