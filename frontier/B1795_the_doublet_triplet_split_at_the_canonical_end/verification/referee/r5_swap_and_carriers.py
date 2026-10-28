"""Referee B1795, r5: (i) residues under the slot swap, unit by unit (expect R_1 -> -R_1, others fixed, since
bil(y, x) = bil(x, y)^T); (ii) the a-component shared on slope-2/5 lines: twist a-parts of D and H mod 1; (iii) strip,
carriers: light_H/light_D per (h, rn) with the extremes; (iv) the order-60 non-carrier lines and other 5a in Z lines."""
import pathlib as _pl; _ROOT = str(next(q for q in _pl.Path(__file__).resolve().parents if (q / 'frontier').is_dir() and (q / 'GENESIS.md').is_file()))
import json, math, pathlib
from fractions import Fraction as Fr
V = pathlib.Path(_ROOT + "/frontier/B1795_the_doublet_triplet_split_at_the_canonical_end/verification")
rows = [json.loads(l) for l in (V / "split_rows.jsonl").read_text().splitlines() if l.strip()]
worst = {}
for r in rows:
    for a, b in (("D", "Dc"), ("H", "Hc")):
        for s in "1ijk":
            x, y = complex(*r[a]["R"][s]), complex(*r[b]["R"][s]); n = math.sqrt(sum(abs(complex(*r[a]["R"][u])) ** 2 for u in "1ijk"))
            worst[s] = max(worst.get(s, 0), abs(x - y) / n, 0)
            worst[s + "+"] = max(worst.get(s + "+", 0), abs(x + y) / n)
print("slot swap, residues relative to |R|: |R_s - R_s'| max", {s: "%.1e" % worst[s] for s in "1ijk"}, " |R_s + R_s'| max", {s: "%.1e" % worst[s + "+"] for s in "1ijk"})
for b in ("7/60", "49/60", "11/12"):
    a = Fr(2, 5); bb = Fr(b)
    print("line (2/5, %s): D left twist (%s, %s), H left twist (%s, %s); a-parts mod 1: %s vs %s; b-parts differ by %s" % (b, -2 * a, -4 * bb, 3 * a, 6 * bb, (-2 * a) % 1, (3 * a) % 1, 6 * bb - (-4 * bb)))
