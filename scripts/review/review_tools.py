#!/usr/bin/env python3
"""The mechanical half of the decadal review, as tools.

Each check is a pure function of its inputs (lists and strings) and can fail on planted input; thin wrappers
gather the inputs from git and the tree.  `python3 scripts/review/review_tools.py [--anchor <commit>] [--json out]`
prints the draft of a review's mechanical sections.  The judgement half -- what the window means, what is promoted --
is not here and is not meant to be.

Template sections covered (docs/progress/REVIEW_TEMPLATE.md):
  1  the loop            action_loop        open items of the last block; how many reviews each carried item has aged
  1b branch inventory    branch_inventory   every unmerged remote ref, matched on its LEAF (R57-1b)
  2  declared modulus    window, sample_draw  what the window holds; a SEEDED draw of the arcs to be read in full
  3  advancement         table_rows_added   LAW_MAP and THEOREM_REGISTRY rows added in the window
  4  error recurrence    error_rows         ERROR_LEDGER rows added: new classes against instances
  5  provenance          provenance_hits, unglossed_terms
  7  protocol integrity  seal_integrity     hashes unchanged, sealed before results, seal on every remote
  +  gates               gate_controls      every gate has a test that names it (a gate nobody tests can be inert)
  +  relays              relay_split        the open rows by direction (R55-3)
"""
import os, sys, re, json, hashlib, subprocess, pathlib, random, collections

ROOT = pathlib.Path(__file__).resolve().parents[2]
MIRRORS = ("origin", "codeberg")          # the remotes that mirror THIS repository; any other remote is named in the report and not read

# ------------------------------------------------------------------ pure checks
PHRASES = ["independently verified", "externally verified", "peer-reviewed", "peer reviewed", "third-party verif", "third party verif",
           "confirmed by experts", "verified by an independent", "verified by an external"]
ARC_RE = re.compile(r"\bB(\d{1,4})\b")
ITEM_RE = re.compile(r"^- \[(.)\] (R\d+-\d+[a-z]?)")

def leaf(ref):
    return ref.rsplit("/", 1)[-1]

def branch_inventory(unmerged, registered_keys):
    """unmerged: {remote: [full refs without the remote prefix]}; registered_keys: text of the registers.
    A ref is registered when its LEAF occurs in the registers (the full ref never does: R57-1b)."""
    out = {}
    for remote, refs in unmerged.items():
        for ref in refs:
            d = out.setdefault(leaf(ref), dict(leaf=leaf(ref), refs={}, registered=leaf(ref) in registered_keys))
            d["refs"][remote] = ref
    rows = sorted(out.values(), key=lambda d: d["leaf"])
    return dict(rows=rows, unregistered=[d["leaf"] for d in rows if not d["registered"]],
                on_one_remote_only=[d["leaf"] for d in rows if len(d["refs"]) == 1])

def parse_hash_file(text):
    """(sha256, relative path) lines; anything else is a comment.  Returns (lines, unparsed non-comment lines)."""
    good, bad = [], []
    for line in text.splitlines():
        s = line.strip()
        if not s or s.startswith("#"): continue
        m = re.match(r"^([0-9a-f]{64})\s+\*?(\S.*)$", s)
        if not m:
            m2 = re.match(r"^(\S+)\s+sha256\s+([0-9a-f]{64})$", s)          # B1410's layout: <path>  sha256  <hash>
            if m2: good.append((m2.group(2), m2.group(1))); continue
        (good if m else bad).append((m.group(1), m.group(2)) if m else s)
    return good, bad

