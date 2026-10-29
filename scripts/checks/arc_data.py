#!/usr/bin/env python3
"""arc-data — P-420's phase 0: every defect in the arcs' machine-readable data that a generated desk would draw wrongly.

WHY (the owner's workdesk, P-420; GO 2026-10-29: "phase 0 first")
-----------------------------------------------------------------
A desk drawn from `arc_verdict.json` shows what the fields say, not what the record means. Three seats measured the
fields independently (main's relay CC_TO_ALL_SEATS_2026-10-29_THE_WORKDESK_YOUR_PROPOSALS; the web seat's proposal
@ a024efb02; the SM seat's Ledger Desk @ f22777298) and their lists differ. This check merges them into one report, so
the fixes can be made before any view is generated:

    D1  an "id" carried by more than one verdict file (B58 three times; B89 twice)
    D2  a folder whose number is not its verdict's "id" (B89T_tower_route carries "B89"; gate_id_collisions reads
        folders with (B\\d+)[a-z]?_ and never sees an upper-case suffix)
    D3  a dependency on a number with no folder at all
    D4  a dependency on a folder with no verdict file
    D5  a dependency on something that is not an arc number (K002, PC12)
    D6  one-sided supersession, both ways (gate_supersession_backlinks enforces forward -> back only)
    D7  a relation recorded only in prose: a claim line naming another arc with retract/refute/supersede/correct/withdraw,
        where no field links the two (candidates for a reader; B288 <- B1419 is the web seat's example)
    D8  with --branches: a number that names a different folder on a seat's branch than on main (the SM seat's
        "one identity per arc across branches")
    and, as counts only (completeness, not defects): verdict files with no dependency recorded, with no scope, with
    weave_or_thread.

RESOLVED, NOT DEFECTS (main's triage, 2026-10-29; audit/drafts/p420_phase0_triage.md, verified on main): a D1 id
grandfathered by gate_id_collisions (B58, B89; GOVERNANCE §12 forbids moving banked folders); a dependency on an arc
whose folder lives as a harvested copy (frontier/*/harvested/frontier/<id>_*: B792, B796 inside B921); on an id banked
as a CHANGELOG section with no folder (B829, B844, B846, B999); on a folder with neither verdict nor FINDINGS (a
preregistration or campaign directory: B506, ...); on a document (K<nnn> in knowledge/, PC<n> in papers/CANDIDATES.md).
These are listed under R1-R5 so a desk can draw them as what they are. A seat id (sm:B..., sm:W...) in depends_on is a
defect (D5): it belongs in rests_on_seat (built on; VERIFIED) or cites_seat (gate_seat_positive_verified).

Report-only: it exits 0 unless --strict is given and a defect class D1-D6 is non-empty.
    python3 scripts/checks/arc_data.py [--json OUT] [--branches] [--strict]
"""
import collections, glob, json, os, re, subprocess, sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
ARC = re.compile(r"B\d+[A-Za-z]?")
RELATION = re.compile(r"(retract|refut|supersed|correct|withdr)", re.I)
BRANCH_SUFFIXES = ("/standard-model-derivation-0qt6ao", "/chat1/web-seat")      # the seats' branches, matched by suffix as harvest_debt does


def _ids(v):
    """a field that may be None, one id, a list, or one string holding several ids (B239's shape)"""
    if not v: return []
    raw = [v] if isinstance(v, str) else list(v)
    return [t for chunk in raw for t in re.split(r"[,\s]+", str(chunk).strip()) if t]


def load(root=ROOT):
    V, bad = {}, []
    for f in sorted(glob.glob(os.path.join(root, "frontier", "*", "arc_verdict.json"))):
        folder = os.path.basename(os.path.dirname(f))
        try: V[folder] = json.load(open(f, encoding="utf-8"))
        except Exception as e: bad.append((folder, str(e)[:80]))
    folders = collections.defaultdict(list)
    for fo in sorted(os.listdir(os.path.join(root, "frontier"))):
        m = re.match(r"(B\d+)", fo)
        if m and os.path.isdir(os.path.join(root, "frontier", fo)): folders[m.group(1)].append(fo)
    return V, folders, bad


