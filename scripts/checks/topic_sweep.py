#!/usr/bin/env python3
"""SEE THE REPO FIRST -- the topic sweep (WORKING_RULES, the rule of 2026-10-02).

Before an arc is opened, and before anything is called new, open, missing, impossible or unproved -- in the record or
in conversation -- the record is swept for the topic.  This is the sweep:

    python3 scripts/checks/topic_sweep.py "<regular expression>" [--refs] [--full] [--limit N]

It reads every arc's verdict line on main (`frontier/*/arc_verdict.json`, field `claim_one_line`) and the title of
every FINDINGS.md, case-insensitively, and prints the arcs that match with their verdicts.  With --refs it also greps
every remote head (the seats' lanes) for the expression in FINDINGS, verdict files and reports.  With --full it greps
the whole text of main's FINDINGS as well.  The last line is the VERDICT line to cite.

`absence_sweep.py` remains the sweep for a specific string anywhere (filenames, deleted history); this one answers
"what does the record already hold on this subject".  --selftest plants a control both ways.

THE REGISTER (proposed by the web seat, 2026-10-27, adopted by main at S225 with its review's two points: malformed rows are counted and named; after a sweep for theta-bar reported "8 of 1533 arcs" while
docs/POINT_REGISTER.md already queued P-323, the same question, and --refs showed main's docs only as one count line):
queued and held work lives in main's register, not in an arc.  Every sweep therefore also reads each register row
(`| P-n | registered | source | point | disposition | where / next | moved |`), matches the expression against the
point and the where/next cells, prints the matching rows with their disposition, and adds "N register rows match
(...)" to the VERDICT line.

ALIASES (Review 66, R65-6, P-123): vocabulary drifts, and a sweep in today's words misses the record's older words for
the same subject (B1290's "I-26 becomes a question about the cusp" is FK10's question; no sweep of B1627, B1629 or
B1632 found it).  Every sweep is expanded by the alias groups below: when the expression matches any term of a group,
the whole group is OR-ed in, and the VERDICT line names the groups used.  --no-aliases turns this off.  Extend the
table whenever a late Seen addendum finds a missed older word.  With --full the VERDICT line says "full text"; a
preregistration's Seen-first line cites a full-text sweep from B1685 on (the gate sealed-preregistration).
"""
import collections, glob, json, os, re, subprocess, sys
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# each group: (a name, its terms as regular expressions); a sweep that matches any term pulls in the whole group
ALIASES = [
    ("the cusp's unit", [r"cusp's unit", r"cusp unit", r"end condition", r"\bFK10\b", r"\bFK11\b", r"\bI-26\b", r"net chirality", r"index formula"]),
    ("the lowest geodesic", [r"lowest closed geodesic", r"shortest (closed )?geodesic", r"\bsystole", r"metallic classification"]),
    ("the weave's measure", [r"uniform measure", r"average over (all )?threads", r"haar limit", r"tower measure", r"tracking the tower"]),
    ("the golden spectrum", [r"golden spectrum", r"fibonacci-golden", r"frequency spectrum", r"particle spectrum", r"iterated hearing"]),
    ("the point i", [r"tau = i\b", r"τ = i\b", r"ℚ\(i\)", r"\bQ\(i\)", r"gaussian (field|integers|point)", r"\bsilver\b"]),
    ("the coupling tensor", [r"multiplicity space", r"coupling tensor", r"yukawa (test|hierarchy)", r"inter-generation hierarchy", r"h¹\(M; 27\)", r"cohomological multiplicity"]),
]


def expand(rx, aliases=ALIASES):
    """the expression OR-ed with every alias group one of whose terms it matches (as text) or which matches it"""
    used = []
    for name, terms in aliases:
        plain = [re.sub(r"\\[bB]|[()?\\]", "", t) for t in terms]
        if any(re.search(rx, p, re.I) for p in plain) or any(re.search(t, rx, re.I) for t in terms):
            used.append(name)
    if not used: return rx, []
    extra = [t for name, terms in aliases if name in used for t in terms]
    return "(?:%s)|%s" % (rx, "|".join(extra)), used


def arcs(root=ROOT):
    out = []
    for d in sorted(glob.glob(os.path.join(root, "frontier", "*"))):
        if not os.path.isdir(d): continue
        name = os.path.basename(d); vid, verdict, claim, title = name.split("_")[0], None, "", ""
        vf = os.path.join(d, "arc_verdict.json")
        if os.path.exists(vf):
            try:
                v = json.load(open(vf)); verdict = v.get("verdict"); claim = v.get("claim_one_line") or ""
            except Exception: pass
        ff = os.path.join(d, "FINDINGS.md")
        if os.path.exists(ff):
            try: title = open(ff, errors="replace").readline().strip()
            except Exception: pass
        out.append(dict(id=vid, dir=name, verdict=verdict, claim=claim, title=title))
    return out


def sweep(rx, rows, full=False, root=ROOT):
    pat = re.compile(rx, re.I); hits = []
    for r in rows:
        where = [k for k in ("claim", "title") if pat.search(r[k])]
        if not where and full:
            ff = os.path.join(root, "frontier", r["dir"], "FINDINGS.md")
            if os.path.exists(ff) and pat.search(open(ff, errors="replace").read()): where = ["text"]
        if where: hits.append(dict(r, where=where))
    return hits


REGISTER_SKIPPED = []                                  # rows that do not split into seven cells (named, never silent)


