#!/usr/bin/env python3
"""CELL 5 -- fork F9 past its declared depth bound (words of length 3 -> 5).

Seal: outside_bench/seals/REQUIRE_AND_TEST_CELL5_PREREG.md
      sha256 3a8103c71d0429e1b6075f8b3770e365652dbda753d5bcbc818c6f99a18344a2

B1323's FINDINGS section 5 states its own next step and no arc has taken it:
  "that F9's ROBUST extends beyond words of length 3 on the two punctured
   carriers (a longer enumeration or a proof is the next step if anyone wants
   the general statement)"

THE INSTRUMENT IS THE ARC'S OWN, UNMODIFIED (memo 154):
  frontier/B1323_the_genesis_upgrades/verification/u1_substrate_count.py
    :: part_c(maxlen), shape_field, bundle
It is already parameterised by maxlen and already computes F9_surface_verdict.

python-flint (absent in this container) was INSTALLED rather than substituted,
so the arc's code runs unaltered.

CONTROL N4 IS THE LOAD-BEARING ONE: F9's verdict is an ABSENCE, and an absence
computed by a predicate that cannot return True is not evidence (#164).
"""
from __future__ import annotations

import importlib.util
import json
import os
import sys
import time
import warnings

warnings.filterwarnings("ignore")

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ARC = os.path.join(ROOT, "frontier", "B1323_the_genesis_upgrades", "verification",
                   "u1_substrate_count.py")

MAXLEN = 5          # sealed
BASELINE_MAXLEN = 3  # B1323's own bound

# B1323's published depth-3 classes (FINDINGS section 1 table)
B1323_CLASSES = {
    "S_1_2": [("abC", 3.663862, 2, "m129"), ("acB", 5.33349, 2, "s780")],
    "S_0_4": [("aB", 7.327725, 4, "t12047"), ("aaB", 8.929318, 4, "o9_44206")],
}


def rule(t):
    print("\n" + "-" * 78)
    print(" " + t)
    print("-" * 78)


def load_arc():
    spec = importlib.util.spec_from_file_location("u1_substrate_count", ARC)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def summarise(out, label):
    print(f"\n    [{label}]")
    for s in ("S_1_1", "S_1_2", "S_0_4"):
        r = out["results"].get(s)
        if not r:
            continue
        print(f"      {s:7s} words {r['words_tried']:6d}  hyperbolic {r['hyperbolic_bundles']:5d}  "
              f"classes {r['distinct_isometry_classes']:3d}  ({r['seconds']}s)")
    print(f"      VERDICT {out['F9_surface_verdict']}   keepers of Q(sqrt-3): "
          f"{out['keepers_of_Q(sqrt-3)'] if out['keepers_of_Q(sqrt-3)'] else 'NONE'}")


