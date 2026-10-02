#!/usr/bin/env python3
"""PRIOR WORK -- the instrument behind SEE THE REPO FIRST, THEN THE LITERATURE (WORKING_RULES, 2026-10-02).
The owner, verbatim: "i ljust lets make sure we dont miss any work and misclaim about it. make a rule to see the repo first
and literature".

Two legs, in this order, before an arc is designed and before any sentence says a result is new, first, absent, ours, or
what another work states:

  1. THE REPO. Every head (run `git fetch --all` first), deleted history and the working tree, for each term: the absence
     sweep (filenames and content, every head) and the already-banked scan (the banked verdicts). A hit is a place to READ,
     never a verdict; read the hit's FINDINGS body and the script behind any number.
  2. THE LITERATURE. Searched and read by the seat -- no tool can do this leg. Each source is recorded with where it states
     the fact (section, lemma, equation, sequence number) and the date it was read. Never cite from memory.

    python3 scripts/checks/prior_work.py "term" ["term" ...]                  # the repo leg, summarised
    python3 scripts/checks/prior_work.py "term" ... --json OUT.json           # also writes a prior_work skeleton
    python3 scripts/checks/prior_work.py --check frontier/BNNNN_x/arc_verdict.json
    python3 scripts/checks/prior_work.py --selftest

THE RECORD (arc_verdict.json, required from B1517 on; tests/test_arc_verdict_schema.py calls validate() below):

  "prior_work": {
    "repo": {"heads": {"<ref, any vendor word written as 'seat'>": "<sha>", ...}, "terms": ["...", ...],
             "hits": [{"where": "<ref:path or arc>", "bearing": "<what it changes for this arc>"}, ...]},
    "literature": {"queries": ["...", ...],
                   "sources": [{"cite": "<author, title, venue, year>", "where": "<section/lemma/eq.>",
                                "read": "YYYY-MM-DD", "says": "<what it states, in a line>"}, ...]},
    "standing": "KNOWN" | "RE-DERIVED" | "EXTENDS" | "NEW-AS-SWEPT" | "NOT-CHECKED",
    "why": "<required for NOT-CHECKED>"
  }

STANDING (of the arc's main result):
  KNOWN         it is already in the literature or the repo; the arc reuses it. Cite.
  RE-DERIVED    own code agrees with a cited source; the arc's contribution is the verification.
  EXTENDS       it extends cited work; say what is added.
  NEW-AS-SWEPT  found in no swept head and in no source read. Novelty is claimed only that far, with the sweep beside it.
  NOT-CHECKED   the sweep was not done; say why. The arc may then claim nothing new or absent.

THIS INSTRUMENT CHECKS THE FORM OF THE RECORD; THE JUDGEMENT STAYS WITH THE SEAT.
"""
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
STANDINGS = ("KNOWN", "RE-DERIVED", "EXTENDS", "NEW-AS-SWEPT", "NOT-CHECKED")
_SHA = re.compile(r"^[0-9a-f]{7,40}$")
_DATE = re.compile(r"^\d{4}-\d{2}-\d{2}$")


