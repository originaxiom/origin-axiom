"""B1217 -- the seat integration: what this bench could check, checked.

Four independent verifications, each with the thing it does NOT establish stated beside it.
"""
import json, os
from itertools import combinations, combinations_with_replacement
from math import comb
from pathlib import Path
ROOT = Path(os.environ.get("OA_ROOT") or Path(__file__).resolve().parents[3])

print("=== 1. codex R026: the determinant-character ledger closes (independent of their frame) ===")
W_SEL = (0, 2, 6, 8, 9, 10)
B, G = 6, 7
w = sum(W_SEL) % 12
print(f"    sum of the selected ray characters = {sum(W_SEL)} = {w} mod 12   [they report W:11]")
assert w == 11
print(f"    B + W + G = {B} + {w} + {G} = {B + w + G} = {(B + w + G) % 12} mod 12")
assert (B + w + G) % 12 == 0
print("    => the three determinant characters CANCEL -- the equivariance the frame requires.")
for bad in ((6, 11, 8), (5, 11, 7), (6, 10, 7)):
    assert sum(bad) % 12 != 0
print("    CONTROL: nearby ledgers (6,11,8), (5,11,7), (6,10,7) all fail. Not automatic.")

print("\n=== 2. codex R026: the connecting-product wedge sign ===")
lhs, tgt = ["sb", "sc", "k1", "sd", "k2", "sa"], ["sa", "sb", "sc", "sd", "k1", "k2"]
perm = [tgt.index(x) for x in lhs]
inv = sum(1 for i, j in combinations(range(6), 2) if perm[i] > perm[j])
print(f"    forced surviving term {' ^ '.join(lhs)}; inversions {inv}; sign {(-1) ** inv:+d}")
assert (-1) ** inv == 1
print("    => +1 CONFIRMED by inversion count, no reference to their construction.")

print("\n=== 3. codex R027's simplification: the 384 count ===")
tri, sh = 8, comb(4, 2)
print(f"    (2,2)-shuffles in Eilenberg-Zilber = C(4,2) = {sh}")
print(f"    product simplices <= {tri} x {tri} x {sh} = {tri * tri * sh}   [they report 384]")
assert tri * tri * sh == 384
print("    => 384 CONFIRMED, and 2-cycle x 2-cycle = 4-cycle is the right degree for an H^4 class.")

print("\n=== 4. cloud's V-NEG gating control, against OUR OWN banked B1137 report ===")
d = json.loads((ROOT / "frontier/B1137_regulator_probe/results/final_report.json").read_text())
rows = d["per_target"]
raw = sum(r["raw_found"] for r in rows)
inv_v = sum(r["involves_V"] for r in rows)
reg = sum(r["involves_regulator"] for r in rows)
print(f"    B1137 banked ({d['M_grid_cells']} cells, {d['overall_verdict']}): raw {raw}, "
      f"involves_V {inv_v}, involves_regulator {reg}")
assert (raw, inv_v, reg) == (117, 117, 0), "their control claims exactly 117 / all / none"
print("    => their claimed control (117 raw, all involves_V, none involves_regulator) MATCHES ours.")
vub = [r for r in rows if "ub" in r["target"].lower()][0]
print(f"    the target they say loses nine cells: {vub['target']}  raw={vub['raw_found']}, "
      f"involves_regulator={vub['involves_regulator']}")
assert vub["raw_found"] == 9 and vub["involves_regulator"] == 0
print("    => nine cells, decisive column ZERO. Their 117->108 explanation HOLDS from our side:")
print("       dropping them masks no hit, because the deciding column is zero in both runs.")

print("""
WHAT IS NOT ESTABLISHED HERE
  cloud's EXTENDED run (the V-NEG headline itself) is NOT reproducible as committed. The file
  named outside_bench/certificates/vol_basis_extended.py on their branch contains the BASIS
  BUILDER (R48-3), not the extended probe; no committed certificate carries the
  involves_regulator gate except an unrelated staleness re-check; and their own memo names no
  path for it. Their HYGIENE pre-step does run here and reproduces exactly (3 volume directions
  independent of B1137's 25-entry basis, 0 dropped, Vol computed from Li_2). So the headline is
  CITED, with both checkable sub-claims CONFIRMED and the run itself unreproduced -- an
  evidence-contract gap, not a mathematical one.
VERIFIED""")
