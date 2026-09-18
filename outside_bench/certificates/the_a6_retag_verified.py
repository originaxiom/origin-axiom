#!/usr/bin/env python3
"""THE A6 RETAG, VERIFIED -- every sentence of memo 235's ADDENDA 1 and 2 checked
against the file it names, at a NAMED REF, by exact string containment.

The owner's standing instruction: ALWAYS VERIFY.  ADDENDUM 1 was written from
quotations and ADDENDUM 2 had to be written against it the same session, so the
addenda are exactly the kind of artifact whose claims must be re-derived from the
sources rather than re-read from the memo.

METHOD.  Every claim below is a (ref, path, needle) triple.  The needle is a
VERBATIM substring of the source; containment is tested after normalising only
whitespace runs, never characters.  A claim that is not found is a FAIL, not a
warning.

CONTROLS THAT CAN FAIL (memo 164 -- a control that cannot fail is not a control):
  C1  a needle this bench INVENTED must come back ABSENT from the same file.
  C2  a true needle looked up in the WRONG file must come back ABSENT.
  C3  the arc-number diff (#39's subject) must be reproduced and must NOT be
      read as a content claim: main's file count for B1350-B1359 is reported
      alongside a CONTENT grep for the same arcs' load-bearing strings.
"""
import re
import subprocess
import sys

SM = "origin/claude/standard-model-derivation-0qt6ao"
MAIN = "origin/main"
HERE = "origin/claude/outside-bench"


def show(ref, path):
    p = subprocess.run(["git", "show", f"{ref}:{path}"], capture_output=True, text=True)
    return p.stdout if p.returncode == 0 else None


def norm(s):
    return re.sub(r"\s+", " ", s)


CACHE = {}


def body(ref, path):
    if (ref, path) not in CACHE:
        t = show(ref, path)
        CACHE[(ref, path)] = None if t is None else norm(t)
    return CACHE[(ref, path)]


CLAIMS = []


def claim(tag, ref, path, needle, why):
    CLAIMS.append((tag, ref, path, needle, why))


B1357 = "frontier/B1357_the_objects_own_joyce_orbifold/FINDINGS.md"
B1358 = "frontier/B1358_the_e6_apex_family/FINDINGS.md"
B1359 = "frontier/B1359_the_k3_alternative/FINDINGS.md"
B1356 = "frontier/B1356_the_three_on_y3/FINDINGS.md"
B1415 = "frontier/B1415_the_sm_seats_closing_arcs_harvested/FINDINGS.md"
B1416 = "frontier/B1416_the_relay_residue_closed/FINDINGS.md"
B1414 = "frontier/B1414_the_outside_benchs_memos_185_233_harvested/FINDINGS.md"

# ---- ADDENDUM 1: A6 is COMPUTED, and it FAILS in the flat class ------------
claim("A1-1", SM, B1357,
      "a compact flat G₂ orbifold — a Joyce orbifold T⁷/Γ with the object's groups in Γ — with exactly one invariant spinor",
      "the compact flat G2 orbifold exists and has N = 1")
claim("A1-2", SM, B1357,
      "b₂ = 0: the flat background carries no C-field U(1) at all",
      "b_2 = 0 for the flat background")
claim("A1-3", SM, B1357,
      "left (a b₂ ≥ 2 with the deck acting irreducibly) is decided in the flat class: the irreducible occurs only on 3-forms",
      "A6 stated in this bench's own words and decided")
claim("A1-4", SM, B1357,
      "After that resolution: cover b₂ = 2, b₃ = 10; descent (parameter along the Z₃ axis) b₂ = 2, b₃ = 4",
      "A6's FIRST clause is satisfied after the Joyce resolution")
claim("A1-5", SM, B1357,
      "So the deck's irreducible occurs on four of the cover's ten 3-forms and on no",
      "A6's SECOND clause fails -- the deck acts trivially on H^2")
claim("A1-6", SM, B1357,
      "(ℝ³)^{V₄} = 0, so the E₆, SO(8) and SU(2) loci are rigid",
      "why only the T^3 locus contributes to b_2")
claim("A1-7", SM, B1357,
      "it must be born with the curved apexes",
      "the location where A6 can still be met")
claim("A1-8", SM, B1358,
      "b₂(CP³/Γ; ℚ) = 1 throughout",
      "the LOCAL class at an apex (never A6's compact b_2 -- the R147 distinction)")
claim("A1-9", SM, B1358,
      "the three 27s told apart by the apexes' own U(1)s in sum-zero combination",
      "the sum-zero mechanism, B1356's, carried through the apex family")
claim("A1-10", SM, B1359,
      "the three-generation design of B1356–B1358 lives on the Hurwitz torus and nowhere else",
      "B1359 pins the ambient: the residue is narrower, not smaller")

