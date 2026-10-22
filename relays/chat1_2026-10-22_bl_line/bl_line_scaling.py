#!/usr/bin/env python3
"""COMPUTED check, no data (committed before bl_line_scan.jsonl was read; the expectation is written here first):
on an order-5 hypercharge line the charges reduce mod 5 to Q ~ e^c and d^c ~ L, so with a B - L line w' the leptons'
twists are the down quarks' with the legs swapped and w' replaced by 3 w' (L: 2w - 3w', e^c: w + 3w' against
Q: w + w', d^c: 2w - w').  If the frame's couplings are symmetric under the leg swap up to transposition (B1703's d = e
suggests so), then on the tick's line, for every w' and every reading,
    leptons(w') = down(3 w')     (both ratios m2/m3 and m1/m3, both horocycles),
exactly, and the two Georgi-Jarlskog ratios are R2(w') = f2(3w')/f2(w'), R1(w') = f1(w')/f1(3w') with f the down
quarks' ratios.  On the order-10 lines of the other two points no such identity is expected.  The script compares, on
the scan's grid, every (a', b') with |a'|, |b'| <= 0.10 against (3a', 3b').
    python3 -B bl_line_scaling.py      # writes bl_line_scaling_run.txt"""
import json, math, pathlib

HERE = pathlib.Path(__file__).resolve().parent
rows = [json.loads(l) for l in (HERE / "bl_line_scan.jsonl").read_text().splitlines() if l.strip()]
LOG = []
for point in ("tick_d_eq_e", "six_best", "nine_best"):
    R = {(r["a2"], r["b2"]): r for r in rows if r["point"] == point}
    worst, n = 0.0, 0
    for (a2, b2), r in R.items():
        if abs(a2) <= 0.10 + 1e-9 and abs(b2) <= 0.10 + 1e-9:
            q = R.get((round(3 * a2, 2), round(3 * b2, 2)))
            if q is None:
                continue
            for hor in ("L_max", "L_2"):
                for rd in ("S", "St", "conjS"):
                    for x, y in zip(r[f"lep|{hor}|{rd}"], q[f"down|{hor}|{rd}"]):
                        n += 1
                        worst = max(worst, abs(x - y) if min(x, y) < 1e-8 else abs(math.log(x / y)))
    LOG.append(f"{point}: leptons(w') against down(3w') over {n} values: max |d ln| = {worst:.2e}")
print("\n".join(LOG))
(HERE / "bl_line_scaling_run.txt").write_text("\n".join(LOG) + "\n")
