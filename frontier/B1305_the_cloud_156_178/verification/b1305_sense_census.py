"""B1305 Q1 -- THE SENSE CENSUS, an INDEPENDENT implementation of the cloud's memo 172 instrument (DESIGN sealed 7e1a7420).
Question it answers: is a technical CONCEPT in the corpus, not merely its WORD? For every occurrence of a term in the prose
(.md/.tex under frontier/ docs/ papers/, the cloud's own memos excluded), test whether a marker of the technical sense occurs within
+-WINDOW characters; a term present >= 5 times with < 2 % technical contexts is FALSE COMFORT; < 10 % is THIN; else GENUINE.
Usage: b1305_sense_census.py <tree-root> [--planted]   (prints the memo's seven cases; --planted runs the three MB12 controls on a copy)."""
import os, re, sys, json, tempfile, shutil
WINDOW = 130
CASES = [("logarithmic", r"\bCFT\b|\bVOA\b|Virasoro|vertex algebra|primary field", "neg"),
         ("non-semisimple", r"tensor categ|\bTQFT\b|modular categ|fusion", "neg"),
         ("character", r"\bVOA\b|Virasoro|vertex algebra|q-series|conformal", None),
         ("modular", r"tensor categ|S-matrix|\bVOA\b|fusion", None),
         ("non-rational", r"\bCFT\b|\bVOA\b|vertex algebra", None),
         ("resurgence", r"Borel|Stokes|transseries", None),
         ("Chern-Simons", r"\bCS\b|level|action|invariant", "pos")]
def prose(root):
    out = []
    for base in ("frontier", "docs", "papers"):
        for dp, dns, fns in os.walk(os.path.join(root, base)):
            dns[:] = sorted(d for d in dns if d not in ("outside_bench", ".git", "__pycache__"))
            out += [os.path.join(dp, f) for f in sorted(fns) if f.endswith((".md", ".tex"))]
    return out
def census(root, cases=CASES):
    files = prose(root)
    texts = [open(f, encoding="utf-8", errors="replace").read() for f in files]
    size = sum(len(t) for t in texts)
    res = {}
    for term, marker, kind in cases:
        tre = re.compile(re.escape(term), re.I); mre = re.compile(marker, re.I); tot = hit = 0
        for t in texts:                                   # per file, not on a joined blob: a window never crosses a file boundary
            for m in tre.finditer(t):
                tot += 1
                if mre.search(t[max(0, m.start() - WINDOW): m.end() + WINDOW]): hit += 1
        frac = hit / tot if tot else 0.0
        verdict = "FALSE COMFORT" if (tot >= 5 and frac < 0.02) else ("thin" if frac < 0.10 else "genuine")
        res[term] = dict(occurrences=tot, technical=hit, frac=round(frac, 4), verdict=verdict, kind=kind)
    return dict(files=len(files), mb=round(size / 1e6, 1), terms=res)
def two_sided(res):
    pos = [v for v in res["terms"].values() if v["kind"] == "pos"]; neg = [v for v in res["terms"].values() if v["kind"] == "neg"]
    return all(v["verdict"] == "genuine" for v in pos), all(v["verdict"] == "FALSE COMFORT" for v in neg)
def planted(root):
    """three MB12 controls on a scratch copy of docs/ only (enough prose to keep the census meaningful)"""
    tmp = tempfile.mkdtemp(); shutil.copytree(os.path.join(root, "docs"), os.path.join(tmp, "docs"))
    os.makedirs(os.path.join(tmp, "frontier")); os.makedirs(os.path.join(tmp, "papers"))
    base = census(tmp)["terms"]["logarithmic"]
    def plant(text):
        p = os.path.join(tmp, "docs", "PLANTED.md"); open(p, "w").write(text); r = census(tmp)["terms"]["logarithmic"]; os.remove(p); return r
    a = plant("x " * 50 + "a logarithmic CFT appears here " + "x " * 50)
    b = plant("x " * 50 + "the logarithmic derivative of the volume " + "x " * 50)
    c = plant("logarithmic " + "y " * 70 + "CFT")          # marker 141+ chars away: outside the window
    out = dict(base=base, technical_marker=a, no_marker=b, marker_outside_window=c,
               ok=(a["technical"] == base["technical"] + 1 and a["occurrences"] == base["occurrences"] + 1
                   and b["technical"] == base["technical"] and b["occurrences"] == base["occurrences"] + 1
                   and c["technical"] == base["technical"] and c["occurrences"] == base["occurrences"] + 1))
    shutil.rmtree(tmp); return out
if __name__ == "__main__":
    root = sys.argv[1]; res = census(root); okp, okn = two_sided(res)
    print(f"tree {root}: {res['files']} prose files, {res['mb']} MB (outside_bench excluded)")
    for term, v in res["terms"].items():
        print(f"  {term:<16}{v['occurrences']:>8}{v['technical']:>8} ({v['frac']*100:5.1f}%)  {v['verdict']}" + (f"   [{v['kind']}]" if v["kind"] else ""))
    print(f"  CONTROL + (Chern-Simons genuine): {'PASS' if okp else 'FAIL'};  CONTROL - (logarithmic, non-semisimple false comfort): {'PASS' if okn else 'FAIL'};  TWO-SIDED: {'PASSED' if okp and okn else 'FAILED'}")
    out = dict(root=root, census=res, two_sided=okp and okn)
    if "--planted" in sys.argv:
        pl = planted(root); out["planted"] = pl
        print(f"  PLANTED CONTROLS: +1 technical with marker: {pl['technical_marker']['technical'] - pl['base']['technical']}; no marker: +{pl['no_marker']['technical'] - pl['base']['technical']}; marker outside window: +{pl['marker_outside_window']['technical'] - pl['base']['technical']}  -> {'PASS' if pl['ok'] else 'FAIL'}")
    tag = os.path.basename(os.path.normpath(root)); json.dump(out, open(f"b1305_sense_census_{tag}.json", "w"), indent=1)
