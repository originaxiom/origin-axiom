"""B385 -- the criterion extraction: property scan on the banked v_word 5-part supports."""
import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
VW = json.load(open(os.path.join(HERE, "vword.json")))

pairs = {k: (v["status"], {tuple(x) for x in v["support"]}) for k, v in VW.items()}

def closed_under(S, f): return all(f(v) in S for v in S)
props = {
    "swap":  lambda v: (v[1], v[0]),
    "neg":   lambda v: ((-v[0]) % 5, (-v[1]) % 5),
    "dbl":   lambda v: ((2*v[0]) % 5, (2*v[1]) % 5),
    "swapneg": lambda v: ((-v[1]) % 5, (-v[0]) % 5),
}
print(f"{'pair':6s} {'status':7s} " + " ".join(f"{n:8s}" for n in props))
feat = {}
for k, (st, S) in pairs.items():
    row = {n: closed_under(S, f) for n, f in props.items()}
    feat[k] = row
    print(f"{k:6s} {st:7s} " + " ".join(f"{str(row[n]):8s}" for n in props))

for n in props:
    b = {feat[k][n] for k, (st, _) in pairs.items() if st == "bright"}
    d = {feat[k][n] for k, (st, _) in pairs.items() if st == "dark"}
    if not (b & d):
        print(f"SEPARATES: {n}  bright={b} dark={d}")

# omega-pairing multiset and diagonal content
def omega(u, v): return (u[0]*v[1] - u[1]*v[0]) % 5
extra = {}
for k, (st, S) in pairs.items():
    diag = sorted(v for v in S if v[0] == v[1])
    anti = sorted(v for v in S if (v[0]+v[1]) % 5 == 0)
    om0 = sum(1 for u in S for v in S if omega(u, v) == 0)
    extra[k] = dict(diag=diag, antidiag=anti, om0=om0, size=len(S))
    print(k, st, "diag:", diag, "antidiag:", anti, f"om0={om0}/{len(S)**2}")
for f in ("diag", "antidiag"):
    b = {str(extra[k][f]) for k, (st, _) in pairs.items() if st == "bright"}
    d = {str(extra[k][f]) for k, (st, _) in pairs.items() if st == "dark"}
    if not (b & d):
        print(f"SEPARATES: {f}  bright={sorted(b)}  dark={sorted(d)}")
