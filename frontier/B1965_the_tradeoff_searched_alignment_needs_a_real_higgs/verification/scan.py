"""B1965 (main, 2026-11-19; data-free; exploratory, its question stated here before the run, no expectations hashed): at fixed points of frame C, an arbitrary constant Higgs triplet h
in C^3 in place of DR.  Under the charge rule (up S~, down S): |V_ll| (lightest up with lightest down), the smallest
diagonal |V| (alignment), and each sector's m2/m3 and m1/m3; with r = |h.h|/|h|^2 (B1739's reality).
Question: is there a frontier, e.g. no h with alignment >= 0.9 and both sectors' m2/m3 <= 1e-2?"""
import sys, pathlib, random, contextlib
from fractions import Fraction as Fr
ROOT = next((q for q in [*pathlib.Path(__file__).resolve().parents, pathlib.Path.cwd()] if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file()))
sys.path.insert(0, str(next((ROOT / "frontier").glob("B1945_*")) / "verification"))
import determinant_law as DL, cusp_mixing as CM
mp = DL.mp; te = DL.FM.te


@contextlib.contextmanager
def const_higgs(h):
    sB, sev = te.B, te.ev
    nB = dict(sB) if isinstance(sB, dict) else list(sB); nB[1] = [0, 1, 2]
    te.B, te.ev = nB, (lambda cc, t: mp.mpc(h[cc]))
    try: yield
    finally: te.B, te.ev = sB, sev


def run(h, y, p):
    with const_higgs(h):
        Yu = DL.parts("0.13", y, p[0], p[1], "up")[2]; Yd = DL.parts("0.13", y, p[0], p[1], "down")[2]
    U, D = CM.U_of(Yu["St"]), CM.U_of(Yd["S"]); V = U.H * D
    sv = lambda M: sorted(float(v) for v in mp.svd_c(M, compute_uv=False))
    su, sd = sv(Yu["St"]), sv(Yd["S"])
    hh = sum(complex(c) ** 2 for c in h); nn = sum(abs(complex(c)) ** 2 for c in h)
    return dict(r=abs(hh) / nn, vll=float(abs(V[0, 0])), diag=min(float(abs(V[k, k])) for k in range(3)),
                u21=su[1] / su[2], u11=su[0] / su[2], d21=sd[1] / sd[2], d11=sd[0] / sd[2])


if __name__ == "__main__":
    rng = random.Random(1964)
    for (y, p) in ((3.0, (Fr(1, 5), Fr(2, 5))), (6.0, (Fr(1, 5), Fr(2, 5))), (3.0, (Fr(3, 7), Fr(1, 7)))):
        rows = []
        for k in range(400):
            # sample r roughly uniformly: h = a + i t b with a, b real orthonormal-ish, plus random complex
            if k % 2 == 0:
                h = [complex(rng.gauss(0, 1), rng.gauss(0, 1)) for _ in range(3)]
            else:
                a = [rng.gauss(0, 1) for _ in range(3)]; b = [rng.gauss(0, 1) for _ in range(3)]
                ab = sum(x * z for x, z in zip(a, b)) / sum(x * x for x in a); b = [z - ab * x for x, z in zip(a, b)]
                na = sum(x * x for x in a) ** 0.5; nb = sum(x * x for x in b) ** 0.5; t = rng.random()
                h = [x / na + 1j * t * z / nb for x, z in zip(a, b)]
            rows.append(run(h, y, p))
        both = [q for q in rows if q["diag"] >= 0.9 and q["u21"] <= 1e-2 and q["d21"] <= 1e-2]
        print("height %.0f point %s,%s: %d triplets; aligned (diag >= 0.9): %d; up m2/m3 <= 1e-2: %d; down m2/m3 <= 1e-2: %d; aligned with both <= 1e-2: %d" % (
            y, p[0], p[1], len(rows), sum(q["diag"] >= 0.9 for q in rows), sum(q["u21"] <= 1e-2 for q in rows), sum(q["d21"] <= 1e-2 for q in rows), len(both)))
        rows.sort(key=lambda q: q["r"])
        for lo, hi in ((0, 0.05), (0.05, 0.2), (0.2, 0.5), (0.5, 0.8), (0.8, 1.01)):
            g = [q for q in rows if lo <= q["r"] < hi]
            if not g: continue
            med = lambda key: sorted(q[key] for q in g)[len(g) // 2]
            print("   r in [%.2f, %.2f): %3d; median |V_ll| %.2e, diag %.2e; median up m2/m3 %.1e, m1/m3 %.1e; down m2/m3 %.1e, m1/m3 %.1e; best (min) max(up, down) m2/m3 among diag >= 0.9: %s" % (
                lo, hi, len(g), med("vll"), med("diag"), med("u21"), med("u11"), med("d21"), med("d11"),
                ("%.1e" % min(max(q["u21"], q["d21"]) for q in g if q["diag"] >= 0.9)) if any(q["diag"] >= 0.9 for q in g) else "none aligned"))
