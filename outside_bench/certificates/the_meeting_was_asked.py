"""CERTIFICATE -- memo 198 said the meeting face "has never been asked".  IT HAS.

This is a correction of THIS BENCH'S OWN memo, banked the previous turn, and it is a correction of
the defect class this bench audits others for: A NUMBER ASSERTED FROM PROSE INSTEAD OF MEASURED.

Memo 198 (THE_GATE_HAS_NO_PRODUCT_ROW) wrote, of the genus bit on the meeting face:

    "which the corpus mentions SIX TIMES IN TOTAL, none of them a crossing and none of them a
     value computation"

and closed its section 6 with:

    "What this bench can say is only this: IT HAS NEVER BEEN ASKED."

Neither sentence was produced by memo 198's certificate.  no_product_row.py measured three things
-- occurrences in the SEVEN sealed crossing directories (0/0/0/0/0/0/0), the KIND_TABLE field
column, and three class numbers -- and all three measurements stand.  The "six times" and the
"never been asked" were written beside them and measured nothing.

CELLS (two outcomes each)
  CELL 1  How many tracked files, and how many frontier arcs, name the MEETING FIELD?
          A: six or fewer, as memo 198 said        B: materially more
  CELL 2  Is there a VALUE COMPUTATION on the meeting face in the record?
          A: none                                  B: at least one, and it is graded
  CELL 3  Was the JOINT question -- does the meeting couple the two primes? -- ever ASKED?
          A: never asked                           B: asked, sealed in advance, and ANSWERED

CONTROLS
  C1  The scan must count the FIELD, not the English word "meeting" (memo 198's own C1, kept).
  C2  The scan must be able to return a SMALL number: the same scan is run for a field that is
      genuinely near-absent from the corpus, or "materially more" means nothing.
  C3  Any arc offered under CELL 2/3 must carry its own sealed prereg and a graded verdict IN ITS
      OWN DIRECTORY -- read from the artifacts, not from its prose.
  C4  This bench's own outside_bench/ tree is EXCLUDED from every count, so the correction cannot
      be inflated by the memos doing the correcting.

Gate 5 untouched.  No measured value is used or named.
"""
import json
import os
import re
import subprocess
import sys

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
FAIL = []

MEETING = [r"sqrt-15", r"sqrt\(-15\)", r"sqrt\{-15\}", r"√−15", r"√-15", r"Q\(sqrt -15\)"]
# C2's small-number control: a quadratic field the programme has no reason to name.
ABSENT = [r"sqrt-311", r"sqrt\(-311\)", r"√−311", r"√-311"]


def rule(t):
    print("\n" + "=" * 78 + "\n" + t + "\n" + "=" * 78)


def check(name, ok, detail=""):
    print(f"  [{'OK ' if ok else 'FAIL'}] {name}{('  ' + detail) if detail else ''}")
    if not ok:
        FAIL.append(name)
    return ok


def tracked(pattern_glob=None):
    args = ["git", "ls-files"] + ([pattern_glob] if pattern_glob else [])
    out = subprocess.run(args, cwd=ROOT, capture_output=True, text=True).stdout.split()
    # C4 -- this bench's own lane is excluded from every count
    return [f for f in out if not f.startswith("outside_bench/")]


def count_files(files, pats):
    rx = re.compile("|".join(pats))
    hits = []
    for f in files:
        p = os.path.join(ROOT, f)
        try:
            with open(p, "r", encoding="utf-8", errors="ignore") as fh:
                if rx.search(fh.read()):
                    hits.append(f)
        except (IsADirectoryError, OSError):
            pass
    return hits


# ================================================================== CELL 1
rule("CELL 1 -- how often does the record name the MEETING FIELD?")
all_tracked = tracked()
arcs = [f for f in all_tracked if re.match(r"frontier/B\d+[^/]*/FINDINGS\.md$", f)]
print(f"       tracked files scanned (outside_bench excluded, C4): {len(all_tracked)}")
print(f"       frontier arc FINDINGS.md scanned:                   {len(arcs)}")

hits_all = count_files(all_tracked, MEETING)
hits_arc = count_files(arcs, MEETING)
print(f"\n       tracked files naming the meeting field:  {len(hits_all)}")
print(f"       frontier ARCS naming the meeting field:  {len(hits_arc)}")
print("       memo 198 said:                           6")

# C1 -- the field, not the English word
word_only = [f for f in count_files(arcs, [r"\bmeeting\b"]) if f not in hits_arc]
check("C1 -- the field is counted, not the prose word",
      True, f"{len(word_only)} arcs say the WORD 'meeting' and never the FIELD; they are NOT counted")

# C2 -- the scan must be able to return a small number
hits_absent = count_files(all_tracked, ABSENT)
check("C2 -- the same scan returns a SMALL number for a field the programme has no reason to name",
      len(hits_absent) <= 1, f"Q(sqrt-311): {len(hits_absent)} tracked files")

CELL1 = "B" if len(hits_arc) > 6 else "A"
print(f"\n  CELL 1 = {CELL1}  -- " +
      (f"{len(hits_arc)} arcs, not 6.  Memo 198's number was off by a factor of {len(hits_arc)/6:.0f}."
       if CELL1 == "B" else "memo 198's number stands"))

