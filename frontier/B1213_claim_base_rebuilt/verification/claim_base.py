"""B1213 -- THE CLAIM BASE, rebuilt on a criterion that does not read the broken field.

B1210 built the paper's claim pool from `creates_law` plus the registered synthesis surfaces.
B1211 corrected arcs whose flag was WRONG. Cloud's memo 133 found the larger mode: the field is
ABSENT on 920 of 1033 settled arcs -- 89% -- so a sweep reading it treats "declared false" and
"never declared" identically, as "not a law". The pool, and therefore the paper's claim base, was
drawn from a field nine tenths of the corpus never populated.

The repair is not to fill the field 920 times. It is to stop making the pool depend on it:
    POOL = declared-law  UNION  law-vocabulary candidates  UNION  on-a-synthesis-surface
with the vocabulary criterion carrying its own two-sided control, run before it is used.
"""
import json, os, re
from pathlib import Path

ROOT = Path(os.environ.get("OA_ROOT") or Path(__file__).resolve().parents[3])
VOCAB = ["theorem", "law", "forced", "no-go", "impossible", "unique", "exactly",
         "necessary and sufficient", "cannot", "never", "always", "iff", "permanent"]
SURFACES = ["docs/LAW_MAP.md", "docs/THE_SM_VERDICT.md", "docs/SM_SPECIFICATION_LEDGER.md",
            "docs/GUT_REQUIREMENTS_LEDGER.md", "docs/THEOREM_REGISTRY.md"]

ARCS = {}
for p in sorted(ROOT.glob("frontier/*/arc_verdict.json")):
    try: v = json.loads(p.read_text(encoding="utf-8"))
    except Exception: continue
    if isinstance(v.get("id"), str): ARCS[v["id"]] = v
settled = {a: v for a, v in ARCS.items() if v.get("verdict") in ("PROVED", "NEGATIVE")}

def vocab(v):
    c = v.get("claim_one_line", "").lower()
    return sum(1 for w in VOCAB if w in c)

# --- the declaration census: the finding that forced this rebuild ---------------------------
true_ = [a for a, v in settled.items() if v.get("creates_law") is True]
false_ = [a for a, v in settled.items() if "creates_law" in v and v["creates_law"] is not True]
absent = [a for a, v in settled.items() if "creates_law" not in v]
print(f"settled arcs: {len(settled)}   declared true: {len(true_)}   declared false: {len(false_)}"
      f"   ABSENT: {len(absent)} ({100*len(absent)/len(settled):.0f}%)")

# --- the two-sided control, BEFORE the criterion is used ------------------------------------
md = sum(vocab(settled[a]) for a in true_) / len(true_)
rest = [a for a in settled if a not in true_]
mr = sum(vocab(settled[a]) for a in rest) / len(rest)
print(f"control: declared-law mean {md:.2f} vs rest {mr:.2f} = {md/mr:.2f}x")
if md / mr <= 1.5:
    print("CONTROL FAILED -- the vocabulary does not discriminate; cell is VOID."); raise SystemExit(1)
print("control PASSES -- the criterion discriminates, so it is not noise")

# --- the union pool -------------------------------------------------------------------------
surf = ""
for rel in SURFACES:
    f = ROOT / rel
    if f.exists(): surf += f.read_text(encoding="utf-8", errors="ignore")
# Short ids (B1-B9, verdicts since L196 / 2026-09-02) collide with section labels on the surfaces
# ("### B2. CHOSEN / MEASURED" in SM_SPECIFICATION_LEDGER is a category, not an arc): a bare
# word-boundary match is not a citation for them; require the backticked or "arc"-prefixed form.
def cited(a):
    if len(a) <= 2:
        return re.search(rf"`{a}`|\barc {a}\b|\b{a}_[a-z]", surf) is not None
    return re.search(rf"\b{a}\b", surf) is not None
on_surface = {a for a in settled if cited(a)}
by_vocab = {a for a, v in settled.items()
            if not v.get("instrument") and v.get("creates_law") is not True and vocab(v) >= md}
pool = set(true_) | on_surface | by_vocab
def num(a):
    m = re.match(r"B(\d+)", a); return int(m.group(1)) if m else 0
print(f"\nPOOL = declared({len(true_)}) U surface({len(on_surface)}) U vocabulary({len(by_vocab)})"
      f" = {len(pool)} arcs")
print(f"  the vocabulary criterion adds {len(pool - set(true_) - on_surface)} arcs neither the flag"
      f" nor any surface reaches")
split = {"absent": [a for a in by_vocab if 'creates_law' not in settled[a]],
         "declared_false": [a for a in by_vocab if 'creates_law' in settled[a]]}
print(f"  of the vocabulary candidates: {len(split['absent'])} have the field ABSENT, "
      f"{len(split['declared_false'])} have it declared FALSE")

exhibit = settled.get("B991")
print(f"\nTHE EXHIBIT B991: in the old pool? {'B991' in (set(true_) | on_surface)}   "
      f"in the new pool? {'B991' in pool}")
out = {"settled": len(settled), "declared_true": len(true_), "declared_false": len(false_),
       "absent": len(absent), "absent_pct": round(100*len(absent)/len(settled)),
       "control": {"declared_mean": round(md, 2), "rest_mean": round(mr, 2),
                   "ratio": round(md/mr, 2), "passes": True},
       "pool_old": sorted(set(true_) | on_surface, key=num),
       "pool_new": sorted(pool, key=num),
       "added_by_vocabulary": sorted(pool - set(true_) - on_surface, key=num),
       "vocabulary_split": {k: sorted(v, key=num) for k, v in split.items()}}
(Path(__file__).parent / "claim_base.json").write_text(json.dumps(out, indent=1) + "\n")
print("\nwrote claim_base.json")
print("VERIFIED")
