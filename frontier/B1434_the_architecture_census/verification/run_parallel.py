#!/usr/bin/env python3
"""Runner for the sealed census: the sealed population (length <= 6, torsion <= 330, k <= 6) split over processes.
Calls architecture_census.census unchanged.  usage: run_parallel.py <slice> <nslices>"""
import sys, json, time, pathlib
import architecture_census as ac
HERE = pathlib.Path(__file__).resolve().parent
i, n = int(sys.argv[1]), int(sys.argv[2])
jobs = []
for w in ac.states(6):
    for eps in (+1, -1):
        for k in range(1, 7):
            ng, rels, mu, lam, tau, A, tors = ac.level(eps, w, k)
            if tors == 0 or tors > 330: continue
            jobs.append((tors, eps, w, k))
jobs.sort()
res = []
for j, (tors, eps, w, k) in enumerate(jobs):
    if j % n != i: continue
    t0 = time.time(); o = ac.census(eps, w, k); o["seconds"] = round(time.time() - t0, 1); res.append(o)
    print(o["state"], k, "tr", o["trace"], "tors", o["torsion"], "loci", o["loci"], "nonsq", o["loci_nonsquare"], "fire", o["firing"],
          "gen", o["generation_backgrounds"], "lifted", o["lifted"], "orbits", o["backgrounds_by_orbit_size"], "absI", o["abs_counts"],
          "signs", o["signs"], "h1", o["h1_multiset"], "differ", o["differing_at_other_primes"], flush=True)
    json.dump(res, open(HERE / f"census_slice_{i}.json", "w"), indent=1)
print("DONE", flush=True)
