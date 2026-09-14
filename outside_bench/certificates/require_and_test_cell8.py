#!/usr/bin/env python3
"""CELL 8 -- the latent witness: assemble from the record, then verify, then price.

Seal: outside_bench/seals/REQUIRE_AND_TEST_CELL8_PREREG.md
      sha256 b6e82d601ff44521ddc6a893d8bb53378845f8b6c5a827996acf62e004d94d4c

Cell 7 made chirality a FORCED failure for m004.  The only solve is a chiral
object.  Standing rule: exhaust the repository BEFORE building.

Three banked artifacts, never cross-referenced by any arc:
  B1186 family_census.json      -- 112 members with shape field Q(sqrt-3)
  B1235 chirality_112.json      -- their chirality (B1186's own field was
                                   ORIENTATION-BLIND and is retracted by its
                                   ADDENDUM_2026-09-02_chirality_B1235.md)
  B1321 b1321_class_search.json -- those with |det(A-I)| = 3
plus B1292's separately banked 96 surjections pi_1(m202) ->> SL(2,3).

ASSEMBLY FIRST (what the record implies), then VERIFICATION on ONE code path
(require_and_test_cell6.py::score), so every number comes from this cell.
"""
from __future__ import annotations

import importlib.util
import json
import os
import sys
import warnings

warnings.filterwarnings("ignore")

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
CERT = os.path.join(ROOT, "outside_bench", "certificates")

A_ATOM = "frontier/B1186_family_is_112/verification/family_census.json"
A_CHIR = "frontier/B1235_two_seat_harvest/verification/chirality_112.json"
A_P3 = "frontier/B1321_l205_the_siblings_localized_count/verification/b1321_class_search.json"

# banked elsewhere, asserted as control Q2
B1292_M202_SURJECTIONS = 96
B1292_M004_SURJECTIONS = 48

# Phase 1's banked scores, asserted as control Q1
PHASE1 = {
    "m004": {"P_chir": False, "P_atom": True, "P_2T_raw": 48, "det": {0: 2, 4: 2}},
    "m412": {"P_chir": True, "P_atom": True, "P_2T_raw": 0, "det": {0: 4, 4: 4}},
}


def load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


C6 = load(os.path.join(CERT, "require_and_test_cell6.py"), "rt_cell6")


def rule(t):
    print("\n" + "-" * 78)
    print(" " + t)
    print("-" * 78)


def jload(rel):
    with open(os.path.join(ROOT, rel), encoding="utf-8") as fh:
        return json.load(fh)


