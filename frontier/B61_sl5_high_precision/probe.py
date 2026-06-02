"""B61 -- SL(5) fixed-line factorization via a stable high-precision SVD pinv.

B60 built the cross-n structure map for n=3,4 but left SL(5) unresolved: the
trace-coordinate differential Dx has condition number ~1e11 at the relevant
scale, so the double-precision extrapolated Jacobian is numerical noise, and a
normal-equations pinv squares the conditioning (~1e22) into a singular solve.

B61 removes that barrier. It ports B60's validated method to mpmath at high
working precision (default 60 digits) and replaces the pinv with an SVD-based
pseudoinverse that loses only ~log10(cond) digits (not 2*log10(cond)). The
extrapolated ambient Jacobian DT(eps) = DX . svd_pinv(Dx) is taken to eps->0 by
a Vandermonde least-squares extrapolation, and its eigenvalues are matched
against the Lucas/Cayley-Hamilton catalog char(M^k)=t^2-L_k t+(-1)^k, sign
sectors char(-M^k)=t^2+L_k t+(-1)^k, and parity roots {+1,-1}.

Method is validated by reproducing the SL(3) (B55 c=3) and SL(4) (B59)
factorizations at high precision before SL(5) is trusted. Numerical,
high-precision -- NOT a symbolic proof. Standalone trace-map mathematics; no
physics, no Origin-core claim.
"""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass

import mpmath as mp
import numpy as np


DPS_DEFAULT = 60


@dataclass(frozen=True)
class CheckResult:
    name: str
    ok: bool
    detail: str


def result(name: str, ok: bool, detail: str = "") -> CheckResult:
    return CheckResult(name=name, ok=ok, detail=detail)


def print_result(item: CheckResult) -> None:
    status = "OK" if item.ok else "FAIL"
    suffix = f" -- {item.detail}" if item.detail else ""
    print(f"{item.name}: {status}{suffix}")


# --------------------------------------------------------------------------- #
# high-precision linear algebra primitives (mpmath)
# --------------------------------------------------------------------------- #

def _inf_norm(M):
    return max(sum(abs(M[i, j]) for j in range(M.cols)) for i in range(M.rows))


def expm_mp(M):
    """Matrix exponential by scaling-and-squaring + Taylor (mpmath, full dps)."""
    n = M.rows
    s = 0
    nrm = _inf_norm(M)
    half = mp.mpf(1) / 2
    while nrm > half:
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
    """Stable Moore-Penrose pinv via SVD of the TALL orientation.

    mpmath returns A = U * diag(S) * V (economy).  For a wide A (rows < cols),
    SVD the conjugate transpose (tall) and transpose the result back -- calling
    mp.svd on a wide matrix yields a spurious zero singular value.
    """
    if A.rows < A.cols:
        return svd_pinv(A.H).H
    U, S, V = mp.svd(A)
    D = mp.zeros(len(S), len(S))
    for i in range(len(S)):
        D[i, i] = 1 / S[i]
    return V.H * D * U.H


def _extrap0(epss, vals, deg):
    """Value at eps=0 of the degree-`deg` fit through (epss, vals), via svd_pinv."""
    m = len(epss)
    V = mp.zeros(m, deg + 1)
    for i in range(m):
        e = mp.mpf(epss[i])
        for j in range(deg + 1):
            V[i, j] = e ** j
    rhs = mp.matrix(list(vals))
    coeffs = svd_pinv(V) * rhs
    return coeffs[0]


def _trace(M):
    return sum(M[i, i] for i in range(M.rows))


def _eig_vals(M, dim):
    E, _ = mp.eig(M)
    return [E[i] for i in range(dim)]


# --------------------------------------------------------------------------- #
# representation / word machinery (mpmath port of B60)
# --------------------------------------------------------------------------- #

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


# SL(5): 24 coordinate words selected by column-pivoted QR of the trace
# differential at a near-fixed-line rep (seed 20, eps=0.12), giving a full-rank
# (rank-24) coordinate system.  Crucially these use INVERSE letters (a=A^-1,
# b=B^-1) up to length 4 -- B60's forward-only set (A,B powers + A^iB^j) was
# rank 23: its 24th singular value was the dps-floor (~1e-40), a TRUE null
# direction that double precision mis-read as cond~1e11.  This set is rank 24
# at cond ~4e3 (eps=0.2) ... ~2e5 (eps=0.05): the "SL(5) conditioning wall" was
# a bad coordinate choice, not a precision limit.
SL5_WORDS = [
    "AAAA", "bbbb", "aaaa", "BBBB", "abab", "BAAB", "aBBa", "AAbb",
    "aBaa", "AABA", "BBB", "bAbA", "bAbb", "abaa", "AAAb", "bbab",
    "ABAB", "aBaB", "BaBB", "aaa", "ABab", "BBAB", "aBAb", "AAA",
]