def check(root=ROOT, branches=False):
    V, folders, bad = load(root)
    by_id = collections.defaultdict(list)
    for fo, d in V.items(): by_id[str(d.get("id"))].append(fo)
    out = {"verdict files": len(V), "unreadable verdict files": bad}
    out["D1 one id, several verdict files"] = {k: v for k, v in sorted(by_id.items()) if len(v) > 1}
    out["D2 folder number is not the verdict id"] = [[fo, d.get("id")] for fo, d in sorted(V.items())
                                                    if not re.match(re.escape(str(d.get("id"))) + r"_", fo)]
    gf = re.search(r"GRANDFATHERED_IDS = frozenset\(\{([^}]*)\}\)", open(os.path.join(root, "scripts", "gates", "gates.py"), encoding="utf-8").read()) \
        if os.path.isfile(os.path.join(root, "scripts", "gates", "gates.py")) else None
    grand = set(re.findall(r'"(B\d+)"', gf.group(1))) if gf else set()
    d1 = out.pop("D1 one id, several verdict files")
    out["D1 one id, several verdict files"] = {k: v for k, v in d1.items() if k not in grand}
    out["R1 grandfathered collisions (gate_id_collisions)"] = {k: v for k, v in d1.items() if k in grand}
    out["D2 folder number is not the verdict id"] = [r for r in out["D2 folder number is not the verdict id"] if str(r[1]) not in grand]
    cl = os.path.join(root, "CHANGELOG.md")
    banked = set(re.findall(r"^## (B\d+)\b", open(cl, encoding="utf-8").read(), re.M)) if os.path.isfile(cl) else set()
    cand = os.path.join(root, "papers", "CANDIDATES.md"); cand = open(cand, encoding="utf-8").read() if os.path.isfile(cand) else ""
    d3, d4, d5 = collections.defaultdict(list), collections.defaultdict(list), collections.defaultdict(list)
    r2, r3, r4, r5 = collections.defaultdict(list), collections.defaultdict(list), collections.defaultdict(list), collections.defaultdict(list)
    for fo, d in sorted(V.items()):
        i = d.get("id")
        for t in _ids(d.get("depends_on")):
            if not ARC.fullmatch(t):
                if re.fullmatch(r"K\d+", t) and glob.glob(os.path.join(root, "knowledge", t + "_*")): r5[t].append(i)
                elif re.fullmatch(r"PC\d+", t) and re.search(r"\b" + t + r"\b", cand): r5[t].append(i)
                else: d5[t].append(i)
                continue
            if t in by_id: continue
            base = re.sub(r"[A-Za-z]$", "", t)
            if base in folders:
                fs = folders[base]
                if any(os.path.isfile(os.path.join(root, "frontier", f, "FINDINGS.md")) for f in fs): d4[t].append(i)
                else: r4[t].append(i)
            elif glob.glob(os.path.join(root, "frontier", "*", "harvested", "frontier", t + "_*")): r2[t].append(i)
            elif t in banked: r3[t].append(i)
            else: d3[t].append(i)
    out["D3 dependency on a number with no folder"] = {k: v for k, v in sorted(d3.items())}
    out["D4 dependency on a folder with FINDINGS but no verdict file"] = {k: {"cited by": v, "folders": folders[re.sub(r"[A-Za-z]$", "", k)]}
                                                                         for k, v in sorted(d4.items())}
    out["D5 dependency on a non-arc id"] = {k: v for k, v in sorted(d5.items())}
    out["R2 dependency on a harvested copy"] = {k: {"cited by": v, "at": [os.path.relpath(x, root) for x in glob.glob(os.path.join(root, "frontier", "*", "harvested", "frontier", k + "_*"))]}
                                                for k, v in sorted(r2.items())}
    out["R3 dependency on an id banked as a CHANGELOG section"] = {k: v for k, v in sorted(r3.items())}
    out["R4 dependency on a folder with neither verdict nor FINDINGS"] = {k: {"cited by": v, "folders": folders[re.sub(r"[A-Za-z]$", "", k)]}
                                                                         for k, v in sorted(r4.items())}
    out["R5 dependency on a document"] = {k: v for k, v in sorted(r5.items())}
    fwd, back = collections.defaultdict(set), collections.defaultdict(set)
    for fo, d in V.items():
        i = str(d.get("id"))
        for t in _ids(d.get("supersedes")): fwd[i].add(t)
        for t in _ids(d.get("superseded_by")): back[i].add(t)
    one_sided = []
    for a, ts in sorted(fwd.items()):
        for t in sorted(ts):
            if t in by_id and a not in back.get(t, set()): one_sided.append(f"{a} supersedes {t}; {t} does not name {a}")
    for b, ss in sorted(back.items()):
        for s in sorted(ss):
            if s in by_id and b not in fwd.get(s, set()): one_sided.append(f"{b} superseded_by {s}; {s} does not name {b}")
            elif s not in by_id and ARC.fullmatch(s): one_sided.append(f"{b} superseded_by {s}; {s} has no verdict file")
    out["D6 one-sided supersession"] = one_sided
    out["supersession counts"] = {"supersedes set": sum(1 for d in V.values() if d.get("supersedes")),
                                  "superseded_by set": sum(1 for d in V.values() if d.get("superseded_by"))}
    d7 = []
    for fo, d in sorted(V.items()):
        i = str(d.get("id")); claim = str(d.get("claim_one_line") or "")
        linked = set(_ids(d.get("depends_on"))) | set(_ids(d.get("supersedes"))) | set(_ids(d.get("superseded_by")))
        for m in re.finditer(r"\b(B\d+)\b", claim):
            t = m.group(1)
            if t == i or t in linked or t not in by_id: continue
            win = claim[max(0, m.start() - 60): m.end() + 60]
            if RELATION.search(win): d7.append([i, t, win.replace("\n", " ")])
    out["D7 relation in prose only (candidates)"] = d7
    out["completeness"] = {"no dependency recorded": sum(1 for d in V.values() if not _ids(d.get("depends_on"))),
                           "no scope": sum(1 for d in V.values() if not d.get("scope")),
                           "weave_or_thread recorded": sum(1 for d in V.values() if d.get("weave_or_thread"))}
    if branches:
        main_names = {fo for fs in folders.values() for fo in fs}; d8 = {}
        refs = subprocess.run(["git", "-C", root, "for-each-ref", "--format=%(refname:short)", "refs/remotes/origin"], capture_output=True, text=True).stdout.split()
        for br in [r for r in refs if r.endswith(BRANCH_SUFFIXES)]:
            try:
                ls = subprocess.run(["git", "-C", root, "ls-tree", "-d", "--name-only", br, "frontier/"], capture_output=True, text=True, check=True).stdout
            except Exception as e:
                d8[br] = "unreadable: " + str(e)[:60]; continue
            rows = []
            for p in ls.split():
                fo = p.split("/", 1)[1] if "/" in p else p; m = re.match(r"(B\d+)", fo)
                if m and fo not in main_names and m.group(1) in folders: rows.append([fo, folders[m.group(1)]])
            d8[br] = rows
        out["D8 a number naming a different folder on a seat's branch"] = d8
    return out


