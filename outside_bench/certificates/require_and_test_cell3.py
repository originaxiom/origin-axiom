#!/usr/bin/env python3
"""CELL 3 -- requirement 1 (matter): the count of three, and the distribution.

Seal: outside_bench/seals/REQUIRE_AND_TEST_CELL3_PREREG.md
      sha256 81021b9ed3527292a77f7d7cd896cfccfaab802d0777ef056b3abbe6476ee434

P_3 = the object has an orientation-preserving cusp-fixing isometry with
|det(A - I)| = 3 -- the Pantev-Wijnholt localized count, in the frame B1321
uses: "in PW's frame the localized count on a fixed cusp is the fixed-point
count of the rotation."

B1321 asked WHICH manifolds have 3 (six of 61911, two-cusped, <= 9 tets).  It
did not ask the DISTRIBUTION.  This cell does, because "m004 counts 2" is only
information against how many objects count what.

Instrument reused: frontier/B1321_.../verification/b1321_class_search.py ::
cusp_rows -- re-implemented here with the orientation check ASSERTED rather
than assumed (control L3).

SnapPy 3.3.2.
"""
from __future__ import annotations

import sys
import time
import warnings
from collections import Counter

warnings.filterwarnings("ignore")

try:
    import snappy
except Exception as exc:  # pragma: no cover
    print("FATAL: snappy unavailable:", exc)
    sys.exit(2)

POPULATION = 4000   # sealed


def rule(t):
    print("\n" + "-" * 78)
    print(" " + t)
    print("-" * 78)


def cusp_counts(N):
    """(multiset of |det(A-I)| over ORIENTATION-PRESERVING cusp-fixing isometries,
    number of orientation-reversing rows rejected).  Returns (None, None) if the
    isometry group is unavailable -- the caller counts that as SKIPPED, not 0."""
    try:
        isos = N.isomorphisms_to(N)
    except Exception:
        return None, None
    vals, rejected = [], 0
    for iso in isos:
        try:
            imgs, mats = iso.cusp_images(), iso.cusp_maps()
        except Exception:
            continue
        for c, (img, A) in enumerate(zip(imgs, mats)):
            if img != c:
                continue
            a, b, cc, d = int(A[0, 0]), int(A[0, 1]), int(A[1, 0]), int(A[1, 1])
            det = a * d - b * cc
            if det != 1:            # L3: orientation-preserving ASSERTED
                rejected += 1
                continue
            vals.append(abs((a - 1) * (d - 1) - b * cc))
    return vals, rejected


