"""B1508 -- the audit lane's R69 (LEVEL_ACTION.md, 2026-10-01) read against B1506's own record.

R69 recomputed B1506's D0 over Q(i) and printed the counts of the induced object restricted to levels 1..6 as (-1,-1,-3,-1,-1,-3),
with the pullback of D0 keeping -1.  B1506's post-run record (post_run_checks.json, RS3) holds the same numbers from this seat's
instrument; B1506's section E holds the pullbacks.  So the two benches agree, and the scope R69 draws is visible in this seat's own
record: one T5 doublet background keeps its count under pullback (T2), while the induced object Ind D0 -- a single rank-six
background on the root -- counts -gcd(n, 3) on M_n.  'One background, one count' holds for the first kind, not the second.
"""
import json
import sys
from math import gcd
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
B1506 = ROOT / "frontier" / "B1506_the_level" / "verification"
R69_PRINTED = [-1, -1, -3, -1, -1, -3]          # LEVEL_ACTION.md, 'Positive result and what it counts'


def main():
    post = json.loads((B1506 / "post_run_checks.json").read_text(encoding="utf-8"))
    rs3 = post["RS3"]
    roots = rs3["root_objects"]["3"]
    unlifted_minus = [r for r in roots if not r["lifted"] and r["background"] == [-1] * 6]
    counts = unlifted_minus[0]["counts_M1_to_M6"] if unlifted_minus else None
    gcd_law = [-gcd(n, 3) for n in range(1, 7)]
    level = json.loads((B1506 / "the_level.json").read_text(encoding="utf-8"))
    pull = [row for row in level["E"] if isinstance(row, dict) and row.get("base") == 3 and row.get("cover") == 6] \
        if isinstance(level.get("E"), list) else []
    if not pull and isinstance(level.get("E"), dict):
        pull = [v for v in level["E"].values() if isinstance(v, dict) and v.get("base") == 3 and v.get("cover") == 6]
    return {
        "s961_generation_shaped": rs3["generation_shaped"],
        "ind_D0_counts_per_sector": counts,
        "every_sector_equals_R69": counts is not None and all(row == R69_PRINTED for row in counts),
        "equals_minus_gcd_n_3": counts is not None and all(row == gcd_law for row in counts),
        "pullback_3_to_6": pull[0] if pull else None,
        "pullbacks_keep_index": bool(pull) and pull[0]["index_kept"] == pull[0]["candidates"],
    }


if __name__ == "__main__":
    res = main()
    out = json.dumps(res, indent=1, sort_keys=True)
    print(out)
    if "--record" in sys.argv:
        Path(__file__).with_name("level_counts_run.txt").write_text(out + "\n", encoding="utf-8")
