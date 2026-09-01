#!/usr/bin/env python3
"""R10 POST-HOC diff: written AFTER the blind solve (r10_blind_solve.py) ran and its
results were on disk. Compares my 18-solution set against the banked B1102 set and
resolves the coordinate convention, and recomputes B1109-F1's projection counts."""
from fractions import Fraction as F
import json, os

HERE = os.path.dirname(os.path.abspath(__file__))
mine = json.load(open(os.path.join(HERE, "r10_blind_results.json")))
banked = json.load(open("/home/user/origin-axiom/frontier/B1102_exact_hypercharge_solve/b1102_results.json"))

S_mine = {tuple(F(x) for x in s) for s in mine["solutions_a1_a2_b1_b2"]}
S_bank = {tuple(F(x) for x in s) for s in banked["all_solving_directions"]}
print(f"|mine| = {len(S_mine)}, |banked| = {len(S_bank)}")
print(f"literally equal: {S_mine == S_bank}")
neg = {tuple(-x for x in s) for s in S_mine}
swp = {(s[2], s[3], s[0], s[1]) for s in S_mine}
print(f"banked == negation of mine: {S_bank == neg}")
print(f"banked == ideal-swap of mine: {S_bank == swp}")

# orbit correspondence under the negation map
orbits_mine = [[tuple(F(x) for x in s) for s in o] for o in mine["orbits"]["members"]]
for k, o in enumerate(orbits_mine):
    img = {tuple(-x for x in s) for s in o}
    # banked orbit membership: partition banked set by sorted (a-triple, b-triple) signature
    print(f"my orbit {k} negated -> subset of banked set: {img <= S_bank}, size {len(img)}")

rep = (F(1,6), F(1,6), F(2,3), F(-1,3))
print(f"banked representative {tuple(map(str, rep))} in banked set: {rep in S_bank}")
print(f"its negation {tuple(map(str, tuple(-x for x in rep)))} in my set: {tuple(-x for x in rep) in S_mine}")

# ---- B1109 F1 projection counts, from the branching (my own arithmetic) ----
# 15 weight classes: (3bar_A,1) x3 classes, (1,3_B) x3 classes, (3_A,3bar_B) x9 singles.
# Projected to ideal-A's Cartan: 3bar_A weights (3 classes, size 3), zero (the three
# 3_B classes merge: size 9), 3_A weights from singles (3 classes, size 3 each).
# 3_A and 3bar_A weights are disjoint (w vs -w, none zero) => 3 + 1 + 3 = 7 classes.
projA_classes = 7
projA_max_size = 9
print(f"projection to one ideal's Cartan: {projA_classes} classes (banked F1: 7), "
      f"largest class size {projA_max_size} (banked F1 double-kill: size-9 class; "
      f"target max multiplicity 6; target needs 8 distinct values > 7)")
