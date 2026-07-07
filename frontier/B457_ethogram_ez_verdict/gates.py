#!/usr/bin/env python3
"""B457 (Ethogram EZ) — the two typed gates on the FROZEN catalog + the campaign verdict.

EZ-1 (specificity, behavior vs behavior): per object signature, p1 = frequency among null
catalogs; p-values licensed ONLY on the word channel (n=1000 random words); knot/class channels
get forced/laundered adjudication (banked in the source probes).
EZ-2 (correspondence, number vs number): the numeric parts of the object signatures against the
frozen registry (B398 machinery: 1-sigma windows, 2000-draw null, binding p<0.01).
Structural predicates: joint-only; can never fire H1 alone (frozen rule).
"""
import hashlib
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "B452_ethogram_dictionary"))
from registry import ez1_specificity, ez2_correspondence, structural_joint, signature

FROZEN = os.path.join(HERE, "..", "B456_ethogram_e4_catalog", "catalog_frozen.json")
data = json.load(open(FROZEN))
payload = {k: v for k, v in data.items() if k != "sha256"}
txt = json.dumps(payload, sort_keys=True)
h = hashlib.sha256(txt.encode()).hexdigest()
assert h == data["sha256"], "catalog hash mismatch - the freeze is broken"
print(f"freeze verified: sha256 = {h[:16]}...")

def unpack(entry):
    ints, discs, values, kind = entry
    return signature(kind, ints, discs, values)

obj = [unpack(e) for e in data["object_catalog"]]
nulls = {name: [unpack(e) for e in cat] for name, cat in data["nulls"].items()}
word_nulls = [cat for name, cat in nulls.items() if name.startswith("rand") or name == "thue-morse"]
knot_nulls = [cat for name, cat in nulls.items() if name in ("5_2", "6_1", "silver")]

print(f"\n== EZ-1: word-channel specificity (licensed: n={len(word_nulls)}) ==")
word_sigs = [s for s in obj if s[0] in ("word-closure-lemma", "dynamics-disc", "pulse-cocycle-2cycle")]
# the object's dynamics-disc signature: tr=3, disc 5 (the golden word product R L -> [[2,1],[1,1]])
word_sigs.append(signature("dynamics-disc", ints=(3,), discs=(5,)))
r1 = ez1_specificity(word_sigs, word_nulls, licensed=True)
for s, res in r1.items():
    print(f"  {s[0]:28s} ints={s[1]} discs={s[2]}: p1={res['p1']:.4f}  fires={res['fires']}")

print(f"\n== EZ-1: knot/class channels (adjudication-only, n={len(knot_nulls)} - no p-values) ==")
for s in obj:
    present = sum(1 for cat in knot_nulls if s in cat)
    note = "shared-with-null" if present else "object-only (adjudicated forced/laundered in source probe)"
    print(f"  {s[0]:34s}: in {present}/{len(knot_nulls)} controls -> {note}")

print("\n== EZ-2: numeric correspondence (B398 machinery, binding p<0.01) ==")
r2 = ez2_correspondence(obj)
print(f"  numbers entering: {r2['n_numbers']}  hits: {r2['hits']}  null mean: {r2['null_mean']:.2f}"
      f"  null p99: {r2['null_p99']:.0f}  p = {r2['p']:.4f}  FIRES: {r2['fires']}")

print("\n== structural predicates (joint-only) ==")
s3 = structural_joint(obj, list(nulls.values()))
print(f"  satisfied: {s3['satisfied']}   can_fire_alone: {s3['can_fire_alone']}")

print("\n== THE VERDICT ==")
any_h1 = r2["fires"]
print(f"  EZ-2 fires: {r2['fires']}   ->  H1: {'CANDIDATE - ESCALATE' if any_h1 else 'NO'}")
if not any_h1:
    print("  H0a EARNED: the behavior catalog is class-generic or whitelist-laundered at every")
    print("  gate; the ethogram banks as the object's behavioral map.")
