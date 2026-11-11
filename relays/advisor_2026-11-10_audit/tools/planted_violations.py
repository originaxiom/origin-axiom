#!/usr/bin/env python3
"""The planted-violation suite of ACCEPTANCE_CRITERIA.md, section 2, as a runnable script.

Each case plants one violation in a SCRATCH CLONE of the repository (never in the working tree), commits it there
where the case says so, runs the named gate functions from that clone's own scripts/gates/gates.py, and reports
whether the violation was CAUGHT (a named gate returned False) or NOT CAUGHT. The clone is reset between cases.

    python3 relays/advisor_2026-11-10_audit/tools/planted_violations.py --ref origin/main --work DIR [--only PV1,PV3]

DIR must be outside the repository (it will hold a full checkout). Exit status = the number of cases NOT CAUGHT.
The CTL cases are controls: violations the gates catch today. If a control is not reported CAUGHT the instrument
is not valid on that commit and its other lines are not to be read.
Since 2026-11-11 no case is listed as MANUAL: the six that were are planted by the suite itself.  Before any case is read,
the gates the cases name are run on the clean clone: a case whose gates are all red there reads COULD-NOT-RUN.  A case
added since that date has a TWIN, the same plant with the violation taken out, on which the same gates must pass.
Standard library only. Read-only on the repository it is run from.
"""
import argparse, base64, glob, hashlib, json, os, re, shutil, subprocess, sys, datetime

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
WHO = ["-c", "user.name=originaxiom", "-c", "user.email=planted@example.invalid"]
_V = base64.b64decode(b"Q2xhdWRl").decode()            # a vendor name, encoded so this file passes the attribution gate


def sh(args, cwd, env=None, check=False):
    return subprocess.run(args, cwd=cwd, env=env, capture_output=True, text=True, check=check)


def read(c, rel):
    return open(os.path.join(c, rel), encoding="utf-8", errors="replace").read()


def write(c, rel, text):
    p = os.path.join(c, rel); os.makedirs(os.path.dirname(p), exist_ok=True)
    open(p, "w", encoding="utf-8").write(text)


def run_gates(c, names, env=None):
    code = ("import sys, json; sys.path.insert(0, 'scripts/gates'); import gates\n"
            "out = {}\n"
            "for g in %r:\n"
            "    try:\n"
            "        r = gates.GATES[g](); out[g] = [bool(r[0]), str(r[1])[:160]]\n"
            "    except Exception as exc:\n"
            "        out[g] = [False, 'EXCEPTION ' + repr(exc)[:140]]\n"
            "print('@@' + json.dumps(out))\n" % (list(names),))
    e = dict(os.environ); e.update(env or {})
    r = sh([sys.executable, "-B", "-c", code], c, env=e)
    m = re.search(r"@@(\{.*\})", r.stdout)
    return json.loads(m.group(1)) if m else {g: [None, "no output: " + (r.stderr or r.stdout)[-160:]] for g in names}


# ---- the mutations ---------------------------------------------------------------------------------------------
def pv1(c):
    L = read(c, "PROGRESS_LOG.md").splitlines(True); write(c, "PROGRESS_LOG.md", "".join(L[:199] + L[400:]))

def pv2(c):
    write(c, "PROGRESS_LOG.md", "# the log, replaced by one line\n")

def pv3(c):
    rel = "frontier/B1841_the_principled_ends_card/PREREGISTRATION.md"
    write(c, rel, read(c, rel) + "\nP9 (added after the seal): pass.\n")

def pv4(c):
    led = read(c, "docs/SEAL_LEDGER.md")
    for m in re.finditer(r"(frontier/[^\s|`]+(?:PREREGISTRATION|DECLARATION)[^\s|`]*\.md)[^\n]*?\b[0-9a-f]{64}\b", led):
        if os.path.isfile(os.path.join(c, m.group(1))):
            os.remove(os.path.join(c, m.group(1))); return "deleted " + m.group(1)
    raise RuntimeError("no digest-covered sealed file found")

def pv6(c):
    led = read(c, "docs/SEAL_LEDGER.md")
    m = re.search(r"\| *`?frontier/B1841_[^|]*\|[^\n]*?\b([0-9a-f]{8})\b", led)
    if not m: raise RuntimeError("no generated row for B1841 found")
    write(c, "docs/SEAL_LEDGER.md", led[:m.start(1)] + "deadbeef" + led[m.end(1):]); return "sha8 %s -> deadbeef" % m.group(1)

def pv8(c):
    d = "frontier/B9001_planted_seal_other_name/"
    src = json.loads(read(c, glob.glob(os.path.join(c, "frontier/B1857_*/arc_verdict.json"))[0][len(c) + 1:]))
    src.update(id="B9001", depends_on=[], claim_one_line="PLANTED: a seal named PREREG.md, first committed with its findings.")
    write(c, d + "PREREG.md", "# PREREG\nThe criterion, sealed before evaluation.\n")
    write(c, d + "FINDINGS.md", "# FINDINGS\nsealed (`PREREG.md`) BEFORE evaluation. Sweep: literature and repo, none.\n")
    write(c, d + "arc_verdict.json", json.dumps(src, indent=1))

