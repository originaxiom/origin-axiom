"""CERTIFICATE -- the exhaustion is exhaustion of a table with no JOINT row in it.

OCCASION (owner, 2026-09-11): "are we making same mistake again by counting only on the object, and
not its relationships, faces interactions.  the nature emerges wher they meet or elsewhere with all
faces accounted for"

Aimed at a sentence this bench banked the same day: "the object's numbers are not nature's numbers"
(memo 195 addendum 2, from the K3 refutation).  The charge is that the sentence generalises from a
tested population to all populations.  This tests the charge.

CELLS (two outcomes each)
  CELL 1  Do the seven sealed crossings ever draw on the MEETING face, Q(sqrt-15)?
          A: at least one does        B: none does
  CELL 2  Does docs/KIND_TABLE.md -- the admissibility GATE, whose own rule is "a prereg
          proposing a pair absent from the admissible list does not seal" -- list any
          object quantity in Q(sqrt-15), or any quantity built from MORE THAN ONE face?
          A: it lists one             B: every admissible row is single-field, none is meeting
  CELL 3  Does the meeting face carry anything the other two do not?
          A: no, it is redundant      B: yes, a non-trivial class group neither other face has

CONTROLS
  C1  The scan must distinguish the FIELD sqrt-15 from the English word "meeting", which occurs in
      ordinary prose.  Both counts are printed.
  C2  Class numbers are COMPUTED by counting reduced primitive forms, not asserted, and the count
      is validated against two known values (h(-4) = 1, h(-23) = 3).
  C3  The tally must find the fields that ARE there, or a zero for sqrt-15 means nothing.
"""
import os, re, subprocess, sys
from math import gcd

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
SEVEN = ["B915", "B925", "B929", "B1027", "B1063", "B1066", "B1075"]


def h(D):
    """class number of the imaginary quadratic order of discriminant D, by reduced forms"""
    n, a = 0, 1
    while a * a <= abs(D) // 3 + 1:
        for b in range(-a + 1, a + 1):
            if (b * b - D) % (4 * a):
                continue
            c = (b * b - D) // (4 * a)
            if c < a or gcd(gcd(a, abs(b)), c) != 1:
                continue
            if a == c and b < 0:
                continue
            if abs(b) == a and b < 0:
                continue
            n += 1
        a += 1
    return n


print(__doc__)
print("=" * 78)

# ------------------------------------------------------------------ C2 + CELL 3
c2 = (h(-4) == 1 and h(-23) == 3)
print(f"C2  class-number counter validated: h(-4) = {h(-4)} (expect 1), h(-23) = {h(-23)} (expect 3)"
      f"  -> {'PASS' if c2 else 'FAIL'}")
print()
print("CELL 3  what each face carries")
print(f"    being    Q(sqrt-3)   unit rank 0   units mu_6 (the TRIT)     CLASS NUMBER {h(-3)}")
print( "    hearing  Q(sqrt5)    unit rank 1   fundamental unit phi      CLASS NUMBER 1  (B1069: h = h+ = 1)")
print(f"    meeting  Q(sqrt-15)  unit rank 0   units +-1                 CLASS NUMBER {h(-15)}")
cell3 = "B" if h(-15) > 1 and h(-3) == 1 else "A"
print(f"    -> {cell3}  " + ("(meeting is the ONLY one of the three with a non-trivial class group --"
                             " the genus bit B1276 names as the meeting-leg)" if cell3 == "B" else ""))

# ------------------------------------------------------------------ CELL 1 + C1
print()
print("CELL 1  do the seven sealed crossings draw on the meeting FIELD?")
FIELD = re.compile(r"sqrt\s*\(?\s*-\s*15|√−15|√-15|sqrt-15", re.I)
WORD = re.compile(r"\bmeeting\b", re.I)
tot_field = 0
for a in SEVEN:
    d = [x for x in os.listdir(os.path.join(ROOT, "frontier")) if x.startswith(a + "_")]
    body = ""
    if d:
        for r, _, fs in os.walk(os.path.join(ROOT, "frontier", d[0])):
            for f in fs:
                try:
                    body += open(os.path.join(r, f), encoding="utf-8", errors="ignore").read()
                except OSError:
                    pass
    nf, nw = len(FIELD.findall(body)), len(WORD.findall(body))
    tot_field += nf
    print(f"    {a:6s} field sqrt-15: {nf:3d}      (English word 'meeting': {nw:3d}  -- C1, kept separate)")
