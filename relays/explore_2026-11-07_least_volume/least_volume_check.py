"""The explore seat, 2026-11-07: THE LEAST-VOLUME DEPARTURE (PREREGISTRATION_LEAST_VOLUME.md in this folder; HV1-HV3).
Data-free: SnapPy volumes of once-punctured-torus bundles and SL(2, Z) arithmetic mod 5 only -- no frame value, no data,
no held-out quantity. The defects, classes and ranges are the web seat's (its modules copied here, pinned at ecda7de70).

  C1-C5  controls (the object, cyclic covers, geometric solutions, single runs, the (6) / (2,2,2) length tie)
  E      rung-invisible defects (E = +-I mod 5): least excess volume, HV1
  F      line-invisible defects (E = +-(LR)^a mod 5): least excess volume against least excess length, HV2
  G      depth sensitivity of the volume action on the rung-invisible single runs 6, 11, 16, HV3

    python3 least_volume_check.py
"""
import importlib.util
import math
import pathlib
import sys
import time

import mpmath as mp
import snappy

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))


def load(name):
    sp = importlib.util.spec_from_file_location(name, HERE / (name + ".py"))
    mod = importlib.util.module_from_spec(sp)
    sys.modules[name] = mod
    sp.loader.exec_module(mod)
    return mod


LA = load("least_action_check")
PH = load("least_action_posthoc_rung")
D0 = LA.D0
VOL4 = float(snappy.ManifoldHP("m004").volume())
K = 10
BAD = []


def letters(runs, k):
    s = "".join(("L" if i % 2 == 0 else "R") * r for i, r in enumerate(runs))
    if len(runs) % 2:
        s += "R"
    return s + "LR" * k


def vol(word, hp=False):
    M = (snappy.ManifoldHP if hp else snappy.Manifold)("b++" + word)
    return float(M.volume()), M.solution_type()


