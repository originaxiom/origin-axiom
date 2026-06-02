"""B66 -- SL(6) numerical fixed-line tower (35 dimensions).

Extends the inverse-word method (B61, SL(5)) to SL(6): a rank-35 coordinate set
of words in {A,B,A^-1,B^-1} (length <= 5), the mpmath SVD-pinv extrapolation of
the ambient fixed-line Jacobian, and identification of the 35 multipliers against
the Dickson catalog char(M^k)=t^2-L_k t+(-1)^k, sign sectors char(-M^k), parity
(t-1)^a(t+1)^b, with L_k=tr(M^k), M=[[1,1],[1,0]] (Fibonacci, m=1).

Key test: the multiplicity of the odd-k degree-3 factors (char(M^3)/char(-M^3))
-- 3 (the max(n-d,1) formula) or 2 -- which disambiguates the tower multiplicity
formula for all n.  Numerical, high-precision; not a symbolic proof.  Standalone
trace-map mathematics; no physics, no Origin-core claim.
"""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass

import mpmath as mp
import numpy as np

DIM = 35  # n^2 - 1, n = 6

# rank-35 inverse-word coordinate set (QR-pivot at a near-fixed-line rep, seed 20)
SL6_WORDS = [
    "BBBBB", "bbbbb", "AAAAA", "aaaaa", "BBBaa", "aabbb", "AAbbb", "BBAAA",
    "aaaBa", "baaaa", "AAbAA", "BBABB", "bbbb", "baBab", "AAAA", "BBBaB",
    "BABBA", "bAbbA", "baaba", "Abbbb", "BaBaB", "aBAba", "AABab", "aaaa",
    "BAbAB", "abAba", "BBBB", "bbAA", "baBBa", "ABAAb", "bbbab", "bAAbA",
    "BaaBA", "bAbba", "AbbAB",
]


@dataclass(frozen=True)
class CheckResult:
    name: str
    ok: bool
    detail: str


def result(name, ok, detail=""):
    return CheckResult(name, ok, detail)


def print_result(item):
    print(f"{item.name}: {'OK' if item.ok else 'FAIL'}" + (f" -- {item.detail}" if item.detail else ""))


# --------------------------------------------------------------------------- #
# mpmath primitives (as B61)
# --------------------------------------------------------------------------- #

def _inf_norm(M):
    return max(sum(abs(M[i, j]) for j in range(M.cols)) for i in range(M.rows))


def expm_mp(M):
    n = M.rows
    s = 0
    nrm = _inf_norm(M)
    while nrm > mp.mpf(1) / 2:
        nrm /= 2
        s += 1
    Ms = M / (2 ** s)
    acc = mp.eye(n)
    term = mp.eye(n)
    tol = mp.mpf(10) ** (-mp.mp.dps - 5)
    k = 1
    while k < 400:
        term = term * Ms / k
        acc = acc + term
        if _inf_norm(term) < tol:
            break
        k += 1
    for _ in range(s):
        acc = acc * acc
    return acc


def svd_pinv(A):
    if A.rows < A.cols:
        return svd_pinv(A.H).H
    U, S, V = mp.svd(A)
    D = mp.zeros(len(S), len(S))
    for i in range(len(S)):
        D[i, i] = 1 / S[i]
    return V.H * D * U.H


def _trace(M):
    return sum(M[i, i] for i in range(M.rows))


def _eig_vals(M, dim):
    E, _ = mp.eig(M)
    return [E[i] for i in range(dim)]


def _extrap0(epss, vals, deg):
    m = len(epss)
    V = mp.zeros(m, deg + 1)
    for i in range(m):
        e = mp.mpf(epss[i])
        for j in range(deg + 1):
            V[i, j] = e ** j
    coeffs = svd_pinv(V) * mp.matrix(list(vals))
    return coeffs[0]


def _basis_sl(n):
    basis = []
    for i in range(n):
        for j in range(n):
            if i != j:
                e = mp.zeros(n, n)
                e[i, j] = mp.mpf(1)
                basis.append(e)
    for i in range(n - 1):
        e = mp.zeros(n, n)
        e[i, i] = mp.mpf(1)
        e[i + 1, i + 1] = mp.mpf(-1)
        basis.append(e)
    return basis


def _perts(h):
    basis = _basis_sl(6)
    return [expm_mp(h * g) for g in basis], [expm_mp(-h * g) for g in basis]


