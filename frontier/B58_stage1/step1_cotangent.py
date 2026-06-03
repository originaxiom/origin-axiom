"""B58 Stage 1, Step 1 -- cotangent spectrum of the metallic trace map at the trivial rep.

sigma: (X,Y) -> (mX+Y, X) = M=[[m,1],[1,0]] on the deformations X,Y in sl(n). At m=1,
sigma(X,Y)=(X+Y, X). The trace algebra of two generic sl(n) matrices, graded by degree;
the COTANGENT spectrum = eigenvalues of d(sigma) on m/m^2 (minimal generators). This is
LARGER than the (n^2-1) Jacobian spectrum for n>=4 by the "excess"; we compute the cotangent
exactly over F_p (modular -> no rational blow-up), then SUBTRACT the known tower to read the
excess. Prime-stability over 3 primes (mirrors B66 seed-stability). Writes
cotangent_spectrum.json. No commit.

Method per degree d: V_single_d = single trace-words tr(w), |w|=d; m^2_d = products of lower
invariants; (m/m^2)_d = V_single_d mod m^2_d; sigma acts -> charpoly mod p -> tag char(+-M^k)/parity.
"""

import json
import time
from pathlib import Path

import numpy as np
import sympy as sp

OUT = Path(__file__).resolve().parent / "cotangent_spectrum.json"
t = sp.symbols("t")

KNOWN_TOWER = {  # the (n^2-1) Jacobian factorization (the a_d/b_d object) -- to subtract
    3: {"char(M^-1)": 1, "char(M^2)": 1, "char(M^3)": 1, "(t-1)": 1, "(t+1)": 1},
    4: {"char(M^-1)": 1, "char(M^1)": 1, "char(M^2)": 1, "char(M^3)": 1, "char(M^4)": 1,
        "char(-M^2)": 1, "(t-1)": 2, "(t+1)": 1},
    5: {"char(M^-1)": 1, "char(M^1)": 2, "char(M^2)": 2, "char(M^3)": 1, "char(M^4)": 1,
        "char(M^5)": 1, "char(-M^2)": 1, "char(-M^3)": 1, "(t-1)": 2, "(t+1)": 2},
}


# --------------------------------------------------------------------------- #
# modular linear algebra (F_p)
# --------------------------------------------------------------------------- #

def rref(A, p):
    A = (np.asarray(A, dtype=np.int64) % p).copy()
    rows, cols = A.shape
    r = 0
    piv = []
    for c in range(cols):
        if r >= rows:
            break
        nz = np.nonzero(A[r:, c])[0]
        if nz.size == 0:
            continue
        pr = r + int(nz[0])
        if pr != r:
            A[[r, pr]] = A[[pr, r]]
        inv = pow(int(A[r, c]), p - 2, p)
        A[r] = (A[r] * inv) % p
        factors = A[:, c].copy()
        factors[r] = 0
        A = (A - np.outer(factors, A[r])) % p      # int64: |factors*A[r]| < p^2 < 4e12
        piv.append(c)
        r += 1
    return A, piv


def rank(A, p):
    A = np.asarray(A, dtype=np.int64)
    if A.size == 0 or 0 in A.shape:
        return 0
    return len(rref(A, p)[1])


def indep_of(B, v, p):
    """is v linearly independent of the columns of B (mod p)?"""
    if B.shape[1] == 0:
        return any(int(x) % p != 0 for x in v)
    return rank(np.hstack([B, v.reshape(-1, 1)]), p) > rank(B, p)


def solve(A, b, p):
    """one solution z to A z = b (mod p), or None."""
    A = np.asarray(A, dtype=np.int64) % p
    b = (np.asarray(b, dtype=np.int64) % p).reshape(-1, 1)
    ncols = A.shape[1]
    R, piv = rref(np.hstack([A, b]), p)
    for i in range(R.shape[0]):
        if not R[i, :ncols].any() and R[i, ncols] != 0:
            return None
    z = np.zeros(ncols, dtype=np.int64)
    for i, c in enumerate(piv):
        if c < ncols:
            z[c] = R[i, ncols] % p
    return z


# --------------------------------------------------------------------------- #
# words, samples, value-vectors over F_p
# --------------------------------------------------------------------------- #

def samples(n, K, p, seed):
    rng = np.random.default_rng(seed)
    def sl():
        Z = rng.integers(0, p, size=(K, n, n)).astype(np.int64)
        diagsum = Z[:, np.arange(n - 1), np.arange(n - 1)].sum(axis=1)
        Z[:, n - 1, n - 1] = (-diagsum) % p       # traceless
        return Z % p
    return sl(), sl()


def matmul_mod(A, B, p):                          # batched (K,n,n) int64; |entries|<p^2*n < 2.4e13
    return (np.matmul(A, B)) % p


