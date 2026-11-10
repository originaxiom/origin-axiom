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
  +  fresh-clone suite   fresh_clone_suite  the FULL suite in a fresh clone, a separate step: --fresh-clone-suite <log> [--head <c>] (R73-7)
"""
import os, sys, re, json, hashlib, subprocess, pathlib, random, collections

ROOT = pathlib.Path(__file__).resolve().parents[2]
MIRRORS = ("origin", "backup")            # the remotes that mirror THIS repository (R67-1, B1709: the owner's mirror is the LaCie
                                          # bare repository, `git push backup`, since R66-1; Codeberg is disabled); any other remote is named and not read

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

def sealed_hash_lines(text):
    """the paths a hash file records at their SEALED version ('# sealed at <commit>: <sha256>  <path> ...' comment lines)"""
    return {m.group(2) for m in re.finditer(r"^#\s*sealed at [0-9a-f]{7,40}:\s*([0-9a-f]{64})\s+\*?(\S+)", text, re.M)}

def on_mirror(commit, remote, root=None):
    """R67-1 (B1709): is `commit` on the mirror's main?  Through the remote-tracking ref when there is one; for a mirror
    pushed to but never fetched (a local bare repository, like `backup`), in that repository itself."""
    root = root or ROOT
    run = lambda *a: subprocess.run(list(a), cwd=root, capture_output=True, text=True)
    if run("git", "rev-parse", "--verify", "-q", remote + "/main").returncode == 0:
        return run("git", "merge-base", "--is-ancestor", commit, remote + "/main").returncode == 0
    url = run("git", "remote", "get-url", remote).stdout.strip()
    if url and os.path.isdir(url):
        full = run("git", "rev-parse", commit).stdout.strip() or commit
        return run("git", "--git-dir", url, "merge-base", "--is-ancestor", full, "main").returncode == 0
    return False


def resolve_hashed(root, arc, rel):
    """R68-1 (2026-10-24): a path in an arc's ARTIFACT_HASHES is relative to the arc (its instruments) or, failing that, to
    the repository (the dependencies a seal pins in place, e.g. frontier/B1723_.../b1656_funcs.py); None when neither exists."""
    root = pathlib.Path(root)
    for f in ((root / arc / rel), (root / rel)):
        if f.resolve().exists(): return f.resolve()
    return None

def seal_check(hash_text, read_file, seal_commit, verdict_commit, is_ancestor, remotes_have, disclosure_text="", sealed_copy=None, by_hash=None):
    """one arc: hashes against the files as they are now; the seal strictly before the verdict; the seal on every remote.
    R61-4: a file changed after the seal is DISCLOSED when the arc's own pages (`disclosure_text`: FINDINGS and addenda) name
    it AND the arc keeps its sealed run (`sealed_copy(rel)` true -- a sealed_run directory or file; the sealed instrument itself
    is in git at the seal commit) or the hash file records the file's sealed hash on a '# sealed at' line.  Disclosed changes are reported, not counted as defects; an undisclosed change is a defect as before."""
    good, bad = parse_hash_file(hash_text); changed, missing, ok = [], [], 0
    # S299 (Review 74): a STAGED table (B1823's: the plan, then each disclosed post-plan change re-hashed, then the final
    # state) hashes one path several times; only its last hash is the file's claimed state, the earlier ones are superseded
    # in the table itself.  A missing file whose hash another file of the arc carries was RENAMED (`by_hash`), not lost.
    last = {}
    for k, (h, rel) in enumerate(good): last[rel] = k
    superseded = len(good) - len(last); renamed = []
    for k, (h, rel) in enumerate(good):
        if last[rel] != k: continue
        data = read_file(rel)
        if data is None:
            other = by_hash(h) if by_hash else None
            if other: renamed.append("%s -> %s" % (rel, other)); ok += 1
            else: missing.append(rel)
        elif hashlib.sha256(data).hexdigest() == h: ok += 1
        else: changed.append(rel)
    kept = sealed_hash_lines(hash_text)
    def disclosed(rel):
        named = os.path.basename(rel) in disclosure_text
        return named and (rel in kept or bool(sealed_copy and sealed_copy(rel)))
    changed_disclosed = [r for r in changed if disclosed(r)]
    changed = [r for r in changed if not disclosed(r)]
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
    return dict(ok=ok, lines=len(good) - superseded, order=order, on_remotes=bool(remotes_have), defects=defects, changed_disclosed=changed_disclosed,
                superseded_in_table=superseded, renamed=renamed)

