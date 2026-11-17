"""Added 2026-11-17: the web seat's W-A1 (H1, H3; harvest row 1846) on main's frame code.  At tau = i the two Higgs readings
give the same coupling at points of order 5 (the triplet's third component vanishes there); at control points they differ."""
import pathlib, sys
from fractions import Fraction as Fr
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "B1945_the_frames_cusp_exponents" / "verification"))
import determinant_law as DL
PTS = ((1, 3), (2, 1), (0, 3), (4, 4))


def diff(tx, ty, a, b, sec):
    Ys = DL.parts(tx, ty, a, b, sec)[2]
    return float(max(abs(x) for x in (Ys["S"] - Ys["St"])) / max(abs(x) for x in Ys["S"]))


if __name__ == "__main__":
    for tx, ty, name in (("0", 1.0, "tau = i"), ("0", 1.3, "tau = 1.3i (control)"), ("0.05", 0.9, "tau = 0.05 + 0.9i (control)")):
        for sec in ("up", "down"):
            d = [diff(tx, ty, Fr(a, 5), Fr(b, 5), sec) for a, b in PTS]
            print("%-28s %-4s: max |Y(S) - Y(S~)| / max |Y(S)| at four points of order 5: %s" % (name, sec, " ".join("%.1e" % x for x in d)), flush=True)