def trace_mod(A, p):
    return np.trace(A, axis1=1, axis2=2) % p


def lucas(k, m=1):
    M = sp.Matrix([[m, 1], [1, 0]])
    return int((M ** k).trace()) if k >= 0 else int((M.inv() ** (-k)).trace())


def tag_charpoly(C, p, kmax):
    """charpoly(C) mod p, divide out catalog factors char(+-M^k)/parity; return {label:mult}, remainder-ok."""
    cp = sp.Poly(sp.Matrix(C.tolist()).charpoly(t).as_expr(), t, modulus=p)
    order = ([("char(M^-1)", (t ** 2 + t - 1))]
             + [(f"char(M^{k})", t ** 2 - lucas(k) * t + (-1) ** (k % 2)) for k in range(1, kmax + 1)]
             + [(f"char(-M^{k})", t ** 2 + lucas(k) * t + (-1) ** (k % 2)) for k in range(1, kmax + 1)]
             + [("(t-1)", t - 1), ("(t+1)", t + 1)])
    out = {}
    for lab, g in order:
        gP = sp.Poly(g, t, modulus=p)
        e = 0
        while True:
            q, r = cp.div(gP)
            if r.is_zero:
                cp = q
                e += 1
            else:
                break
        if e:
            out[lab] = out.get(lab, 0) + e
    return out, (cp.degree() <= 0)


def words_of_len(d):
    return [tuple((i >> b) & 1 for b in range(d)) for i in range(2 ** d)]


def cotangent_spectrum(n, p, seed, K, Lmax=12, verbose=False):
    X, Y = samples(n, K, p, seed)
    Xs, Ys = (X + Y) % p, X                       # sigma-images at m=1
    # value-vectors by degree; matrices for current degree (orig + sigma)
    val = {}          # (degree) -> {word: vec(K)}   single-trace value-vectors
    val_s = {}        # sigma value-vectors
    mats = {1: {(0,): X, (1,): Y}}
    mats_s = {1: {(0,): Xs, (1,): Ys}}
    val[1] = {(0,): trace_mod(X, p), (1,): trace_mod(Y, p)}
    val_s[1] = {(0,): trace_mod(Xs, p), (1,): trace_mod(Ys, p)}

    Mbasis = {}       # degree -> basis matrix (K x dim m_e) of the graded invariant piece
    spectrum = {}     # degree -> {label: mult}
    gens_total = 0
    stale = 0
    for d in range(2, Lmax + 1):
        # extend matrices to degree d
        mats[d] = {}
        mats_s[d] = {}
        val[d] = {}
        val_s[d] = {}
        for w, Mw in mats[d - 1].items():
            for letter, L in ((0, X), (1, Y)):
                nw = w + (letter,)
                mats[d][nw] = matmul_mod(Mw, L, p)
                val[d][nw] = trace_mod(mats[d][nw], p)
        for w, Mw in mats_s[d - 1].items():
            for letter, L in ((0, Xs), (1, Ys)):
                nw = w + (letter,)
                mats_s[d][nw] = matmul_mod(Mw, L, p)
                val_s[d][nw] = trace_mod(mats_s[d][nw], p)
        del mats[d - 1]
        del mats_s[d - 1]

        # products m^2_d = span of M_e (x) M_{d-e}, 2<=e<=d-2
        prod_cols = []
        for e in range(2, d - 1):
            if e in Mbasis and (d - e) in Mbasis:
                Be, Bf = Mbasis[e], Mbasis[d - e]
                for a in range(Be.shape[1]):
                    for b in range(Bf.shape[1]):
                        prod_cols.append((Be[:, a] * Bf[:, b]) % p)
        Pmat = np.array(prod_cols, dtype=np.int64).T % p if prod_cols else np.zeros((K, 0), dtype=np.int64)

        # single traces of degree d
        sing_words = list(val[d].keys())
        Smat = np.array([val[d][w] for w in sing_words], dtype=np.int64).T % p

        # ONE rref of [products | singles]: pivots in the singles block = generators
        # (independent of products + earlier singles); all pivots = basis of m_d.
        nprod = Pmat.shape[1]
        allcols = np.hstack([Pmat, Smat]) if Smat.shape[1] else Pmat
        _, piv = rref(allcols, p)
        Mbasis[d] = allcols[:, piv] if piv else np.zeros((K, 0), dtype=np.int64)
        gen_words = [sing_words[c - nprod] for c in piv if c >= nprod]

        if not gen_words:
            stale += 1
            if stale >= 3 and d > n + 2:
                break
            continue
        stale = 0
        gens_total += len(gen_words)

        # sigma matrix on generators: v_s(w_a) = sum c_ab v(w_b) mod products
        G = np.array([val[d][w] for w in gen_words], dtype=np.int64).T % p   # K x r
        GP = np.hstack([G, Pmat]) if Pmat.shape[1] else G
        r = len(gen_words)
        C = np.zeros((r, r), dtype=np.int64)
        ok = True
        for a, wa in enumerate(gen_words):
            z = solve(GP, val_s[d][wa], p)
            if z is None:
                ok = False
                break
            C[:, a] = z[:r] % p
        if not ok:
            spectrum[d] = {"ERROR": "sigma solve failed"}
            continue
        kmax = 2 * n
        tags, remok = tag_charpoly(C, p, kmax)
        if not remok:
            tags["UNTAGGED_REMAINDER"] = 1
        spectrum[d] = tags
        if verbose:
            print(f"   deg {d}: {len(gen_words)} gens -> {tags}")
    return spectrum, gens_total


