"""B1518 -- the null-model instrument behind THE BAR: what a positive on a generated state is measured against.

Given a population (rows with covariates; one row per word state, each carrying its manifold key) and a hit set (the states
some frame reports as hits), this computes, for a stated unit (word states or manifolds):
  - the base rate, with an exact (Clopper-Pearson) 95% interval;
  - the rate in each stratum of chosen covariates, and whether the hit is constant inside every stratum (determinism);
  - an association between a binary feature and the hit, conditioned on strata: the Mantel-Haenszel odds ratio and an
    exact conditional permutation p-value (the feature is permuted inside each stratum, never across);
  - the leave-one-out stratum-rate score of each unit and its AUC (how much of the hit the covariates predict), with a
    permutation p-value for 'beyond chance';
  - the trials-corrected (Sidak) significance of a claimed positive.
Pure functions; it reads no frame's outcome by itself. Controls in `selftest()` run it on planted data in both
directions before any real population is read.
"""
import math
import random
from collections import defaultdict

from scipy.stats import beta, rankdata


def clopper_pearson(k, n, conf=0.95):
    a = (1 - conf) / 2
    lo = 0.0 if k == 0 else float(beta.ppf(a, k, n - k + 1))
    hi = 1.0 if k == n else float(beta.ppf(1 - a, k + 1, n - k))
    return lo, hi


def units(rows, hits, unit="manifold"):
    """Collapse to the unit. For manifolds, a unit is hit when its states are hit; a split unit (one state hit, its
    partner not) is reported, since a manifold-level frame cannot split one."""
    if unit == "word":
        return [dict(r, hit=r["state"] in hits) for r in rows], []
    groups = defaultdict(list)
    for r in rows:
        groups[r["manifold"]].append(r)
    out, split = [], []
    for key, rs in sorted(groups.items()):
        hs = {r["state"] in hits for r in rs}
        if len(hs) > 1:
            split.append(key)
        u = dict(rs[0])
        u["hit"] = any(r["state"] in hits for r in rs)
        u["n_states"] = len(rs)
        out.append(u)
    return out, split


def base_rate(us):
    k, n = sum(u["hit"] for u in us), len(us)
    lo, hi = clopper_pearson(k, n)
    return {"hits": k, "units": n, "rate": k / n if n else float("nan"), "ci95": [round(lo, 4), round(hi, 4)]}


def strata(us, keys):
    s = defaultdict(list)
    for u in us:
        s[tuple(u[k] for k in keys)].append(u)
    return s


def determinism(us, keys):
    """Strata in which the hit is not constant; a hit determined by `keys` leaves none."""
    s = strata(us, keys)
    mixed = {k: (sum(u["hit"] for u in v), len(v)) for k, v in s.items() if 0 < sum(u["hit"] for u in v) < len(v)}
    return {"strata": len(s), "mixed_strata": len(mixed), "units_in_mixed": sum(n for _, n in mixed.values()),
            "mixed_examples": sorted(mixed.items(), key=lambda kv: -kv[1][1])[:8]}


def loo_scores(us, keys):
    """Score each unit by the hit rate of its stratum with the unit left out. A unit alone in its stratum carries no
    information and gets one constant, the population's rate K/n (the same for every such unit, so it leaks nothing)."""
    s = strata(us, keys)
    K, N = sum(u["hit"] for u in us), len(us)
    scores = []
    for u in us:
        v = s[tuple(u[k] for k in keys)]
        k, n = sum(x["hit"] for x in v) - u["hit"], len(v) - 1
        scores.append((k / n) if n else K / N)
    return scores


def loo_auc(us, keys):
    return auc(loo_scores(us, keys), [u["hit"] for u in us])


def auc(scores, labels):
    """AUC by average ranks (Mann-Whitney); ties count one half."""
    pos = sum(1 for l in labels if l)
    neg = len(labels) - pos
    if not pos or not neg:
        return float("nan")
    r = rankdata(scores)
    return (sum(ri for ri, l in zip(r, labels) if l) - pos * (pos + 1) / 2) / (pos * neg)


def auc_pairwise(scores, labels):
    """The definition, pair by pair; used only to check `auc`."""
    pos = [s for s, l in zip(scores, labels) if l]
    neg = [s for s, l in zip(scores, labels) if not l]
    wins = 0.0
    for p in pos:
        for q in neg:
            wins += 1.0 if p > q else (0.5 if p == q else 0.0)
    return wins / (len(pos) * len(neg))


