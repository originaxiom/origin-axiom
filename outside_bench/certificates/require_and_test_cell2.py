#!/usr/bin/env python3
"""CELL 2 -- requirement 1 (the gauge algebra): the base rate of the 2T door.

Seal: outside_bench/seals/REQUIRE_AND_TEST_CELL2_PREREG.md
      sha256 67166376af6112d57b601b0aa0cfe9978ce57e634e9eea852af5be2ad21b4dcd

P_2T = pi_1(M) surjects onto 2T = SL(2,F_3).  Chain link C6, "the sole source
of the McKay E6" (B266).  B282 computed it for SIX knots.  Its base rate over a
census has NEVER been measured -- which is the price of the row
frontier/B1028_freedom_ledger/ADDENDUM_2026-08-12.md has carried as UNPRICED
since 2026-08-12.

THE INSTRUMENT IS NOT THE RECORD'S.  B282 uses Sage + GAP; neither is installed
in this container.  |SL(2,F_3)| = 24, so homomorphisms are enumerated directly.
Validated against B282's six published knots BEFORE any census manifold is
touched -- the four ZEROS as load-bearing as the two hits.

THE CONFOUND.  If P_2T merely tracks arithmeticity then a tiny rate re-measures
Reid's theorem rather than pricing the family choice.  Discriminated against
B1186's already-banked 112 / 212641 (the Q(sqrt-3) shape-field family).

SnapPy 3.3.2.  Pure Python otherwise.
"""
from __future__ import annotations

import itertools
import json
import os
import sys
import time
import warnings

warnings.filterwarnings("ignore")

try:
    import snappy
except Exception as exc:  # pragma: no cover
    print("FATAL: snappy unavailable:", exc)
    sys.exit(2)

POPULATION = 5000          # sealed
MAX_GENS = 4               # sealed: above this the enumeration is SKIPPED, never scored 0
B1186_JSON = "frontier/B1186_family_is_112/verification/family_census.json"

# B282's published values (GAP GQuotients, i.e. quotients up to Aut(SL(2,3)))
B282 = {"4_1": 2, "m003": 2, "5_2": 0, "6_1": 0, "6_2": 0, "7_4": 0}


# ----------------------------------------------------------------- SL(2,F_3)
def sl23():
    els = []
    for a, b, c, d in itertools.product(range(3), repeat=4):
        if (a * d - b * c) % 3 == 1:
            els.append((a, b, c, d))
    return els


ELS = sl23()
I2 = (1, 0, 0, 1)


def mul(x, y):
    return ((x[0] * y[0] + x[1] * y[2]) % 3, (x[0] * y[1] + x[1] * y[3]) % 3,
            (x[2] * y[0] + x[3] * y[2]) % 3, (x[2] * y[1] + x[3] * y[3]) % 3)


def inv(x):
    a, b, c, d = x
    return (d % 3, (-b) % 3, (-c) % 3, a % 3)


def generates(seed):
    S = {I2}
    frontier = [I2]
    while frontier:
        g = frontier.pop()
        for s in seed:
            for h in (mul(g, s), mul(g, inv(s))):
                if h not in S:
                    S.add(h)
                    frontier.append(h)
    return len(S) == 24


def surjection_count(gens, rels):
    """Number of SURJECTIVE homomorphisms pi_1 -> SL(2,F_3), by enumeration."""
    n = len(gens)
    idx = {g: i for i, g in enumerate(gens)}
    cnt = 0
    for assign in itertools.product(ELS, repeat=n):
        ok = True
        for r in rels:
            acc = I2
            for ch in r:
                g = assign[idx[ch.lower()]]
                acc = mul(acc, g if ch.islower() else inv(g))
            if acc != I2:
                ok = False
                break
        if ok and generates(assign):
            cnt += 1
    return cnt


def rule(t):
    print("\n" + "-" * 78)
    print(" " + t)
    print("-" * 78)


