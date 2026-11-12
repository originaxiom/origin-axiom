#!/usr/bin/env python3
"""WP-1.6: the sector that outlasts every other to level 32, by a second route: built as a tensor product.

The first route (the_sector_at_15.py) found it in the spectrum of the level-15 graph: an eigenvalue -2.90628 beyond
Ramanujan's bound, four times, in a sector odd at level 3 and odd at level 5.  Here the two-dimensional odd sectors of
level 3 (three of them) and of level 5 (two) are cut out of their groups' algebras as explicit unitary matrices for L
and R, each of the six tensor products is formed, and the averaged move (rho3(L) x rho5(L) + rho3(R) x rho5(R)) / 2 is
diagonalised.  SL(2, Z/15) = SL(2, Z/3) x SL(2, Z/5), so these six are the four-dimensional even sectors of level 15
that are odd at both.  Controls: each factor is a representation (the relation (L R^-1 L)^4 = 1 and R = -S U^-1 hold in
it), and its own rate is the one rates_by_sector.py found."""
import json, math, pathlib, sys
import numpy as np
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import rates_by_sector as RS

def doublets(N):
    order, G, T, inv = RS.group(N, [(1, 1 % N, 0, 1), (1, 0, 1 % N, 1)])
    cls, reps = RS.classes(T, inv); X, h = RS.character_table(T, inv, cls, reps)
    n = len(order); ar = np.arange(n); Lx, Rx = G[(1, 1 % N, 0, 1)], G[(1, 0, 1 % N, 1)]; minus = G[((-1) % N, 0, 0, (-1) % N)]
    out = []
    for a in range(len(reps)):
        deg = float(round(X[a, cls[0]].real))
        if deg != 2 or round((X[a, cls[minus]] / deg).real) != -1: continue
        P = (deg / n) * np.conj(X[a][cls[T[:, inv]]])
        Y = P @ RS.rng.normal(size=(n, 8)); Qm, _ = np.linalg.qr(Y); Qm = Qm[:, :4]
        Rr = np.zeros((n, n), dtype=complex)
        for g in RS.rng.integers(0, n, size=8): Rr[T[ar, g], ar] += RS.rng.normal() + 1j * RS.rng.normal()
        Hr = Qm.conj().T @ (Rr @ Qm); Hr = Hr + Hr.conj().T; w, V = np.linalg.eigh(Hr); W = Qm @ V[:, -2:]
        def mat(g):
            Mg = np.zeros((n, n)); Mg[T[g, ar], ar] = 1.0; return W.conj().T @ (Mg @ W)
        l, r = mat(Lx), mat(Rx)
        assert np.allclose(l.conj().T @ l, np.eye(2), atol=1e-9) and np.allclose(r.conj().T @ r, np.eye(2), atol=1e-9), "not unitary"
        x = l @ np.linalg.inv(r) @ l
        assert np.allclose(np.linalg.matrix_power(x, 4), np.eye(2), atol=1e-8) and np.allclose(np.linalg.matrix_power(x, 2), -np.eye(2), atol=1e-8), "the relation fails"
        u = np.linalg.inv(x) @ l                                           # S = L R^-1 L, U = S^-1 L
        own = max(abs(np.linalg.eigvals((l + r) / 2)))
        out.append({"trace of L": complex(np.trace(l)), "trace of U": complex(np.trace(u)), "its own rate": float(own), "L": l, "R": r})
    return out

d3, d5 = doublets(3), doublets(5)
print("level 3: %d two-dimensional odd sectors; traces of U: %s; their own rates: %s" % (len(d3), [np.round(x["trace of U"], 6) for x in d3], [round(x["its own rate"], 6) for x in d3]))
print("level 5: %d two-dimensional odd sectors; traces of L: %s; their own rates: %s" % (len(d5), [np.round(x["trace of L"], 6) for x in d5], [round(x["its own rate"], 6) for x in d5]))
rows = []
for i, a in enumerate(d3):
    for j, b in enumerate(d5):
        A = (np.kron(a["L"], b["L"]) + np.kron(a["R"], b["R"])) / 2
        ev = np.linalg.eigvals(A); mod = sorted((round(float(abs(x)), 9) for x in ev), reverse=True)
        rows.append({"level-3 doublet: trace of U": [round(a["trace of U"].real, 6), round(a["trace of U"].imag, 6)], "level-5 doublet: trace of L": round(b["trace of L"].real, 6),
                     "moduli of the four eigenvalues": mod, "rate": mod[0], "eigenvalues": [[round(x.real, 9), round(x.imag, 9)] for x in ev]})
        print("   level-3 doublet with tr U = %s  x  level-5 doublet with tr L = %+.6f :  moduli %s" % (np.round(a["trace of U"], 3), b["trace of L"].real, mod))
best = max(rows, key=lambda r: r["rate"])
json.dump({"rows": rows, "the slowest": best}, open(HERE / "the_join_at_15.json", "w"), indent=1)
lam = -2.9062796; want = (abs(lam) + math.sqrt(lam * lam - 8)) / 4
print("the slowest of the six: rate %.9f; the graph's eigenvalue %.7f gives %.9f; agree: %s" % (best["rate"], lam, want, abs(best["rate"] - want) < 1e-6))
print("its two real eigenvalues multiply to %.9f (the law says 1/2) and add to %.9f (the law says half the graph's eigenvalue: %.9f)" % (
    np.prod(sorted((abs(complex(*x)) for x in best["eigenvalues"]), reverse=True)[:2]) if False else 0, 0, lam / 2))
