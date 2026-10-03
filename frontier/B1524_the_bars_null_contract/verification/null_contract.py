#!/usr/bin/env python3
"""B1524 -- THE BAR's null contract: the null laws under which its p is a probability, each checked with own code.

Not sealed: nothing here reads a frame, a state or a census outcome. Every check is a statement about distributions (exhaustive,
exact, or on a stated range), and B1518's banked numbers are re-read only to show which of its sealed decisions a change of
correction could touch.

  C1  The finite exchangeable law. In a stratum of N units with K carriers placed uniformly at random, independently of a fixed
      rule, the unit the rule picks carries with probability K/N. So p = K/N, that is (k + 1)/(n + 1) with k carriers among the
      n other units, is a valid p-value at every level. Checked by enumerating every placement (N <= 14) and every level.
  C2  THE BAR's r (B1518's null_model.clopper_pearson: the upper end of the exact two-sided 95% interval for k of n) is at least
      (k + 1)/(n + 1) for every k <= n <= 2000. So p = r is a conservative p-value under C1. Checked as
      P(Bin(n, (k + 1)/(n + 1)) <= k) >= 0.025, exactly in rationals for n <= 120 and in double precision with its margin to 2000,
      and directly against null_model's r.
  C3  The i.i.d. law (the comparable units and the chosen one i.i.d. Bernoulli(q)). The test 'the chosen unit carries and
      r <= alpha' has size sup_q q P_q(r(K, n) <= alpha) <= alpha, for alpha in (0.001, 0.005, 0.01, 0.025, 0.05) and n <= 2000.
      Proof for q <= 40 alpha: q <= alpha is trivial, and alpha < q <= 40 alpha follows from the interval's one-sided coverage
      0.975 (size <= 0.025 q). Above 40 alpha the size is computed.
  C4  The scan law. In a census of N units with K carriers, a scan of n exchangeable units finds a carrier with probability
      1 - C(N - K, n)/C(N, n). THE BAR's 1 - (1 - K/N)^n is never larger. Each factor (N - K - i)/(N - i) <= (N - K)/N, the
      difference being K i/(N (N - i)); checked exactly for N = 536 and 758, every K and every n. The binomial understates p, so
      the exact law replaces it. B1518's FITTED grade (m369 and s639, a scan of 24 at 87 of 536) stands, since its exact p is
      larger.
  C5  Several looks. Bonferroni, min(1, m p_min), is valid under any dependence (Boole's inequality). Sidak's 1 - (1 - p_min)^m
      is not. Under C1, two fixed-rule units of one stratum are negatively dependent: either carries with probability
      2c - c^2 + c (1 - c)/(N - 1), where c = K/N, and that exceeds Sidak's 2c - c^2. Exact counterexamples are given, and the
      search at alpha = 0.01 is reported. Bonferroni >= Sidak always (Bernoulli's inequality). Of B1518's sealed tests, T2 and T3
      (two looks each) reach the same decision under Bonferroni.
Usage: python3 null_contract.py            (writes null_contract.json; prints the checks)"""
import itertools
import json
import math
import pathlib
import sys
import time
from fractions import Fraction

import numpy as np
from scipy.optimize import minimize_scalar
from scipy.stats import binom

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[2]
sys.path.insert(0, str(ROOT / "frontier" / "B1518_the_bar" / "verification"))
import null_model as NM  # noqa: E402  (B1518's instrument, unchanged)


def c1_finite_law(nmax=14):
    """enumerate every placement of K carriers among N units; the fixed unit is unit 0"""
    worst, cases = Fraction(0), 0
    for N in range(1, nmax + 1):
        for K in range(N + 1):
            hits = total = 0
            for carriers in itertools.combinations(range(N), K):
                total += 1
                hits += 0 in carriers
            prob = Fraction(hits, total)
            assert prob == Fraction(K, N), (N, K, prob)
            # p = K/N when unit 0 carries, else 1; its size at level a is prob * [K/N <= a]; levels: every K'/N' up to N' = nmax
            for Np in range(1, nmax + 1):
                for Kp in range(Np + 1):
                    a = Fraction(Kp, Np)
                    size = prob if Fraction(K, N) <= a else Fraction(0)
                    worst = max(worst, size - a)
                    cases += 1
    return {"placements enumerated up to N": nmax, "(N, K, level) cases": cases, "max(size - level)": str(worst),
            "valid at every level": worst <= 0}


def binom_cdf_exact(k, n, p):
    return sum(Fraction(math.comb(n, j)) * p ** j * (1 - p) ** (n - j) for j in range(k + 1))