def seal_check(hash_text, read_file, seal_commit, verdict_commit, is_ancestor, remotes_have):
    """one arc: hashes against the files as they are now; the seal strictly before the verdict; the seal on every remote"""
    good, bad = parse_hash_file(hash_text); changed, missing, ok = [], [], 0
    for h, rel in good:
        data = read_file(rel)
        if data is None: missing.append(rel)
        elif hashlib.sha256(data).hexdigest() == h: ok += 1
        else: changed.append(rel)
    if verdict_commit is None: order = "no verdict yet"
    elif seal_commit == verdict_commit: order = "SEALED WITH ITS RESULTS"
    elif is_ancestor(seal_commit, verdict_commit): order = "sealed before results"
    else: order = "SEAL NOT AN ANCESTOR OF THE RESULTS"
    defects = []
    if not good: defects.append("no hash line parsed")
    if bad: defects.append("%d unparsed lines" % len(bad))
    if changed: defects.append("changed: " + ", ".join(changed))
    if missing: defects.append("missing: " + ", ".join(missing))
    if order.isupper() or order.startswith("SEAL"): defects.append(order)
    if not remotes_have: defects.append("seal not on every remote")
    return dict(ok=ok, lines=len(good), order=order, on_remotes=bool(remotes_have), defects=defects)

def provenance_hits(added_lines, phrases=PHRASES):
    """added_lines: [(path, text)] lines added in the window; a hit is a phrase of external-verification pretense"""
    hits = []
    for path, text in added_lines:
        low = text.lower()
        for ph in phrases:
            if ph in low: hits.append(dict(path=path, phrase=ph, text=text.strip()[:200])); break
    return hits

def table_rows_added(diff_text):
    """rows added to a markdown table in a unified diff: the first cell of each added row"""
    rows = []
    for line in diff_text.splitlines():
        if line.startswith("+|") and not line.startswith("+|-") and not line.startswith("+| ---"):
            cell = line[2:].split("|")[0].strip()
            if cell: rows.append(cell[:160])
    return rows

def error_rows(diff_text, classes_at_anchor=()):
    """rows added to the error ledger: a class is NEW when its id heads no row at the anchor; everything else that
    is added -- an instance row, or a class row rewritten -- is counted as a recurrence of its class"""
    rows = table_rows_added(diff_text); new, inst = [], []; known = set(classes_at_anchor)
    for r in rows:
        m = re.search(r"\bE(\d+)\b", r)
        if not m: continue
        e = "E" + m.group(1)
        if "instance" not in r.lower() and e not in known: new.append(e)
        else: inst.append(e)
    return dict(new_classes=sorted(set(new), key=lambda e: int(e[1:])), instances=collections.Counter(inst))

def class_ids(ledger_text):
    return sorted(set("E" + m.group(1) for line in ledger_text.splitlines() if line.startswith("|") for m in [re.match(r"^\|\s*\**E(\d+)\b", line)] if m and "instance" not in line.split("|")[1].lower()))

def action_loop(reviews_text):
    """the last review's action block, and for each carried item how many reviews it has been carried through"""
    blocks = [(int(m.group(1)), m.start()) for m in re.finditer(r"^### Action items \(Review (\d+)\)", reviews_text, re.M)]
    if not blocks: return dict(review=None, open=[], carried=[], superseded_open=[])
    blocks.sort(); spans = []
    for (n, a), nxt in zip(blocks, blocks[1:] + [(None, len(reviews_text))]):
        end = reviews_text.find("\n# ", a); end = nxt[1] if end < 0 or end > nxt[1] else end
        spans.append((n, reviews_text[a:end]))
    carried_in = collections.Counter(); status = {}
    for n, body in spans:
        for line in body.splitlines():
            m = ITEM_RE.match(line)
            if not m: continue
            ids = [m.group(2)] + (re.findall(r"R\d+-\d+[a-z]?", line.split(":")[0]) if m.group(1) == ">" else [])
            for i in set(ids):
                status[(n, i)] = m.group(1)
                if m.group(1) == ">": carried_in[i] += 1
    last_n, last_body = spans[-1]
    openi = [i for (n, i), s in status.items() if n == last_n and s == " "]
    carried = sorted(((i, carried_in[i]) for (n, i), s in status.items() if n == last_n and s == ">"), key=lambda t: -t[1])
    superseded = [(n, i) for (n, i), s in status.items() if n != last_n and s == " "]
    return dict(review=last_n, open=sorted(openi), carried=carried, superseded_open=sorted(superseded))

