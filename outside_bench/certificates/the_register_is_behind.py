"""OUTSIDE BENCH -- the lead register against its own arcs.

No seal: this certificate asserts only the PRESENCE of exact strings in tracked
files.  Every claim it makes is a substring test on a file at the current HEAD,
and it fails loudly if any string has moved.  Nothing is inferred.

Run: python3 outside_bench/certificates/the_register_is_behind.py
"""
import pathlib
import re
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]


def read(rel):
    p = ROOT / rel
    assert p.exists(), f"missing: {rel}"
    return p.read_text(errors='replace')


def must(rel, needle, label):
    body = read(rel)
    ok = needle in body
    line = None
    if ok:
        for i, l in enumerate(body.split('\n'), 1):
            if needle in l:
                line = i
                break
    print(f"  [{'OK ' if ok else 'MISS'}] {label}")
    print(f"         {rel}" + (f":{line}" if line else ""))
    print(f"         \"{needle[:100]}\"")
    assert ok, f"string not found in {rel}: {needle!r}"
    return line


print("=" * 78)
print("THE LEAD REGISTER AGAINST ITS OWN ARCS")
print(f"HEAD = {subprocess.check_output(['git','-C',str(ROOT),'rev-parse','--short','HEAD']).decode().strip()}")
print("=" * 78)

print("\n--- L53: the row says OPEN; the row above it says CLOSED ---")
must('docs/OPEN_LEADS.md', 'OPEN — first in the queue', 'the duplicate L53 row calls itself open')
must('docs/OPEN_LEADS.md', 'L53 CLOSED.', 'the primary L53 row states it is closed')
must('docs/OPEN_LEADS.md', 'THIRD ORDER NOW ALSO EXACT (B578-D1, 2026-07-14)', 'with the arc that closed it')

print("\n--- L72: the row gates phases 2-3 on phase 1; both have run ---")
must('docs/OPEN_LEADS.md', 'Phases 2-3 (E₆ 6j at levels 1-2; the CS functional along the θ-odd deformation) gated on phase 1', 'the row gates 2-3 on phase 1')
must('docs/OPEN_LEADS.md', '| MATH | ★★★ | OPEN (B579) |', 'and calls L72 open')
must('frontier/B775_phase2_wave1/cells/P2W5-L72/compute.py', 'PHASE 1 is banked: B581', 'the cell states phase 1 is banked')
must('frontier/B775_phase2_wave1/cells/P2W5-L72/compute.py', 'THIS CELL RUNS PHASES 2 AND 3.', 'and that it runs phases 2 and 3')
must('frontier/B775_phase2_wave1/FINDINGS_WAVE5.md', '**P2W5-L72**', 'and the wave findings carry its row')

print("\n--- L78: the row says OPEN; the arc says it resolves ---")
must('docs/OPEN_LEADS.md', 'OPEN — Round 2 first', 'the L78 row calls itself open')
must('frontier/B583_chiral_content/FINDINGS.md', 'L78 resolves', 'the arc says L78 resolves')
must('frontier/B583_chiral_content/FINDINGS.md', 'Level 2: rank exactly 6 = dim(θ-even) over 719 slopes', 'with the number it resolved it on')

print("\n--- L174: the row says C1 first; C1-C4 are all DONE ---")
must('docs/OPEN_LEADS.md', 'OPEN — C1 first', 'the L174 campaign row says C1 first')
for cell, arc in (('C1', 'B1088'), ('C2', 'B1090'), ('C3', 'B1089'), ('C4', 'B1091')):
    must('docs/OPEN_LEADS.md', f'**DONE ({arc}', f'{cell} is banked')

print("\n--- what B583's arc directory actually contains (the gap memo 206 filled) ---")
d = ROOT / 'frontier/B583_chiral_content'
files = sorted(p.name for p in d.iterdir() if p.is_file())
print(f"  {files}")
assert files == ['FINDINGS.md', 'READING_RAW.md', 'arc_verdict.json', 'x2r_recompute.py'], files
lock = read('tests/test_b583_content.py')
names = re.findall(r'def (test_\w+)', lock)
print(f"  the arc's lock defines: {names}")
assert 'def test_x3_mechanism_level1' in lock, "the lock's X3 test is not the level-1 one"
assert 'level 2' not in lock.lower() and 'level2' not in lock.lower(), \
    "the lock does mention level 2 after all -- re-read it"
print("  CONFIRMED: the arc's only X3 lock is the LEVEL-1 mechanism; no level-2 code exists in it.")

print("\n--- the two independent builds of the E6 level-2 stage agree ---")
import json
r = json.load(open(ROOT / 'frontier/B775_phase2_wave1/cells/P2W5-L72/results.json'))
theirs = dict(zip(r['A_modular_data']['2']['weights'], r['A_modular_data']['2']['h']))
mine = {'000000': '0', '000001': '13/21', '000010': '25/21', '001000': '25/21',
        '010000': '6/7', '100000': '13/21', '000002': '4/3', '100001': '9/7',
        '200000': '4/3'}     # memo 206's h, printed as 0, .619048, 1.190476, ... 
from fractions import Fraction
for w in sorted(theirs):
    a, b = Fraction(theirs[w]), Fraction(mine[w])
    assert a == b, f"{w}: P2W5-L72 {a} vs memo 206 {b}"
    print(f"  h[{w}] = {a}  = {float(a):.6f}   both builds")
print("  AGREE on all nine conformal weights.  P2W5-L72 reached 3.4e-41 with high precision;")
print("  memo 206 reached 5.7e-15 in float64 from an independent integer Weyl sum.")

print("\n" + "=" * 78)
print("ALL STRING ASSERTIONS HOLD AT THIS HEAD.")
print("=" * 78)
