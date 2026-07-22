"""Fast, independent recheck of B399's 'gate 0' sum-rule (e1=0) using the ALREADY-BANKED
F_p residue data in singles_1215.json + singles_1215_p3.json (read-only inputs from the
origin-axiom repo). Does NOT redo the ~2.5h F_p matrix computation -- just re-sums the
already-computed per-prime residues, exactly like identify_1215_triple.py's 'gate 0' check."""
import json

files = ["singles_1215.json", "singles_1215_p3.json", "singles_1215_p456.json",
         "singles_1215_p7_10.json", "singles_1215_p11_20.json", "singles_1215_p14_20.json"]
BASE = "<cc2-seat>/origin-axiom/frontier/B399_wall_scale/"
DATA = {}
for f in files:
    try:
        DATA.update(json.load(open(BASE + f)))
    except FileNotFoundError:
        pass

CELLS = (121, 256, 391)
primes = sorted(map(int, DATA))
print(f"{len(primes)} primes available: {primes}")
all_zero = True
for p in primes:
    vals = [int(DATA[str(p)][str(c)]) for c in CELLS]
    s = sum(vals) % p
    ok = (s == 0)
    all_zero &= ok
    print(f"  p={p}: triple values {vals} ; sum mod p = {s} -> {'ZERO (sum rule holds)' if ok else 'NONZERO — FAILS'}")

# also the FULL 24-cell support sum (all keys in one prime's dict) == 1 check, first prime
p0 = primes[0]
full = DATA[str(p0)]
total = sum(int(v) for v in full.values()) % p0
print(f"\nfull 24-cell support sum mod p={p0}: {total} (expect 1)")
print(f"\ne1 = 0 confirmed across ALL {len(primes)} independently-banked primes: {all_zero}")
