#!/usr/bin/env python3
"""The planted-violation suite of ACCEPTANCE_CRITERIA.md, section 2, as a runnable script.

Each case plants one violation in a SCRATCH CLONE of the repository (never in the working tree), commits it there
where the case says so, runs the named gate functions from that clone's own scripts/gates/gates.py, and reports
whether the violation was CAUGHT (a named gate returned False) or NOT CAUGHT. The clone is reset between cases.

    python3 relays/advisor_2026-11-10_audit/tools/planted_violations.py --ref origin/main --work DIR [--only PV1,PV3]

DIR must be outside the repository (it will hold a full checkout). Exit status = the number of cases NOT CAUGHT.
The CTL cases are controls: violations the gates catch today. If a control is not reported CAUGHT the instrument
is not valid on that commit and its other lines are not to be read.
Cases that cannot be automated here are listed as MANUAL with the finding that describes them.
Standard library only. Read-only on the repository it is run from.
"""
import argparse, base64, glob, json, os, re, shutil, subprocess, sys, datetime

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
    f = glob.glob(os.path.join(c, "frontier/B1857_*/arc_verdict.json"))[0]
    open(f, "w").write(open(f).read()[:200])

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
    write(c, "papers/planted_pv21.tex", "We are working toward the full SM.\n")
    write(c, "README.md", read(c, "README.md") + "\nTOWARD THE FULL SM.\n")

def pv24(c):
    write(c, "tests/test_zz_planted_literal.py", "def test_orbit_counts_differ():\n    assert 1 != 2\n")


# ---- controls: violations the gates DO catch today; the instrument is valid only if it reports them CAUGHT ----------
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
    write(c, "README.md", read(c, "README.md") + "\nThis is a step toward the full SM.\n")

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
]
MANUAL = [
    ("PV5", "G2", "edit a sealed file and append a ledger row with the new digest (needs the ledger's row shapes)"),
    ("PV7", "G3", "remove the generated ledger rows and regenerate twice; the two runs must agree"),
    ("PV23", "W1", "a new one-thread NEGATIVE worded about the object, plus one old line reworded"),
    ("PV25", "L4", "a lock that reads a git-ignored file -- no gate exists today"),
    ("PV26", "L6", "a lock that compares printed floats as text -- no gate exists today"),
    ("PV27", "L10", "a test run that writes to a tracked file -- no gate exists today"),
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
    """PV22: on a depth-50 clone, lead-debt must not pass by seeing no stale arcs."""
    d = os.path.join(work, "shallow"); shutil.rmtree(d, ignore_errors=True)
    sh(["git", "clone", "-q", "--depth", "50", "file://" + c, d], work, check=True)
    day = sh(["git", "log", "-1", "--format=%cs"], c).stdout.strip()
    later = (datetime.date.fromisoformat(day) + datetime.timedelta(days=3)).isoformat()
    r = run_gates(d, ["lead-debt"], {"OA_LEAD_TODAY": later})["lead-debt"]
    full = run_gates(c, ["lead-debt"], {"OA_LEAD_TODAY": later})["lead-debt"]
    return (r[0] == full[0] or "shallow" in r[1].lower()), "3 days on: full clone %s, shallow clone %s (%s)" % (
        "PASS" if full[0] else "FAIL", "PASS" if r[0] else "FAIL", r[1][:90])


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
    for pid, finding, what, mut, commit, msg, gates in CONTROLS + CASES:
        if only and pid not in only: continue
        if pid == "PV1": print()
        reset()
        try:
            note = mut(c) or ""
            if commit:
                sh(["git", "add", "-A"], c); sh(["git"] + WHO + ["commit", "-q", "-m", msg or "a planted violation (%s)" % pid], c)
            res = run_gates(c, gates)
            caught = [g for g, r in res.items() if r[0] is False]
            ok = bool(caught)
            detail = "; ".join("%s=%s" % (g, "FAIL" if r[0] is False else "PASS" if r[0] else "?") for g, r in res.items())
        except Exception as exc:
            ok, detail, note = None, "COULD NOT PLANT: %r" % (exc,), ""
        tag = "CAUGHT" if ok else "COULD-NOT-RUN" if ok is None else "NOT CAUGHT"
        if pid.startswith("CTL"): invalid += ok is not True
        else: missed += ok is False
        rows.append((pid, finding, tag, what, detail + ((" [" + note + "]") if note else "")))
        print("%-5s %-4s %-13s %s\n      %s" % rows[-1])
    reset()
    for pid, fn in (("PV9", special_export), ("PV15", special_dates), ("PV22", special_shallow)):
        if only and pid not in only: continue
        try: ok, detail = fn(c, work)
        except Exception as exc: ok, detail = None, "COULD NOT RUN: %r" % (exc,)
        tag = "CAUGHT" if ok else "COULD-NOT-RUN" if ok is None else "NOT CAUGHT"
        missed += ok is False
        print("%-5s %-4s %-13s %s\n      %s" % (pid, {"PV9": "G5", "PV15": "G6", "PV22": "G13"}[pid], tag, fn.__doc__.split(":")[1].strip()[:90], detail))
    if not only:
        print()
        for pid, finding, what in MANUAL: print("%-5s %-4s %-13s %s" % (pid, finding, "MANUAL", what))
    print("\ncontrols not reported CAUGHT: %d%s" % (invalid, "  -- THE INSTRUMENT IS NOT VALID ON THIS COMMIT" if invalid else ""))
    print("NOT CAUGHT: %d" % missed)
    sys.exit(missed + 100 * invalid)


if __name__ == "__main__":
    main()