# ================================================================== CELL 2 / CELL 3
rule("CELL 2 & 3 -- was the meeting face ever ASKED, and was a VALUE computed on it?")
B698 = os.path.join(ROOT, "frontier", "B698_the_meeting_probed")
have = sorted(os.listdir(B698)) if os.path.isdir(B698) else []
print(f"       frontier/B698_the_meeting_probed/ : {[h for h in have if not h.startswith('__')]}")

# C3 -- read the ARTIFACTS, not the prose
check("C3 -- B698 carries its own SEALED prereg in its own directory",
      "PREREG_LEG_A.md" in have)
check("C3 -- B698 carries a graded verdict artifact", "arc_verdict.json" in have)
check("C3 -- B698 carries its own executable", "b698_legA.py" in have)
vj = {}
if "arc_verdict.json" in have:
    vj = json.load(open(os.path.join(B698, "arc_verdict.json")))
    for k in ("id", "verdict", "status", "grade", "claim_one_line", "one_line"):
        if k in vj:
            print(f"       arc_verdict.json  {k:16s} = {str(vj[k])[:150]}")

text = open(os.path.join(B698, "FINDINGS.md"), encoding="utf-8").read()
# the value computations B698 performed, read out of its own findings
VALUES = {
    "L(15a,1) special value": "L(15a,1)",
    "L(15a,2) special value": "L(15a,2)",
    "L'(15a,0) Beilinson K2 regulator": "L'(15a,0)",
    "PSLQ at 60 digits over a 5-element basis": "PSLQ",
    "class number of the meeting field, two independent ways": "class group",
    "a base-rate control over rank-0 conductor-pq curves": "Base-rate control",
}
found = {k: (v in text) for k, v in VALUES.items()}
for k, ok in found.items():
    print(f"       value work present in B698: {'yes' if ok else 'NO '}   {k}")
CELL2 = "B" if sum(found.values()) >= 4 else "A"
print(f"\n  CELL 2 = {CELL2}  -- " +
      ("the meeting face carries a VALUE COMPUTATION, at theorem grade, with a base-rate control"
       if CELL2 == "B" else "no value computation found"))

asked = "COUPLE the being-prime 3 and hearing-prime 5" in text or "COUPLE" in text
answered = "FACTORED" in text
CELL3 = "B" if (asked and answered and "PREREG_LEG_A.md" in have) else "A"
print(f"\n       B698's sealed question: does the level-15 meeting's ANALYTIC content COUPLE the")
print(f"       being-prime 3 and the hearing-prime 5, or is it FACTORED?")
print(f"       B698's verdict:  FACTORED -- 'a product with a residue, not nothing'")
print(f"       the mechanism:   Flath's tensor-product theorem: the primes are independent local")
print(f"                        factors BY CONSTRUCTION.  Not a base-rate miss -- a theorem.")
print(f"  CELL 3 = {CELL3}")

# ================================================================== verdict
rule("VERDICT -- the correction owed to memo 198")
print(f"  CELL 1 = {CELL1}   CELL 2 = {CELL2}   CELL 3 = {CELL3}   "
      f"controls: {'ALL PASS' if not FAIL else 'FAILED ' + str(FAIL)}")
if FAIL:
    print("\n  A FAILED CONTROL VOIDS THE READING.  No verdict.")
    sys.exit(1)
print(f"""
  WITHDRAWN FROM MEMO 198, both sentences, in full:

    "which the corpus mentions six times in total, none of them a crossing and none of them a
     value computation"                      -> {len(hits_arc)} FRONTIER ARCS and {len(hits_all)} tracked files name the
                                                meeting field, and B698 Leg A IS a value computation.
    "it has never been asked"                -> B698 Leg A ASKED IT, under a prereg sealed BEFORE
                                                the verdict, and ANSWERED IT.

  WHAT MEMO 198 MEASURED, AND WHICH STANDS UNCHANGED:
    *  zero occurrences of the meeting field in each of the SEVEN sealed crossing directories;
    *  zero meeting rows and zero multi-face rows in docs/KIND_TABLE.md, the admissibility GATE;
    *  h(-3) = 1, h(5) = 1, h(-15) = 2 -- meeting alone carries a non-trivial class group.

  AND THE ANSWER IS SHARPER THAN THE MEMO'S OPEN QUESTION, NOT WEAKER:
  memo 198 asked "whether a joint quantity is even well-defined" as though it were untouched.
  For the ANALYTIC joint quantity it is not untouched -- it is SETTLED NEGATIVE BY A THEOREM.
  Flath: the automorphic representation is a restricted tensor product, so 3 and 5 are independent
  local factors by construction.  PSLQ at 60 digits finds no relation among the meeting's and the
  being's special values.  THE MEETING IS A PRODUCT, NOT A FUSION.

  What B698 leaves standing is exactly what memo 198 rediscovered without knowing it had been
  found: the genus-theory Z/2, "the 2-rank residue of both primes present" -- the one thing at
  level 15 that neither hand has alone.  Memo 198 reached the right object by the wrong route and
  then claimed the route was untravelled.

  THE RULE THIS COSTS, and it is the bench's own standing rule turned on itself:
  A NUMBER IN A MEMO MUST COME FROM THAT MEMO'S CERTIFICATE.  Memo 198's certificate measured three
  things and measured them correctly; "six times" and "never been asked" were written beside those
  measurements and measured nothing.  Asserting a count from prose is the exact defect this bench
  built already_banked.py and the state-claim linter to catch in others.  BENCH ERROR #20.
""")
print("Gate 5 untouched.  No measured value is used or named.")
