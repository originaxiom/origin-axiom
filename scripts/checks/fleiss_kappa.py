#!/usr/bin/env python3
"""Fleiss' kappa -- inter-rater agreement for MANY raters on the SAME items.

Why this exists
---------------
Wave 1 fanned 300 arcs across 12 readers on DISJOINT slices, and the per-slice PROVED-rate
spanned 0.364 -> 0.917. That spread mixes two causes -- genuine differences between eras, and
reader-to-reader labelling bias -- and the design COULD NOT SEPARATE THEM. Wave 1's kappa = 0.842
was Cohen's, on 20 items with 2 raters; it says nothing about the other ten.

Wave 2 gives every reader the SAME calibration block, which makes the confound measurable rather
than merely admitted. Cohen's kappa handles exactly two raters. Fleiss' handles many, and that is
the whole reason for this file.

The measurement is of THE INSTRUMENT (do readers agree?), not of the object. Nothing here reaches
CLAIMS.md.

Self-test
---------
`--self-test` reproduces Fleiss' published worked example (10 subjects, 14 raters, 5 categories,
kappa = 0.210) before the instrument is trusted on our own data. An agreement statistic that has
never been checked against a known answer is not evidence.
"""
import argparse
import json
import math
import os
import random
import sys
from collections import Counter

# The canonical worked example (Fleiss 1971; the standard reference table), subject x category
# counts, with its PUBLISHED answer. If this does not reproduce, the instrument is wrong and no
# number it emits about our own data means anything.
REFERENCE_TABLE = [
    [0, 0, 0, 0, 14],
    [0, 2, 6, 4, 2],
    [0, 0, 3, 5, 6],
    [0, 3, 9, 2, 0],
    [2, 2, 8, 1, 1],
    [7, 7, 0, 0, 0],
    [3, 2, 6, 3, 0],
    [2, 5, 3, 2, 2],
    [6, 5, 2, 1, 0],
    [0, 2, 2, 3, 7],
]
REFERENCE_KAPPA = 0.210


def fleiss_kappa(table):
    """kappa from an items x categories COUNT table.

    Every item must carry the same number of ratings -- that is a hypothesis of the statistic,
    not a detail. A ragged table is rejected rather than silently averaged over, because the
    quantity it would produce is not Fleiss' kappa and would be reported as if it were.
    """
    if not table:
        raise ValueError("empty table -- nothing to measure")
    totals = [sum(row) for row in table]
    n = totals[0]
    if any(t != n for t in totals):
        bad = [i for i, t in enumerate(totals) if t != n]
        raise ValueError(
            f"ragged table: every item needs the same number of ratings (expected {n}); "
            f"items {bad[:5]} differ. Fleiss' kappa is not defined here -- fix the design or "
            f"restrict to the fully-rated items, but do not average over the gap."
        )
    if n < 2:
        raise ValueError("fewer than 2 ratings per item -- agreement is undefined")

    N = len(table)
    # P_i: observed pairwise agreement within item i
    P = [(sum(c * c for c in row) - n) / (n * (n - 1)) for row in table]
    P_bar = sum(P) / N
    # p_j: marginal share of category j across all ratings
    grand = N * n
    p = [sum(row[j] for row in table) / grand for j in range(len(table[0]))]
    P_e = sum(v * v for v in p)

    if abs(1 - P_e) < 1e-12:
        # Everyone used one category. Agreement is total AND expected -- kappa is 0/0.
        raise ValueError(
            "P_e = 1: every rating fell in a single category, so chance agreement is total and "
            "kappa is undefined (0/0). Report the degenerate margin, not a kappa."
        )
    return (P_bar - P_e) / (1 - P_e), P_bar, P_e, p, P


def bootstrap_ci(table, reps=2000, seed=20260730, alpha=0.05):
    """Percentile CI by resampling ITEMS (the unit the design randomised over).

    A kappa on 15 items is a small-sample estimate and a gate applied to the point estimate alone
    would be a knife-edge. The interval is reported so the gate decision is made in view of it.
    """
    rng = random.Random(seed)
    N = len(table)
    out = []
    for _ in range(reps):
        samp = [table[rng.randrange(N)] for _ in range(N)]
        try:
            out.append(fleiss_kappa(samp)[0])
        except ValueError:
            continue  # degenerate resample (all one category); excluded and counted below
    out.sort()
    if len(out) < reps // 2:
        return None, None, len(out)
    lo = out[int(alpha / 2 * len(out))]
    hi = out[int((1 - alpha / 2) * len(out)) - 1]
    return lo, hi, len(out)


