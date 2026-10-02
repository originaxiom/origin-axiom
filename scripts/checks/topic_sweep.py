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
"""
import collections, glob, json, os, re, subprocess, sys
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


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
        print("selftest: PASS (a planted hit is found, a planted absence is empty, and the real record answers)"); return 0
    args = [a for a in argv if not a.startswith("--")]
    if not args: print(__doc__); return 2
    rx = args[0]; limit = int(argv[argv.index("--limit") + 1]) if "--limit" in argv else 40
    rows = arcs(); hits = sweep(rx, rows, full="--full" in argv)
    by = collections.Counter(h["verdict"] or "no verdict file" for h in hits)
    for h in hits[-limit:]:
        print("  %-7s %-9s %s" % (h["id"], h["verdict"] or "-", (h["claim"] or h["title"])[:170]))
    line = "VERDICT topic-sweep /%s/: %d of %d arcs on main match (%s)" % (rx, len(hits), len(rows), ", ".join("%s %d" % kv for kv in sorted(by.items())) or "none")
    if "--refs" in argv:
        refs = sweep_refs(rx)
        for leaf, files in sorted(refs.items()): print("  lane %-45s %d files, e.g. %s" % (leaf, len(files), files[0][:80]))
        line += "; %d other lanes match (%s)" % (len(refs), ", ".join("%s %d" % (k, len(v)) for k, v in sorted(refs.items())) or "none")
    print(line); return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
