"""OUTSIDE BENCH -- WHAT_WOULD_COUNT section 4A.2 says the seal has not happened. It has.

No seal on this certificate: every claim is a substring test on a tracked file at HEAD.

Run: python3 outside_bench/certificates/the_seal_already_happened.py
"""
import pathlib
import subprocess

ROOT = pathlib.Path(__file__).resolve().parents[2]


def must(rel, needle, label):
    body = (ROOT / rel).read_text(errors='replace')
    line = next((i for i, l in enumerate(body.split('\n'), 1) if needle in l), None)
    print(f"  [{'OK ' if line else 'FAIL'}] {label}   ({rel}" + (f":{line}" if line else "") + ")")
    print(f"         \"{needle[:96]}\"")
    assert line, f"not found in {rel}: {needle!r}"
    return line


print("=" * 78)
print("THE SEAL ALREADY HAPPENED")
print(f"HEAD = {subprocess.check_output(['git','-C',str(ROOT),'rev-parse','--short','HEAD']).decode().strip()}")
print("=" * 78)

print("\n--- (A) what WHAT_WOULD_COUNT section 4A.2 says today ---")
must('docs/WHAT_WOULD_COUNT.md', '**STATUS: SPEC ONLY, OWNER-PENDING**',
     'the tier is marked owner-pending')
must('docs/WHAT_WOULD_COUNT.md', 'what has not happened is the seal',
     'and says in words that the seal has not happened')

print("\n--- (B) the seal, in the ledger, three weeks earlier ---")
must('docs/SEAL_LEDGER.md', 'THE EDGE SEAL (L173;', 'the SEAL LEDGER carries THE EDGE SEAL')
must('docs/SEAL_LEDGER.md', '| 2026-08-21 | THE EDGE SEAL', 'dated 2026-08-21')
must('frontier/B1106_edge_seal/FINDINGS.md',
     "THE EDGE SEAL: the program's first outward-facing falsifier is sealed",
     'B1106 banks it as the first outward-facing falsifier')
must('frontier/B1106_edge_seal/FINDINGS.md', 'Owner rulings', 'with the owner rulings recorded')
must('frontier/B1106_edge_seal/FINDINGS.md', 'D-2 (the edge lane seals alone',
     'D-2 executed')
must('frontier/B1106_edge_seal/FINDINGS.md', 'D-3 (placeholder', 'D-3 executed')
must('docs/EDGE_PREREG_SPEC.md', 'Status at landing: SEALED',
     "and the spec's own header says SEALED")

print("\n--- (C) L173's row contradicts ITSELF, in one line ---")
n = must('docs/OPEN_LEADS.md', '**SEALED 2026-08-21 (B1106;', "the row's header says SEALED")
must('docs/OPEN_LEADS.md', 'the aperiodic unseal RESOLVED', 'and the unseal RESOLVED')
must('docs/OPEN_LEADS.md', "SPEC ONLY until the aperiodic design's owner-pending unseal resolves",
     "the SAME row's body says SPEC ONLY, owner-pending")
must('docs/OPEN_LEADS.md', "GATED on the owner's aperiodic unseal for the seal step",
     "and its value column says GATED on the owner")
print(f"         all four strings are on line {n} of the same file.")

print("\n--- (D) the seal was amended once, by its own rule ---")
must('docs/SEAL_LEDGER.md', 'THE EDGE SEAL ADDENDUM-BESIDE (B1171',
     'an addendum-beside is in the ledger')
must('docs/EDGE_PREREG_SPEC_ADDENDUM_B8146.md', 'is NOT edited',
     'and it states the sealed spec is not edited')
must('docs/EDGE_PREREG_SPEC_ADDENDUM_B8146.md', 'R6′ (the commissioned observable)',
     "R6 re-posed as a commissioned OBSERVABLE")
must('docs/EDGE_PREREG_SPEC_ADDENDUM_B8146.md', 'demonstration paper, not metrology',
     'because the anchor experiment is not metrology')
must('docs/EDGE_PREREG_SPEC_ADDENDUM_B8146.md',
     'The program supplies the KNOB', 'the programme supplies the knob, not the readout')

print("\n--- (E) what the seal actually contains ---")
for needle, label in [
    ('WHAT STANDARD THEORY ALREADY FORCES (read this before the prediction)',
     'section 0 states the standard content FIRST'),
    ('THE PREDICTION (the differential; all content banked in B1095, exact)',
     'section 1 is the differential, not the counts'),
    ('KILL CONDITIONS (any one, at budget, kills the prediction; NEGATIVE banks)',
     'section 2 names what kills it'),
    ('CONTROLS (C-GEN RUN AND PASSED before this seal', 'section 3: the control ran BEFORE the seal'),
]:
    must('docs/EDGE_PREREG_SPEC.md', needle, label)

print("\n--- (F) and this bench already priced what passing would buy ---")
must('outside_bench/INDEX.md', 'THE SEALED EDGE LAW IS THE MODAL BEHAVIOUR OF A RANDOM PHASE',
     'memo 197')
must('outside_bench/INDEX.md', 'ONE PHASE IN FIVE REPRODUCES THE SEALED LAW EXACTLY OVER NINE WINDOWS',
     'one phase in five reproduces the sealed law')

print("\n" + "=" * 78)
print("ALL ASSERTIONS HOLD AT THIS HEAD.")
print("=" * 78)