def pv10(c):
    os.remove(os.path.join(c, "docs/IDENTIFICATION_BASELINE.json"))
    led = read(c, "docs/IDENTIFICATION_LEDGER.md").splitlines(True)
    idx = [i for i, l in enumerate(led) if re.match(r"\| *\**I-\d+", l) and "UNEARNED" in l]
    row = led[idx[-1]]
    new = [re.sub(r"I-\d+", "I-9%d" % k, row, count=1) for k in (1, 2, 3)]
    write(c, "docs/IDENTIFICATION_LEDGER.md", "".join(led[:idx[-1] + 1] + new + led[idx[-1] + 1:]))

def pv11(c):
    os.remove(os.path.join(c, "docs/RETRACTED_PHRASES.md"))

def pv12(c):
    for f in glob.glob(os.path.join(c, "tests/test_b*.py")): os.remove(f)

def pv13(c):
    write(c, "docs/LAW_MAP.md", "# LAW MAP\n"); write(c, "docs/THEOREM_LEDGER.md", "# THEOREM LEDGER\n")

def pv14(c):
    # Corrected 2026-11-11 (re-audit 3): the first version truncated B1857's verdict file. Once a later arc named B1857
    # as a dependency, the gate failed on the missing dependency and the case read CAUGHT for a reason that is not the
    # finding. The finding is that an unreadable verdict file is dropped without a word; so the case now truncates a
    # verdict file that no other arc depends on.
    files = sorted(glob.glob(os.path.join(c, "frontier/B*_*/arc_verdict.json")))
    deps = set()
    for f in files:
        try: deps |= set(json.load(open(f)).get("depends_on") or [])
        except Exception: pass
    f = next(f for f in files if re.match(r"(B\d+)_", os.path.basename(os.path.dirname(f))).group(1) not in deps)
    open(f, "w").write(open(f).read()[:200])
    return "truncated %s, which no arc depends on" % os.path.relpath(os.path.dirname(f), c)

def pv16(c):
    reg = json.loads(read(c, "tests/GATE_CONTROLS.json"))
    body = "import pytest\n" + "".join("\n@pytest.mark.skip\ndef test_c%d():\n    assert True is not False\n" % i for i in range(len(reg)))
    write(c, "tests/test_zz_planted_controls.py", body)
    write(c, "tests/GATE_CONTROLS.json", json.dumps({g: "tests/test_zz_planted_controls.py::test_c%d" % i for i, g in enumerate(sorted(reg))}, indent=1))

def pv17(c):
    write(c, "README.md", read(c, "README.md") + "\nThe convention ρ = lift⁻¹ is forced, and no choice is made.\nEvery coupling is degenerate at ω.\n")

def pv18(c):
    write(c, "docs/planted_note_pv18.txt", "a harmless file\n")

def pv19(c):
    b = json.loads(read(c, "docs/ATTRIBUTION_BASELINE.json")); b["frozen"]["README.md"] = b["frozen"].get("README.md", 0) + 4
    write(c, "docs/ATTRIBUTION_BASELINE.json", json.dumps(b, indent=1))
    write(c, "README.md", read(c, "README.md") + "\n" + " ".join([_V] * 4) + "\n")

def pv20(c):
    s = read(c, "CLAIMS.md"); i = s.index("| P16 |"); j = s.index("\n", i)
    write(c, "CLAIMS.md", s[:j + 1] + "| P999 | A planted proven claim that cites no lock. | (no lock) |\n" + s[j + 1:])

def pv21(c):
    # Changed 2026-11-11 with ctl4, for the same reason: a phrase the list still holds.
    write(c, "papers/planted_pv21.tex", "In this note we derived Einstein's equations.\n")
    write(c, "README.md", read(c, "README.md") + "\nWE DERIVED EINSTEIN'S EQUATIONS.\n")

def pv24(c):
    write(c, "tests/test_zz_planted_literal.py", "def test_orbit_counts_differ():\n    assert 1 != 2\n")


# ---- controls: violations the gates DO catch today; the instrument is valid only if it reports them CAUGHT ----------
def ask(c, expr):
    """what the clone's own gates' file answers for one expression"""
    code = "import sys, json; sys.path.insert(0, 'scripts/gates'); import gates\nprint('@@' + json.dumps(%s))\n" % expr
    r = sh([sys.executable, "-B", "-c", code], c)
    m = re.search(r"@@(.*)", r.stdout)
    if not m: raise RuntimeError("the gates' file did not answer: " + (r.stderr or r.stdout)[-200:])
    return json.loads(m.group(1))


_SEALED = "frontier/B1841_the_principled_ends_card/PREREGISTRATION.md"


def _dated_row(c, rel, text, what):
    led = read(c, "docs/SEAL_LEDGER.md")
    write(c, "docs/SEAL_LEDGER.md", led.rstrip("\n") + "\n\n| 2026-11-11 | B1841 %s | `%s` | `%s` |\n" % (what, rel, hashlib.sha256(text.encode("utf-8")).hexdigest()))


def pv5(c):
    new = read(c, _SEALED) + "\nP9 (added after the seal): pass.\n"
    write(c, _SEALED, new)
    h8 = hashlib.sha256(new.encode("utf-8")).hexdigest()[:8]
    led = read(c, "docs/SEAL_LEDGER.md")
    m = re.search(r"^\| " + re.escape(_SEALED) + r" \| ([0-9a-f]{8}) \|", led, re.M)
    if not m: raise RuntimeError("no generated row for the sealed file found")
    write(c, "docs/SEAL_LEDGER.md", led[:m.start(1)] + h8 + led[m.end(1):])     # the generated row is made to agree with the edit
    _dated_row(c, _SEALED, new, "a planted re-seal")                            # and a dated row carries the whole new digest
    return "the edit; its generated row moved from %s to %s; a dated row with the whole new digest" % (m.group(1), h8)


