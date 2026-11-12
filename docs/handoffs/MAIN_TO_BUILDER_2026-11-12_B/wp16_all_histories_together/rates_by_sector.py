#!/usr/bin/env python3
"""The owner's test of 2026-11-12, looking forward: selection by rates, with nothing ranked.

THE QUESTION.  Let every move act and let the acts compound.  At level N the moves L and R are two elements of the finite
group G_N = SL(2, Z/N), and the sum over all histories of n moves, in a sector rho (an irreducible representation of
G_N), is (rho(L) + rho(R))^n.  Its size goes like r(rho)^n, where r(rho) is the spectral radius of (rho(L) + rho(R)) / 2.
  r = 1   the sector never cancels;
  r < 1   it cancels, at that rate per move.
Nothing is ranked "least" and no sense of "detect" is chosen: the rates are properties of the two moves alone.

WHAT WOULD REFUTE THE HYPOTHESIS (stated before the run, in main's answer to the owner at 12:58):
  (a) the sectors tie: no rate distinguishes them (equal rates select nothing, as the move count showed in B1868);
  (b) the survivor changes when the set of moves is changed (here: with the inverse moves added, which GENESIS adopts).

WHAT IS COMPUTED, for N = 2 .. 13.
  1. G_N by closure from L and R; its conjugacy classes.
  2. Its character table by Burnside's method (the simultaneous eigenvectors of the class-multiplication matrices), with
     the checks: integer degrees, the squares of the degrees sum to |G_N|, the rows are orthonormal.
  3. For each irreducible character chi: the least level it comes from; its sign on -1; and r(chi) for two sets of moves,
     {L, R} and {L, R, L^-1, R^-1}, from the restriction of the averaged move to chi's part of the group algebra.
CONTROLS: the trivial sector has r = 1 for both sets; the characters of the abelian quotient Z/12 must give
|cos(2 pi k / 12)| for {L, R}; the regular representation's second modulus at level 5 must be B1868's (sqrt 3 / 2, eight
times); a planted group (the same with R replaced by L) must give r = 1 in every sector of the cyclic group it generates.
No measured number is read.  0 of 19."""
import itertools, json, math, pathlib, sys
import numpy as np

HERE = pathlib.Path(__file__).resolve().parent
rng = np.random.default_rng(20261112)


def group(N, gens):
    mul = lambda x, y: ((x[0] * y[0] + x[1] * y[2]) % N, (x[0] * y[1] + x[1] * y[3]) % N, (x[2] * y[0] + x[3] * y[2]) % N, (x[2] * y[1] + x[3] * y[3]) % N)
    one = (1 % N, 0, 0, 1 % N); G = {one: 0}; order = [one]; fr = [one]
    while fr:
        nxt = []
        for x in fr:
            for g in gens:
                y = mul(x, g)
                if y not in G: G[y] = len(order); order.append(y); nxt.append(y)
        fr = nxt
    n = len(order)
    T = np.empty((n, n), dtype=np.int32)                                  # T[i, j] = index of order[i] * order[j]
    for i, x in enumerate(order):
        for j, y in enumerate(order): T[i, j] = G[mul(x, y)]
    inv = np.empty(n, dtype=np.int32)
    for i in range(n): inv[i] = int(np.where(T[i] == 0)[0][0])
    return order, G, T, inv


def classes(T, inv):
    n = len(inv); cls = -np.ones(n, dtype=np.int32); reps = []
    for i in range(n):
        if cls[i] >= 0: continue
        conj = np.unique(T[T[np.arange(n), i], inv])                       # g i g^-1 for every g
        cls[conj] = len(reps); reps.append(i)
    return cls, reps


def character_table(T, inv, cls, reps):
    n, k = len(inv), len(reps); h = np.bincount(cls, minlength=k)
    a = np.zeros((k, k, k))                                                # a[i, j, l] = #{x in C_i, y in C_j : x y = g_l}
    for l, gl in enumerate(reps):
        x = T[gl, inv]                                                     # x = g_l y^-1 for every y
        np.add.at(a[:, :, l], (cls[x], cls), 1)
    for attempt in range(20):
        c = rng.normal(size=k); Mx = np.einsum("j,ijl->il", c, a)
        w, V = np.linalg.eig(Mx)
        if min(abs(w[i] - w[j]) for i in range(k) for j in range(i)) > 1e-6: break
    else:
        raise RuntimeError("the class algebra's eigenvalues would not separate")
    one = cls[0]; chars = []
    for col in range(k):
        v = V[:, col] / V[one, col]
        deg = math.sqrt(n / float(np.sum(np.abs(v) ** 2 / h)))
        chars.append(deg * v / h)
    X = np.array(chars)                                                    # X[chi, class]
    deg = X[:, one].real
    assert np.allclose(deg, np.round(deg), atol=1e-6) and np.allclose(X[:, one].imag, 0, atol=1e-6), "a degree is not an integer"
    assert abs(float(np.sum(np.round(deg) ** 2)) - n) < 1e-6, "the squares of the degrees do not sum to the order"
    gram = (X * h) @ X.conj().T / n
    assert np.allclose(gram, np.eye(k), atol=1e-6), "the rows are not orthonormal"
    return X, h


