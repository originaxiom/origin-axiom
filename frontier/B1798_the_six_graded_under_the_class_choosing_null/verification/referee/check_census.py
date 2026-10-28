"""Referee B1798: independent audit of the R71-1 census extension (read-only).
Checks: every line parses; per-row key set equals the committed B1753 rows' key set; apex index -> (Re, Im) matches
B1753's apexes(); line index set; coverage of (apex, line) over 223 x 266 with the committed census; duplicates equal on
EVERY field (not only mass keys); finiteness/positivity of mass entries."""
import sys, json, math, pathlib, importlib.util, collections
ROOT = next(q for q in pathlib.Path(__file__).resolve().parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
V53 = ROOT / "frontier/B1753_the_six_on_the_five_ality_lines/verification"
D = ROOT / "frontier/B1798_the_six_graded_under_the_class_choosing_null/verification/b1753_all266"
sp = importlib.util.spec_from_file_location("b1753_census", V53 / "census.py")
B53 = importlib.util.module_from_spec(sp); sys.modules["b1753_census"] = B53; sp.loader.exec_module(B53)
AP = B53.apexes(); FIVE = set(B53.five_lines()); L = B53._K().lines()
print("apexes", len(AP), "five lines", len(FIVE), "lines", len(L))

def rows_of(p):
    out, bad, last_ok = [], 0, True
    raw = p.read_bytes()
    print(p.name, "bytes", len(raw), "ends with newline", raw.endswith(b"\n"))
    for i, l in enumerate(raw.decode("utf-8").split("\n")):
        if not l.strip(): continue
        try: out.append(json.loads(l))
        except json.JSONDecodeError: bad += 1; print("  BAD line", i, l[:80], "...", l[-80:])
    return out, bad

com, b0 = rows_of(V53 / "census.jsonl")
ext, b1 = rows_of(D / "census_ext.jsonl")
tail, b2 = rows_of(D / "census_ext_tail.jsonl")
print("rows: committed %d (bad %d), ext %d (bad %d), tail %d (bad %d)" % (len(com), b0, len(ext), b1, len(tail), b2))
K0 = set(com[0].keys())
mass_keys = sorted(k for k in K0 if k.startswith(("up|", "down|", "lep|", "ckm|")))
print("key count", len(K0), "mass keys", len(mass_keys))
probs = collections.Counter()
seen = {}
dups = 0; dup_diff = 0
for src, rows in (("com", com), ("ext", ext), ("tail", tail)):
    for r in rows:
        if set(r.keys()) != K0: probs[src + ":keyset"] += 1
        a, k = r["apex"], r["line"]
        p = AP[a]
        if r["Re_tau"] != p["Re_tau"] or r["Im_tau"] != p["Im_tau"]: probs[src + ":tau_mismatch"] += 1
        if r["words"] != p["words"]: probs[src + ":words_mismatch"] += 1
        if src == "com" and k not in FIVE: probs["com:line_not_five"] += 1
        if src != "com" and k in FIVE: probs[src + ":line_in_five"] += 1
        for mk in mass_keys:
            v = r[mk]
            vals = v[:3] if mk.startswith("ckm") else v
            for x in vals:
                if not (isinstance(x, (int, float)) and math.isfinite(x) and x >= 0): probs[src + ":nonfinite_or_neg"] += 1
        key = (a, k)
        if key in seen:
            dups += 1
            if seen[key][1] != r: dup_diff += 1; print("  DUP DIFF", src, seen[key][0], key)
            if seen[key][0] == "com": probs["dup_with_committed"] += 1
        else:
            seen[key] = (src, r)
print("problems:", dict(probs))
print("distinct (apex,line)", len(seen), "expected", 223 * 266, "dups", dups, "dups differing (any field)", dup_diff)
missing = [(a, k) for a in range(len(AP)) for k in range(266) if (a, k) not in seen]
print("missing", len(missing), missing[:5])
# loader key (line, Re, Im) vs (apex, line) bijection
lk = {(r["line"], r["Re_tau"], r["Im_tau"]) for _, r in seen.values()}
print("distinct (line, Re, Im)", len(lk))
# by source composition
c = collections.Counter(s for s, _ in seen.values()); print("first-seen source counts", dict(c))