def pv5_twin(c):
    """the same act done as the rule allows: the amendment is a new file beside the seal, with its own two rows"""
    rel = _SEALED.replace("PREREGISTRATION.md", "PREREGISTRATION_AMENDMENT_1.md")
    new = "# An amendment beside the seal (planted)\n\nP9 (added after the seal, in a file of its own): pass.\n"
    write(c, rel, new)
    led = read(c, "docs/SEAL_LEDGER.md")
    m = re.search(r"^\| " + re.escape(_SEALED) + r" \|[^\n]*\n", led, re.M)
    if not m: raise RuntimeError("no generated row for the sealed file found")
    write(c, "docs/SEAL_LEDGER.md", led[:m.end()] + "| %s | %s | 000000000 | 1 | NO |\n" % (rel, hashlib.sha256(new.encode("utf-8")).hexdigest()[:8]) + led[m.end():])
    _dated_row(c, rel, new, "a planted amendment beside the seal")


def _a_negative(c, claim):
    src = json.loads(open(glob.glob(os.path.join(c, "frontier", "B1857_*", "arc_verdict.json"))[0], encoding="utf-8").read())
    src.update(id="B9003", verdict="NEGATIVE", depends_on=[], claim_one_line=claim)
    d = "frontier/B9003_a_planted_negative_on_one_thread/"
    write(c, d + "arc_verdict.json", json.dumps(src, indent=1) + "\n")
    write(c, d + "FINDINGS.md", "# FINDINGS\n\n" + claim + "\n")


def pv23(c):
    before = ask(c, "gates.member_scope_hits()")
    for arc, _phrase in before:
        found = glob.glob(os.path.join(c, "frontier", arc + "_*", "arc_verdict.json"))
        if len(found) == 1: break
    else: raise RuntimeError("no old line worded about the object on this commit")
    d = json.loads(open(found[0], encoding="utf-8").read())
    d["claim_one_line"] = re.sub(r"(?i)\bthe object\b", "the member m003", d["claim_one_line"])     # the old line now names a member
    open(found[0], "w", encoding="utf-8").write(json.dumps(d, indent=1, ensure_ascii=False) + "\n")
    _a_negative(c, "PLANTED: on the one thread LLR the object cannot carry a third generation.")
    after = ask(c, "gates.member_scope_hits()")
    return "%d such lines before, %d after: %s reworded to name a member, B9003 added" % (len(before), len(after), arc)


def pv23_twin(c):
    _a_negative(c, "PLANTED: on the one thread LLR the member m004 cannot carry a third generation.")


def _a_lock_that_reads(c, name, commit_it):
    d = "frontier/B9002_a_planted_lock/verification/"
    write(c, d + "test_b9002_a_planted_lock.py",
          'import pathlib\n\nHERE = pathlib.Path(__file__).resolve().parent\n\n\ndef test_the_run_reproduces():\n'
          '    assert "converged" in (HERE / "%s").read_text()\n' % name)
    if commit_it: write(c, d + name, "converged\n")


def pv25(c): _a_lock_that_reads(c, "run.log", False)          # .gitignore holds *.log: a clean checkout will not have the file

def pv25_twin(c): _a_lock_that_reads(c, "run.txt", True)


def _a_lock_through_a_second_name(c, name, commit_it):
    """the form of the lock the gate's own note names (B1671's): the root, then the arc, then its folder, then the file"""
    arc = "B9005_a_planted_lock_with_two_names"
    write(c, "tests/test_b9005_a_planted_lock_with_two_names.py",
          'import pathlib\n\nROOT = pathlib.Path(__file__).resolve().parents[1]\nA = ROOT / "frontier" / "%s"\nV = A / "verification"\n\n\n'
          'def test_the_run_reproduces():\n    assert "converged" in (V / "%s").read_text()\n' % (arc, name))
    write(c, "frontier/%s/verification/README.md" % arc, "# a planted arc\n")
    if commit_it: write(c, "frontier/%s/verification/%s" % (arc, name), "converged\n")


def pv32(c): _a_lock_through_a_second_name(c, "run.log", False)

def pv32_twin(c): _a_lock_through_a_second_name(c, "run.txt", True)


def _a_lock_that_runs(c, check):
    d = "frontier/B9004_a_planted_lock_that_runs_a_script/verification/"
    write(c, d + "third.py", "print('one third = %.17f' % (1 / 3))\n")
    write(c, d + "test_b9004_a_planted_lock_that_runs_a_script.py",
          'import pathlib, subprocess, sys\n\nHERE = pathlib.Path(__file__).resolve().parent\n\n\ndef test_the_run_reproduces():\n'
          '    out = subprocess.run([sys.executable, str(HERE / "third.py")], capture_output=True, text=True).stdout\n' + check)


def pv26(c): _a_lock_that_runs(c, '    assert "one third = 0.33333333333333331" in out\n')

def pv26_twin(c): _a_lock_that_runs(c, '    assert abs(float(out.split("=")[1]) - 1 / 3) < 1e-12\n')