RETRIES = []


def rate(T, inv, cls, chi, deg, moves):
    """the spectral radius of the averaged move in the sector chi, and the eigenvalue that attains it.

    chi's part of the group algebra is d copies of the sector (d = its dimension).  The eigenvalues of the averaged move
    on the whole part are each d-fold, and the library's eigenvalue routine did not converge on such blocks (first run of
    2026-11-12: one impossible value, then a failure).  So one copy is cut out first: multiplication on the RIGHT commutes
    with the moves, and a random Hermitian combination of right multiplications has d distinct eigenvalues, each on one
    copy.  The averaged move on that copy is a d by d matrix.  Done twice, with independent draws; the two must agree to
    1e-7 and neither may exceed 1 (an average of permutations has norm 1).  A draw that breaks either is counted."""
    n = len(inv); d = int(round(deg)); d2 = d * d; ar = np.arange(n)
    P = (deg / n) * np.conj(chi[cls[T[:, inv]]])                           # P[x, y] = (deg / n) conj(chi(x y^-1))
    assert np.abs(P @ P - P).max() < 1e-8 and np.abs(P - P.conj().T).max() < 1e-8, "chi's part is not a projection"
    A = np.zeros((n, n))
    for m in moves: A[T[m, ar], ar] += 1.0 / len(moves)                    # e_y -> e_{m y}
    def once():
        Y = P @ rng.normal(size=(n, d2 + 4)); Qm, Rm = np.linalg.qr(Y)
        sd = np.abs(np.diag(Rm)); r = int(np.sum(sd > 1e-8 * sd[0])); assert r == d2, ("the part has the wrong dimension", r, d2)
        Qm = Qm[:, :d2]
        if np.abs(Qm.conj().T @ Qm - np.eye(d2)).max() > 1e-10 or np.abs(P @ Qm - Qm).max() > 1e-8: return None
        Rr = np.zeros((n, n), dtype=complex)
        for g in rng.integers(0, n, size=8):
            Rr[T[ar, g], ar] += rng.normal() + 1j * rng.normal()           # e_y -> e_{y g}
        Hr = Qm.conj().T @ (Rr @ Qm); Hr = Hr + Hr.conj().T
        w, V = np.linalg.eigh(Hr)
        top = w[-d:]; gap = (w[-d] - w[-d - 1]) if d2 > d else 1.0
        if top.max() - top.min() > 1e-8 * max(1.0, abs(w).max()) or gap < 1e-6: return None
        W = V[:, -d:]; B = W.conj().T @ (Qm.conj().T @ (A @ (Qm @ W)))
        if not np.all(np.isfinite(B)) or np.linalg.norm(B, 2) > 1 + 1e-9: return None
        leak = np.linalg.norm((Qm.conj().T @ (A @ (Qm @ W))) - W @ B)       # the copy is carried to itself
        if leak > 1e-8: return None
        ev = np.linalg.eigvals(B); t = ev[np.argmax(np.abs(ev))]
        return float(abs(t)), complex(t)
    for attempt in range(8):
        x, y = once(), once()
        if x is not None and y is not None and abs(x[0] - y[0]) < 1e-7 and x[0] <= 1 + 1e-9:
            return x
        RETRIES.append((n, d, len(moves), None if x is None else round(x[0], 9), None if y is None else round(y[0], 9)))
    raise RuntimeError("the two computations of a rate would not agree")


def level_of(N, order, cls, chi, deg):
    for Mdiv in [m for m in range(1, N + 1) if N % m == 0]:
        ker = [i for i, x in enumerate(order) if (x[0] - 1) % Mdiv == 0 and x[1] % Mdiv == 0 and x[2] % Mdiv == 0 and (x[3] - 1) % Mdiv == 0]
        if all(abs(chi[cls[i]] - deg) < 1e-6 for i in ker): return Mdiv
    raise RuntimeError("no level")


def study(N, gens=None, label=None):
    gens = gens or [(1, 1 % N, 0, 1), (1, 0, 1 % N, 1)]
    order, G, T, inv = group(N, [tuple(v % N for v in g) for g in gens])
    cls, reps = classes(T, inv); X, h = character_table(T, inv, cls, reps)
    L, R = G[tuple(v % N for v in gens[0])], G[tuple(v % N for v in gens[1])]
    minus = G.get(((-1) % N, 0, 0, (-1) % N))
    Uix = G.get((0, 1 % N, (-1) % N, (-1) % N))                           # U = S^-1 L, of order 3: L = S U and R = -S U^-1
    rows = []
    for a in range(len(reps)):
        deg = float(round(X[a, cls[0]].real))
        r2, top2 = rate(T, inv, cls, X[a], deg, [L, R]); r4, top4 = rate(T, inv, cls, X[a], deg, [L, R, int(inv[L]), int(inv[R])])
        rows.append({"dimension": int(deg), "level": level_of(N, order, cls, X[a], deg) if label is None else None,
                     "sign on -1": (None if minus is None else int(round((X[a, cls[minus]] / deg).real))),
                     "vectors U fixes": (None if Uix is None else int(round(float((deg + X[a, cls[Uix]] + X[a, cls[inv[Uix]]]).real) / 3))),
                     "rate, moves L and R": round(r2, 9), "top eigenvalue": [round(top2.real, 9), round(top2.imag, 9)],
                     "rate, with the inverse moves": round(r4, 9)})
    return {"N": N, "order": len(order), "classes": len(reps), "sectors": rows, "T": T, "L": L, "R": R, "inv": inv}


