import json, math
from fractions import Fraction as Fr
R = str(next(q for q in __import__("pathlib").Path(__file__).resolve().parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())) + "/"
rows = [json.loads(l) for l in open(R + "frontier/B1792_the_offset_recurrence_at_order_60/verification/census.jsonl") if l.strip()]
idx = {(r["b"], r["apex"]): r for r in rows}
apx = sorted({(r["apex"], r["Re_tau"], r["Im_tau"]) for r in rows})
lg = lambda x: [math.log(max(t, 1e-300)) for t in x]
def maxdiff(b1, b2, sec):
    worst = 0.0
    for (a, _, _) in apx:
        r1, r2 = idx[(b1, a)], idx[(b2, a)]
        for h in ("L_max", "L_2"):
            for rd in ("S", "St"):
                x, y = lg(r1[f"{sec}|{h}|{rd}"]), lg(r2[f"{sec}|{h}|{rd}"])
                worst = max(worst, max(abs(p - q) for p, q in zip(x, y)))
    return worst
pairs = [("1/60", "41/60", "7/20 shifts: fails/carries"), ("7/12", "11/12", "1/4 shifts: fails/carries"), ("7/60", "47/60", "9/20 shifts: both carry"),
         ("29/60", "49/60", "3/20 shifts: both carry"), ("13/60", "53/60", "11/20 shifts"), ("23/60", "43/60", "1/20 shifts")]
print("max |delta log ratio| over 125 apexes x 2 horocycles x 2 readings, same apex")
for b1, b2, note in pairs:
    print("%-6s vs %-6s %-28s up %.3f down %.3f lep %.3e" % (b1, b2, note, maxdiff(b1, b2, "up"), maxdiff(b1, b2, "down"), maxdiff(b1, b2, "lep")))
