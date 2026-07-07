#!/usr/bin/env python3
"""B452 — the EZ dry run: prove the two typed gates can FIRE and FAIL (the launch gate).

Synthetic object catalog + 200 synthetic null catalogs. Demonstrates:
  EZ-1 fires on a planted rare signature; fails on a common one.
  EZ-2 fires on planted 1-sigma-matching numerics beating the 2000-draw null; fails on random.
  The structural joint statistic counts but cannot fire alone.

Run: python3 ez_dryrun.py   (prints ALL GATES VALIDATED)
"""
import numpy as np

from registry import (NUMERIC_TARGETS, ez1_specificity, ez2_correspondence, signature,
                      structural_joint)

rng = np.random.default_rng(7)


def random_catalog():
    """a null organism's catalog: common behaviors with generic signatures."""
    cat = []
    for _ in range(rng.integers(4, 9)):
        kind = rng.choice(["pulse", "field", "orbit"])
        ints = tuple(sorted(rng.integers(1, 20, size=rng.integers(1, 3)).tolist()))
        discs = tuple(sorted((-rng.integers(1, 30, size=1)).tolist()))
        cat.append(signature(kind, ints, discs))
    # one very common signature shared by ~half the population
    if rng.random() < 0.5:
        cat.append(signature("pulse", (2,), (-3,)))
    return cat


def run():
    ok = True
    nulls = [random_catalog() for _ in range(200)]

    # ---- EZ-1 ----
    planted_rare = signature("orbit", (4,), (-7,), ())
    common = signature("pulse", (2,), (-3,))
    obj = [planted_rare, common]
    r1 = ez1_specificity(obj, nulls, licensed=True)
    fire = r1[planted_rare]["fires"]
    fail = not r1[common]["fires"]
    ok &= fire and fail
    print(f"EZ-1: planted rare fires={fire} (p1={r1[planted_rare]['p1']:.3f}); "
          f"common fails={fail} (p1={r1[common]['p1']:.3f})")

    # ---- EZ-2: planted match-set (5 exact SM values as signature values) ----
    planted_vals = [c for _, c, _ in NUMERIC_TARGETS[:5]]
    obj_hit = [signature("resonance", (), (), planted_vals)]
    r2 = ez2_correspondence(obj_hit)
    ok &= r2["fires"]
    print(f"EZ-2 planted: hits={r2['hits']} null_mean={r2['null_mean']:.2f} "
          f"null_p99={r2['null_p99']:.0f} p={r2['p']:.4f} fires={r2['fires']}")

    # ---- EZ-2: random numerics must FAIL ----
    obj_rand = [signature("resonance", (), (), np.exp(rng.uniform(np.log(1e-3), 0, 6)).tolist())]
    r3 = ez2_correspondence(obj_rand)
    ok &= not r3["fires"]
    print(f"EZ-2 random: hits={r3['hits']} p={r3['p']:.3f} fires={r3['fires']} (must be False)")

    # ---- structural: counts, cannot fire alone ----
    s = structural_joint([signature("count", (3,), ()), signature("dims", (8, 3, 1), ())], nulls)
    ok &= (s["satisfied"] >= 1) and (s["can_fire_alone"] is False)
    print(f"structural: satisfied={s['satisfied']} can_fire_alone={s['can_fire_alone']}")

    print("ALL GATES VALIDATED" if ok else "GATE VALIDATION FAILURE")
    return bool(ok)


if __name__ == "__main__":
    run()
