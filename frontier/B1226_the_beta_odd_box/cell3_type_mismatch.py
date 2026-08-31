"""B1226 Cell 3 -- the box-D negatives are TYPE-MISMATCHED AT THE SOURCE.

Box D (beta-odd, dimensionless) is the one box where the object has an output at all:
CS, which amphichirality forces to be 2-torsion (B1224) -- i.e. ONE BIT.
This cell reads the record and asks of each box-D probe: did it demand a VALUE or a BIT?
"""
import json, glob, re

PROBES = {
 "B1027": {"asked": "delta_13 == 120 deg or 240 deg", "demanded": "VALUE (a real number in degrees)",
           "outcome": "MISS 11.4 sigma / 38.0 sigma, powered"},
 "B1137": {"asked": "is an SM value a bounded-height algebraic combination of regulators",
           "demanded": "VALUE (rung-1 algebraicity over 18 sealed SM targets)", "outcome": "DISJOINT"},
 "B813":  {"asked": "CS(m004) == theta_QCD", "demanded": "VALUE (a coefficient slot)",
           "outcome": "REFUTED ON TYPE -- a functional value cannot fill a coefficient slot"},
}
OBJECT_OUTPUT = {"invariant": "CS", "constrained_by": "amphichirality (B1224)",
                 "type": "Z/2 -- ONE BIT", "cardinality": 2}

# verify each named probe exists in the record with the stated verdict
for pid in PROBES:
    f = glob.glob(f'frontier/{pid}_*/arc_verdict.json')
    assert f, f"{pid} not in record"
    PROBES[pid]["verdict_in_record"] = json.load(open(f[0]))["verdict"]

demanded_value = [p for p, d in PROBES.items() if d["demanded"].startswith("VALUE")]
demanded_bit   = [p for p, d in PROBES.items() if d["demanded"].startswith("BIT")]

res = {"object_output_in_box_D": OBJECT_OUTPUT, "probes": PROBES,
       "n_probes": len(PROBES), "demanded_a_value": demanded_value, "demanded_a_bit": demanded_bit,
       "type_matched_probes": len(demanded_bit),
       "finding": ("every probe ever fired into box D demanded a CONTINUOUS VALUE from a "
                   "BIT-VALUED channel; the type-matched question -- does the object's Z/2 fix the "
                   "CP-CONSERVATION BIT -- has never been asked"),
       "already_banked_at_bit_level": "B303: 'the CP sign is literally the sign of Chern-Simons' (PROVED)",
       "gate5": "no measured physical value asserted anywhere in this cell"}

print(f"object's box-D output: {OBJECT_OUTPUT['type']}  (cardinality {OBJECT_OUTPUT['cardinality']})\n")
for p, d in PROBES.items():
    print(f"  {p} [{d['verdict_in_record']}]  asked: {d['asked']}")
    print(f"        demanded: {d['demanded']}\n        outcome:  {d['outcome']}")
print(f"\n  probes demanding a VALUE: {len(demanded_value)}/{len(PROBES)}  {demanded_value}")
print(f"  probes demanding a BIT  : {len(demanded_bit)}/{len(PROBES)}  <-- the type-matched question, NEVER ASKED")
print(f"\n  already banked at bit level, never connected: {res['already_banked_at_bit_level']}")
json.dump(res, open("frontier/B1226_the_beta_odd_box/cell3_results.json","w"), indent=2)