def c2_r_is_conservative(nmax=2000, nexact=120):
    exact_min = (Fraction(2), None)
    for n in range(1, nexact + 1):
        for k in range(n):        # k = n: r = 1 = (n + 1)/(n + 1) by definition
            v = binom_cdf_exact(k, n, Fraction(k + 1, n + 1))
            if v < exact_min[0]:
                exact_min = (v, (k, n))
    assert exact_min[0] >= Fraction(1, 40), exact_min
    fl_min, fl_where, direct_min, direct_where = 2.0, None, 2.0, None
    for n in range(1, nmax + 1):
        k = np.arange(n)
        v = binom.cdf(k, n, (k + 1) / (n + 1))
        i = int(np.argmin(v))
        if v[i] < fl_min:
            fl_min, fl_where = float(v[i]), (int(k[i]), n)
        if n <= 600 or n % 50 == 0:   # the instrument's own r, directly (beta quantiles; every n to 600, then every 50th)
            for kk in range(n + 1):
                r = NM.clopper_pearson(kk, n)[1]
                gap = r - (kk + 1) / (n + 1)
                if gap < direct_min:
                    direct_min, direct_where = gap, (kk, n)
    return {"exact (rationals), n <= %d: min P(Bin(n, (k+1)/(n+1)) <= k)" % nexact: [float(exact_min[0]), exact_min[1]],
            "double precision, n <= %d: same minimum" % nmax: [fl_min, fl_where],
            "needed": 0.025,
            "null_model r - (k+1)/(n+1), min over every k <= n <= 600 and every 50th n to 2000": [direct_min, direct_where],
            "r >= (k+1)/(n+1) everywhere checked": fl_min >= 0.025 and float(exact_min[0]) >= 0.025 and direct_min >= -1e-12}


def c3_iid_law(nmax=2000, alphas=(0.001, 0.005, 0.01, 0.025, 0.05)):
    out = {}
    for a in alphas:
        worst, where, gate_never = 0.0, None, 0
        for n in range(1, nmax + 1):
            r = np.array([NM.clopper_pearson(k, n)[1] for k in range(min(n, int(3 * a * n) + 30) + 1)])
            ks = np.nonzero(r <= a)[0]
            if len(ks) == 0:
                gate_never += 1
                continue
            kstar = int(ks.max())
            assert np.all(r[:kstar + 1] <= a)  # r is increasing in k

            def size(q):
                return q * binom.cdf(kstar, n, q)

            grid = np.concatenate([np.linspace(1e-6, a, 200), np.linspace(a, 1, 2000)])
            vals = size(grid)
            j = int(np.argmax(vals))
            lo, hi = grid[max(j - 1, 0)], grid[min(j + 1, len(grid) - 1)]
            res = minimize_scalar(lambda q: -size(q), bounds=(lo, hi), method="bounded", options={"xatol": 1e-12})
            best = max(float(vals[j]), float(-res.fun))
            # the region q > 40 a, where the coverage argument alone does not bound the size
            tail = grid[grid > 40 * a]
            tail_max = float(size(tail).max()) if len(tail) else 0.0
            if best > worst:
                worst, where = best, (n, kstar, float(grid[j]))
            assert tail_max <= a, (a, n, tail_max)
        out[str(a)] = {"max size over n <= %d" % nmax: worst, "at (n, k*, q)": where, "n with no gate at all": gate_never,
                       "size <= alpha": worst <= a}
    return out


def c4_scan_law(Ns=(536, 758)):
    out = {}
    for N in Ns:
        # the termwise inequality, exactly, for every K and i: N (N - K - i) <= (N - K)(N - i), the gap being K i
        for K in range(N + 1):
            for i in range(N - K + 1):
                assert (N - K) * (N - i) - N * (N - K - i) == K * i
        worst = 0.0
        for K in range(1, N):
            n = np.arange(1, N - K + 1)
            # log C(N-K, n)/C(N, n) = sum log((N-K-i)/(N-i)); binomial: n log(1 - K/N)
            lr = np.cumsum(np.log((N - K - np.arange(N - K)) / (N - np.arange(N - K))))
            hyper = 1 - np.exp(lr[:len(n)])
            bino = 1 - (1 - K / N) ** n
            worst = max(worst, float((bino - hyper).max()))
        out[str(N)] = {"max(binomial - exact) over every K, n": worst, "binomial never larger": worst <= 1e-15}
    N, K, n = 536, 87, 24
    exact = 1 - Fraction(math.comb(N - K, n), math.comb(N, n))
    bino = 1 - (1 - Fraction(K, N)) ** n
    out["B1518 m369 and s639 (a scan of 24 at 87 of 536)"] = {"binomial (banked)": round(float(bino), 6),
                                                               "exact": round(float(exact), 6), "grade": "FITTED either way"}
    return out