def main() -> int:
    print("=" * 78)
    print(" CELL 5 -- FORK F9 PAST ITS DECLARED DEPTH BOUND")
    print("=" * 78)
    print("""
    seal  outside_bench/seals/REQUIRE_AND_TEST_CELL5_PREREG.md
    sha256 3a8103c71d0429e1b6075f8b3770e365652dbda753d5bcbc818c6f99a18344a2""")
    failures = []

    try:
        import flint
        print(f"\n    python-flint {flint.__version__} present (installed for the arc's shape_field)")
    except Exception as exc:
        print("FATAL: python-flint missing; the arc's own shape_field cannot run:", exc)
        return 2

    arc = load_arc()
    print(f"    instrument: {os.path.relpath(ARC, ROOT)} (unmodified)")

    # ------------------------------------------------------------------ N4
    rule("CONTROL N4 -- can the keeper predicate return True AT ALL?")
    print("""
    F9's verdict is an ABSENCE.  Before reporting one, the predicate
    all_in_Q(sqrt-3) is run on m004's own shapes, which ARE in Q(sqrt-3).
    If it cannot fire there, every ROBUST below is vacuous.
""")
    import snappy
    sf = arc.shape_field(snappy.Manifold("m004"))
    print(f"    m004 shape_field -> {sf}")
    ok_n4 = bool(sf.get("all_in_Q(sqrt-3)"))
    print(f"    -> {'PASS' if ok_n4 else 'FAIL'} (the predicate must be able to return True)")
    if not ok_n4:
        failures.append("N4")

    # ------------------------------------------------------------------ N1/N2
    rule(f"CONTROL N1 / N2 -- reproduce B1323 at its own bound (maxlen {BASELINE_MAXLEN})")
    t0 = time.time()
    base = arc.part_c(BASELINE_MAXLEN)
    summarise(base, f"maxlen {BASELINE_MAXLEN} -- B1323's own bound")
    ok_n1 = base["F9_surface_verdict"] == "ROBUST" and not base["keepers_of_Q(sqrt-3)"]
    for s, expected in B1323_CLASSES.items():
        got = [(c["word"], round(c["volume"], 6), c["cusps"],
                (c["identify"][0].split("(")[0] if c.get("identify") else "?"))
               for c in base["results"][s]["classes"]]
        print(f"      {s}: got {got}")
        print(f"           expected {expected}")
        if len(got) != len(expected):
            ok_n1 = False
            continue
        for g, e in zip(got, expected):
            if g[0] != e[0] or abs(g[1] - e[1]) > 1e-5 or g[2] != e[2] or g[3] != e[3]:
                ok_n1 = False
    s11 = base["results"].get("S_1_1", {}).get("classes", [])
    ok_n2 = bool(s11) and s11[0].get("isometric_to_m004") is True
    print(f"    N1 (B1323's four classes and verdict reproduced) -> {'PASS' if ok_n1 else 'FAIL'}")
    print(f"    N2 (S_1_1 control returns m004) -> {'PASS' if ok_n2 else 'FAIL'}")
    if not ok_n1:
        failures.append("N1")
    if not ok_n2:
        failures.append("N2")

    # ------------------------------------------------------------------ the extension
    rule(f"THE EXTENSION -- maxlen {MAXLEN}")
    t1 = time.time()
    ext = arc.part_c(MAXLEN)
    summarise(ext, f"maxlen {MAXLEN}")
    print(f"    elapsed {time.time() - t1:.0f}s (baseline {t1 - t0:.0f}s)")

    # ------------------------------------------------------------------ N3
    rule("CONTROL N3 -- did the extension actually extend?")
    ok_n3 = True
    for s in ("S_1_2", "S_0_4"):
        b, e = base["results"][s]["words_tried"], ext["results"][s]["words_tried"]
        bc, ec = (base["results"][s]["distinct_isometry_classes"],
                  ext["results"][s]["distinct_isometry_classes"])
        bh, eh = base["results"][s]["hyperbolic_bundles"], ext["results"][s]["hyperbolic_bundles"]
        print(f"    {s:7s} words {b:6d} -> {e:6d}   hyperbolic {bh:5d} -> {eh:5d}   "
              f"classes {bc:3d} -> {ec:3d}")
        if e <= b:
            ok_n3 = False
    print(f"    -> {'PASS' if ok_n3 else 'FAIL'} (population must strictly grow on both carriers)")
    if not ok_n3:
        failures.append("N3")

    # ------------------------------------------------------------------ outcome
    rule("THE PREREGISTERED OUTCOME")
    keepers = ext["keepers_of_Q(sqrt-3)"]
    outcome = "B" if keepers else "A"
    print(f"    F9 surface verdict at maxlen {MAXLEN}: {ext['F9_surface_verdict']}")
    print(f"    keepers of Q(sqrt-3): {keepers if keepers else 'NONE'}")
    print(f"\n    -> OUTCOME {outcome}")
    if outcome == "A":
        gb = sum(base['results'][s]['words_tried'] for s in ('S_1_2', 'S_0_4'))
        ge = sum(ext['results'][s]['words_tried'] for s in ('S_1_2', 'S_0_4'))
        print(f"""    F9 SURVIVES TO LENGTH {MAXLEN}.  No three-record bundle keeps the atom over
    a population {ge / gb:.1f}x larger ({gb} -> {ge} words).  B1323's bound moves
    from 3 to {MAXLEN}.  It is STILL NOT A THEOREM -- B1323's scope line is kept
    with only the number changed.""")
    else:
        print("""    F9 IS FRAGILE.  A three-record carrier KEEPS THE ATOM, and B1323's
    "the atom or the remembered bit, not both" is refuted at depth.""")
        for k in keepers:
            print(f"      keeper: {k}")

    # ------------------------------------------------------------------ what else moved
    rule("WHAT ELSE THE DEEPER ENUMERATION FOUND")
    known = {c[3] for v in B1323_CLASSES.values() for c in v}
    for s in ("S_1_2", "S_0_4"):
        newc = []
        for c in ext["results"][s]["classes"]:
            nm = c["identify"][0].split("(")[0] if c.get("identify") else "?"
            if nm not in known:
                newc.append((c["word"], round(c["volume"], 6), c["cusps"], nm,
                             c.get("amphichiral"), c.get("sym_order")))
        print(f"    {s}: {len(newc)} classes not in B1323's depth-3 table")
        for w, v, cu, nm, am, so in newc[:25]:
            print(f"      {w:6s} vol {v:11.6f}  cusps {cu}  {nm:14s} "
                  f"amphichiral={am}  |Sym|={so}")
        if len(newc) > 25:
            print(f"      ... and {len(newc) - 25} more")

    mt = ext.get("mirror_test", {})
    print(f"\n    mirror test at maxlen {MAXLEN}: three-record classes "
          f"{mt.get('three_record_classes')}, chiral "
          f"{len(mt.get('chiral_classes', []))}, amphichiral "
          f"{len(mt.get('amphichiral_classes', []))}")
    print(f"    members of B1321's three-line class found: "
          f"{ext.get('three_line_class_members') or 'NONE'}")

    out_json = os.path.join(ROOT, "outside_bench", "outputs",
                            "require_and_test_cell5_f9_maxlen5.json")
    with open(out_json, "w") as fh:
        json.dump({"baseline_maxlen": BASELINE_MAXLEN, "maxlen": MAXLEN,
                   "baseline": base, "extended": ext}, fh, indent=1, default=str)
    print(f"\n    artifact: {os.path.relpath(out_json, ROOT)}")

    rule("VERDICT")
    print(f"    OUTCOME {outcome}   F9 at maxlen {MAXLEN} = {ext['F9_surface_verdict']}")
    print(f"    controls: {'ALL PASSED' if not failures else 'FAILED: ' + ', '.join(failures)}")
    print(f"""
    NOT CONCLUDED: that F9 is ROBUST for ALL word lengths, or for carriers
    other than S_1_2 and S_0_4.  B1323's scope line is kept verbatim with only
    the number 3 replaced by {MAXLEN}.  The closed genus-2 carrier stays out of
    frame (A5b).  Nothing about physics.  No value.""")
    return 0 if not failures else 1


if __name__ == "__main__":
    sys.exit(main())
