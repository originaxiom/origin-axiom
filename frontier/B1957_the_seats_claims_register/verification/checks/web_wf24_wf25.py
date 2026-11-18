"""B1957: the web seat's W-F24 and W-F25 (frame C's ratios against height; its cusp exponents), the parts main can
test on its own code.  Data-free.
 F1  W-F24's X1: at the mark, with the canonical end, each sector ratio's logarithm falls from height 2 to height 6
     (the seat: by 5.6 to 20.5, slopes 1.3 to 5.2 per unit of height).
 F2  W-F24's X4: the share of time the measure on words (random words of 40 letters, each weighted by its length,
     B1928's threads) spends above heights 1.5, 2, 3 and 4 (the seat: 0.384, 0.168, 0.035, 0.007).
 F3  W-F25's exponents, in the seat's convention E = -(1/pi) d log r/d Im tau, against B1945's table (rates in |q|,
     so E = 2k), cell by cell, with the seat's referee's limits for the slow cells; and its ratios of exponents."""
import sys, pathlib, functools, math, random
from fractions import Fraction as Fr
import numpy as np
print = functools.partial(print, flush=True)
ROOT = next(q for q in pathlib.Path(__file__).resolve().parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent)); import wb2_stage3_on_main as W
sys.path.insert(0, str(next((ROOT / "frontier").glob("B1932_*")) / "verification")); import ergodic_both_worlds as E

if __name__ == "__main__":
    a, b = Fr(2, 5), Fr(4, 5); drops = []
    for sec, (ql, qr) in W.SIX.items():
        Y2, Y6 = W.coupling("0.0", 2.0, a, b, ql, qr, False, as_mp=True), W.coupling("0.0", 6.0, a, b, ql, qr, False, as_mp=True)
        for rd in ("S", "St"):
            s2 = sorted((W.mp.svd_c(Y2[rd], compute_uv=False)), reverse=True); s6 = sorted((W.mp.svd_c(Y6[rd], compute_uv=False)), reverse=True)
            for i in (1, 2): drops.append((sec, rd, i + 1, float(W.mp.log(s2[i] / s2[0]) - W.mp.log(s6[i] / s6[0]))))
    d = [x[3] for x in drops]
    print("F1: at the mark, Re tau = 0, heights 2 to 6: the 12 ratios' logarithms fall by between %.1f and %.1f (slopes %.2f to %.2f per unit of height); every one falls: %s" % (min(d), max(d), min(d) / 4, max(d) / 4, min(d) > 0))
    cols = ["%.1f" % (k / 10) for k in range(-5, 6)]; acc = {}
    for tx in cols:
        for sec, (ql, qr) in W.SIX.items():
            Y2, Y6 = W.coupling(tx, 2.0, a, b, ql, qr, False, as_mp=True), W.coupling(tx, 6.0, a, b, ql, qr, False, as_mp=True)
            for rd in ("S", "St"):
                s2 = sorted((W.mp.svd_c(Y2[rd], compute_uv=False)), reverse=True); s6 = sorted((W.mp.svd_c(Y6[rd], compute_uv=False)), reverse=True)
                for i in (1, 2): acc.setdefault((sec, rd, i), []).append(float(W.mp.log(s2[i] / s2[0]) - W.mp.log(s6[i] / s6[0])))
    mean = [sum(v) / len(v) for v in acc.values()]
    print("F1 (added 2026-11-18, the seat's section 7.1): the same falls averaged over eleven columns Re tau = -0.5 to 0.5: between %.2f and %.2f (the seat's note: 5.6 to 20.5; its grid: 5.62 to 20.47). So main's 21.0 and the note's 20.5 are one figure read two ways" % (min(mean), max(mean)))
    for seed in (1924, 7):
        rng = random.Random(seed); tot = 0.0; above = {1.5: 0.0, 2: 0.0, 3: 0.0, 4: 0.0}; n = 0
        while n < 600:
            w = "".join(rng.choice("LR") for _ in range(40))
            if "L" not in w or "R" not in w: continue
            pts, ell = E.thread(w); n += 1; tot += ell
            for h in above: above[h] += ell * float((pts[:, 1] > h).mean())
        print("F2: seed %d, 600 words of 40 letters: share of time above heights 1.5, 2, 3, 4: %s (the seat: 0.384, 0.168, 0.035, 0.007)" % (seed, ", ".join("%.3f" % (above[h] / tot) for h in above)))
    main = {("2/5", "up", "S"): (Fr(3, 10), Fr(1, 2)), ("2/5", "up", "St"): (Fr(3, 10), Fr(4, 5)), ("2/5", "down", "S"): (Fr(1, 5), Fr(11, 20)), ("2/5", "down", "St"): (Fr(1, 5), Fr(13, 20)),
            ("1/5", "up", "S"): (Fr(1, 10), Fr(3, 5)), ("1/5", "up", "St"): (Fr(1, 10), Fr(1, 2)), ("1/5", "down", "S"): (Fr(1, 5), Fr(11, 20)), ("1/5", "down", "St"): (Fr(1, 5), Fr(13, 20))}      # B1945's table
    seat = {("2/5", "up", "S"): (Fr(3, 5), Fr(1)), ("2/5", "up", "St"): (Fr(3, 5), Fr(8, 5)), ("2/5", "down", "S"): (Fr(2, 5), Fr(11, 10)), ("2/5", "down", "St"): (Fr(2, 5), Fr(13, 10)),
            ("1/5", "up", "S"): (Fr(1, 5), Fr(6, 5)), ("1/5", "up", "St"): (Fr(1, 5), Fr(1)), ("1/5", "down", "S"): (Fr(2, 5), Fr(11, 10)), ("1/5", "down", "St"): (Fr(2, 5), Fr(13, 10))}          # the note, with its referee's limits
    table = (next((ROOT / "frontier").glob("B1945_*")) / "FINDINGS.md").read_text()
    assert "| ±1/5 | 1/10, 3/5 | 1/10, 1/2 | 1/5, 11/20 | 1/5, 13/20 |" in table and "| ±2/5 | 3/10, 1/2 | 3/10, 4/5 | 1/5, 11/20 | 1/5, 13/20 |" in table
    print("F3: the seat's eight cells (mark and twin, up and down, both readings) equal twice B1945's rates: %s; its ratios at the mark in S: 1/(3/5) = %s and (11/10)/(2/5) = %s within a sector; (3/5)/(2/5) = %s and 1/(11/10) = %s between sectors" % (all(tuple(2 * k for k in main[c]) == seat[c] for c in main), Fr(1) / Fr(3, 5), Fr(11, 10) / Fr(2, 5), Fr(3, 5) / Fr(2, 5), Fr(1) / Fr(11, 10)))
