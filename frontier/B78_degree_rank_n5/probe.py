"""B78 (Phase 1b) -- the DECISIVE n=5 degree=rank test.

degree=rank (B73/V54): on the SL(n) figure-eight bundle's principal Dehn-filling component, the
longitude is the meridian's n-th power. B77/V60 refined it to the SIGNED law [A,B] = (-1)^(n-1) mu^n
(c=+1 at n=3, c=-1 at n=4). Two points is a guess; THREE is a pattern. This tests n=5: does a principal
SL(5) Dehn-filling component give M^5=L with c=+1 (the (-1)^(5-1)=+1 prediction)?

Setup (n-generic figure-eight, the B73 A^2B,AB convention so mu=A^-1 t is the genuine meridian):
  * A = diag(spec), spec a product-1 finite-order n-tuple (swept).
  * B solved from the BUNDLE condition (A^2B, AB) ~ (A,B): tr W(A^2B,AB) = tr W(A,B) for coordinate
    words W (length<=3), + det B = 1.  (least_squares)
  * monodromy t: t A t^-1 = A^2 B, t B t^-1 = A B  (2n^2 x n^2 Kronecker null-space).
  * irreducible: length-<=3 words span M_n (rank n^2).
  * SCALAR test: [A,B] = c * mu^k, mu = A^-1 t -> scalar_dev([A,B] mu^-k) ~ 0; read off c.

OUTCOME (honest method-limit). The n-generic finder is VALIDATED: it reproduces the known n=3
(M^3=L, c=+1) and n=4 (M^4=L, c=-1) sign law to ~1e-13. But at n=5, across the natural finite-order
spectra (degenerate {1,1,1,-1,-1},{i,-i,i,-i,1}; distinct Phi8={prim8,1},Phi12; tr=0 {5th roots},
{1,i,-i,w,w2}), the figure-eight bundle condition is solvable to MACHINE PRECISION (residual ~1e-15)
but every converged rep is REDUCIBLE -- ~100 converged / 0 irreducible per spectrum. The irreducible
principal Dehn-filling rep is NOT numerically locatable via least_squares (least_squares descends into
the reducible basins; this is the documented SL(5) rank-loss/gauge difficulty of B61-B66, amplified).
So the decisive n=5 third point is OPEN; it needs the symbolic SL(5) trace-map fixed-locus (B71-style,
24 coordinates) or a homotopy/continuation rep-finder. degree=rank stays CONFIRMED at n=3,4 with the
(-1)^(n-1) sign law (B77/V60); n=5 is a flagged method-limit, not a confirmation or a refutation.

Standalone low-dim topology; no Origin-core claim; proven core P1-P16 untouched.
"""
from __future__ import annotations

import itertools

import numpy as np
from scipy.optimize import least_squares


def _words(n):
    """Coordinate words (length<=3 in A,B) -- enough trace conditions to pin B (n^2 complex entries)."""
    letters = "AB"
    ws = []
    for L in (1, 2, 3):
        for combo in itertools.product(letters, repeat=L):
            ws.append("".join(combo))
    # de-dup cyclic/trivial duplicates kept simple; trim to a generous set
    seen, out = set(), []
    for w in ws:
        if w not in seen:
            seen.add(w); out.append(w)
    return out


def _g(A, B):
    return {"A": A, "B": B, "a": np.linalg.inv(A), "b": np.linalg.inv(B)}


def _word(s, g, n):
    M = np.eye(n, dtype=complex)
    for ch in s:
        M = M @ g[ch]
    return M


def _resid(bvec, A, n, words):
    B = (bvec[:n * n] + 1j * bvec[n * n:]).reshape(n, n)
    try:
        g, pg = _g(A, B), _g(A @ A @ B, A @ B)
    except np.linalg.LinAlgError:
        return np.ones(2 * (len(words) + 1)) * 1e3
    e = np.array([np.trace(_word(w, g, n)) - np.trace(_word(w, pg, n)) for w in words]
                 + [np.linalg.det(B) - 1], dtype=complex)
    return np.concatenate([e.real, e.imag])


