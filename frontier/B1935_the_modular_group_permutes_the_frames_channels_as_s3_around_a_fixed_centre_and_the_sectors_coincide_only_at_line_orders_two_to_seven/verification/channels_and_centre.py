"""Two questions settled on the frame's own channel residues (main, 2026-11-14 night).
(1) Do T and S permute the frame's channels i, j, k as S3 = SL(2, Z)/Gamma(2), fixing channel 1? For each, find the
    permutation pi of {1, i, j, k} under which log|R_s(transformed)| - log|R_pi(s)(original)| is the same for every
    channel (a common modular factor), at generic points and lines, for all three sectors.
(2) Does the centre -I (two undoings) act as matter's charge sign and leave the Higgs reading? The frame at line -w
    against w, per reading."""
import sys, itertools, math, cmath, pathlib
import numpy as np
ROOT = next(q for q in pathlib.Path(__file__).resolve().parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
sys.path.insert(0, str(next((ROOT / "frontier").glob("B1928_*")) / "verification"))
import fiber_grid as FG
C = FG.C; B = C._modules()["B"]
CH = ["1", "i", "j", "k"]
SECT = {"up": ("Q", "u"), "down": ("Q", "d"), "lep": ("L", "e")}


def res(w, t, sec):
    lf, rf = SECT[sec]; x, y = B.sector_twists(w, t, B.SIXY[lf], B.SIXY[rf]); return B.residues(x, y, t)


def best_perm(R0, R1, tiny=1e-9):
    out = []
    for perm in itertools.permutations(CH):
        z0 = [abs(R0[p]) < tiny for p in perm]; z1 = [abs(R1[s]) < tiny for s in CH]
        if z0 != z1:
            continue
        d = [math.log(abs(R1[s]) / abs(R0[p])) for s, p in zip(CH, perm) if abs(R1[s]) >= tiny]
        if len(d) >= 2:
            out.append((max(d) - min(d), perm))
    out.sort()
    return out[0], (out[1] if len(out) > 1 else (float("inf"), None))


if __name__ == "__main__":
    taus = [complex(0.17, 1.31), complex(-0.23, 1.07), complex(0.31, 1.62)]
    lines = [(1 / 7, 3 / 7), (2 / 9, 5 / 9), (3 / 11, 1 / 11)]
    for name, move in (("T", lambda t, a, b: (t + 1, a, b - a)), ("S", lambda t, a, b: (-1 / t, -b, a))):
        found = {}
        for t, (a, b), sec in itertools.product(taus, lines, SECT):
            w = a * t + b; t2, a2, b2 = move(t, a, b); w2 = a2 * t2 + b2
            (spread, perm), (spread2, _) = best_perm(res(w, t, sec), res(w2, t2, sec))
            found.setdefault(perm, []).append((spread, spread2))
        for perm, v in found.items():
            print("%s: channels (1, i, j, k) -> %s  on %d cases; spread of the common factor max %.1e; next-best permutation's spread min %.1e" % (
                name, perm, len(v), max(x[0] for x in v), min(x[1] for x in v)))

    # (2) the centre -I: the line w -> -w, per reading, both worlds
    dev = {}
    for t, (a, b) in itertools.product(taus, lines):
        L = FG.CR.canon(t); L.pop("_extrapolated")
        o = C.frame(t, a, b, L); on = C.frame(t, (-a) % 1, (-b) % 1, L)
        for k in o:
            if "conjS" in k:
                continue
            r = k.split("|")[-1] if not k.startswith("ckm") else "|".join(k.split("|")[2:])
            d = max(abs(math.log(p / q)) for p, q in zip(o[k], on[k]) if p > 1e-10 and q > 1e-10)
            dev[r] = max(dev.get(r, 0), d)
    print("the centre -I (line -> -line), each reading kept: max |log| per reading:", {k: "%.1e" % v for k, v in dev.items()})
