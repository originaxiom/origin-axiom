#!/usr/bin/env python3
"""CELL 6 -- the first alternative object, scored on the same table.

Seal: outside_bench/seals/REQUIRE_AND_TEST_CELL6_PREREG.md
      sha256 ba82e84adb3c7d3880fc097cb0aa1090b3459c5705606b091f2a7f858df8dd04

Cell 5 produced m412 (= otet05_00001): vol 2.5 x vol(m004), 2 cusps, all five
tetrahedron shapes with minimal polynomial x^2 - x + 1, CHIRAL by both methods.
The first named rival that passes a predicate m004 fails while keeping the atom.

Every predicate is computed with the SAME code path used in cells 1-3, and
m004 is re-scored in this same certificate as control P1.

The COSTS are computed in the same breath as the gains, per the seal.
"""
from __future__ import annotations

import importlib.util
import itertools
import os
import sys
import warnings
from collections import Counter

warnings.filterwarnings("ignore")

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
CERT = os.path.join(ROOT, "outside_bench", "certificates")
ARC1323 = os.path.join(ROOT, "frontier", "B1323_the_genesis_upgrades", "verification",
                       "u1_substrate_count.py")

try:
    import snappy
except Exception as exc:
    print("FATAL: snappy unavailable:", exc)
    sys.exit(2)


def load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


# the SAME code paths as cells 1-3, imported rather than re-implemented
C1 = load(os.path.join(CERT, "require_and_test_cell1.py"), "rt_cell1")
C2 = load(os.path.join(CERT, "require_and_test_cell2.py"), "rt_cell2")
C3 = load(os.path.join(CERT, "require_and_test_cell3.py"), "rt_cell3")
ARC = load(ARC1323, "u1_substrate_count")

# banked m004 values from cells 1-3, asserted by control P1
M004_BANKED = {"P_chir_amphichiral": True, "P_2T_raw": 48,
               "P_det_multiset": {0: 2, 4: 2}, "P_atom": True}


def rule(t):
    print("\n" + "-" * 78)
    print(" " + t)
    print("-" * 78)


def score(name):
    M = snappy.Manifold(name)
    amph = C1.amphichiral_det(M)            # cell 1's orientation-aware test
    try:
        naive = bool(M.symmetry_group().is_amphicheiral())
    except Exception:
        naive = None
    G = M.fundamental_group()
    raw = C2.surjection_count(G.generators(), G.relators())   # cell 2's enumeration
    vals, rej = C3.cusp_counts(M)                             # cell 3's counter
    sf = ARC.shape_field(M)                                   # B1323's own shape field
    return {
        "name": name, "vol": float(M.volume()), "cusps": M.num_cusps(),
        "H1": str(M.homology()), "sym_order": M.symmetry_group().order(),
        "amphichiral_det": amph, "is_amphicheiral": naive,
        "P_chir": (amph is False),
        "P_atom": bool(sf.get("all_in_Q(sqrt-3)")), "shape_field": sf,
        "P_2T_raw": raw, "P_2T": raw > 0,
        "det_multiset": dict(sorted(Counter(vals).items())) if vals else {},
        "P_3": bool(vals and 3 in vals), "rejected_or_rows": rej,
        "gens": len(G.generators()),
    }