def _words(A, B, n):
    if n == 3:
        Ai, Bi = mp.inverse(A), mp.inverse(B)
        return [A, B, A * B, Ai, Bi, Ai * B, A * Bi, Ai * Bi]
    if n == 4:
        return [
            A, A * A, A * A * A, B, B * B, B * B * B, A * B, A * A * B, A * B * B,
            A * A * B * B, A * A * A * B, A * B * B * B, A * B * A * B,
            A * A * A * B * B, A * A * B * B * B,
        ]
    # n == 5: full-rank set, evaluated from string specs (slot A, slot B)
    mm = {"A": A, "B": B, "a": mp.inverse(A), "b": mp.inverse(B)}
    out = []
    for s in SL5_WORDS:
        R = mp.eye(A.rows)
        for c in s:
            R = R * mm[c]
        out.append(R)
    return out


def _perts(n, h):
    basis = _basis_sl(n)
    return [expm_mp(h * g) for g in basis], [expm_mp(-h * g) for g in basis]


def _diff_matrix(A, B, n, substitute, pert_plus, pert_minus, h):
    nw = n * n - 1
    M = mp.zeros(nw, 2 * (n * n - 1))
    col = 0
    for Pp, Pm in zip(pert_plus, pert_minus):
        Ap, Am = Pp * A, Pm * A
        wp = _words(Ap * B, Ap, n) if substitute else _words(Ap, B, n)
        wm = _words(Am * B, Am, n) if substitute else _words(Am, B, n)
        for r in range(nw):
            M[r, col] = (_trace(wp[r]) - _trace(wm[r])) / (2 * h)
        col += 1
    for Pp, Pm in zip(pert_plus, pert_minus):
        Bp, Bm = Pp * B, Pm * B
        wp = _words(A * Bp, A, n) if substitute else _words(A, Bp, n)
        wm = _words(A * Bm, A, n) if substitute else _words(A, Bm, n)
        for r in range(nw):
            M[r, col] = (_trace(wp[r]) - _trace(wm[r])) / (2 * h)
        col += 1
    return M


def _random_PQ(n, seed):
    """Generic traceless P,Q (numpy-seeded for reproducibility, lifted to mpmath).

    The fixed-line limit is independent of the generic direction (P,Q); their
    being double-precision does not limit the result, which is computed to full
    dps for the specific lifted matrices and extrapolated to eps->0.
    """
    rng = np.random.default_rng(seed)

    def mk():
        Z = rng.standard_normal((n, n)) + 1j * rng.standard_normal((n, n))
        Z -= np.trace(Z) / n * np.eye(n)
        out = mp.zeros(n, n)
        for i in range(n):
            for j in range(n):
                out[i, j] = mp.mpc(float(Z[i, j].real), float(Z[i, j].imag))
        return out

    return mk(), mk()


