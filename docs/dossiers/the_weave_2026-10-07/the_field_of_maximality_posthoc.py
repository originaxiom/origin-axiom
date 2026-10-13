"""W57, POST HOC (written after W57's one run and its read-out; labelled; W57's JSON is unchanged). W57's joint test never
reached a resolving rung: no draw of either model came within 32 sigma of the data in all ten shape numbers at once,
and at 64 sigma both accept about 40%. These checks read the same draws (regenerated from W57's own seeds) with
statistics that need no box.

  P1  the nearest-neighbour distance d_min (max-norm in sigma units) from the data at M_Z to each model's draws:
      S_mix, each placement, anarchy; and at the nearest seed draw, each observable's |x - t| / sigma.
  P2  typicality without a box: p_nn = (1 + #{pseudo-data whose own d_min to S_mix >= the data's}) / 201, with W57's
      200 pseudo-data (the same stream).
  P3  the same d_min for the observer-conditioned S_mix (every m1/m3 < 1e-2), and its marginals there.
  P4  the share of each model's draws with all three first-generation ratios below 1e-2, and with all six mass ratios
      within a factor 10 of the data's.

Run: python3 the_field_of_maximality_posthoc.py  ->  the_field_of_maximality_posthoc.json beside it.
"""
import os

for _v in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ.setdefault(_v, "1")

import json  # noqa: E402
import sys  # noqa: E402
from multiprocessing import Pool  # noqa: E402
from pathlib import Path  # noqa: E402

import numpy as np  # noqa: E402

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import the_field_of_maximality as FM  # noqa: E402  (W57: the measures, the draws, the targets)

OUT = HERE / "the_field_of_maximality_posthoc.json"


def regenerate():
    tasks = [(pi, b, FM.BATCH) for pi in range(len(FM.PLACEMENTS)) for b in range(FM.N_PER // FM.BATCH)]
    with Pool(FM.NPROC) as pool:
        rows = pool.map(FM.seed_batch, tasks, chunksize=1)
        arows = pool.map(FM.anarchy_batch, [(b, FM.BATCH) for b in range(FM.N_ANARCHY // FM.BATCH)], chunksize=4)
    by = {pi: np.concatenate([X for p2, X, _ in rows if p2 == pi]) for pi in range(len(FM.PLACEMENTS))}
    return by, np.concatenate([by[pi] for pi in range(len(FM.PLACEMENTS))]), np.concatenate(arows)


def nearest(X, t, sig):
    d = FM.dist(X, t, sig)
    i = int(np.argmin(d))
    return float(d[i]), {lab: float(abs(X[i, k] - t[k]) / sig[k]) for k, lab in enumerate(FM.LABELS)}


def main():
    by, S, A = regenerate()
    stored = json.loads((HERE / "the_field_of_maximality.json").read_text(encoding="utf-8"))
    same = (stored["main (S_mix against anarchy, the data at M_Z)"]["accepted on the ladder (seed, anarchy)"]["64"]
            == [int(np.sum(FM.dist(S, *FM.target("HZ2021_running_masses_MZ.json")) <= 64)),
                int(np.sum(FM.dist(A, *FM.target("HZ2021_running_masses_MZ.json")) <= 64))])
    t, sig = FM.target("HZ2021_running_masses_MZ.json")
    p1 = {"S_mix": nearest(S, t, sig), "anarchy": nearest(A, t, sig)}
    for pi, pl in enumerate(FM.PLACEMENTS):
        p1[str(pl)] = nearest(by[pi], t, sig)
    pseudo = FM.pseudo_draws([5702, 99], list(range(len(FM.PLACEMENTS))), FM.N_PSEUDO)
    d0 = p1["S_mix"][0]
    dps = [float(np.min(FM.dist(S, x, sig))) for x in pseudo]
    p2 = {"the data's d_min to S_mix": d0,
          "the pseudo-data's d_min to S_mix (min, median, max)": [min(dps), float(np.median(dps)), max(dps)],
          "p_nn": (1 + sum(x >= d0 for x in dps)) / (len(dps) + 1)}
    cond = np.all(S[:, [0, 2, 4]] < np.log(1e-2), axis=1)
    Sc = S[cond]
    Fc = (np.sum(Sc <= t, axis=0) + 1) / (len(Sc) + 2)
    p3 = {"kept": int(len(Sc)), "d_min to the conditioned S_mix": nearest(Sc, t, sig),
          "the marginals there (two-sided p)": {lab: float(2 * min(f, 1 - f)) for lab, f in zip(FM.LABELS, Fc)}}
    within10 = lambda X: float(np.mean(np.all(np.abs(X[:, :6] - t[:6]) <= np.log(10), axis=1)))  # noqa: E731
    first = lambda X: float(np.mean(np.all(X[:, [0, 2, 4]] < np.log(1e-2), axis=1)))  # noqa: E731
    p4 = {"S_mix": [first(S), within10(S)], "anarchy": [first(A), within10(A)]}
    for pi, pl in enumerate(FM.PLACEMENTS):
        p4[str(pl)] = [first(by[pi]), within10(by[pi])]
    out = {"status": "W57 post hoc: statistics that need no box (labelled post hoc; W57's JSON unchanged)",
           "the regenerated draws reproduce W57's stored count at 64 sigma": bool(same),
           "P1: d_min from the data (sigma units), and each observable's |x - t| / sigma at the nearest draw": p1,
           "P2: typicality by nearest-neighbour distance": p2,
           "P3: the observer-conditioned S_mix": p3,
           "P4: shares (all three m1/m3 < 1e-2; all six mass ratios within a factor 10 of the data's)": p4}
    OUT.write_text(json.dumps(out, indent=1) + "\n", encoding="utf-8")
    print(json.dumps({k: (v if not isinstance(v, dict) else "...") for k, v in out.items()}, indent=1))


if __name__ == "__main__":
    main()
