"""B1211 -- THE DECLARATION COUNTER-CHECK: the registry gate reads a field the SEAT fills in.

gate_theorem_registry enforces "every arc declaring creates_law=true has a registry row". That
catches OVER-declaration. It cannot catch UNDER-declaration, because an arc that declares false is
invisible to it -- and the seat that writes the claim also writes the flag. This check is the other
side: an arc whose CLAIM TALKS LIKE A THEOREM while its FLAG says otherwise.
"""
import json, os, re
from pathlib import Path
ROOT = Path(os.environ.get("OA_ROOT") or Path(__file__).resolve().parents[3])

# Theorem-grade language: a NAMED result, or an explicit claim of proof/exhaustion/impossibility.
THEOREM_WORDS = [r"\bTHE [A-Z][A-Z' -]{4,40}THEOREM\b", r"\bTHEOREM\b", r"\bwe prove\b",
                 r"\bPROVED (?:EXACTLY|ALL-|IN GENERAL)", r"\bis a THEOREM\b",
                 r"\bIMPOSSIBLE\b", r"\bCANNOT (?:BE|EXIST)", r"\bEXHAUSTIVE\b", r"\bUNIQUE\b"]
# Words by which an arc disowns theorem status FOR ITSELF. Scope matters, again: a first pass put
# "cited, not" and "harvest" in this list globally and lost B1183 (THE ONE-CLASS THEOREM) and B1200,
# because both FENCE AN INPUT with exactly those words while proving something themselves. A fence
# on a borrowed computation is not a disclaimer about the arc. Only strong self-limits count, and
# only in the HEADLINE REGION where an arc states what it is.
DISOWN = [r"not a theorem", r"an interpretation joining", r"process arc", r"no mathematics",
          r"bookkeep", r"NOT PROVED"]
HEADLINE = 400

rows = []
for p in sorted(ROOT.glob("frontier/*/arc_verdict.json")):
    try: v = json.loads(p.read_text(encoding="utf-8"))
    except Exception: continue
    if v.get("verdict") not in ("PROVED", "NEGATIVE") or v.get("creates_law") is True: continue
    if v.get("instrument"): continue
    c = v.get("claim_one_line", "")
    hits = [w for w in THEOREM_WORDS if re.search(w, c)]
    dis = [d for d in DISOWN if re.search(d, c[:HEADLINE], re.I)]
    if len(hits) >= 2 and not dis:
        rows.append({"id": v["id"], "verdict": v["verdict"], "signals": len(hits),
                     "claim": c[:130]})
def num(r):
    m = re.match(r"B(\d+)", r["id"]); return int(m.group(1)) if m else 0
rows.sort(key=lambda r: -num(r))
print(f"UNDER-DECLARATION CANDIDATES (theorem-grade language, creates_law != true, no self-limit):"
      f" {len(rows)}")
print("\nthe 20 most recent -- the band where the registry stops (its last row is B1145):")
for r in rows[:20]:
    print(f"  {r['id']:7s} {r['verdict']:9s} sig={r['signals']}  {r['claim'][:92]}")
(Path(__file__).parent / "declaration_check.json").write_text(json.dumps(rows, indent=1) + "\n")
print(f"\nwrote declaration_check.json ({len(rows)} rows)")
print("VERIFIED")
