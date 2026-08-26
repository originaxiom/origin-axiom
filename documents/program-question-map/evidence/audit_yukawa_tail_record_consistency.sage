#!/usr/bin/env sage
"""Compare the checked tail rows with the coordinates printed in the Markdown record."""

from pathlib import Path

HERE = Path(__file__).resolve().parent
load(str(HERE / "certify_yukawa_down_tail_cech_308.sage"))

documented = {
    0: [1,0,0,0,0,0,0,1008,0,0,0,0,0,0,0,0,0,0,0,0,0],
    2: [0,1,0,0,0,0,0,0,0,0,0,0,1008,0,0,0,0,0,0,0,0],
    4: [0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1008,0,0,0,0,0],
    6: [0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1005,1003,0,0,0],
    8: [0,0,0,1,0,0,0,1008,0,0,0,0,0,0,0,0,0,0,0,0,0],
}

verdict = {}
for label in tail_labels:
    if len(documented[label]) != 21:
        verdict[label] = (False, False, False, len(documented[label]))
        print("DOCUMENTED", label, "invalid coordinate count =", len(documented[label]))
        continue
    row = matrix(k, [documented[label]])
    annihilates = row * cech_map == zero_matrix(k, 1, 18)
    has_phase = row * T.inverse() == zeta_mod**label * row
    matches_runtime = row == tail_rows[label]
    verdict[label] = (annihilates, has_phase, matches_runtime, 21)
    print("DOCUMENTED", label, "annihilates/phase/matches/count =", verdict[label])

assert verdict[2] == (True, True, True, 21)
assert verdict[4] == (True, True, True, 21)
assert verdict[8] == (True, True, True, 21)
assert verdict[0] == (False, False, False, 21)
assert verdict[6] == (False, False, False, 20)

print("RESULT documented row 0 fails both defining identities in the current locked basis")
print("RESULT documented row 6 is malformed: 20 coordinates for a 21-dimensional target")
print("RESULT runtime rows are the checked source of truth for this certificate version")
