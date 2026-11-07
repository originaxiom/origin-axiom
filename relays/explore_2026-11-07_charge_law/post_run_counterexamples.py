"""POST-RUN (written after charge_law_proof_out.txt was read; disclosed): for each S where the B-bound failed, build the
search's minimizing phase sequence as an actual defect (the least positions consistent with the phases), and check it
exactly, by a route independent of the search:
  - E = D_S D_g^-1 in exact integers, and the charge premise E = +-I mod every N in S;
  - the excess by the web seat's own `excess` (k = 20, mpmath), against the single run lcm(S) + 1;
  - the excess again by Lemma A (2 log Q(E)), as a cross-check;
  - the highest apex of the defect's closed approximant (reported).
A defect that satisfies the premise with excess below the single run's is a counterexample to P-737's law at S.
    python3 post_run_counterexamples.py"""
import importlib.util
import math
import pathlib
import sys

import mpmath as mp

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sp = importlib.util.spec_from_file_location("charge_law_proof", HERE / "charge_law_proof.py")
CP = importlib.util.module_from_spec(sp)
sys.modules["charge_law_proof"] = CP
sp.loader.exec_module(CP)
LA, D0 = CP.LA, CP.D0

for S in [(3, 4), (3, 5), (4, 5), (2, 3, 5), (3, 4, 5), (2, 3, 4, 5), (5,)]:
    res = CP.search(S)
    Lm, per, path = res["L"], res["period"], [(int(p), int(s)) for p, s in res["path"]]
    pos, prev = [], None
    for p, s in path:
        if prev is None:
            q = 1
        else:
            d = (p - prev[0]) % per
            d = d if d else per
            q = prev[1] + d
        pos.append((q, s))
        prev = (p, q)
    m = pos[-1][0]
    runs = [1] * m
    for q, s in pos:
        runs[q - 1] = s + 1
    runs = tuple(runs)
    E = CP.E_int(runs)
    prem = all(CP.pmI(CP.red(E, N), N) for N in S)
    ex = LA.excess(runs)
    ex1 = LA.excess((Lm + 1,))
    mp.mp.dps = 120  # E's entries reach ~1e29 at long gaps; the float cross-check cancelled (first attempt crashed here)
    exA = float(2 * mp.log((E[0][0] + (E[0][1] + E[1][0]) * mp.phi + E[1][1] * mp.phi ** 2) / (2 + mp.phi)))
    mp.mp.dps = 50
    im, re_ = D0.highest_cf(LA.closed_runs(runs, 20), reps=20)
    print("S = %-14s L = %2d  search path (phase, s) %s" % (S, Lm, path))
    print("   defect: %d runs; nontrivial runs (position, run) %s" % (m, [(q, s + 1) for q, s in pos]))
    print("   premise E = +-I mod %s: %s;  excess %s (Lemma A: %.10f)  vs single run %d: %s;  below it: %s" % (
        S, prem, mp.nstr(ex, 12), exA, Lm + 1, mp.nstr(ex1, 12), prem and ex < ex1))
    print("   highest apex Im %s  Re %s  (single run %d: %s)" % (mp.nstr(im, 10), mp.nstr(re_, 6), Lm + 1,
                                                                mp.nstr((Lm) / mp.mpf(2) + mp.sqrt(5) / 2, 10)))
print("post_run_counterexamples exit 0")