# ---- ADDENDUM 2: the relay is VOID ----------------------------------------
claim("A2-1", MAIN, B1415,
      "ten scripts re-run green and log-identical",
      "main HARVESTED sm:B1356-B1365 -- the relay 'main needs it' is void")
claim("A2-2", MAIN, B1415,
      "**Verdict:** VERIFIED (ten arcs: the seat's grades stand; nothing raised, nothing lowered without a computation)",
      "main's verdict on those ten arcs")
claim("A2-3", MAIN, B1415,
      "**Date:** 2026-09-16",
      "the harvest predates this memo by two days")
claim("A2-4", MAIN, B1416,
      "eleven were already on main under other arc numbers",
      "#39: main harvests under its OWN arc numbers, so a name diff is not a content diff")
claim("A2-5", MAIN, B1415,
      "sm:B1358's mixed-loci ADE typing",
      "main's bookkeeping BACK to the seat: argued steps to state as argued")

# ---- ADDENDUM 2: the independence claim, corrected -------------------------
claim("A2-6", MAIN, B1414,
      "memo 233's forced escape clause re-derived and its v1 vacuity confirmed",
      "main harvested memo 233 -- so 'neither cites the other' had to be withdrawn")
claim("A2-7", MAIN, B1414,
      "**V-CROSS fails on this bench only on its volume tolerance**",
      "main's re-run of the bench's own certificate, reported against the bench")
claim("A2-8", SM, B1356,
      "*(Currency 2026-09-16, main's B1414 \u00a74: memo 233's v2 re-derived on main's own code",
      "sm:B1356's CURRENCY NOTE cites B1414 s4 by name -- the link that voids 'neither cites'")
claim("A2-8b", SM, B1356,
      "`frontier/B1414_the_outside_benchs_memos_185_233_harvested` on main",
      "and by directory, so the citation is not a coincidence of the three digits")

# ---- ADDENDUM 2: A6 is NOT the last obstruction ----------------------------
claim("A2-9", MAIN, B1415,
      "every tree-level charged-fermion mass matrix is complex symmetric with zero diagonal",
      "sm:B1361's mechanism")
claim("A2-10", MAIN, B1415,
      "σ₁ = σ₂ + σ₃ exactly, refuted in every charged sector",
      "sm:B1361 NEGATIVE -- a computed negative independent of compactness")
claim("A2-11", MAIN, B1415,
      "the three-apex design is excluded",
      "sm:B1365 -- the design is excluded AS IT STANDS")
claim("A2-12", MAIN, B1415,
      "the Majorana mass is forbidden",
      "the ground of that exclusion: no seesaw")
claim("A2-13", MAIN, B1415,
      "a DESIGN with a computed obstruction (no seesaw) — no theorem, no prediction",
      "main's own status line, adopted verbatim by the memo")
claim("A2-14", MAIN, B1415,
      "registered on main as **L220** and **L221**",
      "the remedy (a 27-bar sector) is REGISTERED, not run")
claim("A2-15", MAIN, B1415,
      "the deck must be broken",
      "sm:B1362 -- the deck-symmetric Yukawa cannot carry a hierarchy")

# ---- ADDENDUM 3: the OTHER generation mechanism, verified on main today ----
B1427 = "frontier/B1427_the_towers_generation_count_verified/FINDINGS.md"
claim("A3-1", MAIN, B1427,
      "one chiral generation per background on 80 800 backgrounds, never two, never three",
      "the tower's count, verified on main with independent code")
claim("A3-2", MAIN, B1427,
      "count of three is not this mechanism's** on any level up to seven",
      "the tower does not supply three -- main's own words")
claim("A3-3", MAIN, B1427,
      "there is **no physics reading, no value, and no three**",
      "the fence main keeps on it")
claim("A3-4", MAIN, B1427,
      "The same code returns **h\u00b9 = 2** at the three order-2 characters of the Whitehead link complement m129",
      "vacuity guarded UPWARD: the code CAN return 2")
claim("A3-5", MAIN, B1427,
      "the same index code returns **|I| = 2** on t12835",
      "vacuity guarded on the INDEX too: |I| = 1 is a measurement")
claim("A3-6", MAIN, B1427,
      "The completeness gap, found here:",
      "main found a real gap in the lane's scan and says so")
claim("A3-7", MAIN, B1427,
      "\"h\u00b9(\u03c7\u00b2) = 1 bounds |I| \u2264 1\" is not a proof as stated",
      "and narrowed the lane's own statement")
claim("A3-8", MAIN, B1427,
      "cc, 2026-09-18.",
      "dated TODAY -- newer than ADDENDUM 1 and 2 both")

