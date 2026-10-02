#!/usr/bin/env python3
"""The sealed reader: answers P1-P5 of the preregistration from grid_index.json and B1419's census."""
import sys, json, pathlib, collections
HERE = pathlib.Path(__file__).resolve().parent
name = sys.argv[1] if len(sys.argv) > 1 else "grid_index.json"
rows = json.load(open(HERE / name))["rows"]
cen = [json.loads(l) for l in open(HERE.parents[1] / "B1419_the_arithmetic_fillings_corrected" / "verification" / "arithmetic_census_closed.jsonl")]
hyp = {tuple(r["slope"]): r.get("hyperbolic") is True for r in cen}
ARITH = {(5, 1), (-5, 1), (6, 1), (-6, 1), (8, 1), (-8, 1)}
assert ARITH == {tuple(r["slope"]) for r in cen if r.get("arithmetic") is True}
S = {tuple(r["slope"]): (None if r["series"] is None else {int(k): v for k, v in r["series"].items()}) for r in rows}
have = [s for s in S if s in hyp]; H = [s for s in have if hyp[s]]; E = [s for s in have if not hyp[s]]
def show(d):
    if d is None: return "undefined"
    return " ".join("%+d q^%s" % (v, k // 2 if k % 2 == 0 else "%d/2" % k) for k, v in sorted(d.items())) or "0"
def val(d):
    k = min(k for k in d if k > 0); return k, d[k]
print("slopes read: %d (%d hyperbolic, %d exceptional)" % (len(have), len(H), len(E)))
# P1
good = [s for s in H if S[s] is not None and S[s].get(0) == 1 and min(S[s]) == 0 and len(S[s]) > 1]
print("P1  defined, constant term 1, no negative exponent, non-constant: %d of %d hyperbolic slopes" % (len(good), len(H)))
for s in H:
    if s not in good: print("     exception", s, show(S[s]))
# P2
print("P2  exceptional slopes:")
for s in sorted(E): print("     ", s, show(S[s]))
# P3
pairs = [(s, (-s[0], s[1])) for s in have if s[0] > 0 and (-s[0], s[1]) in S]
same = [a for a, b in pairs if S[a] == S[b]]
print("P3  mirror pairs with identical series: %d of %d" % (len(same), len(pairs)))
# P4
feats = {"valuation of I - 1 (in q)": lambda d: val(d)[0] / 2, "its coefficient": lambda d: val(d)[1],
         "(valuation, coefficient)": lambda d: (val(d)[0] / 2, val(d)[1]), "half-integer exponents occur": lambda d: any(k % 2 for k in d),
         "coefficient of q": lambda d: d.get(2, 0), "coefficient of q^2": lambda d: d.get(4, 0)}
print("P4  features on the %d arithmetic and the %d other hyperbolic slopes:" % (len([s for s in good if s in ARITH]), len([s for s in good if s not in ARITH])))
nsep = 0
for nm, f in feats.items():
    a = collections.Counter(f(S[s]) for s in good if s in ARITH); b = collections.Counter(f(S[s]) for s in good if s not in ARITH)
    sep = not (set(a) & set(b)); nsep += sep
    print("     %-32s arithmetic %s | others %s | %s" % (nm, dict(sorted(a.items(), key=str)), dict(sorted(b.items(), key=str)), "SEPARATES" if sep else "does not separate"))
print("     features that separate: %d of %d" % (nsep, len(feats)))
# P5
cls = collections.defaultdict(list)
for s in good:
    if s[0] > 0: cls[tuple(sorted(S[s].items()))].append(s)
multi = [v for v in cls.values() if len(v) > 1]
print("P5  slopes with p > 0: %d, distinct series to q^10: %d; classes of more than one slope: %d" % (sum(len(v) for v in cls.values()), len(cls), len(multi)))
for v in multi: print("     ", v, "ARITHMETIC MEMBER" if any(s in ARITH for s in v) else "")
print("     an arithmetic slope shares its series with another slope (not its mirror):", any(any(s in ARITH for s in v) for v in multi))
for s in sorted(ARITH):
    if s[0] > 0: print("     ", s, show(S[s]))
