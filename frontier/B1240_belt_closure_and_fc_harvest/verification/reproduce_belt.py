#!/usr/bin/env python3
"""reproduce_belt.py -- the two ways a `reproduce.sh` belt can be green without reproducing (B1240).

Failure class (E57, extended here): a lock that reads a STRING instead of running a TOOL, and a runner
whose tool is not in the tracked tree.  Both leave the local suite green and a fresh clone unable to
reproduce.  fc's Phase-B synthesis named the first shape (L197(b)); this instrument computes both on
the live tree and is the belt's ratchet.

  --string-locks   tests/test_b*.py whose only REPRODUCES check is `"REPRODUCES" in <text>` with no
                   subprocess run anywhere in the file (the B1160 shape, tests.tsv SELF_REFERENTIAL_LOCK)
  --runners        frontier/*/verification/reproduce*.sh: every relative file the runner or the
                   certificates it names refer to, that is NOT tracked (absent or untracked); a runner
                   that cannot run on a fresh clone is listed with the missing files
  --inert          runners that RECOMPUTE nothing: PINS-TEXT (grep/diff only -- a text pin on tracked files) or
                   INERT (echo only; honest when it says RECORD, B1175; the class's third shape if it says REPRODUCES)
  --selftest       planted controls in both directions (MB12)
  (default)        both reports + counts; exit 0 always (the ratchet lives in the test that reads the JSON)

Writes nothing unless --json PATH is given.
"""
import argparse, json, os, re, subprocess, sys
ROOT = os.environ.get("OA_ROOT") or os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

def tracked():
    out = subprocess.run(["git", "ls-files"], cwd=ROOT, capture_output=True, text=True, check=True).stdout
    return set(out.split("\n")) - {""}

STRING_LOCK = re.compile(r'["\']REPRODUCES["\']\s+in\s+\w')
RUNS = re.compile(r"subprocess\.(?:run|check_output|check_call|call|Popen)")

def string_locks(files=None):
    hits = []
    files = files or sorted(f for f in tracked() if f.startswith("tests/test_b") and f.endswith(".py"))
    for rel in files:
        try:
            t = open(os.path.join(ROOT, rel), encoding="utf-8").read()
        except OSError:
            continue
        if "REPRODUCES" in t and STRING_LOCK.search(t) and not RUNS.search(t):
            hits.append(rel)
    return hits

# references a runner (or a certificate it names) can make, relative to the runner's directory
REF = re.compile(r'(?<![\w/$}])((?:\.\./)*(?:certificates|outputs|verification|frontier|scripts|docs|tests|[\w-]+)/[\w./-]+\.(?:py|txt|sh|json|csv))')
CERT_LIST = re.compile(r'^CERTS="([^"]+)"', re.M)
SH_DEFAULT = re.compile(r"\$\{(\w+):-([^}]*)\}")
PY_CALL = re.compile(r'python3?\s+(?:-u\s+)?"?([\w./-]+\.py)"?')
EXEC_SIB = re.compile(r"open\(\s*\w+\s*\+\s*[\x22\x27]/([\w./-]+)[\x22\x27]")
LOAD_SIB = re.compile(r"(?:\+\s*|join\(\s*\w+\s*,\s*)[\x22\x27]/?([\w./-]+\.(?:py|txt|json|csv))[\x22\x27]")