def c5_dependence(alpha=0.01):
    # two fixed-rule units in one stratum of N with K carriers, under C1: p_i = K/N if unit i carries, else 1
    def either(N, K):
        return 1 - Fraction((N - K) * (N - K - 1), N * (N - 1))

    examples = []
    for N, K in ((200, 1), (1000, 5), (40, 1)):
        c = Fraction(K, N)
        a_sidak = 1 - (1 - c) ** 2                  # the level at which Sidak's adjusted p of c equals the level
        size = either(N, K)
        assert size - a_sidak == c * (1 - c) / (N - 1)
        examples.append({"N": N, "K": K, "level (Sidak's 1 - (1 - K/N)^2)": float(a_sidak), "true size": float(size),
                         "excess": float(size - a_sidak), "Bonferroni size at that level (reject iff 2 K/N <= level)":
                         float(size) if 2 * c <= a_sidak else 0.0})
    # at alpha = 0.01: the worst stratum size N <= 200000
    cs = 1 - math.sqrt(1 - alpha)
    worst = (0.0, None)
    for N in range(2, 200001):
        K = math.floor(cs * N + 1e-12)
        if K < 1:
            continue
        c = K / N
        size = 2 * c - c * c + c * (1 - c) / (N - 1)
        if size - alpha > worst[0]:
            worst = (size - alpha, (N, K))
    # Bonferroni >= Sidak for every p and m (Bernoulli's inequality), on a grid
    ps = np.linspace(0, 1, 10001)
    bern = all(np.all(np.minimum(1, m * ps) >= 1 - (1 - ps) ** m - 1e-15) for m in range(1, 51))
    # B1518's sealed T2 and T3 (two looks each; bar_run.json), under both corrections
    br = json.loads((ROOT / "frontier" / "B1518_the_bar" / "verification" / "bar_run.json").read_text())
    t2 = br["tests"]["T2 AUC under S1 against its permutation null"]["p"]
    t3 = br["tests"]["T3 reversal-closed given S2: conditional permutation"]["p_greater"]
    banked = br["predictions"]["corrected p-values (T2, T3)"]
    rows = {}
    for name, p, b in (("T2", t2, banked[0]), ("T3", t3, banked[1])):
        sid, bon = 1 - (1 - p) ** 2, min(1.0, 2 * p)
        assert abs(sid - b) < 1e-6, (name, sid, b)
        rows[name] = {"p": p, "Sidak (banked)": round(sid, 6), "Bonferroni": round(bon, 6),
                      "decision at 0.01": ["YES" if sid < 0.01 else "NO", "YES" if bon < 0.01 else "NO"]}
    return {"two units of one stratum: exact counterexamples": examples,
            "alpha = 0.01, worst over stratum sizes N <= 200000: (size - alpha, (N, K))": [worst[0], worst[1]],
            "Bonferroni >= Sidak (m <= 50, p on a grid of 10001)": bool(bern),
            "B1518's sealed tests under both corrections": rows,
            "B1518's decisions unchanged": all(r["decision at 0.01"][0] == r["decision at 0.01"][1] for r in rows.values())}


def main():
    t0 = time.time()
    out = {"C1 the finite exchangeable law": c1_finite_law(),
           "C2 THE BAR's r against the exact law": c2_r_is_conservative(),
           "C3 the i.i.d. law": c3_iid_law(),
           "C4 the scan law": c4_scan_law(),
           "C5 several looks": c5_dependence()}
    out["seconds"] = round(time.time() - t0, 1)
    checks = {"C1": out["C1 the finite exchangeable law"]["valid at every level"],
              "C2": out["C2 THE BAR's r against the exact law"]["r >= (k+1)/(n+1) everywhere checked"],
              "C3": all(v["size <= alpha"] for v in out["C3 the i.i.d. law"].values()),
              "C4": all(v["binomial never larger"] for k, v in out["C4 the scan law"].items() if k.isdigit()),
              "C5 counterexample": all(e["excess"] > 0 for e in out["C5 several looks"]["two units of one stratum: exact counterexamples"]),
              "C5 Bonferroni >= Sidak": out["C5 several looks"]["Bonferroni >= Sidak (m <= 50, p on a grid of 10001)"],
              "C5 B1518 unchanged": out["C5 several looks"]["B1518's decisions unchanged"]}
    out["checks"] = checks
    (HERE / "null_contract.json").write_text(json.dumps(out, indent=1, default=str) + "\n")
    print(json.dumps(out, indent=1, default=str))
    print("ALL CHECKS PASS" if all(checks.values()) else "SOME CHECK FAILED")


if __name__ == "__main__":
    main()
