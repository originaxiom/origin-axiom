"""B1026 -- the nomination scoring (sealed 7e798db1). DATA-BLIND: no measured value
appears anywhere in this file. Deterministic: grade + priced bits, lowest wins, cap 3.0."""
import math

log2 = lambda n: math.log2(n)

# The inventory (grade: THEOREM = 0, observed-law = 1) and the kind classes.
# Structural selectors (each MUST cite a banked reason) reduce priced choices.
PAIRINGS = []

def price(name, grade, object_choices, object_selector, target_choices, target_selector, notes):
    bits = 0.0
    if object_selector is None:
        bits += log2(object_choices)
    if target_selector is None:
        bits += log2(target_choices)
    PAIRINGS.append({"pairing": name, "grade": grade, "priced_bits": round(bits, 3),
                     "score": round(grade + bits, 3),
                     "object_selector": object_selector, "target_selector": target_selector,
                     "notes": notes})

# T4 <-> Phi (phases). Object: {0, +2pi/3, -2pi/3}. Selector: "the nontrivial chi values"
# (banked: chi != 1 iff A not in ker chi -- B1011's forced-criterion structure) -> the
# conjugate pair {+-2pi/3}; the SIGN remains a genuine choice (1 bit; the orientation input
# is a bit of the price, but USING it here is a pairing choice -> priced). Targets: 2 deltas
# (leptonic, quark), no banked selector -> 1 bit.
price("T4 phases <-> delta_CP", grade=0,
      object_choices=2, object_selector=None,          # the +- sign: 1 bit
      target_choices=2, target_selector=None,          # which delta: 1 bit
      notes="object set reduced to {+-2pi/3} by the banked nontriviality selector (0 bits); "
            "sign 1 bit + sector 1 bit = 2.0")

# T2 <-> P (probabilities). Object: {1/(phi sqrt5), phi/sqrt5, 1}; "1" excluded by the
# kind's own bounds as a mixing probability (a probability of exactly 1 is not a mixing
# angle -- structural). Remaining 2 values. N4 kills (smallest <-> solar theta12). Remaining
# admissible: 2 values x {theta13, theta23} minus nothing = 2x2 = 4 combos -> 2 bits; grade
# observed-law +1.
price("T2 |h|^2 <-> sin^2(theta)", grade=1,
      object_choices=2, object_selector=None,
      target_choices=2, target_selector=None,
      notes="'1' excluded structurally; theta12 dead (N4); 2x2 remaining = 2.0 bits; grade +1")

# T1 <-> A (amplitude moduli). Object: 5 tones, no banked selector names one; targets: 3
# moduli, no selector. log2(5)+log2(3) = 3.907 > cap even at THEOREM grade.
price("T1 tones <-> |V_ij|", grade=0,
      object_choices=5, object_selector=None,
      target_choices=3, target_selector=None,
      notes="no banked selector on either side")

# T3 mirror set <-> A: 15 signed values -> 8 magnitudes {0,1/4,1/(4phi),1/2,1/(2phi),phi/4,
# phi/2,1}; no selector; targets 3.
price("T3 mirror <-> |V_ij|", grade=0,
      object_choices=8, object_selector=None,
      target_choices=3, target_selector=None,
      notes="the never-compared sector, but no banked selector -> expensive")

# T5 h(5) = -1: EXCLUDED AT N1. The sealed inventory types T5 as "signed amplitude";
# docs/KIND_TABLE.md licenses NO signed-amplitude <-> modulus pairing (the licensed A-row is
# |tone|-type magnitudes). A first draft of this script included T5 <-> |V_ij| in violation
# of the sealed N1 and it SCORED FIRST (1.585) -- the seal's kind-exactness clause is what
# stopped a boundary-degenerate nominee (|h| = 1 is a no-mixing datum; the targets are
# mixing data). Kept here as the recorded near-miss: the gate worked against its own author.
print("  [N1] T5 excluded: 'signed amplitude' has no licensed pairing in KIND_TABLE "
      "(a first draft scored it 1.585 and FIRST -- the seal caught it)")

CAP = 3.0
for p in sorted(PAIRINGS, key=lambda r: r["score"]):
    ok = "CLEARS" if p["score"] <= CAP else "over cap"
    print(f"  {p['score']:>5}  {ok:8}  {p['pairing']}  [{p['notes'][:60]}...]")
winners = [p for p in PAIRINGS if p["score"] <= CAP]
winners.sort(key=lambda r: r["score"])
print()
if not winners:
    print("VERDICT: EMPTY")
elif len(winners) > 1 and winners[0]["score"] == winners[1]["score"]:
    print(f"VERDICT: TIE at {winners[0]['score']}:", [w["pairing"] for w in winners if w["score"]==winners[0]["score"]])
else:
    w = winners[0]
    print(f"VERDICT: NOMINATED -- {w['pairing']} at score {w['score']}")
    print(f"  runners-up clearing the cap: {[ (x['pairing'], x['score']) for x in winners[1:] ]}")