def validate(block):
    """Problems with a prior_work block, as a list of strings (empty means well formed)."""
    p = []
    if not isinstance(block, dict):
        return ["prior_work must be an object"]
    repo, lit, st = block.get("repo"), block.get("literature"), block.get("standing")
    if st not in STANDINGS:
        p.append(f"standing must be one of {STANDINGS}")
    if not isinstance(repo, dict):
        p.append("repo must be an object")
        repo = {}
    heads = repo.get("heads")
    if not (isinstance(heads, dict) and heads and all(isinstance(v, str) and _SHA.match(v) for v in heads.values())):
        p.append("repo.heads must map each swept ref to its commit sha")
    terms = repo.get("terms")
    if not (isinstance(terms, list) and terms and all(isinstance(t, str) and t.strip() for t in terms)):
        p.append("repo.terms must list the searched terms")
    hits = repo.get("hits", [])
    if not (isinstance(hits, list) and all(isinstance(h, dict) and h.get("where") and h.get("bearing") for h in hits)):
        p.append("repo.hits must be a list of {where, bearing}")
    if not isinstance(lit, dict):
        p.append("literature must be an object")
        lit = {}
    queries, sources = lit.get("queries", []), lit.get("sources", [])
    if not (isinstance(queries, list) and all(isinstance(q, str) and q.strip() for q in queries)):
        p.append("literature.queries must be a list of strings")
        queries = []
    ok_src = isinstance(sources, list) and all(
        isinstance(s, dict) and s.get("cite") and s.get("where") and s.get("says") and _DATE.match(str(s.get("read", "")))
        for s in sources)
    if not ok_src:
        p.append("literature.sources must be a list of {cite, where, read: YYYY-MM-DD, says}")
        sources = []
    if st == "NOT-CHECKED":
        if not (isinstance(block.get("why"), str) and block["why"].strip()):
            p.append("NOT-CHECKED needs a why")
    elif st in STANDINGS:
        if not queries:
            p.append(f"{st} needs the literature queries that were run")
        if st in ("KNOWN", "RE-DERIVED", "EXTENDS") and not (sources or hits):
            p.append(f"{st} needs the source it rests on: a literature source or a repo hit")
    return p


def _vendor_re():
    """The attribution gate's own pattern (scripts/gates/gates.py), so a recorded ref name never carries a vendor word into a
    tracked file. Loaded from the gate, which keeps the tokens encoded; the same encoded list is the fallback."""
    try:
        import importlib.util
        spec = importlib.util.spec_from_file_location("_oa_gates", ROOT / "scripts" / "gates" / "gates.py")
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        return mod._VENDOR_RE
    except Exception:
        import base64
        toks = [base64.b64decode(b).decode() for b in (b"Y2xhdWRl", b"YW50aHJvcGlj", b"b3B1cw==", b"c29ubmV0", b"ZmFibGU=")]
        return re.compile(r"\b(" + "|".join(toks) + r")\b", re.I)


def ref_label(name):
    """A ref name as recorded: any vendor word in it becomes 'seat'. The sha beside it identifies the commit."""
    return _vendor_re().sub("seat", name)


def heads_now():
    sys.path.insert(0, str(ROOT / "scripts" / "checks"))
    import absence_sweep
    return {ref_label(k): v for k, v in absence_sweep.heads()}


def repo_leg(terms, regex=False):
    """Run the absence sweep and the already-banked scan for each term; return a summary and a skeleton block."""
    sys.path.insert(0, str(ROOT / "scripts" / "checks"))
    import absence_sweep
    import already_banked
    summary = []
    for t in terms:
        rep = absence_sweep.sweep(t, regex=regex)
        per_head = {ref_label(h["head"]): len(h["content"]) + len(h["filenames"]) for h in rep["heads"]}
        files = sorted({f.split(":", 1)[-1] for h in rep["heads"] for f in h["content"] + h["filenames"]})
        banked = [(n, v, w) for n, v, w, _ in already_banked.scan(already_banked._terms([t]))][:8]
        summary.append({"term": t, "present": bool(absence_sweep.present(rep)), "hits_per_head": per_head,
                        "files": files[:25], "n_files": len(files), "deleted": rep["deleted"][:10],
                        "worktree": rep["worktree"][:10], "banked_verdicts": banked})
    skeleton = {"repo": {"heads": {ref_label(k): v for k, v in absence_sweep.heads()}, "terms": list(terms), "hits": []},
                "literature": {"queries": [], "sources": []}, "standing": "NOT-CHECKED",
                "why": "skeleton: read the hits, run the literature leg, then set the standing"}
    return summary, skeleton


