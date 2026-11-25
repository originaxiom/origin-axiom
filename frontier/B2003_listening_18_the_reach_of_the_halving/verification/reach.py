"""B2003, listening card 18 (main, 2026-11-25; data-free): the reach of B2002's halving identity. The symmetric six-move
covariant unfolding on the orbit of (3,3,3) at mod 9, 27, 81, 243, 25, 49, 15, 45: C-fixed points; the multiplicity-aware
pairing of neutral modes mu (below the top) with charged modes mu/2; the identity p_n(2x) = 2^d (x^2 - 9) x S(x), exactly
(FLINT) up to 1,500 points, numerically (eigvalsh, 1e-8) above.
    python3 -B reach.py > reach_run.txt"""
import pathlib, time
import numpy as np, flint
from scipy.sparse import csr_matrix
HERE = pathlib.Path(__file__).resolve().parent
src = (HERE.parent.parent / "B2002_listening_17_the_halving_at_the_wholes_prime_exactly" / "verification" / "halving.py").read_text().split("summary = {}")[0]
ns = {"__file__": str(HERE / "reach.py")}; exec(compile(src, "b2002_head", "exec"), ns)
t0 = time.time()
def structure(N):
    pts, moves, C = ns["leaf"](N, (3, 3, 3)); idx = {v: i for i, v in enumerate(pts)}; n = len(pts)
    fixed = [v for v in pts if C(v) == v]
    return pts, moves, C, idx, n, fixed
def exact(N):
    n, k, sym, pQ, pC = ns["polys"](N, (3, 3, 3))
    c, fs = pC.factor(); sq = all(e % 2 == 0 for _, e in fs)
    S = flint.fmpz_poly([1])
    for f, e in fs: S = S * f ** (e // 2)
    d = pQ.degree()
    lhs = flint.fmpz_poly([int(cf) * 2 ** i for i, cf in enumerate(pQ.coeffs())])
    ident = lhs == flint.fmpz_poly([0, -9, 0, 1]) * S * (2 ** d)
    paired, total = 0, 0
    cQ, fQ = pQ.factor()
    for f, e in fQ:
        rts = np.roots([int(x) for x in reversed(f.coeffs())]) if f.degree() > 0 else []
        if any(abs(abs(r) - 6) < 1e-9 for r in rts): continue
        total += f.degree() * e
        g = ns["halved"](f); m = 0; q = S
        while g.degree() > 0 and (q % g) == 0: q = q // g; m += 1
        paired += f.degree() * min(e, m)
    return n, k, sq, ident, paired, total, S.degree()
def numeric(N):
    pts, moves, C, idx, n, fixed = structure(N)
    rows, cols = [], []
    for v in pts:
        for m in moves: rows.append(idx[m(v)]); cols.append(idx[v])
    W = csr_matrix((np.ones(len(rows)), (rows, cols)), shape=(n, n))
    Cp = np.array([idx[C(v)] for v in pts])
    seen, cyc, fx = set(), [], []
    for i in range(n):
        if i in seen: continue
        j, k = Cp[i], Cp[Cp[i]]
        if j == i: fx.append(i); seen.add(i)
        else: cyc.append((i, j, k)); seen.update((i, j, k))
    w = np.exp(2j * np.pi / 3); spec = {}
    for q in (0, 1):
        B = np.zeros((n, len(cyc) + (len(fx) if q == 0 else 0)), complex)
        for c, (i, j, k) in enumerate(cyc): B[i, c], B[j, c], B[k, c] = 1 / np.sqrt(3), w ** (-q) / np.sqrt(3), w ** (-2 * q) / np.sqrt(3)
        if q == 0:
            for c, i in enumerate(fx): B[i, len(cyc) + c] = 1
        M = B.conj().T @ (W @ B); spec[q] = np.sort(np.linalg.eigvalsh((M + M.conj().T) / 2))
    neu = list(spec[0]); top = [x for x in neu if abs(abs(x) - 6) < 1e-8]
    for x in top: neu.remove(x)
    ch = list(spec[1])
    # multiplicity-aware matching of mu/2 against charged values
    half = sorted(x / 2 for x in neu); i = j = paired = 0
    chs = sorted(ch)
    while i < len(half) and j < len(chs):
        if abs(half[i] - chs[j]) < 1e-8: paired += 1; i += 1; j += 1
        elif half[i] < chs[j]: i += 1
        else: j += 1
    # identity: charged == half of (neutral minus the top ones and one zero)
    neu2 = list(neu); z = min(range(len(neu2)), key=lambda t: abs(neu2[t])); zero_removed = abs(neu2[z]) < 1e-8
    if zero_removed: neu2.pop(z)
    ident = zero_removed and len(neu2) == len(chs) and np.max(np.abs(np.sort(np.array(neu2) / 2) - np.array(chs))) < 1e-8
    return n, len(fx), ident, paired, len(neu), len(chs)
for N in (9, 27, 81, 243, 25, 49, 15, 45):
    pts, moves, C, idx, n, fixed = structure(N)
    if n <= 1500:
        n, k, sq, ident, paired, total, dS = exact(N)
        print("mod %3d: orbit %5d points, C-fixed %d; EXACT: charged polynomial a square %s; identity p_n(2x) = 2^d (x^2-9) x S(x): %s; neutral non-top degree %d, paired by halving (multiplicity-aware) %d; charged-sector degree %d  [%.0f s]" % (
            N, n, len(fixed), sq, ident, total, paired, dS, time.time() - t0), flush=True)
    else:
        n, nf, ident, paired, nn, nc = numeric(N)
        print("mod %3d: orbit %5d points, C-fixed %d; NUMERIC (eigvalsh, 1e-8): identity (charged = half of neutral minus +-6 and one 0): %s; neutral non-top modes %d, paired by halving %d; charged-sector dimension %d  [%.0f s]" % (
            N, n, nf, ident, nn, paired, nc, time.time() - t0), flush=True)