def _words(A, B):
    mm = {"A": A, "B": B, "a": mp.inverse(A), "b": mp.inverse(B)}
    out = []
    for s in SL6_WORDS:
        R = mp.eye(A.rows)
        for c in s:
            R = R * mm[c]
        out.append(R)
    return out


def _diff_matrix(A, B, substitute, pert_plus, pert_minus, h):
    M = mp.zeros(DIM, 2 * DIM)
    col = 0
    for Pp, Pm in zip(pert_plus, pert_minus):
        Ap, Am = Pp * A, Pm * A
        wp = _words(Ap * B, Ap) if substitute else _words(Ap, B)
        wm = _words(Am * B, Am) if substitute else _words(Am, B)
        for r in range(DIM):
            M[r, col] = (_trace(wp[r]) - _trace(wm[r])) / (2 * h)
        col += 1
    for Pp, Pm in zip(pert_plus, pert_minus):
        Bp, Bm = Pp * B, Pm * B
        wp = _words(A * Bp, A) if substitute else _words(A, Bp)
        wm = _words(A * Bm, A) if substitute else _words(A, Bm)
        for r in range(DIM):
            M[r, col] = (_trace(wp[r]) - _trace(wm[r])) / (2 * h)
        col += 1
    return M


def _random_PQ(seed):
    rng = np.random.default_rng(seed)

    def mk():
        Z = rng.standard_normal((6, 6)) + 1j * rng.standard_normal((6, 6))
        Z -= np.trace(Z) / 6 * np.eye(6)
        out = mp.zeros(6, 6)
        for i in range(6):
            for j in range(6):
                out[i, j] = mp.mpc(float(Z[i, j].real), float(Z[i, j].imag))
        return out

    return mk(), mk()