def _edit_a_lock(c, above):
    rel = "tests/test_derived_potential.py"                 # a lock that no list of hashes names
    t = read(c, rel)
    m = re.search(r"^def (test_\w+)\(", t, re.M)
    if not m: raise RuntimeError("no test function found in " + rel)
    write(c, rel, t[:m.start()] + "import pytest as _planted_pytest\n\n\n" + above + t[m.start():])
    return m.group(1)


def pv31(c): return "a skip mark on " + _edit_a_lock(c, "@_planted_pytest.mark.skip(reason='planted')\n")

def pv31_twin(c): return "a comment above " + _edit_a_lock(c, "# a comment, and no mark\n")


# ---- WP-0.9, series 1 (card C4): the grade of a verdict file says more than its evidence -----------------------------------
_CHAIN_ARC = "B1612_the_mixing_patterns_the_weave_fixes"          # one of the fourteen arcs the candidate runs on (main's B1888)


def _grade(c, folder, **fields):
    """write the fields into the verdict file of `folder`; a folder that is not there is made, as a new PROVED arc"""
    p = os.path.join(c, "frontier", folder, "arc_verdict.json")
    if os.path.isfile(p):
        d = json.loads(open(p, encoding="utf-8").read())
    else:
        d = json.loads(open(glob.glob(os.path.join(c, "frontier", "B1857_*", "arc_verdict.json"))[0], encoding="utf-8").read())
        d.update(id=folder.split("_")[0], verdict="PROVED", depends_on=[], claim_one_line="PLANTED: a new arc with a grade.")
        write(c, "frontier/%s/FINDINGS.md" % folder, "# FINDINGS\n\nA planted arc.\n")
    d.update(fields)
    write(c, "frontier/%s/arc_verdict.json" % folder, json.dumps(d, indent=1, ensure_ascii=False) + "\n")


def _own_lock(c, folder):
    return sorted(glob.glob(os.path.join(c, "frontier", folder, "verification", "test_*.py")))[0][len(c) + 1:]


_NEW = "B9020_a_planted_arc_with_a_grade"
_NEW_DIR = "frontier/" + _NEW + "/verification/"
_SCRIPT = "print(sum(range(10)))\n"
_LOCK = "def test_the_sum():\n    assert sum(range(10)) == 45\n"


def pv33(c): _grade(c, _CHAIN_ARC, grade="theorem", grade_evidence=["frontier/%s/FINDINGS.md" % _CHAIN_ARC])

def pv33_twin(c): _grade(c, _CHAIN_ARC, grade="theorem", grade_evidence=[_own_lock(c, _CHAIN_ARC)])

def pv34(c): _grade(c, _NEW, grade="proved beyond doubt", grade_evidence=[])

def pv34_twin(c): _grade(c, _NEW, grade="process", grade_evidence=[])

def pv35(c): _grade(c, _NEW, grade="exact computation", grade_evidence=[_NEW_DIR + "sum.py", _NEW_DIR + "test_b9020_the_sum.py"])


def pv35_twin(c):
    pv35(c); write(c, _NEW_DIR + "sum.py", _SCRIPT); write(c, _NEW_DIR + "test_b9020_the_sum.py", _LOCK)


def pv36(c):
    _grade(c, _NEW, grade="numerical estimate", grade_evidence=[_NEW_DIR + "sum.py"]); write(c, _NEW_DIR + "sum.py", _SCRIPT)


def pv36_twin(c):
    _grade(c, _NEW, grade="numerical estimate", grade_evidence=[_NEW_DIR + "sum.py", _NEW_DIR + "sum_run.txt"])
    write(c, _NEW_DIR + "sum.py", _SCRIPT); write(c, _NEW_DIR + "sum_run.txt", "45\n")


def _sealed(c, held, of):
    _grade(c, _NEW, grade="sealed cells held", grade_evidence=["frontier/%s/PREREGISTRATION.md" % _NEW], grade_cells=[held, of])
    write(c, "frontier/%s/PREREGISTRATION.md" % _NEW, "# A planted seal\n\nThirteen cells.\n")


def pv37(c): _sealed(c, 14, 13)

def pv37_twin(c): _sealed(c, 7, 13)


def pv30(c):
    head = sh(["git", "rev-parse", "--short=9", "HEAD"], c).stdout.strip()
    write(c, "docs/progress/REVIEWS.md", read(c, "docs/progress/REVIEWS.md")
          + "\n\nA note, not a review: the gates were run at **anchor-commit: `%s`** today.\n" % head)


def ctl1(c):
    write(c, "PROGRESS_LOG.md", "# an uncommitted replacement of the log\n")

def ctl2(c):
    led = read(c, "docs/SEAL_LEDGER.md")
    for m in re.finditer(r"(frontier/[^\s|`]+(?:PREREGISTRATION|DECLARATION)[^\s|`]*\.md)[^\n]*?\b[0-9a-f]{64}\b", led):
        if os.path.isfile(os.path.join(c, m.group(1))):
            write(c, m.group(1), read(c, m.group(1)) + "\nan added line\n"); return "edited " + m.group(1)
    raise RuntimeError("no digest-covered sealed file found")

def ctl3(c):
    write(c, "docs/planted_ctl3.md", "written with %s\n" % _V)

