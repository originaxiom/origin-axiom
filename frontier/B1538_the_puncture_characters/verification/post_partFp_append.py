"""B1538 -- the append: written during Part F' (before any Part F' reading was read), run once after Part F' exits 0.
Checks run_F_scoped.jsonl's structure (kinds and counts only), appends it to run_F.jsonl (the sealed partial record), and
records the sha-256 of each file before and after (verification/run_F_append.json).  No reading is printed."""
import hashlib
import json
from pathlib import Path

V = Path(__file__).resolve().parent
F, P = V / "run_F.jsonl", V / "run_F_scoped.jsonl"


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


before = sha(F)
assert before == "1e9c6e5550f2bb46453375cce8761e87ad6307a19d0ce25f1bb80f74602bcec7", "run_F.jsonl is not the sealed partial"
assert F.read_bytes().endswith(b"\n")
heads = reads = 0
with open(P) as f:
    for line in f:
        k = json.loads(line)["kind"]
        heads += k == "candidate"
        reads += k == "reading"
assert (heads, reads) == (12152, 501792), (heads, reads)
assert P.read_bytes().endswith(b"\n")
scoped = sha(P)
lines_before = F.read_bytes().count(b"\n")
with open(F, "ab") as f:
    f.write(P.read_bytes())
after = sha(F)
lines_after = F.read_bytes().count(b"\n")
rec = {"run_F.jsonl before (the sealed partial record)": before, "lines before": lines_before,
       "run_F_scoped.jsonl (Part F')": scoped, "Part F' candidates": heads, "Part F' readings": reads,
       "run_F.jsonl after (the partial record, then Part F')": after, "lines after": lines_after}
assert rec["lines after"] == lines_before + heads + reads
(V / "run_F_append.json").write_text(json.dumps(rec, indent=1) + "\n")
print(json.dumps(rec, indent=1))
