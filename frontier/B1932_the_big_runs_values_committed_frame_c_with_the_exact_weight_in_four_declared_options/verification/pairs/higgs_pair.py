"""The Higgs pair (main, 2026-11-14): does any orientation-reversing move of the record carry world 1 (up S~, down S,
leptons S) onto world 2 (up S, down S~, leptons S~)? Expectations: EXPECTATIONS_higgs_pair.md, written first.
Frame: B1656's with the closed-form channel norm, read through B1928's fiber_grid import; the canonical end read at
each point (B1927: covariant, so reading it at the image is the end's own law). Writes higgs_pair.json beside itself."""
import json, math, pathlib, sys, itertools
import numpy as np
ROOT = next(q for q in pathlib.Path(__file__).resolve().parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
sys.path.insert(0, str(next((ROOT / "frontier").glob("B1928_*")) / "verification"))
import fiber_grid as FG
CR, C = FG.CR, FG.C
HERE = pathlib.Path(__file__).resolve().parent

W1 = lambda h: {"up": "up|%s|St" % h, "down": "down|%s|S" % h, "lep": "lep|%s|S" % h, "ckm": "ckm|%s|St|S" % h}
W2 = lambda h: {"up": "up|%s|S" % h, "down": "down|%s|St" % h, "lep": "lep|%s|St" % h, "ckm": "ckm|%s|S|St" % h}
TAUS = [complex(0.13, 1.4), complex(-0.27, 1.9), complex(0.31, 1.15)]
LINES = [(0.2, 0.4), (0.4, 0.2), (0.6, 0.8)]
MOVES = {"mirror": lambda t: -t.conjugate(), "swap": lambda t: 1 / t.conjugate()}
LINEMAPS = {"%s%s%s" % (o, sa, sb): (o, sa, sb) for o in ("ab", "ba") for sa in "+-" for sb in "+-"}


def canon(t):
    L = CR.canon(t); L.pop("_extrapolated"); return L


def frame(t, a, b):
    return C.frame(t, a, b, canon(t))


def dev(o1, k1, o2, k2):
    d = 0.0
    for h in ("L_max", "L_2"):
        for s in ("up", "down", "lep", "ckm"):
            for p, q in zip(o1[k1(h)[s]], o2[k2(h)[s]]):
                if p > 1e-10 and q > 1e-10:
                    d = max(d, abs(math.log(p / q)))
    return d


def mapline(a, b, spec):
    o, sa, sb = spec
    x, y = (a, b) if o == "ab" else (b, a)
    return (x if sa == "+" else -x) % 1, (y if sb == "+" else -y) % 1


if __name__ == "__main__":
    base = {(i, j): frame(t, *l) for i, t in enumerate(TAUS) for j, l in enumerate(LINES)}
    out = {}
    for mv, f in MOVES.items():
        for name, spec in LINEMAPS.items():
            w12 = w11 = 0.0
            for (i, j), o in base.items():
                t2 = f(TAUS[i]); a2, b2 = mapline(*LINES[j], spec); o2 = frame(t2, a2, b2)
                w12 = max(w12, dev(o, W1, o2, W2)); w11 = max(w11, dev(o, W1, o2, W1))
            out["%s|%s" % (mv, name)] = {"world1_to_world2": w12, "world1_to_world1 (control)": w11}
            print("%-7s %-5s  world1->world2 %.2e   world1->world1 %.2e" % (mv, name, w12, w11), flush=True)
    (HERE / "higgs_pair.json").write_text(json.dumps(out, indent=1))