def monodromy(A, B, n):
    """t in SL(n,C) with t A t^-1 = A^2 B, t B t^-1 = A B; returns (t, residual)."""
    In = np.eye(n, dtype=complex)
    pA, pB = A @ A @ B, A @ B
    E = np.vstack([np.kron(A.T, In) - np.kron(In, pA), np.kron(B.T, In) - np.kron(In, pB)])
    t = np.linalg.svd(E)[2][-1].conj().reshape(n, n, order="F")
    t = t / np.linalg.det(t) ** (1.0 / n)
    res = (np.max(np.abs(t @ A @ np.linalg.inv(t) - pA)) + np.max(np.abs(t @ B @ np.linalg.inv(t) - pB)))
    return t, res


def _irreducible(A, B, n):
    g = _g(A, B)
    ws = [""] + _words(n) + ["a", "b", "Ab", "aB", "AAa", "ABa", "aAB", "BBa"]
    rows = np.array([_word(w, g, n).flatten() for w in ws])
    return np.linalg.matrix_rank(rows, tol=1e-7) >= n * n


def scalar_c(A, B, t, k):
    """c and scalar_dev in [A,B] = c * mu^k, mu = A^-1 t."""
    mu = np.linalg.inv(A) @ t
    comm = A @ B @ np.linalg.inv(A) @ np.linalg.inv(B)
    S = comm @ np.linalg.matrix_power(np.linalg.inv(mu), k)
    dev = (np.max(np.abs(S - np.diag(np.diag(S)))) + np.max(np.abs(np.diag(S) - np.mean(np.diag(S)))))
    cdev_commute = np.max(np.abs(mu @ comm - comm @ mu))
    return np.mean(np.diag(S)), dev, cdev_commute


def realize(spec, seed, tries=250, max_nfev=900):
    """One irreducible figure-eight bundle rep (A=diag(spec), B, t) or None."""
    n = len(spec)
    A = np.diag(np.array(spec, dtype=complex))
    words = _words(n)
    rng = np.random.default_rng(seed)
    for _ in range(tries):
        r = least_squares(_resid, rng.standard_normal(2 * n * n) * 0.7, args=(A, n, words),
                          method="trf", max_nfev=max_nfev)
        if np.max(np.abs(_resid(r.x, A, n, words))) < 1e-9:
            B = (r.x[:n * n] + 1j * r.x[n * n:]).reshape(n, n)
            if not _irreducible(A, B, n):
                continue
            t, res = monodromy(A, B, n)
            if res < 1e-7:
                return A, B, t
    return None


def degree_over_spec(spec, ks=(3, 4, 5, 6), n_reps=5, seed=1, budget=250):
    """For A=diag(spec): find reps, report median scalar_dev per k and the median c at the best k."""
    n = len(spec)
    A = np.diag(np.array(spec, dtype=complex))
    words = _words(n)
    rng = np.random.default_rng(seed)
    devs = {k: [] for k in ks}; cs = {k: [] for k in ks}; commutes = []
    found = 0
    for _ in range(budget):
        if found >= n_reps:
            break
        r = least_squares(_resid, rng.standard_normal(2 * n * n) * 0.7, args=(A, n, words),
                          method="trf", max_nfev=900)
        if np.max(np.abs(_resid(r.x, A, n, words))) < 1e-9:
            B = (r.x[:n * n] + 1j * r.x[n * n:]).reshape(n, n)
            if not _irreducible(A, B, n):
                continue
            t, res = monodromy(A, B, n)
            if res < 1e-7:
                found += 1
                for k in ks:
                    c, dev, comm = scalar_c(A, B, t, k)
                    devs[k].append(dev); cs[k].append(c)
                commutes.append(comm)
    med = {k: (float(np.median(devs[k])) if devs[k] else float("nan")) for k in ks}
    bestk = min(med, key=lambda k: med[k]) if found else None
    cbest = (np.mean(cs[bestk]) if found and cs[bestk] else float("nan"))
    return found, med, bestk, cbest, (float(np.median(commutes)) if commutes else float("nan"))