def render(summary):
    for s in summary:
        where = (f"{s['n_files']} files on the heads, {len(s['deleted'])} deleted in history, "
                 f"{len(s['worktree'])} in the working tree")
        if s["present"] and not s["n_files"] and not s["deleted"]:
            where += " ONLY (uncommitted text; no head has it)"
        print(f"PRIOR WORK, repo leg, term {s['term']!r}: {'PRESENT' if s['present'] else 'ABSENT'} ({where})")
        for f in s["worktree"][:3]:
            print(f"      worktree: {f}")
        for h, n in s["hits_per_head"].items():
            if n:
                print(f"    {h:55s} {n:5d}")
        for f in s["files"][:8]:
            print(f"      {f}")
        for n, v, w in s["banked_verdicts"][:5]:
            print(f"      banked: [{n} terms] {v:<9} {w}")
    print("Read every hit that bears on the claim; then run the literature leg and record both (WORKING_RULES 2026-10-02).")


def selftest():
    """Controls in both directions for validate(), and the repo leg on a planted term and a fresh nonce."""
    import uuid
    good = {"repo": {"heads": {"origin/main": "bd48dd28"}, "terms": ["x"], "hits": [{"where": "a", "bearing": "b"}]},
            "literature": {"queries": ["q"], "sources": [{"cite": "c", "where": "w", "read": "2026-10-02", "says": "s"}]},
            "standing": "RE-DERIVED"}
    checks = [("accepts a well-formed block", validate(good) == [])]
    bad = json.loads(json.dumps(good)); bad["standing"] = "NEW"
    checks.append(("rejects an unknown standing", bool(validate(bad))))
    bad = json.loads(json.dumps(good)); bad["repo"]["heads"] = {"origin/main": "not-a-sha"}
    checks.append(("rejects a head without a sha", bool(validate(bad))))
    bad = json.loads(json.dumps(good)); bad["literature"] = {"queries": [], "sources": []}
    checks.append(("rejects a standing with no literature queries", bool(validate(bad))))
    bad = json.loads(json.dumps(good)); bad["literature"]["sources"][0]["read"] = "yesterday"
    checks.append(("rejects a source without a read date", bool(validate(bad))))
    bad = json.loads(json.dumps(good)); bad["standing"] = "NOT-CHECKED"; bad.pop("why", None)
    checks.append(("rejects NOT-CHECKED without a why", bool(validate(bad))))
    bad = json.loads(json.dumps(good)); bad["literature"]["sources"] = []; bad["repo"]["hits"] = []
    checks.append(("rejects RE-DERIVED resting on nothing", bool(validate(bad))))
    summ, skel = repo_leg(["GENESIS.md"])
    checks.append(("the repo leg finds a planted term", summ[0]["present"]))
    summ, _ = repo_leg(["ZQX" + uuid.uuid4().hex[:12]])
    checks.append(("the repo leg reports a fresh nonce absent", not summ[0]["present"]))
    checks.append(("the skeleton records more than one head with its sha", len(skel["repo"]["heads"]) > 1))
    checks.append(("the skeleton is well formed", validate(skel) == []))
    checks.append(("recorded ref names carry no vendor word", not any(_vendor_re().search(k) for k in skel["repo"]["heads"])))
    for name, ok in checks:
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}")
    ok = all(c for _, c in checks)
    print("CONTROLS PASS" if ok else "CONTROLS FAIL")
    return 0 if ok else 1


if __name__ == "__main__":
    args = sys.argv[1:]
    if not args:
        print(__doc__)
        sys.exit(2)
    if args == ["--selftest"]:
        sys.exit(selftest())
    if args[0] == "--check":
        d = json.loads(pathlib.Path(args[1]).read_text(encoding="utf-8"))
        probs = validate(d.get("prior_work"))
        print("\n".join(probs) if probs else "prior_work: well formed")
        sys.exit(1 if probs else 0)
    out = None
    if "--json" in args:
        i = args.index("--json")
        out = args[i + 1]
        args = args[:i] + args[i + 2:]
    regex = "--regex" in args
    terms = [a for a in args if not a.startswith("--")]
    summary, skeleton = repo_leg(terms, regex=regex)
    render(summary)
    if out:
        pathlib.Path(out).write_text(json.dumps({"summary": summary, "prior_work": skeleton}, indent=1,
                                                ensure_ascii=False) + "\n", encoding="utf-8")
        print(f"wrote {out}")