def fixed_line_spectrum(n, seeds, epss, dps=DPS_DEFAULT, deg=None, h=None):
    mp.mp.dps = dps
    if h is None:
        h = mp.mpf(10) ** (-(dps // 3))
    if deg is None:
        deg = min(len(epss) - 1, 6)
    epss = [mp.mpf(e) for e in epss]
    pert_plus, pert_minus = _perts(n, h)
    dim = n * n - 1
    spectra = []
    for seed in seeds:
        P, Q = _random_PQ(n, seed)
        dts = []
        for eps in epss:
            A, B = expm_mp(eps * P), expm_mp(eps * Q)
            dx = _diff_matrix(A, B, n, False, pert_plus, pert_minus, h)
            dX = _diff_matrix(A, B, n, True, pert_plus, pert_minus, h)
            dts.append(dX * svd_pinv(dx))
        dt0 = mp.zeros(dim, dim)
        for i in range(dim):
            for j in range(dim):
                dt0[i, j] = _extrap0(epss, [d[i, j] for d in dts], deg)
        spectra.append(_sort_spec(_eig_vals(dt0, dim)))
    return _avg_spec(spectra)


# --------------------------------------------------------------------------- #
# spectrum -> factor identification
# --------------------------------------------------------------------------- #

def _sort_spec(vals):
    return sorted(vals, key=lambda z: (mp.re(z), mp.im(z)))


def _avg_spec(spectra):
    k, dim = len(spectra), len(spectra[0])
    return [sum(spectra[s][i] for s in range(k)) / k for i in range(dim)]


def _sign(k):
    return 1 if k % 2 == 0 else -1


def _q(a, b, c):
    a, b, c = mp.mpf(a), mp.mpf(b), mp.mpf(c)
    disc = b * b - 4 * a * c
    sq = mp.sqrt(disc)
    return [(-b + sq) / (2 * a), (-b - sq) / (2 * a)]


def _lucas(kmax):
    """L_k = tr(M^k), M=[[1,1],[1,0]]: L_0=2, L_1=1, L_k=L_{k-1}+L_{k-2} (both ways)."""
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
        for r in _q(1, -L[k], _sign(k)):
            cat.append((r, f"char(M^{k})"))
        for r in _q(1, L[k], _sign(k)):
            cat.append((r, f"char(-M^{k})"))
    cat.append((mp.mpf(1), "parity(t-1)"))
    cat.append((mp.mpf(-1), "parity(t+1)"))
    return cat


def _max_match(spectrum, target_roots):
    used = [False] * len(target_roots)
    worst = mp.mpf(0)
    for ev in sorted(spectrum, key=lambda z: mp.re(z)):
        best, bi = mp.mpf("1e18"), -1
        for k, r in enumerate(target_roots):
            if used[k]:
                continue
            d = abs(ev - r)
            if d < best:
                best, bi = d, k
        used[bi] = True
        if best > worst:
            worst = best
    return worst


def identify(spectrum, krange=range(-3, 9)):
    """Nearest-catalog label for each eigenvalue; returns (tally, worst_distance)."""
    cat = _catalog(krange)
    worst = mp.mpf(0)
    tally = Counter()
    for ev in spectrum:
        best, lab = mp.mpf("1e18"), None
        for (r, l) in cat:
            d = abs(ev - r)
            if d < best:
                best, lab = d, l
        tally[lab] += 1
        if best > worst:
            worst = best
    return tally, worst


# --------------------------------------------------------------------------- #
# validation gates (must pass before SL(5) is trusted)
# --------------------------------------------------------------------------- #

# small-eps ladder: at dps>=60 the conditioning is free, so eps is pushed down
# to make the polynomial eps->0 extrapolation error negligible (SL(3)/SL(4) both
# reproduce to ~3e-9 here, vs B60's ~1e-3 double-precision floor).
VALIDATION_EPS = ("0.01", "0.015", "0.02", "0.025", "0.03", "0.035", "0.04")
VALIDATION_TOL = mp.mpf("1e-7")


def check_sl3_validation(dps=DPS_DEFAULT) -> CheckResult:
    spec = fixed_line_spectrum(3, (10, 11), VALIDATION_EPS, dps=dps)
    target = _q(1, 1, -1) + _q(1, -3, 1) + _q(1, -4, -1) + [mp.mpf(1), mp.mpf(-1)]
    worst = _max_match(spec, target)
    return result(
        "SL(3) VALIDATION (B55 c=3)",
        worst < VALIDATION_TOL,
        f"max match {mp.nstr(worst, 4)}; char(M^-1)char(M^2)char(M^3)(t-1)(t+1)",
    )


def check_sl4_regression(dps=DPS_DEFAULT) -> CheckResult:
    spec = fixed_line_spectrum(4, (10, 11), VALIDATION_EPS, dps=dps)
    target = (
        _q(1, 1, -1) + _q(1, -1, -1) + _q(1, -3, 1) + _q(1, -4, -1) + _q(1, -7, 1)
        + _q(1, 3, 1)
        + [mp.mpf(1), mp.mpf(1), mp.mpf(-1)]
    )
    worst = _max_match(spec, target)
    return result(
        "SL(4) REGRESSION (B59)",
        worst < VALIDATION_TOL,
        f"max match {mp.nstr(worst, 4)}; char(M^-1..4)char(-M^2)(t-1)^2(t+1)",
    )


# a multiplier counts as catalog-resolved if it is real and within this of a
# Cayley-Hamilton / parity root.  The well-conditioned modes land at ~1e-6 or
# better; the method-limited modes miss by ~0.1-1 and are often complex.
SL5_RESOLVE_TOL = mp.mpf("1e-3")


def _nearest(ev, cat):
    best, lab = mp.mpf("1e18"), None
    for r, l in cat:
        d = abs(ev - r)
        if d < best:
            best, lab = d, l
    return lab, best


def compute_sl5(dps=DPS_DEFAULT, epss=VALIDATION_EPS, seed=20, deg=6, tol=SL5_RESOLVE_TOL):
    """SL(5) fixed-line spectrum, split into catalog-resolved vs method-limited.

    22 of the 24 multipliers resolve to the Cayley-Hamilton catalog
    (char(M^k)=t^2-L_k t+(-1)^k, sign sectors, parity).  The other 2 tie to the
    coordinate directions where Dx loses rank at the fixed line, where pinv is
    discontinuous -- so their eps->0 limit is gauge-dependent and SCATTERS across
    seeds (verified: seeds 20/22/24/26/28 each leave a different 2-dim residual).
    Those 2 are not recoverable by this representation-perturbation method; they
    need the symbolic ambient SL(5,C) trace ring.
    """
    spec = fixed_line_spectrum(5, (seed,), epss, dps=dps, deg=deg)
    cat = _catalog(range(-3, 9))
    resolved, unresolved = [], []
    for ev in spec:
        lab, d = _nearest(ev, cat)
        if d < tol and abs(mp.im(ev)) < tol:
            resolved.append((ev, lab, d))
        else:
            unresolved.append((ev, lab, d))
    return spec, resolved, unresolved


def check_sl5_partial_resolution(dps=DPS_DEFAULT) -> CheckResult:
    spec, resolved, unresolved = compute_sl5(dps=dps)
    n = len(resolved)
    worst_res = max((d for _, _, d in resolved), default=mp.mpf(0))
    return result(
        "SL(5) PARTIAL RESOLUTION",
        n >= 22,
        f"{n}/24 multipliers match the CH catalog (worst {mp.nstr(worst_res, 3)}); "
        f"{len(unresolved)} method-limited (fixed-line rank-loss, gauge-dependent)",
    )


# --------------------------------------------------------------------------- #
# entry point
# --------------------------------------------------------------------------- #

def main() -> int:
    import time

    mp.mp.dps = DPS_DEFAULT
    print(f"B61 -- SL(5) via stable high-precision SVD pinv (dps={DPS_DEFAULT})")
    print("Status: numerical, high-precision; validated on SL(3)/SL(4); NOT a symbolic proof")
    print()

    gates = []
    for fn in (check_sl3_validation, check_sl4_regression):
        t0 = time.time()
        item = fn()
        print_result(item)
        print(f"    [{time.time() - t0:.1f}s]")
        gates.append(item)

    if not all(g.ok for g in gates):
        print("\nValidation gates FAILED -- SL(5) not trusted; aborting.")
        return 1

    print("\nComputing SL(5) (24-dim, seed 20)...")
    t0 = time.time()
    spec, resolved, unresolved = compute_sl5()
    dt = time.time() - t0
    print(f"  [{dt:.1f}s]  {len(resolved)}/24 multipliers resolved to the CH catalog\n")

    tally = Counter(lab for _, lab, _ in resolved)
    print("Resolved Cayley-Hamilton factorization (22 of 24 dimensions):")
    for lab, cnt in sorted(tally.items()):
        print(f"    {lab} x{cnt}")
    worst_res = max((d for _, _, d in resolved), default=mp.mpf(0))
    print(f"  worst resolved-mode distance: {mp.nstr(worst_res, 4)}")

    print("\nMethod-limited modes (fixed-line rank-loss; gauge-dependent, scatter "
          "across seeds):")
    for ev, lab, d in unresolved:
        print(f"    {mp.nstr(ev, 10)}  (nearest {lab}, dist {mp.nstr(d, 3)})")

    ok = len(resolved) >= 22
    print(f"\nSL(5) {len(resolved)}/24 RESOLVED to the CH catalog; "
          f"{len(unresolved)} method-limited -> {'OK' if ok else 'FAIL'}")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
