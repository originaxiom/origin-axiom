"""Referee's read-only check of the 2026-10-15 corrections against post_hoc_invariant_masses.json and lagrange_law.json."""
import json, re

SEL = "<repo>/relays/chat1_2026-10-14_selection/"
raw = open(SEL + "post_hoc_invariant_masses.json").read()
ph = json.loads(raw)
rows = ph["rows"]
ll = json.load(open(SEL + "lagrange_law.json"))

print("top keys:", list(ph.keys()))
print("P1 keys:", list(ph["P1"].keys()))
print("count of the duplicated key string in the raw JSON text:", raw.count('"their worst old-vs-new difference"'))
print("P1 value:", ph["P1"]["their worst old-vs-new difference"])

def rots(w): return {w[k:] + w[:k] for k in range(len(w))}
def refl(w):
    R = rots(w)
    return w[::-1] in R or w.translate(str.maketrans("LR", "RL")) in R

short = [w for w in rows if rows[w]["length"] <= 8]
long_ = [w for w in rows if rows[w]["length"] > 8]
print("rows:", len(rows), " length<=8:", len(short), " long:", long_)
print("JSON flag agrees with referee's symmetry test:", all(rows[w]["reflection-symmetric"] == refl(w) for w in rows))
sym = [w for w in short if rows[w]["reflection-symmetric"]]
non = [w for w in short if not rows[w]["reflection-symmetric"]]
print("sym<=8:", len(sym), " non<=8:", len(non), " sym incl long:", sum(rows[w]["reflection-symmetric"] for w in rows))

adm = [w for w in short if rows[w]["admitted (new)"]]
sym_adm = [w for w in sym if rows[w]["admitted (new)"]]
sym_un = [w for w in sym if not rows[w]["admitted (new)"]]
print("admitted:", len(adm), " sym admitted:", len(sym_adm), " sym unadmitted:", len(sym_un), " non admitted:", sum(rows[w]["admitted (new)"] for w in non))

print("\n-- symmetric (51) --")
print("max Im K/|K| over 51:", max((rows[w]["max|Im K|/|K|"], w) for w in sym))
print("max old-vs-new over 51:", max((rows[w]["old vs new, worst relative"], w) for w in sym))
print("max Im Y/|Y| over 41 admitted:", max((rows[w]["max|Im Y|/|Y|"], w) for w in sym_adm))
print("max Im Y/|Y| over 10 unadmitted:", max((rows[w]["max|Im Y|/|Y|"], w) for w in sym_un))
print("N256 vs N384 (new form) over 10 unadmitted:", sorted(((round(rows[w]["new N256 vs N384"], 4), w) for w in sym_un), reverse=True))
print("Im K over 10 unadmitted:", max((rows[w]["max|Im K|/|K|"], w) for w in sym_un))
print("y_max of unadmitted:", sorted((round(rows[w]["y_max"], 4), w) for w in sym_un))

print("\n-- non-symmetric (18) --")
print("Im K/|K| range:", min((rows[w]["max|Im K|/|K|"], w) for w in non), max((rows[w]["max|Im K|/|K|"], w) for w in non))
print("Im Y/|Y| max:", max((rows[w]["max|Im Y|/|Y|"], w) for w in non), " min:", min((rows[w]["max|Im Y|/|Y|"], w) for w in non))
print("old vs new max:", sorted(((rows[w]["old vs new, worst relative"], w) for w in non), reverse=True)[:3])

print("\n-- long words --")
for w in long_:
    r = rows[w]
    print(w, len(w), "sym" if r["reflection-symmetric"] else "non", "old-vs-new %.3g" % r["old vs new, worst relative"],
          "ImK %.2g ImY %.2g" % (r["max|Im K|/|K|"], r["max|Im Y|/|Y|"]), "N-agree %.2g" % r["new N256 vs N384"], "adm", r["admitted (new)"])

print("\n-- the 12 threads of length <= 5 --")
tf = [w for w in short if len(w) <= 5]
print(len(tf), tf)
print("max Im K:", max((rows[w]["max|Im K|/|K|"], w) for w in tf))
print("max Im Y:", max((rows[w]["max|Im Y|/|Y|"], w) for w in tf))
print("all symmetric:", all(rows[w]["reflection-symmetric"] for w in tf))
print("deepest (max y):", max((rows[w]["y_max"], w) for w in tf))

print("\n-- reversal words (P3 vs docstring's 'seven') --")
p3 = ph["P3"]
print("P3 holds", len(p3), "entries:", list(p3.keys()))
rev_words = [w for w in p3 if len(w) <= 8]
print("P3 entries of length <= 8 (the reversal words):", rev_words, len(rev_words))
print("their old-vs-new:", [(w, "%.3g" % p3[w]["old vs new, worst relative"]) for w in rev_words])
print("LLR in rows:", "LLR" in rows, rows["LLR"]["old vs new, worst relative"])

print("\n-- LL cells: invariant vs sealed (lagrange_law.json) --")
print("post hoc P2:", ph["P2"])
def find(d, pat, path=""):
    out = []
    if isinstance(d, dict):
        for k, v in d.items():
            p = path + "/" + str(k)
            if re.search(pat, str(k)): out.append((p, v if not isinstance(v, (dict, list)) or len(str(v)) < 200 else str(v)[:200]))
            out += find(v, pat, p)
    return out
print("lagrange_law.json top keys:", list(ll.keys()))
for k in ("cells", "LL1", "LL2", "LL3", "LL4", "LL5", "Q0"):
    if k in ll: print(k, json.dumps(ll[k])[:400])
for p, v in find(ll, r"RMS|Spearman|largest|violation"):
    print("  ", p, v)
