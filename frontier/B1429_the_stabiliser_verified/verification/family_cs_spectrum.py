"""The family's CS spectrum, in the group CS actually lives in for a cusped manifold.

SnapPy returns the Chern-Simons invariant of a cusped hyperbolic manifold modulo 1/2. So a value that is
a multiple of 1/12 lives in (1/12)Z / (1/2)Z, which is Z/6 -- NOT Z/12. Reading residues mod 12 reads a
representative, not a class. This does both, so the normalisation is visible rather than assumed.
"""
import json
import pathlib
import warnings
from collections import Counter

warnings.filterwarnings("ignore")
import snappy

ROOT = pathlib.Path(__file__).resolve().parents[3]
fam = json.load(open(ROOT / "frontier" / "B1186_family_is_112" / "verification"
                     / "family_census.json"))["members_B"]
r12, r6 = {}, {}
for name in fam:
    c = float(snappy.Manifold(name).chern_simons()) % 0.5     # the class, not a representative
    x = 12 * c
    if abs(x - round(x)) > 1e-6:
        continue
    r12[name] = round(x) % 12
    r6[name] = round(x) % 6

hit12, hit6 = sorted(set(r12.values())), sorted(set(r6.values()))
print("integral 12*CS: %d of %d" % (len(r12), len(fam)))
print("as a representative mod 12 : %s   (%d of 12)" % (hit12, len(hit12)))
print("as a CLASS in Z/6 (=CS mod 1/2 in twelfths): %s   -> SURJECTIVE: %s"
      % (hit6, len(hit6) == 6))
print("counts in Z/6:", dict(sorted(Counter(r6.values()).items())))

fixed6 = [r for r in range(6) if (-r) % 6 == r]
print()
print("the orientation/order bit acts as r -> -r; on Z/6 it fixes exactly %s" % fixed6)
print("so of the 6 classes the family realises, %d are MOVED by it"
      % len([r for r in hit6 if r not in fixed6]))
print("and on the 2-element sister orbit {0, 1/4} = classes {0, 3} it fixes BOTH -- those are precisely")
print("the fixed points, so the two bits are invisible there and visible on the wider family.")

n = 0; sm = []
for M in snappy.OrientableCuspedCensus(cusps=1):
    if n >= 600:
        break
    n += 1
    if M.name() in r12:
        continue
    try:
        c = float(M.chern_simons()) % 0.5
    except Exception:
        continue
    if abs(12 * c - round(12 * c)) < 1e-6:
        sm.append(round(12 * c) % 6)
print()
print("control: %d of %d non-family one-cusped census manifolds have CS in twelfths (%.2f%%); classes %s"
      % (len(sm), n, 100.0 * len(sm) / n, sorted(set(sm))))
json.dump({"family_Z6": r6, "hit6": hit6, "surjective_onto_Z6": len(hit6) == 6,
           "hit12_representatives": hit12, "control_percent": 100.0 * len(sm) / n, "control_n": n},
          open(str(pathlib.Path(__file__).resolve().parent / "family_cs_spectrum.json"), "w"), indent=1)
