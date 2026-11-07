"""The web seat, 2026-11-06: THE LEAST-ACTION DEPARTURE (PREREGISTRATION_LEAST_ACTION.md in this folder, hypothesis H).
Data-free: SL(2, Z) arithmetic mod 5 and geodesic lengths only -- no frame value, no data, no held-out quantity.

A defect replaces m consecutive golden runs (L-start at a period boundary) by runs S = (r1, ..., rm), first and last
>= 2. It is line-invisible (L) when E = D_S D_g^-1 fixes each line of the golden pair own(LR) up to sign. Its excess
length is lim_k [l(D_S X (LR)^k) - l(D_g X (LR)^k)], X = R for odd m, I for even m, l = 2 arccosh(tr/2), evaluated at
k = 20 (and k = 30 for the cheapest, as a convergence check). Range: m <= 6 with runs <= 6; m = 7, 8 with runs <= 3.

  A  control: the single runs (n), n = 2..12 -- invisible iff n = 1 mod 5; excess against 2 log((n - 1 + sqrt5)/sqrt5)
  B  the enumeration: counts per m; the cheapest line-invisible defects (with their highest apex, reported only)
  C  H: is (6) the unique cheapest line-invisible defect in the range?

    python3 least_action_check.py
"""
import importlib.util
import itertools
import pathlib
import sys

import mpmath as mp

HERE = pathlib.Path(__file__).resolve().parent
sp = importlib.util.spec_from_file_location("departure_check", HERE / "departure_check.py")
D0 = importlib.util.module_from_spec(sp)
sys.modules["departure_check"] = D0
sp.loader.exec_module(D0)
L, R, LR, I2 = D0.L, D0.R, D0.LR, D0.I2
mul, inv, pw, tr, own, act, pm, fl = D0.mul, D0.inv, D0.pw, D0.tr, D0.own, D0.act, D0.pm, D0.fl
mp.mp.dps = 50
PAIR = own(LR)


def mat(runs):
    M = I2
    for i, r in enumerate(runs):
        M = mul(M, pw(L if i % 2 == 0 else R, r))
    return M


def invisible(runs):
    E = mul(mat(runs), inv(mat([1] * len(runs))))
    Ei = inv(E)
    return all(pm(act(w, Ei)) == w for w in PAIR)


def excess(runs, k=20):
    m = len(runs)
    X = R if m % 2 else I2
    W = mul(mul(mat(runs), X), pw(LR, k))
    G = mul(mul(mat([1] * m), X), pw(LR, k))
    return 2 * mp.acosh(mp.mpf(tr(W)) / 2) - 2 * mp.acosh(mp.mpf(tr(G)) / 2)


def closed_runs(runs, k=20):
    return list(runs) + ([1] if len(runs) % 2 else []) + [1] * (2 * k)


def space():
    for m in range(1, 9):
        top = 6 if m <= 6 else 3
        for runs in itertools.product(range(1, top + 1), repeat=m):
            if runs[0] >= 2 and runs[-1] >= 2:
                yield runs


if __name__ == "__main__":
    print("THE LEAST-ACTION DEPARTURE -- data-free check (the web seat, 2026-11-06)")
    print("  golden pair own(LR): %s" % fl(PAIR))

    print("\nA. CONTROL: single runs (n)")
    for n in range(2, 13):
        target = 2 * mp.log((n - 1 + mp.sqrt(5)) / mp.sqrt(5))
        print("  n = %2d: invisible %-5s excess %s (formula %s)" % (n, invisible((n,)), mp.nstr(excess((n,)), 12), mp.nstr(target, 12)))

    print("\nB. THE ENUMERATION (m <= 6, runs <= 6; m = 7, 8, runs <= 3)")
    counts, inv_list, cheapest_any = {}, [], None
    for runs in space():
        m = len(runs)
        c = counts.setdefault(m, [0, 0])
        c[0] += 1
        if invisible(runs):
            c[1] += 1
            inv_list.append((excess(runs), runs))
    for m in sorted(counts):
        print("  m = %d: defects %6d, line-invisible %5d" % (m, counts[m][0], counts[m][1]))
    inv_list.sort(key=lambda t: t[0])
    print("  the 15 cheapest line-invisible defects (excess at k = 20; highest apex of the closed approximant, reported only):")
    for d, runs in inv_list[:15]:
        im, re_ = D0.highest_cf(closed_runs(runs), reps=20)
        print("    %-26s excess %s   apex Im %s Re %s" % (runs, mp.nstr(d, 12), mp.nstr(im, 10), mp.nstr(re_, 6)))
    per_m = {}
    for d, runs in inv_list:
        if len(runs) not in per_m:
            per_m[len(runs)] = (d, runs)
    print("  the cheapest line-invisible defect at each m: %s" % "; ".join(
        "m=%d %s %s" % (m, per_m[m][1], mp.nstr(per_m[m][0], 8)) for m in sorted(per_m)))

    print("\nC. H")
    best_d, best = inv_list[0]
    runner_d, runner = inv_list[1]
    print("  cheapest: %s excess %s (k = 30: %s); next: %s excess %s; gap %s" % (
        best, mp.nstr(best_d, 15), mp.nstr(excess(best, 30), 15), runner, mp.nstr(runner_d, 15), mp.nstr(runner_d - best_d, 6)))
    ties = [runs for d, runs in inv_list if abs(d - best_d) < mp.mpf(10) ** -20]
    print("  H (the cheapest is (6), uniquely): %s; defects within 1e-20 of the minimum: %s" % (best == (6,) and ties == [(6,)], ties))
    print("least_action_check exit 0")