def ctl4(c):
    # Changed 2026-11-11 (re-audit 4): the control used the phrase "toward the full SM". Main took that phrase off the
    # banned list at the owner's ruling on the goal (B1878): it states an aim. The control now uses a phrase the list
    # still holds.
    write(c, "README.md", read(c, "README.md") + "\nThis note says that we derived Einstein's equations.\n")

def ctl5(c):
    write(c, "tests/test_zz_planted_tautology.py", "def test_nothing():\n    assert True\n")

CONTROLS = [
    ("CTL1", "G1", "an UNCOMMITTED replacement of PROGRESS_LOG.md", ctl1, False, None, ["append-only"]),
    ("CTL2", "G2", "an edit to a digest-covered sealed file, commit", ctl2, True, None, ["seal-digests"]),
    ("CTL3", "G9", "a vendor name in a new .md file, commit", ctl3, True, None, ["attribution"]),
    ("CTL4", "G10", "a banned phrase verbatim in README.md, commit", ctl4, True, None, ["framing"]),
    ("CTL5", "L7", "a test whose only assert is `assert True`, commit", ctl5, True, None, ["test-vacuity"]),
]

CASES = [
    # id, finding, what is planted, mutation, commit?, commit message, gates that should fail
    ("PV1", "G1", "delete lines 200-400 of PROGRESS_LOG.md, commit", pv1, True, None, ["append-only"]),
    ("PV2", "G1", "replace PROGRESS_LOG.md with one line, commit", pv2, True, None, ["append-only"]),
    ("PV3", "G2", "append a criterion to B1841's PREREGISTRATION.md, commit", pv3, True, None,
     ["seal-digests", "seal-provenance", "seal-ledger-current", "seal-order-unshown"]),
    ("PV4", "G2", "delete a digest-covered sealed file, commit", pv4, True, None,
     ["seal-digests", "seal-provenance", "seal-ledger-current"]),
    ("PV6", "G2", "hand-edit a generated sha8 in docs/SEAL_LEDGER.md, commit", pv6, True, None,
     ["seal-ledger-current", "seal-digests"]),
    ("PV8", "G4", "an arc whose seal is PREREG.md, first committed with FINDINGS.md", pv8, True, None, ["seal-order-unshown"]),
    ("PV10", "G5", "delete IDENTIFICATION_BASELINE.json and add three UNEARNED rows", pv10, True, None, ["identification-register"]),
    ("PV11", "G5", "delete docs/RETRACTED_PHRASES.md", pv11, True, None, ["retraction-sweep"]),
    ("PV12", "G5", "delete every tests/test_b*.py", pv12, True, None, ["test-vacuity"]),
    ("PV13", "G5", "empty LAW_MAP.md and THEOREM_LEDGER.md", pv13, True, None, ["law-map-provenance", "chain-locks"]),
    ("PV14", "G14", "truncate one arc_verdict.json to invalid JSON", pv14, True, None, ["arc-data"]),
    ("PV16", "G7", "point every gate control at a skipped trivial test", pv16, True, None, ["gate-controls"]),
    ("PV17", "G8", "two retracted phrases (rows added after 2026-10-07) pasted into README.md", pv17, True, None, ["retraction-sweep"]),
    ("PV18", "G9", "a commit message with a vendor co-author trailer", pv18, True,
     "a planted commit\n\nCo-Authored-By: %s <noreply@example.invalid>" % _V, ["attribution"]),
    ("PV19", "G9", "raise a baseline count and add that many tokens, same commit", pv19, True, None, ["attribution"]),
    ("PV20", "G10", "a PROVEN row in CLAIMS.md that cites no lock", pv20, True, None, ["claims"]),
    ("PV21", "G10", "a banned phrase in a .tex file and a capitalised variant in README.md", pv21, True, None, ["framing"]),
    ("PV24", "L7", "a test whose only assert is `assert 1 != 2`", pv24, True, None, ["test-vacuity"]),
    # added 2026-11-11 (series 4): the cases this suite listed as manual, planted by the suite itself; and M5's
    ("PV5", "G2", "edit a sealed file and write its new digest into both of the ledger's rows, commit", pv5, True, None, ["seal-immutable", "seal-digests", "seal-ledger-current"]),
    ("PV23", "W1", "a new NEGATIVE worded about the object, and an old one reworded so the count stays, commit", pv23, True, None, ["member-scope"]),
    ("PV25", "L4", "an arc's own lock that reads a file git ignores, commit", pv25, True, None, ["tracked-deps"]),
    ("PV32", "L4", "a lock in tests/ that names an ignored file through a second name, commit", pv32, True, None, ["tracked-deps"]),
    ("PV26", "L6", "a lock that runs a script and pins a float it prints, as text, commit", pv26, True, None, ["test-vacuity"]),
    ("PV31", "new", "a test of a lock that no hash list names is made to skip, commit (M5)", pv31, True, None, ["test-vacuity"]),
    # added 2026-11-11 (WP-0.9, series 1): a grade that says more than its evidence
    ("PV33", "M1", "an arc the candidate runs on is graded a theorem and names no lock, commit", pv33, True, None, ["arc-data"]),
    ("PV34", "M1", "a new arc with a grade that is not one of the five words, commit", pv34, True, None, ["arc-data"]),
    ("PV35", "M1", "a new arc graded an exact computation, naming a script and a lock that are not there, commit", pv35, True, None, ["arc-data"]),
    ("PV36", "M1", "a new arc graded a numerical estimate, naming a script and no output, commit", pv36, True, None, ["arc-data"]),
    ("PV37", "M1", "a new arc graded sealed cells held, with more cells held than were sealed, commit", pv37, True, None, ["arc-data"]),
    # added 2026-11-11 (series 4): found on main's f9e70c167 while reading main's page on the periodic review
    ("PV30", "new", "a sentence on the reviews' page that names the head as an anchor, commit", pv30, True, None, ["review-fires"]),
]
MANUAL = []          # until 2026-11-11 six cases stood here; the suite now plants them itself (PV5, PV7, PV23, PV25, PV26, PV27)

