#!/usr/bin/env python3
"""B1455, post-seal -- is the counted configuration W1 itself fixed by a bare mirror?

W1 is not semisimple, so characters do not decide conjugacy; intertwiners do.  For each symmetry sigma: the space of
X with X (sigma^* W1)(g) = T(g) X, g = m, n, for T = W1 at q0, W1 at 1/q0, and their duals; conjugate iff it contains
an invertible X.  60 digits; the singular-value gap is reported.

    python3 mirror_fixes_the_counted_one.py     # prints, writes mirror_fixes_the_counted_one.json
"""
import json, sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import followup_index as FI
J = FI.J
from mpmath import mp, mpf, mpc, sqrt, matrix, zeros, svd_c, det, nstr, inverse


def W1(q, mu):
    g = J.ballas(q, mu); reps, z, rb = J.cocycles(g)
    c = {"m": matrix([reps[0][i] for i in range(4)]), "n": matrix([reps[0][4 + i] for i in range(4)])}
    return J.ext(g, c)


def intertwiners(R1, R2):
    """X with X R1(g) = R2(g) X for g = m, n: (dimension, |det| of a basis element or of a generic combination, gap)"""
    n = R1["m"].rows; rows = []
    for g in "mn":
        A, B = R1[g], R2[g]
        for i in range(n):
            for j in range(n):
                r = [mpc(0)] * (n * n)
                for k in range(n):
                    r[i * n + k] += A[k, j]          # (X A)_ij = sum_k X_ik A_kj
                    r[k * n + j] -= B[i, k]          # (B X)_ij = sum_k B_ik X_kj
                rows.append(r)
    M = matrix(len(rows), n * n)
    for a, r in enumerate(rows):
        for b, v in enumerate(r): M[a, b] = v
    U, S, Vh = svd_c(M, full_matrices=True)
    s = sorted(abs(S[i]) for i in range(len(S)))
    tol = mpf(10) ** (-30); dim = sum(1 for v in s if v < tol * max(1, s[-1]))
    kept = min((v for v in s if v >= tol * max(1, s[-1])), default=None); dropped = max((v for v in s if v < tol * max(1, s[-1])), default=None)
    best = mpf(0)
    for k in range(dim):
        v = Vh[n * n - 1 - k, :].H
        X = matrix(n, n)
        for i in range(n):
            for j in range(n): X[i, j] = v[i * n + j]
        best = max(best, abs(det(X)))
    return dim, best, (kept, dropped)


def main():
    s2 = sqrt(mpf(2)); q0, q1 = 17 + 12 * s2, 17 - 12 * s2
    W, Wp = W1(q0, mpc(-1)), W1(q1, mpc(-1))
    targets = {"W1(q0)": W, "W1(q0)*": J.dualrep(W), "W1(1/q0)": Wp, "W1(1/q0)*": J.dualrep(Wp)}
    out = {}
    for name, (x, y) in list(FI.SIGMAS.items()) + [("identity", ("m", "n"))]:
        P = FI.pull(W, x, y); row = {}
        for tn, T in targets.items():
            dim, d, (kept, dropped) = intertwiners(P, T)
            row[tn] = dict(dim=dim, conjugate=bool(dim >= 1 and d > mpf(10) ** (-20)), det=nstr(d, 5), smallest_kept=nstr(kept, 5), largest_dropped=nstr(dropped, 5) if dropped is not None else None)
        out[name] = row
        print("%-42s conjugate to: %s" % (name, [t for t, r in row.items() if r["conjugate"]]), "  dims", {t: r["dim"] for t, r in row.items()})
    json.dump(out, open(HERE / "mirror_fixes_the_counted_one.json", "w"), indent=1)


if __name__ == "__main__":
    main()