def runner_refs(runner_rel, tr):
    """files a runner needs, resolved relative to its directory; returns (needed, missing)."""
    rdir = os.path.dirname(runner_rel)
    raw = open(os.path.join(ROOT, runner_rel), encoding="utf-8").read()
    # comment lines describe, they do not run: drop them before extracting references
    txt = "\n".join(l for l in raw.split("\n") if not l.lstrip().startswith("#"))
    # a shell default `${CERTS:-a b c}` names a, b, c: expand it to its default before extracting
    txt = SH_DEFAULT.sub(r"\2", txt)
    needed = set()
    # explicit CERTS lists -> certificates/<c>.py and outputs/<c>_out.txt when the runner diffs against outputs
    for m in CERT_LIST.finditer(txt):
        for c in m.group(1).split():
            needed.add(f"certificates/{c}.py")
            if "outputs/" in txt:
                needed.add(f"outputs/{c}_out.txt")
    for m in PY_CALL.finditer(txt):
        p = m.group(1)
        if "$" in p or "{" in p:
            continue
        needed.add(p)
    for m in REF.finditer(txt):
        p = m.group(1)
        if "$" in p or "{" in p:
            continue
        needed.add(p)
    # transitive: a certificate that execs / loads a sibling
    frontier = set()
    for p in list(needed):
        if p.endswith(".py"):
            fp = next((os.path.join(ROOT, os.path.normpath(os.path.join(b, p))) for b in (rdir, os.path.dirname(rdir), "")
                       if os.path.isfile(os.path.join(ROOT, os.path.normpath(os.path.join(b, p))))), None)
            if fp:
                src = open(fp, encoding="utf-8", errors="ignore").read()
                for mm in list(EXEC_SIB.finditer(src)) + list(LOAD_SIB.finditer(src)):
                    ref = mm.group(1)
                    # a loaded path that already resolves from the repo root is root-relative, not a sibling
                    if "/" in ref and os.path.isfile(os.path.join(ROOT, ref)):
                        frontier.add(ref)
                    else:
                        frontier.add(os.path.join(os.path.dirname(p), ref))
    needed |= frontier
    # a runner may `cd` to its own dir, the arc root, or the repo root before running: a file counts as
    # present if it is tracked under ANY of the three bases (conservative -- a true miss is absent under all)
    bases = [rdir, os.path.dirname(rdir), ""]
    resolved, missing = [], []
    for p in sorted(needed):
        cands = [os.path.normpath(os.path.join(b, p)) for b in bases]
        hit = next((c for c in cands if c in tr), None)
        resolved.append(hit or cands[0])
        if hit is None:
            missing.append(cands[0])
    return resolved, missing

EXEC_LINE = re.compile(r"(?:^|[\s;&|(=`])(?:python3?|bash|sh|sage|gp|magma|julia|make|pytest)\s")
PIN_LINE = re.compile(r"(?:^|[\s;&|(=`])(?:grep|diff|cmp|test|\[)\s")

def inert_runners(tr=None):
    """classify every runner by what its non-comment lines EXECUTE: RECOMPUTES (a python/bash/... invocation
    anywhere on a line), PINS-TEXT (only grep/diff/cmp/test -- a text pin on tracked files, no tool run),
    INERT (neither: echo only -- the B1175 shape, honest when the runner says RECORD, the E57 class's third
    shape when it says REPRODUCES).  Returns the PINS-TEXT and INERT runners."""
    tr = tr or tracked()
    out = []
    for rel in sorted(tr):
        if not (rel.startswith("frontier/") and "/verification/" in rel and re.search(r"/reproduce[\w-]*\.sh$", rel)):
            continue
        raw = open(os.path.join(ROOT, rel), encoding="utf-8", errors="ignore").read()
        body = "\n".join(l for l in raw.split("\n") if not l.lstrip().startswith("#"))
        if EXEC_LINE.search(body):
            continue
        kind = "PINS-TEXT" if PIN_LINE.search(body) else "INERT"
        out.append({"runner": rel, "kind": kind, "says_reproduces": "REPRODUCES" in body, "says_record": "RECORD" in body})
    return out

def runners_report(tr=None):
    tr = tr or tracked()
    rep = []
    for rel in sorted(tr):
        if not (rel.startswith("frontier/") and "/verification/" in rel and re.search(r"/reproduce[\w-]*\.sh$", rel)):
            continue
        needed, missing = runner_refs(rel, tr)
        rep.append({"runner": rel, "needed": len(needed), "missing": missing})
    return rep

