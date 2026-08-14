#!/usr/bin/env python3
"""Draw a REPRODUCIBLE random audit sample of authored verdicts.

Why this exists
---------------
Wave 1 audited the first three arcs of each reader's slice and got 36/36 correct. That number is
uninformative and the reason is structural, not statistical: the first arcs of a slice are the ones
a reader judged while freshest, and -- worse -- anyone choosing which arcs to audit AFTER seeing the
verdicts can land on an agreeable set without meaning to. A 100% pass rate on a set selected that
way is compatible with a substantial error rate on the rest.

This draws instead by a rule fixed in advance:

    sort the eligible arc ids lexically, seed the RNG with a committed constant, sample without
    replacement.

Given the same seed and the same eligible set, the draw is identical for anyone who runs it. Given
a DIFFERENT eligible set (verdicts that landed differently), the draw changes -- which is the point:
the sample tracks the data, not the auditor's preferences.

Committed BEFORE the verdicts it will audit exist. That ordering is what makes the sample honest;
the code itself is nearly trivial.
"""
import argparse
import json
import os
import random
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
SEED = 20260730          # committed constant -- changing it after seeing verdicts voids the audit
DEFAULT_N = 30


def eligible(frontier=None, require_verdict=True):
    """Arc dirs carrying an arc_verdict.json, sorted -- the sampling frame, stated explicitly."""
    frontier = frontier or os.path.join(ROOT, "frontier")
    out = []
    for d in sorted(os.listdir(frontier)):
        p = os.path.join(frontier, d, "arc_verdict.json")
        if os.path.isfile(p):
            out.append(d)
        elif not require_verdict and os.path.isdir(os.path.join(frontier, d)):
            out.append(d)
    return out


def draw(frame, n=DEFAULT_N, seed=SEED):
    """Sample without replacement from a SORTED frame under a fixed seed."""
    frame = sorted(frame)
    if n >= len(frame):
        return list(frame)
    return sorted(random.Random(seed).sample(frame, n))


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("-n", type=int, default=DEFAULT_N)
    ap.add_argument("--seed", type=int, default=SEED)
    ap.add_argument("--only", help="restrict the frame to ids listed in this JSON array "
                                   "(e.g. the arcs a given wave authored)")
    ap.add_argument("--json", action="store_true", help="emit the sample as JSON only")
    args = ap.parse_args()

    frame = eligible()
    if args.only:
        keep = set(json.load(open(args.only, encoding="utf-8")))
        frame = [d for d in frame if d in keep or d.split("_")[0] in keep]

    sample = draw(frame, args.n, args.seed)

    if args.json:
        print(json.dumps(sample, indent=1))
        return 0

    print("=" * 78)
    print("Reproducible random audit sample")
    print("=" * 78)
    print(f"\n  sampling frame : {len(frame)} arcs carrying an authored verdict")
    print(f"  seed           : {args.seed}  (committed constant -- changing it after seeing "
          f"verdicts voids the audit)")
    print(f"  drawn          : {len(sample)}")
    if args.seed != SEED:
        print(f"\n  WARNING: seed differs from the committed constant {SEED}. This draw is NOT the")
        print(f"  pre-registered one and must not be reported as the audit sample.")
    print()
    for i, d in enumerate(sample, 1):
        print(f"    {i:>3}. {d}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