def register(root=ROOT):
    """main's POINT_REGISTER rows: id, disposition, where / next and the point's text (seven cells per row); a row that does
    not split into seven cells is recorded in REGISTER_SKIPPED and reported by main(), not dropped silently"""
    p = os.path.join(root, "docs", "POINT_REGISTER.md"); out = []; del REGISTER_SKIPPED[:]
    if not os.path.exists(p): return out
    for line in open(p, errors="replace"):
        if not re.match(r"\| P-\d+ \|", line): continue
        f = line.rstrip("\n").split(" | ")
        if len(f) != 7: REGISTER_SKIPPED.append(line.split(" | ")[0].lstrip("| ").strip()); continue
        out.append(dict(id=f[0].lstrip("| ").strip(), disposition=f[4].strip(), where=f[5].strip(), point=f[3].strip()))
    return out


def sweep_register(rx, rows):
    pat = re.compile(rx, re.I)
    return [r for r in rows if pat.search(r["point"]) or pat.search(r["where"])]


def sweep_refs(rx, root=ROOT):
    """per remote head: the number of files under frontier/, reports/ and docs/ whose text matches"""
    heads = subprocess.run(["git", "-C", root, "for-each-ref", "--format=%(refname:short)", "refs/remotes"], capture_output=True, text=True).stdout.split()
    seen, out = set(), {}
    for h in heads:
        if h.endswith("/HEAD") or h.split("/", 1)[-1] in ("main",): continue
        leaf = h.split("/", 1)[-1]
        if leaf in seen: continue
        seen.add(leaf)
        r = subprocess.run(["git", "-C", root, "grep", "-I", "-l", "-i", "-E", rx, h, "--", "frontier", "reports", "docs"], capture_output=True, text=True)
        files = [l.split(":", 1)[1] for l in r.stdout.splitlines() if ":" in l]
        if files: out[leaf] = files
    return out


def main(argv):
    if "--selftest" in argv:
        rows = [dict(id="B1", dir="B1_x", verdict="PROVED", claim="the dynamics is a Painleve VI flow", title="# B1"),
                dict(id="B2", dir="B2_y", verdict="NEGATIVE", claim="no canonical arrow", title="# B2 time")]
        assert [h["id"] for h in sweep(r"painlev", rows)] == ["B1"] and [h["id"] for h in sweep(r"\btime\b", rows)] == ["B2"]
        assert sweep(r"zzzz-not-there", rows) == [] and len(sweep(r"zzzz-not-there", arcs())) == 0
        assert len(sweep(r"figure-eight|m004", arcs())) > 50, "the sweep finds what is known to be there"
        rx, used = expand(r"cusp unit"); assert used == ["the cusp's unit"] and re.search(rx, "I-26 becomes a question about the cusp", re.I)
        assert expand(r"zzzz-not-there") == (r"zzzz-not-there", [])
        reg = [dict(id="P-1", disposition="QUEUED", where="Q3", point="theta-bar in the mass frame"),
               dict(id="P-2", disposition="DONE", where="B9 (a Painleve flow)", point="the arrow")]
        assert [r["id"] for r in sweep_register(r"theta.?bar", reg)] == ["P-1"] and [r["id"] for r in sweep_register(r"painlev", reg)] == ["P-2"]
        assert sweep_register(r"zzzz-not-there", reg) == [] and sweep_register(r"zzzz-not-there", register()) == []
        assert len(register()) > 300 and all(r["id"].startswith("P-") for r in register()), "the register is read"
        print("selftest: PASS (a planted hit is found, a planted absence is empty, and the real record answers)"); return 0
    args = [a for a in argv if not a.startswith("--")]
    if not args: print(__doc__); return 2
    rx = args[0]; limit = int(argv[argv.index("--limit") + 1]) if "--limit" in argv else 40
    erx, used = (rx, []) if "--no-aliases" in argv else expand(rx)
    rows = arcs(); hits = sweep(erx, rows, full="--full" in argv)
    by = collections.Counter(h["verdict"] or "no verdict file" for h in hits)
    for h in hits[-limit:]:
        print("  %-7s %-9s %s" % (h["id"], h["verdict"] or "-", (h["claim"] or h["title"])[:170]))
    reg = sweep_register(erx, register())
    if REGISTER_SKIPPED: print("  register rows skipped (not seven cells): %s" % ", ".join(REGISTER_SKIPPED))
    for r in reg[-limit:]:
        print("  %-7s %-9s %s  [%s]" % (r["id"], r["disposition"], r["point"][:140], r["where"][:40]))
    tags = (["full text"] if "--full" in argv else []) + (["aliases: " + "; ".join(used)] if used else [])
    line = "VERDICT topic-sweep /%s/%s: %d of %d arcs on main match (%s)" % (rx, (" (" + ", ".join(tags) + ")") if tags else "", len(hits), len(rows), ", ".join("%s %d" % kv for kv in sorted(by.items())) or "none")
    rby = collections.Counter(r["disposition"] or "-" for r in reg)
    line += "; %d register rows match (%s)" % (len(reg), ", ".join("%s %d" % kv for kv in sorted(rby.items())) or "none")
    if "--refs" in argv:
        refs = sweep_refs(erx)
        for leaf, files in sorted(refs.items()): print("  lane %-45s %d files, e.g. %s" % (leaf, len(files), files[0][:80]))
        line += "; %d other lanes match (%s)" % (len(refs), ", ".join("%s %d" % (k, len(v)) for k, v in sorted(refs.items())) or "none")
    print(line); return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