def selftest():
    import tempfile
    # string-lock detector: positive and negative controls
    pos = 'def test_x():\n    assert "REPRODUCES" in open("a").read()\n'
    neg = 'import subprocess\ndef test_x():\n    r = subprocess.run(["bash","reproduce.sh"], capture_output=True, text=True)\n    assert "REPRODUCES" in r.stdout\n'
    assert STRING_LOCK.search(pos) and not RUNS.search(pos), "positive control failed"
    assert not (STRING_LOCK.search(neg) and not RUNS.search(neg)), "negative control failed"
    # runner detector: a runner naming a cert that is absent must be MISSING; one naming a tracked file must not
    tr = {"frontier/X/verification/reproduce.sh", "frontier/X/verification/certificates/present.py"}
    with tempfile.TemporaryDirectory() as d:
        global ROOT
        old = ROOT; ROOT = d
        # fixture paths built from components: a literal "…/present.py" here would be read by LOAD_SIB as a
        # dependency of any runner that calls this very script (the instrument must not scan its own fixtures)
        fx = lambda *p: os.path.join(d, "frontier", "X", "verification", *p)
        os.makedirs(fx("certificates"))
        open(fx("reproduce.sh"), "w").write('CERTS="present absent"\nfor c in $CERTS; do python3 "certificates/$c.py"; done\n')
        open(fx("certificates", "present.py"), "w").write("print(1)\n")
        needed, missing = runner_refs("frontier/X/verification/reproduce.sh", tr)
        # the overridable form the B1240 runners carry: `${CERTS:-present absent}` must name the same two files
        open(fx("reproduce.sh"), "w").write('CERTS="${CERTS:-present absent}"\nfor c in $CERTS; do python3 "certificates/$c.py"; done\n')
        needed2, missing2 = runner_refs("frontier/X/verification/reproduce.sh", tr)
        ROOT = old
    assert "frontier/X/verification/certificates/absent.py" in missing, missing
    assert "frontier/X/verification/certificates/present.py" not in missing, missing
    assert (needed2, missing2) == (needed, missing) and not any("$" in m or "{" in m for m in needed2), (needed2, missing2)
    # inert detector: a runner with only echo lines is inert; one with a python3 line is not
    assert not EXEC_LINE.search('echo "RECORD: verified at bank time"\n'), "inert positive control failed"
    assert EXEC_LINE.search('cd x\npython3 -u cert.py\n'), "inert negative control failed"
    assert EXEC_LINE.search('  if out=$(python3 "$s.py" 2>&1); then\n'), "inert nested-call control failed"
    assert PIN_LINE.search('grep -q "X" file && echo OK\n') and not EXEC_LINE.search('grep -q "X" file && echo OK\n'), "pin control failed"
    print("selftest: 9/9 controls pass (string-lock +/-, runner missing/present, shell-default form, exec +/-/nested, pin)")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--string-locks", action="store_true")
    ap.add_argument("--runners", action="store_true")
    ap.add_argument("--inert", action="store_true")
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--json")
    a = ap.parse_args()
    if a.selftest:
        selftest(); return
    tr = tracked()
    out = {}
    only = a.string_locks or a.runners or a.inert
    if a.string_locks or not only:
        sl = string_locks()
        out["string_locks"] = sl
        print(f"string-only REPRODUCES locks (no subprocess in file): {len(sl)}")
        for f in sl: print("  ", f)
    if a.inert or not only:
        ir = inert_runners(tr)
        out["inert"] = ir
        print(f"runners that recompute nothing: {len(ir)} ({sum(r['kind']=='PINS-TEXT' for r in ir)} PINS-TEXT, {sum(r['kind']=='INERT' for r in ir)} INERT)")
        for r in ir: print("  ", r["runner"], r["kind"], "says REPRODUCES" if r["says_reproduces"] else "", "says RECORD" if r["says_record"] else "")
    if a.runners or not only:
        rr = runners_report(tr)
        bad = [r for r in rr if r["missing"]]
        out["runners"] = rr
        print(f"runners scanned: {len(rr)}; runners with untracked/absent inputs: {len(bad)}")
        for r in bad:
            print("  ", r["runner"], "->", ", ".join(os.path.relpath(m, os.path.dirname(r["runner"])) for m in r["missing"][:8]), ("..." if len(r["missing"]) > 8 else ""))
    if a.json:
        json.dump(out, open(a.json, "w"), indent=1)

if __name__ == "__main__":
    main()
