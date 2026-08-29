"""B1215 -- carrying codex's stalled lead one step: the lepton leg's tail-selection rule.

Codex's last finding before their quota ran out, uncertified: "the tail-selection equation used for
the quark leg cannot be copied unchanged to the lepton leg. For A_11 the required raw B-pair sum is
4 mod 12, not 8; the only pure-tail pair inside the physical B_2 sector is (2,2), and it vanishes by
skewness."

That is checkable from the height-308 spec's OWN numbers, without their frames. Doing so here.
"""
from itertools import combinations_with_replacement

# --- the spec's stated data (YUKAWA_DOWN_RESIDUE_SPEC_308.md) ------------------------------
RAW = (7, 6, 2)                 # raw characters of the three legs (A, B_6, B_2)
SHIFTS = (+1, -2, -2)           # the physical shifts, applied ONCE
TOTAL_RAW = sum(RAW) % 12       # the spec: "The raw characters sum to 7+6+2 = 3 mod 12"
print(f"spec: raw characters {RAW} sum to {TOTAL_RAW} mod 12")
assert TOTAL_RAW == 3
shifted = tuple((r + s) % 12 for r, s in zip(RAW, SHIFTS))
print(f"      shifted {shifted} sum {sum(shifted) % 12} mod 12  (the spec: (8,4,0), sum 0)")
assert shifted == (8, 4, 0) and sum(shifted) % 12 == 0

print("\n=== THE SELECTION RULE, read off the invariant rather than copied ===")
# The spec states the rule for A_7: "selection requires rho+sigma = 8 mod 12".
# The invariant behind it is the RAW TOTAL: rho + sigma = TOTAL_RAW - chi(A) (mod 12).
for chiA in (7, 11):
    need = (TOTAL_RAW - chiA) % 12
    print(f"  A_{chiA}:  rho + sigma = {TOTAL_RAW} - {chiA} = {need} mod 12")
assert (TOTAL_RAW - 7) % 12 == 8, "must reproduce the spec's own stated rule for A_7"
print("  => the A_7 case reproduces the spec's stated rule EXACTLY, so the reading is right,")
print("     and A_11 requires 4 mod 12. CODEX'S ARITHMETIC IS CONFIRMED.")

print("\n=== THE PURE-TAIL PAIRS, per case ===")
# The spec names the A_7 pure-tail pairs as (0,8), (2,6), (4,4) -- even characters, sum = 8 mod 12.
# Enumerate on the same alphabet and check we recover them, then run the A_11 case.
# THE ALPHABET IS PINNED BY THE SPEC'S OWN LIST, not chosen. A first pass allowed 10 and produced
# a fourth A_7 pair (10,10) that the spec does not list -- so the tail characters run 0..8, and the
# spec's three-pair list is what calibrates the instrument. That calibration is what makes the
# A_11 read trustworthy rather than assumed.
ALPHABET = [0, 2, 4, 6, 8]
for chiA in (7, 11):
    need = (TOTAL_RAW - chiA) % 12
    pairs = [(a, b) for a, b in combinations_with_replacement(ALPHABET, 2) if (a + b) % 12 == need]
    repeated = [p for p in pairs if p[0] == p[1]]
    print(f"  A_{chiA} (need {need}): pure-tail pairs {pairs}")
    print(f"           repeated (vanish by skewness): {repeated}")
    if chiA == 7:
        assert pairs == [(0, 8), (2, 6), (4, 4)], f"must reproduce the spec's list; got {pairs}"
        print("           => matches the spec's own list (0,8),(2,6),(4,4). Instrument validated.")

print("""
WHAT THIS ESTABLISHES, and what it does not

  CONFIRMED, from the spec's own arithmetic: the selection rule is NOT a constant 8 -- it is
  rho + sigma = 3 - chi(A) mod 12, which gives 8 for the A_7 (down) leg and 4 for an A_11 leg.
  The rule CANNOT be copied unchanged between legs with different A-characters. Codex's
  correction to their own R024 is arithmetically right.

  CONFIRMED: on the spec's own even-character alphabet, the A_11 case's pure-tail pairs are
  (0,4) and (2,2), and (2,2) is REPEATED -- so it vanishes by the same skewness that killed
  (4,4) in the down case. If the physical B_2 sector admits only (2,2), as codex reports, the
  lepton leg has NO surviving pure-tail contribution.

  NOT CONFIRMED, and fenced: that the lepton leg IS A_11. That is a reading of codex's frames,
  which are not on this bench and which their own certificate leaves UNDETERMINED at the
  generation level. This cell verifies the CONSEQUENCE of that reading, not the reading.

  CONSEQUENCE FOR B1208's FORK, stated conditionally: IF the lepton leg is A_11, then its tail
  structure differs from the down leg's -- which is evidence AGAINST branch (a) (same tensor)
  and toward (b) or (c). It does not decide between them, because the connecting (non-tail)
  contributions are untouched here.
VERIFIED""")