STOP = set("the a an of in on at to for and or is are was were be by with from that this it its as not no one two three four all each every any which than then there here has have had can cannot does do did but if so".split())
def term_candidates(window_claims, earlier_claims, min_arcs=3):
    """word pairs carried by at least min_arcs claims of the window and by no earlier claim: the window's new vocabulary"""
    def pairs(text):
        w = re.findall(r"[a-z][a-z'\-]{2,}", text.lower()); return set(" ".join(p) for p in zip(w, w[1:]) if p[0] not in STOP and p[1] not in STOP)
    old = set()
    for c in earlier_claims: old |= pairs(c)
    cnt = collections.Counter()
    for c in window_claims: cnt.update(pairs(c) - old)
    return [t for t, n in cnt.most_common() if n >= min_arcs]
def unglossed_terms(candidates, terminology_text):
    low = terminology_text.lower()
    return [t for t in candidates if t.lower() not in low]

def gate_controls(gate_names, test_texts, registry=None):
    """a gate is controlled when some test names it (quoted, as gate_<name>, or in the test file's own name); test_texts: {file: text}.
    B1461: with `registry` (tests/GATE_CONTROLS.json as a dict) it also reports which gates have a REGISTERED failing-path test
    whose function exists in test_texts -- the core check of Review 58's governance delta."""
    out = {}
    for g in gate_names:
        fn = "gate_" + g.replace("-", "_")
        files = [f for f, t in test_texts.items() if ('"%s"' % g) in t or ("'%s'" % g) in t or fn in t or g.replace("-", "_") in f]
        out[g] = files
    res = dict(uncontrolled=sorted(g for g, f in out.items() if not f), controlled=len([g for g, f in out.items() if f]))
    if registry is not None:
        ok = []
        for g in gate_names:
            ref = registry.get(g, "")
            f, _, fnname = ref.partition("::")
            text = test_texts.get(f.split("/")[-1], "")
            if fnname and re.search(r"^def %s\(" % re.escape(fnname), text, re.M): ok.append(g)
        res["registered"] = len(ok); res["unregistered"] = sorted(g for g in gate_names if g not in ok)
    return res


def fresh_clone(root, head="HEAD", timeout=1800):
    """B1461 (the core's second check): clone `root` at `head` into a temporary directory and run the gates and the
    reproduction belt THERE -- what a reader with only the repository gets.  Returns dict(status, commit, detail)."""
    import tempfile, subprocess, shutil
    tmp = tempfile.mkdtemp(prefix="oa-fresh-clone-"); detail = []
    try:
        subprocess.run(["git", "clone", "--quiet", "--no-local", str(root), tmp], check=True, capture_output=True, text=True, timeout=timeout)
        subprocess.run(["git", "checkout", "--quiet", head], cwd=tmp, check=True, capture_output=True, text=True, timeout=timeout)
        commit = subprocess.run(["git", "rev-parse", "--short", "HEAD"], cwd=tmp, capture_output=True, text=True).stdout.strip()
        status = "PASS"
        g = subprocess.run([sys.executable, "scripts/gates/gates.py"], cwd=tmp, capture_output=True, text=True, timeout=timeout)
        fails = [l.strip() for l in g.stdout.splitlines() if l.strip().startswith("FAIL")]
        detail.append("gates %s" % ("all PASS" if g.returncode == 0 and not fails else "FAIL: " + "; ".join(fails)[:300]))
        if g.returncode != 0 or fails: status = "FAIL"
        belt = os.path.join(tmp, "scripts", "checks", "reproduce_belt.py")
        if os.path.isfile(belt):
            b = subprocess.run([sys.executable, belt], cwd=tmp, capture_output=True, text=True, timeout=timeout)
            detail.append("belt %s" % ("ok" if b.returncode == 0 else "FAIL: " + (b.stdout + b.stderr).strip().splitlines()[-1][:200] if (b.stdout + b.stderr).strip() else "FAIL"))
            if b.returncode != 0: status = "FAIL"
        return dict(status=status, commit=commit, detail="; ".join(detail))
    except Exception as ex:
        return dict(status="FAIL", commit="?", detail=("%s: %s" % (type(ex).__name__, ex))[:300])
    finally:
        shutil.rmtree(tmp, ignore_errors=True)