def main() -> int:
    print("=" * 78)
    print(" CELL 6 -- THE FIRST ALTERNATIVE OBJECT, SCORED ON THE SAME TABLE")
    print("=" * 78)
    print("""
    seal  outside_bench/seals/REQUIRE_AND_TEST_CELL6_PREREG.md
    sha256 ba82e84adb3c7d3880fc097cb0aa1090b3459c5705606b091f2a7f858df8dd04""")
    failures = []

    rule("CONTROL P2 -- a negative control INSIDE this cell, not inherited")
    M = snappy.Manifold("5_2")
    G = M.fundamental_group()
    r52 = C2.surjection_count(G.generators(), G.relators())
    print(f"    5_2 raw 2T surjections = {r52}   (B282: 0)")
    ok_p2 = (r52 == 0)
    print(f"    -> {'PASS' if ok_p2 else 'FAIL'}")
    if not ok_p2:
        failures.append("P2")

    rule("THE SCORES")
    rows = [score("m004"), score("m412")]
    for r in rows:
        print(f"\n    {r['name']}  vol {r['vol']:.6f}  cusps {r['cusps']}  H1 {r['H1']}  "
              f"|Sym| {r['sym_order']}  gens {r['gens']}")
        print(f"      P_chir (no orientation-reversing self-isometry) : "
              f"{r['P_chir']}   (amphichiral_det={r['amphichiral_det']}, "
              f"is_amphicheiral={r['is_amphicheiral']})")
        print(f"      P_atom (shape field in Q(sqrt-3))               : {r['P_atom']}   "
              f"min_polys {r['shape_field'].get('min_polys')}")
        print(f"      P_2T   (surjects onto SL(2,F_3))                : {r['P_2T']}   "
              f"raw {r['P_2T_raw']}  /24 = {r['P_2T_raw'] // 24}")
        print(f"      P_3    (|det(A-I)| = 3 somewhere)               : {r['P_3']}   "
              f"multiset {r['det_multiset']}")

    m004, m412 = rows

    # ------------------------------------------------------------------ P1
    rule("CONTROL P1 -- m004 re-scored here must match cells 1-3")
    checks = [
        ("amphichiral", m004["amphichiral_det"] is M004_BANKED["P_chir_amphichiral"]),
        ("2T raw = 48", m004["P_2T_raw"] == M004_BANKED["P_2T_raw"]),
        ("det multiset {0:2, 4:2}", m004["det_multiset"] == M004_BANKED["P_det_multiset"]),
        ("shape field Q(sqrt-3)", m004["P_atom"] is M004_BANKED["P_atom"]),
    ]
    for label, ok in checks:
        print(f"    [{'ok ' if ok else 'FAIL'}] {label}")
    ok_p1 = all(ok for _, ok in checks)
    print(f"    -> {'PASS' if ok_p1 else 'FAIL'}")
    if not ok_p1:
        failures.append("P1")

    # ------------------------------------------------------------------ P3
    rule("CONTROL P3 -- m412's chirality by BOTH methods, agreeing")
    agree = (m412["amphichiral_det"] is False) and (m412["is_amphicheiral"] is False)
    print(f"    amphichiral_det = {m412['amphichiral_det']}   "
          f"is_amphicheiral = {m412['is_amphicheiral']}")
    print(f"    -> {'PASS' if agree else 'FAIL'} (both must read CHIRAL)")
    if not agree:
        failures.append("P3")

    # ------------------------------------------------------------------ P4
    rule("CONTROL P4 -- the commensurability question, ANSWERED not skipped")
    ratio = m412["vol"] / m004["vol"]
    print(f"    vol(m412)/vol(m004) = {ratio:.10f}")
    print(f"    integer? {abs(ratio - round(ratio)) < 1e-9}  -> m412 is "
          f"{'a possible cover of' if abs(ratio - round(ratio)) < 1e-9 else 'NOT a cover of'} m004")
    same_shape_poly = (m412["shape_field"]["min_polys"] and
                       all(p == [1, -1, 1] for p in m412["shape_field"]["min_polys"]))
    print(f"    every m412 tetrahedron shape has min poly x^2-x+1 (the regular ideal "
          f"tetrahedron, m004's own): {same_shape_poly}")
    print(f"    m004 shapes: {m004['shape_field'].get('min_polys')}")
    print("""
    READING, and it is a COST not a gain: both are tiled by REGULAR IDEAL
    TETRAHEDRA, so both are arithmetic over Q(sqrt-3) and COMMENSURABLE.  By
    frontier/B803_commensurability_audit -- "any derivation routing through it
    is class-level not the object's specific" -- m412's arithmetic face is
    INHERITED from the class, not independent evidence for m412.  What is NOT
    inherited is chirality: it is not a commensurability invariant, and that is
    exactly the predicate on which the two objects differ.""")

    # ------------------------------------------------------------------ outcome
    rule("THE PREREGISTERED OUTCOME")
    preds = ["P_chir", "P_atom", "P_2T", "P_3"]
    print(f"    {'predicate':10s} {'m004':>8s} {'m412':>8s}")
    for p in preds:
        print(f"    {p:10s} {str(m004[p]):>8s} {str(m412[p]):>8s}")
    gains = [p for p in preds if m412[p] and not m004[p]]
    losses = [p for p in preds if m004[p] and not m412[p]]
    dominates = bool(gains) and not losses
    outcome = "A" if dominates else "B"
    print(f"\n    m412 GAINS : {gains if gains else 'none'}")
    print(f"    m412 LOSES : {losses if losses else 'none'}")
    print(f"    -> OUTCOME {outcome}")
    if outcome == "A":
        print("""    m412 STRICTLY DOMINATES m004 on these four predicates.  For the first
    time the programme has a NAMED RIVAL that is better on its own stated
    requirements -- and the costs below are the price to be argued about.""")
    else:
        print("""    m412 does NOT strictly dominate: it gains and it loses.  The fork is a
    trade like every other trade in the record.""")

    rule("THE COSTS -- fixed in the seal BEFORE the gains were seen")
    print(f"    cusps            m004 {m004['cusps']}   m412 {m412['cusps']}")
    print("      the chain's C4/A1 carrier story and every one-cusped instrument")
    print("      (the D2 index frame, the knot-complement dictionary) assume ONE cusp")
    print(f"    H1               m004 {m004['H1']}   m412 {m412['H1']}")
    print("      m412 is NOT a knot complement, so Reid's uniqueness of the")
    print("      arithmetic KNOT does not apply to it")
    print("    arithmetic face  INHERITED from the commensurability class (P4), not")
    print("      independent evidence for m412")

    rule("VERDICT")
    print(f"    OUTCOME {outcome}   gains {gains}   losses {losses}")
    print(f"    controls: {'ALL PASSED' if not failures else 'FAILED: ' + ', '.join(failures)}")
    print("""
    NOT CONCLUDED: that m412 should replace m004 -- that is the owner's call
    and a whole chain's worth of work, not a four-predicate score.  That m412
    supplies physics: nothing here touches the SM.  That these are the right
    four predicates: they are the four this programme has base rates for.""")
    return 0 if not failures else 1


if __name__ == "__main__":
    sys.exit(main())