def main() -> int:
    print("=" * 78)
    print(" CELL 3 -- REQUIREMENT 1 (MATTER): THE COUNT OF THREE")
    print("=" * 78)
    print("""
    seal  outside_bench/seals/REQUIRE_AND_TEST_CELL3_PREREG.md
    sha256 81021b9ed3527292a77f7d7cd896cfccfaab802d0777ef056b3abbe6476ee434""")
    failures = []

    # ------------------------------------------------------------------ L1/L2
    rule("CONTROLS L1 / L2 -- the object, and a witness the instrument must see")
    print("""
    L1 AS FIRST SEALED WAS MIS-SPECIFIED (seal ADDENDUM 1).  It demanded a 2 in
    the |det(A-I)| frame, importing a number that lives in the OTHER frame the
    record uses.  The two counts:
      |det(A-I)|          the cusp fixed-point count (PW's localized count)
                          on m004: {0, 4}  -- MAIN_GOAL.md quoting B1295 as a
                          banked NEGATIVE, "|det(A-I)| in {0: 882, 4: 494}"
                          over all 87 covers to degree 10
      chi(Fix g) = 1-s_mu the Euler characteristic of the fixed locus in the
                          3-manifold; on m004: {0, 2}  -- MAIN_GOAL.md l.87
    "The object counts 2 at every fixed locus" is the SECOND.  B1321's 3, and
    requirement 1's three generations, are the FIRST.  TOE_REQUIREMENTS_LEDGER
    section C row 2 carries the sentence with no frame attached.
    chi is NOT swept: it is stated in the record FOR m004, and generalising it
    would repeat the same paraphrase error one level down.
""")
    for nm, want in (("m004", 4), ("m202", 3)):
        M = snappy.Manifold(nm)
        vals, rej = cusp_counts(M)
        ms = Counter(vals) if vals is not None else None
        print(f"    {nm:5s} cusps={M.num_cusps()}  multiset of |det(A-I)| = "
              f"{dict(sorted(ms.items())) if ms else 'UNAVAILABLE'}   "
              f"max={max(vals) if vals else '-'}   "
              f"orientation-reversing rows rejected: {rej}")
        ok = bool(vals) and want in vals
        src = ("B1295's banked values {0, 4}" if nm == "m004" else "B1321's own witness")
        print(f"      -> {'PASS' if ok else 'FAIL'} (must contain {want}; source: {src})")
        if not ok:
            failures.append(f"L{1 if nm == 'm004' else 2}")

    # ------------------------------------------------------------------ sweep
    rule(f"THE SWEEP -- OrientableCuspedCensus, all cusp numbers, population {POPULATION}")
    t0 = time.time()
    scanned = skipped = 0
    rejected_total = 0
    maxdist = Counter()
    anydist = Counter()
    has3 = []
    for M in snappy.OrientableCuspedCensus:
        if scanned + skipped >= POPULATION:
            break
        vals, rej = cusp_counts(M)
        if vals is None:
            skipped += 1
            continue
        scanned += 1
        rejected_total += rej
        mx = max(vals) if vals else 0
        maxdist[mx] += 1
        for v in set(vals):
            anydist[v] += 1
        if 3 in vals:
            has3.append((M.name(), M.num_cusps(), float(M.volume())))
        if scanned % 1000 == 0:
            print(f"    scanned {scanned}  with a 3: {len(has3)}  ({time.time() - t0:.0f}s)")

    print(f"\n    POPULATION SCANNED (printed before any rate): {scanned}")
    assert scanned > 0, "empty population -- the B1197 vacuity trap"
    print(f"    SKIPPED, isometry group unavailable (NOT counted as 0): {skipped}")
    print(f"    L3: orientation-REVERSING cusp-fixing rows rejected: {rejected_total}")
    print(f"    elapsed: {time.time() - t0:.0f}s")

    # ------------------------------------------------------------------ results
    rule("THE DISTRIBUTION -- the second question, sealed in advance")
    print("    maximum |det(A-I)| attained, per manifold:")
    for v in sorted(maxdist):
        n = maxdist[v]
        print(f"      max = {v:3d} : {n:5d}   {100 * n / scanned:6.2f} %")
    print("\n    manifolds attaining each value SOMEWHERE (not exclusive):")
    for v in sorted(anydist):
        n = anydist[v]
        print(f"      value {v:3d} : {n:5d}   {100 * n / scanned:6.2f} %")

    r3 = len(has3) / scanned
    rule("P_3 -- THE PREREGISTERED OUTCOME")
    print(f"    P_3 holds for {len(has3)} of {scanned}  =  {100 * r3:.4f} %")
    for nm, nc, vol in has3[:20]:
        print(f"      {nm:12s} cusps {nc}  vol {vol:.6f}")
    if len(has3) > 20:
        print(f"      ... and {len(has3) - 20} more")
    outcome = "A" if r3 < 0.01 else "B"
    print(f"\n    -> OUTCOME {outcome}")
    print("    A = the 3 is RARE (<1%): 'three generations' does real selecting work.")
    print("    B = the 3 is COMMON (>=1%): it selects little, as Cell 2 found for 2T.")

    rule("IS 2 DISTINGUISHED, OR MERELY MODAL?")
    modal = max(anydist, key=lambda k: anydist[k]) if anydist else None
    n2 = anydist.get(2, 0)
    print(f"    modal attained value : {modal}  ({anydist[modal]} of {scanned} = "
          f"{100 * anydist[modal] / scanned:.2f} %)" if modal is not None else "    no values")
    print(f"    manifolds attaining 2: {n2} of {scanned} = {100 * n2 / scanned:.2f} %")
    if modal == 2:
        print("    -> 2 IS THE MODAL VALUE.  'The object counts 2 at every fixed locus'")
        print("       is then a statement about tori, not a distinguishing fact about m004.")
    else:
        print(f"    -> 2 is NOT modal (modal is {modal}); m004's 2 is not the default.")

    rule("VERDICT")
    print(f"    OUTCOME = {outcome}   P_3 rate {100 * r3:.4f} %   scanned {scanned}")
    print(f"    controls: {'ALL PASSED' if not failures else 'FAILED: ' + ', '.join(failures)}")
    print("""
    NOT CONCLUDED: nothing about generations as physics.  h1 <-> 4d generations
    is I-26, a DECLARED INPUT (TOE_REQUIREMENTS_LEDGER section E row 4, "the
    dimension gap not exhibited").  This is a fixed-point count on a torus.""")
    return 0 if not failures else 1


if __name__ == "__main__":
    sys.exit(main())