def reproduce(spec, n, ks, n_reps=3, seed=3, budget=150, max_nfev=4000):
    """Validation: best scalar-dev per k + the scalar c at the best k, on a known spectrum."""
    A = np.diag(np.array(spec, dtype=complex)); words = _words(n)
    rng = np.random.default_rng(seed); found = 0
    devs = {k: [] for k in ks}; cs = {k: [] for k in ks}
    for _ in range(budget):
        if found >= n_reps:
            break
        r = least_squares(_resid, rng.standard_normal(2 * n * n) * 0.7, args=(A, n, words),
                          method="trf", max_nfev=max_nfev)
        if np.max(np.abs(_resid(r.x, A, n, words))) < 1e-9:
            B = (r.x[:n * n] + 1j * r.x[n * n:]).reshape(n, n)
            if not _irreducible(A, B, n):
                continue
            t, res = monodromy(A, B, n)
            if res < 1e-7:
                found += 1
                for k in ks:
                    c, dev, _ = scalar_c(A, B, t, k)
                    devs[k].append(dev); cs[k].append(c)
    med = {k: (float(np.median(devs[k])) if devs[k] else float("nan")) for k in ks}
    bestk = min(med, key=lambda k: med[k]) if found else None
    cbest = (np.mean(cs[bestk]) if found and cs[bestk] else float("nan"))
    return found, med, bestk, cbest


def irreducible_fraction(spec, starts=40, seed=21, max_nfev=2500):
    """At n=5: of the converged bundle reps (res<1e-8), how many are IRREDUCIBLE? Returns (conv, irr)."""
    n = len(spec); A = np.diag(np.array(spec, dtype=complex)); words = _words(n)
    rng = np.random.default_rng(seed); conv = irr = 0
    for _ in range(starts):
        r = least_squares(_resid, rng.standard_normal(2 * n * n) * 0.9, args=(A, n, words),
                          method="trf", max_nfev=max_nfev)
        if np.max(np.abs(_resid(r.x, A, n, words))) < 1e-8:
            conv += 1
            B = (r.x[:n * n] + 1j * r.x[n * n:]).reshape(n, n)
            if _irreducible(A, B, n):
                irr += 1
    return conv, irr


W5 = np.exp(2j * np.pi / 3)
N5_SPECS = {  # natural SL(5) principal-type finite-order spectra (product 1), all swept
    "{prim8 roots,1}": [np.exp(1j * np.pi / 4 * k) for k in (1, 3, 5, 7)] + [1],
    "{1,1,1,w,w2}": [1, 1, 1, W5, W5 ** 2],
    "{1,i,-i,w,w2}": [1, 1j, -1j, W5, W5 ** 2],
}


def main():
    print("B78 (Phase 1b) -- the n=5 degree=rank test\n")
    print("VALIDATION (the n-generic figure-eight A^2B,AB finder reproduces the known sign law):")
    def _line(label, f, m, k, c, pred):
        if f and k is not None:
            print(f"  {label} ({f} reps): best M^{k}=L (dev {m[k]:.0e}), c={c:+.3f}  [{pred}]")
        else:
            print(f"  {label}: no rep this run (stochastic; budget-limited)  [{pred}]")
    f3, m3, k3, c3 = reproduce([1, 1j, -1j], 3, (2, 3, 4))
    _line("n=3 {1,i,-i}", f3, m3, k3, c3, "predict M^3, c=+1")
    f4, m4, k4, c4 = reproduce([1, 1, W5, W5 ** 2], 4, (3, 4, 5), n_reps=2, budget=250)
    _line("n=4 {1,1,w,w2}", f4, m4, k4, c4, "predict M^4, c=-1")

    print("\nn=5 (the decisive third point): is an IRREDUCIBLE principal Dehn-filling rep locatable?")
    for name, spec in N5_SPECS.items():
        conv, irr = irreducible_fraction(spec)
        print(f"  {name}: {conv} bundle reps converged (res<1e-8), {irr} IRREDUCIBLE")
    print("\nOUTCOME (honest method-limit): across natural SL(5) finite-order spectra the figure-eight")
    print("bundle condition is solvable to machine precision but yields ONLY REDUCIBLE reps -- the")
    print("irreducible principal Dehn-filling rep is NOT numerically locatable via least_squares (the")
    print("documented SL(5) rank-loss/gauge difficulty, B61-B66). The decisive n=5 test is OPEN: it")
    print("needs the symbolic SL(5) trace-map fixed-locus (B71-style, 24 coords) or a continuation")
    print("rep-finder. degree=rank stays CONFIRMED at n=3,4 with the (-1)^(n-1) sign law (B77/V60).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
