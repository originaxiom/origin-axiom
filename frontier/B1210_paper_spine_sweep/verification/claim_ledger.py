"""Generate P3's CLAIM CANDIDATES from the sweep: the 48 law-creating arcs, thematically grouped."""
import json, os, re
from pathlib import Path
ROOT = Path(os.environ.get("OA_ROOT") or Path(__file__).resolve().parents[3])
sw = json.loads((Path(__file__).parent / "spine_sweep.json").read_text())
ARCS = {}
for p in ROOT.glob("frontier/*/arc_verdict.json"):
    try: v = json.loads(p.read_text(encoding="utf-8"))
    except Exception: continue
    if isinstance(v.get("id"), str): ARCS[v["id"]] = v

SECTIONS = [
 ("§3 forced — the chain and its landing",
  ["cascade", "landing", "global form", "hypercharge", "terminat", "Levi", "matter content", "Z/6", "Z6"]),
 ("§5 withheld — the value wall and the rank wall",
  ["value", "rank wall", "disjoint", "period", "regulator", "no bridge", "numerolog", "Door"]),
 ("§6 the observer — one bit, priced",
  ["mirror", "orientation", "torsor", "bit", "quine", "selector", "kappa", "K4", "parity", "spin"]),
 ("§2 the object — arithmetic and geometry",
  ["trace field", "quadratic", "Eisenstein", "spectrum", "arithmetic", "genesis axiom", "meridian"]),
 ("§10 the wall — what a specialist must supply",
  ["seam", "SEAM", "wall", "specialist", "hatch", "bar"]),
]
def assign(c):
    best, score = None, 0
    for name, kws in SECTIONS:
        s = sum(1 for k in kws if k.lower() in c.lower())
        if s > score: best, score = name, s
    return best or "UNASSIGNED — needs an editorial call"

law = sw["law_creating"]
groups = {}
for a in law:
    v = ARCS[a]
    groups.setdefault(assign(v["claim_one_line"]), []).append((a, v["verdict"], v["claim_one_line"]))

out = ["# P3 — CLAIM CANDIDATES, swept from the corpus (B1210)", "",
       "**Generated, not remembered.** The P3 spec was drafted from the thesis as held in mind and",
       f"cited **1 of the corpus's {len(law)} law-creating arcs**. This ledger is the mechanical",
       "counterpart: every arc with `creates_law = true` and a PROVED/NEGATIVE verdict, grouped by the",
       "section it would serve. **The grouping is a first pass by keyword; the disposition is an",
       "editorial call and is not made here.** Regenerate with `verification/spine_sweep.py` +",
       "`claim_ledger.py` whenever the corpus moves.", "",
       "Disposition column to be filled as the paper is written: **IN** (a claim P3 makes) ·",
       "**SUP** (cited as supporting evidence) · **OUT** (process, instrument, off-thesis, or superseded).", ""]
for name, _ in SECTIONS + [("UNASSIGNED — needs an editorial call", None)]:
    rows = groups.get(name)
    if not rows: continue
    out += [f"## {name}", "", "| arc | verdict | disposition | claim |", "|---|---|---|---|"]
    for a, v, c in rows:
        sup = sw["supersession"].get(a)
        flag = ""
        if sup:
            flag = " **⚠ later: " + ", ".join(f"{b} ({'/'.join(k)})" for b, k, _ in sup[:3]) + "**"
        out.append(f"| `{a}` | {v} | | {c[:200].replace('|', '/')}…{flag} |")
    out.append("")
out += ["## The spec's own citations, audited", "",
        "| cited arc | later arc that extends/corrects/withdraws it | action |", "|---|---|---|"]
for a, hits in sw["spec_citations_at_risk"].items():
    out.append(f"| `{a}` | " + ", ".join(f"`{b}` ({'/'.join(k)})" for b, k in hits) + " | read before quoting |")
out += ["", "*(Clause-scoped matching: the verb must sit within 90 characters of the reference. An",
        "earlier claim-scoped pass flagged 15 of 24 citations and was mostly noise — arc claims are",
        "long sentences about many things.)*"]
(ROOT / "papers/P3_THE_PAPER/CLAIM_CANDIDATES.md").write_text("\n".join(out) + "\n", encoding="utf-8")
print(f"claim ledger written: {sum(len(v) for v in groups.values())} law-creating arcs in "
      f"{len(groups)} groups")
for k, v in groups.items(): print(f"   {len(v):3d}  {k}")
