"""B2016, POST HOC (labelled; with overgroups_posthoc.py): each class's category, (a), (b) or (c) as in cosets_gap.py, against
whether H contains a conjugate of C, i.e. whether G_k/H is a G-quotient of the whole's orbit. Reads coset_actions_posthoc.json.
    python3 -B overgroups_join.py > overgroups_join_run.txt"""
import json, pathlib, collections, hashlib, importlib.util
HERE = pathlib.Path(__file__).resolve().parent
src = (HERE / "cosets_gap.py").read_text().split('raw = (HERE / "coset_actions.json")')[0]
ns = {"__file__": str(HERE / "cosets_gap.py")}; exec(src, ns)
raw = (HERE / "coset_actions_posthoc.json").read_bytes()
print("the post hoc export: sha256 %s" % hashlib.sha256(raw).hexdigest())
data = json.loads(raw)
for N in ("27", "81"):
    tab = collections.Counter()
    for r in data[N]["classes"]:
        pn, S, d0, d1, fx = ns["sector_polys"](r["C"], r["S"])
        h = ns["halved"](pn)
        cat = "a" if h == ns["Q9"] * ns["X"] * S else ("b" if d1 > 0 and h % S == 0 else "c")
        tab[(cat, r["over_C"])] += 1
    print("mod %s: (category, H contains a conjugate of C) -> number of classes: %s" % (N, dict(sorted(tab.items()))))