def main():
    br = "--branches" in sys.argv; out = check(branches=br)
    if "--json" in sys.argv:
        p = sys.argv[sys.argv.index("--json") + 1]
        open(p, "w", encoding="utf-8").write(json.dumps(out, indent=1, ensure_ascii=False) + "\n")
    print("arc-data (P-420 phase 0): %d verdict files" % out["verdict files"])
    for k, v in out.items():
        if k[:2] in ("D1", "D2", "D3", "D4", "D5", "D6", "D7", "D8", "R1", "R2", "R3", "R4", "R5"):
            n = len(v) if not isinstance(v, dict) or not k.startswith("D8") else sum(len(x) for x in v.values() if isinstance(x, list))
            edges = (" (%d edges)" % sum(len(x if isinstance(x, list) else x["cited by"]) for x in v.values())) if k[:2] in ("D3", "D4", "D5", "R2", "R3", "R4", "R5") else ""
            print("  %-60s %d%s" % (k, n, edges))
    print("  completeness:", out["completeness"], "; supersession:", out["supersession counts"])
    hard = sum(len(out[k]) for k in out if k[:2] in ("D1", "D2", "D3", "D4", "D5", "D6"))
    verdict = "VERDICT arc-data: %d defects in D1-D6, %d prose-only candidates (D7)" % (hard, len(out["D7 relation in prose only (candidates)"]))
    print(verdict)
    sys.exit(1 if ("--strict" in sys.argv and hard) else 0)


if __name__ == "__main__":
    main()