def merge(specs):
    tot = {}
    for s in specs.values():
        for lab, m in s.items():
            tot[lab] = tot.get(lab, 0) + m
    return tot


DJOKOVIC_TRACELESS = {3: 9, 4: 30, 5: None}   # Teranishi/Djokovic minimal generators of two TRACELESS nxn matrices


def main():
    res = {"job": "B58_stage1_step1_cotangent", "m": 1,
           "note": ("COTANGENT spectrum (m/m^2) of the two-(traceless-)matrix trace algebra, labeled as "
                    "such -- NOT a_d for n>=4 (inflated by excess). Validated against Teranishi (n=3: 9) and "
                    "Djokovic (n=4: 30)."),
           "BRIEF_FORMULA_DISCREPANCY": ("Brief's 3n^2-10n+11 (=8,19,36) and excess 2(n-2)(n-3) (=0,4,12) are "
                                         "REFUTED: actual cotangent = Teranishi/Djokovic minimal-generator count "
                                         "(9, 30, ...), excess = cotangent - (n^2-1) Jacobian = 1, 15, ... -- much "
                                         "larger and mixed. Flagged per hygiene item (Djokovic cross-check)."),
           "results": {}}
    # per-n: (K, Lmax, primes, partial?)  -- n=4 needs K>=600 to reach deg-10 gen; n=5 best-effort/PARTIAL
    cfg = {3: (96, 8, [2000003, 2000029, 2000039], False),
           4: (600, 11, [2000003, 2000029, 2000039], False),
           5: (1100, 11, [2000003], True)}
    for n in (3, 4, 5):
        K, Lmax, primes, partial = cfg[n]
        per_prime = []
        spec0 = None
        t0 = time.time()
        for pi, p in enumerate(primes):
            spec, gens = cotangent_spectrum(n, p, seed=20 + pi, K=K, Lmax=Lmax, verbose=(pi == 0))
            per_prime.append(merge(spec))
            if pi == 0:
                spec0 = spec
        stable = all(per_prime[0] == per_prime[j] for j in range(1, len(per_prime))) if len(per_prime) > 1 else None
        cot = per_prime[0]
        cotdim = sum((2 if ("M" in k) else 1) * v for k, v in cot.items())
        tower = KNOWN_TOWER[n]
        excess = {}
        for lab, m in cot.items():
            if m - tower.get(lab, 0):
                excess[lab] = m - tower.get(lab, 0)
        for lab, m in tower.items():
            if lab not in cot:
                excess[lab] = -m
        exdim = sum((2 if ("M" in k) else 1) * v for k, v in excess.items())
        res["results"][f"n={n}"] = {
            "K_samples": K, "Lmax": Lmax, "partial_best_effort": partial,
            "cotangent_dim": cotdim, "Teranishi_Djokovic_traceless_count": DJOKOVIC_TRACELESS[n],
            "matches_published_count": (DJOKOVIC_TRACELESS[n] is not None and cotdim == DJOKOVIC_TRACELESS[n]),
            "brief_formula_3n2_10n_11": 3 * n * n - 10 * n + 11,
            "per_degree": {str(d): s for d, s in spec0.items()},
            "cotangent_multiset": cot, "prime_stable": (bool(stable) if stable is not None else "single-prime"),
            "jacobian_tower": tower, "excess_multiset": excess, "excess_dim": exdim,
            "brief_excess_dim_2(n-2)(n-3)": 2 * (n - 2) * (n - 3),
            "seconds": round(time.time() - t0, 1)}
        print(f"n={n}: cot dim {cotdim} (Teranishi/Djokovic {DJOKOVIC_TRACELESS[n]}, brief said {3*n*n-10*n+11}), "
              f"excess dim {exdim} (brief said {2*(n-2)*(n-3)}), stable {stable}, partial {partial}")
        print(f"     excess: {excess}")
        OUT.write_text(json.dumps(res, indent=2, default=str))
    OUT.write_text(json.dumps(res, indent=2, default=str))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
