#!/usr/bin/env python3
"""B1244 -- recompute the arc's numbers on the live tree. Prints REPRODUCES. No measured value."""
import glob, json, os, re, subprocess, sys
R = os.environ.get("OA_ROOT") or os.path.abspath(os.path.join(os.path.dirname(__file__),"..","..",".."))
ok = True
def chk(l,g,w):
    global ok
    good = g==w; ok &= good
    print(f"  {'OK ' if good else 'DIFF'}  {l}: {g}"+("" if good else f"  (expected {w})"))
led = open(os.path.join(R,"docs/THEOREM_LEDGER.md"),encoding="utf-8").read()
links = re.findall(r"^\*\*C(\d+)\s*\[([A-Z][A-Z-]*)", led, re.M)
chk("chain links", len(links), 46)
chk("axioms still 4", sum(1 for _,l in links if l=="AXIOM"), 4)
chk("C46 admitted as THEOREM", ("46","THEOREM") in links, True)
chk("C22 carries its scope line", "a terminology collision, resolved" in led, True)
for a in ("B286","B287","B288","B294","B295"):
    chk(f"C46 cites {a}", a in led[led.index("**C46 ["):], True)
# the seam family's locks are green
r = subprocess.run([sys.executable,"-m","pytest","tests/test_b286_the_seam.py",
    "tests/test_b287_distinguished_closing.py","tests/test_b288_arithmetic_filling_census.py",
    "tests/test_b294_selection_verdict.py","tests/test_b295_ssb_gauge_status.py","-q"],
    capture_output=True,text=True,cwd=R)
chk("seam-family locks", r.returncode, 0)
# coverage pins present and satisfied
cov = json.load(open(os.path.join(R,"docs/CHAIN_COVERAGE.json"),encoding="utf-8"))["must_appear_in_chain"]
chk("coverage pins", len(cov), 9)
chk("all pins carried by the chain", [c["token"] for c in cov if c["token"] not in led], [])
r = subprocess.run([sys.executable,"scripts/checks/citation_status.py","--chain"],
                   capture_output=True,text=True,cwd=R,env={**os.environ,"OA_ROOT":R})
chk("citation gate green", r.returncode, 0)
r = subprocess.run([sys.executable,"scripts/checks/forcedness_census.py"],capture_output=True,text=True,cwd=R)
chk("census green", r.returncode, 0)
print("REPRODUCES" if ok else "DIFF"); sys.exit(0 if ok else 1)
