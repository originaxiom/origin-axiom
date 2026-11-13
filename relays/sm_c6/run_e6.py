#!/usr/bin/env python3
"""SM-C6 E6 steps 1 and 2: filling descent of the record's sector modules and their count after filling.
Card: relays/cards/SM_C6_E6_filling-descent-and-count.md (pushed first).  Uses B1434/B1438's level presentation and
exact slopes from a checkout of main (first argument).  Data-free.
    python3 run_e6.py MAIN_CHECKOUT [out.json]"""
import sys, io, json, cmath, math, contextlib, pathlib
from fractions import Fraction as Fr
from collections import Counter
import numpy as np
HERE = pathlib.Path(__file__).resolve().parent
MAIN = pathlib.Path(sys.argv[1]).resolve()
sys.path.insert(0, str(MAIN / "frontier" / "B1438_the_slope_law" / "verification"))
with contextlib.redirect_stdout(io.StringIO()):
    import slope_law as SL
LEVELS = [(eps, w, k) for eps in (1, -1) for (w, ks) in (("LR", range(1, 6)), ("LLR", range(1, 5)), ("LLLR", range(1, 4)))
          for k in ks]
X, Y, T = 1, 2, 3


def inv(w): return [-g for g in reversed(w)]


def rank(M, tol=1e-8):
    if M.size == 0: return 0
    s = np.linalg.svd(M, compute_uv=False)
    return int(np.sum(s > tol * max(1.0, s[0])))


class Module:
    def __init__(self, N, Phi, l, a, s_l, split=False):
        z = lambda i: cmath.exp(2j * math.pi * i / N)
        self.al = {X: z(a[0]), Y: z(a[1]), T: 1.0}
        self.ll = {X: z(l[0]), Y: z(l[1]), T: 1.0}
        self.be = {g: self.al[g] / self.ll[g] for g in self.al}
        i, j = l[0], l[1]
        if i % N:
            u = {X: 0.0, Y: 1 / (z(i) - 1)}
        else:
            u = {X: 1 / (1 - z(j)), Y: 0.0}
        self.c = {X: u[X], Y: u[Y], T: complex(s_l)}
        if split: self.c = {g: 0.0 for g in self.c}
        self.R = {g: np.array([[self.al[g], self.c[g] * self.be[g]], [0, self.be[g]]], dtype=complex) for g in (X, Y, T)}
        self.Ri = {g: np.linalg.inv(self.R[g]) for g in (X, Y, T)}

    def rho(self, w):
        M = np.eye(2, dtype=complex)
        for g in w: M = M @ (self.R[g] if g > 0 else self.Ri[-g])
        return M

    def fox(self, r):
        """the 2 x 6 block [d r/dx, d r/dy, d r/dt] evaluated in rho (left action)"""
        D = {g: np.zeros((2, 2), dtype=complex) for g in (X, Y, T)}
        pre = np.eye(2, dtype=complex)
        for g in r:
            if g > 0:
                D[g] += pre; pre = pre @ self.R[g]
            else:
                pre = pre @ self.Ri[-g]; D[-g] -= pre
        return np.hstack([D[X], D[Y], D[T]])

    def h1(self, rels):
        J = np.vstack([self.fox(r) for r in rels])
        z1 = 6 - rank(J)
        B = np.vstack([self.R[g] - np.eye(2) for g in (X, Y, T)])
        return z1 - rank(B)


def main():
    out_path = pathlib.Path(sys.argv[2]) if len(sys.argv) > 2 else HERE / "e6_results.json"
    rows, lev_rows = [], []
    for eps, w, k in LEVELS:
        N, F, S = SL.exact_slopes(eps, w, k)
        ng, rels, mu, lam, tau, A, tors = SL.ac.level(eps, w, k)
        Phi = SL.ic.Phi_of(eps, w, k)
        chars = [c for c in S if c != (0, 0, 0)]
        rat = {c: Fr(S[c].c[0]) for c in chars if not any(S[c].c[1:])}
        sval = {c: complex(sum(float(q) * cmath.exp(2j * math.pi * e / N) for e, q in enumerate(S[c].c))) for c in chars}
        lev = {"state": ("+" if eps > 0 else "-") + w, "level": k, "N": N, "characters": len(chars),
               "rational_slopes": len(rat), "slopes": sorted(set(str(v) for v in rat.values()))}
        check_bad = p1_bad = p2_changed = hom_bad = 0; tested = 0
        for l, r in rat.items():
            a_, b_ = r.numerator, r.denominator
            lamw = [X, Y, -X, -Y]
            gam = [T] * b_ + (inv(lamw) * a_ if a_ > 0 else lamw * (-a_))
            gam_wrong = [T] * (b_ + 1) + (inv(lamw) * a_ if a_ > 0 else lamw * (-a_))
            for al in chars:
                if al == l: continue
                beta = tuple((x - y) % N for x, y in zip(al, l))
                bi = tuple((-x) % N for x in beta)
                n, ns = int(S[al] == S[l]), int(S[bi] == S[l])
                V = Module(N, Phi, l, al, sval[l].real)
                assert abs(sval[l].imag) < 1e-9
                hom_bad += not all(np.allclose(V.rho(rr), np.eye(2), atol=1e-8) for rr in rels)
                desc = np.allclose(V.rho(gam), np.eye(2), atol=1e-8)
                h_M = V.h1(rels)
                expect_M = 1 + int(S[beta] == S[l])
                check_bad += (h_M != expect_M)
                h_fill = V.h1(rels + [gam])
                p1_bad += np.allclose(V.rho(gam_wrong), np.eye(2), atol=1e-8)
                Vs = Module(N, Phi, l, al, sval[l].real, split=True)
                p2_changed += (Vs.h1(rels) != h_M)
                tested += 1
                rows.append({"state": lev["state"], "level": k, "l": l, "alpha": al, "slope": str(r), "gamma": [b_, -a_],
                             "descends": bool(desc), "n": n, "nstar": ns, "h1_M": h_M, "h1_M_expected": expect_M,
                             "h1_filled": h_fill, "count_carries": h_fill == n})
        lev.update({"modules_tested": tested, "not_a_representation": hom_bad, "builtin_check_failures": check_bad, "P1_wrong_slope_descended": int(p1_bad),
                    "P2_split_changed_rank": p2_changed})
        lev_rows.append(lev)
        print(lev, flush=True)
    C = Counter((r["n"], r["nstar"], r["h1_filled"]) for r in rows)
    summary = {"levels": len(lev_rows), "levels_with_rational_slopes": sum(1 for l in lev_rows if l["rational_slopes"]),
               "modules_descending": sum(r["descends"] for r in rows), "modules_tested": len(rows),
               "builtin_check_failures": sum(l["builtin_check_failures"] for l in lev_rows),
               "not_a_representation": sum(l["not_a_representation"] for l in lev_rows),
               "P1_wrong_slope_descended": sum(l["P1_wrong_slope_descended"] for l in lev_rows),
               "P2_split_changed_rank_on": sum(l["P2_split_changed_rank"] for l in lev_rows),
               "census_(n,n*,h1_filled)": {str(k): v for k, v in sorted(C.items())},
               "count_carries": sum(r["count_carries"] for r in rows)}
    summary["outcome"] = ("3" if not rows else "1" if summary["count_carries"] else "2")
    json.dump({"summary": summary, "levels": lev_rows, "rows": rows}, open(out_path, "w"), indent=1)
    print(json.dumps(summary, indent=1))


if __name__ == "__main__":
    main()