def table_from_ratings(ratings, categories=None):
    """ratings: {item_id: {rater_id: label}} -> (count table, category list, item order)."""
    items = sorted(ratings)
    if categories is None:
        categories = sorted({v for r in ratings.values() for v in r.values()})
    idx = {c: i for i, c in enumerate(categories)}
    table = []
    for it in items:
        row = [0] * len(categories)
        for lab in ratings[it].values():
            if lab not in idx:
                raise ValueError(f"item {it}: label {lab!r} is outside the declared vocabulary "
                                 f"{categories} -- a reader used a value the gate does not know")
            row[idx[lab]] += 1
        table.append(row)
    return table, categories, items


def per_rater_distribution(ratings):
    """Each rater's verdict mix on the SAME items -- this is the conservatism offset itself.

    Wave 1 could only observe that slices differed. On an identical block, a rater who returns
    PROVED twice as often as another is showing bias, not a different era.
    """
    per = {}
    for it, rs in ratings.items():
        for rater, lab in rs.items():
            per.setdefault(rater, Counter())[lab] += 1
    return per


def self_test(verbose=True):
    k, P_bar, P_e, p, _ = fleiss_kappa(REFERENCE_TABLE)
    ok = abs(k - REFERENCE_KAPPA) < 0.001
    if verbose:
        print("  self-test against Fleiss' published worked example")
        print(f"    10 subjects x 14 raters x 5 categories")
        print(f"    P_bar = {P_bar:.4f}   P_e = {P_e:.4f}")
        print(f"    kappa = {k:.4f}   published = {REFERENCE_KAPPA}   "
              f"{'MATCH' if ok else 'MISMATCH -- DO NOT TRUST THIS INSTRUMENT'}")
    return ok


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("ratings", nargs="?",
                    help='JSON: {"item": {"rater": "LABEL", ...}, ...}')
    ap.add_argument("--self-test", action="store_true")
    ap.add_argument("--gate", type=float, default=0.75,
                    help="the sealed bar; below it, verdicts are HELD, not written")
    ap.add_argument("--categories", help="comma-separated vocabulary (else inferred)")
    args = ap.parse_args()

    print("=" * 78)
    print("Fleiss' kappa -- inter-rater agreement on a shared calibration block")
    print("=" * 78)

    if not self_test():
        print("\n  ABORT: the instrument fails its own reference case.")
        return 2
    if args.self_test or not args.ratings:
        if not args.ratings:
            print("\n  (no ratings file given -- self-test only)")
        return 0

    ratings = json.load(open(args.ratings, encoding="utf-8"))
    cats = args.categories.split(",") if args.categories else None
    table, categories, items = table_from_ratings(ratings, cats)
    n_raters = sum(table[0])

    k, P_bar, P_e, p, P = fleiss_kappa(table)
    lo, hi, reps = bootstrap_ci(table)

    print(f"\n  items {len(items)}   raters per item {n_raters}   categories {categories}")
    print(f"  P_bar (observed) = {P_bar:.4f}    P_e (chance) = {P_e:.4f}")
    print(f"  marginal shares  = " + "  ".join(f"{c}={v:.3f}" for c, v in zip(categories, p)))
    print(f"\n  FLEISS' KAPPA = {k:.4f}")
    if lo is not None:
        print(f"  bootstrap 95% CI over items = [{lo:.4f}, {hi:.4f}]  ({reps} usable resamples)")

    print(f"\n  per-rater verdict mix on the IDENTICAL block (the conservatism offset):")
    per = per_rater_distribution(ratings)
    for rater in sorted(per):
        c = per[rater]
        tot = sum(c.values())
        print(f"    {rater:24} " + "  ".join(f"{lab}={c[lab]}" for lab in categories)
              + f"   (n={tot})")

    print(f"\n  hardest items (lowest within-item agreement):")
    for i in sorted(range(len(items)), key=lambda i: P[i])[:5]:
        mix = {categories[j]: table[i][j] for j in range(len(categories)) if table[i][j]}
        print(f"    {items[i]:24} P_i={P[i]:.3f}   {mix}")

    passed = k >= args.gate
    print(f"\n  SEALED GATE: kappa >= {args.gate}")
    print(f"  VERDICT: {'PASS -- wave 2 verdicts may be WRITTEN' if passed else 'FAIL -- wave 2 verdicts are HELD, not written'}")
    if not passed:
        print(f"  The verdicts are not discarded; they are unwritten pending a vocabulary fix.")
        print(f"  A disagreeing panel writing 413 verdicts would bake its disagreement into the")
        print(f"  ledger as if it were knowledge.")
    return 0 if passed else 1


if __name__ == "__main__":
    sys.exit(main())