def fixed_line_spectrum(seed=20, epss=("0.006", "0.009", "0.012", "0.015", "0.018", "0.021", "0.024", "0.027"),
                        dps=60, deg=7):
    mp.mp.dps = dps
    h = mp.mpf(10) ** (-(dps // 3))
    epss = [mp.mpf(e) for e in epss]
    pert_plus, pert_minus = _perts(h)
    P, Q = _random_PQ(seed)
    dts = []
    for eps in epss:
        A, B = expm_mp(eps * P), expm_mp(eps * Q)
        dx = _diff_matrix(A, B, False, pert_plus, pert_minus, h)
        dX = _diff_matrix(A, B, True, pert_plus, pert_minus, h)
        dts.append(dX * svd_pinv(dx))
    dt0 = mp.zeros(DIM, DIM)
    for i in range(DIM):
        for j in range(DIM):
            dt0[i, j] = mp.re(_extrap0(epss, [d[i, j] for d in dts], deg))
    return sorted(_eig_vals(dt0, DIM), key=lambda z: (mp.re(z), mp.im(z)))


# --------------------------------------------------------------------------- #
# Dickson catalog and identification
# --------------------------------------------------------------------------- #

def _q(a, b, c):
    a, b, c = mp.mpf(a), mp.mpf(b), mp.mpf(c)
    disc = mp.sqrt(b * b - 4 * a * c)
    return [(-b + disc) / (2 * a), (-b - disc) / (2 * a)]


def _lucas(kmax):
    L = {0: 2, 1: 1}
    for k in range(2, kmax + 1):
        L[k] = L[k - 1] + L[k - 2]
    for k in range(-1, -kmax - 1, -1):
        L[k] = L[k + 2] - L[k + 1]
    return L


def _catalog(krange):
    L = _lucas(max(abs(k) for k in krange) + 1)
    cat = []
    for k in krange:
        for r in _q(1, -L[k], (-1) ** (k % 2)):
            cat.append((r, f"char(M^{k})"))
        for r in _q(1, L[k], (-1) ** (k % 2)):
            cat.append((r, f"char(-M^{k})"))
    cat.append((mp.mpf(1), "parity(t-1)"))
    cat.append((mp.mpf(-1), "parity(t+1)"))
    return cat


def identify(spectrum, krange=range(-6, 8), tol=mp.mpf("1e-3")):
    cat = _catalog(krange)
    tally = Counter()
    resolved, unresolved = [], []
    for ev in spectrum:
        best, lab = mp.mpf("1e18"), None
        for (r, l) in cat:
            d = abs(ev - r)
            if d < best:
                best, lab = d, l
        if best < tol and abs(mp.im(ev)) < tol:
            tally[lab] += 1
            resolved.append((ev, lab, best))
        else:
            unresolved.append((ev, lab, best))
    return tally, resolved, unresolved


def theta_split(n, h):
    """(dim, theta+1, theta-1) of the opposition involution on the height-h root
    space of A_{n-1} (B62/B64).  Fast pure combinatorics."""
    roots = [(i, j) for i in range(1, n + 1) for j in range(1, n + 1)
             if i != j and abs(i - j) == h]
    theta = lambda r: (n + 1 - r[1], n + 1 - r[0])
    seen = set()
    fixed = tw = 0
    for r in roots:
        if r in seen:
            continue
        tr = theta(r)
        if tr == r:
            fixed += 1
            seen.add(r)
        else:
            tw += 1
            seen.add(r)
            seen.add(tr)
    return len(roots), fixed + tw, tw


def sector_prediction(n=6):
    """(odd-height quads, even-height quads, parity dim) from the theta-split.

    NB: the binning is by ROOT-HEIGHT parity. This equals the char(M^k) |k|-parity
    count only for ODD n; at even n the highest even-|k| factor sits in an
    odd-height space (verified: SL(4) is |k|-parity (3,3) but height (4,2), since
    |k| ranges past the maximal root height). Used here as a dimension/sector
    check; the |k|=3 multiplicity result comes from direct root-matching, not this.
    """
    odd_q = even_q = 0
    for h in range(1, n):
        q = theta_split(n, h)[0] // 2
        if h % 2:
            odd_q += q
        else:
            even_q += q
    return odd_q, even_q, n - 1


def _near_count(spec, root, tol):
    """How many spectrum eigenvalues lie within tol of a real catalog root."""
    return sum(1 for ev in spec if abs(mp.re(ev) - root) < tol and abs(mp.im(ev)) < tol)


def factor_profile(spec, tol=mp.mpf("0.03")):
    """Multiplicity of each char(M^k)/char(-M^k) quadratic by direct root matching
    (avoids the char(-M^k)=char(M^-k) label aliasing). Returns {(k,sign): mult}."""
    L = _lucas(8)
    prof = {}
    for k in range(1, 7):
        for sign, lab in ((+1, f"char(M^{k})"), (-1, f"char(-M^{k})")):
            roots = _q(1, -sign * L[k], (-1) ** (k % 2))
            r0, r1 = float(mp.re(roots[0])), float(mp.re(roots[1]))
            mult = (_near_count(spec, r0, tol) + _near_count(spec, r1, tol)) / 2
            if mult > 0:
                prof[lab] = mult
    # M^{-k} aliases: char(M^-1)=char(-M^1) etc.; count char(M^-1) separately (roots 0.618,-1.618)
    return prof


def main():
    print("B66 -- SL(6) numerical fixed-line tower (35-dim), inverse-word method")
    print("Status: numerical, high-precision; not a symbolic proof")
    print()
    spec = fixed_line_spectrum()
    _, resolved, unresolved = identify(spec, tol=mp.mpf("0.03"))
    print(f"resolved {len(resolved)}/35 multipliers to the Dickson catalog (tol 0.03)\n")
    print("full sorted spectrum (value | nearest catalog | dist):")
    for ev, lab, d in sorted(identify(spec, tol=mp.mpf("1e9"))[1], key=lambda x: mp.re(x[0])):
        print(f"    {mp.nstr(ev, 9):>22}  {lab:>12}  {mp.nstr(d, 3)}")
    print()
    prof = factor_profile(spec)
    print("factor multiplicity profile (by direct root matching):")
    for lab in sorted(prof, key=lambda s: (("-" in s), s)):
        print(f"    {lab}: x{prof[lab]}")
    print("\nlikely-gauge modes (large imaginary part):")
    for ev in spec:
        if abs(mp.im(ev)) > mp.mpf("0.03"):
            print(f"    {mp.nstr(ev, 8)}")
    # KEY TEST: |k|=3 multiplicity = char(M^3) {4.236,-0.236} + char(-M^3) {-4.236,0.236}
    big, small = float(2 + mp.sqrt(5)), float(2 - mp.sqrt(5))  # 4.236, -0.236
    m3 = (_near_count(spec, big, mp.mpf("0.05")) + _near_count(spec, small, mp.mpf("0.05"))
          + _near_count(spec, -big, mp.mpf("0.05")) + _near_count(spec, -small, mp.mpf("0.05"))) / 2
    print(f"\nKEY TEST -- |k|=3 multiplicity (char(M^3)+char(-M^3), roots +-4.236, -+0.236): {m3}")
    print("  max(n-d,1) with n=6,d=3 predicts 3; alternative 2.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
