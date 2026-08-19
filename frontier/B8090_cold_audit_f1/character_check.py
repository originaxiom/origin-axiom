#!/usr/bin/env python3
"""B8090 -- COLD AUDIT FINDING 1: B1076's "new exact character" is mis-stated in every
summary surface. The computation is right; the banked claim inverts it and mis-types it.

No recomputation of B1076's algebra is involved. This is a CLAIM-LEVEL check, decidable
from B1076's own record, and it needs only the Klein group's multiplication table.
"""
from fractions import Fraction as F
import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
FAILED = []
def gate(l, ok, d=""):
    print(f"  [{'PASS' if ok else 'FAIL'}] {l}" + (f"  {d}" if d else ""))
    if not ok: FAILED.append(l)

# The four lambda^2 values, transcribed from B1076's OWN b1076_results.json record.
LSQ = {"I":    F(-1),
       "chi_a": -F(746496, 170569),      # = -(864/413)^2
       "chi_b":  F(47775744, 9284209),   # = +(6912/3047)^2
       "D2":     F(5308416, 908209)}     # = +(2304/953)^2
gate("chi_a's lambda^2 is exactly -(864/413)^2", LSQ["chi_a"] == -F(864,413)**2)
gate("chi_b's lambda^2 is exactly +(6912/3047)^2", LSQ["chi_b"] == F(6912,3047)**2)
gate("D2's   lambda^2 is exactly +(2304/953)^2",  LSQ["D2"]   == F(2304,953)**2)

sgn = {k: (1 if v > 0 else -1) for k, v in LSQ.items()}
print(f"\n  sign(lambda^2) as computed = {sgn}")
gate("sign(lambda^2) is negative on {I, chi_a} and positive on {chi_b, D2} -- as BANKED",
     sgn == {"I": -1, "chi_a": -1, "chi_b": 1, "D2": 1})

# Klein four-group multiplication table
E = ["I", "chi_a", "chi_b", "D2"]
MUL = {("I",x): x for x in E} | {(x,"I"): x for x in E} | {
    ("chi_a","chi_a"):"I", ("chi_b","chi_b"):"I", ("D2","D2"):"I",
    ("chi_a","chi_b"):"D2", ("chi_b","chi_a"):"D2",
    ("chi_a","D2"):"chi_b", ("D2","chi_a"):"chi_b",
    ("chi_b","D2"):"chi_a", ("D2","chi_b"):"chi_a"}
def is_hom(f):
    return all(f[a]*f[b] == f[MUL[(a,b)]] for a in E for b in E)

print()
print("=" * 74)
print("THE DEFECT")
print("=" * 74)
gate("a character MUST send the identity to +1 -- sign(lambda^2)(I) = -1 violates this",
     sgn["I"] == -1)
gate("=> sign(lambda^2) is NOT a homomorphism (checked on all 16 products)", not is_hom(sgn))
bad = [(a,b) for a in E for b in E if sgn[a]*sgn[b] != sgn[MUL[(a,b)]]]
print(f"      it fails multiplicativity on {len(bad)} of 16 products, e.g. {bad[:3]}")

# the correct object: normalise by the value at the identity
chi = {k: v * sgn["I"] for k, v in sgn.items()}
print(f"\n  the CORRECT character chi = sign(lambda^2)/sign(lambda^2(I)) = {chi}")
gate("chi IS a homomorphism (all 16 products)", is_hom(chi))
gate("chi is NONTRIVIAL", set(chi.values()) == {1, -1})
gate("chi is TRIVIAL on {I, chi_a} and -1 on {chi_b, D2} -- the OPPOSITE polarity to the bank",
     chi == {"I": 1, "chi_a": 1, "chi_b": -1, "D2": -1})

print()
print("=" * 74)
print("WHERE THE ERROR IS, AND WHERE IT IS NOT")
print("=" * 74)
print("""  B1076's INTERNAL record states it CORRECTLY:
      "character of the Klein four-group B^1, trivial on the subgroup <chi_a>={I,chi_a}
       and equal to -1 on the coset chi_b.<chi_a>={chi_b,D2}"
  Its SUMMARY surfaces state it incorrectly, on three of them:
      FINDINGS.md, arc_verdict.json, CHANGELOG.md all read
      "sign(lambda^2) is a NEW nontrivial character (negative on {I,chi_a}, positive on
       {chi_b,D2})"
  Two errors compounded: (1) sign(lambda^2) is called a CHARACTER when it is -1 at the
  identity and so is not a homomorphism at all; (2) the polarity is INVERTED relative to
  the character the internal record correctly identifies.

  THE COMPUTATION IS NOT IN QUESTION and the arc's NEGATIVE verdict is UNAFFECTED. This
  is a transcription defect in a banked one-line claim -- the class the corpus already
  tracks (headline drifting from the record).""")

RES = {"lambda_sq": {k: str(v) for k, v in LSQ.items()},
       "sign_lambda_sq": sgn, "sign_is_homomorphism": is_hom(sgn),
       "n_failed_products": len(bad),
       "correct_character": chi, "correct_is_homomorphism": is_hom(chi),
       "banked_polarity_matches_character": sgn == chi,
       "defect": "summary-layer only; computation and NEGATIVE verdict unaffected",
       "surfaces_affected": ["FINDINGS.md", "arc_verdict.json", "CHANGELOG.md"],
       "scope": ("A CLAIM-LEVEL check on B1076's own recorded values, using only the Klein "
                 "group multiplication table. Recomputes NONE of B1076's algebra and casts "
                 "no doubt on it. Gate 5 untouched.")}
json.dump(RES, open(os.path.join(HERE, "results.json"), "w"), indent=1, sort_keys=True)
print("\n  results.json written")
if FAILED:
    raise SystemExit(f"FAILED: {FAILED}")
print("\n  ALL CHECKS PASS")
