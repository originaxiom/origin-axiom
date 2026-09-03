#!/usr/bin/env python3
"""B1243 -- recompute every number this arc asserts, on the live tree.
Prints REPRODUCES on success.  No measured value is used (Gate 5)."""
import glob, json, os, re, subprocess, sys
R = os.environ.get("OA_ROOT") or os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
ok = True
def chk(label, got, want):
    global ok
    good = got == want
    ok &= good
    print(f"  {'OK ' if good else 'DIFF'}  {label}: {got}" + ("" if good else f"  (expected {want})"))

led = open(os.path.join(R, "docs/THEOREM_LEDGER.md"), encoding="utf-8").read()
links = re.findall(r"^\*\*C(\d+)\s*\[([A-Z][A-Z-]*)", led, re.M)
chk("chain links", len(links), 45)
chk("NO-GO links", sum(1 for _, l in links if l == "NO-GO"), 7)
chk("AXIOM links", sum(1 for _, l in links if l == "AXIOM"), 4)
chk("forced (non-axiom)", sum(1 for _, l in links if l != "AXIOM"), 41)

# the two catches
chk("C25 carries the 14-vs-12 scope", "14-dimensional" in led[led.index("**C25 ["):led.index("**C26 [")], True)
chk("chain cites the genesis theorem", "UNIQUENESS_THEOREM" in led, True)

# the genesis theorem is real and green
r = subprocess.run([sys.executable, "-m", "pytest", "tests/test_uniqueness_theorem.py", "-q"],
                   capture_output=True, text=True, cwd=R)
chk("uniqueness-theorem lock", r.returncode, 0)

# the bannered-arc census the gate keys on
KEY = re.compile(r"(PARTIALLY RETRACTED|CORRECTED BY|SENTENCE CORRECTED|SCOPE.CORRECTED"
                 r"|SUPERSEDED BY|RETRACTED BY|RE-SCOPED|WITHDRAWN BY)", re.I)
ban = []
for p in glob.glob(os.path.join(R, "frontier/*/FINDINGS.md")):
    for ln in open(p, encoding="utf-8", errors="ignore").readlines()[:30]:
        s = ln.strip()
        if s.startswith(">") and KEY.search(s):
            ban.append(os.path.basename(os.path.dirname(p)).split("_")[0]); break
chk("arcs carrying a real correction banner", len(ban), 4)
chk("B892 among them", "B892" in ban, True)

# the register
b = json.load(open(os.path.join(R, "docs/IDENTIFICATION_BASELINE.json"), encoding="utf-8"))
chk("baseline unearned", b["unearned"], 10)
chk("baseline total_rows", b["total_rows"], 18)
chk("I-18 registered", "I-18" in b["rows"], True)

# the instrument's own controls
r = subprocess.run([sys.executable, "scripts/checks/citation_status.py", "--selftest"],
                   capture_output=True, text=True, cwd=R, env={**os.environ, "OA_ROOT": R})
chk("gate selftest", r.returncode, 0)
chk("gate controls non-vacuous", "10/10" in r.stdout, True)
r = subprocess.run([sys.executable, "scripts/checks/citation_status.py", "--chain"],
                   capture_output=True, text=True, cwd=R, env={**os.environ, "OA_ROOT": R})
chk("gate green on the live chain", r.returncode, 0)

print("REPRODUCES" if ok else "DIFF")
sys.exit(0 if ok else 1)
