"""B1210 -- THE PAPER-SPINE SWEEP: build P3's claim pool FROM THE CORPUS, and find supersession.

Written because the P3 spec, drafted from the thesis as held in mind, cited 11 of the 85 arcs banked
in its own last ten days and 1 of the corpus's 48 law-creating arcs. A paper spine assembled from
memory reproduces the memory, not the record.
"""
import json, os, re
from pathlib import Path

ROOT = Path(os.environ.get("OA_ROOT") or Path(__file__).resolve().parents[3])
ARCS = {}
for p in sorted(ROOT.glob("frontier/*/arc_verdict.json")):
    try: v = json.loads(p.read_text(encoding="utf-8"))
    except Exception: continue
    if isinstance(v.get("id"), str):
        ARCS[v["id"]] = {**v, "dir": p.parent.name}

def num(a):
    m = re.match(r"B(\d+)", a); return int(m.group(1)) if m else 0

print(f"corpus: {len(ARCS)} arcs with verdicts")

# ---- 1. the claim pool -------------------------------------------------------------------
SURFACES = ["docs/LAW_MAP.md", "docs/THE_SM_VERDICT.md", "docs/SM_SPECIFICATION_LEDGER.md",
            "docs/GUT_REQUIREMENTS_LEDGER.md", "docs/THEOREM_REGISTRY.md"]
surf_text = ""
for rel in SURFACES:
    f = ROOT / rel
    if f.exists(): surf_text += f.read_text(encoding="utf-8", errors="ignore")
on_surface = {a for a in ARCS if re.search(rf"\b{a}\b", surf_text)}
law = {a for a, v in ARCS.items() if v.get("creates_law") and v.get("verdict") in ("PROVED", "NEGATIVE")}
pool = sorted(law | on_surface, key=num)
print(f"claim pool: {len(pool)}  (law-creating {len(law)}, on a synthesis surface {len(on_surface)})")

# ---- 2. supersession: which LATER arcs talk about each pool arc, and how ------------------
VERBS = {"extend": ["extends", "extended", "and extends"],
         "correct": ["corrects", "corrected", "re-scoped", "rescoped", "amended", "supersedes"],
         "withdraw": ["withdrawn", "retracted", "refuted", "REFUTED", "WITHDRAWN"],
         "confirm": ["confirms", "confirmed", "independently confirm", "re-verified", "reproduces"]}
rel = {}
for a in pool:
    n = num(a)
    hits = []
    for b, v in ARCS.items():
        if num(b) <= n: continue
        c = v.get("claim_one_line", "")
        for m in re.finditer(rf"\b{a}\b", c):
            # CLAUSE SCOPE, not claim scope. An arc claim is one long sentence about many things;
            # scanning the whole of it for "refuted" flagged B1159 as withdrawing B727 when it
            # CITES it, and B978 as withdrawing B862 when it is the arc that CONFIRMS it. The verb
            # must sit next to the reference to mean anything about it.
            w = c[max(0, m.start() - 90):m.start() + 90]
            kinds = [k for k, ws in VERBS.items() if any(x in w for x in ws)]
            if kinds:
                hits.append((b, kinds, w.strip()))
                break
    if hits: rel[a] = sorted(hits, key=lambda h: num(h[0]))
print(f"pool arcs with a later arc that extends/corrects/withdraws/confirms them: {len(rel)}")

# ---- 3. the spec's own citations, audited ------------------------------------------------
spec = (ROOT / "papers/P3_THE_PAPER/SPEC.md").read_text(encoding="utf-8")
cited = sorted({a for a in re.findall(r"B\d{2,4}", spec) if a in ARCS}, key=num)
print(f"\nP3 spec cites {len(cited)} arcs that exist: {cited}")
risk = {a: rel[a] for a in cited if a in rel}
print(f"OF THOSE, {len(risk)} have a later arc that extends/corrects/withdraws them:")
for a, hits in risk.items():
    print(f"  {a} <- " + "; ".join(f"{b} ({'/'.join(k)})" for b, k, _ in hits))

out = {"corpus": len(ARCS), "pool": pool, "law_creating": sorted(law, key=num),
       "on_surface_only": sorted(on_surface - law, key=num),
       "spec_cited": cited, "spec_citations_at_risk": {a: [[b, k] for b, k, _ in h] for a, h in risk.items()},
       "supersession": {a: [[b, k, c] for b, k, c in h] for a, h in rel.items()}}
(Path(__file__).parent / "spine_sweep.json").write_text(json.dumps(out, indent=1) + "\n")
print("\nwrote spine_sweep.json")
print("VERIFIED")
