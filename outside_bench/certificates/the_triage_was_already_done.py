"""OUTSIDE BENCH -- the B666 cell-T lead triage, against the register it was built for.

No seal: every claim here is a substring or table test on tracked files at HEAD.

B666 cell T (2026-07-17) triaged every L-numbered lead below L91 not already marked
resolved in its own row, citing a decider for every SUPERSEDED verdict.  This
certificate asks the only question that matters about it: DID THE VERDICTS LAND?

Run: python3 outside_bench/certificates/the_triage_was_already_done.py
"""
import pathlib
import re
import subprocess

ROOT = pathlib.Path(__file__).resolve().parents[2]
TT = ROOT / 'frontier/B666_leads_campaign/cellT/TRIAGE_TABLE.md'
OL = ROOT / 'docs/OPEN_LEADS.md'

# a row counts as CARRYING a resolution if any of these appears in it.  The list is
# deliberately generous: a false NEGATIVE here would invent staleness that is not there.
RESOLVED = ('SUPERSEDED', 'CLOSED', 'RESOLVED', 'DONE', 'ANSWERED', 'CHARACTERIZED',
            'CONFIRMED', 'WITHDRAWN', 'RETRACTED', 'CLEARED', 'MOOT', 'ADJUDICATED',
            'PROVED', 'REFUTED', 'TOMBSTONE', 'DISCHARGED', 'COMPLETE', 'BANKED')

print("=" * 78)
print("THE TRIAGE WAS ALREADY DONE")
print(f"HEAD = {subprocess.check_output(['git','-C',str(ROOT),'rev-parse','--short','HEAD']).decode().strip()}")
print("=" * 78)

tt = TT.read_text()
assert 'B666 CELL T — WAVE 0: the historical-leads triage (2026-07-17)' in tt
assert 'Every SUPERSEDED\nverdict cites the superseding arc; nothing is asserted from memory.' in tt
print(f"\n  {TT.relative_to(ROOT)}")
print("  \"B666 CELL T — WAVE 0: the historical-leads triage (2026-07-17)\"")
print("  \"Every SUPERSEDED verdict cites the superseding arc; nothing is asserted from memory.\"")

rows = []
for line in tt.split('\n'):
    if not line.startswith('|'):
        continue
    c = [x.strip() for x in line.strip('|').split('|')]
    if len(c) < 4:
        continue
    m = re.match(r'\*\*(L\d+)\*\*', c[0])
    if m:
        rows.append((m.group(1), c[2].replace('*', ''), c[3]))
sup = [r for r in rows if r[1] == 'SUPERSEDED']
print(f"\n  triage rows parsed: {len(rows)}   of which SUPERSEDED: {len(sup)}")

ollines = OL.read_text().split('\n')


def register_rows(lid):
    out = []
    for i, l in enumerate(ollines, 1):
        if l.startswith('|') and re.search(r'\*\*' + lid + r'(\*\*|\s+[—-])', l):
            out.append((i, l))
    return out


print("\n" + "-" * 78)
print("For each SUPERSEDED verdict: does its row in docs/OPEN_LEADS.md carry ANY")
print("resolution word at all?  (generous vocabulary -- a miss here would invent staleness)")
print("-" * 78)
unapplied, applied, missing = [], [], []
for lid, _, cite in sup:
    rs = register_rows(lid)
    if not rs:
        missing.append(lid)
        print(f"  {lid:5s}  NO ROW FOUND in docs/OPEN_LEADS.md")
        continue
    carries = [w for i, l in rs for w in RESOLVED if w in l]
    if carries:
        applied.append(lid)
        print(f"  {lid:5s}  applied      -- row {rs[0][0]} carries {sorted(set(carries))[:3]}")
    else:
        unapplied.append(lid)
        print(f"  {lid:5s}  *** NOT APPLIED *** -- row {rs[0][0]} carries no resolution word")
        print(f"         triage decider: {cite[:120]}")

print(f"\n  applied: {len(applied)}  {applied}")
print(f"  NOT applied: {len(unapplied)}  {unapplied}")
print(f"  no row: {len(missing)}  {missing}")

print("\n" + "-" * 78)
print("The four found by reading this session, which post-date or escaped the triage")
print("-" * 78)


def must(rel, needle, label):
    body = (ROOT / rel).read_text(errors='replace')
    line = next((i for i, l in enumerate(body.split('\n'), 1) if needle in l), None)
    print(f"  [{'OK ' if line else 'MISS'}] {label}  ({rel}:{line})")
    print(f"         \"{needle[:96]}\"")
    assert line, f"not found in {rel}: {needle!r}"


must('docs/OPEN_LEADS.md', 'OPEN — first in the queue', 'L53 duplicate row reads open')
must('docs/OPEN_LEADS.md', 'L53 CLOSED.', 'L53 primary row reads closed')
must('docs/OPEN_LEADS.md', '| MATH | ★★★ | OPEN (B579) |', 'L72 row reads open')
must('frontier/B775_phase2_wave1/cells/P2W5-L72/compute.py', 'THIS CELL RUNS PHASES 2 AND 3.', 'L72 phases 2-3 ran')
must('docs/OPEN_LEADS.md', 'OPEN, ready', 'L112 row at 659 reads open')
must('docs/OPEN_LEADS.md', '| L112 | **CLOSED**', 'L112 row at 807 reads CLOSED')
must('docs/OPEN_LEADS.md', 'OPEN — C1 first', 'L174 campaign row reads C1 first')
must('docs/OPEN_LEADS.md', '**DONE (B1088', 'L174 C1 is banked, eight lines above')
must('docs/OPEN_LEADS.md', 'NEEDS-SPECIALIST, honestly fenced', 'L174 C5 reads needs-specialist')
must('frontier/B1108_c5_archimedean/FINDINGS.md', 'C5 CLOSED NEGATIVE, harvested', 'an arc titled C5 CLOSED NEGATIVE')

print("\n" + "=" * 78)
print("ALL ASSERTIONS HOLD AT THIS HEAD.")
print("=" * 78)