def relay_split(ledger_text):
    """the open rows of the relay ledger by direction (R55-3): outbound = from main (CC_TO_*), inbound = everything else"""
    out = dict(outbound=collections.Counter(), inbound=collections.Counter(), declined=0, banked=0)
    for line in ledger_text.splitlines():
        m = re.match(r"^\|\s*`?([A-Za-z0-9_.\-]+)`?[^|]*\|\s*(BANKED|DECLINED|OPEN)\s*\|", line)
        if not m: continue
        name, disp = m.group(1), m.group(2)
        if disp == "DECLINED": out["declined"] += 1
        elif disp == "BANKED": out["banked"] += 1
        else:
            t = re.match(r"^CC_TO_([A-Z0-9_]+?)_\d{4}-", name)
            if t: out["outbound"][t.group(1)] += 1
            else: out["inbound"][(re.match(r"^([A-Z0-9]+)_TO_CC", name) or re.match(r"^([A-Za-z0-9]+)", name)).group(1)] += 1
    return dict(outbound=dict(out["outbound"]), inbound=dict(out["inbound"]), declined=out["declined"], banked=out["banked"])

def sample_draw(arcs, seed, n):
    """the arcs to be read in full: a draw seeded by the window's anchor, not chosen by the reviewer"""
    rng = random.Random(seed); pool = sorted(arcs)
    return sorted(rng.sample(pool, min(n, len(pool))))

# ------------------------------------------------------------------ wrappers
def git(*a, cwd=None):
    return subprocess.run(["git", *a], capture_output=True, text=True, cwd=cwd or ROOT).stdout

def last_anchor():
    t = (ROOT / "docs/progress/REVIEWS.md").read_text()
    m = re.findall(r"anchor-commit: `([0-9a-f]{7,40})`", t)
    return m[-1] if m else None

