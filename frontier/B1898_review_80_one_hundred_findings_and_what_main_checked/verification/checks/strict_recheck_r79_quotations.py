#!/usr/bin/env python3
"""Review 80, on agy-002's finding about Review 79's quotation checker: the 99 quotations checked again, strictly. [CORRECTED 2026-11-13 (Review 81, the SM seat's finding 05: its output counts 111 quotations, as FINDINGS says]

The old rule called a quotation found when it stood in ANY file of the finding's arc folder or in one of eighteen wide
pages.  Here each is looked for in the file its finding NAMES (for the SM seat's file, which names no file: in the
arc's own folder, or for a finding on the window in one wide page).  Counts only are printed; nothing of a reader's
file is.  Uses the arc's own parser, so that the difference shown is the rule's and not the parser's."""
import importlib.util, json, pathlib, re, sys
ROOT = pathlib.Path(__file__).resolve().parents[2]
spec = importlib.util.spec_from_file_location("qc79", ROOT / "frontier/B1892_review_79_read_by_those_who_did_not_build_it/verification/quote_check.py")
qc = importlib.util.module_from_spec(spec); spec.loader.exec_module(qc)
flat = lambda s: " ".join(s.split())
out = {}
for reader, (commit, path, read) in qc.READERS.items():
    rc, page = qc.git("show", "%s:%s" % (commit, path))
    if rc != 0:
        out[reader] = None; continue
    qs = qc.quotations(reader, page)
    res = {"quotations": len(qs), "found by the old rule": 0, "in the file the finding names": 0, "in the arc's own folder (no file named)": 0,
           "in a wide page only": 0, "the named file is not at the commit": 0, "empty quotations": 0, "found nowhere, strictly": 0}
    for arc, named, q in qs:
        if not flat(q):
            res["empty quotations"] += 1
        old = qc.found(q, arc, named, read)
        res["found by the old rule"] += bool(old)
        strict = where = False
        for c in read:
            rc2, ls = qc.git("ls-tree", "-r", "--name-only", c); files = ls.split("\n")
            if named:
                if named in files:
                    if flat(q) in qc.text(c, named): strict = True
                else:
                    res_missing = True
                    cand = [f for f in files if f.endswith(named.split("/")[-1])]
                    if any(flat(q) in qc.text(c, f) for f in cand): strict = True
            else:
                own = [f for f in files if arc != "window" and f.startswith("frontier/%s_" % arc)]
                if any(flat(q) in qc.text(c, f) for f in own): where = True
        if named and strict:
            res["in the file the finding names"] += 1
        elif not named and where:
            res["in the arc's own folder (no file named)"] += 1
        elif old:
            res["in a wide page only"] += 1
        else:
            res["found nowhere, strictly"] += 1
    # rows the parser does not read: lines that begin as a finding's row and give fewer than four cells
    if reader not in ("the SM seat", "agy-exp"):
        res["lines that begin as a row and are not read"] = sum(1 for l in page.split("\n") if re.match(r"\|\s*(B\d+|window)\s*\|", l) and len([x for x in l.strip().strip("|").split(" | ")]) < 4)
    out[reader] = res
    print("%-12s %s" % (reader, json.dumps(res)))
tot = {k: sum(v[k] for v in out.values() if v and k in v) for k in ("quotations", "found by the old rule", "in the file the finding names", "in the arc's own folder (no file named)", "in a wide page only", "found nowhere, strictly", "empty quotations")}
print("all four:", json.dumps(tot))
json.dump({"readers": out, "all": tot}, open(pathlib.Path(__file__).with_name("strict_recheck_r79_quotations.json"), "w"), indent=1)