def auc_permutation(us, keys, n_perm=2000, seed=12345):
    """Does the stratum of `keys` predict the hit beyond chance? The hit labels are permuted across all units and the
    leave-one-out AUC recomputed; p = (1 + #{null >= observed}) / (1 + n_perm)."""
    rng = random.Random(seed)
    obs = loo_auc(us, keys)
    labels = [u["hit"] for u in us]
    null = []
    for _ in range(n_perm):
        perm = labels[:]
        rng.shuffle(perm)
        vs = [dict(u, hit=h) for u, h in zip(us, perm)]
        null.append(loo_auc(vs, keys))
    null.sort()
    return {"auc": round(obs, 4), "null_median": round(null[len(null) // 2], 4),
            "null_q99": round(null[int(0.99 * len(null))], 4),
            "p": (1 + sum(1 for x in null if x >= obs)) / (1 + len(null))}


def mantel_haenszel(us, feature, keys):
    """Common odds ratio of hit for feature vs not, over strata of `keys` (strata with both feature values only)."""
    num = den = 0.0
    used = 0
    for v in strata(us, keys).values():
        a = sum(1 for u in v if u[feature] and u["hit"])
        b = sum(1 for u in v if u[feature] and not u["hit"])
        c = sum(1 for u in v if not u[feature] and u["hit"])
        d = sum(1 for u in v if not u[feature] and not u["hit"])
        n = a + b + c + d
        if (a + b) and (c + d):
            num += a * d / n
            den += b * c / n
            used += 1
    return {"odds_ratio": (num / den) if den else float("inf"), "strata_used": used}


def conditional_permutation(us, feature, keys, n_perm=20000, seed=12345):
    """Exact-in-distribution p-value for 'feature units are hit more often', permuting the feature inside each stratum
    of `keys`. Statistic: number of hit units carrying the feature. Two-sided p from the permutation distribution."""
    rng = random.Random(seed)
    s = list(strata(us, keys).values())
    obs = sum(1 for u in us if u[feature] and u["hit"])
    blocks = [([u["hit"] for u in v], sum(1 for u in v if u[feature])) for v in s]
    null = []
    for _ in range(n_perm):
        t = 0
        for hits, m in blocks:
            if m:
                t += sum(rng.sample(hits, m))
        null.append(t)
    mean = sum(null) / len(null)
    p_hi = (1 + sum(1 for x in null if x >= obs)) / (1 + len(null))
    p_lo = (1 + sum(1 for x in null if x <= obs)) / (1 + len(null))
    return {"observed": obs, "null_mean": round(mean, 3), "p_greater": p_hi, "p_two_sided": min(1.0, 2 * min(p_hi, p_lo))}


def sidak(p_local, trials):
    """Global significance of the best of `trials` independent looks."""
    return 1 - (1 - p_local) ** trials


def selftest():
    """Planted controls in both directions."""
    rng = random.Random(7)
    rows = []
    for i in range(400):
        g = i % 8
        f = rng.random() < 0.5
        rows.append({"state": f"s{i}", "manifold": f"m{i // 2}", "g": g, "f": f})
    # (1) a hit determined by g: determinism finds no mixed stratum; AUC is 1; f shows no conditional effect
    hits = {r["state"] for r in rows if r["g"] in (1, 5)}
    us, split = units(rows, hits, "word")
    ok1 = determinism(us, ["g"])["mixed_strata"] == 0 and abs(loo_auc(us, ["g"]) - 1.0) < 1e-12
    p1 = conditional_permutation(us, "f", ["g"], n_perm=2000)["p_two_sided"]
    # (2) a hit planted on f inside every g: the conditional test must find it
    hits2 = {r["state"] for r in rows if r["f"] and rng.random() < 0.6} | {r["state"] for r in rows if not r["f"] and rng.random() < 0.1}
    us2, _ = units(rows, hits2, "word")
    p2 = conditional_permutation(us2, "f", ["g"], n_perm=2000)["p_greater"]
    or2 = mantel_haenszel(us2, "f", ["g"])["odds_ratio"]
    # (3) the manifold collapse reports a split unit
    us3, split3 = units(rows, {"s0"}, "manifold")
    # (4) Clopper-Pearson against a known value and Sidak against its formula
    lo, hi = clopper_pearson(0, 10)
    # (5) the rank AUC equals the pair-by-pair definition, ties included
    sc = [rng.choice([0.0, 0.25, 0.5, 1.0]) for _ in range(300)]
    lb = [rng.random() < 0.3 for _ in range(300)]
    # (6) the AUC permutation test: finds a planted stratum effect, and finds none where the hit ignores the stratum
    hits6 = {r["state"] for r in rows if (r["g"] in (1, 5) and rng.random() < 0.7) or rng.random() < 0.1}
    us6, _ = units(rows, hits6, "word")
    p6 = auc_permutation(us6, ["g"], n_perm=300)["p"]
    hits7 = {r["state"] for r in rows if rng.random() < 0.25}
    us7, _ = units(rows, hits7, "word")
    p7 = auc_permutation(us7, ["g"], n_perm=300)["p"]
    # (7) a unit alone in its stratum gets the population rate, the same constant for hit and non-hit units
    lone = [{"state": "a", "manifold": "a", "g": 0, "hit": True}, {"state": "b", "manifold": "b", "g": 1, "hit": False},
            {"state": "c", "manifold": "c", "g": 2, "hit": False}, {"state": "d", "manifold": "d", "g": 2, "hit": True}]
    ls = loo_scores(lone, ["g"])
    checks = {"determinism and AUC on a planted invariant": ok1,
              "no conditional effect where none was planted": p1 > 0.05,
              "the planted conditional effect is found": p2 < 0.001 and or2 > 3,
              "a split manifold is reported": split3 == ["m0"],
              "exact interval for 0 of 10": abs(hi - (1 - 0.025 ** 0.1)) < 1e-9 and lo == 0.0,
              "Sidak": abs(sidak(0.01, 5) - (1 - 0.99 ** 5)) < 1e-15,
              "rank AUC equals the pairwise definition": abs(auc(sc, lb) - auc_pairwise(sc, lb)) < 1e-12,
              "AUC permutation finds a planted stratum effect": p6 < 0.01,
              "AUC permutation finds none where none was planted": p7 > 0.05,
              "a lone unit gets the population rate, hit or not": ls[0] == ls[1] == 0.5 and ls[2] == 1.0 and ls[3] == 0.0}
    return checks


if __name__ == "__main__":
    c = selftest()
    for k, v in c.items():
        print(f"  [{'PASS' if v else 'FAIL'}] {k}")
    print("CONTROLS PASS" if all(c.values()) else "CONTROLS FAIL")
