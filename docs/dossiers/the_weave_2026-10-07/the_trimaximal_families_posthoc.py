"""W43, POST HOC (written after W43's one run and its read-out; no cell depends on it). The run's tally under T-bar (x) T
counted one pair with a fixed TM2 column at family dimension 1 and one at dimension 3. A fixed column allows at most 2,
so the two were recomputed: the same pairs, B1620's rank rule, at 8 fresh points and three finite-difference steps, with
each sector's smallest relative eigenvalue gap of M M^dagger at each point. The run's estimator takes the maximum over
three points, so one point near a degeneracy can add a spurious rank.

Run: python3 the_trimaximal_families_posthoc.py  ->  the_trimaximal_families_posthoc.json beside it.
"""
import itertools
import json
import random
import sys
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import the_breaking_verified as BV  # noqa: E402
import the_trimaximal_families as TF  # noqa: E402

OUT = HERE / "the_trimaximal_families_posthoc.json"


def ranks(Bl, Bn, seed, h, npts=8):
    r = np.random.default_rng(seed)
    nl, nn = 2 * len(Bl), 2 * len(Bn)

    def V(x):
        return TF.left(TF.member(Bl, x[:nl])).conj().T @ TF.left(TF.member(Bn, x[nl:]))

    def gap(B, y):
        w = np.linalg.eigvalsh(TF.member(B, y) @ TF.member(B, y).conj().T)
        return float(min(np.diff(w)) / w[-1])

    out = []
    for _ in range(npts):
        x = r.normal(size=nl + nn)
        Jm = np.array([(TF.invariants(V(x + h * e)) - TF.invariants(V(x - h * e))) / (2 * h) for e in np.eye(nl + nn)]).T
        s = np.linalg.svd(Jm, compute_uv=False)
        out.append({"rank": int(sum(s > max(1e-5, 1e-6 * s[0]))), "smallest gaps": [round(gap(Bl, x[:nl]), 6),
                                                                                       round(gap(Bn, x[nl:]), 6)]})
    return out


def main():
    G, _, _, _ = BV.the_group_exact()
    subs, _ = TF.lattice(G)
    t = "T-bar (x) T"
    rng_exact, rng = random.Random(101), np.random.default_rng(101)     # the run's seeds, so the same pairs recur
    viable = []
    for H in subs:
        basis = BV.fixed_basis(H, t)
        if BV.viable_exact(basis, t, rng_exact) > 0:
            viable.append((H, TF.numeric_basis(basis, t)))
    rows = []
    for (Hl, Bl), (Hn, Bn) in itertools.product(viable, viable):
        types = TF.fixed_columns(Bl, Bn, rng)
        if types:
            d = TF.family_dim(Bl, Bn, rng)
            if "TM2" in types and d in (1, 3):
                per_h = {str(h): ranks(Bl, Bn, 5, h) for h in (1e-5, 1e-6, 1e-7)}
                all_ranks = [p["rank"] for v in per_h.values() for p in v]
                rows.append({"orders (charged leptons, neutrinos)": [len(Hl), len(Hn)], "the run's dimension": d,
                             "ranks at 8 points x 3 steps": sorted(set(all_ranks)),
                             "the dimension recomputed": max(set(all_ranks), key=all_ranks.count),
                             "points": per_h})
    out = {"status": "W43 POST HOC: the two outliers of the T-bar (x) T TM2 tally recomputed (no cell depends on them)",
           "outliers found again": len(rows), "rows": rows,
           "both recomputed at 2 or below": all(r["the dimension recomputed"] <= 2
                                                for r in rows)}
    OUT.write_text(json.dumps(out, indent=1) + "\n", encoding="utf-8")
    print(json.dumps({k: v for k, v in out.items() if k != "rows"}, indent=1))
    for r in rows:
        print(r["orders (charged leptons, neutrinos)"], r["the run's dimension"], "->", r["the dimension recomputed"],
              r["ranks at 8 points x 3 steps"])


if __name__ == "__main__":
    main()