def gather(anchor):
    R = {}
    log = [l for l in git("log", "--format=%h%x09%ad%x09%s", "--date=short", anchor + "..HEAD").splitlines() if l]
    added = [p for p in git("diff", "--name-only", "--diff-filter=A", anchor, "HEAD").splitlines() if p]
    arcs = sorted(set(m.group(1) for p in added for m in [re.match(r"frontier/(B\d{1,4})_[^/]*/arc_verdict\.json$", p)] if m), key=lambda b: int(b[1:]))
    R["window"] = dict(anchor=anchor, head=git("rev-parse", "--short", "HEAD").strip(), commits=len(log), first_parent=len(git("log", "--first-parent", "--format=%h", anchor + "..HEAD").split()),
                       arcs=arcs, arcs_n=len(arcs), sealed_commits=[l.split("\t")[0] for l in log if "sealed" in l.lower()])
    allr = [r for r in git("remote").split() if r]; remotes = [r for r in MIRRORS if r in allr]
    R["remotes"] = dict(mirrors=remotes, missing_mirrors=[r for r in MIRRORS if r not in allr], ignored=[r for r in allr if r not in MIRRORS])
    unmerged = {r: [b.strip()[len(r) + 1:] for b in git("branch", "-r", "--no-merged", "HEAD").splitlines() if b.strip().startswith(r + "/") and "->" not in b] for r in remotes}
    reg = "".join((ROOT / p).read_text() for p in ("docs/HARVEST_LEDGER.md", "docs/SEAT_REGISTER.md") if (ROOT / p).exists())
    inv = branch_inventory(unmerged, reg)
    for d in inv["rows"]:
        tips = {r: git("rev-parse", "--short", "%s/%s" % (r, ref)).strip() for r, ref in d["refs"].items()}
        d["tips"] = tips; d["in_step"] = len(set(tips.values())) == 1
        ref0 = "%s/%s" % next(iter(d["refs"].items())); d["ahead_of_main"] = int(git("rev-list", "--count", "HEAD.." + ref0).strip() or 0)
        d["tip_date"] = git("log", "-1", "--format=%ad", "--date=short", ref0).strip()
    inv["out_of_step"] = [d["leaf"] for d in inv["rows"] if not d["in_step"]]
    R["branches"] = inv
    seals = []
    for p in added:
        if not (p.startswith("frontier/") and p.endswith("ARTIFACT_HASHES.txt")): continue
        arc = pathlib.Path(p).parent
        sc = git("log", "--diff-filter=A", "--format=%h", "--", p).split()[-1]
        vc = (git("log", "--diff-filter=A", "--format=%h", "--", str(arc / "arc_verdict.json")).split() or [None])[-1]
        anc = lambda a, b: subprocess.run(["git", "merge-base", "--is-ancestor", a, b], cwd=ROOT).returncode == 0
        rd = lambda rel, arc=arc: ((ROOT / arc / rel).resolve().read_bytes() if (ROOT / arc / rel).resolve().exists() else None)
        c = seal_check((ROOT / p).read_text(), rd, sc, vc, anc, all(anc(sc, r + "/main") for r in remotes))
        c.update(arc=arc.name, seal=sc, verdict=vc); seals.append(c)
    R["seals"] = seals
    addl = []
    cur = None
    for line in git("diff", anchor, "HEAD", "--", "*.md").splitlines():
        if line.startswith("+++ b/"): cur = line[6:]
        elif line.startswith("+") and not line.startswith("+++") and cur and not cur.startswith("docs/progress/REVIEWS.md"): addl.append((cur, line[1:]))
    hits = provenance_hits(addl)
    for h in hits: h["public_facing"] = not ("/verification/" in h["path"] or "/reads_" in h["path"] or h["path"].startswith("outside_bench/"))
    R["provenance"] = dict(lines_scanned=len(addl), hits=hits)
    R["law_map_rows_added"] = table_rows_added(git("diff", anchor, "HEAD", "--", "docs/LAW_MAP.md"))
    R["theorem_rows_added"] = table_rows_added(git("diff", anchor, "HEAD", "--", "docs/THEOREM_REGISTRY.md"))
    e = error_rows(git("diff", anchor, "HEAD", "--", "docs/ERROR_LEDGER.md"), class_ids(git("show", anchor + ":docs/ERROR_LEDGER.md"))); e["instances"] = dict(e["instances"]); R["errors"] = e
    R["loop"] = action_loop((ROOT / "docs/progress/REVIEWS.md").read_text())
    claims = {}
    for p in (ROOT / "frontier").glob("B*/arc_verdict.json"):
        try: d = json.loads(p.read_text()); claims[d.get("id") or p.parent.name.split("_")[0]] = d.get("claim_one_line", "")
        except Exception: pass
    inw = set(arcs); cand = term_candidates([c for a, c in claims.items() if a in inw], [c for a, c in claims.items() if a not in inw])
    R["terms"] = dict(candidates=cand[:60], unglossed=unglossed_terms(cand, (ROOT / "TERMINOLOGY.md").read_text())[:40])
    sys.path.insert(0, str(ROOT / "scripts/gates"))
    try:
        import gates as G
        tests = {p.name: p.read_text() for p in (ROOT / "tests").glob("test_*.py")}
        regp = ROOT / "tests/GATE_CONTROLS.json"
        R["gates"] = gate_controls(sorted(G.GATES), tests, json.loads(regp.read_text()) if regp.exists() else None)
    except Exception as ex:
        R["gates"] = dict(error=str(ex)[:200])
    R["sample"] = sample_draw(arcs, anchor, max(5, len(arcs) // 6))
    R["relays"] = relay_split((ROOT / "docs/RELAY_LEDGER.md").read_text()) if (ROOT / "docs/RELAY_LEDGER.md").exists() else {}
    R["fresh_clone"] = fresh_clone(ROOT) if "--fresh-clone" in sys.argv else dict(status="NOT RUN", commit=R["window"]["head"], detail="pass --fresh-clone")
    return R

def render(R):
    w = R["window"]; L = []
    L.append("window %s..%s: %d commits (%d on the first-parent line), %d arcs with a verdict (%s … %s)" % (w["anchor"], w["head"], w["commits"], w["first_parent"], w["arcs_n"], w["arcs"][0] if w["arcs"] else "-", w["arcs"][-1] if w["arcs"] else "-"))
    rm = R["remotes"]; L.append("remotes: mirrors %s; missing mirrors %s; other remotes not read: %s" % (rm["mirrors"], rm["missing_mirrors"] or "none", rm["ignored"] or "none"))
    lp = R["loop"]; L.append("loop: Review %s block -- open %s; carried %d (oldest: %s); open items left in superseded blocks: %s" % (lp["review"], lp["open"] or "none", len(lp["carried"]), lp["carried"][:4], lp["superseded_open"] or "none"))
    b = R["branches"]; L.append("branches: %d unmerged leaves; unregistered: %s; on one remote only: %s; remotes out of step: %s" % (len(b["rows"]), b["unregistered"] or "none", b["on_one_remote_only"] or "none", b["out_of_step"] or "none"))
    for d in b["rows"]: L.append("   %-40s +%d  tip %s  %s" % (d["leaf"], d["ahead_of_main"], d["tip_date"], "registered" if d["registered"] else "UNREGISTERED"))
    L.append("seals: %d in the window; with defects: %d" % (len(R["seals"]), sum(1 for s in R["seals"] if s["defects"])))
    for s in R["seals"]: L.append("   %-52s %d/%d hashes, %s%s" % (s["arc"][:52], s["ok"], s["lines"], s["order"], ("  DEFECTS: " + "; ".join(s["defects"])) if s["defects"] else ""))
    p = R["provenance"]; L.append("provenance: %d added lines scanned, %d hits, %d in public-facing files" % (p["lines_scanned"], len(p["hits"]), sum(1 for h in p["hits"] if h["public_facing"])))
    for h in p["hits"]: L.append("   %s%s: %s" % ("" if h["public_facing"] else "(reader note) ", h["path"], h["text"][:120]))
    L.append("advancement: LAW_MAP +%d rows, THEOREM_REGISTRY +%d rows" % (len(R["law_map_rows_added"]), len(R["theorem_rows_added"])))
    e = R["errors"]; L.append("errors: new classes %s; instances %s" % (e["new_classes"] or "none", e["instances"] or "none"))
    L.append("new vocabulary (word pairs in >= 3 of the window's claims and in none before) not in TERMINOLOGY.md: %s" % (", ".join(R["terms"]["unglossed"]) or "none"))
    g = R["gates"]; L.append("gates: %s" % (g if "error" in g else "%d named by a test; not named by any: %s" % (g["controlled"], g["uncontrolled"] or "none")))
    if "registered" in g: L.append("gate controls: %d registered failing-path tests; unregistered: %s" % (g["registered"], g["unregistered"] or "none"))
    fc = R.get("fresh_clone") or {}
    if fc: L.append("fresh-clone: %s @ %s (%s)" % (fc.get("status"), fc.get("commit"), fc.get("detail")))
    rl = R.get("relays") or {}
    if rl: L.append("relays open: outbound %d %s; inbound %d %s; declined %d; banked %d" % (sum(rl["outbound"].values()), rl["outbound"], sum(rl["inbound"].values()), rl["inbound"], rl["declined"], rl["banked"]))
    L.append("sample seed: %s; to be read in full (seeded by the anchor): %s" % (w["anchor"], ", ".join(R["sample"])))
    return "\n".join(L)

if __name__ == "__main__":
    a = sys.argv[sys.argv.index("--anchor") + 1] if "--anchor" in sys.argv else last_anchor()
    R = gather(a); print(render(R))
    if "--json" in sys.argv: json.dump(R, open(sys.argv[sys.argv.index("--json") + 1], "w"), indent=1, default=str)
