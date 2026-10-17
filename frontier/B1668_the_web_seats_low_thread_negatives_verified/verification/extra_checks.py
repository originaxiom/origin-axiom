import json, pickle, collections, hashlib
d = json.load(open("tu/twisted_units_seal_output.json"))
for i in (35, 3, 56, 23, 84, 15):
    json.dump(d["records"][i], open(f"stored_rec_{i}.json", "w"))
recs = d["records"]
# sign-flip pairs in the null: bitwise identical masses?
nd = json.load(open("tu/null_draws.json"))["draws_in_order"][:199]
print("null draw keys", list(nd[0]))
def key(a): return tuple(sorted(a.items()))
draws = {f"null{i:03d}": {k: int(v) for k, v in x.items()} for i, x in enumerate(nd)}
flip = {k: {f: -q for f, q in a.items()} for k, a in draws.items()}
idx = {key(a): k for k, a in draws.items()}
pairs = [(k, idx[key(f)]) for k, f in flip.items() if key(f) in idx and idx[key(f)] > k]
print("sign-flip pairs inside the 199 nulls:", len(pairs), "distinct outcomes by assignment-up-to-sign:", 199 - len(pairs))
# gauge invariance: check anomaly-type conditions? print first assignment
SM = {"Q": 1, "u": -4, "d": 2, "L": -3, "e": 6, "H": 3}
# masses bitwise identical for flipped pairs?
same = 0
for k, k2 in pairs:
    ok = True
    for r in recs:
        for rd in ("per-field", "minimal"):
            for s in ("up", "down", "lepton"):
                for c in {kk.split("|")[3] for kk in r["cells"] if kk.startswith(f"{k}|{rd}|up|")}:
                    a = r["cells"][f"{k}|{rd}|{s}|{c}"]["s"]; b = r["cells"][f"{k2}|{rd}|{s}|{c}"]["s"]
                    if a != b: ok = False
    same += ok
print("pairs with bitwise-identical singular values over all cells:", same, "of", len(pairs))
# SM -q? (SM negative excluded)
print("SM negated in nulls:", key({f: -q for f, q in SM.items()}) in idx)
# classes: word reversal + L<->R mirror
def canon(w):
    m = w.translate(str.maketrans("LR", "RL")); 
    return min(w, w[::-1], m, m[::-1])
words = collections.defaultdict(list)
for r in recs: words[canon(r["word"])].append(r["index"])
print("distinct words", len({r["word"] for r in recs}), "word classes (reversal+mirror, no rotation)", len(words))
# config classes: (N, word-class, line?) — use identical masses signature
sig = collections.defaultdict(list)
for r in recs:
    s = hashlib.sha256(json.dumps([r["cells"][k]["s"] for k in sorted(r["cells"]) if k.startswith("SM|")]).encode()).hexdigest()
    sig[s].append(r["index"])
print("classes by identical SM singular values (all cells, both readings):", len(sig))
# distinct per-field SM cells
rows = pickle.load(open("tu/mine_rows.pkl", "rb"))
cl = {i: min(v) for v in sig.values() for i in v}
dist_pass = {(cl[w["i"]], w["cell"]) for w in rows if w["name"] == "SM" and w["reading"] == "per-field" and w["ok"] and w["chi_shape"] <= 7.815}
print("SM S-shape passes: distinct (class, cell):", len(dist_pass), "classes:", len({c for c, _ in dist_pass}))
alln = {(cl[w["i"]], w["cell"]) for w in rows if w["name"] == "SM" and w["reading"] == "per-field"}
print("distinct per-field config-cells:", len(alln))
ps = sorted(w["chi_shape"] for w in rows if w["name"] == "SM" and w["reading"] == "per-field" and w["chi_shape"] <= 7.815)[-1]
pf = sorted(w["chi_shape"] for w in rows if w["name"] == "SM" and w["reading"] == "per-field" and w["chi_shape"] > 7.815)[0]
print("SM max passing chi_shape", ps, "min failing", pf)
# class-level p for S-shape: a class 'passes' if any cell passes
cnt = collections.defaultdict(set)
for w in rows:
    if w["reading"] == "per-field" and w["ok"] and w["chi_shape"] <= 7.815: cnt[w["name"]].add(cl[w["i"]])
sm = len(cnt["SM"]); nn = [len(cnt[f"null{i:03d}"]) for i in range(199)]
print("class-level: SM classes with a pass", sm, "p", (1 + sum(x >= sm for x in nn)) / 200, "classes total", len(sig))