NEGATION = ("nothing here is", "nothing is", " not ", " no ", "never", "without", "has not", "have not", "is not", "are not")   # = gates.PRETENSE_NEGATION

def provenance_hits(added_lines, phrases=PHRASES, negation=NEGATION):
    """added_lines: [(path, text)] lines added in the window; a hit is a phrase of external-verification pretense.
    S299 (Review 74): a phrase preceded within 48 characters by a negation is a DISCLAIMER, not a pretense -- the window
    the gate `pretense-phrases` has used since B1464; without it Review 74's first run reported three disclaimers."""
    hits = []
    for path, text in added_lines:
        low = text.lower()
        for ph in phrases:
            k = low.find(ph)
            while k >= 0 and any(n in low[max(0, k - 48):k] for n in negation): k = low.find(ph, k + 1)
            if k >= 0: hits.append(dict(path=path, phrase=ph, text=text.strip()[:200])); break
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

LINEAGE_RE = re.compile(r"(?:carried (?:from|to Review \d+ as|as)|before it|itself from|\bex-|restated as)\s*((?:R\d+-\d+[a-z]?(?:\s*(?:,|and|/)\s*)?)+)")

def _lineage(line):
    """the review keys a carried line names as its own lineage: written before the colon (Reviews 55-58's convention) or in
    a carry phrase anywhere on the line ('carried from R72-3, before it R71-8', 'carried to Review 73 as R73-1', 'ex-R54-1')
    -- the convention since about Review 62, which re-keys each carry and writes its lineage after the colon"""
    ids = set(re.findall(r"R\d+-\d+[a-z]?", line.split(":")[0]))
    for m in LINEAGE_RE.finditer(line): ids |= set(re.findall(r"R\d+-\d+[a-z]?", m.group(1)))
    return ids