def dV(runs, k=K, hp=False):
    v, st = vol(letters(runs, k), hp)
    if st != "all tetrahedra positively oriented":
        BAD.append((runs, k, st))
        return None
    return v - (k + (len(runs) + 1) // 2) * VOL4


def ranked(items):
    out = [(d, r) for d, r in items if d is not None]
    out.sort(key=lambda t: t[0])
    return out


if __name__ == "__main__":
    t0 = time.time()
    print("THE LEAST-VOLUME DEPARTURE -- data-free check (the explore seat, 2026-11-07)")

    print("\nC1. the object")
    M = snappy.Manifold("b++LR")
    ident = [str(x) for x in M.identify()]
    print("  b++LR -> %s; volume %.12f; %s" % (ident, M.volume(), M.solution_type()))
    c1 = ident[0].startswith("m004") and abs(float(M.volume()) - 2.02988321282) < 1e-10
    print("  C1 pass: %s" % c1)

    print("\nC2. cyclic covers")
    c2 = True
    for k in range(2, 7):
        v, st = vol("LR" * k)
        ok = abs(v - k * VOL4) < 1e-9
        c2 &= ok
        print("  (LR)^%d: %.12f vs %.12f  %s" % (k, v, k * VOL4, "ok" if ok else "FAIL"))
    print("  C2 pass: %s" % c2)

    print("\nC4. single runs n = 2..16: excess volume at k = 8, 10, 12 (and the excess length, for comparison)")
    single = {}
    for n in range(2, 17):
        a, b, c = dV((n,), 8), dV((n,), 10), dV((n,), 12)
        single[n] = b
        print("  n = %2d  class %-4s  dV(8) %.10f  dV(10) %.10f  dV(12) %.10f  |dV12-dV10| %.1e   dL %s" % (
            n, PH.klass(PH.E_of((n,))), a, b, c, abs(c - b), mp.nstr(LA.excess((n,)), 10)))
    rising = all(single[n + 1] > single[n] for n in range(2, 16))
    print("  dV rises with n on 2..16: %s" % rising)

    print("\nC5. the length tie (6) against (2, 2, 2)")
    print("  excess length (6) %s, (2,2,2) %s; classes %s, %s" % (
        mp.nstr(LA.excess((6,)), 15), mp.nstr(LA.excess((2, 2, 2)), 15), PH.klass(PH.E_of((6,))), PH.klass(PH.E_of((2, 2, 2)))))
    print("  excess volume (6) %.10f, (2,2,2) %.10f" % (dV((6,)), dV((2, 2, 2))))

    print("\nE / F. the enumeration (the web seat's range)")
    rung, line, count = [], [], {}
    for runs in LA.space():
        a = PH.klass(PH.E_of(runs))
        count[a] = count.get(a, 0) + 1
        if a is None:
            continue
        d = dV(runs)
        if a == 0:
            rung.append((d, runs))
        line.append((d, runs))
    print("  classes: rung-invisible %d; phase shifts a = 1..4 %s; neither %d; total %d" % (
        count.get(0, 0), [count.get(a, 0) for a in range(1, 5)], count.get(None, 0), sum(count.values())))
    print("  C3: non-geometric solutions met: %d %s" % (len(BAD), BAD[:5]))

    print("\nE. HV1 -- the rung-invisible defects by excess volume (k = 10; k = 8, 12 and high precision for the leaders)")
    R_ = ranked(rung)
    for d, runs in R_[:12]:
        print("    %-26s dV %.10f  (k=8 %.10f, k=12 %.10f)  dL %s" % (
            runs, d, dV(runs, 8), dV(runs, 12), mp.nstr(LA.excess(runs), 10)))
    best_d, best = R_[0]
    nxt_d, nxt = R_[1]
    hp_best, hp_next = dV(best, 12, hp=True), dV(nxt, 12, hp=True)
    print("  least: %s dV %.12f; next %s dV %.12f; gap %.3e (high precision at k = 12: %.12f, %.12f)" % (
        best, best_d, nxt, nxt_d, nxt_d - best_d, hp_best, hp_next))
    hv1 = best == (6,) and (nxt_d - best_d) > 1e-6
    print("  HV1 (least excess volume among rung-invisible defects is (6), uniquely): %s" % hv1)

    print("\nF. HV2 -- the line-invisible defects by excess volume, against excess length")
    Lv = ranked(line)
    for d, runs in Lv[:10]:
        print("    %-26s class %d  dV %.10f  dL %s" % (runs, PH.klass(PH.E_of(runs)), d, mp.nstr(LA.excess(runs), 10)))
    least_len = min(((LA.excess(r), r) for d, r in line if d is not None), key=lambda t: t[0])
    print("  least excess volume: %s; least excess length: %s; same: %s" % (Lv[0][1], least_len[1], Lv[0][1] == least_len[1]))

    print("\nG. HV3 -- depth sensitivity of the volume action on the rung-invisible single runs")
    g = {n: dV((n,), 12) for n in (6, 11, 16)}
    print("  dV(6) %.10f, dV(11) %.10f, dV(16) %.10f; (dV11 - dV6)/dV6 = %.4f; (dV16 - dV11)/dV6 = %.4f" % (
        g[6], g[11], g[16], (g[11] - g[6]) / g[6], (g[16] - g[11]) / g[6]))
    print("  HV3 saturation (dV11 - dV6 < 0.05 dV6): %s" % ((g[11] - g[6]) < 0.05 * g[6]))
    print("  for comparison, the excess length: dL(6) %s, dL(11) %s, dL(16) %s" % tuple(
        mp.nstr(LA.excess((n,)), 10) for n in (6, 11, 16)))

    print("\nReported only, never a criterion: the highest apex of the least-volume rung-invisible defect (k = 20)")
    im, re_ = D0.highest_cf(LA.closed_runs(best), reps=20)
    print("  %s: apex Im %s Re %s" % (best, mp.nstr(im, 10), mp.nstr(re_, 6)))
    print("\nruntime %.1f s" % (time.time() - t0))
    print("least_volume_check exit 0")