# Added 2026-11-11 (series 4).  A twin is the same plant with the violation taken out: every gate its case names must PASS on
# it.  A twin that fails means the gate fires on the plant's shape and not on the violation, and its case cannot be read.
TWINS = [
    ("PV5", "the amendment as a new file beside the seal, with its two rows", pv5_twin, ["seal-immutable", "seal-digests", "seal-ledger-current"]),
    ("PV23", "the same new NEGATIVE worded about the member", pv23_twin, ["member-scope"]),
    ("PV25", "the same lock reading a file that is committed", pv25_twin, ["tracked-deps"]),
    ("PV32", "the same lock reading a file that is committed", pv32_twin, ["tracked-deps"]),
    ("PV26", "the same lock comparing the number as a number", pv26_twin, ["test-vacuity"]),
    ("PV31", "the same lock edited with no mark", pv31_twin, ["test-vacuity"]),
    ("PV33", "the same arc graded a theorem and naming its own lock", pv33_twin, ["arc-data"]),
    ("PV34", "the same new arc graded a process", pv34_twin, ["arc-data"]),
    ("PV35", "the same, with the script and a lock that can fail in the commit", pv35_twin, ["arc-data"]),
    ("PV36", "the same, naming the script and its committed output", pv36_twin, ["arc-data"]),
    ("PV37", "the same, with seven of thirteen cells held", pv37_twin, ["arc-data"]),
]


def special_export(c, work):
    """PV9: the gates on a `git archive` export (no .git). The ten git-dependent gates must not report PASS."""
    d = os.path.join(work, "export"); shutil.rmtree(d, ignore_errors=True); os.makedirs(d)
    tar = subprocess.run(["git", "archive", "HEAD"], cwd=c, capture_output=True, check=True).stdout
    subprocess.run(["tar", "-x", "-C", d], input=tar, check=True)
    need = ["append-only", "attribution", "tracked-forbidden", "log-changelog-paired", "views-fresh", "path-refs",
            "test-vacuity", "retraction-sweep", "review-fires", "harvest-debt"]
    res = run_gates(d, need)
    passing = sorted(g for g, r in res.items() if r[0])
    return (not passing), "gates that still PASS with no git: %s" % (", ".join(passing) or "none")


def special_dates(c, work):
    """PV15: three date-reading gates at HEAD's commit date and 60 days later must agree."""
    day = sh(["git", "log", "-1", "--format=%cs"], c).stdout.strip()
    later = (datetime.date.fromisoformat(day) + datetime.timedelta(days=60)).isoformat()
    names = ["lead-debt", "point-debt", "relay-debt"]
    env = lambda d: {"OA_LEAD_TODAY": d, "OA_POINT_TODAY": d, "OA_RELAY_TODAY": d, "OA_HARVEST_TODAY": d}
    a, b = run_gates(c, names, env(day)), run_gates(c, names, env(later))
    diff = [g for g in names if a[g][0] != b[g][0]]
    return (not diff), "on %s vs %s the result changes for: %s" % (day, later, ", ".join(diff) or "none")


def special_shallow(c, work):
    """PV22: on a depth-50 clone, a history-reading gate must say that the clone is shallow."""
    d = os.path.join(work, "shallow"); shutil.rmtree(d, ignore_errors=True)
    sh(["git", "clone", "-q", "--depth", "50", "file://" + c, d], work, check=True)
    day = sh(["git", "log", "-1", "--format=%cs"], c).stdout.strip()
    # Corrected 2026-11-10 at main's catch (B1865): the first version compared the shallow clone's verdict with the
    # full clone's on one date, so it reported CAUGHT whenever the two happened to agree. The criterion is now the
    # one ACCEPTANCE_CRITERIA.md states: the gate fails on a shallow clone AND says why.
    r = run_gates(d, ["lead-debt"])["lead-debt"]
    ok = (r[0] is False) and ("shallow" in r[1].lower())
    return ok, "lead-debt on the shallow clone: %s (%s)" % ("PASS" if r[0] else "FAIL", r[1][:90])


_GEN_ROW = re.compile(r"^\| frontier/B[^ |]+ \| [0-9a-f]{8} \|.*$", re.M)


def _ledger_rebuilt_twice(c):
    """remove the ledger's generated rows, run the generator twice: (rows after the first run, after the second, what it printed)"""
    rel = "docs/SEAL_LEDGER.md"
    write(c, rel, _GEN_ROW.sub("", read(c, rel)))
    runs, said = [], []
    for _ in range(2):
        r = sh([sys.executable, "-B", os.path.join("scripts", "seal_ledger.py")], c)
        runs.append(_GEN_ROW.findall(read(c, rel))); said.append((r.stdout.strip().splitlines() or ["(nothing printed)"])[-1])
    return runs[0], runs[1], said


