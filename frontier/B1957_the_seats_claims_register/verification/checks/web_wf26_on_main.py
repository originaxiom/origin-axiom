"""B1957: the web seat's W-F26 (frame C's mixing high in the cusp, in all eight options), on main's own frame.
Data-free: outputs of the frame only; nothing is compared with a measured number.
The mixing |V| = |U_u^dagger U_d| with each sector's left-singular vectors ordered by falling singular value, at the
mark (2/5, 4/5) and the twin (1/5, 2/5), for the up sector's reading (S or S~) and the down sector's; main's frame in
extended precision (B1957's `wb2_stage3_on_main.coupling`, with the canonical end), heights 6, 8 and 12, Re tau = 0, 1/4.
 Z1  the nearest permutation in each option, whether it is the same at both Re tau and at heights 8 and 12, and the
     greatest deviation of |V| from it at heights 8 and 12.
 Z2  where |V| tends to the identity (same readings, at the mark): the exponents F = -(1/pi) d log|V_ij| / d Im tau of
     its off-diagonal entries between heights 8 and 12.
The permutation is printed as the tuple s with |V[i][s[i]]| near 1, index 0 the heaviest state; the seat writes the
inverse, so its (2 0 1) is this script's (1, 2, 0)."""
import sys, pathlib, functools, itertools
from fractions import Fraction as Fr
import mpmath as mp
print = functools.partial(print, flush=True)
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent)); import wb2_stage3_on_main as W
mp.mp.dps = 60


def left_basis(Y):
    U, S, Vh = mp.svd_c(mp.matrix(Y)); order = sorted(range(3), key=lambda i: -S[i]); return mp.matrix([[U[r, c] for c in order] for r in range(3)])
def mixing(tx, ty, a, b, ru, rd):
    Yu = W.coupling(tx, ty, a, b, *W.SIX["up"], False, as_mp=True)[ru]; Yd = W.coupling(tx, ty, a, b, *W.SIX["down"], False, as_mp=True)[rd]
    Uu, Ud = left_basis(Yu), left_basis(Yd); V = Uu.H * Ud; return [[abs(V[i, j]) for j in range(3)] for i in range(3)]
def nearest_perm(V):
    best = max(itertools.permutations(range(3)), key=lambda s: sum(V[i][s[i]] for i in range(3))); P = [[1 if best[i] == j else 0 for j in range(3)] for i in range(3)]
    return best, max(abs(V[i][j] - P[i][j]) for i in range(3) for j in range(3))

if __name__ == "__main__":
    pts = {"mark": (Fr(2, 5), Fr(4, 5)), "twin": (Fr(1, 5), Fr(2, 5))}; store = {}
    for pname, (a, b) in pts.items():
        for ru, rd in (("S", "S"), ("St", "St"), ("S", "St"), ("St", "S")):
            perms = set(); dev = {}
            for ty in (6.0, 8.0, 12.0):
                for tx in ("0.0", "0.25"):
                    V = mixing(tx, ty, a, b, ru, rd); s, d = nearest_perm(V); store[(pname, ru, rd, tx, ty)] = V
                    if ty >= 8: perms.add(s)
                    dev[(tx, ty)] = d
            kind = "identity" if perms == {(0, 1, 2)} else ("cyclic %s" % (sorted(perms)[0],) if len(perms) == 1 else "NOT ONE PERMUTATION %s" % sorted(perms))
            print("Z1 %s, up %s, down %s: %s (the same at Re tau = 0 and 1/4 and at heights 8 and 12: %s); deviation at height 8: %.1e, at height 12: %.1e" % (pname, ru, rd, kind, len(perms) == 1, float(max(dev[("0.0", 8.0)], dev[("0.25", 8.0)])), float(max(dev[("0.0", 12.0)], dev[("0.25", 12.0)]))))
    for ru in ("S", "St"):
        for tx in ("0.0", "0.25"):
            V8, V12 = store[("mark", ru, ru, tx, 8.0)], store[("mark", ru, ru, tx, 12.0)]; F = lambda i, j: float(-(mp.log(V12[i][j]) - mp.log(V8[i][j])) / (mp.pi * 4)) if V12[i][j] > 0 and V8[i][j] > 0 else float("nan")
            G = lambda g, h: F(3 - g, 3 - h)                              # generations numbered from the lightest, as the seat and B1724 do; the code's index 0 is the heaviest
            print("Z2 mark, both sectors in %s, Re tau = %s: exponents between heights 8 and 12 (generations from the lightest): 1-2 %.3f, 2-1 %.3f, 2-3 %.3f, 1-3 %.3f, 3-1 %.3f" % (ru, tx, G(1, 2), G(2, 1), G(2, 3), G(1, 3), G(3, 1)))
