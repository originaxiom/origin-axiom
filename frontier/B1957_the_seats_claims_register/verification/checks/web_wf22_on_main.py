"""B1957: the web seat's W-F22 (B1922's negative half, checked again), the parts main can test on its own code.
Data-free.  gamma = [[2, 1], [1, 1]] acts on a line (a, b) of the torus by (a - b, 2b - a).
 L1  among the 266 lines of order at most 12 (points up to sign): the lines gamma, gamma^2 and gamma^3 fix up to sign.
 L2  gamma and gamma^2 are not in Gamma^0(2); gamma^3 is the identity mod 2.
 O1  main's own B1922 routine (its frame, its three windows of the golden thread): at the own line (2/5, 4/5), at the
     other non-trivial fixed line (1/5, 2/5), and at (1/5, 3/5), which gamma does not fix: the greatest deviation of
     the covariant readings S, S~ after one turn, and of S*.
The seat's figures: own line 3e-10, 1e-9, 8e-5 and S* 2.7, 1.5, 2.7; (1/5, 2/5): 8e-11, 8e-10, 6e-5 and S* 3.2, 1.8, 4.9;
(1/5, 3/5): every reading deviates."""
import sys, pathlib, functools, collections
from fractions import Fraction as Fr
from math import lcm
print = functools.partial(print, flush=True)
ROOT = next(q for q in pathlib.Path(__file__).resolve().parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())

if __name__ == "__main__":
    pts = {(Fr(a, n), Fr(b, n)) for n in range(1, 13) for a in range(n) for b in range(n)}; neg = lambda p: ((-p[0]) % 1, (-p[1]) % 1); lines = {min(p, neg(p)) for p in pts}
    act = lambda p: ((p[0] - p[1]) % 1, (2 * p[1] - p[0]) % 1); order = lambda p: lcm(p[0].denominator, p[1].denominator)
    def fixed(k):
        out = []
        for p in sorted(lines):
            q = p
            for _ in range(k): q = act(q)
            if q in (p, neg(p)): out.append(p)
        return out
    f1, f2, f3 = fixed(1), fixed(2), fixed(3)
    print("L1: %d lines; gamma fixes up to sign %d: %s; gamma^2 fixes %d (by order %s); gamma^3 fixes %d (by order %s)" % (len(lines), len(f1), [(str(p[0]), str(p[1])) for p in f1], len(f2), dict(sorted(collections.Counter(order(p) for p in f2).items())), len(f3), dict(sorted(collections.Counter(order(p) for p in f3).items()))))
    g = [[2, 1], [1, 1]]; mm = lambda A, B: [[sum(A[i][k] * B[k][j] for k in range(2)) for j in range(2)] for i in range(2)]; g2 = mm(g, g); g3 = mm(g2, g)
    print("L2: upper-right entries of gamma, gamma^2, gamma^3: %d, %d, %d (Gamma^0(2) needs an even one); gamma^3 = %s is the identity mod 2: %s" % (g[0][1], g2[0][1], g3[0][1], g3, all((g3[i][j] - int(i == j)) % 2 == 0 for i in range(2) for j in range(2))))
    sys.path.insert(0, str(next((ROOT / "frontier").glob("B1922_*")) / "verification")); import periodic as P
    for name, line in (("the own line (2/5, 4/5)", (0.4, 0.8)), ("the line (1/5, 2/5), fixed up to sign", (0.2, 0.4)), ("the line (1/5, 3/5), not fixed", (0.2, 0.6))):
        rows = [P.deviations(s0, line) for s0 in (-P.ell / 2, -P.ell / 2 + 0.15, 0.0)]
        print("O1 %s: S, S~ after one turn: %s; S*: %s (heights %s)" % (name, ", ".join("%.1e" % r["S, St"] for r in rows), ", ".join("%.1f" % r["S*"] for r in rows), ", ".join("%.3f->%.3f" % (r["Im tau"], r["Im gamma tau"]) for r in rows)))