def special_ledger_twice(c, work):
    """PV7: the seal ledger's generated rows, removed and rebuilt twice, must come out the same both times."""
    committed = _GEN_ROW.findall(read(c, "docs/SEAL_LEDGER.md"))
    if not committed: return None, "no generated row found in the ledger"
    first, second, said = _ledger_rebuilt_twice(c)
    differ = sum(1 for a, b in zip(first, second) if a != b) + abs(len(first) - len(second))
    # the twin: the same two runs with the generator made to read the ledger as evidence for itself, as it did when the case
    # was found.  The two runs must then DIFFER, or this case cannot tell a mended generator from an unmended one.
    sh(["git", "checkout", "-q", "--", "docs/SEAL_LEDGER.md"], c)
    gen = read(c, "scripts/seal_ledger.py")
    old = '        if rel_t == "docs/SEAL_LEDGER.md":\n            continue\n'
    if old in gen:
        write(c, "scripts/seal_ledger.py", gen.replace(old, ""))
        t1, t2, _ = _ledger_rebuilt_twice(c)
        twin = sum(1 for a, b in zip(t1, t2) if a != b) + abs(len(t1) - len(t2))
        tells = "with the generator reading its own ledger again, %d rows differ between the two runs" % twin
    else:
        twin, tells = (1 if differ else 0), "the generator has no line that leaves its own ledger out: it is as it was when the case was found"
    if differ == 0 and twin == 0: return None, "the two runs agree, and they agree with the old fault planted too: the case cannot tell (%s)" % tells
    return (differ == 0 and len(first) == len(committed)), ("%d generated rows removed; rebuilt: %d, then %d; rows that differ between the two runs: %d; "
            "the generator printed '%s', then '%s'; %s" % (len(committed), len(first), len(second), differ, said[0], said[1], tells))


def _a_test_that_writes(c, name, where):
    write(c, "tests/" + name,
          "import pathlib\n\nROOT = pathlib.Path(__file__).resolve().parents[1]\n\n\ndef test_it_reproduces(tmp_path):\n"
          "    p = %s\n    p.write_text('a line written by a test run\\n')\n    assert p.read_text()\n" % where)
    sh(["git", "add", "-A"], c); sh(["git"] + WHO + ["commit", "-q", "-m", "a planted test (PV27)"], c)
    r = sh([sys.executable, "-B", "-m", "pytest", "-q", "-p", "no:cacheprovider", "tests/" + name], c, env=dict(os.environ, PYTHONDONTWRITEBYTECODE="1"))
    changed = sh(["git", "status", "--porcelain", "--untracked-files=no"], c).stdout.split()
    sh(["git", "checkout", "-q", "--", "."], c)
    return r.returncode, (r.stdout + r.stderr), changed


def special_writes_tracked(c, work):
    """PV27: a test run that writes to a tracked file must end red, and name the file."""
    rc, out, changed = _a_test_that_writes(c, "test_zz_planted_writes_a_tracked_file.py", "ROOT / 'CHANGELOG.md'")
    if "CHANGELOG.md" not in changed: return None, "the planted test did not change the tracked file: " + out[-160:]
    rc2, out2, changed2 = _a_test_that_writes(c, "test_zz_planted_writes_nothing_tracked.py", "tmp_path / 'CHANGELOG.md'")
    if rc2 != 0 or changed2: return None, "the twin, which writes under a temporary folder, ended with status %d: the case cannot be read" % rc2
    caught = rc != 0 and "CHANGELOG.md" in out
    return caught, ("the run of a test that rewrites CHANGELOG.md ended with status %d and %s the file; the twin that writes under a temporary folder ended with status 0"
                    % (rc, "names" if "CHANGELOG.md" in out else "does not name"))


def special_seams(c, work):
    """PV28: three gates with the project's own variables set must print what they print without them."""
    empty = os.path.join(work, "a_page_with_no_row.md")
    open(empty, "w", encoding="utf-8").write("# a page with no row\n")
    names = ["review-fires", "point-debt", "retraction-debt"]
    env = {"OA_REVIEW_MERGES": "0", "OA_POINT_REGISTER": empty, "OA_RETRACTIONS_LEDGER": empty}
    a, b = run_gates(c, names), run_gates(c, names, env)
    diff = [g for g in names if a[g] != b[g]]
    return (not diff), "with OA_REVIEW_MERGES, OA_POINT_REGISTER and OA_RETRACTIONS_LEDGER set, the line changes for: %s" % (", ".join(diff) or "none")