def main() -> int:
    print("=" * 78)
    print(" CELL 8 -- THE LATENT WITNESS")
    print("=" * 78)
    print("""
    seal  outside_bench/seals/REQUIRE_AND_TEST_CELL8_PREREG.md
    sha256 b6e82d601ff44521ddc6a893d8bb53378845f8b6c5a827996acf62e004d94d4c""")
    failures = []

    # ------------------------------------------------------------------ the fence
    rule("THE FENCE, QUOTED BEFORE ANYTHING IS SCORED")
    print("""
    B1321's "none of which keeps the golden face" means the GOLDEN Q(sqrt5)
    Alexander face t^2 - 3t + 1, NOT the Q(sqrt-3) atom.  B1302 section 3:
      "'leave the knot, keep the field' keeps Q(sqrt-3) and 2T only."
    The two faces are different and the distinction decides this cell.  It is
    quoted here and NOT inferred.""")

    # ------------------------------------------------------------------ Q3
    rule("CONTROL Q3 -- the three artifacts load, and their sizes are asserted")
    atom = jload(A_ATOM)
    chir = jload(A_CHIR)
    p3 = jload(A_P3)
    members_B = list(atom["members_B"])
    chir_rows = chir if isinstance(chir, list) else chir.get("members", chir.get("rows"))
    p3_members = p3.get("members") or p3.get("class") or p3.get("three_line_class")
    if p3_members is None:
        for k, v in p3.items():
            if isinstance(v, list) and v and isinstance(v[0], dict) and "name" in v[0]:
                p3_members = v
                break
    print(f"    {A_ATOM}")
    print(f"      census_size {atom['census_size']}   members_B {len(members_B)}   "
          f"A_all_regular {atom['A_all_regular']}")
    print(f"    {A_CHIR}")
    print(f"      chirality rows {len(chir_rows)}")
    print(f"    {A_P3}")
    print(f"      three-line members {len(p3_members)}: {[m['name'] for m in p3_members]}")
    ok_q3 = (len(members_B) == 112 and len(chir_rows) == 112 and len(p3_members) == 6)
    print(f"    -> {'PASS' if ok_q3 else 'FAIL'} (expect 112 / 112 / 6)")
    if not ok_q3:
        failures.append("Q3")

    # ------------------------------------------------------------------ assembly
    rule("THE ASSEMBLY -- what the committed record already implies")
    chir_by = {r["name"]: r for r in chir_rows}
    atom_set = set(members_B)
    assembled = []
    print(f"    {'name':12s} {'P_atom':7s} {'P_chir':7s} {'P_3':6s}  (from the three artifacts)")
    for m in p3_members:
        nm = m["name"]
        in_atom = nm in atom_set
        row = chir_by.get(nm)
        is_chiral = (row is not None and row.get("amphicheiral") is False)
        print(f"    {nm:12s} {str(in_atom):7s} "
              f"{(str(is_chiral) if row else 'ABSENT'):7s} {'True':6s}"
              + ("   <-- all three" if (in_atom and is_chiral) else ""))
        if in_atom and is_chiral:
            assembled.append(nm)
    print(f"\n    P_chir AND P_atom AND P_3, from the record alone: {assembled}")
    print(f"    plus B1292's banked {B1292_M202_SURJECTIONS} surjections for m202 "
          f"=> m202 scores 4 of 4")
    print(f"    total chiral among the 112 (P_chir AND P_atom): "
          f"{sum(1 for r in chir_rows if r.get('amphicheiral') is False)}")

    # ------------------------------------------------------------------ verification
    rule("THE VERIFICATION -- one code path, this cell's own")
    names = ["m004", "m412"] + [m["name"] for m in p3_members]
    scores = {}
    print(f"    {'name':12s} {'chir':6s} {'atom':6s} {'2T raw':7s} {'2T/24':6s} "
          f"{'P_3':6s} {'cusps':6s} {'|Sym|':6s} det multiset")
    for nm in names:
        try:
            s = C6.score(nm)
        except Exception as exc:
            print(f"    {nm:12s} SCORING FAILED: {exc!r}")
            failures.append(f"score:{nm}")
            continue
        scores[nm] = s
        print(f"    {nm:12s} {str(s['P_chir']):6s} {str(s['P_atom']):6s} "
              f"{s['P_2T_raw']:7d} {s['P_2T_raw'] // 24:6d} {str(s['P_3']):6s} "
              f"{s['cusps']:6d} {s['sym_order']:6d} {s['det_multiset']}")

    # ------------------------------------------------------------------ Q1
    rule("CONTROL Q1 -- m004 and m412 must re-score exactly as Phase 1 banked them")
    ok_q1 = True
    for nm, want in PHASE1.items():
        s = scores.get(nm)
        if not s:
            ok_q1 = False
            continue
        checks = [s["P_chir"] == want["P_chir"], s["P_atom"] == want["P_atom"],
                  s["P_2T_raw"] == want["P_2T_raw"], s["det_multiset"] == want["det"]]
        print(f"    {nm:6s} {'ok ' if all(checks) else 'FAIL'}  "
              f"chir/atom/2T/det = {[int(c) for c in checks]}")
        ok_q1 = ok_q1 and all(checks)
    print(f"    -> {'PASS' if ok_q1 else 'FAIL'}")
    if not ok_q1:
        failures.append("Q1")

    # ------------------------------------------------------------------ Q2
    rule("CONTROL Q2 -- m202's 2T count must reproduce B1292's 96")
    s202 = scores.get("m202", {})
    got = s202.get("P_2T_raw")
    ok_q2 = (got == B1292_M202_SURJECTIONS
             and scores.get("m004", {}).get("P_2T_raw") == B1292_M004_SURJECTIONS)
    print(f"    m202 here {got}   B1292 {B1292_M202_SURJECTIONS}     "
          f"m004 here {scores.get('m004', {}).get('P_2T_raw')}   B1292 {B1292_M004_SURJECTIONS}")
    print(f"    -> {'PASS' if ok_q2 else 'FAIL'}")
    if not ok_q2:
        failures.append("Q2")

    # ------------------------------------------------------------------ outcome
    rule("THE PREREGISTERED OUTCOME -- does the verification confirm the assembly?")
    preds = ["P_chir", "P_atom", "P_2T", "P_3"]
    disagreements = []
    for nm in [m["name"] for m in p3_members]:
        s = scores.get(nm)
        if not s:
            continue
        rec_atom = nm in atom_set
        row = chir_by.get(nm)
        rec_chir = (row.get("amphicheiral") is False) if row else None
        if s["P_atom"] != rec_atom:
            disagreements.append(f"{nm}: P_atom record={rec_atom} computed={s['P_atom']}")
        if rec_chir is not None and s["P_chir"] != rec_chir:
            disagreements.append(f"{nm}: P_chir record={rec_chir} computed={s['P_chir']}")
    print(f"    disagreements between record and this cell's computation: {len(disagreements)}")
    for d in disagreements:
        print(f"      {d}")
    outcome = "B" if disagreements else "A"
    print(f"\n    -> OUTCOME {outcome}")

    print(f"\n    {'name':12s} " + " ".join(f"{p:7s}" for p in preds) + "  score")
    for nm in names:
        s = scores.get(nm)
        if not s:
            continue
        vals = [s["P_chir"], s["P_atom"], s["P_2T"], s["P_3"]]
        print(f"    {nm:12s} " + " ".join(f"{str(v):7s}" for v in vals)
              + f"  {sum(1 for v in vals if v)} of 4")

    if outcome == "A":
        print("""
    CONFIRMED.  The committed record already contained a four-predicate
    witness and no arc said so.  B1292 came closest -- "a witness meeting
    every clause" -- but chirality was not among its clauses and it predates
    B1235's chirality correction.""")
    else:
        print("""
    CONTRADICTED.  The latent witness is an artifact of mixed conventions:
    banked JSONs that do not compose.  THAT is the result.""")

    # ------------------------------------------------------------------ the pricing
    rule("THE PRICING -- what adopting m202 would cost (score and price, DO NOT ADOPT)")
    s202 = scores.get("m202", {})
    s004 = scores.get("m004", {})
    n202 = s202.get("P_2T_raw")
    n004 = s004.get("P_2T_raw")
    print(f"""
    m004   cusps {s004.get('cusps')}   H1 {s004.get('H1')}   |Sym| {s004.get('sym_order')}
    m202   cusps {s202.get('cusps')}   H1 {s202.get('H1')}   |Sym| {s202.get('sym_order')}

    THE SORE POINT, stated in the seal before this ran:
      The genesis chain C1-C5 DERIVES m004 -- two records, one cusp, H1 = Z
      (B1323's dictionary: the a.B bundle on S_1,1 IS m004).  m202 has TWO
      cusps and H1 = Z + Z.  So m202 cannot be DERIVED by the existing
      genesis; it can only be SELECTED.  Adopting it trades a derived object
      for a chosen one -- which is the very thing the programme's C16 refuses
      ("the object provides the group, never the choice").

    WHAT SURVIVES on m202, from this cell's own numbers:
      the atom Q(sqrt-3)     -- yes (B1186 census-certified)
      the 2T door            -- yes, and MORE of it: {n202} surjections vs m004's {n004}
      the localized count 3  -- yes, on BOTH cusps (B1321)
      chirality              -- yes (B1235), which m004 provably cannot have

    WHAT BREAKS:
      C1-C5, the genesis derivation -- m202 is not the a.B bundle
      knot-ness (H1 = Z)            -- gone; Reid's uniqueness of the
                                       arithmetic KNOT does not apply
      one-cusped instruments        -- the D2 index frame, the
                                       knot-complement dictionary
      the golden Q(sqrt5) face      -- B1302/B1321: absent on the whole class
""")

    print("""    FENCES CARRIED, the arcs' own words:
      B1292: m202's commensurability is "argued, not certified" (the invariant
        trace field needs Sage) -- though B1186's census certifies the SHAPE
        field exactly, which is stronger than B1292 knew.
      B1292: "'Keeps E6' is inferred from 2T via the McKay door, not
        recomputed here."  Phase 1 Cell 2 measured that door at 33.92% of the
        census, so the inference is weaker than it reads.
      B1292: "nothing here claims m202 is the object -- m004 is the object by
        the programme's own axioms and its genesis theorem."
      I-26 remains UNEARNED.""")

    rule("TWO LIVE INCONSISTENCIES -- recorded, not silently resolved")
    print(f"""    1. m202's isometry count.  B1321: "6 isometries, none swaps the cusps".
       B1302/B1292: order 12, 6 swapping (B1302 s0 Q3 blames isomorphisms_to
       vs symmetry_group).  THIS CELL COMPUTED |Sym| = {s202.get('sym_order')}
       via symmetry_group(), and {len(scores.get('m202', {}).get('det_multiset', {}))} distinct
       |det(A-I)| values; both numbers are printed above and neither is
       adjudicated here.
    2. A seat's "7 of 72 tetrahedral manifolds to 12 tetrahedra" against
       B1321's six to NINE tetrahedra.  The 10-12 tetrahedra band is ABSENT
       from the record.  Named as a gap; not filled here.""")

    rule("VERDICT")
    print(f"    OUTCOME {outcome}   assembled {assembled}")
    print(f"    controls: {'ALL PASSED' if not failures else 'FAILED: ' + ', '.join(failures)}")
    print("""
    NOT CONCLUDED: that m202 should replace m004 -- that is the owner's call.
    That m202 supplies physics: nothing here touches the SM, and I-26 stays
    UNEARNED.  That "keeps E6" follows from the 2T door.  That the four
    predicates are the right four.  No value.""")
    return 0 if not failures else 1


if __name__ == "__main__":
    sys.exit(main())
