"""chat1, 2026-10-28: post hoc read-out (labelled), written after the relay's read-only referee and committed before its
own run. No frame computation and no data; it reads committed files only.
  a  B1786's 12 slope-2/5 carriers grouped into T-orbit classes, with each class's mirror partner (b -> 3/5 - b).
  b  B1667's untwisted channel constants, c_r ~ N_2 - 2 pi L_2, at its grid points with Im tau >= 3 (the length-2
     horocycle is where the small-cut form is accurate), for comparison with the frame's twisted c_s.
  c  From explore_ckm_and_bit.json: at B1720's apexes off the mirror lines, the sign relation of J on v and on 2v,
     per (horocycle, up reading, down reading).
Run:  python3 -B riddles_posthoc2.py <main_checkout>"""
import sys, json, math, pathlib
from fractions import Fraction as Fr
ROOT = pathlib.Path(sys.argv[1]).resolve(); HERE = pathlib.Path(__file__).resolve().parent
A = Fr(2, 5)
carriers = [Fr(k, 25) for k in (3, 4, 11, 12, 17, 19, 21, 23)] + [Fr(1, 6), Fr(13, 30), Fr(23, 30), Fr(5, 6)]
def cls(b):
    """the offsets of the slope-2/5 representatives in the T-orbit of (2/5, b); T: b -> b - 2/5. (The sign flip sends a
    slope-2/5 line to slope 3/5, so among slope-2/5 representatives the class is this orbit.)"""
    out, x = [], b % 1
    for _ in range(60):
        out.append(x); x = (x - A) % 1
    return frozenset(out)
classes = {}
for b in carriers: classes.setdefault(cls(b), []).append(b)
print("a  %d carriers in %d T-orbit classes:" % (len(carriers), len(classes)))
for k, (orb, bs) in enumerate(classes.items()):
    partner = cls((Fr(3, 5) - bs[0]) % 1)
    pk = [j for j, o in enumerate(classes) if o == partner]
    print("   class %d: carriers %s; orbit %s; mirror partner class %s" % (k, [str(b) for b in bs], sorted(str(x) for x in orb), pk))
d = json.loads((ROOT / "frontier" / "B1667_the_canonical_cusp" / "verification" / "the_canonical_cusp.json").read_text())
print("b  B1667's untwisted c_r = N_2 - 2 pi L_2 at its grid points with Im tau >= 3:")
for p in d["points"]:
    if p["where"] == "grid" and p["tau"][1] >= 3.0:
        print("   tau %s: %s" % (p["tau"], {r: round(p["N_2"][r] - 2 * math.pi * p["L_2"], 3) for r in p["N_2"]}))
e = json.loads((HERE / "explore_ckm_and_bit.json").read_text())["B"]
off = [r for r in e if not r["on_mirror_line"]]
print("c  apexes off the mirror lines: %d; sign of J(v) against J(2v):" % len(off))
for key in sorted(off[0]["v"].keys()):
    opp = sum(1 for r in off if r["v"][key] * r["2v"][key] < 0); same = sum(1 for r in off if r["v"][key] * r["2v"][key] > 0)
    print("   %-16s opposite %2d, same %2d, of %d" % (key, opp, same, len(off)))
print("riddles_posthoc2 exit 0")