# ---- the memo itself carries the corrections (a correction in one place ----
#      is not a correction) ---------------------------------------------------
MEMO = "outside_bench/memos/THE_ASSUMPTION_LEDGER.md"
INDEX = "outside_bench/INDEX.md"
REG = "outside_bench/THE_OWNER_REGISTER.md"
claim("P-1", HERE, MEMO, "PARTLY SUPERSEDED BY ADDENDUM 2", "ADDENDUM 1 s4 marked superseded IN PLACE")
claim("P-2", HERE, MEMO, "ITS RELAY IS VOID", "ADDENDUM 1 s7 marked superseded IN PLACE")
claim("P-3", HERE, MEMO, "SUPERSEDED BY ADDENDUM 1", "the original A6 tag marked superseded IN PLACE")
claim("P-4", HERE, INDEX, "A6 IS NOT THE LAST OBSTRUCTION AND NEVER WAS", "INDEX row 235 carries the correction")
claim("P-5", HERE, REG, "A6 IS NOT THE LAST OBSTRUCTION AND NEVER WAS", "register row R153 carries it")
claim("P-6", HERE, REG, "| R153 |", "the owner's question got its row the same session")

# ---- CONTROLS --------------------------------------------------------------
CONTROLS = [
    ("C1", SM, B1357,
     "the compact curved closing is hereby constructed",
     "an INVENTED needle must come back ABSENT"),
    ("C2", SM, B1359,
     "b₂ = 0: the flat background carries no C-field U(1) at all",
     "a TRUE needle in the WRONG file must come back ABSENT"),
]


def run():
    print("=" * 78)
    print(" THE A6 RETAG, VERIFIED -- every claim re-derived from its source")
    print("=" * 78)
    for nm, ref in (("SM head", SM), ("main", MAIN), ("this branch", HERE)):
        sha = subprocess.run(["git", "rev-parse", "--short", ref],
                             capture_output=True, text=True).stdout.strip()
        print(f"  {nm:12s} {ref} = {sha}")
    print()

    bad = []
    for tag, ref, path, needle, why in CLAIMS:
        t = body(ref, path)
        if t is None:
            ok, note = False, "FILE ABSENT AT REF"
        else:
            ok, note = (norm(needle) in t), ""
        print(f"  [{'PASS' if ok else 'FAIL'}] {tag:6s} {path.split('/')[1][:34]:34s} {why}")
        if not ok:
            bad.append((tag, path, needle, note))

    print()
    print("-" * 78)
    print(" CONTROLS -- each MUST report ABSENT")
    print("-" * 78)
    cbad = []
    for tag, ref, path, needle, why in CONTROLS:
        t = body(ref, path) or ""
        absent = norm(needle) not in t
        print(f"  [{'PASS' if absent else 'FAIL'}] {tag}  {why}")
        if not absent:
            cbad.append(tag)

    # C3 -- the #39 subject, reproduced: names against content
    print()
    print("-" * 78)
    print(" C3 -- #39 REPRODUCED: the arc-NAME count against a CONTENT grep")
    print("-" * 78)
    names = subprocess.run(
        ["git", "ls-tree", "-r", "--name-only", MAIN, "--", "frontier"],
        capture_output=True, text=True).stdout
    n_dirs = len({m for m in re.findall(r"frontier/(B135\d[^/]*)/", names)})
    print(f"  files on main under frontier/B1350-B1359/ : {n_dirs}")
    content = body(MAIN, B1415)
    hits = [s for s in ("sm:B1357", "sm:B1358", "sm:B1359", "sm:B1361", "sm:B1365")
            if content and s in content]
    print(f"  those arcs' CONTENT on main, inside B1415  : {len(hits)}/5 present  {hits}")
    c3 = (n_dirs == 0 and len(hits) == 5)
    print(f"  [{'PASS' if c3 else 'FAIL'}] C3  zero directories AND full content -- "
          f"a name diff is NOT a content diff")
    if not c3:
        cbad.append("C3")

    print()
    print("=" * 78)
    print(f" {len(CLAIMS) - len(bad)}/{len(CLAIMS)} claims verified; "
          f"{3 - len(cbad)}/3 controls PASS")
    if bad:
        print(" FAILED CLAIMS:")
        for tag, path, needle, note in bad:
            print(f"   {tag} {path} {note}\n     needle: {needle[:90]}")
    print("=" * 78)
    print(" WHAT THIS DOES NOT VERIFY: that the mathematics of B1356-B1359 is correct.")
    print(" It verifies that the memo says what its sources say. Main's own re-runs")
    print(" (B1415: ten scripts green and log-identical) are the check on the")
    print(" mathematics, and they are MAIN's, not this bench's.")
    print(" I-26 UNEARNED. No value. Gate 5 untouched.")
    return 1 if (bad or cbad) else 0


if __name__ == "__main__":
    sys.exit(run())
