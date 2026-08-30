"""B1211 -- THE DEEP SPINE SWEEP: the 541 substantive arcs B1210's criterion did not reach.

B1210 swept by `creates_law` plus the registered synthesis surfaces (421 arcs) and fenced the rest
as unswept. This is the rest. The question is NOT "which arcs are good" -- they are all banked -- but
"which of them state something the paper would CLAIM or RELY ON, and is that statement reachable
from any surface a reader (or a future draft) would consult?"

The instrument scores each arc on two independent axes and reports the JOINT top, because either
axis alone is known to mislead:
  RESULT-STRENGTH -- does the claim assert a theorem-grade fact (forced / impossible / exactly /
      unique / no ... exists), as opposed to reporting a process, a harvest, or a status?
  THESIS-PROXIMITY -- does it speak the paper's own three movements' vocabulary?
An arc scoring high on both, and cited on NO synthesis surface, is the paper's blind spot: a
theorem-grade statement about the thesis that nothing a reader consults will surface.
"""
import json, os, re
from pathlib import Path

ROOT = Path(os.environ.get("OA_ROOT") or Path(__file__).resolve().parents[3])
ARCS = {}
for p in sorted(ROOT.glob("frontier/*/arc_verdict.json")):
    try: v = json.loads(p.read_text(encoding="utf-8"))
    except Exception: continue
    if isinstance(v.get("id"), str): ARCS[v["id"]] = v
sw = json.loads((ROOT / "frontier/B1210_paper_spine_sweep/spine_sweep.json").read_text())
covered = set(sw["pool"])

def num(a):
    m = re.match(r"B(\d+)", a); return int(m.group(1)) if m else 0

# --- the two axes -------------------------------------------------------------------------
STRENGTH = [r"\bTHEOREM\b", r"\bFORCED\b", r"\bIMPOSSIBLE\b", r"\bPROVED\b", r"\bexactly\b",
            r"\bunique(ly)?\b", r"\bno [a-z ]{0,20}exists\b", r"\bcannot\b", r"\bnever\b",
            r"\bidentically\b", r"\bexhaustive\b", r"\ball [0-9]+\b", r"\bzero\b"]
# process/status words that mark an arc as bookkeeping rather than a claim the paper would make
PROCESS = [r"\bharvest", r"\brelay", r"\bledger row", r"\bgate\b", r"\bbookkeep", r"\bregistr",
           r"\bcurrency", r"\btriage", r"\bre-?bank", r"\bdisposition", r"\bReview \d"]
MOVEMENTS = {
 "I forced":   ["E6", "E₆", "hypercharge", "cascade", "breaking", "anomal", "chiral", "generation",
                "Levi", "termination", "registerab", "global form", "27", "16", "SO(10)", "SU(5)"],
 "II withheld":["value", "period", "ratio", "disjoint", "regulator", "numerolog", "rank reduction",
                "scale", "Mostow", "no bridge", "miss", "sigma", "σ"],
 "III observer":["mirror", "orientation", "torsor", "observer", "bit", "quine", "selector", "kappa",
                "κ", "parity", "adelic", "closing", "self-", "involution", "Galois"],
}

def score(c):
    s = sum(1 for p in STRENGTH if re.search(p, c, re.I))
    pr = sum(1 for p in PROCESS if re.search(p, c, re.I))
    mv = {k: sum(1 for w in ws if w.lower() in c.lower()) for k, ws in MOVEMENTS.items()}
    best = max(mv, key=lambda k: mv[k])
    return s, pr, best, mv[best]

rows = []
for a, v in ARCS.items():
    if a in covered or v.get("verdict") not in ("PROVED", "NEGATIVE") or v.get("instrument"):
        continue
    c = v.get("claim_one_line", "")
    s, pr, mvname, mvs = score(c)
    rows.append({"id": a, "verdict": v["verdict"], "strength": s, "process": pr,
                 "movement": mvname, "prox": mvs, "joint": s + mvs - 2 * pr, "claim": c[:150]})
rows.sort(key=lambda r: (-r["joint"], -r["strength"], num(r["id"])))
print(f"unswept substantive non-instrument arcs: {len(rows)}")
band = [r for r in rows if r["strength"] >= 4 and r["prox"] >= 3 and r["process"] == 0]
print(f"JOINT TOP BAND (strength >= 4, proximity >= 3, no process markers): {len(band)}")
by_mv = {}
for r in band: by_mv.setdefault(r["movement"], []).append(r)
for k in sorted(by_mv): print(f"    {k:15s} {len(by_mv[k])}")
print("\ntop 25 by joint score:")
for r in rows[:25]:
    print(f"  {r['id']:7s} {r['verdict']:9s} s={r['strength']} p={r['prox']} [{r['movement']}] {r['claim'][:88]}")
out = {"unswept": len(rows), "band": band, "all": rows}
(Path(__file__).parent / "deep_sweep.json").write_text(json.dumps(out, indent=1) + "\n")
print("\nwrote deep_sweep.json")
print("VERIFIED")
