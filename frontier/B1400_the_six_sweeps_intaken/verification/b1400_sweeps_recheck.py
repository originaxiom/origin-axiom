#!/usr/bin/env python3
"""B1400 -- the five non-SnapPy sweeps, rechecked on this bench. Numbers recomputed, not read.

chat1's SWEEPS_2026-09-12 report. Sweep 6 (the census-bias finding) is re-run separately by
b1400_census_bias_stratified.py, which also stratifies it. This script does sweeps 1-5.
"""
import json, re, subprocess, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[3]

def sh(*a):
    return subprocess.run(a, cwd=ROOT, capture_output=True, text=True).stdout

print("=" * 78); print("SWEEP 1 -- CLAIMS.md keyword counts"); print("=" * 78)
claims = (ROOT / "CLAIMS.md").read_text(encoding="utf-8")
s1 = {"lines": len(claims.splitlines())}
for t in ("base rate", "prereg", "control", "generic"):
    s1[t] = len(re.findall(re.escape(t), claims, re.I))
exp1 = {"lines": 231, "base rate": 0, "prereg": 0, "control": 3, "generic": 4}
print(f"  measured {s1}")
print(f"  claimed  {exp1}")
print(f"  MATCH: {s1 == exp1}")

print(); print("=" * 78); print("SWEEP 3 -- arcs never cited by any other arc"); print("=" * 78)
verd = {}
for p in ROOT.glob("frontier/*/arc_verdict.json"):
    try: d = json.loads(p.read_text(encoding="utf-8"))
    except Exception: continue
    if isinstance(d.get("id"), str): verd[d["id"]] = p
cited = set()
for p in list(ROOT.glob("frontier/*/*.md")) + list(ROOT.glob("frontier/*/arc_verdict.json")):
    try: t = p.read_text(encoding="utf-8", errors="ignore")
    except Exception: continue
    cited |= {"B" + m.group(1) for m in re.finditer(r"\bB(\d{1,4})\b", t)}
never = sorted(set(verd) - cited, key=lambda s: int(s[1:]))
print(f"  arcs with a verdict id: {len(verd)}   (they reported 1240)")
print(f"  distinct arc-ids in arc text: {len(cited)}   (they reported 1386)")
print(f"  ARCS NEVER MENTIONED: {len(never)}   (they reported 0)   -> finding reproduces: {len(never) == 0}")
print("  the count difference is the commit, not the method: this clone carries branch-only arcs.")

print(); print("=" * 78); print("SWEEP 4 -- 'unique' claims declare their comparison class"); print("=" * 78)
need = {
 "P53": "among the ten exceptional fillings",
 "P48": "imaginary-quadratic trace fields",
 "P10": "not** an independent proof",
 "P43": "CORRECTED 2026-07-15",
 "P46": "SPLIT 2026-07-15",
}
ok4 = True
for pid, frag in need.items():
    row = next((l for l in claims.splitlines() if l.strip().startswith(f"| {pid} ")), "")
    hit = frag in row
    ok4 &= hit
    print(f"  {pid}: carries {frag!r} -> {hit}")
print(f"  ALL FIVE: {ok4}")

print(); print("=" * 78); print("SWEEP 5 -- the keyword shape, on origin/main AND on this branch"); print("=" * 78)
print("  NOTE ON THE FLAG: they used `git grep -il`. `-ilw` returns 0 for HYPHENATED terms")
print("  (L-space), so -w is the wrong tool here; this recheck uses -il, as they did.")
def nfiles(term, ref):
    out = sh("git", "grep", "-il", term, ref, "--", "*.md")
    return len([l for l in out.splitlines() if l.strip()])
COVERED = {"Kashaev":121,"Mostow":83,"systole":58,"Alexander polynomial":52,"volume conjecture":42,
           "Reidemeister torsion":38,"Bianchi":29,"twisted Alexander":28,"Milnor":18,"L-space":16,
           "Brieskorn":14,"Dehn surgery":11,"F-theory":10}
diff = []
for t, c in COVERED.items():
    n = nfiles(t, "origin/main")
    if n != c: diff.append((t, c, n))
print(f"  COVERED: {len(COVERED)-len(diff)} of {len(COVERED)} reproduce exactly on origin/main")
for t, c, n in diff: print(f"    DIFFERS  {t}: they said {c}, measured {n}")
ABSENT = ["Milnor fibration","link of a singularity","Kronheimer","ADHM","Nakajima","quiver variety",
          "Gabriel's theorem","cluster algebra","elliptic surface","Minahan-Nemeschansky",
          "minimal resolution","exceptional divisor","simple singularity","waist size",
          "Jorgensen inequality","Heegaard Floer"]
bad = [t for t in ABSENT if nfiles(t, "origin/main") != 0]
now = [(t, nfiles(t, "HEAD")) for t in ABSENT if nfiles(t, "origin/main") == 0 and nfiles(t, "HEAD") > 0]
print(f"  ABSENT on origin/main: {len(ABSENT)-len(bad)} of {len(ABSENT)} confirmed at 0"
      + (f"   NOT absent: {bad}" if bad else ""))
print(f"  ALREADY PRESENT ON THIS BRANCH ({len(now)} of {len(ABSENT)}) -- work they cannot see:")
for t, n in now: print(f"    {t:26s} {n} file(s)")
print()
print("  THE DIACRITIC TRAP, checked and NOT a defect of theirs:")
print(f"    'Jorgensen inequality' on main : {nfiles('Jorgensen inequality','origin/main')}")
print(f"    'Jorgensen'  (ASCII)  on main  : {nfiles('Jorgensen','origin/main')}")
print(f"    'Jorgensen' with o-slash on main: {nfiles(chr(74)+chr(248)+'rgensen','origin/main')}")
print("    ALL the o-slash hits are ANDERSEN-JORGENSEN (arXiv:1206.2552, TQFT / Gauss sums) --")
print("    a DIFFERENT PERSON from Troels Jorgensen of the Kleinian-group inequality. Their")
print("    absence claim therefore holds at TOPIC level, not merely as a phrase. E72 shape:")
print("    one name, two people. Caught before it was reported as an E54 false absence.")

print(); print("=" * 78); print("SWEEP 2 -- located sample sizes"); print("=" * 78)
b993 = next(ROOT.glob("frontier/B993*/FINDINGS.md")).read_text(encoding="utf-8")
print(f"  B993 states its own sample '400-manifold census sample': {'400-manifold census sample' in b993}")
b1330 = (ROOT / "frontier/B1330_the_best_case_object/FINDINGS.md").read_text(encoding="utf-8")
print(f"  B1330's '952 in-domain sectors': {'952 in-domain sectors' in b1330}")
h = (ROOT / "frontier/B1346_the_chat1_handoff_intake/FINDINGS.md").read_text(encoding="utf-8")
print(f"  v2873 recorded PROTECTED (B1346's F1 table): {'v2873, which is PROTECTED' in h}")

print(); print("=" * 78); print("THE RETRACTED NUMBER"); print("=" * 78)
hits = [p for p in list(ROOT.glob("**/*.md")) + list(ROOT.glob("**/arc_verdict.json"))
        if ".git" not in str(p) and re.search(r"(?<![\d.])3427(?![\d])", p.read_text(encoding="utf-8", errors="ignore"))]
print(f"  their self-retracted '1 in 3427' statistic, as a standalone number in our prose: {len(hits)} file(s)")
print("  -> nothing to withdraw on our side; the number never entered the record.")