if __name__ == "__main__":
    out, checks = {}, []
    def check(name, ok, detail=""):
        checks.append({"check": name, "holds": bool(ok), "detail": str(detail)[:400]})
        print("%s  %s%s" % ("ok  " if ok else "FAIL", name, ("  [%s]" % str(detail)[:300]) if detail else ""), flush=True)

    levels = [int(a) for a in sys.argv[1:]] or list(range(2, 14))
    seen = {}                                                              # (level, dimension, sign, rates) of each new sector
    for N in levels:
        S = study(N)
        new = [r for r in S["sectors"] if r["level"] == N]
        out[str(N)] = {"order": S["order"], "classes": S["classes"], "sectors": S["sectors"]}
        print("\nlevel %d: the group has %d elements and %d sectors, %d of them new at this level" % (N, S["order"], S["classes"], len(new)), flush=True)
        for r in sorted(new, key=lambda r: -r["rate, moves L and R"]):
            print("   dimension %2d  sign %s   rate %.6f   with the inverse moves %.6f" % (r["dimension"], {1: "+", -1: "-", None: " "}[r["sign on -1"]], r["rate, moves L and R"], r["rate, with the inverse moves"]), flush=True)
        if N == 5:
            n = S["order"]; A = np.zeros((n, n))
            for m in (S["L"], S["R"]): A[S["T"][m, np.arange(n)], np.arange(n)] += 0.5
            mod = np.sort(np.abs(np.linalg.eigvals(A)))[::-1]
            second = mod[1]; mult = int(np.sum(np.abs(mod - second) < 1e-7))
            check("control: at level 5 the averaged move on the whole group has second modulus sqrt 3 / 2, eight times, as B1868 has it", abs(second - math.sqrt(3) / 2) < 1e-8 and mult == 8, "%.9f, %d times" % (second, mult))
    allrows = [dict(r, N=int(N)) for N, v in out.items() for r in v["sectors"] if r["level"] == int(N)]
    triv = [r for N, v in out.items() for r in v["sectors"] if r["level"] == 1]
    check("control: the trivial sector never cancels, for both sets of moves", all(abs(r["rate, moves L and R"] - 1) < 1e-8 and abs(r["rate, with the inverse moves"] - 1) < 1e-8 for r in triv), "%d levels" % len(triv))
    one_dim = sorted({(r["N"], r["rate, moves L and R"]) for r in allrows if r["dimension"] == 1})
    want = sorted(round(abs(math.cos(2 * math.pi * k / 12)), 6) for k in range(1, 12))
    got = sorted(round(r["rate, moves L and R"], 6) for r in allrows if r["dimension"] == 1)
    if set(levels) >= {2, 3, 4, 6, 12}:
        check("control: the eleven non-trivial characters of the abelian quotient Z/12 have rates |cos(2 pi k / 12)|", got == want, "%s" % got)
    never = [(r["N"], r["dimension"]) for r in allrows if abs(r["rate, moves L and R"] - 1) < 1e-8]
    check("what never cancels, besides the trivial sector: one sector, of dimension 1, at level 2", never == [(2, 1)], never)
    never4 = [(r["N"], r["dimension"]) for r in allrows if abs(r["rate, with the inverse moves"] - 1) < 1e-8]
    check("the same sector never cancels with the inverse moves added, and no other", never4 == [(2, 1)], never4)
    # the planted group: R replaced by L, so the moves generate a cyclic group and every sector has r = 1
    P = study(5, gens=[(1, 1, 0, 1), (1, 1, 0, 1)], label="planted")
    check("planted: with R replaced by L every sector has rate 1 (the instrument does not manufacture cancelling)", all(abs(r["rate, moves L and R"] - 1) < 1e-8 for r in P["sectors"]), "%d sectors" % len(P["sectors"]))
    check("every rate was computed twice, on two independent bases, and the two agree; none exceeds 1", True, "%d draws thrown away and redone: %s" % (len(RETRIES), RETRIES[:6]))
    res = {"levels": {N: {"order": v["order"], "classes": v["classes"], "sectors": v["sectors"]} for N, v in out.items()}, "checks": checks, "draws thrown away": RETRIES,
           "failing": [c["check"] for c in checks if not c["holds"]]}
    (HERE / "rates_by_sector.json").write_text(json.dumps(res, indent=1) + "\n", encoding="utf-8")
    print("\n%d checks, %d failing" % (len(checks), len(res["failing"])))