cell1 = "B" if tot_field == 0 else "A"
print(f"    -> {cell1}  " + ("(NOT ONE of the seven touches the meeting field)" if cell1 == "B" else ""))

# ------------------------------------------------------------------ CELL 2 + C3
print()
print("CELL 2  the admissibility GATE, docs/KIND_TABLE.md")
kt = open(os.path.join(ROOT, "docs", "KIND_TABLE.md"), encoding="utf-8").read()
print("    its own rule: 'a prereg proposing a pair absent from the admissible list does not seal.'")
fields = []
for line in kt.splitlines():
    if line.startswith("|") and line.count("|") > 5:
        cells = [c.strip() for c in line.split("|")]
        # the object-side table is | quantity | kind | bounds | FIELD | channel |, so split()
        # gives ['', quantity, kind, bounds, field, channel, ''] -- the field is cells[4].
        # (C3 caught cells[5] here on the first run: the control earned its place.)
        if len(cells) > 5 and cells[1] and cells[1] != "object quantity" and not cells[1].startswith("-"):
            fields.append(cells[4])
tally = {}
for f in fields:
    if f and f != "field" and not f.startswith("-"):
        tally[f] = tally.get(f, 0) + 1
print("    the FIELD column of every object-side row:")
for f, n in sorted(tally.items(), key=lambda kv: -kv[1]):
    print(f"       {n} x  {f}")
c3 = any("√5" in f or "ω" in f for f in tally)
n15 = len(FIELD.findall(kt))
joint = [f for f in tally if ("√5" in f and "ω" in f)]
cell2 = "B" if (n15 == 0 and not joint) else "A"
print(f"\n    C3  the tally finds the fields that ARE there (Q(sqrt5), Q(omega)): {'PASS' if c3 else 'FAIL'}")
print(f"    occurrences of the meeting field anywhere in the gate: {n15}")
print(f"    rows built from MORE THAN ONE face: {len(joint)}")
print(f"    -> {cell2}  " + ("(every admissible object quantity is SINGLE-FIELD; the product face is"
                             " absent from the gate entirely)" if cell2 == "B" else ""))

ok = c2 and c3
print()
print("ALL CONTROLS PASSED" if ok else "CONTROL FAILURE")
print(f"VERDICT: CELL 1 = {cell1}, CELL 2 = {cell2}, CELL 3 = {cell3}")
print("""
WHAT THIS LICENSES, AND WHAT IT DOES NOT.

  LICENSED: the seven-for-seven is exhaustion of a table whose field column never
  contained the product face, and whose every admissible row is single-field.  So
  "the object's numbers are not nature's numbers" OVERREACHES.  The sentence the
  record supports is: THE OBJECT'S SINGLE-FACE NUMBERS ARE NOT NATURE'S NUMBERS, AND
  NO MULTI-FACE QUANTITY HAS EVER BEEN ADMISSIBLE.

  NOT LICENSED, and saying it would repeat the error in the other direction: that the
  meeting face will yield values.  Meeting is imaginary quadratic, unit rank 0 -- by
  the same Dirichlet argument it carries TORSION, not growth.  What it has that the
  others do not is a CLASS GROUP of order 2.  A bit is still a bit, not a value.

  The untested population is therefore not "Q(sqrt-15) numbers".  It is ANY QUANTITY
  BUILT FROM MORE THAN ONE FACE AT ONCE -- and the gate has no such row.
""")
sys.exit(0 if ok else 1)
