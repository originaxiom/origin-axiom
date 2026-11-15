"""B1946 (main, 2026-11-15; data-free): frame C's mixing at the 24 points of order 5 at heights 6 and 30 for all four pairings of
the Higgs reading (up, down) in (S, S~)^2; and |U(S)^H U(S~)| per sector (agy-exp's X-WALL, recomputed on main's code)."""
import sys, pathlib
ROOT = next(q for q in pathlib.Path(__file__).resolve().parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
sys.path.insert(0, str(next((ROOT / "frontier").glob("B1945_*")) / "verification"))
import determinant_law as DL, cusp_mixing as CM
from fractions import Fraction as Fr
mp = DL.mp
def pair_stats(y, pts=None):
    res = {}
    for (a, b) in (pts or [(Fr(i, 5), Fr(j, 5)) for i in range(5) for j in range(5) if (i, j) != (0, 0)]):
        _, _, Yu, *_ = DL.parts("0.13", y, a, b, "up"); _, _, Yd, *_ = DL.parts("0.13", y, a, b, "down")
        U = {(sec, r): CM.U_of(Y[r]) for sec, Y in (("up", Yu), ("down", Yd)) for r in ("S", "St")}
        for ru, rd in (("S", "S"), ("St", "St"), ("St", "S"), ("S", "St")):
            Vm = U[("up", ru)].H * U[("down", rd)]
            res.setdefault((ru, rd), []).append((min(float(abs(Vm[k, k])) for k in range(3)), max(float(abs(Vm[r, c])) for r in range(3) for c in range(3) if r != c)))
    return res


if __name__ == "__main__":
  for y in (6.0, 30.0):
      res = {}
      for i in range(5):
          for j in range(5):
              if (i, j) == (0, 0): continue
              a, b = Fr(i, 5), Fr(j, 5)
              _, _, Yu, *_ = DL.parts("0.13", y, a, b, "up"); _, _, Yd, *_ = DL.parts("0.13", y, a, b, "down")
              U = {(sec, r): CM.U_of(Y[r]) for sec, Y in (("up", Yu), ("down", Yd)) for r in ("S", "St")}
              for ru, rd in (("S", "S"), ("St", "St"), ("St", "S"), ("S", "St")):
                  V = U[("up", ru)].H * U[("down", rd)]
                  d = min(float(abs(V[k, k])) for k in range(3)); o = max(float(abs(V[r, c])) for r in range(3) for c in range(3) if r != c)
                  res.setdefault((ru, rd), []).append((d, o))
              # the shift: is U(S~) = C U(S) up to phases? |U(S)^H U(S~)| for each sector
              for sec in ("up", "down"):
                  W = U[(sec, "S")].H * U[(sec, "St")]
                  A = [[round(float(abs(W[r, c])), 3) for c in range(3)] for r in range(3)]
                  res.setdefault(("shift", sec), []).append(tuple(map(tuple, A)))
      print("height %s:" % y)
      for k in (("S", "S"), ("St", "St"), ("St", "S"), ("S", "St")):
          v = res[k]; print("  up %-2s down %-2s: smallest diagonal |V| %.2e, largest off-diagonal %.2e" % (k[0], k[1], min(t[0] for t in v), max(t[1] for t in v)))
      for sec in ("up", "down"):
          from collections import Counter
          print("  |U(S)^H U(S~)| in %s, its patterns:" % sec, Counter(res[("shift", sec)]).most_common(3))