def action_loop(reviews_text):
    """the last review's action block, and for each carried item how many reviews it has been carried through.
    S299 (Review 74): the age follows the item's LINEAGE across re-keyings (union of the keys its carry phrases name), counted
    as the number of review blocks the lineage is CARRIED INTO (an earlier review's key, or a line naming its origin).  Counting only the keys before the colon -- the rule
    as built at Review 58 -- restarted every re-keyed carry at 1, so the third-carry rule could never fire (R71-8 -> R72-3 ->
    R73-1 read as carried once)."""
    blocks = [(int(m.group(1)), m.start()) for m in re.finditer(r"^### Action items \(Review (\d+)\)", reviews_text, re.M)]
    if not blocks: return dict(review=None, open=[], carried=[], superseded_open=[])
    blocks.sort(); spans = []
    for (n, a), nxt in zip(blocks, blocks[1:] + [(None, len(reviews_text))]):
        end = reviews_text.find("\n# ", a); end = nxt[1] if end < 0 or end > nxt[1] else end
        spans.append((n, reviews_text[a:end]))
    parent = {}
    def find(x):
        parent.setdefault(x, x)
        while parent[x] != x: parent[x] = parent[parent[x]]; x = parent[x]
        return x
    def union(a, b): parent[find(a)] = find(b)
    status = {}; seen_in = []
    FROM = re.compile(r"carried from|before it|itself from|\bex-R\d")
    for n, body in spans:
        for line in body.splitlines():
            m = ITEM_RE.match(line)
            if not m: continue
            own = m.group(2)
            ids = [own] + (sorted(set(re.findall(r"R\d+-\d+[a-z]?", line.split(":")[0])) - {own}) if m.group(1) == ">" else [])
            for i in set(ids):
                status[(n, i)] = m.group(1)
            for i in _lineage(line) | set(ids): union(own, i)
            # a line CARRIES the item INTO block n when its key is an earlier review's, or it names where it came from;
            # a line whose key is block n's own and that names no origin is where the item was raised (not a carry)
            carried_in = int(re.match(r"R(\d+)-", own).group(1)) < n or bool(FROM.search(line))
            seen_in.append((n, ids, carried_in))
    blocks_of = collections.defaultdict(set)
    for n, ids, carried_in in seen_in:
        if carried_in:
            for i in ids: blocks_of[find(i)].add(n)
    last_n, last_body = spans[-1]
    openi = [i for (n, i), s in status.items() if n == last_n and s == " "]
    carried = sorted(((i, len(blocks_of[find(i)])) for (n, i), s in status.items() if n == last_n and s == ">"), key=lambda t: (-t[1], t[0]))
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
    reproduction belt THERE -- what a reader with only the repository gets.  Returns dict(status, commit, detail).
    The clone also receives root's remote-tracking refs, as `fresh_clone_suite` does and as a clone of the published
    repository carries its branches (Review 77, 2026-11-10: without them the `seal-order-unshown` gate, added in that
    window, could not see B1670's order on its kept referee branch and failed in this clone only)."""
    import tempfile, subprocess, shutil
    tmp = tempfile.mkdtemp(prefix="oa-fresh-clone-"); detail = []
    try:
        subprocess.run(["git", "clone", "--quiet", "--no-local", str(root), tmp], check=True, capture_output=True, text=True, timeout=timeout)
        subprocess.run(["git", "checkout", "--quiet", head], cwd=tmp, check=True, capture_output=True, text=True, timeout=timeout)
        subprocess.run(["git", "fetch", "--quiet", str(root), "+refs/remotes/origin/*:refs/remotes/origin/*"], cwd=tmp, capture_output=True, text=True, timeout=timeout)
        commit = subprocess.run(["git", "rev-parse", "--short", "HEAD"], cwd=tmp, capture_output=True, text=True).stdout.strip()
        status = "PASS"
        g = subprocess.run([sys.executable, "scripts/gates/gates.py"], cwd=tmp, capture_output=True, text=True, timeout=timeout)
        # a gate that SKIPS in a fresh clone checked nothing there: it counts against the clone (the advisor seat's audit, G5)
        fails = [l.strip() for l in g.stdout.splitlines() if l.strip().startswith(("FAIL", "SKIP"))]
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

def suite_summary(log_text):
    """R73-7 (S299): a pytest log's summary -- the counts of its last summary line and the failing or erroring test ids"""
    lines = re.findall(r"^=*\s*(\d+ (?:passed|failed).*?) in [\d.]+s", log_text, re.M)
    counts = {}
    if lines:
        for n, k in re.findall(r"(\d+) (passed|failed|skipped|errors?|xfailed|xpassed|warnings?)", lines[-1]):
            counts[{"error": "errors", "warning": "warnings"}.get(k, k)] = int(n)
    failing = sorted(set(re.findall(r"^(?:FAILED|ERROR) (\S+)", log_text, re.M)))
    return dict(counts=counts, failing=failing)

def fresh_clone_suite(root, head="HEAD", log_path=None, workers=8, timeout=7200):
    """R73-7 (S299): the FULL suite in a fresh clone of `root` at `head` -- what a reader with only the repository gets, at
    the scale of every lock, not only the gates (P-511's run at Review 73 found E94's ignored outputs this way).  The clone
    also receives root's remote-tracking refs, as a clone of the published repository would carry its branches (B1306's
    slice D reads them).  Single-threaded BLAS per worker, `workers` processes (the CPU rule: at most 8 of 16), nice 10."""
    import tempfile, subprocess, shutil
    tmp = tempfile.mkdtemp(prefix="oa-fresh-suite-")
    try:
        subprocess.run(["git", "clone", "--quiet", "--no-local", str(root), tmp], check=True, capture_output=True, text=True, timeout=timeout)
        subprocess.run(["git", "checkout", "--quiet", head], cwd=tmp, check=True, capture_output=True, text=True, timeout=timeout)
        subprocess.run(["git", "fetch", "--quiet", str(root), "+refs/remotes/origin/*:refs/remotes/origin/*"], cwd=tmp, capture_output=True, text=True, timeout=timeout)
        commit = subprocess.run(["git", "rev-parse", "--short", "HEAD"], cwd=tmp, capture_output=True, text=True).stdout.strip()
        env = dict(os.environ, OMP_NUM_THREADS="1", OPENBLAS_NUM_THREADS="1", MKL_NUM_THREADS="1", VECLIB_MAXIMUM_THREADS="1")
        r = subprocess.run(["nice", "-n", "10", sys.executable, "-m", "pytest", "-q", "-p", "no:randomly", "-p", "no:cacheprovider", "-n", str(workers)],
                           cwd=tmp, capture_output=True, text=True, timeout=timeout, env=env)
        log = r.stdout + r.stderr
        if log_path: pathlib.Path(log_path).write_text(log + "\nSUITE_EXIT %d\n" % r.returncode, encoding="utf-8")
        s = suite_summary(log)
        return dict(status="PASS" if r.returncode == 0 else "FAIL", commit=commit, counts=s["counts"], failing=s["failing"])
    except Exception as ex:
        return dict(status="FAIL", commit="?", counts={}, failing=[], detail=("%s: %s" % (type(ex).__name__, ex))[:300])
    finally:
        shutil.rmtree(tmp, ignore_errors=True)

def render_suite(s):
    c = s.get("counts", {})
    return "fresh-clone suite: %s @ %s (%s)%s" % (s.get("status"), s.get("commit"), ", ".join("%d %s" % (v, k) for k, v in c.items()) or s.get("detail", "no summary"),
                                                  ("; failing: " + ", ".join(s["failing"])) if s.get("failing") else "")

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
        hdir = pathlib.Path(p).parent
        arc = pathlib.Path(*pathlib.Path(p).parts[:2])          # S299: frontier/B<n>_..., also when the table sits in verification/ (B1823)
        sc = git("log", "--diff-filter=A", "--format=%h", "--", p).split()[-1]
        vc = (git("log", "--diff-filter=A", "--format=%h", "--", str(arc / "arc_verdict.json")).split() or [None])[-1]
        anc = lambda a, b: subprocess.run(["git", "merge-base", "--is-ancestor", a, b], cwd=ROOT).returncode == 0
        rd = lambda rel, arc=arc, hdir=hdir: (lambda f: f.read_bytes() if f is not None else None)(resolve_hashed(ROOT, hdir, rel) or resolve_hashed(ROOT, arc, rel))
        def bh(h, arc=arc):
            for f in sorted((ROOT / arc).rglob("*")):
                if f.is_file() and f.stat().st_size < 50_000_000 and hashlib.sha256(f.read_bytes()).hexdigest() == h: return str(f.relative_to(ROOT / arc))
            return None
        pages = "".join(f.read_text(errors="replace") for f in sorted((ROOT / arc).glob("*.md")) if f.name != "PREREGISTRATION.md")
        kept = lambda rel, arc=arc: any("sealed_run" in q.name for q in (ROOT / arc).rglob("*sealed_run*"))   # the arc keeps its sealed run (R61-4's wording); the sealed instrument is in git at the seal
        c = seal_check((ROOT / p).read_text(), rd, sc, vc, anc, all(on_mirror(sc, r) for r in remotes), pages, kept, bh)
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
    # R55-2 (B1464): CHAIN_COVERAGE's criterion says the review adjudicates the reporter's ranked list; the reporter is run here
    try:
        cg = subprocess.run([sys.executable, str(ROOT / "scripts/checks/coverage_candidates.py"), "--chain-gap"], capture_output=True, text=True, timeout=600).stdout
        top = re.findall(r"^\s+(B\d+)\s+on (\d+) surface", cg, re.M)[:8]
        tot = re.search(r"CHAIN-GAP[^:]*: (\d+)", cg)
        R["chain_gap"] = dict(total=int(tot.group(1)) if tot else None, top=[(a, int(n)) for a, n in top])
    except Exception as ex:
        R["chain_gap"] = dict(error=str(ex)[:200])
    return R

def render(R):
    w = R["window"]; L = []
    L.append("window %s..%s: %d commits (%d on the first-parent line), %d arcs with a verdict (%s … %s)" % (w["anchor"], w["head"], w["commits"], w["first_parent"], w["arcs_n"], w["arcs"][0] if w["arcs"] else "-", w["arcs"][-1] if w["arcs"] else "-"))
    rm = R["remotes"]; L.append("remotes: mirrors %s; missing mirrors %s; other remotes not read: %s" % (rm["mirrors"], rm["missing_mirrors"] or "none", rm["ignored"] or "none"))
    lp = R["loop"]; L.append("loop: Review %s block -- open %s; carried %d (oldest: %s); open items left in superseded blocks: %s" % (lp["review"], lp["open"] or "none", len(lp["carried"]), lp["carried"][:4], lp["superseded_open"] or "none"))
    b = R["branches"]; L.append("branches: %d unmerged leaves; unregistered: %s; on one remote only: %s; remotes out of step: %s" % (len(b["rows"]), b["unregistered"] or "none", b["on_one_remote_only"] or "none", b["out_of_step"] or "none"))
    for d in b["rows"]: L.append("   %-40s +%d  tip %s  %s" % (d["leaf"], d["ahead_of_main"], d["tip_date"], "registered" if d["registered"] else "UNREGISTERED"))
    L.append("seals: %d in the window; with defects: %d" % (len(R["seals"]), sum(1 for s in R["seals"] if s["defects"])))
    for s in R["seals"]: L.append("   %-52s %d/%d hashes, %s%s%s%s%s" % (s["arc"][:52], s["ok"], s["lines"], s["order"], ("  DEFECTS: " + "; ".join(s["defects"])) if s["defects"] else "", ("  disclosed post-seal: " + ", ".join(s.get("changed_disclosed", []))) if s.get("changed_disclosed") else "",
                                                                  ("  superseded in the table: %d" % s["superseded_in_table"]) if s.get("superseded_in_table") else "", ("  renamed: " + ", ".join(s["renamed"])) if s.get("renamed") else ""))
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
    cg = R.get("chain_gap") or {}
    if cg: L.append("chain gap (the review adjudicates the top; promotions are pinned in docs/CHAIN_COVERAGE.json): %s of the record's arcs on a surface and not in the chain; top: %s" % (cg.get("total"), ", ".join("%s (%d)" % t for t in cg.get("top", [])) or cg.get("error")))
    L.append("sample seed: %s; to be read in full (seeded by the anchor): %s" % (w["anchor"], ", ".join(R["sample"])))
    return "\n".join(L)

if __name__ == "__main__":
    if "--fresh-clone-suite" in sys.argv:          # R73-7: `--fresh-clone-suite <log> [--head <commit>]`, a separate step (about 40 min at 8 workers)
        log = sys.argv[sys.argv.index("--fresh-clone-suite") + 1]
        hd = sys.argv[sys.argv.index("--head") + 1] if "--head" in sys.argv else "HEAD"
        s = fresh_clone_suite(ROOT, hd, log); print(render_suite(s))
        json.dump(s, open(log + ".json", "w"), indent=1)
        sys.exit(0)
    a = sys.argv[sys.argv.index("--anchor") + 1] if "--anchor" in sys.argv else last_anchor()
    R = gather(a); print(render(R))
    if "--json" in sys.argv: json.dump(R, open(sys.argv[sys.argv.index("--json") + 1], "w"), indent=1, default=str)
