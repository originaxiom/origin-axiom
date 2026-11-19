"""B1962 (P-861; main, 2026-11-19; data-free): frame D1's cusp mixing, computed as frame C at shifted charges.

The web seat's W-B2 stage 3 (harvest row 1842), in agreement with main's hand reduction (P-861's note of 2026-11-15): the only
modular-covariant place for the Higgs's twist is its own Szego zero, and there frame D1's residue is frame C's at shifted
charges q' = q - c q_H / 2, with q_H = -(q_L + q_R).  c = -2 gives frame C again (up to the sign of every charge); c = +2
gives up (-2, -7), down (4, 5), leptons (0, 9) in 6Y.  This instrument runs frame C's own code (B1945's determinant_law,
B1946's cusp_mixing, B1940's frame, unchanged) with those charges entered as three extra sectors of B1656's tables.

HYPOTHESIS (stated, not tested here): identity E, D1 = frame C at shifted charges, is shown at the residues; that it holds for
the norms too is assumed, and is P-861's owed item.

CELLS (each printed; the classification, expectations and priors are in ../CARD.md, sealed before the run):
 M0  control, c = 0 (frame C's own charges): must reproduce B1946's table to its printed digits, or the run is void.
 M1  c = +2, M3  c = -2: at the 24 points of order 5, heights 6 and 30, for the four reading pairs (up, down) in {S, S~}^2:
     the smallest diagonal |V| and the largest off-diagonal |V| of V = U_up^H U_down (B1946's measure).
 M2  each c: does the lepton sector copy the down sector, plainly or transposed?  Per reading, the largest distance of
     |U_lep^H U_down| and of |U_lep^H U(Y_down^T)| from a 0/1 pattern, and the largest difference of the normalised
     singular values (s/s_max) of Y_lep and Y_down, over the 24 points.
    python3 -B d1_mixing.py > d1_mixing_run.txt"""
import sys, pathlib
from fractions import Fraction as Fr
ROOT = next(q for q in pathlib.Path(__file__).resolve().parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
sys.path.insert(0, str(next((ROOT / "frontier").glob("B1945_*")) / "verification"))
import determinant_law as DL, cusp_mixing as CM
B = DL.FM.B
QH = {"up": 3, "down": -3, "lep": -3}
BASE = {"up": ("Q", "u"), "down": ("Q", "d"), "lep": ("L", "e")}


def install(c):
    """the three sectors at shifted charges q' = q - c q_H / 2, under new names; returns the names"""
    names = {}
    for sec, (fl, fr) in BASE.items():
        ql, qr = B.SIXY[fl], B.SIXY[fr]; s = Fr(c, 2) * QH[sec]
        nl, nr = "%s_c%+d_%s" % (fl, c, sec), "%s_c%+d_%s" % (fr, c, sec)
        B.SIXY[nl], B.SIXY[nr] = int(ql - s), int(qr - s)
        name = "%s_c%+d" % (sec, c); B.SECTORS[name] = (nl, nr); names[sec] = name
    return names


POINTS = [(Fr(i, 5), Fr(j, 5)) for i in range(5) for j in range(5) if (i, j) != (0, 0)]
PAIRS = (("S", "S"), ("St", "St"), ("St", "S"), ("S", "St"))


def table(names, y):
    res = {}; lep = {}
    for (a, b) in POINTS:
        Y = {sec: DL.parts("0.13", y, a, b, names[sec])[2] for sec in ("up", "down", "lep")}
        U = {(sec, r): CM.U_of(Y[sec][r]) for sec in ("up", "down", "lep") for r in ("S", "St")}
        for ru, rd in PAIRS:
            V = U[("up", ru)].H * U[("down", rd)]
            res.setdefault((ru, rd), []).append((min(float(abs(V[k, k])) for k in range(3)), max(float(abs(V[r, c])) for r in range(3) for c in range(3) if r != c)))
        for r in ("S", "St"):
            pat = lambda W: max(min(abs(float(abs(W[i, j])) - 1), float(abs(W[i, j]))) for i in range(3) for j in range(3))
            plain = pat(U[("lep", r)].H * U[("down", r)]); trans = pat(U[("lep", r)].H * CM.U_of(Y["down"][r].T))
            sv = lambda M: sorted(float(v) for v in DL.mp.svd_c(M, compute_uv=False))
            sl, sd = sv(Y["lep"][r]), sv(Y["down"][r]); spec = max(abs(sl[k] / sl[2] - sd[k] / sd[2]) for k in range(3))
            lep.setdefault(r, []).append((plain, trans, spec))
    return res, lep


def card_is_sealed():
    import subprocess
    here = pathlib.Path(__file__).resolve().parent.parent / "CARD.md"
    tracked = subprocess.run(["git", "ls-files", "--error-unmatch", str(here)], cwd=ROOT, capture_output=True).returncode == 0
    clean = subprocess.run(["git", "diff", "--quiet", "HEAD", "--", str(here)], cwd=ROOT).returncode == 0
    return tracked and clean


if __name__ == "__main__":
    if not card_is_sealed():
        sys.exit("CARD.md is not committed unchanged: the run refuses (the card is sealed before any output)")
    for c in (0, -2, 2):
        names = install(c) if c else {"up": "up", "down": "down", "lep": "lep"}
        print("c = %+d: charges %s" % (c, {s: (B.SIXY[B.SECTORS[n][0]], B.SIXY[B.SECTORS[n][1]]) for s, n in names.items()}))
        for y in (6.0, 30.0):
            res, lep = table(names, y)
            for k in PAIRS:
                v = res[k]; print("  height %4.1f  up %-2s down %-2s: smallest diagonal |V| %.3e, largest off-diagonal %.3e" % (y, k[0], k[1], min(t[0] for t in v), max(t[1] for t in v)))
            for r in ("S", "St"):
                v = lep[r]; print("  height %4.1f  leptons against down, reading %-2s: |U_lep^H U_down| from a 0/1 pattern %.3e; against Y_down^T %.3e; normalised singular values differ by %.3e" % (y, r, max(t[0] for t in v), max(t[1] for t in v), max(t[2] for t in v)))
