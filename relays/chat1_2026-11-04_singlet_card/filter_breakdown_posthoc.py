"""POST HOC (after the card's output 6d2c385b1 was read): which part of main's filter fails under each variant.  It re-reads
only the coarse facts the card's filter already read, at the card's 1 380 points: for each variant, how many points have
the up sector hierarchical (s2 > 0, 1e-12 < s0/s2 < 0.01, s1/s2 < 0.1), the down sector hierarchical, both, and up steeper
than down (the filter's last two conditions), and the median s1/s2 and s0/s2 per quark sector.  No CKM element is read.

    python3 filter_breakdown_posthoc.py <main checkout>      (main at eb130f01f)
"""
import pathlib
import sys

import numpy as np

HERE = pathlib.Path(__file__).resolve().parent
src = (HERE / "admissible_singlet_card.py").read_text().split('if __name__ == "__main__":')[0]
exec(compile(src, "admissible_singlet_card.py", "exec"))


def parts(Y):
    sp = spectra(Y)
    su, sd = sp["up"][1], sp["down"][1]
    hu, hd = hier(su), hier(sd)
    steeper = su[1] / su[2] < sd[1] / sd[2] / 2 and su[0] / su[2] < sd[0] / sd[2]
    return hu, hd, steeper, su[1] / su[2], su[0] / su[2], sd[1] / sd[2], sd[0] / sd[2]


if __name__ == "__main__":
    tasks = [(a, b, t) for (a, b) in KEPT for t in TAUS]
    with Pool(4) as pool:
        FR = dict(pool.map(frame_task, tasks, chunksize=4))
    rbar = float(np.median([2 * abs(FR[p][2]) / abs(FR[p][3]) for p in tasks]))
    print("POST HOC: the filter's parts at the card's %d points (rbar %.4g)" % (len(tasks), rbar))
    print("    variant    up hier  down hier  both  up steeper  both+steeper  | median s1/s2 up, s0/s2 up, s1/s2 down, s0/s2 down")
    for v in VARIANTS:
        rows = [parts(yukawas(M, DR, sigmas(v, a0, E, rbar), READS[v])) for (M, DR, a0, E) in (FR[p] for p in tasks)]
        hu = sum(r[0] for r in rows); hd = sum(r[1] for r in rows); hb = sum(r[0] and r[1] for r in rows)
        st = sum(r[2] for r in rows); al = sum(r[0] and r[1] and r[2] for r in rows)
        med = [float(np.median([r[k] for r in rows])) for k in (3, 4, 5, 6)]
        print("    %-10s %7d  %9d  %4d  %10d  %12d  | %.3g, %.3g, %.3g, %.3g" % (v, hu, hd, hb, st, al, *med))
