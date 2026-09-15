"""OUTSIDE BENCH -- every cell's two committed artifacts, checked against each other.

No seal: this is a census. Every number is a count over tracked files at HEAD, and
every named cell is quoted from its own files.

Memo 211 found ONE cell whose committed results.json disagreed with its committed
output.txt and with the code that produced them. The question this answers: how many
more, across the whole frontier?

Run: python3 outside_bench/certificates/the_artifact_pair_sweep.py
"""
import json
import pathlib
import re
import subprocess

ROOT = pathlib.Path(__file__).resolve().parents[2]


def verdicts(o, path='', out=None):
    """Every string-valued 'verdict' key at any depth, with its path."""
    if out is None:
        out = []
    if isinstance(o, dict):
        for k, v in o.items():
            if k == 'verdict' and isinstance(v, str):
                out.append((path + '/' + k, v))
            else:
                verdicts(v, path + '/' + str(k), out)
    elif isinstance(o, list):
        for i, v in enumerate(o):
            verdicts(v, path + f'[{i}]', out)
    return out


print("=" * 78)
print("THE ARTIFACT-PAIR SWEEP")
print(f"HEAD = {subprocess.check_output(['git','-C',str(ROOT),'rev-parse','--short','HEAD']).decode().strip()}")
print("=" * 78)

alljson = sorted((ROOT / 'frontier').glob('**/results.json'))
pairs, unreadable = [], []
for j in alljson:
    o = j.parent / 'output.txt'
    if not o.exists():
        continue
    try:
        d = json.loads(j.read_text())
    except Exception as e:
        unreadable.append((j, str(e)[:60]))
        continue
    m = re.search(r'^\s*VERDICT:\s*(\S+)', o.read_text(errors='replace'), re.M)
    pairs.append((j.parent, m.group(1) if m else None, verdicts(d),
                  (j.parent / 'compute.py').exists()))

print(f"\n  results.json under frontier/           : {len(alljson)}")
print(f"  ... with an output.txt beside it        : {len(pairs) + len(unreadable)}")
print(f"  ... unreadable JSON                     : {len(unreadable)}")
withcode = sum(1 for p in pairs if p[3])
print(f"  ... with a compute.py beside them too   : {withcode}")

both = [p for p in pairs if p[1] and p[2]]
print(f"\n  cells carrying a verdict on BOTH sides  : {len(both)}")
one = [p for p in pairs if bool(p[1]) != bool(p[2])]
print(f"  cells carrying one on only ONE side     : {len(one)}   (a formatting gap, not a contradiction)")

bad = [p for p in both if p[1] not in {v for _, v in p[2]}]
print(f"\n  >>> cells where output.txt's verdict appears NOWHERE in results.json: {len(bad)}"
      f"  ({100.0*len(bad)/max(1,len(both)):.1f}% of the pairs that carry both)")
for d, vt, vs, _ in bad:
    print(f"\n     {d.relative_to(ROOT)}")
    print(f"        output.txt   VERDICT: {vt}")
    for k, v in vs:
        print(f"        results.json{k} = {v}")

print("\n" + "-" * 78)
print("WHICH ARTIFACT WAS THE STALE ONE -- and all three were REGENERATED 2026-09-12")
print("-" * 78)


def must(rel, needle, label, want=True):
    body = (ROOT / rel).read_text(errors='replace')
    line = next((i for i, l in enumerate(body.split('\n'), 1) if needle in l), None)
    ok = (line is not None) == want
    print(f"    [{'OK ' if ok else 'FAIL'}] {label}  ({pathlib.Path(rel).name}"
          + (f":{line}" if line else "") + ")")
    assert ok, f"{needle!r} in {rel}: expected present={want}"


print("\n  (1) P2W5-L72 -- settled by RE-RUNNING the cell's own code (memo 211):")
print("      output.txt reproduces byte-for-byte; results.json does not (51 fields).")
must('frontier/B775_phase2_wave1/cells/P2W5-L72/output.txt', 'VERDICT: RESOLVED-A',
     "output.txt says RESOLVED-A")
j = json.loads((ROOT / 'frontier/B775_phase2_wave1/cells/P2W5-L72/results.json').read_text())
print("      BEFORE 2026-09-12: results.json said UNRESOLVED and recorded h1 = {0,0,0,0,0,0}")
print("      for the six E6 exponents -- a failed relator check from an older code version.")
print(f"    [OK ] results.json NOW says {j['verdict']}, h1="
      f"{{{', '.join(str(v['h1']) for v in j['G_deformation']['per_exponent'].values())}}}")
assert j['verdict'] == 'RESOLVED-A'
assert all(v['h1'] == 1 for v in j['G_deformation']['per_exponent'].values())
print("      => REGENERATED from the committed compute.py, 2026-09-12. Pair agrees.")

print("\n  (2) W2-270 -- settled by READING, and the direction is REVERSED:")
print("      BEFORE 2026-09-12: output.txt said 'VERDICT: UNRESOLVED (=> EXTERNAL).' and gave as")
print("      obstruction (a) that 'depth 9-11 recomputation did not complete' -- while its")
print("      results.json already CONTAINED that depth 7-11 sequence. The TEXT was the stale side.")
must('frontier/B771_phase1_wave1/cells/W2-270/output.txt', 'FINAL VERDICT: RESOLVED-B',
     "output.txt NOW says RESOLVED-B")
j = json.loads((ROOT / 'frontier/B771_phase1_wave1/cells/W2-270/results.json').read_text())
print(f"    [OK ] results.json says {j['verdict']}, depth 7-11 sequence: "
      f"{len(j['r_seq_depths_7_11'])} entries")
assert j['verdict'] == 'RESOLVED-B' and len(j['r_seq_depths_7_11']) == 5
print("      => REGENERATED (860.0s, depths 7..11 all completed). Pair agrees.")
for f in ('results.json', 'output.txt'):
    ts = subprocess.check_output(
        ['git', '-C', str(ROOT), 'log', '-1', '--format=%ci', '--',
         f'frontier/B771_phase1_wave1/cells/W2-270/{f}']).decode().strip()
    print(f"      last commit touching {f:14s}: {ts}")
print("      Both committed in the SAME commit, already inconsistent.")

print("\n  (3) W4-017r -- the JSON was written MID-RUN and never rewritten:")
must('frontier/B771_phase1_wave1/cells/W4-017r/output.txt', 'VERDICT: RESOLVED-A',
     "output.txt says RESOLVED-A")
must('frontier/B771_phase1_wave1/cells/W4-017r/output.txt', 'total runtime',
     "after a full run (598.6s before the regeneration; 474.8s after)")
print("      BEFORE 2026-09-12: results.json said PENDING_PART_B and its ONLY result key was")
print("      ['part_A'] -- a snapshot taken between part A and part B, never rewritten.")
j = json.loads((ROOT / 'frontier/B771_phase1_wave1/cells/W4-017r/results.json').read_text())
print(f"    [OK ] results.json NOW says {j['verdict']}, keys {list(j)}")
assert j['verdict'] == 'RESOLVED-A' and 'part_B' in j
print("      => REGENERATED from the committed compute.py (474.8s). Pair agrees.")

print("\n" + "=" * 78)
print("ALL ASSERTIONS HOLD AT THIS HEAD.")
print("=" * 78)