def special_redirect(c, work):
    """PV29: on an export, with GIT_DIR pointing at a real clone, no git-dependent gate may report PASS."""
    d = os.path.join(work, "export_redirected"); shutil.rmtree(d, ignore_errors=True); os.makedirs(d)
    tar = subprocess.run(["git", "archive", "HEAD"], cwd=c, capture_output=True, check=True).stdout
    subprocess.run(["tar", "-x", "-C", d], input=tar, check=True)
    need = ["append-only", "attribution", "tracked-forbidden", "log-changelog-paired", "views-fresh", "path-refs",
            "test-vacuity", "retraction-sweep", "review-fires", "harvest-debt"]
    res = run_gates(d, need, {"GIT_DIR": os.path.join(c, ".git")})
    passing = sorted(g for g, r in res.items() if r[0])
    shutil.rmtree(d, ignore_errors=True)
    return (not passing), "gates that PASS on an export when GIT_DIR points at a clone: %s" % (", ".join(passing) or "none")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--ref", default="origin/main"); ap.add_argument("--work", required=True); ap.add_argument("--only", default="")
    a = ap.parse_args()
    work = os.path.abspath(a.work)
    if os.path.commonpath([work, REPO]) == REPO: sys.exit("--work must be outside the repository")
    os.makedirs(work, exist_ok=True)
    c = os.path.join(work, "clone")
    if not os.path.isdir(c): sh(["git", "clone", "-q", REPO, c], work, check=True)
    base = sh(["git", "rev-parse", a.ref], REPO, check=True).stdout.strip()
    sh(["git", "fetch", "-q", REPO, base], c); sh(["git", "checkout", "-q", "--detach", base], c, check=True)
    only = set(x for x in a.only.split(",") if x)
    reset = lambda: (sh(["git", "reset", "-q", "--hard", base], c), sh(["git", "clean", "-fdq"], c))
    rows, missed, invalid = [], 0, 0
    print("planted-violation suite at %s (%s)\n" % (a.ref, base[:9]))
    # Added 2026-11-11: a case can be read only if the gates it names pass before anything is planted.  A gate that is red on
    # the clean clone would read every case that names it as CAUGHT.
    named = sorted({g for row in CONTROLS + CASES for g in row[6]})
    clean = run_gates(c, named)
    red_before = sorted(g for g in named if clean[g][0] is not True)
    print("the %d gates the cases name, on the clean clone: %s\n" % (len(named), "all pass" if not red_before else "RED BEFORE ANY PLANT: " + ", ".join(red_before)))
    for pid, finding, what, mut, commit, msg, gates in CONTROLS + CASES:
        if only and pid not in only: continue
        if pid == "PV1": print()
        reset()
        try:
            note = mut(c) or ""
            if commit:
                sh(["git", "add", "-A"], c); sh(["git"] + WHO + ["commit", "-q", "-m", msg or "a planted violation (%s)" % pid], c)
            res = run_gates(c, gates)
            caught = [g for g, r in res.items() if r[0] is False and g not in red_before]
            ok = bool(caught) if not all(g in red_before for g in gates) else None
            detail = "; ".join("%s=%s" % (g, "FAIL" if r[0] is False else "PASS" if r[0] else "?") for g, r in res.items())
        except Exception as exc:
            ok, detail, note = None, "COULD NOT PLANT: %r" % (exc,), ""
        tag = "CAUGHT" if ok else "COULD-NOT-RUN" if ok is None else "NOT CAUGHT"
        if pid.startswith("CTL"): invalid += ok is not True
        else: missed += ok is False
        rows.append((pid, finding, tag, what, detail + ((" [" + note + "]") if note else "")))
        print("%-5s %-4s %-13s %s\n      %s" % rows[-1])
    print()
    twin_fails = 0
    for pid, what, mut, gates in TWINS:
        if only and pid not in only: continue
        reset()
        try:
            note = mut(c) or ""
            sh(["git", "add", "-A"], c); sh(["git"] + WHO + ["commit", "-q", "-m", "a twin with no violation (%s)" % pid], c)
            res = run_gates(c, gates)
            fails = [g for g, r in res.items() if r[0] is not True and g not in red_before]
            detail = "; ".join("%s=%s" % (g, "FAIL: " + r[1][:110] if r[0] is False else "PASS" if r[0] else "?") for g, r in res.items())
        except Exception as exc:
            fails, detail, note = ["could not plant"], "COULD NOT PLANT: %r" % (exc,), ""
        twin_fails += bool(fails)
        print("%-5s twin %-12s %s\n      %s" % (pid, "FAILS" if fails else "PASSES", what, detail + ((" [" + note + "]") if note else "")))
    print()
    for pid, fn in (("PV9", special_export), ("PV15", special_dates), ("PV22", special_shallow), ("PV28", special_seams), ("PV29", special_redirect),
                    ("PV7", special_ledger_twice), ("PV27", special_writes_tracked)):
        if only and pid not in only: continue
        reset()
        try: ok, detail = fn(c, work)
        except Exception as exc: ok, detail = None, "COULD NOT RUN: %r" % (exc,)
        tag = "CAUGHT" if ok else "COULD-NOT-RUN" if ok is None else "NOT CAUGHT"
        missed += ok is False
        print("%-5s %-4s %-13s %s\n      %s" % (pid, {"PV9": "G5", "PV15": "G6", "PV22": "G13", "PV28": "G6", "PV29": "G5", "PV7": "G3", "PV27": "L10"}[pid], tag, fn.__doc__.split(":")[1].strip()[:90], detail))
    if not only:
        print()
        for pid, finding, what in MANUAL: print("%-5s %-4s %-13s %s" % (pid, finding, "MANUAL", what))
    reset()
    print("\ncontrols not reported CAUGHT: %d%s" % (invalid, "  -- THE INSTRUMENT IS NOT VALID ON THIS COMMIT" if invalid else ""))
    print("twins that do not pass: %d%s" % (twin_fails, "  -- THE CASE OF EACH SUCH TWIN IS NOT TO BE READ" if twin_fails else ""))
    print("NOT CAUGHT: %d" % missed)
    sys.exit(missed + 100 * invalid)


if __name__ == "__main__":
    main()
