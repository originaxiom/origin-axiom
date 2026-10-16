"""The three exact symmetries the replication accounts for, checked on T-low's sealed output (09f41b453, read after its
read-out: post hoc on old data; no fresh configuration is touched):
  (a) the configuration classes of classes.py equal the partition of T-low's 90 configurations by bitwise-identical
      masses (every assignment, both readings, every cell);
  (b) every pair of T-low's nulls related by q -> -q has bitwise-identical singular values on every configuration,
      reading and cell;
  (c) at each order, the members of every orbit q -> k.q mod N (k a unit) have identical per-field mass multisets over
      the order's configurations (single-sector entries; the pre-seal review's line-mapped check of whole cells, 1.49M
      cells bitwise identical, is the stronger form).
Usage: python3 -B symmetry_check_on_tlow.py <decompressed twisted_units_seal_output.json> > symmetry_check_on_tlow_run.txt
"""
import hashlib, json, os, sys
from classes import orbit

HERE = os.path.dirname(os.path.abspath(__file__))
TU = os.path.join(HERE, "..", "chat1_2026-10-15_route", "twisted_units")

o = json.load(open(sys.argv[1]))
recs = o["records"]

# (a)
groups, pred = {}, {}
for r in recs:
    h = hashlib.sha256()
    for k in sorted(r["cells"]):
        c = r["cells"][k]
        h.update((k + (repr(c["s"]) if c else "none")).encode())
    groups.setdefault(h.hexdigest(), []).append((r["N"], r["word"], tuple(r["line"])))
    pred.setdefault((r["N"], orbit(r["word"], r["line"], r["N"])), []).append((r["N"], r["word"], tuple(r["line"])))
obs = sorted(sorted(g) for g in groups.values())
prd = sorted(sorted(g) for g in pred.values())
print(f"(a) configuration classes: observed {len(obs)}, predicted {len(prd)}, identical partition: {obs == prd}")

# (b)
draws = json.load(open(os.path.join(TU, "null_draws.json")))["draws_in_order"][:199]
index = {tuple(sorted(d.items())): i for i, d in enumerate(draws)}
pairs = []
for i, d in enumerate(draws):
    j = index.get(tuple(sorted((k, -v) for k, v in d.items())))
    if j is not None and i < j:
        pairs.append((f"null{i:03d}", f"null{j:03d}"))
worst_mismatch = 0
for r in recs:
    for a, b in pairs:
        for k, c in r["cells"].items():
            name, rest = k.split("|", 1)
            if name != a:
                continue
            c2 = r["cells"].get(f"{b}|{rest}")
            if (c is None) != (c2 is None) or (c is not None and c["s"] != c2["s"]):
                worst_mismatch += 1
print(f"(b) sign-flip pairs among T-low's 199 nulls: {len(pairs)}; configuration-cells where a pair's singular values "
      f"differ (bitwise): {worst_mismatch}")

# (c) unit scaling: in the per-field reading masses(k.q, line) = masses(q, k.line) for a unit k mod N, and each order's
# closing set is closed under line scaling, so an assignment's multiset of masses over an order's configurations is
# constant on its orbit q -> k.q mod N. Checked on T-low's per-field output; then the orbit counts of the replication's
# 112 distinct nulls.
import math
FIELDS = ("Q", "u", "d", "L", "e", "H")
def unit_orbit(q, N):
    r = [q[f] % N for f in FIELDS]
    return min(tuple((k * x) % N for x in r) for k in range(1, N) if math.gcd(k, N) == 1)
allq = {"SM": {"Q": 1, "u": -4, "d": 2, "L": -3, "e": 6, "H": 3}}
allq.update({f"null{i:03d}": d for i, d in enumerate(draws)})
for N in (9, 11, 12):
    ms = {}
    for r in recs:
        if r["N"] != N:
            continue
        for k, c in r["cells"].items():
            name, reading, sec, cell = k.split("|")
            if reading != "per-field":
                continue
            ms.setdefault(name, []).append(f"{sec}|{cell}|{c['s'] if c else None}")
    h = {n: hashlib.sha256("\n".join(sorted(v)).encode()).hexdigest() for n, v in ms.items()}
    orbits = {}
    for n, q in allq.items():
        orbits.setdefault(unit_orbit(q, N), []).append(n)
    split = sum(1 for mem in orbits.values() if len({h[m] for m in mem}) > 1)
    multi = sum(1 for mem in orbits.values() if len(mem) > 1)
    sm_shares = [n for n in orbits[unit_orbit(allq["SM"], N)] if n != "SM"]
    print(f"(c) N = {N}: T-low's 200 assignments in {len(orbits)} unit orbits ({multi} with two or more members); orbits "
          f"whose members' per-field mass multisets differ: {split}; nulls sharing the SM's orbit: {len(sm_shares)}")
seal_nulls = []
seen = set()
for d in json.load(open(os.path.join(TU, "null_draws.json")))["draws_in_order"]:
    key = tuple(sorted(d.items())); neg = tuple(sorted((k, -v) for k, v in d.items()))
    if key in seen or neg in seen:
        continue
    seen.add(key); seal_nulls.append(d)
print(f"(c) the replication's {len(seal_nulls)} distinct nulls fall into unit orbits: " + ", ".join(
    f"N = {N}: {len({unit_orbit(q, N) for q in seal_nulls})}" for N in (9, 11, 12)) +
    f"; jointly over the three orders: {len({tuple(unit_orbit(q, N) for N in (9, 11, 12)) for q in seal_nulls})}")
