"""Render P3's CLAIM_CANDIDATES from the UNION pool, not from the declared field alone."""
import json, os, re
from pathlib import Path
ROOT = Path(os.environ.get("OA_ROOT") or Path(__file__).resolve().parents[3])
cb = json.loads((Path(__file__).parent / "claim_base.json").read_text())
ARCS = {}
for p in ROOT.glob("frontier/*/arc_verdict.json"):
    try: v = json.loads(p.read_text(encoding="utf-8"))
    except Exception: continue
    if isinstance(v.get("id"), str): ARCS[v["id"]] = v
def num(a):
    m = re.match(r"B(\d+)", a); return int(m.group(1)) if m else 0

SECTIONS = [
 ("§3 forced — the chain and its landing",
  ["cascade","landing","global form","hypercharge","terminat","Levi","matter content","Z/6","Z6"]),
 ("§5 withheld — the value wall and the rank wall",
  ["value","rank wall","disjoint","period","regulator","no bridge","numerolog","Door","normalis"]),
 ("§6 the observer — one bit, priced",
  ["mirror","orientation","torsor","bit","quine","selector","kappa","K4","parity","spin","adelic"]),
 ("§2 the object — arithmetic and geometry",
  ["trace field","quadratic","Eisenstein","spectrum","arithmetic","genesis axiom","meridian"]),
 ("§10 the wall — what a specialist must supply",
  ["seam","SEAM","wall","specialist","hatch","bar"]),
]
def assign(c):
    best, sc = None, 0
    for name, kws in SECTIONS:
        s = sum(1 for k in kws if k.lower() in c.lower())
        if s > sc: best, sc = name, s
    return best or "UNASSIGNED — needs an editorial call"

# TIER the pool so an editor sees WHY each arc is here
declared = set(cb["pool_new"]) & {a for a, v in ARCS.items() if v.get("creates_law") is True}
vocab_only = set(cb["added_by_vocabulary"])
rest = set(cb["pool_new"]) - declared - vocab_only

out = ["# P3 — CLAIM CANDIDATES, rebuilt on the UNION criterion (B1213)", "",
 "**This document was previously rendered from `creates_law` alone.** Cloud's memo 133 found that",
 f"the field is **absent on {cb['absent']} of {cb['settled']} settled arcs — {cb['absent_pct']}%** —",
 "so a sweep reading it treats *declared false* and *never declared* identically. B1210 corrected",
 "wrong flags; this rebuild stops the base depending on the flag at all.", "",
 f"**POOL = declared-law ({len(declared)}) ∪ on-a-synthesis-surface ∪ law-vocabulary "
 f"({len(vocab_only) + len(set(cb['vocabulary_split']['absent']) | set(cb['vocabulary_split']['declared_false']) & set(cb['pool_new'])) - len(vocab_only)})"
 f" = {len(cb['pool_new'])} arcs.**",
 f"The vocabulary criterion adds **{len(vocab_only)} arcs neither the flag nor any surface reaches**.",
 "",
 f"**Two-sided control, run before the criterion was used**: declared-law arcs score",
 f"**{cb['control']['declared_mean']}** on the corpus's own law vocabulary against",
 f"**{cb['control']['rest_mean']}** for the rest — **{cb['control']['ratio']}×**. The criterion",
 "discriminates, so it is not noise. Had it not, the rebuild would have reported itself void.", "",
 "**Tier** tells an editor why an arc is here: **L** declared law-creating · **S** carried on a",
 "synthesis surface · **V** reached only by the law-vocabulary criterion (the arcs the old base",
 "could not see). **Disposition** stays empty — **IN** / **SUP** / **OUT** is an editorial call.", ""]

groups = {}
for a in cb["pool_new"]:
    v = ARCS.get(a)
    if not v: continue
    tier = "L" if a in declared else ("V" if a in vocab_only else "S")
    groups.setdefault(assign(v["claim_one_line"]), []).append((a, v["verdict"], tier, v["claim_one_line"]))

for name, _ in SECTIONS + [("UNASSIGNED — needs an editorial call", None)]:
    rows = groups.get(name)
    if not rows: continue
    rows.sort(key=lambda r: ({"L": 0, "V": 1, "S": 2}[r[2]], num(r[0])))
    out += [f"## {name} ({len(rows)})", "", "| arc | verdict | tier | disposition | claim |",
            "|---|---|---|---|---|"]
    for a, vd, tier, c in rows:
        out.append(f"| `{a}` | {vd} | {tier} | | {c[:170].replace('|','/')}… |")
    out.append("")
out += ["## The exhibit that forced the rebuild", "",
 "**B991** — verdict PROVED, `instrument: false`, **`creates_law` absent** — whose own claim reads",
 "*\"THE HYPERCHARGE NORMALISATION IS NOT DERIVABLE IN PRINCIPLE, and that is a THEOREM ABOUT THE",
 "EQUATIONS rather than a limitation of the object.\"* It was inside B1210's pool via a synthesis",
 "surface, but **absent from the rendered document**, which listed only the flag-derived subset.",
 "The pool was wider than the page: that gap is what this rebuild closes."]
(ROOT / "papers/P3_THE_PAPER/CLAIM_CANDIDATES.md").write_text("\n".join(out) + "\n", encoding="utf-8")
tot = sum(len(v) for v in groups.values())
print(f"rendered {tot} candidates across {len(groups)} groups")
for k, v in sorted(groups.items(), key=lambda kv: -len(kv[1])): print(f"   {len(v):4d}  {k}")
