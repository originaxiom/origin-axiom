"""OUTSIDE BENCH -- triaging the 28 sweep hits that are NOT docs/OPEN_LEADS.md rows.

No seal: every claim is a substring test on a tracked file at HEAD, or a count
taken from the corpus's own instrument.

The question: memo 208 left 28 flagged claims unexamined on eleven other surfaces
and implied they were a backlog.  Are they?

Run: python3 outside_bench/certificates/the_sweeps_false_positives.py
"""
import pathlib
import subprocess

ROOT = pathlib.Path(__file__).resolve().parents[2]


def must(rel, needle, label, want=True):
    body = (ROOT / rel).read_text(errors='replace')
    line = next((i for i, l in enumerate(body.split('\n'), 1) if needle in l), None)
    ok = (line is not None) == want
    print(f"  [{'OK ' if ok else 'FAIL'}] {label}   ({rel}" + (f":{line}" if line else "") + ")")
    print(f"         \"{needle[:98]}\"")
    assert ok, f"{needle!r} in {rel}: expected present={want}"
    return line


print("=" * 78)
print("THE SWEEP'S FALSE POSITIVES")
print(f"HEAD = {subprocess.check_output(['git','-C',str(ROOT),'rev-parse','--short','HEAD']).decode().strip()}")
print("=" * 78)

print("\n--- (A) GENUINELY STALE: two status rows in docs/views/THE_SPINE.md ---")
must('docs/views/THE_SPINE.md', '- **B171** `OPEN`', 'B171 is listed OPEN on the spine')
must('frontier/B172_combination_gap_resolution/FINDINGS.md',
     'the combination gap, resolved (Phase 1)', 'B172 resolves it (Phase 1)')
must('frontier/B172_combination_gap_resolution/FINDINGS.md',
     'Answers the question B171', 'and names B171 as the question it answers')
must('docs/views/THE_SPINE.md', '- **B1130** `OPEN`', 'B1130 is listed OPEN on the spine')
must('frontier/B1133_c4_single_end/FINDINGS.md',
     'the tower is SINGLE-END', 'B1133 answers the two-ended question')
must('frontier/B1133_c4_single_end/FINDINGS.md',
     'RESOLVED single-end', 'and says so in the word RESOLVED')

print("\n--- (B) CORRECT: the spine agrees with the arc's own verdict ---")
must('docs/views/THE_SPINE.md', '- **B1156** `OPEN`', 'B1156 is listed OPEN on the spine')
must('frontier/B1156_seam_a_gate2/FINDINGS.md', 'Verdict OPEN (seam',
     "and B1156's own arc verdict IS open -- the spine is right")

print("\n--- (C) EXEMPLARY: docs/OPEN_PROBLEMS.md gate D does the write-back itself ---")
must('docs/OPEN_PROBLEMS.md', 'the non-Hermitian case is open (L19/L20)', 'gate D states its own scope')
must('docs/OPEN_PROBLEMS.md', 'Currency note, Review 47 (2026-08-20)', 'and carries a dated currency note')
must('docs/OPEN_PROBLEMS.md',
     'tempted to reuse B1085/B1095', 'that warns the next reader off the wrong machinery')

print("\n--- (D) TRACKED-PENDING: the I3 row is stale against THIS BENCH's own memo 136 ---")
must('docs/GRAND_COMPUTATION_LEDGER.md', 'I3. **THE DESIGNED CROSSING, never run**',
     'the ledger still calls the designed crossing never run')
must('docs/GRAND_COMPUTATION_LEDGER.md', "SPEC'D-READY, off-queue", 'and spec-d-ready')
must('outside_bench/INDEX.md', 'NOT FIREABLE, THE LAST LICENSED ROW LEFT UNSPENT',
     'while memo 136 found the shot NOT FIREABLE')
must('docs/HARVEST_LEDGER.md', 'THE θ-EVEN DESIGNED CROSSING', 'and the harvest ledger carries it')
must('docs/HARVEST_LEDGER.md', 'the slice D backlog, read before Review 57',
     '**SCHEDULED**, with a reason and a deadline -- an OWNED write-back')

print("\n--- (E) BENIGN: a verdict document citing the arc that produced its verdict ---")
for rel, needle, label in [
    ('docs/LAW_MAP.md', 'THE MEETING IS A PRODUCT, NOT A FUSION (B698 Leg A',
     'LAW_MAP names its decider in the law row itself'),
    ('docs/LAW_MAP.md', 'MULTIPLICITY/SCALE IS THE OBSERVER\'S (B719)',
     'and again'),
    ('docs/THE_SM_VERDICT.md', 'The VEV *direction* is an input in every framework',
     'THE_SM_VERDICT states a verdict its arc proved'),
]:
    must(rel, needle, label)
print("  These score high on the sweep BECAUSE they are well sourced: the surface and the")
print("  arc share the rare terms by construction.  A high score here is the HEALTHY state.")

print("\n" + "-" * 78)
print("THE TRIAGE OF THE 28")
print("-" * 78)
print("""  Examined here, one by one (5 of 28):
    genuinely stale .......... 2   THE_SPINE: B171, B1130
    correct as written ....... 1   THE_SPINE: B1156 (the arc's own verdict is OPEN)
    exemplary write-back ..... 1   OPEN_PROBLEMS gate D (dated currency note)
    tracked-pending .......... 1   GRAND_COMPUTATION_LEDGER I3 (HARVEST_LEDGER: SCHEDULED)

  Not examined one by one (23 of 28), CLASSIFIED BY CLASS and fenced as such:
    every remaining hit is a verdict/law/paper surface citing the arc that
    produced its verdict.  Per-surface totals from the sweep:
      LAW_MAP 7 - main.tex 3 - THE_SM_VERDICT 3 - THE_SPINE 3 - THE_FRAMEWORK 2
      PRICED_DOORS 2 - OPEN_PROBLEMS 2 - CROSSING_REQUIREMENTS 2
      GRAND_COMPUTATION_LEDGER 2 - CLOSED_DOORS 1 - THE_ROAD 1   = 28
    (THE_SPINE's 3, OPEN_PROBLEMS' 1 and GRAND_COMPUTATION_LEDGER's 1 are the
     five examined above; 23 remain in the benign class BY CLASSIFICATION, not
     by individual verification.  Stated as a classification, not a verdict.)""")
print("\n" + "=" * 78)
print("ALL ASSERTIONS HOLD AT THIS HEAD.")
print("=" * 78)