def main() -> int:
    print("=" * 78)
    print(" CELL 2 -- THE BASE RATE OF THE 2T DOOR")
    print("=" * 78)
    print("""
    seal  outside_bench/seals/REQUIRE_AND_TEST_CELL2_PREREG.md
    sha256 67166376af6112d57b601b0aa0cfe9978ce57e634e9eea852af5be2ad21b4dcd""")
    failures = []

    # -------------------------------------------------------------- K1 + K2
    rule("CONTROL K1/K2 -- the instrument against B282's six published knots")
    print("    |SL(2,F_3)| = %d ; |Aut(SL(2,3))| = |S_4| = 24\n" % len(ELS))
    ok = True
    for name, expect in B282.items():
        M = snappy.Manifold(name)
        G = M.fundamental_group()
        raw = surjection_count(G.generators(), G.relators())
        quot = raw // 24 if raw else 0
        exact = (raw % 24 == 0)
        good = (quot == expect)
        print(f"    {name:5s} raw surjections = {raw:4d}   /24 = {quot:2d}   "
              f"B282 = {expect}   {'ok' if good else 'MISMATCH'}"
              + ("" if exact else "   (NOT divisible by 24!)"))
        if not good or not exact:
            ok = False
    print(f"    -> {'PASS' if ok else 'FAIL'}  (two hits AND four zeros must both reproduce)")
    if not ok:
        failures.append("K1/K2")

    # -------------------------------------------------------------- the sweep
    rule(f"THE SWEEP -- one-cusped OrientableCuspedCensus, population {POPULATION}")
    census = snappy.OrientableCuspedCensus
    t0 = time.time()
    scanned = 0
    skipped_gens = 0
    errors = 0
    hits = []
    gen_hist = {}
    strata = {}   # K6: B282's six knots are ALL H1 = Z; stratify to rule out the confound
    for M in census:
        if scanned + skipped_gens + errors >= POPULATION:
            break
        try:
            if M.num_cusps() != 1:
                continue
            G = M.fundamental_group()
            gens, rels = G.generators(), G.relators()
        except Exception:
            errors += 1
            continue
        gen_hist[len(gens)] = gen_hist.get(len(gens), 0) + 1
        if len(gens) > MAX_GENS:
            skipped_gens += 1
            continue
        try:
            raw = surjection_count(gens, rels)
        except Exception:
            errors += 1
            continue
        scanned += 1
        try:
            key = "H1 = Z (knot-like: B282's own population)" if str(M.homology()) == "Z" \
                  else "H1 with torsion"
        except Exception:
            key = "H1 unavailable"
        sl = strata.setdefault(key, [0, 0])
        sl[0] += 1
        if raw:
            sl[1] += 1
            hits.append((M.name(), raw, raw // 24, float(M.volume())))
        if scanned % 1000 == 0:
            print(f"    scanned {scanned}  hits {len(hits)}  ({time.time() - t0:.0f}s)")

    print(f"\n    POPULATION SCANNED (printed before any rate): {scanned}")
    assert scanned > 0, "empty population -- the B1197 vacuity trap"
    print(f"    skipped, >{MAX_GENS} generators (counted as skipped, NOT as zero): {skipped_gens}")
    print(f"    errors: {errors}")
    print(f"    generator-count histogram: {dict(sorted(gen_hist.items()))}")
    print(f"    elapsed: {time.time() - t0:.0f}s")

    rate = len(hits) / scanned
    print(f"\n    P_2T HOLDS FOR {len(hits)} of {scanned}  =  {100 * rate:.4f} %")
    for nm, raw, q, vol in hits[:40]:
        print(f"      {nm:12s} raw {raw:4d}  /24 = {q:3d}  vol {vol:.6f}")
    if len(hits) > 40:
        print(f"      ... and {len(hits) - 40} more")

    # -------------------------------------------------------------- K3
    rule("CONTROL K3 -- a positive control other than m004/m003")
    others = [h for h in hits if h[0] not in ("m003", "m004")]
    if others:
        print(f"    {len(others)} census manifolds other than m004/m003 carry the door, e.g.:")
        for nm, raw, q, vol in others[:5]:
            print(f"      {nm:12s} /24 = {q}")
        print("    -> PASS (the null is not an instrument failure)")
    else:
        print("    NO manifold other than m004/m003 carries the door in this population.")
        print("    -> REPORTED AS A POSSIBLE INSTRUMENT FAILURE, NOT AS A FINDING (#164).")
        failures.append("K3")

    # -------------------------------------------------------------- K6
    rule("CONTROL K6 -- B282's six knots are ALL H1 = Z.  Stratify.")
    print("""
    If the door were common only among manifolds UNLIKE B282's sample, the
    sweep would have measured a different population rather than corrected
    B282.  This control asks the rate inside B282's own stratum.
""")
    for k in sorted(strata):
        tot, hit = strata[k]
        print(f"    {k:42s} population {tot:5d}   hits {hit:5d}   "
              f"= {100 * hit / tot if tot else 0:7.3f} %")
    kz = strata.get("H1 = Z (knot-like: B282's own population)", [0, 0])
    if kz[0] and (kz[1] / kz[0]) >= 0.01:
        print("    -> the door is COMMON inside B282's own stratum: the six-knot")
        print("       sample was unrepresentative, not a different population.")
    elif kz[0]:
        print("    -> the door is RARE inside B282's stratum: the sweep measured a")
        print("       DIFFERENT population and the headline must be restricted.")
    else:
        print("    -> stratum empty; no conclusion.")

    # -------------------------------------------------------------- outcome
    rule("THE PREREGISTERED OUTCOME")
    outcome = "A" if rate < 0.01 else "B"
    print(f"    rate {100 * rate:.4f} %  ->  OUTCOME {outcome}")
    print("    A = the door is RARE (<1%): requirement 1 does real selecting work.")
    print("    B = the door is COMMON (>=1%): B282's genericity collapse extends to")
    print("        the McKay door itself, and C6 selects less than the chain reads.")

    # -------------------------------------------------------------- the confound
    rule("THE CONFOUND -- is P_2T just arithmeticity restated?")
    members = None
    try:
        with open(B1186_JSON) as fh:
            d = json.load(fh)
        members = set(d["members_B"])
        print(f"    B1186, cited to file: census_size = {d['census_size']}, "
              f"Q(sqrt-3) shape field = {d['B_shape_field_in_Qsqrt3']}  "
              f"({100 * d['B_shape_field_in_Qsqrt3'] / d['census_size']:.4f} %)")
    except Exception as exc:
        print(f"    could not read {B1186_JSON}: {exc}")

    if members is not None:
        hit_names = {h[0] for h in hits}
        both = hit_names & members
        only2T = hit_names - members
        print(f"\n    of the {len(hits)} P_2T hits in the swept range:")
        print(f"      also in B1186's Q(sqrt-3) family : {len(both)}  {sorted(both)[:12]}")
        print(f"      NOT in it                        : {len(only2T)}  {sorted(only2T)[:12]}")
        if len(hits):
            if len(only2T) == 0:
                print("    -> D = SAME : within the swept range every 2T manifold is a")
                print("       Q(sqrt-3) manifold.  P_2T IS ARITHMETICITY RESTATED here;")
                print("       this cell has re-measured Reid, and says so.")
            else:
                print("    -> D = DIFFERENT : the populations diverge.  P_2T is its own")
                print("       predicate, and the divergence is the finding.")
        print("    (comparison over the SWEPT RANGE only; never extrapolated to 212641)")

    rule("VERDICT")
    print(f"    OUTCOME = {outcome}   scanned {scanned}   hits {len(hits)}")
    print(f"    controls: {'ALL PASSED' if not failures else 'FAILED: ' + ', '.join(failures)}")
    return 0 if not failures else 1


if __name__ == "__main__":
    sys.exit(main())
